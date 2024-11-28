
def main(): # asking the name to search in the file
    name = input("Enter the full name to search for: ")
    result = search_name(name)

    if result:
        print("Information Found:")
        print(result)

    else:
        print(f"No information found for {name}.")

def search_name(name): # seaarching the name in file
    try:
        with open("personal_info.txt", "r") as file:  # Open the file in read mode
            data = file.read() 

            entries = data.split("-" * 50)

            for entry in entries:
                if name in entry: 
                    return entry
            
    except :
        print("The file does not exist.")
        return None
    
if __name__ == "__main__":
    main()