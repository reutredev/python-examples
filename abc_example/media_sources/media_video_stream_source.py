import datetime

import requests

from abc_example.media_sources.media_source import MediaSource
import logging

logger = logging.getLogger(__name__)

class MediaVideoStreamSource(MediaSource):
    def __init__(self, media_type, file_id, file_uri):
        MediaSource.__init__(self, file_id, uri=file_uri, media_type=media_type)
        self.is_stream = True

    def download_source(self, dir_name):
        pass

    def remove(self):
        pass

    @staticmethod
    def stream_exist(url):
        try:
            start = datetime.datetime.utcnow()
            response = requests.get(url)
            if response.status_code == 200:
                end = datetime.datetime.utcnow()
                logger.info(f"Check stream exists {(end-start).total_seconds()} seconds")

                return True
            return False
        except Exception as e:
            return False

    def get_media_info(self):
        return self.is_stream