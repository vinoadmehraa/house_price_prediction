import os
import tarfile
from six.moves import urllib
from src.data import data_load

import pandas as pd

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
ROOT_PATH = "datasets/housing"
ROOT_URL = DOWNLOAD_ROOT + ROOT_PATH + "/housing.tgz"

HOUSING_PATH = os.path.join(os.path.dirname(__file__), '../../datasets/raw','../../datasets/processed')
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

## Fetch the data set from the original location.
def fetch_housing_data(housing_path=HOUSING_PATH, housing_url=HOUSING_URL):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    
    tgz_path = os.path.join("../../datasets/raw","housing.tgz")
    print("The tgz path is:",tgz_path)
    urllib.request.urlretrieve(ROOT_URL,tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path='../../datasets/raw')
    print("The housing path is:",HOUSING_PATH)
    housing_tgz.close()

## Load the data.
def load_housing_data(file_path):
    csv_path = os.path.join(file_path,"housing.csv")
    return pd.read_csv(csv_path)


if __name__ == "__main__":
    fetch_housing_data()
    df = data_load.load_housing_data("../../datasets/raw")
    print(f"Data has been downloaded and extracted to {HOUSING_PATH}")