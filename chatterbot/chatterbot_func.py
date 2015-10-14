def _answer_question(inp):
    result = ""

    if "why" in inp:
        result += "Because "

    if "what is" in inp:
        result += "it's all part of the mystery..."
    else:
        result += "waffles!"

    return result


def _answer_exclamation(inp):

    if "this is" in inp or "you are" in inp or "you're" in inp:
        result = "YAHHHHHHHHHHHH! Backatcha ;)"
    else:
        result = "Yeah, things are totally sweet."

    return result


def _normalize(inp):
    return inp.lower().strip()


def get(obj, prop):
    if hasattr(obj, '__getitem__'):
        return obj[prop]
    else:
        return getattr(obj, prop)


def create_bot(name):
    return {'name': name, 'type': 'bot'}


def create_dog(name):
    return {'name': name, 'type': 'dog'}


def chat(bot, inp):
    inp = _normalize(inp)

    if inp.endswith("?"):
        result = _answer_question(inp)
    elif inp.endswith("!"):
        result = _answer_exclamation(inp)
    else:
        result = "You're a dope."

    result = '%s says, "%s"' % (get(bot, 'name'), result)

    return result


def chat_loud(bot, inp):
    return chat(bot, inp).upper().replace('SAYS', 'SCREAMS')
