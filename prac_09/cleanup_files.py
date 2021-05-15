"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main():
    """Cleanup Song Lyric File Names"""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics')

    # Print a list of all files in current directory
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    main_name = new_name.split('.')[0]
    extension = new_name.split('.')[-1]
    letter_to_check = ""
    special_characters = ["'", ".", "_", "(", ")"]
    alt_name = ""
    for i in enumerate(main_name):
        if not i[0] == 0 and letter_to_check == letter_to_check.lower() and not i[1] == i[
                1].lower() and letter_to_check not in special_characters:

            alt_name += "_" + i[1]
        elif i[1] == "(" and letter_to_check != "_":
            alt_name += "_" + i[1]
        else:
            alt_name += i[1]
        letter_to_check = i[1]
    main_name = alt_name

    new_name = "{}.{}".format(main_name, extension)
    return new_name


main()
