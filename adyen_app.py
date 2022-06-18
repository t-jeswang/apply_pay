

from unittest import result
from Adyen.util import is_valid_hmac_notification
from flask import Flask, render_template, send_from_directory, request, abort
from flask_cors import CORS
from adyen_test import *

def create_app():
    app = Flask('app')
    CORS(app)
    # Register 404 handler
    # app.register_error_handler(404, page_not_found)

    # Routes:
    @app.route('/')
    def home():
        return render_template('cart.html')
    @app.route('/cart')
    def cart():
        return render_template('cart.html')
    @app.route('/checkout')
    def checkout():
        return render_template('index.html')

    @app.route('/payment/<integration>')
    
    def payment(integration):

        
        return render_template('payment_process.html', method=integration, client_key=get_adyen_client_key())
        
    @app.route('/api/sessions', methods=['POST'])
    def sessions():

        host_url = request.host_url 
        response= adyen_sessions(host_url)
      
          
        return response
       
    # @app.route('/payment_process')
    # # def apple_pay():    # change here
    # #     applePayConfiguration = { "amount": { "value": 10,
    # #         "currency": "USD"
    # #     },
    # #     "countryCode": "US"
    # #     }
    

    @app.route('/redirect', methods=['POST', 'GET'])
    def redirect():

        return render_template('payment_process.html', method=None, client_key=get_adyen_client_key())

    #     return render_template('apple_pay_form.html')
    # @app.route('/api/sessions', methods=['POST'])
  
    @app.route('/result/failed', methods=['GET'])
    def checkout_failure():
        return render_template('payment_fail.html')

    @app.route('/result/pending', methods=['GET'])
    def checkout_pending():
        return render_template('payment_fail.html')

    @app.route('/result/error', methods=['GET'])
    def checkout_error():
        return render_template('payment_fail.html')

     

    return app


if __name__ == '__main__':
    web_app = create_app()
    web_app.run(debug=True, port=get_port(), host='0.0.0.0')