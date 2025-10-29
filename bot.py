# bot.py
import os
import random
from flask import Flask, request, jsonify

app = Flask(__name__)

GAMES = {
    "chicken": {
        "title": "Chicken Road",
        "steps": [
            ("🐔 Курочка готовится к прыжку...", 10),
            ("🔎 Сканирование дороги...", 30),
            ("⚡ Поиск безопасных клеток...", 55),
            ("🚀 Расчёт оптимального прыжка...", 80),
            ("✅ Сигнал готов! Удачи!", 100),
        ],
    },
    "mines": {
        "title": "Lucky Mines",
        "steps": [
            ("🧭 Подключение к модулям...", 10),
            ("⚙️ Анализ карты мин...", 25),
            ("💣 Сканирование мин...", 50),
            ("🔒 Проверка безопасных зон...", 80),
            ("✅ Сигнал Lucky Mines готов!", 100),
        ],
    },
    "aviator": {
        "title": "Aviator",
        "steps": [
            ("✈️ Подключение к пилоту...", 10),
            ("📡 Сбор телеметрии...", 30),
            ("🔎 Анализ траектории...", 60),
            ("⚡ Вычисление оптимального момента...", 90),
            ("✅ Сигнал Aviator готов!", 100),
        ],
    },
    "penalty": {
        "title": "Penalty ShotOut",
        "steps": [
            ("🧤 Вратарь готовится...", 10),
            ("📊 Анализ вратарской позиции...", 35),
            ("🎯 Сканирование углов...", 65),
            ("⚽ Финальное расчётное окно...", 90),
            ("✅ Сигнал Penalty готов!", 100),
        ],
    },
}

DEFAULT_FLOW = [
    ("🧠 Подключение к системе...", 10),
    ("⚙️ Анализ аккаунта...", 25),
    ("💣 Сканирование мин...", 50),
    ("🧩 Обработка данных...", 75),
    ("✅ Доступ к HackBot открыт!", 100),
]


@app.route("/", methods=["GET"])
def index():
    return "OK", 200


@app.route("/webhook", methods=["POST"])
def webhook():
    """
    Ожидаемый JSON от Chatterfy:
    {
      "user": {"name": "Ivan"},
      "game": "mines"    # optional, one of: chicken/mines/aviator/penalty
    }

    Возвращает:
    {
      "dynamic_messages": [
         {"text": "💣 Сканирование мин... (50%)"},
         ...
      ],
      "meta": {"game": "Lucky Mines"}
    }
    """
    try:
        data = request.get_json(force=True) or {}
    except Exception:
        data = {}

    user = data.get("user", {}) or {}
    user_name = user.get("name") or user.get("first_name") or "друг"

    requested_game = (data.get("game") or "").lower()
    if requested_game in GAMES:
        chosen = GAMES[requested_game]
    else:
        # иногда может прийти game как "Lucky Mines" - попробуем простую проверку
        for key, spec in GAMES.items():
            if requested_game and requested_game in spec["title"].lower():
                chosen = spec
                break
        else:
            # случайный выбор
            chosen = random.choice(list(GAMES.values()))

    steps = chosen.get("steps", DEFAULT_FLOW)

    messages = []
    # предисловие можно кастомизировать
    messages.append({"text": f"Привет, {user_name}! Подготавливаю сигнал для {chosen['title']}..."})

    for text, prog in steps:
        messages.append({"text": f"{text} ({prog}%)"})

    messages.append({"text": "Если хочешь — нажми ⚡ Получить сигнал"} )

    return jsonify({
        "dynamic_messages": messages,
        "meta": {"game": chosen["title"]}
    }), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
