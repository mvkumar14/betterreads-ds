"""Entry point for our twitoff flask app"""

from .app import create_app
# NOTE  that when you deploy you have to get rid of the relative
# references so from app instead of from .app

application = create_app()


if __name__ == '__main__':
    application.run(debug=True)
