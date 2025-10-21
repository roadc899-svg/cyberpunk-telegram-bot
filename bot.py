import asyncio
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Получаем токен из Render Environment
TOKEN = os.getenv("BOT_TOKEN")
DELAY_SECONDS = 1.0

# ================================
# 🔰 Шаги загрузки с процентами
# ================================
LOADING_STEPS = [
    ("Conexión al sistema", 0),
    ("Verificación de registro", 12),
    ("Verificación de depósito", 25),
    ("Análisis del historial de apuestas", 40),
    ("Conexión de la cuenta a Lucky Mines", 55),
    ("Recolección de datos del algoritmo de ubicación de minas", 70),
    ("Creación de la primera señal", 88),
    ("✅ Acceso al hackbot concedido", 100),
]

# ================================
# 🔰 Функция выравнивания текста
# ================================
def align_text(text: str, total_length: int = 45) -> str:
    """Добавляет точки, чтобы все строки были одинаковой длины."""
    dots = "." * max(0, total_length - len(text))
    return f"{text}{dots}"

# ================================
# 🔰 Функция создания прогресс-бара
# ================================
def make_progress_bar(percent: int, length: int = 20) -> str:
    filled = int(length * percent / 100)
    empty = length - filled
    return f"[{'█' * filled}{'▒' * empty}] {percent}%"

# ================================
# 🔰 Команда /start
# ================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = await update.message.reply_text("⚙️ Iniciando proceso...")
    
    # Проходим все шаги кроме последнего
    for text, pct in LOADING_STEPS[:-1]:
        await asyncio.sleep(DELAY_SECONDS)
        aligned = align_text(text)
        bar = make_progress_bar(pct)
        try:
            await msg.edit_text(f"{aligned}\n{bar}")
        except Exception as e:
            print(f"⚠️ Edit error: {e}")
            continue

    # Последний шаг (показываем только текст без прогресс-бара)
    final_text, _ = LOADING_STEPS[-1]
    await asyncio.sleep(DELAY_SECONDS)
    aligned_final = align_text(final_text)
    try:
        await msg.edit_text(aligned_final)
    except Exception as e:
        print(f"⚠️ Edit error (final): {e}")

# ================================
# 🔰 Точка входа
# ================================
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Bot started and listening (aligned progress mode)...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
