
contacts = {}

def parse_input(user_input):     # Most diffcult part...
 
  cmd, *args = user_input.split()
  cmd = cmd.strip().lower()
  return cmd, args

def add_contact(name, phone_number):
 
  contacts[name] = phone_number
  print("Contact added.")

def change_contact(name, new_phone_number):
 
  if name in contacts:
    contacts[name] = new_phone_number
    print("Contact updated.")
  else:
    print("Contact not found.")

def show_phone(name):
 
  if name in contacts:
    print(contacts[name])
  else:
    print("Contact not found.")

def show_all():
  
  for name, phone_number in contacts.items():
    print(f"{name}: {phone_number}")

def remove_contact(name):
    
    if name in contacts:
      del contacts[name]
      print("Contact removed.")
    else:
      print("Contact not found.")

def main():
 
  print("Welcome to the assistant bot!")
  while True:
    user_input = input("Enter a command: ")
    command, args = parse_input(user_input)

    if command in ["close", "exit", "end", "finish", "bye"]:     # I decided to add new commands to make code more flexible
      print("Good bye!")
      break

    elif command == "hello" or command == "hi":
      print("How can I help you?")

    elif command == "add" or command == "new" or command == "create":
      if len(args) == 2:
        add_contact(args[0], args[1])
      else:
        print("Invalid command format. Please use: add [name] [phone number]")

    elif command == "remove" or command == "delete":   # We got a possibility to delete some phone numbers with few words options
      if len(args) == 1:
        remove_contact(args[0])
      else:
        print("Ivalid command. Please use such command format as: remove [name]")

    elif command == "change" or command == "update":
      if len(args) == 2:
        change_contact(args[0], args[1])
      else:
        print("Invalid command format. Please use: change [name] [new phone number]")

    elif command == "phone" or command == "contact":
      if len(args) == 1:
        show_phone(args[0])
      else:
        print("Invalid command format. Please use: phone or contact + [name]")

    elif command == "all":
      show_all()

    else:
      print("Invalid command.")

if __name__ == "__main__":
  main()




# P.S. Unfortunatly I couldn't find the way to use two-words commands 