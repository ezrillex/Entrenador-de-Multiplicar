import json
import random
import os

# For later more advanced version comparison
# import distutils.version


def version():
    return 1.2


def initialize_directory():
    path = os.path.join(os.path.expanduser('~'), 'Documents', 'Multiplication Trainer')
    if not os.path.exists(path):
        os.makedirs(path)


# GLOBAL
# Initializes the configuration file to use in other methods.
def initialize_config_file():
    initialize_directory()
    path = os.path.join(os.path.expanduser('~'), 'Documents', 'Multiplication Trainer', 'config.txt')
    file = open(path, "w", encoding="UTF-8")
    data = "{'language': 'default', 'first_launch': 'True', 'interface': 'CLI'}"
    file.write(data)
    file.close()


# GLOBAL
# Converts the loaded config file to a dictionary for easier reading in methods.
def load_config_file():
    path = os.path.join(os.path.expanduser('~'), 'Documents', 'Multiplication Trainer', 'config.txt')
    with open(path, "r", encoding="UTF-8") as load:
        load = load.read()
        clean = "{' }"
        for x in range(0, len(clean)):
            load = load.replace("%s" % clean[x], "")
        load = load.split(",")
        for x in range(0, len(load)):
            load[x] = load[x].split(":")
        load = dict(load)
    return load


# GLOBAL
# saves the configuration file to the .txt
def save_config_file(data):
    path = os.path.join(os.path.expanduser('~'), 'Documents', 'Multiplication Trainer', 'config.txt')
    with open(path, "w", encoding="UTF-8") as save:
        data = str(data)
        save.write(data)


# GLOBAL
# changes the cli in the config file to the mode that is passed.
def change_interface_mode(mode):
    conf = load_config_file()
    conf['interface'] = mode
    save_config_file(conf)


# GLOBAL
# Edits the language of the program
def edit_language(language):
    config = load_config_file()
    config['language'] = language
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
    path = os.path.join(os.path.expanduser('~'), 'Documents', 'Multiplication Trainer', 'user_statistics.json')
    file = open(path, "r", encoding="UTF-8")
    data = file.read()
    data = json.loads(data)
    file.close()
    return data


# GLOBAL
# Save user statistics
def save_user_stats(modified_user_stats):
    path = os.path.join(os.path.expanduser('~'), 'Documents', 'Multiplication Trainer', 'user_statistics.json')
    file = open(path, "w", encoding="UTF-8")
    data = str(modified_user_stats)
    data = data.replace("'", '"')
    file.write(data)
    file.close()


# GLOBAL
# Reset user statistics to 0. Without deleting the name.
def reset_user_stats():
    stats = load_user_stats()
    stats[0]['historico'] = 0
    stats[0]['fallos'] = 0
    stats[0]['aciertos'] = 0
    stats[0]['streaks'] = 0
    save_user_stats(stats)


# GLOBAL
# Edits the name of the user
def edit_name(name):
    user_stats = load_user_stats()
    user_stats[0]['name'] = name
    save_user_stats(user_stats)


def initialize_user_stats():
    path = os.path.join(os.path.expanduser('~'), 'Documents', 'Multiplication Trainer', 'user_statistics.json')
    file = open(path, "w", encoding="UTF-8")
    data = '[{"name": "", "historico": 0, "fallos": 0, "aciertos": 0, "streaks": 0}]'
    file.write(data)
    file.close()


# GLOBAL
# Performs a setup if its the first time the program is launched
def check_first_launch():
    try:
        path = os.path.join(os.path.expanduser('~'), 'Documents', 'Multiplication Trainer', 'config.txt')
        test = open(path, "r", encoding="UTF-8")
        blow = load_config_file()
        if blow['first_launch'] == 'True':
            return True
        test.close()
        return False
    except FileNotFoundError:
        initialize_config_file()
        initialize_user_stats()
        return True


# GLOBAL
# A counter for historical attempts, historical corrects, historical failures
class Counter(object):
    def __init__(self, key):
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


# GLOBAL
# Save a matrix given filename and variable containing the matrix to save.
class Matrix(object):
    def __init__(self, name, dim_x, dim_y):
        self.name = name
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.path = os.path.join(os.path.expanduser('~'), 'Documents', 'Multiplication Trainer', '%s.txt' % self.name)
        try:
            self.data = self.load()
        except FileNotFoundError:
            self.data = self.reset()

    # Sets the file to all 0's
    def reset(self):
        matrix = [[0 for x in range(self.dim_x)] for y in range(self.dim_y)]
        data = str(matrix)
        file = open(self.path, "w", encoding="UTF-8")
        file.write(data)
        file.close()
        return matrix

    # Load the matrix from file, if it not exists then do a reset to create an all 0's file.
    def load(self):
        file = open(self.path, "r", encoding="UTF-8")
        data = file.read()
        file.close()
        data = data.split("], [")
        for x in range(0, len(data)):
            data[x] = data[x].replace("[", "")
            data[x] = data[x].replace("]", "")
            data[x] = data[x].replace(" ", "")
            data[x] = data[x].split(",")
        for x in range(0, len(data)):
            for y in range(0, len(data[x])):
                data[x][y] = int(data[x][y])
        return data

    # Save the matrix to a file.
    def save(self, data):
        data = str(data)
        file = open(self.path, "w", encoding="UTF-8")
        file.write(data)
        file.close()

    # .update()
    def update(self):
        """Saves the current self.data, useful if .data has been modified directly"""
        self.save(self.data)

    # Find the lowest value and return its value and indexes in a matrix.
    def get_minimum_argument(self):
        min_x = 0
        min_y = 0
        min_value = self.data[min_x][min_y]
        for x in range(0, self.dim_x):
            for y in range(0, self.dim_y):
                if self.data[x][y] < min_value:
                    min_x = x
                    min_y = y
                    min_value = self.data[x][y]
        # Returning the minimum value is unnecessary since we only need to know the x,y of the lowest not how low it is.
        return [min_x, min_y, min_value]


# GLOBAL
# A class with methods such as .get_random and .get_low_confidence, that generate random or low confidence exercises.
class Exercise(object):
    def __init__(self):
        self.historic = Counter('historico')
        self.corrects = Counter('aciertos')
        self.fails = Counter('fallos')
        self.streaks = Counter('streaks')
        self.confidence = Matrix('confidence', 12, 12)
        self.tables = Matrix('tables', 12, 12)
        # Check if the multiplication tables that were loaded are not empty, if so generate them.
        # This might allow flexibility to change the size in the future by changing the x, y parameters.
        if self.tables.data[11][11] == 0:
            for x in range(12):
                for y in range(12):
                    self.tables.data[x][y] = (x + 1) * (y + 1)
            self.tables.update()
        self.answer = None
        self.current_exercise = None

    def get_exercise(self):
        diff = self.get_difficulty()
        if diff == 1:
            self.low_confidence_exercise()
        elif diff == 2:
            self.random_exercise()
        else:
            pass

    # random
    def random_exercise(self):
        random_x = random.randint(0, 11)
        random_y = random.randint(0, 11)
        self.answer = self.tables.data[random_x][random_y]
        self.current_exercise = [random_x, random_y]
        return self.current_exercise

    # low confidence
    def low_confidence_exercise(self):
        location = self.confidence.get_minimum_argument()
        self.answer = self.tables.data[location[0]][location[1]]
        self.current_exercise = [location[0], location[1]]
        return self.current_exercise

    def check_answer(self, answer):
        self.historic.increase()
        if answer == self.answer:
            self.corrects.increase()
            self.streaks.increase()
            self.confidence.data[self.current_exercise[0]][self.current_exercise[1]] += 1
            self.confidence.update()
            return True
        else:
            self.streaks.reset()
            if self.confidence.data[self.current_exercise[0]][self.current_exercise[1]] > 0:
                self.confidence.data[self.current_exercise[0]][self.current_exercise[1]] -= 1
                self.confidence.update()
            self.fails.increase()
            return False

    def get_difficulty(self):
        """Determines the current difficulty by checking historic and streak values. Returns 1 or 2 to tell the
            caller which type of exercise to generate being 1 for low confidence and 2 for random exercise"""
        rng = random.randint(1, 100)
        streak_percent = (self.streaks.value // 5)
        if rng < streak_percent and self.historic.value > 144:
            return 1
        else:
            return 2


if __name__ == "__main__":
    pass
