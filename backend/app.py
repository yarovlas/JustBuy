from flask import Flask
from __init__ import create_app
from routes import register_routes
from error_handlers import register_error_handlers

# Initialize the Flask application
app = create_app()

# Register routes and error handlers
register_routes(app)
register_error_handlers(app)

# Run the application
if __name__ == '__main__':
    app.run(debug=True, port='3000')