import json

import google.generativeai as genai

def _config():
	with open("../docs/config.json") as config_file:
		return json.load(config_file)


class PMAgent:
	def __init__(self):
		config = _config()
		genai.configure(api_key=config["key"])
		self._model = genai.GenerativeModel("gemini-pro")
		self._tune = config["fine-tuning"]

	def query(self, query):
		return self._model.generate_content(self._tune + "\n\n" + query).text



