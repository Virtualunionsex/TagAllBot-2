import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID", "22825629"))
api_hash = os.environ.get("API_HASH", "e8db542482a1638b4e5b03ed1ddae521")
bot_token = os.environ.get("TOKEN", "6637498343:AAGMoAT_eAz3n19MyvyYrX0IuUUiVBTeWSo")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
spam_chats = []

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply(
    "*𝐇𝐚𝐥𝐥𝐨 𝐤𝐚\n\n𝟏. 𝐔𝐧𝐭𝐮𝐤 𝐝𝐚𝐩𝐚𝐭 𝐝𝐢 𝐚𝐜𝐜 𝐝𝐚𝐥𝐚𝐦 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐕𝐕𝐈𝐏 𝟔𝟗 𝐚𝐧𝐝𝐚 𝐡𝐚𝐫𝐮𝐬 𝐨𝐫𝐝𝐞𝐫 𝐭𝐞𝐫𝐥𝐞𝐛𝐢𝐡 𝐝𝐚𝐡𝐮𝐥𝐮\n𝟐. 𝐊𝐞𝐭𝐢𝐤 /help 𝐔𝐧𝐭𝐮𝐤 𝐤𝐞𝐭𝐞𝐫𝐚𝐧𝐠𝐚𝐧 𝐥𝐞𝐛𝐢𝐡 𝐥𝐚𝐧𝐣𝐮𝐭.",
    link_preview=False,
    buttons=(
      [
        Button.url('VVIP INDO', 'https://t.me/+JwJvH6WYxJUxYzM9'),
        Button.url('VVIP BARAT', 'https://t.me/+sp7IZ5sqyaQ5NzVh'),
        Button.url('VVIP JAPAN', 'https://t.me/+zYNYxA8ynMMyODA9')
      ], 
      [
        Button.url('VVIP SPECIAL', 'https://t.me/+QgE_FnYmJyNjM2Q1'),
        Button.url('VVIP HENTAI', 'https://t.me/+vT6fFhFvsNZhN2Vl'),
        Button.url('VVIP RANDOM 1', 'https://t.me/+_ODzudM3VRc0Yjk1')
      ], 
      [
        Button.url('VVIP RANDOM 2', 'https://t.me/+I1gHwnaRh2FlNDk1'),
        Button.url('VVIP RANDOM 3', 'https://t.me/+fdGS9EPjxAI5MDQ1'),
        Button.url('VVIP RANDOM 4', 'https://t.me/+WBcdV9sTt1A3YjA1')
      ]
    )
  )

@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "*𝐂𝐀𝐑𝐀 𝐎𝐑𝐃𝐄𝐑 \n\n𝟏. 𝐏𝐈𝐥𝐢𝐡 𝐕𝐕𝐈𝐏 𝐲𝐚𝐧𝐠 𝐀𝐧𝐝𝐚 𝐢𝐧𝐠𝐢𝐧𝐤𝐚𝐧 (𝐭𝐞𝐤𝐚𝐧 𝐭𝐨𝐦𝐛𝐨𝐥 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 & 𝐃𝐞𝐬𝐤𝐫𝐢𝐩𝐬𝐢) \n𝟐. 𝐓𝐫𝐚𝐧𝐬𝐟𝐞𝐫 𝐬𝐞𝐬𝐮𝐚𝐢 𝐝𝐞𝐧𝐠𝐚𝐧 𝐡𝐚𝐫𝐠𝐚 𝐕𝐕𝐈𝐏 𝐲𝐚𝐧𝐠 𝐝𝐢 𝐢𝐧𝐠𝐢𝐧𝐤𝐚𝐧 \n𝟑. 𝐊𝐢𝐫𝐢𝐦 𝐛𝐮𝐤𝐭𝐢 𝐩𝐞𝐦𝐛𝐚𝐲𝐚𝐫𝐚𝐧 𝐤𝐞𝐩𝐚𝐝𝐚 𝐀𝐝𝐦𝐢𝐧 (𝐭𝐞𝐤𝐚𝐧 𝐭𝐨𝐦𝐛𝐨𝐥 𝐚𝐝𝐦𝐢𝐧 𝐚𝐭𝐚𝐰 𝐤𝐞 @ordervvip_69bot)\n𝟒. 𝐀𝐧𝐝𝐚 𝐚𝐤𝐚𝐧 𝐝𝐢 𝐚𝐜𝐜 𝐬𝐞𝐭𝐚𝐤𝐚𝐡 𝐚𝐧𝐝𝐚 𝐦𝐞𝐥𝐚𝐤𝐮𝐤𝐚𝐧 𝐩𝐞𝐦𝐛𝐚𝐲𝐚𝐫𝐚𝐧"
  await event.reply(
    helptext,
    link_preview=False,
    buttons=(
      [
        Button.url('Admin 1', 'https://t.me/panggil_m'),
        Button.url('Admin 2', 'https://t.me/xxgt4us')
      ], 
      [
        Button.url('Opsi Pembayaran', 'https://telegra.ph/Opsi-Pembayaran-08-23'),
        Button.url('Testy', 'https://t.me/+wrS0J0dsDh82NmI1')
      ], 
      [
        Button.url('List Harga & Deskripsi', 'https://telegra.ph/Deskripsi-VVIP-08-23')
      ]
    )
  )
  



print(">> VVIP STARTED @nakama_asl<<")
client.run_until_disconnected()
