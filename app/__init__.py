from flask import Flask
from config import Config

# Create Flask app instance
app = Flask(__name__, template_folder="templates/index.html")

# Load configuration
app.config.from_object(Config)

# Import routes to avoid circular imports
# from app import routes