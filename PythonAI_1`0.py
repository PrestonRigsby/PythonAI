print("Welcome to Preston's Artificial Intelligence Program")
print("Please remember this program may still have many bugs as it is in ALPHA")
print("")

First = input()

def restart():
    print("")
    First = input()

if First == "EXIT GAME":
    print("Bye")

elif First == "Hello":
    print("Hello, how are you?")
    Hello1 = input()
    if Hello1 == "EXIT":
        print("Oh, Bye.")
        restart()
    if Hello1 == "Good":
        print("Thats good!")
        restart()

elif First == "Who are you?":
    print("I am an Artificial Intelligence Program (AI)")
    print("Made by Preston Rigsby")
    restart()

elif First == "":
    print("")

else:
    print("Sorry I can not read that. Please check your spelling.")
    restart()