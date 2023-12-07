from pyrogram import Client, filters

bot_token = "5875531360:AAGDX44S1U323YST2wi5HHRWswQO2umudIs"

api_id = 8373939
api_hash = "dc1476b2e297c057ee2d7b6df265a199"
app = Client("nb", api_id, api_hash, bot_token=bot_token)


app.start()


@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(f"Hello")


app.run()
