"""Creating Reverse Complimentary string for any given string"""

DNA_string = "AAAACCCGGT"

complimentary = ""

for letter in DNA_string: 

    if letter == "A":
        complimentary += "T"

    elif letter == "T":
        complimentary += "A"

    elif letter == "G":
        complimentary += "C"

    else:
        complimentary += "G"

print(complimentary [::-1])
