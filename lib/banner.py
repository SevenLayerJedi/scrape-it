
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


banner = """\033[91m
                                      _ _   
                                     (_) |  
 ___  ___ _ __ __ _ _ __   ___ ______ _| |_ 
/ __|/ __| '__/ _` | '_ \ / _ \______| | __|
\__ \ (__| | | (_| | |_) |  __/      | | |_ 
|___/\___|_|  \__,_| .__/ \___| \033[90mv1.0\033[0m\033[91m |_|\__|
  \033[0m@SevenLayerjedi  \033[91m| |                      
                   |_|\n"""


def print_banner():
    print(banner + bcolors.ENDC)
