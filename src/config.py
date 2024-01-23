import json


def _load_json_file(file_name: str):
	with open(file_name) as json_file:
		return json.load(json_file)


class Configuration:
	def __init__(self):
		self.config = _load_json_file("../docs/config.json")

	def key(self):
		return self.config["key"]

	def ufm_tune(self):
		return self.config["user-facing-model-tuning"]

	def memory_prompt(self):
		return self.config["memory-prompt"]