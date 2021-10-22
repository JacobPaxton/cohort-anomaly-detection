import pandas as pd
import re
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

# ---------------- wrangle script ---------------- #
def wrangle_cohorts(show=False):
    """ returns dataframe of curriculum_logs, 
        reads local csv if it can or pulls from Codeup's database if it can't """
    # run, store query if file not found locally
    if not os.path.isfile('cohort_logs.csv'):
        # build query
        url = url_grab()
        query = """ SELECT date, time, path, user_id, ip, 
                    name as cohort, start_date, end_date, program_id
                    FROM logs 
                    JOIN cohorts ON logs.cohort_id = cohorts.id """
        # run query
        df = pd.read_sql(query, url)
        # push dataframe to csv
        df.to_csv('cohort_logs.csv')
    # read file if found locally
    else:
        # read local file
        df = pd.read_csv('cohort_logs.csv', index_col=0)
    # anonymize ip addresses
    # df = anonymize_ips(df)
    # add program information
    df = add_program_info(df)
    # fix path column
    df['path'] = df['path'].astype('str')
    # set datetime index
    df['datetime'] = pd.to_datetime(df['date'].astype('str') + " " + df['time'])
    df.index = df.datetime
    df.drop(columns='datetime', inplace=True)
    # print head, return df
    if show == True:
        print(df.head(10))
    return df

# ---------------- prepare functions ---------------- #
# def anonymize_ips(df):
#     ips = []
#     for ip in df['ip']:
#         anonymous_ip = re.findall(r'.*\..*\.*\.', ip)[0] + 'xxx'
#         ips.append(anonymous_ip)
#     df['ip'] = ips
#     return df

def add_program_info(df):
    """ add columns for program information """
    # create program list
    program_list = ['PHP Full Stack Web Development',
                    'Java Full Stack Web Development',
                    'Data Science',
                    'Front End Web Development']
    # create dataframe for program information and keys
    programs = pd.DataFrame({'program_id':[1,2,3,4], 
                             'program_name':program_list,
                             'subdomain':['php','java','ds','fe']})
    # set index to key
    programs = programs.set_index('program_id')
    # merge program information into dataframe
    df = pd.merge(left=df, right=programs, on='program_id')

    return df

def lesson_identification(df):
    """ uses a lot of masks to try to identify lessons based on path requests """
    # directory-based filters
    not_fwdslash = df.path != '/' # ignore values of just a slash
    has_subdirectory = df.path.str.contains('/') # make sure all values have a slash
    not_search = ~df.path.str.contains('search_index', na=False) # ignore index searches
    not_examples = ~df.path.str.contains('examples', na=False) # ignore examples folders
    # filtering out images
    not_images_sub = ~df.path.str.contains('images', na=False) # ignore images folders
    not_jpg = ~df.path.str.contains('.jpg', na=False) # ignore pics outside images folders
    not_jpeg = ~df.path.str.contains('.jpeg', na=False) # ignore pics
    not_svg = ~df.path.str.contains('.svg', na=False) # ignore pics
    not_gif = ~df.path.str.contains('.gif', na=False) # ignore pics
    not_ico = ~df.path.str.contains('.ico', na=False) # ignore pics
    not_png = ~df.path.str.contains('.png', na=False) # ignore pics
    # combine non-image masks
    not_weirdness = (not_fwdslash & has_subdirectory & not_search & not_examples)
    # combine image masks
    not_pictures = (not_jpg & not_jpeg & not_svg & not_images_sub & not_gif & not_ico & not_png)
    # new column regarding above masks
    df['is_lesson'] = not_weirdness & not_pictures 

    return df

def html_php_requests(df):
    """ new columns showing path requests that end in html or php """
    # new columns regarding certain requests
    df['html_request'] = df['path'].str.endswith('.html', na=False) # mark html requests
    df['php_request'] = df['path'].str.endswith('.php', na=False) # mark php requests

    return df

def alter_paths(df):
    """ add new column having dropped '.html' and '.php' from paths having them """
    paths = []
    for path in df.path: # going through all paths
        if path[-5:] == '.html':
            path = path[:-5] # delete .html
        if path[-4:] == 'php':
            path = path[:-4] # delete .php
        paths.append(path) # append all paths back
    df['alter_path'] = paths # new column containing all paths

    return df