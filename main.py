# Single Line comment
# C:\Users\Laptop-16\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.9
import wikipedia
import cgi
def que():
    person = input('Write the title of the information you want to know = ')
    info = wikipedia.summary(person, 2)
    print(info)
    print()
    a = input("Want to get more information?(Y/N)")
    if a == "y" or a == "Y":
        info = wikipedia.summary(person)
        print(info)
        print()
        print("SOURCE: WIKIPEDIA")
        print()
    elif a == "n" or a == "N":
        print("Thanks For using us. Bye Bye.....")
    else:
        print("Invalid choice")

while True:
    que()

