import pandas as pd
import os
import env

# ---------------- url creation for SQL query ---------------- #
def get_db_url_1(db_name, user=env.user, host=env.host, password=env.password):
    """ create URL for SQL query using user, host, password, and db_name """
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'

def get_db_url_2(db_name, username=env.username, host=env.host, password=env.password):
    """ create URL for SQL query using username, host, password, and db_name """
    return f'mysql+pymysql://{username}:{password}@{host}/{db_name}'

def get_db_url_3(db_name, username=env.username, hostname=env.hostname, password=env.password):
    """ create URL for SQL query using username, hostname, password, and db_name """
    return f'mysql+pymysql://{username}:{password}@{hostname}/{db_name}'

def url_grab():
    """ runs most common combinations of env credentials to generate a SQL URL """
    if env.user != None and env.host != None:
        url = get_db_url_1(db_name='curriculum_logs')
    elif env.username != None and env.host != None:
        url = get_db_url_2(db_name='curriculum_logs')
    elif env.username != None and env.hostname != None:
        url = get_db_url_3(db_name='curriculum_logs')
    else:
        print('env.py credentials must contain host/hostname, user/username, and password variable declarations.')
        return None
    return url

# ---------------- acquire script ---------------- #
def wrangle_cohorts(show=False):
    """ returns dataframe of curriculum_logs, 
        reads local csv if it can or pulls from Codeup's database if it can't """
    # run, store query if file not found locally
    if not os.path.isfile('cohort_logs.csv'):
        # build query
        url = url_grab()
        query = " SELECT * FROM logs JOIN cohorts ON logs.cohort_id = cohorts.id "
        # run query
        df = pd.read_sql(query, url)
        # set datetime index
        df['date'] = df['date'].astype('datetime64')
        df.index = df.date
        # push dataframe to csv
        df.to_csv('cohort_logs.csv')
    # read file if found locally
    else:
        # read local file
        df = pd.read_csv('cohort_logs.csv')
    # print head, return df
    if show == True:
        print(df.head(10))
    return df


