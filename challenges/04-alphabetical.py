# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabetize(str):
    str_alphabetized = list(str)
    str_alphabetized.sort()

    new_str = ""
    for i in str_alphabetized:
      new_str = new_str + i
    return new_str


print(alphabetize("testingthisstringandyeah"))