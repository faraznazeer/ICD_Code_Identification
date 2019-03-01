from Database import Database
from Preprocessor import Preprocessor
from Mapper import Mapper
from collections import defaultdict

dictionary1 = defaultdict(list)
dictionary2 = defaultdict(list)
database_object = Database()
data_object = Preprocessor()
mapper = Mapper()

value = []
query = " SELECT * FROM ICD_data WHERE diagnosis LIKE %s AND diagnosis LIKE %s"
query1 = "UPDATE ICD_data SET diagnosis = %s WHERE code = %s "
query2 = 'SELECT code,diagnosis FROM ICD_data'

def update_data():
    
    (icd, diagnosis) = data_object.get_full_data()
   
    for i in range( len(icd) ): 
        value.append( ( ' '.join(diagnosis[i]) , icd[i] ) ) 

    database_object.insert_many( query, value  )

'''
def fetch_data():   
    value = ('%anemia%', '%unspecified%')
    print ( x for x in database_object.fetch_data(query, value) )

'''

def map_data(diagnosis):

    data = database_object.fetch_data(query2, None)
    
    for disease in diagnosis:

        for item in data:
            icds = list(item)

            if( disease in icds[1].split(' ') ):
                dictionary1[disease].append(icds[0])
                dictionary2[disease].append(icds[1])

        print(disease+"\n")
        if ( disease.find(' ') == -1):
            for i in range(len(dictionary1[disease])):
                
                if 'unspecified' in dictionary2[disease][i].split(' ') and len(dictionary2[disease][i].split(' ')) == 2:
                    print (dictionary1[disease][i]+"\n")

   # print(dictionary)   

if __name__ == '__main__':

    database_object.connect('localhost', 'root', 'zaraf', 'ICD')
    #fetch_data()

    diagnosis1 = ['Anemia']
    #diagnosis2 = ['']
    map_data(diagnosis1 )
    
