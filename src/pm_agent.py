import json

from config import _config

import google.generativeai as genai


class PMAgent:
	def __init__(self):
		config_content = _config()
		genai.configure(api_key=config_content["key"])
		self._model = genai.GenerativeModel("gemini-pro")
		self._tune = config_content["fine-tuning"]

	def query(self, query: str) -> str:
		return self._model.generate_content(self._tune + "\n\n" + query).text