# Web Scraping Alert Bot

This project is a web scraping bot that monitors websites, detects changes, and sends alerts via Discord, Email, and Telegram.

## Project Structure

- `/scrapers`: Contains the logic for different website scrapers.
- `/core`: Main engine for change detection and processing.
- `/alerts`: Modules for Discord, Email, and Telegram notifications.
- `/storage`: Data persistence (JSON/SQLite).
- `/utils`: Common utility functions.
- `config.py`: Configuration settings and API keys.
- `main.py`: The entry point for the bot.

## Roadmap

- [x] Phase 1: Basic Scraper
- [x] Phase 2: Data Storage
- [x] Phase 3: Change Detection
- [x] Phase 4: Alert System (Discord, Email, Telegram)
- [x] Phase 5: Multi-site Support
- [x] Phase 6: Scheduler
- [x] Phase 7: Real-world Handling (Headers, Proxies)
- [x] Phase 8: Smart Detection
- [ ] Phase 9: CLI Interface
- [ ] Phase 10: Deployment
