# Command Line Interface Version
import pprint
import trainer
import winsound
# TODO check for crashes if user inputs non integer values and build more robust inputs.
interface_mode = "CLI"

trainer.check_first_launch()

lang = trainer.get_language_file()
user_stats = trainer.load_user_stats()
exercise = trainer.Exercise()

# TODO Window name according to language
# TODO Revert multilanguage implementation for later doing that, because in this stage of development is confusing.
print("Hello!", user_stats[0]['name'])
print("Welcome to the multiplication trainer %s!" % trainer.version())

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
                print("That's right!")
                winsound.PlaySound("ding.wav", winsound.SND_ASYNC)
            else:
                # If this is another elif to check if is False then the historic and other counters will increase twice.
                print("Wrong! The answer was ", str(exercise.answer))
                winsound.PlaySound("buzz.wav", winsound.SND_ASYNC)
    elif selection == 2:
        print("\nStatistics by Multiplication table:")
        pprint.pprint(exercise.confidence.data)

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

    elif selection == 4:
        print("Multiplication Trainer v.%s\nMade in Python 3\nAuthor: Ezra AA Cordova\nWebsite: www.ezrillex.club" %
              trainer.version())

    elif selection == 5:
        break
