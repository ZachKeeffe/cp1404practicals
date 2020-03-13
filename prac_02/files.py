name = input("Please enter your name.\n>>>")
out_file = open("names.txt", "w")
print("{}".format(name), file=out_file)
out_file.close()

input_file = open("names.txt", "r")
name = input_file.read()
print("Your name is {}".format(name))
input_file.close()

input_file = open("numbers.txt", 'r')
number1 = int(input_file.readline())
number2 = int(input_file.readline())
print(number1 + number2)
input_file.close()

input_file = open("numbers.txt", 'r')
final_number = 0
for i in input_file:
    number = int(i)
    final_number += number
print(final_number)
input_file.close()
