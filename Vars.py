token = '' 
userId = ''
channelId = ''                 
serverId = ''

# Language configuration - Supported: 'pt_BR', 'en',
language = 'pt_BR'
rollCommand= 'wx'

# Configurations for desired modes:
# 'all' for all messages on channel or 'self' for only your own rolls
desiredKakerasMode = 'all' # react to kakera emojis
wishlistMode = 'all' # autoclaim wishlist characters
desiredSeriesMode = 'all' # autoclaim desired series
minCardPowerMode = 'all' # autoclaim cards above min power

# Claim Rules
minCardPower = 150
desiredKakeras = ['kakeraP','kakeraY','kakeraO','kakeraR','kakeraW','kakeraL',]
desiredSeries = [
]
wishlist = [
]

# Other Settings
marryLastRoll = True # automatically marry the highest card power on last roll opportunity if no claim was made
divorceLastRoll = False # automatically divorce after marry on last roll if not match any marry rule
pokeRoll = True  # automatically roll Pokeslot if available
claimDk = True # automatically claim $dk/$daily when available
runImmediately = True # run immediately when the bot starts
snooze = True # do not execute rolls between snoozeBegin and snoozeEnd hours (24h format)

# Random Scheduling between two minutes (e.g., between 06 and 20 minutes past each hour)
repeatMinute = '06'
repeatBetween = '20'

# Snooze period (24h format)
snoozeBegin = '01'
snoozeEnd = '08'
