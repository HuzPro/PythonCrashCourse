def get_formatted_name(first_name = '', last_name = '', middle_name = 'H'):

    if first_name and middle_name and last_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    elif first_name and last_name:
        full_name = first_name + ' ' + last_name
    elif middle_name and last_name:
        full_name = middle_name + ' ' + last_name
    elif first_name and middle_name:
        full_name = first_name + ' ' + middle_name
    elif first_name:
        full_name = first_name
    return full_name.title()

Fname = input("Please enter the first name: ")
Mname = input("Please enter the middle name: ")
Lname = input("Please enter the last name: ")


fullName = get_formatted_name(Fname, Mname, Lname)
print(fullName)