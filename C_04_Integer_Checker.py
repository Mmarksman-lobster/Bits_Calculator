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

#main routine goes here
for item in range(0, 2):
    integer = int_check("integer",0)
    print(integer)


for item in range(0, 2):
    width = int_check("Width:", 1)
    print(width)

print()

for item in range(0, 2):
    height = int_check("Height:", 1)
    print(height)