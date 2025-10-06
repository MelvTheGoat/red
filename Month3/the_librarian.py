book1 = {'Title': 'The Daily Stoic', 'Author': 'Ryan Holiday', 'Year of publication': 2016, 'ISBN': '0735211736 ', 'Available': True}
book2 = {'Title': 'The Richest Man in Babylon', 'Author': 'George S. Clason', 'Year of publication': 1926, 'ISBN': '0451165209 ', 'Available': False}
book3 = {'Title': 'Rich Dad Poor Dad', 'Author': 'Robert T. Kiyosaki', 'Year of publication': 1997, 'ISBN': '1612680194 ', 'Available': False}
book4 = {'Title': 'The Psychology of Money', 'Author': 'Morgan Housel', 'Year of publication': 2020, 'ISBN': '0857197681', 'Available': True}

all = [book1, book2, book3, book4]

def add_book(**book):
    all.append(book)
    # print("Added")
add_book(Title='Deep Work', Author='Cal Newport', Year_of_Publication=2016, ISBN= '9781455586691')

def view_books():
    print(all)

def update_book(isbn, **changes):
    for book in all:
        if book['ISBN'] == isbn:
            book.update(changes)
            return book
print(update_book('9781455586691',  Title='9999', Author = 'Melv'))

def search_book(title):
    for name in all:
        if name['Title'] == title:
            return name
print(search_book('The Richest Man in Babylon'))

def delete_book(isbn):
    global all
    all = [delete for delete in all if delete['ISBN'] != isbn]
    print('Deleted')

delete_book('0735211736')
print(all)

def borrow_book(isbn):
    for borrow in all:
        if borrow['ISBN'] == isbn:
            if borrow['Available']:
                borrow["Available"] = False
                print(f"You borrowed '{borrow['Title']}'")
            else:
                print("Book already borrowed")
            return
    print("Book not found")

def return_book(isbn):
    for book in all:
        if book['ISBN'] == isbn:
            book["Available"] = True
            print(f"You returned '{book['Title']}'")
            return
    print("Book not found")

def menu():
    while True:
        print("Menu:")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Search Book")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. Exit")

        choice = input("Enter from 1-8: ")

        if choice == '1':
            book = {'Title':input('Enter title: '),
            'Author':input('Enter author: '),
            'Year':input('Enter year of publication: '),
            'ISBN':input('Enter ISBN: ')
            }
            add_book(**book)
        elif choice == '2':
            view_books()
        # elif choice == '3':
        #     Title = str(input("Enter title: "))
        #     if all['Title'] == Title:
        #         return Title
        #     pass
        elif choice == '4':
            pass
        elif choice == '5':
            title = input("Enter: ")
            search_book(title)
        else:
            print('Invalid Input')
        


menu()