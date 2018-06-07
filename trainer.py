import json
# This module works as logic of the program, but some of the methods are only suited to be used by the CLI.
# TODO adapt each method to be used by either the CLI or the GUI. Maybe with a global var called Interface Mode.
# Methods tagged with GLOBAL are interface independent, methods tagged CLI are CLI specific and need to be generalized.


# GLOBAL
# Initializes the configuration file to use in other methods.
def initialize_config_file():
    file = open("config.txt", "w", encoding="UTF-8")
    data = "{'language': 'default', 'first_launch': 'false', 'interface': 'CLI'}"
    file.write(data)
    file.close()


# GLOBAL
# Converts the loaded config file to a dictionary for easier reading in methods.
def load_config_file():
    with open("config.txt", "r", encoding="UTF-8") as load:
        load = load.read()
        clean = "{' }"
        for x in range(0,len(clean)):
            load = load.replace("%s" % clean[x], "")
        load = load.split(",")
        for x in range(0,len(load)):
            load[x] = load[x].split(":")
        load = dict(load)
    return load


# GLOBAL
# saves the configuration file to the .txt
def save_config_file(data):
    with open("config.txt", "w", encoding="UTF-8") as save:
        data = str(data)
        save.write(data)


# CLI
# Edits the language of the program
def edit_language():
    config = load_config_file()
    while True:
        print("Seleccione idioma / Select a language:\n1 - Español\n2 - English")
        selection = int(input())
        if selection == 1:
            lang = "español"
            break
        elif selection == 2:
            lang = "english"
            break
        else:
            print("Error! Seleccione 1 o 2 / Error! Select either 1 or 2")
    config['language'] = lang
    save_config_file(config)


# GLOBAL
# Gets the language from the config file
def get_language():
    config = load_config_file()
    return config['language']


# GLOBAL
# Gets the file according to the language
def get_language_file():
    lang = get_language()
    file = open("%s.json" % lang, "r", encoding="UTF-8")
    data = file.read()
    data = json.loads(data)
    file.close()
    return data


# GLOBAL
# Load user statistics
def load_user_stats():
    file = open("user_statistics.json", "r", encoding="UTF-8")
    data = file.read()
    data = json.loads(data)
    file.close()
    return data


# GLOBAL
# Save user statistics
def save_user_stats(modified_user_stats):
    file = open("user_statistics.json", "w", encoding="UTF-8")
    data = str(modified_user_stats)
    data = data.replace("'", '"')
    file.write(data)
    file.close()


# CLI
# Edits the name of the user
def edit_name():
    lang = get_language_file()
    user_stats = load_user_stats()
    print(lang[0]['8'], user_stats[0]['name'])
    print(lang[0]['9'])

    s = input(lang[0]['6'])
    if s == '1':
        print(lang[0]['7'])
        user_stats[0]['name'] = str(input())
        save_user_stats(user_stats)


# GLOBAL
# Performs a setup if its the first time the program is launched
def check_first_launch():
    first = False
    try:
        test = open("config.txt", "r", encoding="UTF-8")
        test.close()
    except FileNotFoundError:
        first = True
        initialize_config_file()

    if first is True:
        edit_language()
        edit_name()


# GLOBAL
# A counter for historical attempts, historical corrects, historical failures
class Counter(object):
    def __init__(self,key):
        load = load_user_stats()
        self.value = load[0]["%s" % key]
        self.key = '%s' % key

    def increase(self):
        save = load_user_stats()
        self.value += 1
        save[0][self.key] = self.value
        save_user_stats(save)

    def reset(self):
        save = load_user_stats()
        self.value = 0
        save[0][self.key] = self.value
        save_user_stats(save)

    def current_value(self):
        return self.value


if __name__ == "__main__":
    check_first_launch()
