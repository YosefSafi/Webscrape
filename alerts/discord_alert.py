from discord_webhook import DiscordWebhook

class DiscordAlert:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send(self, message):
        if not self.webhook_url:
            print("Discord Webhook URL not set.")
            return False
        
        webhook = DiscordWebhook(url=self.webhook_url, content=message)
        response = webhook.execute()
        return response.status_code == 200
