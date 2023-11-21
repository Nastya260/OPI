import sqlite3

def connect():
    conn = sqlite3.connect("tickets.db")
    conn.row_factory = sqlite3.Row
    return conn

def disconnect(conn):
    conn.commit()
    conn.close()

def read_session(session_id):
    conn = connect()

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sessions WHERE session_id = ?", (session_id,))

    row = cursor.fetchone()

    disconnect(conn)

    if row is not None:
        return row
    else:
        return None

def write_bought_tickets(tickets):
    conn = connect()

    for ticket in tickets:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tickets (event_id, seat_id, user_id) VALUES (?, ?, ?)",
                       (ticket['event_id'], ticket['seat_id'], ticket['user_id']))

    disconnect(conn)

# Приклад використання
session_data = read_session(13)
print(session_data)

tickets_data = [{"event_id": 1, "seat_id": 2, "user_id": 3}, {"event_id": 4, "seat_id": 5, "user_id": 6}]
write_bought_tickets(tickets_data)
