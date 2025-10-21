import asyncio
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

CYBER_STEPS = [
    "[BOOT SEQUENCE INITIATED] █▒▒▒▒▒▒▒▒▒",
    "Step 1/10: Scanning neural grids... █▒▒▒▒▒▒▒▒",
    "Step 2/10: Decrypting cortex shard... ██▒▒▒▒▒▒▒",
    "Step 3/10: Injecting synth-protocols... ███▒▒▒▒▒▒",
    "Step 4/10: Overclocking cyber-threads... ████▒▒▒▒",
    "Step 5/10: Patching memory splinters... █████▒▒▒",
    "Step 6/10: Syncing black-ops node... ██████▒▒",
    "Step 7/10: Calibrating holo-interface... ███████▒",
    "Step 8/10: Seeding phantom drivers... ████████",
    "Step 9/10: Finalizing spectral handshake... ████████▒",
    "Step 10/10: Stabilizing matrix core... █████████",
    "✅ SYSTEM ONLINE — ACCESS GRANTED"
]

DELAY_SECONDS = 1.2

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("⚡ INITIATE INSTALLATION ⚡", callback_data="install_cyber")]]
    )
    await update.message.reply_text(
        "[WELCOME TO NEON SYSTEM]\nSelect protocol:", reply_markup=keyboard
    )

async def install_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    msg = await query.message.reply_text("Initializing protocol...")
    for step in CYBER_STEPS:
        await asyncio.sleep(DELAY_SECONDS)
        await msg.edit_text(step)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(install_callback, pattern="^install_cyber$"))
    print("✅ Bot started and listening...")
    app.run_polling()

if __name__ == "__main__":
    main()
