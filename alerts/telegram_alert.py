import telebot

class TelegramAlert:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        if self.token:
            self.bot = telebot.TeleBot(token)
        else:
            self.bot = None

    def send(self, message):
        if not self.bot or not self.chat_id:
            print("Telegram Bot Token or Chat ID not set.")
            return False
        
        try:
            self.bot.send_message(self.chat_id, message)
            return True
        except Exception as e:
            print(f"Error sending Telegram alert: {e}")
            return False
