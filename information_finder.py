
def main(): # asking the name to search in the file
    while True:
        name = input("Enter the full name to search for: ")
        result = search_name(name)

        if result:
            print("Information Found:")
            print(result)
        else:
            print(f"No information found for {name}.")

        while True:
            another_user = input("Do you want to search another person? (yes/no): ").strip().lower()
            
            if another_user == "yes":
                break 
            elif another_user == "no":
                print("Thank you!")
                exit()
            else:
                print("Invalid answer, try again.")

def search_name(name): # seaarching the name in file
    try:
        with open("personal_info.txt", "r") as file:  # Open the file in read mode
            data = file.read() 

            entries = data.split("-" * 50) # seperating the informations by the inputted line

            for entry in entries:
                if name in entry: 
                    return entry
            
    except :
        print("The file does not exist.")
        return None
    
if __name__ == "__main__":
    main()