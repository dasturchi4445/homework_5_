from db import Database


def db():
    service = input(f"""
        1. Users
           >>> """)

    if service == "1":
        qeary = "SELECT * FROM person"
        print(Database.connect(qeary, "select"))


if __name__ == "__main__":
    db()
