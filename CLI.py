# Command Line Interface Version

import trainer

interface_mode = "CLI"

trainer.check_first_launch()

lang = trainer.get_language_file()
user_stats = trainer.load_user_stats()
exercise = trainer.Exercise()

# TODO Window name according to language

print(lang[0]['11'], user_stats[0]['name'])
print(lang[0]['12'])

while True:
    print("\nMain Menu Options:\n1 - Practice Multiplications!\n2 - See Statistics\n3 - Settings\n4 - About\n5 - Exit")
    selection = int(input("\nWhat do you want to do?\n"))

    if selection == 1:
        q = int(input("\nHow many exercises do you want to do?\n"))

        for x in range(q):
            exercise.get_exercise()
            print("%s * %s = ?" % (str(exercise.current_exercise[0] + 1), str(exercise.current_exercise[1] + 1)))
            answer = int(input())

            if exercise.check_answer(answer) is True:
                print("Correcto!")
            else:
                # If this is another elif to check if is False then the historic and other counters will increase twice.
                print("Incorrecto! La respuesta era: ", str(exercise.answer))
    elif selection == 3:
        print("\nSettings:\n1 - Reset statistics\n2 - Edit your name\n3 - Go back to the main menu")
        sub_selection = int(input("\nWhat do you want to do?\n"))
        if sub_selection == 1:
            trainer.reset_user_stats()
            print("Reset successful! All stats have been set to 0.")
        elif sub_selection == 2:
            trainer.edit_name()
        elif sub_selection == 3:
            continue

    elif selection == 5:
        break
