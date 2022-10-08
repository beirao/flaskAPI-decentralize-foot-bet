import json
import sqlite3 as db
import yaml, os
import logging, time


now_timestamp = int(time.time())
treeHours = 3*60*60 
dbPath = "ext/matches.db"
rmpArray = [('390101', now_timestamp + 2*treeHours, 'TIMED', '2013', 'Campeonato Brasileiro Série A', '1783', 'CR Flamengo', 'https://crests.football-data.org/1783.png', '-1', '6684', 'SC Internacional', 'https://crests.football-data.org/6684.svg', '-1', '1', '0x71109969f4B56d8d7422F31cF8c0812F76392010'), 
            ('390103', now_timestamp + treeHours, 'TIMED', '2013', 'Campeonato Brasileiro Série A', '1769', 'SE Palmeiras', 'https://crests.football-data.org/1769.png', '-1', '4241', 'Coritiba FBC', 'https://crests.football-data.org/4241.svg', '-1', '1', '0x'),
            ('390110', now_timestamp - 1*treeHours, 'TIMED', '2013', 'Campeonato Brasileiro Série A', '1838', 'América FC', 'https://crests.football-data.org/1838.png', '-1', '1776', 'São Paulo FC', 'https://crests.football-data.org/1776.svg', '-1', '1', '0x71109969f4B56d8d7422F31cF8c0812F76392010'),
            ('390100', now_timestamp - 2*treeHours, 'TIMED', '2013', 'Campeonato Brasileiro Série A', '1775', 'Avaí FC', 'https://crests.football-data.org/1775.png', '-1', '1770', 'Botafogo FR', 'https://crests.football-data.org/1770.svg', '-1', '1', '0x71109969f4B56d8d7422F31cF8c0812F76392010'),
            ('390107', now_timestamp - 4*treeHours, 'TIMED', '2013', 'Campeonato Brasileiro Série A', '1769', 'SE Palmeiras', 'https://crests.football-data.org/1769.png', '1', '4241', 'Coritiba FBC', 'https://crests.football-data.org/4241.svg', '2', '2', '0x71109969f4B56d8d7422F31cF8c0812F76392010'),
            ('390111', now_timestamp - 5*treeHours, 'TIMED', '2013', 'Campeonato Brasileiro Série A', '1838', 'América FC', 'https://crests.football-data.org/1838.png', '4', '1776', 'São Paulo FC', 'https://crests.football-data.org/1776.svg', '3', '2', '0x71109969f4B56d8d7422F31cF8c0812F76392010')]

def main() :
    connection = db.connect(dbPath)
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS matches
                    ("match_id" INTEGER UNIQUE,
                        "date" INTEGER,
                        "status" TEXT,
                        "league_id" INTEGER,
                        "league_string" TEXT,
                        "home_id" INTEGER NOT NULL,
                        "home_string" TEXT NOT NULL,
                        "home_logo" TEXT,
                        "home_score" INTEGER,
                        "away_id" INTEGER NOT NULL,
                        "away_string" TEXT NOT NULL,
                        "away_logo" TEXT,
                        "away_score" INTEGER,
                        "isDeployed" INTEGER,
                        "address" TEXT,
                        PRIMARY KEY("match_id"))''')
    
    for match_api in rmpArray :
        req = f"INSERT INTO matches VALUES {tuple(match_api)};"
        cursor.execute(req)
        print("DB updated, matches ID: ", match_api[0])

        connection.commit()

if __name__ == "__main__":
    os.system(f"rm {dbPath}")
    main()