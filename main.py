from pyrogram import Client, filters
import os

# Use environment variables (recommended for Koyeb)
api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
bot_token = os.environ["BOT_TOKEN"]

source_chat_id = int(os.environ["SOURCE_CHAT_ID"])
target_chat_id = int(os.environ["TARGET_CHAT_ID"])

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
