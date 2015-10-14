import chatterbot_func
import chatterbot
import random

from timekeeper import TimeKeeper

print "Say something to our chatterbot!"

bots = [
    chatterbot.Bot("Etta"),
    chatterbot_func.create_bot("Gertrude"),
]

keeper = TimeKeeper()
keeper.start()

while True:
    inp = raw_input()
    print chatterbot_func.chat_loud(random.choice(bots), inp)
    print "Time elapsed: %d seconds" % int(keeper.elapsed())
