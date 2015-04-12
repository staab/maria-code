class Bot(object):
    def __init__(self, name):
        self.name = name

    def _answer_question(self, inp):
        result = ""

        if "why" in inp:
            result += "Because "

        if "what is" in inp:
            result += "it's all part of the mystery..."
        else:
            result += "waffles!"

        return result

    def _answer_exclamation(self, inp):

        if "this is" in inp or "you are" in inp or "you're" in inp:
            result = "YAHHHHHHHHHHHH! Backatcha ;)"
        else:
            result = "Yeah, things are totally sweet."

        return result

    def _normalize(self, inp):
        return inp.lower().strip()

    def chat(self, inp):
        inp = self._normalize(inp)

        if inp.endswith("?"):
            result = self._answer_question(inp)
        elif inp.endswith("!"):
            result = self._answer_exclamation(inp)
        else:
            result = "You're a dope."

        result = '%s says, "%s"' % (self.name, result)

        return result
