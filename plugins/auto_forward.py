# plugins/auto_forward.py
from pyrogram import Client, filters

# আপনার চ্যানেল আইডি এখানে লিখুন (নেগেটিভ সংখ্যা)
AUTO_CHANNEL = -1002980448155   # ← এখানে বসান

@Client.on_message(filters.outgoing & ~filters.bot)
async def auto_forward_to_channel(client, message):
    if AUTO_CHANNEL == -100:   # যদি -100 থাকে তাহলে কিছু করবে না
        return
    
    if message.video or message.document or message.audio or message.photo:
        try:
            await message.copy(chat_id=AUTO_CHANNEL)
            print(f"✅ Forwarded to {AUTO_CHANNEL}")
        except Exception as e:
            print(f"❌ Error: {e}")
