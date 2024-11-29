
def user_personal_info(): # to collect the info
# ask user information
    while True:
        name = input("Enter first name (letters only): ")
        if not all(c.isalpha() or c.isspace() for c in name):
            print("Name should only contain letters")
            continue
        
        while True:
            try:
                age = int(input("Enter age: "))
                if age < 0 or age > 120:
                    raise ValueError
                break

            except ValueError:
                print("Age must be reasonable age and a number")

        address = input("Enter address: ")

        while True:
            try:
                number = int(input("Enter phone number (e.g 09161161553): "))
                if len(str(number)) != 10: 
                    raise ValueError
                break
                
            except ValueError:
                print("Phone number must be a number with 11 digits")

        email = input("Enter email: ")

        while True:
            try:
                birthdate = int(input("Enter birthdate (YYYYMMDD): "))
                if len(str(birthdate)) != 8:
                    raise ValueError
                break

            except ValueError:
                print("Birthdate must be a number with format YYYYMMDD")

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