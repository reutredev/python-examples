from abc_example.media_sources.media_file_source import MediaFileSource
from abc_example.media_sources.media_video_stream_source import MediaVideoStreamSource
import logging

logger = logging.getLogger(__name__)

from enum import Enum

class MediaType(str, Enum):
    IMAGE = 'image'
    VIDEO = 'video'
    VIDEO_STREAM = 'video-stream'

    def __str__(self):
        return self.value


def verify_media_source(media_type, src):
    if media_type == "image" or media_type == "video":
        if MediaFileSource.file_exist(src):
            return
        raise FileNotFoundError(f"File: {src} does not exist")
    elif media_type == "video-stream":
        if MediaVideoStreamSource.stream_exist(url=src):
            return
        raise FileNotFoundError(f"Stream: {src} does not exist")
    else:
        logger.error(f"Invalid media source type: {media_type}")
        raise ValueError(f"Invalid media source type: {media_type}")


def create_media_source(media_type, file_id, file_url):
    if media_type == "image" or media_type == "video":
        return MediaFileSource(media_type, file_id, file_url)
    elif media_type == "video-stream":
        return MediaVideoStreamSource(media_type, file_id, file_url)
    else:
        logger.error(f"Invalid media source type: {media_type}")
        raise ValueError(f"Invalid media source type: {media_type}")
