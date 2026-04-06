import time
import schedule
import config
from scrapers import SCRAPERS
from core.monitor import ChangeMonitor
from alerts.discord_alert import DiscordAlert
from alerts.telegram_alert import TelegramAlert
from alerts.email_alert import EmailAlert
from utils.logger import setup_logger

logger = setup_logger("bot")

def run_bot():
    logger.info("Bot execution cycle started...")
    
    # Initialize components
    monitor = ChangeMonitor()
    
    discord = DiscordAlert(config.DISCORD_WEBHOOK_URL)
    telegram = TelegramAlert(config.TELEGRAM_TOKEN, config.TELEGRAM_CHAT_ID)
    email = EmailAlert(config.SMTP_SERVER, config.SMTP_PORT, config.SENDER_EMAIL, config.SENDER_PASSWORD, config.RECEIVER_EMAIL)

    for site_name, ScraperClass in SCRAPERS.items():
        try:
            logger.info(f"Scraping {site_name}...")
            scraper = ScraperClass()
            data = scraper.scrape()
            
            if data:
                changed, message = monitor.has_changed(site_name, data)
                if changed:
                    headline = data[0].get('title', 'Check site for details')
                    url = data[0].get('url', scraper.url)
                    alert_msg = f"Alert: {site_name} updated!\n{message}\nTop headline: {headline}\nURL: {url}"
                    logger.info(alert_msg)
                    
                    # Send alerts
                    discord.send(alert_msg)
                    telegram.send(alert_msg)
                    email.send(f"Web Scraping Alert: {site_name}", alert_msg)
                    
                    # Save new state
                    monitor.save_current_data(site_name, data)
                else:
                    logger.info(f"No changes detected for {site_name}.")
            else:
                logger.warning(f"Failed to scrape {site_name}.")
        except Exception as e:
            logger.error(f"Unexpected error while processing {site_name}: {e}")

    logger.info("Bot execution cycle completed.")

if __name__ == "__main__":
    logger.info("Starting bot...")
    # Run once at start
    run_bot()
    
    # Schedule
    schedule.every(config.SCRAPE_INTERVAL_MINUTES).minutes.do(run_bot)
    logger.info(f"Bot scheduled to run every {config.SCRAPE_INTERVAL_MINUTES} minutes.")
    
    while True:
        schedule.run_pending()
        time.sleep(1)
