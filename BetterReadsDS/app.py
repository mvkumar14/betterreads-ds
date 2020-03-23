# Inbuild Modules
import os
import json
import pickle

# Third Party Modules
import requests
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
# import numpy as np
# import pandas as pd
from sklearn.neighbors import NearestNeighbors
# from scipy.sparse import csr_matrix
# from decouple import config #<-- not sure what this does yet

# Custom Modules
from .google_books_hf import process_list

# Retreive Google API key from environment

# Loading in model
with open('test.obj','rb') as f:
    knn_deserial = pickle.load(f)
with open('user_matrix.obj','rb') as f:
    user_matrix = pickle.load(f)

print(type(user_matrix))

# Defining function to return model values
def get_recommendations(book_title, matrix=user_matrix, model=knn_deserial, topn=10):
    book_index = list(matrix.index).index(book_title)
    distances, indices = model.kneighbors(matrix.iloc[book_index,:].values.reshape(1,-1), n_neighbors=topn+1)
    print('Recommendations for {}:'.format(matrix.index[book_index]))
    output_list = []
    for i in range(1, len(distances.flatten())):
        output_list.append('{}. {}, distance = {}'.format(i, matrix.index[indices.flatten()[i]], "%.3f"%distances.flatten()[i]))

def create_app():
    app = Flask(__name__)
    CORS(app,supports_credentials=True)
    # Whenever we output a list of books the json format of the
    # list should be the same. Lets call this format
    # OUT_LIST format for now. This format is what the Web team is
    # currently using to render book list results.


    @app.route('/')
    # some details about the api and some references
    # to api documentation
    def root():
        return render_template('base.html',page_name='home')

    @app.route('/test',methods=['POST'])
    def test():
        print('test')
        test_val = request.get_json(force=True)
        print(test_val)
        return "3"

    @app.route('/search', methods=['GET','POST'])
    def search():
        # variables used throughout the function
        GOOGLE_KEY = os.environ['GOOGLE_KEY']
        relevant_details=['id','title','authors','publisher',
                  'publishedDate','description','industryIdentifiers',
                  'pageCount','categories','thumbnail','smallThumbnail',
                  'language','webReaderLink','textSnippet','isEbook']

        # Retreive the information from the POST request body

        # try:
        #     input_data = request.get_json()
        # except:
        #     print("that didn't work")
        # print(input_data)

        input_data = request.get_json(force=True)

        # Try to access keys from the post request
        try:
            if input_data['type'] == 'googleId':
                search_id = input_data['query']
                response = requests.get('https://www.googleapis.com/books/v1/volumes/'
                                        + search_id
                                        + '?key='
                                        + GOOGLE_KEY)
                # If invalid google id, then display/return an error message
                result = json.loads(response.text)
                output = process_list([result],relevant_details)
                return jsonify(output)

            elif input_data['type'] == 'search':
                search_term = input_data['query']
                response = requests.get('https://www.googleapis.com/books/v1/volumes?q='
                    + search_term
                    + '&key='
                    + GOOGLE_KEY)
                result = json.loads(response.text)
                output = process_list(result['items'],relevant_details)
                return jsonify(output)
            else:
                message = """ The value for the 'type' key was invalid.
                 Please change the value to 'googleId', or 'search' """
                return render_template('echo.html',page_name='error',
                                        echo=message)

        # If you can't access keys from the post request display error message
        except KeyError:
            message = """ The key wasn't in the request body"""
            return render_template('echo.html',page_name='error', echo=message)

        return render_template('echo.html',page_name='search')

    @app.route('/subject_list')
    # input will be subject heading (this should be a valid value)
    # We need to give BE/FE a list of valid subject headings
    # output is going to be a list of books in the OUT_LIST format
    def subjects():
        return render_template('base.html',page_name='subjects')


    @app.route('/recommendations',methods = ['POST'])
    # Input is possibly a user id
    # we need to access and search the user's data for a book that they might
    # want recommendations for
    # Change the model to return isbns instead of book titles
    # Take list of isbns and search GAPI for Books
    # Return values in proper output format
    def recommendations():
        input_data = request.get_json(force=True)
        book_title = input_data['title']
        # if book_title in valid_titles:
        reccs = get_recommendations(book_title)
        out_string = " ".join(reccs)
        return render_template('echo.html',page_name='Recommendations',
                                echo=out_string)

        # else:
        #     # The file should be where your pipenv pipfile is located
        #     with open('hardcode_reccs.json','r',encoding='utf8') as f:
        #         output = json.load(f)
        #     return jsonify(output)


    return app

if __name__=="__main__":
    print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))
