from abc_example.media_sources.media_source_factory import create_media_source, MediaType
import logging

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    #logging.basicConfig(level=logging.INFO)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    media_source = create_media_source(MediaType.VIDEO, file_id=1,
                                                file_url="http://techslides.com/demos/sample-videos/small.mp4")

    uri = media_source.media_path()
    logger.info(f"media_path = {uri}")
    media_source.download_source("test_video")
    media_source.remove()