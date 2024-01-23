from config import Configuration
import google.generativeai as genai


class UserFacingAgent:
	def __init__(self):
		self.config = Configuration()
		genai.configure(api_key=self.config.get_key())
		self._model = genai.GenerativeModel("gemini-pro")
		self._tune = self.config.get_user_facing_model_tuning()
		self._memory = ""

	def query(self, query: str) -> str:
		return self._model.generate_content(self._tune + "\n\n" + query).text