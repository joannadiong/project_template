import numpy as np
import pandas as pd
import polars as pl
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

import utils

Filepaths = utils.Filepaths
Constants = utils.Constants


def process_data():
    df = pl.read_csv(Filepaths.path_raw / 'data.csv')




# TODO: 
#  * process
#  * plot

