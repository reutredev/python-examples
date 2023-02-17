from abc import ABC, abstractmethod, ABCMeta
import logging

logger = logging.getLogger(__name__)


class MediaSource(ABC):
    def __init__(self, file_id, uri, media_type, file_timestamp=None):
        self.file_id = file_id
        self.file_timestamp = file_timestamp
        self.uri = uri
        self.media_type = media_type

    def media_path(self):
        return self.uri

    @abstractmethod
    def download_source(self, dir_name):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def get_media_info(self):
        pass