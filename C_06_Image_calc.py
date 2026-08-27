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

#main routine
image_ans = image_calc()
print(image_ans)