import os
from dotenv import load_dotenv
load_dotenv()
DB_NAME           = os.environ.get("DB_NAME")
DB_USER           =os.environ.get("DB_USER")
DB_PASSWORD       = os.environ.get("DB_PASSWORD")
DOMAINE_NAME      = os.environ.get("DOMAINE_NAME")



# TEST ENVIRONEMENT
TEST_DB_NAME        = os.environ.get("TEST_DB_NAME")
TEST_DB_USER        =os.environ.get("TEST_DB_USER")
TEST_DB_PASSWORD    = os.environ.get("TEST_DB_PASSWORD")
TEST_DOMAINE_NAME   = os.environ.get("TEST_DOMAINE_NAME")
