from shreddit import default_config
from shreddit.shredder import Shredder
import yaml
import configparser
import os
import sys

CONFIG_FILE = "./shreddit.yml"
PRAW_USER = "default"


def shred():
    os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

    print("Reading Shreddit config")
    with open(CONFIG_FILE) as f:
        user_config = yaml.safe_load(f)
        for option in default_config:
            if option in user_config:
                default_config[option] = user_config[option]

    print("Starting Shreddit")
    shredder = Shredder(default_config, PRAW_USER)
    shredder.shred()


if __name__ == "__main__":
    shred()
