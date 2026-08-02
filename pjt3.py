while True:
    print("\n TEXT EDITOR ")
    print("1. Write Text")
    print("2. View Text")
    print("3. Save to File")
    print("4. Open File")
    print("5. Clear Text")
    print("6. Count Words")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nEnter your text.")
        print("Type 'DONE' on a new line to finish.\n")

        lines = []

        while True:
            line = input()
            if line == "DONE":
                break
            lines.append(line)

        text = "\n".join(lines)
        print("Text saved in editor.")

    elif choice == "2":
        if text == "":
            print("Editor is empty.")
        else:
            print("\nYour Text ")
            print(text)

    elif choice == "3":
        filename = input("Enter file name (example: notes.txt): ")

        try:
            file = open(filename, "w")
            file.write(text)
            file.close()
            print("File saved successfully.")
        except:
            print("Error while saving the file.")

    elif choice == "4":
        filename = input("Enter file name to open: ")

        try:
            file = open(filename, "r")
            text = file.read()
            file.close()

            print("\nFile Content ")
            print(text)
        except:
            print("File not found.")

    elif choice == "5":
        confirm = input("Are you sure? (yes/no): ")

        if confirm.lower() == "yes":
            text = ""
            print("Editor cleared.")
        else:
            print("Nothing was deleted.")

    elif choice == "6":
        if text == "":
            print("No text available.")
        else:
            words = text.split()
            print("Total words:", len(words))

    elif choice == "7":
        print("Thank you for using the Simple Text Editor")

        break

    else:
        print("Invalid choice. Please try again")
