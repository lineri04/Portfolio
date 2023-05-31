address_book = {}

def add_contact(name, phone):
    address_book[name] = phone

def update_contact(name, phone):
    address_book[name] = phone

def delete_contact(name):
    del address_book[name]

def lookup_contact(name):
    return address_book.get(name)

add_contact("John Doe", "555-555-5555")
add_contact("Jane Smith", "444-444-4444")

print(lookup_contact("John Doe")) # prints "555-555-5555"

update_contact("John Doe", "555-555-5556")

print(lookup_contact("John Doe")) # prints "555-555-5556"

delete_contact("Jane Smith")

print(lookup_contact("Jane Smith")) # prints None
