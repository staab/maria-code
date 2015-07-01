import chatterbot
import random

from timekeeper import TimeKeeper

print "Say something to our chatterbot!"

bots = [
    chatterbot.Bot("Etta"),
    chatterbot.Bot("Gertrude"),
    chatterbot.Bot("Brunhilde")
]

keeper = TimeKeeper()
keeper.start()

while True:
    inp = raw_input()
    print random.choice(bots).chat(inp)
    print "Time elapsed: %d seconds" % int(keeper.elapsed())
