#!/usr/bin/env python3
# Auto-Boost Scheduler
import schedule
import time
from datetime import datetime
from socmed_booster import SocialMediaBooster

def daily_boost():
    """Daily boosting task"""
    print(f"[{datetime.now()}] Starting daily boost...")
    
    booster = SocialMediaBooster()
    
    # Your targets
    targets = {
        'tiktok': 'your_tiktok_username',
        'instagram': 'your_instagram_username',
        'telegram': '@your_channel',
        'whatsapp': 'your_channel_id'
    }
    
    counts = {
        'tiktok': 500,
        'instagram': 500,
        'telegram': 300,
        'whatsapp': 200
    }
    
    results = booster.boost_all(targets, counts)
    
    # Log results
    with open('logs/boost_log.txt', 'a') as f:
        f.write(f"{datetime.now()} - {results}\n")
    
    print(f"[{datetime.now()}] Daily boost complete: {results}")

# Schedule tasks
schedule.every().day.at("09:00").do(daily_boost)
schedule.every().day.at("15:00").do(daily_boost)
schedule.every().day.at("21:00").do(daily_boost)

print("⏰ Auto-Boost Scheduler started...")
print("🕘 Scheduled: 09:00, 15:00, 21:00 daily")

while True:
    schedule.run_pending()
    time.sleep(60)
