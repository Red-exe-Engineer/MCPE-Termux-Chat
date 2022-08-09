# Created by Wallee#8314/Red-exe-Engineer

# Imports
from mcpi.minecraft import Minecraft
from os import system

# Clear the screen
system("clear")

# Print a start message
print("Type \"!exit\" to exit the program.\n - Wallee\n")

# Repeat forever
while True:

    # Get a string from the user
    message = input("Chat: ")

    # Check if the string is "!exit"
    if message == "!exit":

        # Break out of the loop
        break

    # May not be able to connect to Minecraft
    try:

        # Connect to Minecraft
        mc = Minecraft.create()

        # Post the message to chat
        mc.postToChat(message)

    # Probably didn't connect to Minecraft
    except ConnectionRefusedError:

        # Tell the user the connection failed
        print("> Couldn't connect to Minecraft")

    # The user wants to stop the program
    except KeyboardInterrupt:

        # Break out of the loop
        break
