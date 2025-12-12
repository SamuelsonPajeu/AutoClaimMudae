import Vars
import time
import schedule
import threading
import random
from Function import simpleRoll, watchMessages
from i18n import get_text

# Optional icecream import for debugging
try:
    from icecream import ic
except ImportError:
    # Fallback to print if icecream is not installed
    ic = lambda *args: print(*args) if args else None

nextMinute = None

lang = Vars.language

def scheduleNextRoll():
    global nextMinute
    lang = Vars.language
    schedule.clear()
    
    if Vars.repeatBetween:
        minMinute = int(Vars.repeatMinute)
        maxMinute = int(Vars.repeatBetween)
        nextMinute = random.randint(minMinute, maxMinute)
        timeString = f':{nextMinute:02d}'
    else:
        nextMinute = int(Vars.repeatMinute)
        timeString = ':' + Vars.repeatMinute
    
    schedule.every().hour.at(timeString).do(lambda: [simpleRoll(), scheduleNextRoll()])
    print(get_text('log_next_execution', lang, minute=nextMinute))
    return nextMinute

print('='*50)
print(get_text('log_bot_started', lang))
print('='*50)
ic(Vars.desiredSeriesMode)
ic(Vars.minCardPowerMode)
ic(Vars.desiredKakerasMode)
ic(Vars.wishlistMode)

if Vars.repeatBetween:
    print(get_text('log_random_execution', lang, min=Vars.repeatMinute, max=Vars.repeatBetween))
else:
    print(get_text('log_fixed_execution', lang, min=Vars.repeatMinute))

print('='*50)

if Vars.runImmediately:
    simpleRoll()

scheduleNextRoll()

watchThread = threading.Thread(target=watchMessages, daemon=True)
watchThread.start()

while True:
    schedule.run_pending()
    time.sleep(1)
