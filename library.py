import sys

HEADER  = "\nBook|Writer|ISBN|Year"
WELCOME = "\n\nWelcome to the library!\n\nChoose from the following options\n" \
          "1) Add new book\n2) Print current database content in ascending" \
          "order by publishing year\nQ) Exit the program\n"

def add_book(db_file):
    with open(db_file, "r") as f:
        database = [tuple(map(str, i.strip('\n').split('|'))) for i in f]
    print("Book's name?")
    book = input()
    print("Writer's name?")
    writer = input()
    print("Book's ISBN?")
    isbn = input()
    print("Publising year?")
    year = input()
    print(HEADER)
    print(book + "|" + writer + "|" + isbn +  "|" + year)
    print("Do you want to udpdate the database? (yes / no)")
    update = input()
    if update == "yes":
        database.append((book, writer, isbn, year))
        update_database(db_file, database)
    else:
        ui(db_file)

def update_database(db_file, database):
    with open(db_file, "w") as f:
        database.sort(key=lambda entry: (entry[0].lower(), entry[3]))
        for entry in database:
            f.write(entry[0] + "|" + entry[1] + "|" + entry[2] + "|" + entry[3] + "\n")
    print("\n***DATABASE UPDATED***\n")
    read_file(db_file)

def read_file(db_file):
    with open(db_file, "r") as f:
        print(f.read())

def ui(db_file):
    print(WELCOME)
    user_input = input()
    if user_input == "1":
        add_book(db_file)
    elif user_input == "2":
        read_file(db_file)
    
def main():
    db_file = sys.argv[1]
    ui(db_file)

if __name__ == "__main__":
    main()
