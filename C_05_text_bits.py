#calculates number of bits

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


#main routine

text_ans = calc_text_bits()
print(text_ans)