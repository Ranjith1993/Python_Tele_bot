import telegram.bot
tele_token = input("Enter Telegram Token")
channel_id = input("Enter channel id")
bot = telegram.Bot(token=tele_token)

Data = "Hello.. This is a Test Message"
bot.send_message(chat_id=channel_id, text=Data)
print("Data sent to Telegram group Successfully")
