from flask import Flask
from flask_cors import CORS
from database import init_db
from routes import api_blueprint

app = Flask(__name__)
CORS(app)

# Initialize DB
init_db(app)

# Register API routes
app.register_blueprint(api_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
