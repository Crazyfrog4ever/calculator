import math
from pyrogram import Client, filters
from pyrogram.types import Message

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
API_TOKEN = "6851644356:AAGyr6GilrkK7OyhAXxmcWuV_E4Iih-0cag"

# Create a Pyrogram Client
app = Client("my_calculator_bot", api_id=12345, api_hash="your_api_hash", bot_token=API_TOKEN)

# Define a command handler
@app.on_message(filters.command("start"))
def start(_, message: Message):
    message.reply_text("Welcome to the calculator bot! Send me a calculation, e.g., /calc 2+2")

# Define a command handler for calculations
@app.on_message(filters.command("calc"))
def calculate(_, message: Message):
    try:
        # Extract the calculation expression from the message
        expression = message.text.split(" ", 1)[1]
        result = eval(expression)
        message.reply_text(f"Result: {result}")
    except Exception as e:
        message.reply_text(f"Error: {e}")

# Run the bot
app.run()
