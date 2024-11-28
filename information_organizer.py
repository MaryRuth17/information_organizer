
def user_personal_info(): # to collect the info
# ask user information
    name = input("Enter full name: ")
    age = int(input("Enter age: "))
    address = input("Enter address: ")
    number = int(input("Enter phone number: "))
    email = input("Enter email: ")
    birthdate = int(input("Enter birthdate (e.g., YYYYMMDD): "))

    # list the information
    return {
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
        file.write(f"Full Name: {data['name']}\n")
        file.write(f"Age: {data['age']}\n")
        file.write(f"Address: {data['address']}\n")
        file.write(f"Phone Number: {data['number']}\n")
        file.write(f"Email: {data['email']}\n")
        file.write(f"Birthdate: {data['birthdate']}\n")
        file.write("-"*50 + "\n") 

def main():
    while True: # looping the program flow
        # Collect personal information
        personal_info = user_personal_info()
        
        # Write the collected data to a file
        write_to_file(personal_info)

        # Ask if the user wants to input another person's information
        while True:
            another_user = input("Do you want to input another person? (yes/no): ").strip().lower()
        
            if another_user == "yes":
                break 
            elif another_user == "no":
                print("Thank you!")
                exit()

            else:
                print("Invalid answer, try again.")

if __name__ == "__main__":
    main()