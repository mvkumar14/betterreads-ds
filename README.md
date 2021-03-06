## Readrr Labs 21
Main Site: https://www.readrr.app/

DS API: readrr-heroku-test.herokuapp.com/
View Docs for endpoint: https://documenter.getpostman.com/view/10879384/SzYXXz7Z?version=latest

## DS TEAM


|                                              [Claudia Chajon](https://github.com/claudiasofiac)                                               |                                          [Enrique Collado](https://github.com/fwechino)                                          |                                              [Dylan Nason](https://github.com/DNason1999)                                              |                                             [Kumar Veeravel](https://github.com/mvkumar14)                                             |
| :----------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------: |
|         [<img src="https://avatars1.githubusercontent.com/u/53544970?s=460&v=4" width = "200" />](https://github.com/claudiasofiac)         |    [<img src="https://avatars2.githubusercontent.com/u/7489370?s=460&v=4" width = "200" />](https://github.com/fwenchino)     |        [<img src="https://ca.slack-edge.com/T4JUEB3ME-UNK2RLD3P-2d36559d35c0-512" width = "200" />](https://github.com/DNason1999)         |       [<img src="https://avatars0.githubusercontent.com/u/45538556?s=460&v=4" width = "200" />](https://github.com/mvkumar14)       |
|                         [<img src="https://github.com/favicon.ico" width="15">](https://github.com/claudiasofiac)                          |                      [<img src="https://github.com/favicon.ico" width="15">](https://github.com/fwenchino)                      |                         [<img src="https://github.com/favicon.ico" width="15">](https://github.com/DNason1999)                          |                        [<img src="https://github.com/favicon.ico" width="15">](https://github.com/mvkumar14)                        |
| [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](https://www.linkedin.com/in/claudia-chajon-129ab8197/) | [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](https://www.linkedin.com/in/enrique-collado-fernández-b649504b/) | [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](https://www.linkedin.com/in/dylan-nason-768001171/) | [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](https://www.linkedin.com/in/kumar-veeravel-b8a70a4a/) |





TECH STACK IMAGES (___)

![MIT](https://img.shields.io/packagist/l/doctrine/orm.svg)
![Typescript](https://img.shields.io/npm/types/typescript.svg?style=flat)
[![Netlify Status](https://api.netlify.com/api/v1/badges/b5c4db1c-b10d-42c3-b157-3746edd9e81d/deploy-status)](netlify link goes in these parenthesis)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

🚫 more info on using badges [here](https://github.com/badges/shields)

## Project Overview

 [Deployed Front End](https://www.readrr.app/)

 [Trello Board](https://trello.com/b/pfNUGgG3/betterreads)

 [Product Canvas](https://www.notion.so/betterReads-66b5ba5a4c7e4036ab786e10b8c2de4d)

The aim of this project is to provide a clean, uncluttered user interface that allows a user to track books similar to how GoodReads allows you to track books. More details can be found in the [product vision document](https://www.notion.so/Vision-Problem-Objectives-bb24ca087420443e8503115552bf4b25) (PVD accessible only to team members)

The core DS role on this project is to provide recommendations. If there are other DS utilties that you would like to add, talk to the Web, and UI teams, and figure out what the feature is going to look like (from a UI standpoint) and what data you need to send back and forth in order to impliment the feature.


### Tech Stack

Experiments are run locally in jupyter notebooks, and uploaded to branches of the repo. The API is currently being hosted on heroku, with data being hosted in an AWS RDS database. See [issue #8](https://github.com/Lambda-School-Labs/betterreads-ds/issues/8) for details on why we switched to heroku from an AWS elastic beanstalk instance. 

### Predictions

 The core recommendation model is based off of a list of the top 10,000 books from goodreads. The data is sourced from [here](https://github.com/zygmuntz/goodbooks-10k). In the future this data will (hopefully) be augmented by OpenLibrary Data, and Google API data. 
 
 Recommendation models seem to nearly always come down to some implimentation of the nearest neighbors model. The key is to find a proper embedding such that the nearest neighbors model returns good results. The current model is a K-nearest-neighbors model using user rating profiles. For more information about the model see the [recommendations](https://github.com/Lambda-School-Labs/betterreads-ds/tree/Recommendations) branch.


### Explanatory Variables
 Currently the only explanitory variable in the recommendations data is user ratings. 
-   Explanatory Variable 1
-   Explanatory Variable 2
-   Explanatory Variable 3
-   Explanatory Variable 4
-   Explanatory Variable 5

### Data Sources
  Add to or delete souce links as needed for your project


-   [Source 1] (🚫add link to python notebook here)
-   [Source 2] (🚫add link to python notebook here)
-   [Source 3] (🚫add link to python notebook here)
-   [Source 4] (🚫add link to python notebook here)
-   [Source 5] (🚫add link to python notebook here)

### Python Notebooks

  Add to or delete python notebook links as needed for your project

[Python Notebook 1](🚫add link to python notebook here)

[Python Notebook 2](🚫add link to python notebook here)

[Python Notebook 3](🚫add link to python notebook here)

### How to connect to the web API

Details on how to connect to the Web API are located at the top of [this](https://www.notion.so/Architecture-Details-21cb8620660946b68e16762429d778c5) document. 

### How to connect to the data API

API Documentation can be found here: https://documenter.getpostman.com/view/10879384/SzYXXz7Z?version=latest

The account used for the postman collection is the betterreadslabs21@gmail.com account (Sign in using google). Ask the TL or SL for login credentials.

There are currently two endpoints. One serves two types of search results (Depending on POSTed parameters) and the other serves recommendations. Currently the recommendations endpoint serves hardcoded recommendations. The code to serve recommendations is commented out in the application.py file [see here](https://github.com/Lambda-School-Labs/betterreads-ds/blob/heroku_deployment/application.py). Some of the issues regarding getting the recommendations endpoint are documented in [issue #8](https://github.com/Lambda-School-Labs/betterreads-ds/issues/8)

Here is an example of the formatting for an individual book in the response:
```
{
            "authors": ["Frank Herbert"],
            "averageRating": 4.5,
            "categories": ["Fiction"],
            "description": "Follows the adventures of Paul Atreides, the son of a betrayed duke given up for dead on a treacherous desert                 planet and adopted by its fierce, nomadic people, who help him unravel his most unexpected destiny.",
            "googleId": "B1hSG45JCX4C",
            "isEbook": false,
            "isbn10": "0441013597",
            "isbn13": "9780441013593",
            "language": "en",
            "pageCount": 528,
            "publishedDate": "2005",
            "publisher": "Penguin",
            "smallThumbnail": "http://books.google.com/books/content?id=B1hSG45JCX4C&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
            "textSnippet": "Follows the adventures of Paul Atreides, the son of a betrayed duke given up for dead on a treacherous desert planet and adopted by its fierce, nomadic people, who help him unravel his most unexpected destiny.",
            "thumbnail": "http://books.google.com/books/content?id=B1hSG45JCX4C&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
            "title": "Dune",
            "webReaderLink": "http://play.google.com/books/reader?id=B1hSG45JCX4C&hl=&printsec=frontcover&source=gbs_api"
        }
```
## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Please note we have a [code of conduct](./code_of_conduct.md.md). Please follow it in all your interactions with the project.

### Issue/Bug Request

 **If you are having an issue with the existing project code, please submit a bug report under the following guidelines:**
 - Check first to see if your issue has already been reported.
 - Check to see if the issue has recently been fixed by attempting to reproduce the issue using the latest master branch in the repository.
 - Create a live example of the problem.
 - Submit a detailed bug report including your environment & browser, steps to reproduce the issue, actual and expected outcomes,  where you believe the issue is originating from, and any potential solutions you have considered.

### Feature Requests

We would love to hear from you about new features which would improve this app and further the aims of our project. Please provide as much detail and information as possible to show us why you think your new feature should be implemented.

### Pull Requests

If you have developed a patch, bug fix, or new feature that would improve this app, please submit a pull request. It is best to communicate your ideas with the developers first before investing a great deal of time into a pull request to ensure that it will mesh smoothly with the project.

Remember that this project is licensed under the MIT license, and by submitting a pull request, you agree that your work will be, too.

#### Pull Request Guidelines

- Ensure any install or build dependencies are removed before the end of the layer when doing a build.
- Update the README.md with details of changes to the interface, including new plist variables, exposed ports, useful file locations and container parameters.
- Ensure that your code conforms to our existing code conventions and test coverage.
- Include the relevant issue number, if applicable.
- You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

### Attribution

These contribution guidelines have been adapted from [this good-Contributing.md-template](https://gist.github.com/PurpleBooth/b24679402957c63ec426).

## Documentation

See [Backend Documentation](_link to your backend readme here_) for details on the backend of our project.

See [Front End Documentation](_link to your front end readme here_) for details on the front end of our project.
