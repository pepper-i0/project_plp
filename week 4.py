try:
    with open("input.txt", "r")as myfile:
        content = myfile.read()

    modified_content = content.upper()

    with open("output.txt", "w") as thisfile:
        thisfile.write(modified_content)

    print("this file has been modified")

except FileNotFoundError:
    print("File not found. Please check the file name and try again.")