from random import choice
# print command is used to print text on screen
print("what's your name?")
# input command is used to wait the user that needs to type something on the terminal
name=input()
# split is used to get a random thing, in this case an emoji
emojis="😎 🥱 🤯 🤮 😍".split()
emoji=choice(emojis)
# at the end the program print your name (variable), a text message (this will be your mood today) and the random emoji
print(name,",this will be your mood today!",emoji)