import sqlite3

def init_db():
    conn = sqlite3.connect("word_scores.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS leaderboard (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        attempts INTEGER
    )""")
    conn.commit()
    conn.close()

def add_score(name, attempts):
    conn = sqlite3.connect("word_scores.db")
    c = conn.cursor()
    c.execute("INSERT INTO leaderboard (name, attempts) VALUES (?, ?)", (name, attempts))
    conn.commit()
    conn.close()

def get_top_scores():
    conn = sqlite3.connect("word_scores.db")
    c = conn.cursor()
    c.execute("SELECT name, attempts FROM leaderboard ORDER BY attempts ASC LIMIT 5")
    data = c.fetchall()
    conn.close()
    return data

