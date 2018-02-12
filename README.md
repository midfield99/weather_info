Status
=====
Travis-CI: [![Build Status](https://travis-ci.org/midfield99/weather_info.png)](https://travis-ci.org/midfield99/weather_info)

Set Up
=====
This program was developed with Python 3.6

Create this file the root directory:
`config.sh`:
```
#!/bin/bash
#config file to set up configuration details
#Run source config.sh to set environmental config variables.
export OWM_API_KEY="FAKE_KEY"
export OWM_BASE_URL="http://api.openweathermap.org/data/2.5/"
```

Replace default key in `config.sh` with your Open Weather Map API Key

Usage
=====
Run `source config.sh` to set environmental config variables.

`python main_unit_tests.py` will run unit tests.

`python main.py` will run the main program.
