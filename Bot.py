import Vars
import time
import schedule
import threading
import random
from Function import simpleRoll, watchMessages
from icecream import ic

nextMinute = None

def scheduleNextRoll():
    global nextMinute
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
    return nextMinute

print('='*50)
print('Bot iniciado')
print('='*50)
ic(Vars.desiredSeriesMode)
ic(Vars.minCardPowerMode)
ic(Vars.desiredKakerasMode)
ic(Vars.wishlistMode)

if Vars.repeatBetween:
    print(f'Execução aleatória: entre XX:{Vars.repeatMinute} e XX:{Vars.repeatBetween}')
else:
    print(f'Execução fixa: a cada hora no minuto {Vars.repeatMinute}')

print('='*50)

if Vars.runImmediately:
    simpleRoll()

scheduledMinute = scheduleNextRoll()
print(f'Próxima execução agendada para: XX:{scheduledMinute:02d}')

watchThread = threading.Thread(target=watchMessages, daemon=True)
watchThread.start()

print('Monitoramento de mensagens ativo')
print('Aguardando próxima execução...\n')

while True:
    schedule.run_pending()
    time.sleep(1)
