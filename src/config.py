import json

def _load_json_file(file_name: str):
	with open(file_name) as json_file:
		return json.load(json_file)


class Configuration:
	def __init__(self, json_file):
		self.config = _load_json_file("../docs/config.json")
