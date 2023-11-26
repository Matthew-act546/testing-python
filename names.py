from name_function import get_formatted_name

print("Press q to quit")
while True:
    first = input("Enter your first name here: ")
    if first == 'q':
        break
    last = input("Enter your last name here: ")
    if last == 'q':
        break
    
    formatted_name = get_formatted_name(first, last)
    print(f"This is your formatted name {formatted_name}")