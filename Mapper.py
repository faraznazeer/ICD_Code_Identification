from Database import Database

class Mapper:

    def __init__(self):
        self.database = Database()
        self.data = None
        self.query = 'SELECT code,diagnosis FROM ICD_data'
        self.icd = []
        self.data = []
        self.final_icd = []
        self.final_data = []
        self.special = ["unspecified", "others", "other","disease","diseases"]
        

    def search(self, keyword, icd, data ):


        self.final_data = []
        self.final_icd = []

        for i in range( len(data) ):
            if keyword in data[i]:
                self.final_data.append( data[i] )
                self.final_icd.append( icd[i] )

        if ( self.final_icd  ):
            return True
        else:
            return False


    def checkForSpecial(self, disease, icd, data):

        self.final_data = []
        self.final_icd = []

        keyword = disease.split(' ')

        for i in range( len(data) ):
            if( len(set(data[i]) & set(self.special)) > 0 ):
                if (len(data[i]) == len(keyword) + ( len( set(data[i] )&set(self.special) ) ) ):
                    self.final_data.append( data[i] )
                    self.final_icd.append( icd[i] )


       
        return len(self.final_icd)


    ''' INPUT : List of diagnosis
        OUTPUT : List of mapped ICD Codes in order with Diagnosis    '''

    def map(self, diagnosis):
        
        self.database.connect('localhost', 'root', 'zaraf', 'ICD')
        codes = []
        for item in diagnosis:

            #word = self.processitem(item)
            data_element = self.database.fetch_data(self.query, None)

            self.icd = [ x[0] for x in data_element]
            self.data = [ x[1].split(' ') for x in data_element]
            
            self.final_icd = self.icd
            self.final_data = self.data

            for keyword in item.split(' '):
                if( self.search( keyword , self.final_icd, self.final_data) ):
                    print(self.final_data)


            if( len( self.final_icd ) == 1):
                #print(self.final_icd)
                codes.append(self.final_icd)
            elif( len( self.final_icd) > 1 ):
                count = self.checkForSpecial(item, self.final_icd, self.final_data)
                if( count == 1 ):
                    #print( self.final_icd )
                    codes.append(self.final_icd)
                else:
                    print('Error : Ambiguous')
                    codes.append('ERROR(Ambiguous)')
            else:
                codes.append('ERROR(invalid keyword)')

        return codes
        #print(final_data)



ma = Mapper()

code = ma.map(['anemia','mumps polyneuropathy','ross river','plasmodium malariae malaria nephropathy'])
print(code)

