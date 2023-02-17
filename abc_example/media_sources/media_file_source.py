import datetime
from urllib.parse import urlparse
import requests
import shutil
import logging
import os
logger = logging.getLogger(__name__)

from abc_example.media_sources.media_source import MediaSource


class MediaFileSource(MediaSource):
    def __init__(self, media_type, file_id, file_uri):
        MediaSource.__init__(self, file_id, uri=file_uri, media_type=media_type)
        self.is_stream = False
        self.file_path = None

    def download_source(self, dir_name):
        try:
            file_path = urlparse(self.uri).path
            file_ext = os.path.splitext(file_path)[1]
            base_name = str(self.file_id) + file_ext
            self.file_path = os.path.join(dir_name, base_name)
            logger.info(f"Download file from uri: {self.uri} to: {self.file_path}")
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            with requests.get(self.uri, stream=True) as r:
                r.raise_for_status()
                with open(self.file_path, 'wb') as f:
                    shutil.copyfileobj(r.raw, f, length=0)
            return self.file_path

        except Exception as e:
            logger.exception(f"file download_source exception: {repr(e)}")
            self.file_path = None
            raise

    def remove(self):
        try:
            if self.file_path is not None:
                os.remove(self.file_path)
        except FileNotFoundError as e:
            logger.error(f"failed to remove local file {self.file_path}) {repr(e)}")

    @staticmethod
    def file_exist(url):
        try:
            start = datetime.datetime.utcnow()
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                end = datetime.datetime.utcnow()
                logger.info(f"Check file exists {(end - start).total_seconds()} seconds")

                return True
            return False
        except Exception as e:
            return False

    def get_media_info(self):
        return self.is_stream
