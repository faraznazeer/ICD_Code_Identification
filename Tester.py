from Database import Database
from Preprocessor import Preprocessor

database_object = Database()
data_object = Preprocessor()
value = []

def insert_data():
    
    (icd, diagnosis) = data_object.get_full_data()
    query = "UPDATE ICD_data SET diagnosis = %s WHERE code = %s "
   
    for i in range( len(icd) ): 
        value.append( ( ' '.join(diagnosis[i]) , icd[i] ) ) 

    database_object.insert_many( query, value  )



def fetch_data():

    query = " SELECT * FROM ICD_data WHERE diagnosis LIKE %s AND diagnosis LIKE %s"
    value = ('%anemia%', '%unspecified%')
    print ( x for x in database_object.fetch_data(query, value) )





if __name__ == '__main__':

    database_object.connect('localhost', 'root', 'zaraf', 'ICD')
    insert_data()