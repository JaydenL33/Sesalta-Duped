from flask import Flask
from routes import app

application = app
if __name__ == "__main__":
    application.run()
