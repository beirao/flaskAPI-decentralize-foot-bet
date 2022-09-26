# FlaskAPI for [frontend-decentralize-foot-bet](https://github.com/beirao/frontend-decentralize-foot-bet)

## This Flask app implement [Gunicorn](https://gunicorn.org/) as WSGI server

### Launch the API with this command :

```bash
gunicorn -c gunicorn_config.py "main:app()"
```

## All GET requests

### Get all deployed contract

```url
http://0.0.0.0:8080/getDeployedContracts/?return=RET
```

return can be : address, match_id, league_id, league_string, date...

### Get match data with the its address

```url
http://0.0.0.0:8080/getMatchDataWithAddress/?address=ADDR
```

### Get match data with the its ID

```url
http://0.0.0.0:8080/getMatchDataWithMatchId/?match_id=ID
```

## The Database

Need a sql database as describe in the [autoDeployment-decentralize-foot-bet](https://github.com/beirao/autoDeployment-decentralize-foot-bet) repository.

Specify the data base path in the **config-api.yaml**

# Docker

## Build

```bash
sudo docker build -t api-foot-boarbet .
```

## Create image

## Run image

```bash
sudo docker run -p 80:80 api-foot-boarbet

sudo docker run -p 80:80 -d --mount type=bind,src="$(pwd)/logs",dst=/logs api-foot-boarbet
```

## Save the image

```bash
sudo docker save -o api-foot-boarbet.tar api-foot-boarbet
```
