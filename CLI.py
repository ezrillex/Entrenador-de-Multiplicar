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


print("\nMain Menu Options:\n1 - Practice Multiplications!\n2 - About\n3 - Exit")
