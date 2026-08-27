#functions go here
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5} ")


def instructions():
    statement_generator("instructions", "-")
    print("""
Instructions are here
-use: picture, image, img or p. for image
-use: integer or int for an integer
-use: text, txt or t for text.
- if you say anything other than these the program will loop until you do
- to end the program type xxx when prompted for file type     
    """)

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

#ask user for width and loop
# until they enter a number more than 0
def int_check ( question, low):

    error = f"please enter a number that is more than or equal to {low}\n"
    while True:

        try:
    #ask user for number
             response = int(input(question))

             #check number is more than 0
             if response >= low:
                return response
             else:
                 print(error)
        except ValueError:
            print (error)


def image_calc():
    pass


#main routine goes here
    width = int_check("Width:", 1)
    height = int_check("Height:", 1)
    #calculate number of pixels
    num_pixels = width * height
    num_bits = num_pixels * 24

    #set up answer and return it
    answer = (f"number of pixels {width} x {height} = {num_pixels}"
              f" \nnumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer


def integer_calc():
    #ask user for an integer (more than/= to 0)
    integer = int_check( "integer: ", 0)
    #convert integer into binary and work out bits
    raw_binary = bin(integer)

    #to remove the 'ob'
    binary = raw_binary[2:]
    num_bits = len(binary)


 #set up answer and return it
    answer = f"{integer} in binary is {binary}. and we need {num_bits} to represent it."

    return answer


def calc_text_bits():

    # get text
    response = input("enter some text: ")

    #claculate numbers of bits
    num_chars = len(response)
    num_bits = num_chars * 8

    # set up answer and return it
    answer = (f"{response} has {num_chars} characters."
              f"\n We need {num_chars} x 8 bits to represent it"
              f"\n which is {num_bits} bits ")

    return answer

#main routine goes here

#display instructions if wanted
want_instructions = input("press <enter> to see instructions"
                          " or any key to continue")

if want_instructions == "":
    instructions()

while True:
    file_type = get_filetype()

    if file_type == "xxx":
        break

    # if user meant image or integer when they say "i"
    if file_type =='i':

        want_image = input("press <enter> for an integer or <any key> for image")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    if file_type == "image":
        image_ans = image_calc()
        print(image_ans)

    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)

    else:
        text_ans = calc_text_bits()
        print(text_ans)
