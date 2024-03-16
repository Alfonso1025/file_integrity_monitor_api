from flask import Flask
from hash.HashRoutes import hash_routes
# Create Flask app
app = Flask(__name__)

app.register_blueprint(hash_routes)

# Define a route
@app.route('/')
def hello():
    return 'Hello, World!'


# Run the app
if __name__ == '__main__':
    app.run(debug=True)


