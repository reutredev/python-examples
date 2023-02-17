import os
import logging
import json
import bottle
from server_example.request_data import RequestData


logger = logging.getLogger(__name__)

server_app = bottle.Bottle()
#bottle.TEMPLATE_PATH.append(os.path.dirname(__file__))


def prepare_result(status, body):
    bottle.response.status = status
    bottle.response.content_type = 'application/json'
    bottle.response.body = body


@server_app.route('/data/data_post', method='POST')
def data_post():
    try:
        logger.info(bottle.request.method + " " + bottle.request.url)
        logger.debug("Headers request: {}".format(dict(bottle.request.headers)))
        logger.info(bottle.request.json)
        request_data = RequestData()
        request_data.parse_request(bottle.request.json)
        prepare_result(200, {"message": request_data.name})
        logger.info("Response OK request name: {}".format(request_data.name))

    except KeyError as ex:
        logger.error("{} request missing mandatory fields. {}".format(bottle.request.json, ex))
        prepare_result(400, {
            'Error message': '{} missing mandatory fields. {}'.format(bottle.request.json, ex)})
    except Exception as err:
        prepare_result(500,
                                  {'Error message': '{} request failed, {}'.format(bottle.request.json, err)})
        logger.exception("{} request failed".format(bottle.request.json))
    finally:
        return bottle.response.body


# if __name__ == '__main__':  # pragma: no cover
#     bottle.run(server_app, host='0.0.0.0', port=5040, debug=True)