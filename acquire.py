#######IMPORTS

import pandas as pd
import os
import env



#######FUNCTIONS

def get_connection_url(db, username=env.username, host=env.host, password=env.password):
    """
    This function will:
    - take username, pswd, host credentials from imported env module
    - output a formatted connection_url to access mySQL db
    """
    return f'mysql+pymysql://{username}:{password}@{host}/{db}'



def new_titanic_data(SQL_query):
    """
    This function will:
    - take in a SQL_query
    - create a connection_url to mySQL
    - return a df of the given query from the titanic_db
    """
    url = get_connection_url('titanic_db')
    
    return pd.read_sql(SQL_query, url)



def get_titanic_data(SQL_query, directory, filename = 'titanic.csv'):
    """
    This function will:
    - Check local directory for csv file
        - return if exists
    - if csv doesn't exist:
        - creates df of sql query
        - writes df to csv
    - outputs titanic df
    """
    if os.path.exists(directory+filename): 
        df = pd.read_csv(filename)
        return df
    else:
        df = new_titanic_data(SQL_query)

        df.to_csv(filename)
        return df
    
    
    
    
def new_iris_data(SQL_query):
    """
    This function will:
    - take in a SQL_query
    - create a connection_url to mySQL
    - return a df of the given query from the iris_db
    """
    url = get_connection_url('iris_db')
    
    return pd.read_sql(SQL_query, url)


def get_iris_data(SQL_query, directory, filename = 'iris.csv'):
    """
    This function will:
    - Check local directory for csv file
        - return if exists
    - if csv doesn't exist:
        - creates df of sql query
        - writes df to csv: defaulted to iris.csv
    - outputs iris df
    """
    if os.path.exists(directory+filename): 
        df = pd.read_csv(filename)
        return df
    else:
        df = new_iris_data(SQL_query)

        df.to_csv(filename)
        return df

    
    
    
def new_telco_data(SQL_query):
    """
    This function will:
    - take in a SQL_query
    - create a connection_url to mySQL
    - return a df of the given query from the telco_db
    """
    url = get_connection_url('telco_churn')
    
    return pd.read_sql(SQL_query, url)



def get_telco_data(SQL_query, directory, filename = 'telco.csv'):
    """
    This function will:
    - Check local directory for csv file
        - return if exists
    - if csv doesn't exist:
        - creates df of sql query
        - writes df to csv: defaulted to telco.csv
    - outputs iris df
    """
    if os.path.exists(directory+filename): 
        df = pd.read_csv(filename)
        return df
    else:
        df = new_telco_data(SQL_query)

        df.to_csv(filename)
        return df
    
    
    
    
