#functions go here
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5} ")


def instructions():
    statement_generator("instructions", "-")
    print("""
Instructions go here
-instruction 1
-instruction 2  
-etc      
    """)



#main routine goes here
want_instructions = input("press <enter> to see instructions"
                          " or any key to continue")
#display instructions if wanted
if want_instructions == "":
    instructions()
print("program continues")