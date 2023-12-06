def out_red(text):
    print("\033[31m{}".format(text))
    out_white("")


def out_white(text):
    print("\033[37m{}".format(text), end='')


def out_blue(text):
    print("\033[34m{}".format(text))
    out_white("")


def out_green(text):
    print("\033[32m{}".format(text))
    out_white("")
