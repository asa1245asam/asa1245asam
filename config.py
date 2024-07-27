import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("6868992854:AAEWVQbBu_Bi_GXHK8myaQ8R_77I4XUDnfw", "")

    APP_ID = int(os.environ.get("APP_ID", 24936636))

    API_HASH = os.environ.get("API_HASH", "8b31da388113c1dd1619d34fa867f6d0")
