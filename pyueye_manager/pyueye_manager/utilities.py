import colorama
colorama.init()


def print_style(*args, **kwargs):
    """
        color = "color_name"
        color_name :
            blue
            green
            red
            yellow
    """
    text = ""
    if not "color" in kwargs:
        color = "clear"
    else:
        color = kwargs['color']
    color_dict = {
        "blue": colorama.Fore.BLUE,
        "green": colorama.Fore.GREEN,
        "yellow": colorama.Fore.YELLOW,
        "red": colorama.Fore.RED,
        "clear": colorama.Style.RESET_ALL,
    }

    for t in args:
        text += " "+str(t)
    print(color_dict[color] + text + color_dict["clear"])
