from openai import OpenAI
import os

# Hugging Face API, not tested.
client = OpenAI(base_url='https://router.huggingface.co/v1', api_key=os.environ["HF_TOKEN"], default_headers={"X-use-cache": "false"})

# Gets user prediction request.
userinput = input("I am the magic 8 ball, ask me something, and I will predict your future!  ")
wackymode = input("\n Do you want it to be extremely wacky? Yes or No only, capital letter first only.  ")
freedommode = input("\n Do you want the built in options for the answers, or for the AI to make them up? Say Freedom to turn on freedom mode, capital only.   " )

if wackymode == "yes".lower:
    wackysysprompttext = "Please be EXTREMELY WACKY, DO NOT BE NORMAL, MAKE THE PREDICTIONS WACKY!!"
else:
    print("\n \nI guess you don't want it to be wacky, OK!")
    wackysysprompttext = "Do not be wacky."

if freedommode == "freedom".lower:
    freedomsysprompttext = "You can make up any option you want, no matter what. ONE, TWO OR THREE WORDS ONLY"
else:
    print("\n \nI guess you don't want it to make up it's own predictions, OK!")
    freedomsysprompttext = "you can only respond with Yes, No, Maybe, Definetly Not, Less Likely, Unsure, and 50/50."


# Sends data to API along with magic 8 ball system message.
response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3-0324",
    messages=[{"role": "user", "content": f"You are a magic 8 ball that makes predictions for fun, {freedomsysprompttext} The prediction to answer (choose a bit accuratly like this is going to be real) is: {userinput} DO NOT PUT IN ANY EMOJIS!! THIS IS FOR FUN ONLY!!! {wackysysprompttext}"}]
)


# Displays prediction results
print(f"\n \nPREDITCTION RESULTS: {response.choices[0].message.content}")

# For anyone thinking this is AI written, this is all human made, sorry for AI looking comments lol
# - Nintechblox XD
