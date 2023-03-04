from sofifa_scraper import merge_ova_to_cleaned_all
from constants import (
    CURRENT_YEAR,
    DATA_PATH,
    RAW_DATA_FILE_PATH,
    OVA_FILE_PATH,
    STANDINGS_PATH,
    RAW_CLEANED_DATA_FILE_PATH,
    CLEANED_DATA_FILE_PATH,
    FINAL_FILE,
    RAW_DATA_FILE_PATH_CURRENT,

)
from current_status import add_current_details_all
from clean_data import (
    clean_all,
    combine_matches,
    get_match_results_against,
)
from helpers import (
    copy_csv
)

from match_history import get_fixtures, get_current_fixtures
from rankings import get_rankings_all

def preprocessing(data_year_available_from=1993, data_year_collect_from=2006):
    # Preprocessing

    # Preprocessing-1. Latest premier league results
    # This data can also be retrieved from http://www.football-data.co.uk/englandm.php
    # Uncomment below to get the latest match results
    get_fixtures(RAW_DATA_FILE_PATH, data_year_available_from, CURRENT_YEAR)
    get_current_fixtures(RAW_DATA_FILE_PATH_CURRENT)

    # Run the functions below to start generating necessary data

    # 1. From raw data, remove all data but the selected columns.
    # Produces: cleaned data csv located in CLEANED_DATA_FILE_PATH
    clean_all(RAW_DATA_FILE_PATH, RAW_CLEANED_DATA_FILE_PATH, data_year_available_from, CURRENT_YEAR)

    # Preprocessing-2. Standings (from 1993 to curent year)
    # Uncomment below to run the function
    get_rankings_all(data_year_available_from, CURRENT_YEAR, RAW_CLEANED_DATA_FILE_PATH, STANDINGS_PATH)

    # 2. From 1, add Overall Rating columns
    merge_ova_to_cleaned_all(OVA_FILE_PATH, RAW_CLEANED_DATA_FILE_PATH, data_year_collect_from, CURRENT_YEAR)

    # 3. From 2, copy cleaned raw data to cleaned data for prediction purpose
    # Produces: copy csv from RAW_CLEANED_DATA_FILE_PATH to CLEANED_DATA_FILE_PATH
    copy_csv(RAW_CLEANED_DATA_FILE_PATH, CLEANED_DATA_FILE_PATH)

    # 4. From 3, add current status columns (current point, current goal for,against,difference, match played, losing/winning streaks, last 5 games)
    # Produces: cleaned csv modified, located in CLEANED_DATA_FILE_PATH. Now all cleaned csv from 1993-2018 have additional columns
    add_current_details_all(CLEANED_DATA_FILE_PATH, CLEANED_DATA_FILE_PATH, STANDINGS_PATH, data_year_available_from,
                            CURRENT_YEAR, data_year_available_from)

    # 5. From 4, merge all csv files from startYear to endYear together.
    # FOR NOW, I only collect data from 2006 because sofifa only provides ova data from 2006, and model tends to perform better with this approach
    # Produces: new csv file on FINAL_FILE
    combine_matches(CLEANED_DATA_FILE_PATH, FINAL_FILE, data_year_collect_from, CURRENT_YEAR)

    # 6. From 5, get all head-to-head results (match results against the other team over time)
    # Produces: editted final.csv file under DATA_PATH
    get_match_results_against(FINAL_FILE, CLEANED_DATA_FILE_PATH, DATA_PATH, data_year_available_from, CURRENT_YEAR)





if __name__ == "__main__":

    preprocessing()