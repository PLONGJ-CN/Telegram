import os

from telethon import TelegramClient


from dotenv import load_dotenv
import os

load_dotenv()  # 加载 .env 文件中的环境变量

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

print(api_id,api_hash)


client = TelegramClient('session', api_id, api_hash)

async def main():
    await client.start(phone='+8613500240929')

    await client.send_message('@sttlink_bot','/checkin')

    await client.send_message('@iKuuuu_VPN_bot','/checkin')

with client:
    client.loop.run_until_complete(main())
