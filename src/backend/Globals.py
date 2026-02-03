from chars_betterlogs.logs import Logging as Logger # funny
from datetime import datetime

time = str(datetime.today().strftime('%d_%m_%Y-%H_%M_%S'))
log = Logger(f"KrillYouBotLog_{time}.log", "<!-- Krill You Bot v5.0 -->")