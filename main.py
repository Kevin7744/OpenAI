"""Intergrate chat gpt with open ai"""

# pip install openai package
import openai
# Create an openai key
API_KEY = open("API_KEY", "r").read()
openai.api_key = API_KEY

# response = openai.ChatCompletion.create(
#     model="gpt-3.6-turbo",
#     messages=[
#         {"role": "user", "content": "what is the difference between celsius and Fahrenheit?"}
#     ]
# )

# print(response)

chat_log = []
while True:
    user_message = input()
    if user_message.lower() == "quit":
        break
    else:
        chat_log.append({"role": "user", "content":user_message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_log
        )
        assistance_response = response['choices'][0]['messages']['content']
        print("ChatGpt:", assistance_response.strip("\n").strip())
        chat_log.append({"role":"assistant", "content":assistance_response.strip("\n").strip()})