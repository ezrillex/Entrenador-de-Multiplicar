import CLI
import GUI
import trainer

# TODO check file for interface mode

try:
    conf = trainer.load_config_file()
    inter = conf['interface']

    if inter == 'CLI':
        CLI.cli()
    elif inter == 'GUI':
        GUI.gui()
    else:
        trainer.initialize_config_file()
except FileNotFoundError:
    # launch default interface mode:
    # Maybe initialize the config file here instead of the CLI and GUI?
    trainer.initialize_config_file()
    CLI.cli()


