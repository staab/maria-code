import chatterbot_func


class Bot(object):
    def __init__(self, name):
        self.name = name

    def chat(self, inp):
        return chatterbot_func.chat(self, inp)

    def chat_loud(self, inp):
        return chatterbot_func.chat_loud(self, inp)
