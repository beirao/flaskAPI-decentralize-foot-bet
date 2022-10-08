import json
from flask import *
from flask_cors import CORS 
import sqlite3 as db
import yaml
import logging, time

app = Flask(__name__)
CORS(app)

# def app():
with open("ext/config-api.yaml", "r") as stream:
    try:
        config_bet = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

logging.basicConfig(filename=config_bet["logPath"], level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s")


@app.route('/', methods=['GET']) # http://127.0.0.1:8000/
def main():
    logging.info("Main called")
    data = {"Working !" : 1}
    return(json.dumps(data))

@app.route('/getDeployedContracts/', methods=['GET']) # http://127.0.0.1:8000/getDeployedContracts/?return=[address/match_id/league_id]
def getDeployedContract():
    try :
        ret = str(request.args.get('return')) # /getDeployedContracts/?return=[address/match_id]
        logging.info(f"getDeployedContracts called : ret = {ret}")
        connection = db.connect(config_bet["databasePath"])
        cursor = connection.cursor()
        req = cursor.execute(f'SELECT {ret} FROM matches WHERE isDeployed = ?',(1,))
        deployementNeeded  = req.fetchall()
        data = {'contractDeployed': [x[0] for x in deployementNeeded]}
    except Exception as e :
        print("Error /getDeployedContracts/ :",e)
        logging.error(f"Error /getDeployedContracts/ : {e}")
        data = {'Error': e}
    finally :
        connection.close()
        return(json.dumps(data))

@app.route('/getMatchDataWithAddress/', methods=['GET']) # http://127.0.0.1:8000/getMatchDataWithAddress/?address=0xE06fc0711Da91027d7d07B10288f08702d6B604E
def getMatchDataWithAddress():
    try :
        query = str(request.args.get('address')) # /getMatchDataWithAddress/?address=addr
        logging.info(f"getMatchDataWithAddress called : address = {query}")
        connection = db.connect(config_bet["databasePath"])
        cursor = connection.cursor()
        req = cursor.execute('SELECT * FROM matches WHERE address = ?', (query,))
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
                    "home_score": matchData[0][8],
                    "away_id": matchData[0][9],
                    "away_string": matchData[0][10],
                    "away_logo": matchData[0][11],
                    "away_score": matchData[0][12],
                    "isDeployed": matchData[0][13],
                    "address": matchData[0][14]
                }
    except Exception as e :
        print("Error /getMatchDataWithAddress/ :",e)
        logging.error(f"Error /getMatchDataWithAddress/ : {e}")
        data = {'Error': e}
    finally :
        connection.close()
        return(json.dumps(data))

@app.route('/getMatchDataWithMatchId/', methods=['GET']) # http://127.0.0.1:8000/getMatchDataWithMatchId/?match_id=418874
def getMatchDataWithMatchId():
    try :
        query = str(request.args.get('match_id')) # /getMatchDataWithMatchId/?match_id=ID 
        logging.info(f"getMatchDataWithMatchId called : match_id = {query}")
        connection = db.connect(config_bet["databasePath"])
        cursor = connection.cursor()
        req = cursor.execute('SELECT * FROM matches WHERE match_id = ?', (query,))
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
                    "home_score": matchData[0][8],
                    "away_id": matchData[0][9],
                    "away_string": matchData[0][10],
                    "away_logo": matchData[0][11],
                    "away_score": matchData[0][12],
                    "isDeployed": matchData[0][13],
                    "address": matchData[0][14]
                }
    except Exception as e :
        print("Error /getMatchDataWithMatchId/ :",e)
        logging.error(f"Error /getMatchDataWithMatchId/ : {e}")            
        data = {'Error': e}
    finally :
        connection.close()
        return(json.dumps(data))

@app.route('/getAllActiveBet/', methods=['GET']) # http://127.0.0.1:8000/getAllActiveBet/
def getAllActiveBet():
    try :
        connection = db.connect(config_bet["databasePath"])
        cursor = connection.cursor()
        logging.info(f"getAllActiveBet called")
        now_timestamp = int(time.time())
        req = cursor.execute('SELECT * FROM matches WHERE date > ? AND isDeployed == ?', (now_timestamp, 1))
        matchData = req.fetchall()        
        data = json.loads("[]")
        for match in matchData : 
            dataElement = {
                        "match_id": match[0],
                        "date": match[1],
                        "status": match[2],
                        "league_id": match[3],
                        "league_string": match[4],
                        "home_id": match[5],
                        "home_string": match[6],
                        "home_logo": match[7],
                        "home_score": match[8],
                        "away_id": match[9],
                        "away_string": match[10],
                        "away_logo": match[11],
                        "away_score": match[12],
                        "isDeployed": match[13],
                        "address": match[14]
                    }
            data.append(dataElement)
    except Exception as e :
        print("Error /getAllActiveBet/ :",e)
        logging.error(f"Error /getAllActiveBet/ : {e}")
        data = {'Error': e}
    finally :
        connection.close()
        return(json.dumps(data))

@app.route('/getAllProcessingBet/', methods=['GET']) # http://127.0.0.1:8000/getAllProcessingBet/
def getAllProcessingBet():
    try :
        connection = db.connect(config_bet["databasePath"])
        cursor = connection.cursor()
        logging.info(f"getAllProcessingBet called")
        now_timestamp = int(time.time())
        req = cursor.execute('SELECT * FROM matches WHERE date < ? AND isDeployed == ?', (now_timestamp, 1))
        matchData = req.fetchall()        
        data = json.loads("[]")
        for match in matchData : 
            dataElement = {
                        "match_id": match[0],
                        "date": match[1],
                        "status": match[2],
                        "league_id": match[3],
                        "league_string": match[4],
                        "home_id": match[5],
                        "home_string": match[6],
                        "home_logo": match[7],
                        "home_score": match[8],
                        "away_id": match[9],
                        "away_string": match[10],
                        "away_logo": match[11],
                        "away_score": match[12],
                        "isDeployed": match[13],
                        "address": match[14]
                    }
            data.append(dataElement)
    except Exception as e :
        print("Error /getAllProcessingBet/ :",e)
        logging.error(f"Error /getAllProcessingBet/ : {e}")
        data = {'Error': e}
    finally :
        connection.close()
        return(json.dumps(data))


@app.route('/getAllEndedBet/', methods=['GET']) # http://127.0.0.1:8000/getAllEndedBet/
def getAllEndedBet():
    try :
        connection = db.connect(config_bet["databasePath"])
        cursor = connection.cursor()
        logging.info(f"getAllEndedBet called")
        persistenceTime_timestamp = int(time.time()) + config_bet["persistenceTimeEndedBet"] * 24 * 60 * 60
        req = cursor.execute('SELECT * FROM matches WHERE date < ? AND isDeployed == ?', (persistenceTime_timestamp, 2))
        matchData = req.fetchall()        
        data = json.loads("[]")
        for match in matchData : 
            dataElement = {
                        "match_id": match[0],
                        "date": match[1],
                        "status": match[2],
                        "league_id": match[3],
                        "league_string": match[4],
                        "home_id": match[5],
                        "home_string": match[6],
                        "home_logo": match[7],
                        "home_score": match[8],
                        "away_id": match[9],
                        "away_string": match[10],
                        "away_logo": match[11],
                        "away_score": match[12],
                        "isDeployed": match[13],
                        "address": match[14]
                    }
            data.append(dataElement)
    except Exception as e :
        print("Error /getAllEndedBet/ :",e)
        logging.error(f"Error /getAllEndedBet/ : {e}")
        data = {'Error': e}
    finally :
        connection.close()
        return(json.dumps(data))



if __name__ == "__main__":
    app.run()