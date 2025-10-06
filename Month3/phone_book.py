# num1 = {"Name": 'James', 'Phone Number': '08104133346', 'Favorite': True}
# num2 = {"Name": 'Tomi', 'Phone Number': '09004155346', 'Favorite': False}
# num1 = {"Name": 'Randy', 'Phone Number': '07007826346', 'Favorite': True}
# num1 = {"Name": 'Sade', 'Phone Number': '08071132446', 'Favorite': False}

# def add_contact():
    

phonebook = []

def add_contact(**details):
    phonebook.append(details)
    return phonebook
add_contact(Name='Tomi', Phone='09004155346', Favorite=False)
add_contact(Name='Henry', Phone='07007826346', Favorite=False)
add_contact(Name='Sade', Phone='08071132446', Favorite=False)


def view_contacts(*view):
    for view in phonebook:
        return phonebook

# print(view_contacts())

def update_contact(phone_number, **changes):
    for number in phonebook:
        if number['Phone'] == phone_number:
            number.update(changes)
            print(f"{phone_number} updated!")
            return number
# print(update_contact('09004155346', Phone='09004'))

def search_contact(name):
    for contact in phonebook:
        if contact['Name'] == name:
            return contact
        
# print(search_contact('Sade'))

def mark_favorite(phone_number):
    for contact in phonebook:
        if contact['Phone'] == phone_number:
            contact['Favorite'] = True
            return
        
# print(mark_favorite('09004155346'))

def unmark_favorite(phone_number):
    for contact in phonebook:
        if contact['Phone'] == phone_number:
            contact['Favorite'] = False
            return
        
# print(mark_favorite('09004155346'))




def update_book(isbn, **changes):
    for book in all:
        if book['ISBN'] == isbn:
            book.update(changes)
            return book
# print(update_book('9781455586691',  Title='9999', Author = 'Melv'))

def main():
    while True:
        print("Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Mark Favorite")
        print("7. Unmark Favorite")
        print("8. Exit")

        choice = input("Enter choice 1-8: ")

        if choice == '1':
           details = {'name': input('Name'), 'phone': input('Phone')}
           add_contact(**details)

        elif choice == '2':
            view_contacts()
        
        elif choice == '3':
            update = {'phone': input("Enter Number: ") }
            pass

        elif choice == '4':
            pass

        elif choice == '5':
            search = {'Phnone Number': input('Number: ')}
            search_contact(search)
        
        elif choice == "6":
            phone = {'phone': input("Enter phone number: ")}
            mark_favorite(phone)

        elif choice == "7":
            phone = {'phone': input("Enter phone number: ")}
            unmark_favorite(phone)

print(main())


