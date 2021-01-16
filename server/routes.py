from flask import Flask
from User import user_db
from User import user_routes
from SerialRegister import serial_routes
from ItemRegister import item_routes
from flask_cors import CORS
from KCAD import kcad_routes
from OrderRegister import order_routes
from ReceivedRegister import received_routes
from PreInvoice import preinv_routes
from DrillPipe import dp_routes
from Delivery import delivery_routes
from HeavyWeight import hw_routes
from DrillCollar import dc_routes
from OCTG import octg_routes
import logging
import sys;


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

if (str(sys.version)[0] == '3'):
	from http.server import BaseHTTPRequestHandler, HTTPServer


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        #self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        #self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        #logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n", str(self.path), str(self.headers), post_data.decode('utf-8'))
        logging.info(post_data.decode('utf-8'))

        self._set_response()
        #self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')






# two decorators, same function
@app.route('/')
def test():
    return 'OCEAN IMR API'

app.register_blueprint(user_routes.user)
app.register_blueprint(serial_routes.serial)
app.register_blueprint(kcad_routes.kcad)
app.register_blueprint(item_routes.item)
app.register_blueprint(order_routes.order)
app.register_blueprint(received_routes.received)
app.register_blueprint(preinv_routes.preinv)
app.register_blueprint(dp_routes.dp)
app.register_blueprint(delivery_routes.delivery)
app.register_blueprint(hw_routes.hw)
app.register_blueprint(dc_routes.dc)
app.register_blueprint(octg_routes.octg)



if __name__ == '__main__':
    app.run(debug=True)

