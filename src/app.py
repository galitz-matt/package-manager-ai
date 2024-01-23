from user_facing_agent import UserFacingAgent


def client_loop():
	model = UserFacingAgent()
	while True:
		query = input("Q: ")
		if query == "quit":
			break
		print(f"A: {model.query(query)}\n")


if __name__ == "__main__":
	client_loop()