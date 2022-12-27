def show_menu() -> int:
    print("\n Choose your action:\n"
          "1. Show all phonebook\n"
          "2. Find a subscriber by second name\n"
          "3. Find a subscriber by number\n"
          "4. Add a subscriber to the phone book\n"
          "5. Save the phone book in txt format\n"
          "6. Finish")
    choice = int(input())
    return choice

def print_result(data:list):
    for el in data:
        s= ' '
        for v, k in el.items(): #ключ значения словаря 
            s += f'{v}: {k}\n'
        print(s)
        
def get_search_name() -> str:
    return input ('Enter a second name for serach: ')

def get_search_number() -> str:
    return input("Enter a phone number for search: ")

def get_new_user() -> str:
    last_name = input('Impue a second name')
    first_name = input('Imput a name')
    phone_number = input('Input a phone number')
    description = input('Input an info') 
    return f'{last_name}, {first_name}, {phone_number}, {description}'

def get_file_name() -> str:
    return input('Input file name and save: ')
        

        

