# SoundCloudBot
SoundCloud Bot to play target track by using selenium. Includes 50, 100, 500, 1000 runs script. 

## Dependency
```pip install -r requirements.txt```

## How to run
### Default run script for 1 run
```python sc_bot.py```
### Run script for a specific number of runs
```
python sc_bot.py <NUMBER>
e.g. python sc_bot.py 3 # Play default track for 3 times
```
### Run script for a specific number of runs and customized url.
```
python sc_bot.py <NUMBER> <URL>
e.g. python sc_bot.py 5 https://soundcloud.com/decentral-mike/basshead-mix # Play basshead-mix for 5 times
```

### Script for 50 runs
```
chmod 777 50_run.sh
./50_run.sh
```
### Script for 100 runs
```
chmod 777 100_run.sh
./100_run.sh
```
### Script for 500 runs
```
chmod 777 500_run.sh
./500_run.sh
```
### Script for 1000 runs
```
chmod 777 1000_run.sh
./1000_run.sh
```