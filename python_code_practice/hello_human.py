import functionGreet

def helloHuman(name):
    functionGreet.greet(name)

humanName = input("Enter your name: ")
helloHuman(humanName)