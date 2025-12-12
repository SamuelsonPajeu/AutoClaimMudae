# Mudae AutoRoll AutoClaim AutoReact 2025
### by GDiazFentanes
#### contributors: Samuelson Pajeu

## Introduction
Auto Rolling, Auto Claiming and Auto Reacting, in order to claim mudae's waifus, kakeras or husbandos every hour automatically. Slash rolling with given parameters for a better botting experience.
These files make it possible to use the Mudae Discord Bot 24/7 without any human input. It is supported by the Discord Api to send and receive messages from any account. After extensive research into the existing bots in late 2023, I realized that none of them are actually working/supported. In order to use it you only need basic knowledge about Discord and Python (If you don't have it, read this document completely and you will easily achieve it).

## Quick Start Guide

1. **Install Python 3** and the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
   Or manually:
   ```bash
   pip install discum schedule
   ```

2. **Get your Discord credentials**:
   - Discord Token ([How to get](https://www.androidauthority.com/get-discord-token-3149920/))
   - Your User ID ([How to get](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID))
   - Channel ID where you want to roll ([How to get](https://docs.statbot.net/docs/faq/general/how-find-id/))
   - Server/Guild ID ([How to get](https://docs.statbot.net/docs/faq/general/how-find-id/))

3. **Edit Vars.py**:
   - Fill in your `token`, `userId`, `channelId`, and `serverId`
   - Configure your preferences (language, roll command, desired series, etc.)
   - Adjust mode settings (`'all'` or `'self'`)

4. **Run the bot**:
   ```bash
   python Bot.py
   ```

5. **Watch the console** for logs and make sure everything is working correctly!

## Features
- **Auto roll** every hour with the command you want
- **Auto Claim** cards based on wishlist, desired series, or minimum power
- **Auto React** only to the kakera you prefer
- **Smart Marry** - Automatically marry the highest power card on your last roll opportunity
- **Auto Divorce** - Optionally divorce after marrying to keep claiming
- **Auto DK/Daily** - Automatically claim $dk and $daily when available
- **Snooze Mode** - Pause bot activity during specific hours (e.g., while sleeping)
- **Random Scheduling** - Execute rolls at random minutes within a range for more human-like behavior
- **Multi-language Support** - Interface in Portuguese (PT-BR) and English (EN)
- **Flexible Modes** - React to all channel messages or only your own rolls
- **Anti-Steal Protection** - Waits before claiming cards rolled by others
- **BONUS** - Uses always slash commands in order to benefit from the native slash boosts (10% extra Kakera)

## Files
This repository contains the following files:
| File Name | File Purpose | Action |
| ------ | ------ |------ |
| Vars.py | Where the variables that you need to change are stored | Edit it!
| Bot.py | The bot is launched from here | Execute it!
| Function.py | Contains the function and code for the bot to work | Nothing!
| i18n.py | Multi-language support (PT-BR, EN) | Nothing!
| requirements.txt | List of required Python packages | Use with pip!

## Requirements
This bot requires the following libraries in order to work correctly. Make sure you have them all installed.
- [Discum](https://pypi.org/project/discum/) for message management
- [Schedule](https://pypi.org/project/schedule/) in order to be permanently executed at an exact minute of an hour

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install discum schedule
```

## How to set up /use
##### Packages
To use this bot you just need to set up a few things. Make sure python 3 is installed along with the 2 required libraries (Discum and Schedule).
If you don't know how to do it, read here → [How to install a Python package](https://packaging.python.org/en/latest/tutorials/installing-packages/)

##### Variables (Vars)
Time to open Vars.py. Here you decide what settings the bot will have. In this section we will see what each variable does and what are the possibilities to fill them out. 
You also choose what Discord account you want to execute the code in and on what guild channel you want the bot to execute the Mudae commands. These two decision will be reflected in these two variables.

**Mandatory variables**: You will have to fill them in if you want the bot to work
+ `token` - The discord Token of the account you want to bot with → [How to get a Discord Token](https://www.androidauthority.com/get-discord-token-3149920/)
+ `userId` - Your Discord User ID → [How to get your user ID](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID)
+ `channelId` - ID of the channel you want to roll in → [How to get a channel ID](https://docs.statbot.net/docs/faq/general/how-find-id/)  
+ `serverId` - ID of the server/guild you want to roll in → [How to get a server/guild ID](https://docs.statbot.net/docs/faq/general/how-find-id/)  

**Configuration variables**: Choose your preferred language and roll command
+ `language` - Choose your preferred language: `'pt_BR'` for Portuguese (Brazil) or `'en'` for English
+ `rollCommand` - Choose what command (only one) will the bot use to roll (`mx`, `ma`, `mg`, `wx`, `wg`, `wa`, `hx`, `ha` or `hg`)

**Mode variables**: Control which messages the bot should react to
+ `desiredKakerasMode` - React to kakera on: `'all'` (all channel messages) or `'self'` (only your own rolls)
+ `wishlistMode` - Claim wishlist characters from: `'all'` (all channel messages) or `'self'` (only your own rolls)
+ `desiredSeriesMode` - Claim desired series from: `'all'` (all channel messages) or `'self'` (only your own rolls)
+ `minCardPowerMode` - Claim cards above min power from: `'all'` (all channel messages) or `'self'` (only your own rolls)

**Claim Rules**: Define what cards and kakera to claim
+ `minCardPower` - Minimum card power to auto-claim (default: `150`)
+ `desiredKakeras` - **Case-sensitive** - Array of kakera types between single quotes separated by commas (see example below)
+ `desiredSeries` - **Case-sensitive** - Array of series between single quotes separated by commas (see example below)
+ `wishlist` - **Case-sensitive** - Array of character names between single quotes separated by commas (see example below)

**Smart Features**: Advanced automation options
+ `marryLastRoll` - Automatically marry the highest power card on your last roll opportunity if no claim was made (`True` or `False`)
+ `divorceLastRoll` - Automatically divorce after marrying on last roll if it doesn't match any marry rule (`True` or `False`)
+ `pokeRoll` - If you want to also roll the Mudae's Pokeslot (`True` or `False`)
+ `claimDk` - Automatically claim $dk/$daily when available (`True` or `False`)
+ `runImmediately` - Run immediately when the bot starts, don't wait for the scheduled time (`True` or `False`)

**Scheduling variables**: Control when the bot executes
+ `repeatMinute` - Exact minute of the hour when the bot will roll (value between `'00'` and `'59'`)
+ `repeatBetween` - If set, bot will roll at a random minute between `repeatMinute` and `repeatBetween` (more human-like behavior)
+ `snooze` - Enable snooze mode to pause bot during specific hours (`True` or `False`)
+ `snoozeBegin` - Hour when snooze starts (24h format, e.g., `'01'` for 1 AM)
+ `snoozeEnd` - Hour when snooze ends (24h format, e.g., `'08'` for 8 AM)

##### Example of correctly filled variables
Depending on the variable type (boolean, string, int or array), the data might be between quotes or not. Please pay attention to it.
In the example, the token, userId, channelId and serverId are invented fields.

```python
# Required Configuration
token = 'MTE4MDIyNzU4NTUzNjQzNDMxNw.GDXjNH.YqGhIq7GwyVHSk9sf9zod3AACAffJeZiynTexc' 
userId = '123456789012345678'
channelId = '1182144443902599230'                 
serverId = '816317249082097684'

# Language and Command Settings
language = 'pt_BR'  # or 'en' for English
rollCommand = 'wa'

# Mode Configuration (how bot reacts to messages)
desiredKakerasMode = 'all'    # React to kakera on all messages or only 'self'
wishlistMode = 'all'          # Claim wishlist from all messages or only 'self'
desiredSeriesMode = 'all'     # Claim desired series from all or only 'self'
minCardPowerMode = 'all'      # Claim min power cards from all or only 'self'

# Claim Rules
minCardPower = 150
desiredKakeras = ['kakeraP','kakeraY','kakeraO','kakeraR','kakeraW','kakeraL']
desiredSeries = ['One Piece', 'Dragon Ball Z', 'Death Note']
wishlist = ['Monkey D. Luffy', 'Roronoa Zoro', 'Nami']

# Smart Features
marryLastRoll = True      # Marry highest power card on last roll
divorceLastRoll = False   # Divorce after marry on last roll
pokeRoll = True           # Roll Pokeslot
claimDk = True            # Auto claim $dk/$daily
runImmediately = True     # Run on bot start

# Scheduling
snooze = True             # Enable snooze mode
repeatMinute = '06'       # Start of time window
repeatBetween = '20'      # End of time window (random execution)

# Snooze hours (24h format)
snoozeBegin = '01'        # 1 AM
snoozeEnd = '08'          # 8 AM
```

##### Understanding the new features

**1. Multi-Language Support:**
The bot now supports Portuguese (Brazil) and English. Set `language = 'pt_BR'` or `language = 'en'` to choose your preferred language. All bot messages and logs will be displayed in the selected language.

**2. Mode System (all vs self):**
You can now control whether the bot should react to all messages in the channel or only to your own rolls:
- `'all'` - Bot will react to any eligible message in the channel (good for claiming from other users)
- `'self'` - Bot will only react to messages from your own rolls (safer, avoids "stealing")

**3. marryLastRoll Feature:**
When enabled, if you're on your last roll opportunity (claim resets in less than 1 hour) and haven't claimed anything, the bot will automatically marry the highest power card from your rolls. This prevents wasting claim opportunities.

**4. divorceLastRoll Feature:**
Works together with `marryLastRoll`. After marrying the highest power card, the bot will automatically divorce it, freeing your harem slot. Useful if you only want to collect kakera and not keep low-priority cards.

**5. Random Scheduling:**
Instead of rolling at the exact same minute every hour, you can set `repeatBetween` to create a time window. For example:
- `repeatMinute = '06'` and `repeatBetween = '20'` means the bot will roll at a random minute between XX:06 and XX:20 each hour
- This makes the bot behavior more human-like

**6. Snooze Mode:**
Perfect for when you're sleeping or away. The bot will skip executions during the specified hours:
- `snoozeBegin = '01'` and `snoozeEnd = '08'` means no rolls between 1 AM and 8 AM
- Useful to save rolls for when you're active or to avoid suspicious 24/7 activity

**7. Wishlist System:**
In addition to `desiredSeries`, you can now specify exact character names in the `wishlist` array. The bot will prioritize claiming these characters over series-based claims.

**8. Minimum Card Power:**
Set `minCardPower` to automatically claim any card above a certain power level, regardless of series. Useful for claiming high-value cards you might want to trade later.
##### Execution
![image](https://github.com/GuilleDiazFentanes/AutoClaim-AutoRoll-AutoReact-MudaeBot-2023/assets/152492889/b39973db-35b7-4de4-a111-95c40de5c04d)

Once you have completed all the previous steps, you will be able to safely execute Bot.py
This will open the file and start the Bot, logging all the rolls and actions made. The console should look like the image.

**Console Output Symbols:**
- ❤️ (Red heart) → Already claimed cards
- 🤍 (White heart) → Not claimed yet cards
- 💎 (Diamond) → Kakera reactions

**What happens on startup:**
1. Bot displays current configuration (modes, language, scheduling)
2. If `runImmediately = True`, performs first roll right away
3. Schedules next roll according to `repeatMinute` and `repeatBetween` settings
4. Starts watching for new messages in the channel (for `'all'` modes)

**Scheduling Examples:**
- Fixed schedule: "Execução fixa: a cada hora no minuto 25" (rolls at XX:25 every hour)
- Random schedule: "Execução aleatória: entre XX:06 e XX:20" (rolls at random minute between XX:06-XX:20)
- Next execution: "Próxima execução agendada para: XX:15" (next roll at XX:15)

## Possible Errors
- Mudae has no access/write/read permission to the channel you decided
- Your Discord Token may have changed or expired
- Your Mudae settings always have a button on each character roll
- Series and Characters are **case-sensitive** (must match exactly)
- Your account must have a DM (at any time) with the mudae bot (try $help to make sure)
- `userId` must be filled correctly for the bot to work properly
- If using `'all'` modes, make sure you want to react to other users' rolls
- Invalid kakera names in `desiredKakeras` array (check spelling and capitalization)
- Snooze hours must be in 24h format as strings (e.g., `'01'`, `'08'`, `'23'`)
- If bot is not reacting to kakera, check if buttons are enabled in your Mudae settings

## Troubleshooting

**Bot is not claiming cards:**
1. Check if you have available claims ($tu command)
2. Verify `desiredSeries`, `wishlist`, or `minCardPower` settings
3. Ensure mode settings match your intent (`'all'` vs `'self'`)
4. Check if card names/series are spelled correctly (case-sensitive)

**Bot is not reacting to kakera:**
1. Verify kakera names in `desiredKakeras` are correct and case-sensitive
2. Check `desiredKakerasMode` setting
3. Make sure Mudae displays kakera as buttons, not emoji reactions

**Bot stops working after some time:**
1. Your Discord token may have expired - get a new one
2. Check if you were rate-limited by Discord (too many requests)
3. Verify your internet connection is stable

**marryLastRoll is not working:**
1. Check if your claim cooldown is less than 1 hour when rolling
2. Ensure at least one unclaimed card was rolled
3. Verify you have an available marry slot

## What's New in 2025 Version

### Major Features Added:
1. **Multi-language Support (i18n)**: Full support for Portuguese (PT-BR) and English (EN)
2. **Mode System**: Choose between `'all'` (react to all channel messages) or `'self'` (only your rolls)
3. **Wishlist System**: Specify exact character names for priority claiming
4. **Minimum Power Claiming**: Auto-claim cards above a certain power level
5. **Smart Marry**: Automatically marry highest power card on last roll opportunity
6. **Auto Divorce**: Optionally divorce after marrying to free harem slots
7. **Auto DK/Daily**: Automatically execute $dk and $daily commands when available
8. **Random Scheduling**: Roll at random minutes within a time window (more human-like)
9. **Snooze Mode**: Pause bot activity during specific hours
10. **Run Immediately**: Option to execute first roll on bot startup
11. **Anti-Steal Protection**: Built-in delay when claiming from other users' rolls
12. **Enhanced Error Handling**: Better detection and recovery from invalid messages
13. **User Status Checking**: Automatic verification of rolls remaining and claim availability
14. **Real-time Message Watching**: Bot monitors channel continuously for new cards

### Technical Improvements:
- Refactored code into modular functions
- Improved error recovery with retry mechanism
- Better regex patterns for parsing Mudae responses
- Support for both PT-BR and EN Mudae bot responses
- Gateway-based real-time message monitoring
- Automatic detection of roll owner to prevent stealing
- Optional debugging support (compatible with icecream if installed)

## Advanced Bot

Many advanced features are already included in this version! Here's what's currently implemented:

### ✅ Currently Available Features:
- ✅ **Desired Characters**: AutoClaim exact characters through the `wishlist` array
- ✅ **Optimized Kakera react**: Supports all kakera types with button-based reactions
- ✅ **Optimized claiming**: Claims based on wishlist → desired series → minimum power priority
- ✅ **Optimized $dk use**: Bot automatically claims $dk and $daily when available
- ✅ **marryLastRoll**: Automatically uses available claim on highest power card
- ✅ **Multi-Bot Ready**: Code structure supports multiple accounts (advanced users can adapt)
- ✅ **Anti-Steal Protection**: Built-in delay system when claiming from other users

### 🚀 Potential Future Features:
- **Enhanced Kakera Algorithm**: Advanced priority system based on kakera value
- **Automatic $rt use**: Smart usage of the $rt command when no claims available
- **Automatic $rolls management**: Optimal usage of accumulated rolls
- **Multi-Account Manager**: Built-in support for running multiple Discord accounts simultaneously
- **Web Dashboard**: Monitor and control the bot through a web interface
- **Statistics Tracking**: Track claimed cards, kakera collected, and success rates
- **Auto-Trade System**: Automatically trade duplicate or low-priority cards

Want to contribute or suggest features? Open an issue on GitHub!

## Version Comparison

| Feature | Original | Current |
|---------|---------------|--------------|
| Auto Roll | ✅ | ✅ |
| Auto Claim by Series | ✅ | ✅ |
| Auto React Kakera | ✅ | ✅ |
| Slash Commands Support | ✅ | ✅ |
| Multi-language Support | ❌ | ✅ |
| Wishlist System | ❌ | ✅ |
| Minimum Power Claiming | ❌ | ✅ |
| Mode System (all/self) | ❌ | ✅ |
| Smart Marry Feature | ❌ | ✅ |
| Auto Divorce | ❌ | ✅ |
| Auto DK/Daily | ❌ | ✅ |
| Random Scheduling | ❌ | ✅ |
| Snooze Mode | ❌ | ✅ |
| Run Immediately | ❌ | ✅ |
| Anti-Steal Protection | ❌ | ✅ |
| Real-time Monitoring | ❌ | ✅ |
| User Status Check | ❌ | ✅ |

## Contributing

Contributions are welcome! If you have ideas for new features or improvements, please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Disclaimer

This bot is for educational purposes only. Using self-bots is against Discord's Terms of Service. Use at your own risk. The authors are not responsible for any bans or restrictions on your Discord account.

## Credits

- **Original Creator**: GDiazFentanes
- **Contributor**: Samuelson Pajeu
- **Libraries**: discum, schedule

## License

This project is open source and available for personal use and modification.


