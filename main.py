import json
from flask import * 
import sqlite3 as db
import yaml

with open("config-api.yaml", "r") as stream:
    try:
        config_bet = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

app = Flask(__name__)

@app.route('/getDeployedContracts/',methods=['GET']) # http://127.0.0.1:7777/getDeployedContracts/?return=[address/match_id/league_id]
def getDeployedContract():
    try :
        ret = str(request.args.get('return')) # /getDeployedContracts/?return=[address/match_id]
        connection = db.connect(config_bet["databasePath"])
        cursor = connection.cursor()
        req = cursor.execute(f'SELECT {ret} FROM match WHERE isDeployed = ?',(1,))
        deployementNeeded  = req.fetchall()
        data = {'contractDeployed': [x[0] for x in deployementNeeded]}
    except Exception as e :
        print("Error /getDeployedContracts/ :",e)
        data = {'Error': e}
    finally :
        connection.close()
        return(json.dumps(data))



@app.route('/getMatchDataWithAddress/',methods=['GET']) # http://127.0.0.1:7777/getMatchDataWithAddress/?address=0xE06fc0711Da91027d7d07B10288f08702d6B604E
def getMatchDataWithAddress():
    try :
        query = str(request.args.get('address')) # /getMatchDataWithAddress/?address=addr
        connection = db.connect(config_bet["databasePath"])
        cursor = connection.cursor()
        req = cursor.execute('SELECT * FROM match WHERE address = ?', (query,))
        matchData = req.fetchall()
        print(matchData)
        data = {
                    "match_id": matchData[0][0],
                    "date": matchData[0][1],
                    "status": matchData[0][2],
                    "league_id": matchData[0][3],
                    "league_string": matchData[0][4],
                    "home_id": matchData[0][5],
                    "home_string": matchData[0][6],
                    "home_logo": matchData[0][7],
                    "away_id": matchData[0][8],
                    "away_string": matchData[0][9],
                    "away_logo": matchData[0][10],
                    "isDeployed": matchData[0][11],
                    "address": matchData[0][12]
                }
    except Exception as e :
        print("Error /getMatchDataWithAddress/ :",e)
        data = {'Error': e}
    finally :
        connection.close()
        return(json.dumps(data))

@app.route('/getMatchDataWithMatchId/',methods=['GET']) # http://127.0.0.1:7777/getMatchDataWithMatchId/?match_id=418874
def getMatchDataWithMatchId():
    try :
        query = str(request.args.get('match_id')) # /getMatchDataWithMatchId/?match_id=ID 
        connection = db.connect(config_bet["databasePath"])
        cursor = connection.cursor()
        req = cursor.execute('SELECT * FROM match WHERE match_id = ?', (query,))
        matchData = req.fetchall()
        print(matchData)
        data = {
                    "match_id": matchData[0][0],
                    "date": matchData[0][1],
                    "status": matchData[0][2],
                    "league_id": matchData[0][3],
                    "league_string": matchData[0][4],
                    "home_id": matchData[0][5],
                    "home_string": matchData[0][6],
                    "home_logo": matchData[0][7],
                    "away_id": matchData[0][8],
                    "away_string": matchData[0][9],
                    "away_logo": matchData[0][10],
                    "isDeployed": matchData[0][11],
                    "address": matchData[0][12]
                }
    except Exception as e :
        print("Error /getMatchDataWithMatchId/ :",e)
        data = {'Error': e}
    finally :
        connection.close()
        return(json.dumps(data))



if __name__ == "__main__":
    app.run(port=7777)