import requests
import configparser

config = configparser.ConfigParser()

config.read("../config_file/config.cfg")

print(config.get("section", "username"))
print(config.get("section", "password"))
