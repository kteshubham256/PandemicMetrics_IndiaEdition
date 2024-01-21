from sqlalchemy import create_engine
import pandas as pd
import os

def sqlConnection(TableOne,TableTwo):
    # creating connection to sql and creating a engine
    database_url = 'mysql+mysqlconnector://root:@localhost/Covid19'
    engine = create_engine(database_url)
    
    # inserting tableOne and TableTwo in database
    TableOne.to_sql('tableone', con=engine, index=False, if_exists='replace')
    

    # for rows insertion we are using batch processing
    chunk_size = 1000  # Adjust the batch size based on your dataset
    num_rows = len(TableTwo)

    print(num_rows)
    for i in range(0, num_rows, chunk_size):
        chunk = TableTwo[i:i + chunk_size]
        chunk.to_sql("tabletwo", con=engine, index=False, if_exists='append')
        
    # SQL query
    query = "select state_code,year(dates) as _year,monthname(dates)as _month,CEIL(DAYOFMONTH(dates) / 7) AS _week, sum(state_total_confirmed),sum(state_total_deceased),sum(state_total_recovered),sum(state_total_tested) from tabletwo t1 join tableone t2 on t1.state_code = t2.state group by state,_year,_month,_week;"

    #  Execute the query
    with engine.connect() as connection:
        cursor = connection.connection.cursor()
        cursor.execute(query)       # executing the query
        rows = cursor.fetchall()              # fetching the data and getting all rows
        columns = [column[0] for column in cursor.description]  # reading columns

    # creating dataframe of sqlQuery table
    sqlWeekTable = pd.DataFrame(rows, columns=columns)
    
    # Close the connection
    engine.dispose()
    
    
    # Create the directory if it doesn't exist
    os.makedirs("ExcelFiles", exist_ok=True)

    # creating a excel file
    TableOne.to_excel(os.path.join("ExcelFiles", 'TableOne.xlsx'),index=False)
    TableTwo.to_excel(os.path.join("ExcelFiles", 'TableTwo.xlsx'),index=False)
    sqlWeekTable.to_excel(os.path.join("ExcelFiles", 'sqlWeekTable.xlsx'),index=False)
        