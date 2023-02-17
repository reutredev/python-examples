import logging.config
import os
from optparse import OptionParser
import cherrypy
from server_example.server_app import server_app

logger = logging.getLogger(__name__)

def run_server(ip, port):
    logger.info("Starting Server ....")
    logger.info("Listening on " + ip + ":" + str(port))

    # Mount the application
    cherrypy.tree.graft(server_app, "/")

    # Unsubscribe the default server
    cherrypy.server.unsubscribe()

    # Instantiate a new server object
    server = cherrypy._cpserver.Server()

    # Configure the server object
    server.socket_host = ip  # "0.0.0.0"
    server.socket_port = port  # 8080
    server.thread_pool = 30
    #server.thread_pool_max = 30

    # server.accepted_queue_size = 3
    # server.socket_queue_size = 3
    # server.queue_size = 3

    # For SSL Support
    # server.ssl_module            = 'pyopenssl'
    # server.ssl_certificate       = 'ssl/certificate.crt'
    # server.ssl_private_key       = 'ssl/private.key'
    # server.ssl_certificate_chain = 'ssl/bundle.crt'

    # configs we should be aware of
    # default is 60
    # cherrypy.engine.timeout_monitor.frequency

    # default is 300
    # cherrypy.response.timeout

    # default is 100MB, 0 removes the limit
    # cherrypy.server.max_request_body_size
    # server.max_request_body_size = video_max_file_size

    # Default is 10 seconds
    # cherrypy.server.socket_timeout

    # Subscribe this server
    server.subscribe()

    try:
        # Start the server engine (Option 1 *and* 2)
        cherrypy.engine.signals.subscribe()
        cherrypy.engine.start()
        cherrypy.engine.block()
    except KeyboardInterrupt:
        logger.error("got KeyboardInterrupt stopping cherrypy engine")
        cherrypy.engine.exit()

def setup_logging():
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    if not os.path.exists("Logs"):
        os.makedirs("Logs")
    logging.basicConfig(handlers=[logging.StreamHandler(),
                                  logging.FileHandler(filename='Logs/server.log')],
                        level=logging.DEBUG,
                        format=log_format,
                        datefmt='%Y-%m-%d %H:%M:%S%z')

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-i", "--ip", dest="ip", default="0.0.0.0", help="IP on which the CherryPy server will listen (default is 0.0.0.0)")
    parser.add_option("-p", "--port", dest="port", type="int", default=4050, help="Port on which the CherryPy server will listen (default is 5040)")
    (options, args) = parser.parse_args()
    setup_logging()
    run_server(options.ip, options.port)