import json


def _config():
	with open("../docs/config.json") as config_file:
		return json.load(config_file)