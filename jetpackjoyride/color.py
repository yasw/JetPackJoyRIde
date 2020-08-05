import config
def color_text(text, color):
    if '\x1b' in color:
        return color + text + config.Reset
    else:
        try:
            letter = color[0]
            if letter.islower():
                letter = letter.upper()
            color = letter + color[1:]
            return config.COLORS[color] + text + config.Reset
        except Exception as e:
            print(e)
            exit()
            return text
