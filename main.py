from pyrogram import Client, filters
import os

# Use environment variables (recommended for Koyeb)
api_id = int(os.environ["23939637"])
api_hash = os.environ["477f51720ede3eef6997dbc442151c43"]
bot_token = os.environ["7489586742:AAFyIDZwQa8prfQqhtXYgBJYrqhT94JuRWE"]

source_chat_id = int(os.environ["-1002557248555"])
target_chat_id = int(os.environ["-4686512840"])

app = Client("caption_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define replacement rules
replacements = {
    "bor": "bro",
    "hello": "hi",
    "telegram": "Telegram App"
}

@app.on_message(filters.chat(source_chat_id) & filters.caption)
def forward_and_replace_caption(client, message):
    caption = message.caption
    for old, new in replacements.items():
        caption = caption.replace(old, new)
    
    if message.photo:
        client.send_photo(target_chat_id, message.photo.file_id, caption=caption)
    elif message.video:
        client.send_video(target_chat_id, message.video.file_id, caption=caption)
    elif message.document:
        client.send_document(target_chat_id, message.document.file_id, caption=caption)
    else:
        client.send_message(target_chat_id, caption)

app.run()
