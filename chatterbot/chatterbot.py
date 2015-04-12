def chat(inp):
    result = ""

    if "why" in inp.lower():
        result += "Because "

    if inp.endswith("?"):
        if "what is" in inp.lower():
            result += "It's all part of the mystery..."
        else:
            result += "Waffles!"
    elif inp.endswith("!"):
        result += "YAHHHHHHHHHHHH! Backatcha ;)"
    else:
        result += "You're a dope."

    return result
