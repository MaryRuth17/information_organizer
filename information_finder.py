def main(): # find the name in the file
    name = input("Enter the full name to search: ").strip()
    result = search_name(name)

    if result:
        print("Information Found:\n")
        print(result)

    else:
        print(f"No information found for {name}.")

