

from Adyen.util import is_valid_hmac_notification
from flask import Flask, render_template, send_from_directory, request, abort

from adyen_test import adyen_sessions

def create_app():
    app = Flask('app')

    # Register 404 handler
    # app.register_error_handler(404, page_not_found)

    # Routes:
    @app.route('/')
    def home():
        return render_template('index.html')

  
    return app


if __name__ == '__main__':
    web_app = create_app()
    web_app.run()