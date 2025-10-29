# HackBot Webhook

Этот репозиторий хранит webhook для Chatterfy / Render — возвращает динамические сообщения (сканирование, прогресс) для игр: Chicken Road, Lucky Mines, Aviator, Penalty ShotOut.

## Как это работает
- `bot.py` — Flask-сервер с маршрутом `/webhook`.
- Chatterfy отправляет POST-запрос с телом:
  ```json
  {
    "user": {"name": "Ivan"},
    "game": "mines"
  }
