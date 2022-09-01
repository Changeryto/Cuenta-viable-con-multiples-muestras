def colonias(text):
    if text == '':
        return True
    else:
            try:
                text = int(text)
                return isinstance(text, int)
            except Exception as exp:
                return False


def diluciones(text):
    try:
        float(text)
        return True
    except Exception as ex:
        return False



