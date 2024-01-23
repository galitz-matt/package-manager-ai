from config import Configuration

import google.generativeai as genai


class PMAgent:
	def __init__(self):
		self._config = Configuration()
		genai.configure(api_key=self._config.get_key())
		self._model = genai.GenerativeModel("gemini-pro")