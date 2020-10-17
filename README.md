# CREVIL-USERBOT

<p align="center">
<img src="https://telegra.ph/file/7801faba2f8fb880015bc.jpg" alt="FRIDAY USERBOT">


[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)



Best User Bot To Manage Your Telegram Account 
## Most PowerFul And Better And Secure

## © By [CrevilOfficial](http://t.me/crevilofficial)

### For any query or want to know how it works join Group And Channel 

<a href="https://t.me/CrevilOfficial"><img src="https://img.shields.io/badge/Join-Telegram%20Channel-red.svg?logo=Telegram"></a>
<a href="https://t.me/crevilSupport"><img src="https://img.shields.io/badge/Join-Telegram%20Group-blue.svg?logo=telegram"></a>

### Host Crevil In Heroku

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/crevils/crevilbot)



### The Normal Way

Simply clone the repository and run the main file:
```sh
git clone https://github.com/Crevils/crevilbot
cd crevilbot
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m userbot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```
## Support
Join [CrevilBot Support group](https://t.me/CrevilBotSupport) for updates and new plugin suggestions.
Do fork and star the repo 

### Session String 
<a href="https://crevilbotsession.crevil.repl.run/" target="_blank"><img src="https://img.shields.io/badge/run-string__session.py-red?style=for-the-badge&logo=repl.it" alt="generate_string" /></a>



### UniBorg Configuration

The UniBorg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.

## Credits 
```- Thanks To All Contributers For This Project 
- $ UserBot - @Crevil
- $ Some Bug Fixes - @okay_retard
