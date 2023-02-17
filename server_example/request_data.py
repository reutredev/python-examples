import logging

logger = logging.getLogger(__name__)


class RequestData:
    def __init__(self):
        self.id = None
        self.name = None
        self.algorithm = "Algorithm1"
        self.start_from = 0
        self.length_to_check = 65

    def parse_request(self, request_data):
        self.id = request_data['id']
        self.name = request_data['name']
        if "algorithm" in request_data:
            if request_data["algorithm"] not in ("Algorithm1", "Algorithm2"):
                raise KeyError("algorithm field is not correct")
            self.algorithm = request_data["algorithm"]
        if "Start_from" in request_data:
            self.start_from = request_data["Start_from"]
        if "Length_to_check" in request_data:
             self.length_to_check = request_data["Length_to_check"]

        logger.info("id: {}".format(self.id))
        logger.info("name: {}".format(self.name))