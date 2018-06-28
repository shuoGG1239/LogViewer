RED = 'red'
BLUE = 'blue'
GREEN = 'green'
LIGHT_BLUE = '#64b2ed'


def bold(text):
    f = "<b>{}</b>"
    return f.format(text)


def italic(text):
    f = "<i>{}</i>"
    return f.format(text)


def underline(text):
    f = "<u>{}</u>"
    return f.format(text)


def colorize(text, color):
    f = "<font color={}>{}</font>"
    return f.format(color, text)
