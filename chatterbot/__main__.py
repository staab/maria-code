import chatterbot
import random

print "Say something to our chatterbot!"

bots = [
    chatterbot.Bot("Etta"),
    chatterbot.Bot("Gertrude"),
    chatterbot.Bot("Brunhilde")
]

while True:
    inp = raw_input()
    print random.choice(bots).chat(inp)
