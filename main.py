import time
import schedule
import config
from scrapers.hn_scraper import HackerNewsScraper
from core.monitor import ChangeMonitor
from alerts.discord_alert import DiscordAlert
from alerts.telegram_alert import TelegramAlert
from alerts.email_alert import EmailAlert

def run_bot():
    print("Bot is running...")
    
    # Initialize components
    monitor = ChangeMonitor()
    hn_scraper = HackerNewsScraper()
    
    discord = DiscordAlert(config.DISCORD_WEBHOOK_URL)
    telegram = TelegramAlert(config.TELEGRAM_TOKEN, config.TELEGRAM_CHAT_ID)
    email = EmailAlert(config.SMTP_SERVER, config.SMTP_PORT, config.SENDER_EMAIL, config.SENDER_PASSWORD, config.RECEIVER_EMAIL)

    # Scrape Hacker News
    print("Scraping Hacker News...")
    data = hn_scraper.scrape()
    
    if data:
        changed, message = monitor.has_changed("hacker_news", data)
        if changed:
            alert_msg = f"Alert: Hacker News updated!\n{message}\nTop headline: {data[0]['title']}\nURL: {data[0]['url']}"
            print(alert_msg)
            
            # Send alerts
            discord.send(alert_msg)
            telegram.send(alert_msg)
            email.send("Web Scraping Alert: Hacker News", alert_msg)
            
            # Save new state
            monitor.save_current_data("hacker_news", data)
        else:
            print("No changes detected for Hacker News.")
    else:
        print("Failed to scrape Hacker News.")

if __name__ == "__main__":
    # Run once at start
    run_bot()
    
    # Schedule
    schedule.every(config.SCRAPE_INTERVAL_MINUTES).minutes.do(run_bot)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
