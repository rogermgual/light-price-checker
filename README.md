# light-price-checker

## Purpose
Light price predictor, collecting data from public lihgt API, and realising a little predicor job in order to predict in which hours in the following 3 days the light price will reach its minimum and maximum price.
Also, can send some notification (fe via Telegram, Discord, etc) in order to notify.
***
## Deploy
Dockerfile will copy the necessary directories and will install the specified dependencies in the *requirements.txt* file.
Then, the +start.sh* shell script will be launched in order to execute the python script.
To build the image, run:
>`docker build -t light-price-checker-img .`

***
## Execution
Once the image is created, then run the container like:
>`docker run light-price-checker-img`

[TBD]