import subprocess


def execute_command(command: str) -> str:
	result = subprocess.run(command.split(" "), stdout=subprocess.PIPE, text=True)
	return result.stdout
