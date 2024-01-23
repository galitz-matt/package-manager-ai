import json


def _load_json_file(file_name: str):
	with open(file_name) as json_file:
		return json.load(json_file)


class Configuration:
	def __init__(self):
		self._config = _load_json_file("../docs/config.json")
		self._key = self._config["key"]
		self._ufmodel_tune = self._config["user-facing-model-tuning"]
		self._memory = ""

	def get_key(self):
		return self._key

	def get_user_facing_model_tuning(self):
		return self._ufmodel_tune

	def get_memory(self):
		return self._memory

	def append_memory(self, data):
		self._memory += f"\n {data}"

	def clear_memory(self):
		self._memory = ""