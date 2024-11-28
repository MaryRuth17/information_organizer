    

#ask user information
name = input("Enter full name: ")
age = int(input("Enter age: "))
address = input("Enter address: ")
number = int(input("Enter phone number: "))
email = input("Enter email: ")
birthdate = int(input("Enter birthdate (e.g., YYYYMMDD): "))

# list the information
personal_info = {
    "name" : name,
    "age" : age,
    "address" : address,
    "number" : number,
    "email" : email,
    "birthdate" : birthdate
}