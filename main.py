from openai import OpenAI
import os

# Hugging Face API, not tested.
client = OpenAI(base_url='https://router.huggingface.co/v1', api_key=os.environ["HF_TOKEN"])

# Gets user prediction request.
userinput = input("I am the magic 8 ball, ask me something, and I will predict your future!  ")

# Sends data to API along with magic 8 ball system message.

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[{"role": "user", "content": f"You are a magic 8 ball that makes predictions for fun, you can only respond with Yes, No, Maybe, Definetly Not, Less Likely, Unsure, and 50/50. The prediction to answer (choose a bit accuratly like this is going to be real) is: {userinput} DO NOT PUT IN ANY EMOJIS"}]
)

# Displays prediction results
print(f"\n \n PREDITCTION RESULTS: {response.output_text}")

# For anyone thinking this is AI written, this is all human made, sorry for AI looking comments lol
# - Nintechblox XD
