import configparser

config = configparser.ConfigParser()
config.read("config.ini")

API_KEY = config.get("API", "API_KEY")
BASE_URL = config.get("API", "BASE_URL")
ENDPOINT = config.get("API", "ENDPOINT")
