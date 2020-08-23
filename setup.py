import os
import subprocess
import sys
import configparser
import shutil
import yaml

PRAW_FILE = "./praw.ini"
PRAW_USER = "default"
CONFIG_FILE = "./shreddit.yml"
ORIG_CONFIG_FILE = "./shreddit/shreddit.yml.example"


def install_deps():
    print("* Installing requirements")

    pip_exit = subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", "-r", "requirements.txt"])

    if pip_exit != 0:
        raise Exception("Pip exited with code " + pip_exit)


def create_praw_ini():
    print("* Setting up praw authentication")
    if os.path.exists(PRAW_FILE):

        ans = input("praw.ini already exists. Use this praw config? [Y/n]")
        if ans.lower() != "n":
            return
        os.remove(PRAW_FILE)

    print("Creating new praw.ini. Enter credentials:")
    praw_keys = ["client_id", "client_secret", "username", "password"]
    config = configparser.ConfigParser()
    config[PRAW_USER] = {}
    for k in praw_keys:
        config[PRAW_USER][k] = input(k + ":")
        with open(PRAW_FILE, "w") as f:
            config.write(f)


def create_shreddit_json():
    print("* Setting up Shreddit config")
    if os.path.exists(CONFIG_FILE):
        ans = input(f"Shreddit config already exists ({CONFIG_FILE}). Use this shreddit config? [Y/n]")
        if ans.lower() != "n":
            return
        os.remove(CONFIG_FILE)

    print("Creating new shreddit.yml")
    shutil.copyfile(ORIG_CONFIG_FILE, CONFIG_FILE)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
    install_deps()
    create_praw_ini()
    create_shreddit_json()

print(f"""--------------------
Shreddit setup complete.

Remember to configure shreddit.yml in the text editor

Use {os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "main.py")} as a target for a scheduled task.
https://help.pythonanywhere.com/pages/ScheduledTasks/
""")
