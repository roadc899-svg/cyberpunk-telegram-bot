import asyncio
import os
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# 🔹 Получаем токен из переменных окружения (Render → Environment → BOT_TOKEN)
TOKEN = os.getenv("BOT_TOKEN")
DELAY_SECONDS = 1.2

# ================================
# 🔰 Темы загрузки
# ================================
BOOT_THEMES = {
    "MATRIX": [
        "[MATRIX SEQUENCE ONLINE] ▓▒░▒▓▒░",
        "Step 1/10: Rebuilding system grid... ▓▒░▒",
        "Step 2/10: Injecting data stream... ▓▓▒░",
        "Step 3/10: Encrypting I/O channels... ▓▓▓▒░",
        "Step 4/10: Validating access node... ▓▓▓▓▒",
        "Step 5/10: Syncing submatrix core... ▓▓▓▓▓",
        "Step 6/10: Reconstructing neural map... ▓▓▓▓▓▒",
        "Step 7/10: Running deep scan... ▓▓▓▓▓▓",
        "Step 8/10: Linking memory clusters... ▓▓▓▓▓▓▓",
        "Step 9/10: Activating code layer... ▓▓▓▓▓▓▓▒",
        "Step 10/10: MATRIX ONLINE ✅"
    ],

    "CYBERCORE": [
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
    ],

    "SPACE": [
        "[STARLINK BOOT] 🚀 Initializing modules...",
        "Step 1/10: Aligning solar arrays... ☀️",
        "Step 2/10: Engaging thrusters... 🔥",
        "Step 3/10: Stabilizing orbit... 🌍",
        "Step 4/10: Deploying communication links... 📡",
        "Step 5/10: Charging quantum cores... ⚡",
        "Step 6/10: Calibrating AI navigation... 🧠",
        "Step 7/10: Checking life support... 💨",
        "Step 8/10: Syncing with mission control... 🛰",
        "Step 9/10: Engaging hyperspace engine... 🌌",
        "Step 10/10: SYSTEM READY ✅ — Captain, we’re go for launch!"
    ],

    "NEURAL_AI": [
        "[NEURAL LINK BOOT] 🧠 Initializing...",
        "Step 1/10: Mapping synaptic grid...",
        "Step 2/10: Uploading cognitive layers...",
        "Step 3/10: Activating emotion module...",
        "Step 4/10: Loading decision matrix...",
        "Step 5/10: Scanning for consciousness...",
        "Step 6/10: Merging quantum cores...",
        "Step 7/10: Optimizing neural weights...",
        "Step 8/10: Bootstrapping cognition...",
        "Step 9/10: Validating core alignment...",
        "Step 10/10: AI LINK ESTABLISHED ✅"
    ],

    "DEEP_WEB": [
        "[DARKNET INITIALIZATION] 🕶",
        "Step 1/10: Masking IP signature... 🧬",
        "Step 2/10: Routing via onion layers... 🧅",
        "Step 3/10: Accessing deep protocols... ⚫",
        "Step 4/10: Decrypting data vaults... 🔐",
        "Step 5/10: Uploading stealth module... 👁‍🗨",
        "Step 6/10: Bypassing firewall nodes... 🔥",
        "Step 7/10: Injecting phantom identity... 🧑‍💻",
        "Step 8/10: Syncing ghost network... 🌐",
        "Step 9/10: Engaging cloaking field... 🕳",
        "Step 10/10: SYSTEM INVISIBLE ✅"
    ],

    "BLACK_OPS": [
        "[BLACK OPS SYSTEM] 🕶 Secure boot initiated...",
        "Step 1/10: Establishing encrypted channel... 🔒",
        "Step 2/10: Locating mission server... 🛰",
        "Step 3/10: Bypassing security gateway... 🧬",
        "Step 4/10: Uploading black-ops directives... 💾",
        "Step 5/10: Calibrating drone optics... 🎯",
        "Step 6/10: Patching stealth systems... ⚙️",
        "Step 7/10: Deploying infiltration matrix... 🕵️",
        "Step 8/10: Activating night protocol... 🌑",
        "Step 9/10: Preparing combat link... 🔗",
        "Step 10/10: MISSION ONLINE ✅"
    ],

    # ⚡️ Новая тема с процентами
    "QUANTUM_UPLINK": [
        "[QUANTUM LINK INITIALIZATION] ⚛️ (0%)",
        "Calibrating quantum nodes... (8%)",
        "Synchronizing tachyon relays... (17%)",
        "Decrypting dimensional keys... (29%)",
        "Stabilizing wormhole network... (41%)",
        "Uploading entangled memory cores... (53%)",
        "Reconstructing spacetime lattice... (67%)",
        "Balancing energy flux... (79%)",
        "Activating Q-Core Intelligence... (88%)",
        "Finalizing uplink sequence... (96%)",
        "✅ UPLINK STABLE — 100% COMPLETED"
    ]
}


# ================================
# 🔰 Команда /start
# ================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    theme_name, steps = random.choice(list(BOOT_THEMES.items()))
    msg = await update.message.reply_text(f"🧩 Loading theme: {theme_name}...")
    for step in steps:
        await asyncio.sleep(DELAY_SECONDS)
        try:
            await msg.edit_text(step)
        except Exception as e:
            print(f"⚠️ Edit error: {e}")
            continue
    await msg.reply_text(f"✅ Boot completed ({theme_name} Mode).")


# ================================
# 🔰 Точка входа
# ================================
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Bot started and listening...")
    app.run_polling()


if __name__ == "__main__":
    main()
