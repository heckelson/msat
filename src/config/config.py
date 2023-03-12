import logging

config = {
    # this also gets written into when parsing the arguments.

    # TODO: Update when output_dir is set to avoid code duplication.
    "OUTPUT_MEDIA_DIRNAME": "generated_media",

    "OUTPUT_DB_DIRNAME": "db",
    "OUTPUT_DB_FILENAME": "results.db"
}

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)7s] %(name)-10s: %(message)s"
)