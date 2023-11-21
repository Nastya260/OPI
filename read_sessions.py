def read_sessions():
  """
  Зчитує інформацію про всі сеанси з бази даних.

  Повертає:
    Список інформації про всі сеанси.
  """

  # Підключення до бази даних
  conn = connect()

  # Виконання запиту до бази даних
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM sessions")

  # Зчитування результатів запиту
  sessions = cursor.fetchall()

  # Закриття з’єднання
  conn.close()

  # Повернення результату
  return sessions
