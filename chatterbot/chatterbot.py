def answer_question(inp):
    result = ""

    if "why" in inp:
        result += "Because "

    if "what is" in inp:
        result += "it's all part of the mystery..."
    else:
        result += "waffles!"

    return result


def answer_exclamation(inp):

    if "this is" in inp or "you are" in inp or "you're" in inp:
        result = "YAHHHHHHHHHHHH! Backatcha ;)"
    else:
        result = "Yeah, things are totally sweet."

    return result


def normalize(inp):
    return inp.lower().strip()


def chat(inp):
    inp = normalize(inp)

    if inp.endswith("?"):
        result = answer_question(inp)
    elif inp.endswith("!"):
        result = answer_exclamation(inp)
    else:
        result = "You're a dope."

    return result
