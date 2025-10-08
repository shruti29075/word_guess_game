from app.database import init_db
from app.ui import render_ui

def main():
    init_db()
    render_ui()

if __name__ == "__main__":
    main()



