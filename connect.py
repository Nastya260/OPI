def read_session(session_id):
  """
  Читає інформацію про сеанс з бази даних.

  Аргументи:
    session_id: Ідентифікатор сеансу.

  Повертає:
    Інформацію про сеанс або None, якщо сеанс не знайдено.
  """

  # Підключення до бази даних
  conn = connect()

  # Виконання запиту до бази даних
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM sessions WHERE session_id = ?", (session_id,))

  # Зчитування результатів запиту
  row = cursor.fetchone()

  # Закриття з’єднання
  conn.close()

  # Повернення результату
  if row is not None:
    return row
  else:
    return None
