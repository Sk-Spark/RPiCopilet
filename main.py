import openai

# Set your OpenAI API key
openai.api_key = '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'

# Define the prompt for generating the shell script
prompt = """
Prompt: Write a shell script to list all files in the current directory.

Shell script:
"""

# Call the OpenAI completion API to generate the shell script
response = openai.Completion.create(
    engine="gpt-3.5-turbo",  # Select the engine you want to use
    prompt=prompt,
    max_tokens=100  # Set the maximum number of tokens for the completion
)

# Extract the generated shell script from the response
shell_script = response.choices[0].text.strip()

# Print the generated shell script
print(shell_script)
