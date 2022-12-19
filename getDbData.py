
from connection import Dbconnector

class GetDbData:
    
    @classmethod
    def getAllActors(cls):
        all_actors = "SELECT * FROM Actor"
        results = Dbconnector.executeQuery(all_actors)
        Dbconnector.close()
        return results
    
    @classmethod
    def getAllFilms(cls):
        all_films = "SELECT * FROM Film"
        results = Dbconnector.executeQuery(all_films)
        Dbconnector.close()
        return results
    
    