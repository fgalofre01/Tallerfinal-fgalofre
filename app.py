from flask import Flask
from views.guarderia_controller import principal_routes

app = Flask(__name__)

principal_routes(app)


if __name__ == "__main__":
    app.run(debug=True)