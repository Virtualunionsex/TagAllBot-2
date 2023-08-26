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
bot_token = os.environ.get("TOKEN", "6185575028:AAHXlMB2Wzzw34LfaxYAIg1pMWMHbI7TfGU")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
spam_chats = []

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply(
    "𝙎𝙚𝙡𝙖𝙢𝙖𝙩 𝙙𝙖𝙩𝙖𝙣𝙜 𝙙𝙞 𝘽𝙤𝙩 𝙑𝙑𝙄𝙋 𝙋𝙍𝙀𝙈𝙄𝙐𝙈 𝘾𝘼𝙎𝙀𝙔\n\nUntuk dapat di acc dalam VVIP Premium Casey anda harus order terlebih dahulu\nKetik /help untuk order sekarang juga (hub admin)",
    link_preview=False,
    buttons=(
      [
        Button.url('Vip Barat', 'https://t.me/+ogAPs2a5V6Q5MDg1'),
        Button.url('Vip Indo', 'https://t.me/+ZPGGejCtidI2YmZl'),
        Button.url('Vip Japan', 'https://t.me/+AfnaaWvPy_M3OGZl'), 
        Button.url('Vip Random', 'https://t.me/+2P_gt1UC8NUyNTdl')
      ], 
      [
        Button.url('Vip Hijab', 'https://t.me/+Dnj_Rl12uz4yNDQ9'),
        Button.url('Vip Colmek', 'https://t.me/+1jMoO7jdWfcyNDM9'), 
        Button.url('Vip Galery Hot', 'https://t.me/+SydNzuyT4nc1Mjc1')
      ], 
      [ 
        Button.url('Vvip Rare', 'https://t.me/+G6pYPjyv_GJlNGM1'), 
        Button.url('Vvip Sultan', 'https://t.me/+MZS6Bh6Bmag4MzI9'),
        Button.url('Vvip Bocil', 'https://t.me/+7BDWowl_LBA4YTQ1')
      ], 
      [ 
        Button.url('Vvip Cosplay Hot', 'https://t.me/+vafRZM3V_HI1N2Q1'), 
        Button.url('Vvip Durasi 1Jam ', 'https://t.me/+vUJLYw2PQF0xNTA1'),
      ], 
      [
        Button.url('Vvip Anak Sekolah Cabul', 'https://t.me/+kaOTRtB1q2llMDBl')
      ]
    )
  )

@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "𝙏𝙚𝙠𝙣𝙞𝙨 𝙊𝙧𝙙𝙚𝙧:\n\n1. Pilih VVIP yang Anda inginkan cek tombol list harga\n2. Transfer sesuai harga VVIP (Hub Admin) \n3. Kirim bukti pembayaran ke admin\n4. Anda akan di acc setalah mengirimkan bukti paembayaran"
  await event.reply(
    helptext,
    link_preview=False,
    buttons=(
      [
        Button.url('👩‍💻 Admin', 'https://t.me/CASEYYTRUSTED'),
        Button.url('🛒 Testy', 'https://t.me/testi_casey')
      ],
      [
        Button.url('List Harga', 'https://telegra.ph/Deskripsi-VVIP-08-23')
      ]
    )
  )
    
  @client.on(events.NewMessage(pattern="^/settings$"))
async def help(event):
  helptext = "Hungungi Bot Teknisi Jika ada Kendala Pada Setiap Bot Kami"
  await event.reply(
    helptext,
    link_preview=False,
    buttons=(
      [
        Button.url('🤖 Teknisi', 'https://t.me/teknisi69_bot')
      ]
    )
  )



print(">> VVIP STARTED @nakama_asl<<")
client.run_until_disconnected()
