from flask import Flask

app = Flask(__name__)

# Set default configuration if not already set
app.config.setdefault("ENV", "development")  # You can change this to "production" or other as needed

# Load configurations based on the ENV value
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

from app import views

