# Command Line Interface Version

import trainer

interface_mode = "CLI"

trainer.check_first_launch()

lang = trainer.get_language_file()
user_stats = trainer.load_user_stats()

historic = trainer.Counter('historico')
corrects = trainer.Counter('aciertos')
fails = trainer.Counter('fallos')
streaks = trainer.Counter('streaks')

# TODO Window name according to language

print(lang[0]['11'], user_stats[0]['name'])
print(lang[0]['12'])


print("\nMain Menu Options:\n1 - Practice Multiplications!\n2 - Settings\n3 - About\n4 - Exit")

confidence = trainer.Matrix('confidence', 12, 12)
tables = trainer.Matrix('tables', 12, 12)

# Check if the multiplication tables that were loaded are not empty, if so generate them.
# This will allow to change the size in the future by changing the x, y parameters.
if tables.see(11, 11) == 0:
    for x in range(12):
        for y in range(12):
            tables.set(x, y, (x+1)*(y+1))
