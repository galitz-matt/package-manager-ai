from user_facing_agent import UserFacingAgent


def client_loop():
	model = UserFacingAgent()
	while True:
		query = input("Q: ")
		if query == "quit":
			break
		if query == "resolved":
			model.clear_memory()
			print("A: Is there anything else you need help with?\n")
			continue
		# handle installation step, we don't want instructions, we want: installing... another model might handle this
		model.append_memory(query)
		response = model.query(query)
		print(f"A: {response}\n")
		model.append_memory(response)


if __name__ == "__main__":
	client_loop()