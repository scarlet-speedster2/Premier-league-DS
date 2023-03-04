import datetime
import os

def get_current_season():
    now = datetime.datetime.now()
    # By July, fixture of the season should be available.
    new_season_start = datetime.datetime(now.year, 7, 1)
    return now.year if now > new_season_start else now.year - 1

CURRENT_YEAR = get_current_season()
CURRENT_FILE = '{}-{}.csv'.format(CURRENT_YEAR, CURRENT_YEAR + 1)

DATA_PATH = 'data'

RAW_DATA_FILE_PATH = 'data/raw/results'
OVA_FILE_PATH =      'data/raw/OVAs'

STANDINGS_PATH =             'data/cleaned/standings'
RAW_CLEANED_DATA_FILE_PATH = 'data/cleaned/results'

CLEANED_DATA_FILE_PATH = 'data/train_data/results'
FINAL_FILE =             'data/train_data/final.csv'
CLF_FILE =               'data/train_data/best_clf.joblib'


RAW_DATA_FILE_PATH_CURRENT =         os.path.join(RAW_DATA_FILE_PATH, CURRENT_FILE)
RAW_CLEANED_DATA_FILE_PATH_CURRENT = os.path.join(RAW_CLEANED_DATA_FILE_PATH, CURRENT_FILE)
CLEANED_DATA_FILE_PATH_CURRENT =     os.path.join(CLEANED_DATA_FILE_PATH, CURRENT_FILE)
SCRAPER_TIMEOUT = 5
SCRAPER_SLEEP = 1


