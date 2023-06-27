import logging

# TODO: Replace this with a better suited data structure

config = {
    # this gets written into when parsing the arguments.
    "outputdir": None,
    "FULL_OUTPUT_MEDIA_DIR": None,

    "OUTPUT_MEDIA_DIRNAME": "generated_media",

    "OUTPUT_DB_DIRNAME": "db",
    "OUTPUT_DB_FILENAME": "results.db"
}


def configure_logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)7s] %(name)-10s: %(message)s"
    )
