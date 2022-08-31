# FlaskAPI for [frontend-decentralize-foot-bet](https://github.com/beirao/frontend-decentralize-foot-bet)

## This Flask app implement [Gunicorn](https://gunicorn.org/) as WSGI server

### Launch the API with this command :

```bash
gunicorn -c gunicorn_config.py "main:app()"
```

## All GET requests

### Get all deployed contract

```url
http://127.0.0.1:8000/getDeployedContracts/?return=RET
```

return can be : address, match_id, league_id, league_string, date...

### Get match data with the its address

```url
http://127.0.0.1:8000/getMatchDataWithAddress/?address=ADDR
```

### Get match data with the its ID

```url
http://127.0.0.1:8000/getMatchDataWithMatchId/?match_id=ID
```

## The Database

Need a sql database as describe in the [autoDeployment-decentralize-foot-bet](https://github.com/beirao/autoDeployment-decentralize-foot-bet) repository.

Specify the data base path in the **config-api.yaml**
