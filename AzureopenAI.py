import os
from openai import AzureOpenAI
import sys

# Read command-line arguments
args = sys.argv[1:]

# Print the arguments
print("Arguments:", args)
# print count of arguments
print("Number of arguments:", len(args))

prompt = "how May I help you?"

if len(args) > 0:
    prompt = f"""
    I have a raspberry pi 4.
    whose GPIO 2 is connected to a red led.
    {args[0]}
    Just return the code.
    """


client = AzureOpenAI(
  azure_endpoint = "https://roborumble.openai.azure.com/",
  api_key="4d53012074d2477c8bb2a9c8fff0c24c",  
  api_version="2024-02-15-preview"
)

# print("prompt:", prompt)
message_text = [{"role":"system","content":""+prompt}]
print("msg to AI::")
print(message_text)

completion = client.chat.completions.create(
  model="test", # model = "deployment_name"
  messages = message_text,
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)

print("\n\ncompletion:")
print(completion)

print("\n\ncompletion message:")
print(completion.choices[0].message.content)

code = completion.choices[0].message.content.replace("```python","").replace("```","")
print("\ncode:")
print(code)

# Write code to a file
f = open("output.py", "w")
f.write(code)
f.close()

# Run the shell script
os.system("python output.py")