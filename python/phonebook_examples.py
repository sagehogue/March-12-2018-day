phonebook = {
            'Kieran': {
                'name': 'Kieran',
                'number': 8456331959,
                'phrase': 'Good code is not written, it\'s re-written.'
                },
            'Lambda': {
                'name': 'Lambda',
                'number': 8454185633,
                'phrase': 'I am a robot.'
                },
            'Katie': {
                'name': 'Katie',
                'number': 5552121212,
                'phrase': 'I am a Kaie, I code.'
                }
            }

# Create New Contact
def add_contact(name, phone, phrase):
    """
    Adds an entry to the dictionary
    """
    if name not in phonebook:
        phonebook[name] = {
            'name': name,
            'number': phone,
            'phrase': phrase
            }
    else:
        print('There is already an entry by that name. Please use the update option.')


# Retrieve Contact
def search(query):
    """
    Search the dictionary for a number name or phrase (part or whole)
    """
    entries_list = []
    if query in phonebook:
        entries_list.append(phonebook[query])
    else:
        for key, value in phonebook.items():
            for k, v in value.items():
                if query in str(v):
                    entries_list.append(value)
    return entries_list

# Delete Contact
def delete_entry(key, silent=False):
    if not silent:
        print("Are you sure you want to delete the following person? ")
        display(phonebook[key])
        q= input('>: ').lower()
        if q == 'y':
            del phonebook[key]
            print('You have deleted {} from the phonebook.'.format(key))
        else:
            print('You have canceled the deletion. No data was lost.')
    else:
        del phonebook[key]

def remove(query):
    options = search(query)
    if len(options) == 1:
        delete_entry(options[0]['name'])
    else:
        container = enumerate(options)
        print('Which entry do you wish to delete?: ')
        for i in container:
            print('*'*20)
            print('Choice #{}:'.format(i[0]))
            display(i[1])
            print()
        q = int(input('>: '))

        delete_entry(i[1]['name'])


def display(entry):
    print('Name: {}'.format(entry['name']))
    print('Phone: {}'.format(entry['number']))
    print('Phrase: {}'.format(entry['phrase']))

def menu():
    while True:
        q = input('Would you like to (a)dd ' \
        '(s)earch (u)pdate (r)emove or (q)uit?: ').lower()
        if q == 's':
            search_term = input('Enter the name number or phrase (partial or whole): ')
            results = search(search_term)
            if len(results) > 0:
                for i in results:
                    print('*'*20)
                    display(i)
                    print()
            else:
                print('No one was found with that search term: {}'.format(search_term))
        elif q == 'a':
            name = input("What is the first name of the person you are adding?: ")
            phone = int(input("what is the 10 digit number of the person you are adding?: "))
            phrase = input("What is the favored phrase of the person you are adding?: ")
            add_contact(name, phone, phrase)
        elif q == 'u':
            search_term = input('Enter the name number or phrase (partial or whole) of the entry you wish to change: ')
            options = search(search_term)
            container = list(enumerate(options))
            print('Which entry do you wish to change?: ')
            for i in container:
                print('*'*20)
                print('Choice #{}:'.format(i[0]))
                display(i[1])
                print()
            q = int(input('>: '))
            delete_entry(container[q][1]['name'], silent=True)
            new_name = input("What is the first name of the person you are changing?: ")
            new_phone = int(input("what is the 10 digit number of the person you are changing?: "))
            new_phrase = input("What is the favored phrase of the person you are changing?: ")
            add_contact(new_name, new_phone, new_phrase)
        elif q == 'r':
            remove_query = input('Enter the name number or phrase (partial or whole) of the person you wish to remove: ')
            remove(remove_query)
        elif q == 'q':
            exit()
        else:
            print('I did not understand that. Please try again.')

menu()
