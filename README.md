# Natural Language Software Installer (Name TBD)

## Description
This project bridges Large Language Models (LLMs), specifically Google's Gemini, with Package Managers to enable software installations using natural language. It simplifies the process of installing software by allowing users to make requests in natural language, which are then processed and executed automatically.

## Features
* Natural Language Understanding: Interprets software installation requests made in conversational language.
* Integration with Google Gemini: Utilizes the advanced capabilities of Google's Gemini LLM for prompt engineering and command generation.
* Automatic Command Execution: Converts natural language requests into terminal commands and executes them for software installation.

## Usage
1. User Query: The user inputs a natural language request, e.g., "Can you install Spotify for me?"
2. Prompt Engineering: The query is restructured into a format suitable for processing by Google Gemini.
3. Command Generation: Google Gemini processes the query and generates appropriate terminal commands for software installation using a package manager (e.g., winget).
4. Execution: A Python script executes the generated terminal commands to install the requested software.

## Acknowledgments
* Google Gemini LLM
* winget package manager
