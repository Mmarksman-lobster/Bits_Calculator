#ask user for file type
from selectors import SelectSelector


def get_filetype():
    while True:
        response = input("file type: ").lower()

        if response == "xxx" or response == "i":
            return response

        elif response in ['integer','int' ]:
            return "integer"

        elif response in ['image', 'picture', 'img', 'p']:
            return "image"

        elif response in ["text", 'txt', 't']:
            return "text"

        else:
            print("please input a valid file type")

#main routine goes here
while True:
    file_type = get_filetype()
    # if user meant image or integer when they say "i"
    if file_type =='i':

        want_image = input("press <enter> for an integer or <any key> for image")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    print(f"you chose {file_type}")

    if file_type == "xxx":
        break