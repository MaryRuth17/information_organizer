    

#ask user information
name = input("Enter full name: ")
age = int(input("Enter age: "))
address = input("Enter address: ")
number = int(input("Enter phone number: "))
email = input("Enter email: ")
birthdate = int(input("Enter birthdate (e.g., YYYYMMDD): "))

# list the information
user_personal_info = {
    "name" : name,
    "age" : age,
    "address" : address,
    "number" : number,
    "email" : email,
    "birthdate" : birthdate
}

# write the collected information to a file
def write_to_file(data):
    with open("personal_info.txt", "a") as file:
        file.write(f"Full Name: {data['name']}")
        file.write(f"Age: {data['age']}")
        file.write(f"Address: {data['address']}")
        file.write(f"Phone Number: {data['number']}")
        file.write(f"Email: {data['email']}")
        file.write(f"Birthdate: {data['birthdate']}")