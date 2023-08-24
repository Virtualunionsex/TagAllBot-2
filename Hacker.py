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
    "*Selamat datang di Bot VVIP Premium 69 \n\nUntuk dapat di acc dalam VVIP Premium 69 anda harus order terlebih dahulu\nKetik /help untuk order sekarang juga ",
    link_preview=False,
    buttons=(
      [
        Button.url('Vvip Indo', 'https://t.me/+JwJvH6WYxJUxYzM9'),
        Button.url('Vvip Barat', 'https://t.me/+sp7IZ5sqyaQ5NzVh'),
        Button.url('Vvip Japan', 'https://t.me/+zYNYxA8ynMMyODA9')
      ], 
      [
        Button.url('Vvip Special', 'https://t.me/+QgE_FnYmJyNjM2Q1'),
        Button.url('Vvip Hentai', 'https://t.me/+vT6fFhFvsNZhN2Vl')
      ], 
      [ 
        Button.url('Random1', 'https://t.me/+_ODzudM3VRc0Yjk1'), 
        Button.url('Random2', 'https://t.me/+I1gHwnaRh2FlNDk1'),
        Button.url('Random3', 'https://t.me/+fdGS9EPjxAI5MDQ1'),
        Button.url('Random4', 'https://t.me/+WBcdV9sTt1A3YjA1')
      ]
    )
  )

@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "*Teknis Order \n\n1. Pilih VVIP yang Anda inginkan cek tombol deskripsi\n2. Transfer sesuai harga VVIP (cek Opsi pembayaran)\n3. Kirim bukti pembayaran ke admin ataw bot acc admin\n4. Anda akan di acc setalah mengirimkan bukti paembayaran"
  await event.reply(
    helptext,
    link_preview=False,
    buttons=(
      [
        Button.url('Admin1', 'https://t.me/panggil_m'),
        Button.url('Admin2', 'https://t.me/xxgt4us'), 
        Button.url('Bot admin', 'https://t.me/ordervvip_69bot')
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
