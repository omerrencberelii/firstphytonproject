"""
Hi, My name is Omer Rençbereli

"""
import random
import time
with open("hello_world.txt", "w") as file:
    while True:
        random_number = random.randrange(10000)
        print(random_number)
        file.write(str(random_number)+"\n")
        time.sleep(3)
        if random_number == 7777:
            file.write("Found!!!")
            break

#%%

def count_substring(string, sub_string):
    string_length = len(string)
    sub_string_length = len(sub_string)
    counter1 = 0
    output = 0
    while True:
        if string[counter1: sub_string_length + counter1] == sub_string:
            output += 1
        counter1 += 1
        if sub_string_length + counter1 - 2 == string_length:
            break

    return output


string = input("Give an example for string: ")
sub_string = input("Give an example for sub_string: ")
print(count_substring(string,sub_string))
