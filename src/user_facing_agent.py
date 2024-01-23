from config import Configuration
import google.generativeai as genai


class UserFacingAgent:
	def __init__(self):
		self.config = Configuration()
		genai.configure(api_key=self.config.key())
		self.model = genai.GenerativeModel("gemini-pro")
		self.tune = self.config.ufm_tune()
		self.prompt = self.config.memory_prompt()
		self.memory = ""

	def query(self, query: str) -> str:
		try:
			return self.model.generate_content(f"{self.tune}\n\n{self.prompt}\n\n{self.memory}\n{query}").text
		except ValueError:
			return "I didn't quite get that. Try asking something else."

	def append_memory(self, conversation):
		self.memory += f"{conversation}\n"

	def clear_memory(self):
		self.memory = ""