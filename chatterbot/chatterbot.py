def chat(inp):
    result = ""

    if "why" in inp.lower():
        result += "Because "

    if inp.endswith("?"):
        result += "Waffles!"
    elif inp.endswith("!"):
        result += "YAHHHHHHHHHHHH! Backatcha ;)"
    else:
        result += "You're a dope."

    return result
