import json


# Initializes the configuration file to use in other methods.
def initialize_config_file():
    file = open("config.txt", "w", encoding="UTF-8")
    data = "{'language': 'default', 'first_launch': 'false'}"
    file.write(data)
    file.close()


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


# saves the configuration file to the .txt
def save_config_file(data):
    with open("config.txt", "w", encoding="UTF-8") as save:
        data = str(data)
        save.write(data)


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


# Gets the language from the config file
def get_language():
    config = load_config_file()
    return config['language']


# Gets the file according to the language
def get_language_file():
    lang = get_language()
    file = open("language/%s.json" % lang, "r", encoding="UTF-8")
    data = file.read()
    data = json.loads(data)
    file.close()
    return data


# Load user statistics
def load_user_stats():
    file = open("data/user_statistics.json", "r", encoding="UTF-8")
    data = file.read()
    data = json.loads(data)
    file.close()
    return data


# Save user statistics
def save_user_stats(modified_user_stats):
    file = open("data/user_statistics.json", "w", encoding="UTF-8")
    data = str(modified_user_stats)
    data = data.replace("'", '"')
    file.write(data)
    file.close()


# Edits the name of the user
def edit_name():
    lang = get_language_file()
    user_stats = load_user_stats()
    print(lang[0]['curr_name'], user_stats[0]['name'])
    print(lang[0]['name_opt'])

    s = input(lang[0]['do_next'])
    if s == '1':
        print(lang[0]['name?'])
        user_stats[0]['name'] = str(input())
        save_user_stats(user_stats)


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


if __name__ == "__main__":
    check_first_launch()
