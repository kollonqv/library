import sys

HEADER  = "\nBook|Writer|ISBN|Year"
WELCOME = "\n\nWelcome to the library!\n\nChoose from the following options\n" \
          "1) Add new book\n2) Print current database content in ascending" \
          "order by publishing year\nQ) Exit the program\n"


def add_book(db):
    database = [tuple(map(str, i.split('|'))) for i in db]
    print("EXISTING DATABSE:")
    print(database)

    print("Book's name?")
    book = input()
    print("Writer's name?")
    writer = input()
    print("Book's ISBN?")
    isbn = input()
    print("Publising year?")
    year = input()
    print(HEADER)
    entry = (book, writer, isbn, year)
    entry_str = book + "|" + writer + "|" + isbn +  "|" + year
    print(entry_str)

    print("Do you want to udpdate the database? (yes / no)")
    update = input()
    if update == "yes":
        database.append(entry)
        database.sort(key=lambda entry: (entry[0], entry[3]))
        print(database)
    else:
        return

def ui(db):
    print(WELCOME)
    user_input = input()
    if user_input == "1":
        add_book(db)
    else:
        print("WRONG INPUT" + user_input)

def main():
    db = sys.argv[1]
    with open(db) as database_file:
        ui(database_file)

    #database_file.close()

if __name__ == "__main__":
    main()
