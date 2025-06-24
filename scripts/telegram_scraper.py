import asyncio
import csv
import os
from telethon import TelegramClient
from dotenv import load_dotenv

# --- Configuration and Initialization ---

load_dotenv('.env')

api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
phone = os.getenv('phone')


if not all([api_id, api_hash, phone]):
    print("Error: Telegram API credentials (TG_API_ID, TG_API_HASH, phone) not found in .env file.")
    print("Please create a .env file in the 'scripts/' directory with your credentials.")
    exit("Missing Telegram API credentials.")


session_file = os.path.join(os.getcwd(), 'telethon_session.session') # Stores session in current working directory


client = TelegramClient(session_file, api_id, api_hash)

# --- Asynchronous Channel Scraping Function ---


async def scrape_channel(client, channel_username, writer, media_dir):
    try:
        
        entity = await client.get_entity(channel_username)
        channel_title = entity.title 

        print(f"--- Starting scraping for channel: {channel_title} (@{channel_username}) ---")

       
        async for message in client.iter_messages(entity, limit=None): 
            media_path = None
            if message.media and hasattr(message.media, 'photo'):
              
                filename = f"{channel_username.replace('@', '')}_{message.id}.jpg"
                media_path = os.path.join(media_dir, filename)
                
                await client.download_media(message.media, media_path)
                
            writer.writerow([channel_title, channel_username, message.id, message.message, message.date, media_path])
            
        print(f"--- Finished scraping for {channel_title} (@{channel_username}). ---")

    except Exception as e:
        
        print(f"Error scraping data from {channel_username}: {e}")

# --- Main Scraping Execution Function ---

async def main():
    
    try:
        await client.start(phone=phone)
        print("Telegram client started successfully.")
    except Exception as e:
        print(f"Failed to start Telegram client: {e}")
        print("Please ensure your phone number in .env is correct and you can receive codes.")
        exit("Client start failed.")
    
    media_dir = 'data/raw/telegram_photos'
    os.makedirs(media_dir, exist_ok=True) 
    print(f"Ensured media directory '{media_dir}' exists for photos.")

    output_csv_path = 'data/raw/telegram_data.csv'

    with open(output_csv_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Channel Title', 'Channel Username', 'ID', 'Message', 'Date', 'Media Path'])
        
        channels_to_scrape = [
            '@ZemenExpress', '@nevacomputer', '@meneshayeofficial',
            '@ethio_brand_collection', '@Leyueqa', '@sinayelj',
            '@Shewabrand', '@helloomarketethiopia', '@modernshoppingcenter',
            '@qnashcom', '@Fashiontera', '@kuruwear',
            '@gebeyaadama', '@MerttEka', '@forfreemarket',
            '@classybrands', '@marakibrand', '@aradabrand2',
            '@marakisat2', '@belaclassic', '@AwasMart',
            '@shager_onlinestore' 
        ]
        
        for channel in channels_to_scrape:
            await asyncio.sleep(2) 
            await scrape_channel(client, channel, writer, media_dir)
            
    print(f"\nAll specified Telegram channels have been processed. Data saved to '{output_csv_path}'.")
    
    await client.disconnect()
    print("Telegram client disconnected.")

with client:
    client.loop.run_until_complete(main())

print("\n--- Data Ingestion (Task 1 - Part 1) Complete! ---")
print("You now have a 'telegram_data.csv' file in 'data/raw/' and 'telegram_photos/' with your collected data.")
print("\nNext, we will move on to the 'Data Preprocessing' part of Task 1, preparing this raw data for NER.")

