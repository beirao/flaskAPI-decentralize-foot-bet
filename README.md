# Flask API for [frontend-decentralize-foot-bet](https://github.com/beirao/frontend-decentralize-foot-bet)

This Flask app implement [Gunicorn](https://gunicorn.org/) as WSGI server

### Launch the API with this command :

```bash
gunicorn -c gunicorn_config.py "main:app"
```

## All GET requests

### Get all deployed contract

```url
http://0.0.0.0:8080/getDeployedContracts/?return=RET
```

return can be : address, match_id, league_id, league_string, date...

### Get match data with its address

```url
http://0.0.0.0:8080/getMatchDataWithAddress/?address=ADDR
```

### Get match data with its ID

```url
http://0.0.0.0:8080/getMatchDataWithMatchId/?match_id=ID
```

### Get all active bet

```url
http://0.0.0.0:8080/getAllActiveBet/
```

### Get all processing bet

```url
http://0.0.0.0:8080/getAllProcessingBet/
```

### Get all ended bet

```url
http://0.0.0.0:8080/getAllEndedBet/
```

### Get all recent ended betget

```url
http://0.0.0.0:8080/AllRecentEndedBet/
```

## The Database

Need a sql database as describe in the [autoDeployment-decentralize-foot-bet](https://github.com/beirao/autoDeployment-decentralize-foot-bet) repository.

Specify the data base path in the **config-api.yaml**

# Docker

## Build

```bash
sudo docker build -t api-foot-boarbet .
```

## Run image

```bash
sudo docker run -p 8080:8080 -d -v $dst:$src api-foot-boarbet
```

## Save the image

```bash
sudo docker save -o api-foot-boarbet.tar api-foot-boarbet
```
