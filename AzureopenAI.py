import os
from openai import AzureOpenAI
import sys

def readPrompt():
  # Check if prompts.txt file exists
  if os.path.exists("prompts.txt"):
    # Read prompts from the file
    with open("prompts.txt", "r") as file:
      prompt = file.read()
  else:
    prompt = "how May I help you?"
  return prompt

def preparePrompt():
    # Read command-line arguments
    args = sys.argv[1:]
    # Print the arguments
    print("Arguments:", args)
    # print count of arguments    
    print("Number of arguments:", len(args))
    if len(args) > 0:
        prompt = f"""
        I have a raspberry pi 4.
        Whose GPIO 2 is connected to a red led.
        Whose GPIO 13 is connected to a servo.
        {args[0]}
        Just return the code.
        """
    else:
        fileData = readPrompt()
        if len(fileData) > 0:
          prompt = f"""
          I have a raspberry pi 4.
          whose GPIO 2 is connected to a red led.
          Whose GPIO 13 is connected to a servo.
          {fileData}
          Just return the code.
          """
    return prompt

def getCompletion(prompt):
    client = AzureOpenAI(
      azure_endpoint = "https://roborumble.openai.azure.com/",
      api_key="4d53012074d2477c8bb2a9c8fff0c24c",  
      api_version="2024-02-15-preview"
    )
    message_text = [{"role":"system","content":""+prompt}]
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
    return completion


def getCode(completion):
    code = completion.choices[0].message.content.replace("```python","").replace("```","")
    return code


def runCode(code):
    f = open("output.py", "w")
    f.write(code)
    f.close()
    os.system("python output.py")


# Main
prompt = preparePrompt()
print("prompt:", prompt)
completion = getCompletion(prompt)
print("completion:", completion)
code = getCode(completion)
print("code:", code)
runCode(code)

