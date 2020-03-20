def main():
    stored_numbers = []
    for item in range(1, 6):
        number = int(input("Enter number {:2}: ".format(item)))
        stored_numbers.append(number)

    print("The first number is", stored_numbers[0])
    print("The last number is", stored_numbers[-1])
    print("The smallest number is", min(stored_numbers))
    print("The largest number is", max(stored_numbers))
    print("The average of the numbers is", sum(stored_numbers) / len(stored_numbers))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username_input = input("Please enter your username: ")
    if username_input in usernames:
        print("Access Granted")
    else:
        print("Access Denied")


main()
