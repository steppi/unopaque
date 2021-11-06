"""Stores locations of resources used by opaque."""
import os
from appdirs import user_data_dir

here = os.path.dirname(os.path.realpath(__file__))

OPAQUE_HOME = os.environ.get("OPAQUE_HOME")
if OPAQUE_HOME is None:
    OPAQUE_HOME = os.path.join(user_data_dir(), 'opaque')
BACKGROUND_DICTIONARY_PATH = os.path.join(
    OPAQUE_HOME, "entrez_pubmed_dictionary.pkl"
)
TEST_DATA_LOCATION = os.path.join(here, "tests", "data")
S3_BUCKET_URL = "https://adeft.s3.amazonaws.com/opaque"
