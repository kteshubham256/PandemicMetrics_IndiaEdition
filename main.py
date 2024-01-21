from readingJson.read import reading
from readingJson.scrappingjson import scrappingJson
from readingJson.CreatingDataframe import creatingDataframe
from Cleaning.clean import cleaningDataframe
from SqlConnection.connection import sqlConnection

def main():
    json_data_One,json_data_Two = scrappingJson()
    reading(json_data_One,json_data_Two)
    TableOneState,TableOneDistrict,TableTwo = creatingDataframe()
    TableOne,TableTwo = cleaningDataframe(TableOneState,TableOneDistrict,TableTwo)
    sqlConnection(TableOne,TableTwo)


if __name__ == "__main__":
    main()



    
    






