#Here is where the connection to the database is made and contains the logic for the SportsTracker DAO.

from config.pgconfig import hostname, database, username, pwd, port_id
import psycopg2

class PartDAO():
    def __init__(self):
        
        self.conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
        )
        
    def getAllChampionship(self):
        cursor = self.conn.cursor()
        query = "SELECT id, name, winner_team, winner_year FROM championships"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def createChampionShip(self, name, winner_team, winner_year):
        cursor = self.conn.cursor()
        query = "INSERT INTO championships (name, winner_team, winner_year) VALUES (%s, %s, %s) RETURNING id"
        cursor.execute(query, (name, winner_team, winner_year))
        championship_id = cursor.fetchone()[0]
        self.conn.commit()
        cursor.close()
        return championship_id
    
    def deleteChampionById(self, id):
        cursor = self.conn.cursor()
        pre_query = "SELECT 1 FROM championships WHERE id = %s"
        cursor.execute(pre_query, (id,))
        exists = cursor.fetchone()
        if exists:
            query = "DELETE FROM championships WHERE id = %s"
            cursor.execute(query, (id,))
            self.conn.commit()
            cursor.close()
            return True
        else:
            cursor.close()
            return False
        
        
    def updateChampionship(self, id, name, winner_team, winner_year):
        cursor = self.conn.cursor()
        pre_query = "SELECT 1 FROM championships WHERE id = %s"
        cursor.execute(pre_query, (id,))
        exists = cursor.fetchone()
        if exists:
            query = "UPDATE championships SET name = %s, winner_team = %s, winner_year = %s WHERE id = %s"
            cursor.execute(query, (name, winner_team, winner_year, id))
            self.conn.commit()
            cursor.close()
            return True
        else:
            cursor.close()
            return False
        
    def getChampionshipForUpdate(self, id):
        cursor = self.conn.cursor()
        query = "SELECT id, name, winner_team, winner_year FROM championships WHERE id = %s"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def getChampionshipById(self, id):
        cursor = self.conn.cursor()
        query = "SELECT id, name, winner_year, winner_team FROM championships WHERE id = %s" 
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def getWinnerTeamById(self, id):
        cursor = self.conn.cursor()
        
        getwinner_team_id_query = "select winner_team from championships where id = %s"
        cursor.execute(getwinner_team_id_query, (id,))
        winner_team_id = cursor.fetchone()
        
        query = "SELECT id, name FROM teams WHERE id = %s"
        cursor.execute(query, (winner_team_id,))
        result = cursor.fetchone()
        
        cursor.close()
        return result
        
        
        
    