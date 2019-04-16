def not_string(str):
    if str[:3] == "not" and 3 <= len(str):
        return str
    return "not " + str
