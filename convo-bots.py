import openai
import time

# Set up OpenAI API credentials
openai.api_key = "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"

# Set up GPT model ID
model_id = "gpt-3.5-model"

# Read in initial messages from text files
with open("bot1_initial_message.txt", "r") as f:
    bot1_initial_message = f.read().strip()

with open("bot2_initial_message.txt", "r") as f:
    bot2_initial_message = f.read().strip()

# Define function to generate bot responses
def generate_bot_response(bot_message):
    response = openai.Completion.create(
        engine=model_id,
        prompt=[{"role": "system", "content": bot_message}],
        temperature=0.5,
        max_tokens=150,
        n=1,
        stop=None
    )

    bot_response = response.choices[0].text.strip()
    return bot_response

# Set up initial messages and roles for each bot
bot1_message = bot1_initial_message
bot2_message = bot2_initial_message
bot1_role = "system"
bot2_role = "system"

# Start conversation loop
while True:
    # Bot 1 sends message
    time.sleep(2) # wait for 2 seconds before sending message
    print("Bot 1:", bot1_message)
    
    # Bot 2 generates response
    bot2_role = "user"
    bot2_message = generate_bot_response(bot1_message)
    
    # Bot 2 sends message
    time.sleep(2) # wait for 2 seconds before sending message
    print("Bot 2:", bot2_message)
    
    # Bot 1 generates response
    bot1_role = "user"
    bot1_message = generate_bot_response(bot2_message)