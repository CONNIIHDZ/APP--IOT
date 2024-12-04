import pymongo
from pymongo.errors import ConnectionFailure

class DB:
    
    def __init__(self, tabla, bd = "PHYTONMONGO", url= "mongodb://localhost:27017/" ):
        self.client = pymongo.MongoClient(url)
        self.db = self.client[bd]
        self.collection = self.db[tabla]
        
  
    def insertDoc(self, data):
        
         if isinstance(data, dict):
            result = self.collection.insert_one(data)
            return result.inserted_id
         elif isinstance(data, list) and all(isinstance(item, dict) for item in data):
            result = self.collection.insert_many(data)
            return result.inserted_ids
         else:
            raise ValueError("El dato debe ser un diccionario o una lista de diccionarios")
        
    def findDoc(self, query={}):
        """Lee documentos de la colección según un criterio de búsqueda (query)."""
        results = self.collection.find(query)
        return list(results)
    
    def deleteAllDocs(self):
        """Elimina todos los documentos de la colección."""
        result = self.collection.delete_many({})
        return result.deleted_count
    
    def update(self, query, data):
        query = {"curp": query} 
        data = {"$set": data}
        self.collection.update_one(query, data)
        
   
    def ping(self):
        try:
            # Realiza un comando 'ping' para verificar la conexión
            self.client.CRUD.command('ping')
            print("Conexión exitosa a MongoDB.")
            return True
        except ConnectionFailure:
            print("Error: No se pudo conectar a MongoDB.")
            return False
        
if __name__ == "__main__":
    
    x=DB("Alumnos")
    print(x.ping())
    