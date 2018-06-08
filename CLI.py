def cli():
    # Command Line Interface Version
    import pprint
    import trainer
    import winsound

    # TODO check for crashes if user inputs non integer values and build more robust inputs.
    interface_mode = "CLI"
    first = trainer.check_first_launch()

    user_stats = trainer.load_user_stats()
    exercise = trainer.Exercise()

    if first is True:
        while True:
            print("Seleccione idioma / Select a language:\n1 - Español(NO IMPLEMENTADO)\n2 - English")
            selection = int(input())
            if selection == 1:
                idioma = "español"
                break
            elif selection == 2:
                idioma = "english"
                break
            else:
                print("Error! Seleccione 1 o 2 / Error! Select either 1 or 2")
        conf = trainer.load_config_file()
        conf['first_launch'] = 'False'
        conf['language'] = idioma
        trainer.save_config_file(conf)
        lang = trainer.get_language_file()
    else:
        lang = trainer.get_language_file()

    # TODO Window name according to language
    # TODO Implement multilingual support.
    print("Hello %s!" % user_stats[0]['name'])
    print("Welcome to the multiplication trainer v.%s!" % trainer.version())

    while True:
        print(
            "\nMain Menu Options:\n1 - Practice Multiplications!\n2 - See Statistics\n3 - Settings\n4 - About"
            "\n5 - Exit")
        selection = int(input("\nWhat do you want to do?\n"))

        if selection == 1:
            q = int(input("\nHow many exercises do you want to do?\n"))

            for x in range(q):
                exercise.get_exercise()
                print("\n%s * %s = ?" % (str(exercise.current_exercise[0] + 1), str(exercise.current_exercise[1] + 1)))
                answer = int(input())

                if exercise.check_answer(answer) is True:
                    print("That's right!\n")
                    winsound.PlaySound("ding.wav", winsound.SND_ASYNC)
                else:
                    # Not another elif because if is False then the historic and other counters will increase twice.
                    print("Wrong! The answer was ", str(exercise.answer), "\n")
                    winsound.PlaySound("buzz.wav", winsound.SND_ASYNC)

        elif selection == 2:
            print("\nSTATISTICS!")
            print("All time exercises made:", exercise.historic.value)
            print("All time right answers: ", exercise.corrects.value)
            print("All time wrong answers: ", exercise.fails.value)
            print("Current number of streaks: ", exercise.streaks.value)
            print("\nStatistics by Multiplication table:")
            pprint.pprint(exercise.confidence.data)

        elif selection == 3:
            print("\nSettings:\n1 - Reset statistics\n2 - Edit your name\n3 - Change Interface Mode"
                  "\n4 - Go back to the main menu")
            sub_selection = int(input("\nWhat do you want to do?\n"))

            if sub_selection == 1:
                trainer.reset_user_stats()
                print("Reset successful! All stats have been set to 0.")

            elif sub_selection == 2:
                print("What is your name?\n")
                name = str(input())
                trainer.edit_name(name)
                print("Name changed successfully %s!" % user_stats[0]['name'])
            elif sub_selection == 3:
                print("Current interface mode is %s" % interface_mode)
                print("Select a new interface mode:\n1 - Command Line Interface\n2 - Graphical User Interface"
                      "\n3 - Cancel and go back")
                a = int(input("What do you want to do?\n"))
                if a == 1:
                    trainer.change_interface_mode('CLI')
                elif a == 2:
                    trainer.change_interface_mode('GUI')
                else:
                    continue
            elif sub_selection == 4:
                continue

        elif selection == 4:
            print("Multiplication Trainer v.%s\nMade in Python 3\nAuthor: Ezra AA Cordova\nWebsite: www.ezrillex.club" %
                  trainer.version())

        elif selection == 5:
            break
