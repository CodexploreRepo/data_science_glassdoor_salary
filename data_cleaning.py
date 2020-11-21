# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import os

dir_name = os.path.join(os.getcwd(), "csv")
path = os.path.join(dir_name, "glassdoor_jobs.csv")

print(path)
df = pd.read_csv(path)
df




