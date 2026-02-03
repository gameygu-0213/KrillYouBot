# Welcome to Krill You Bot!

import atexit
import BotHandler as bot
from backend.Globals import log

print("Setting up bot!")

def cleanup():
    log.log_info("Stopping Bot!"); log.close()
    print("closing!")

atexit.register(cleanup)

bot.runBot()