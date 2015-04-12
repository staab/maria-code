import chatterbot

print "Say something to our chatterbot!"

while True:
    inp = raw_input()
    print chatterbot.chat(inp)
