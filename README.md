# heroku_pinger
Pings Heroku dynos to keep them from falling asleep

## Installation
Fork this repository and create a Heroku application. PING_URL environment variable must be set on this heroku application
```
pip install -r requirements.txt
git push heroku master
git config:set PING_URL=<URL of your dyno>
```

Default time set to 28 minutes since dynos power down after 30 minutes, you can change this in clock.py

## TODO:
Add capability to ping multiple applications
