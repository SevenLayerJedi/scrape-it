from lib.banner import *
from lib.pastebin import *

# Print the obligatory banner
print_banner()

def __signal_handler(signal, frame):
    cprint(" [+] Kill commanded received - Quitting...", "yellow", attrs=["bold"])
    sys.exit(0)


# Run the scrape_pastebin function
while True:
    try:
        scrape_pastebin()
    except Exception as e:
        print(' [ERROR MAIN] ')

