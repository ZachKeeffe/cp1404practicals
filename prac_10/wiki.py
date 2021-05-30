import wikipedia


def main():
    choice = input("Search: ")
    while choice != "":
        try:
            print("**Searching for {}**".format(choice))
            summary = wikipedia.summary(choice)
            print(wikipedia.page(choice).title)
            print(summary)
            print(wikipedia.page(choice).url)
        except wikipedia.exceptions.DisambiguationError:
            print("error")
        choice = input("Search: ")


main()
