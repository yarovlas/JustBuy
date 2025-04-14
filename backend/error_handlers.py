from flask import render_template, request
import logging

logger = logging.getLogger(__name__)

def register_error_handlers(app):
    # Error handler for 404 errors
    @app.errorhandler(404)
    def page_not_found(e):
        logger.error(f"Page not found: {request.url}")
        return render_template("404.html"), 404

    # Error handler for 500 errors
    @app.errorhandler(500)
    def internal_server_error(e):
        logger.error(f"Internal server error: {request.url}")
        return render_template("500.html"), 500
