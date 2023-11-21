
# Online Python - IDE, Editor, Compiler, Interpreter
import requests
import json
import os

def chose_seat():
  # Запит на отримання картинки з розташуванням місць
  response = requests.get("https://api.seatgeek.com/venues/1/seatmap?client_id=YOUR_CLIENT_ID")
  seatmap_data = json.loads(response.content)
  seatmap_image = seatmap_data["images"]["large"]

  # Створення меню з кнопками, які відповідають місцям
  buttons = []
  for seat in seatmap_data["seats"]:
    if seat["status"] == "available":
      buttons.append(
        {
          "text": f"Місце {seat['row']}-{seat['section']}-{seat['number']}",
          "callback_data": f"{seat['row']}_{seat['section']}_{seat['number']}",
        }
      )

  # Надсилання картинки з розташуванням місць та меню з кнопками
  message = {
    "attachment": {
      "type": "template",
      "payload": {
        "template_type": "button",
        "text": "Виберіть місця",
        "buttons": buttons,
      },
    },
  }
  bot.send_message(chat_id, json.dumps(message))

  # Запуск функції registration(), якщо користувач натиснув кнопку "Зареєструватися"
  def register_handler(update):
    registration()
  bot.register_callback_query_handler(register_handler)

  # Запуск функції buy_ticket(), якщо користувач натиснув кнопку "Купити квиток"
  def buy_ticket_handler(update):
    buy_ticket(update.callback_query.data.split("_")[0], update.callback_query.data.split("_")[1], update.callback_query.data.split("_")[2])
  bot.register_callback_query_handler(buy_ticket_handler)



