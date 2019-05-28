MANUSCRIPT
----------
<Title>


JOURNAL
-------
<Journal>


AUTHORS
-------
<Author list>


CORRESPONDING AUTHOR
--------------------
Joanna Diong, School of Medical Sciences, Faculty of Medicine and Health, The University of Sydney, Sydney, NSW 2006, Australia.
Email: joanna.diong@sydney.edu.au


DATA FILES
----------
Data for each subject are stored in the zipped `data` folder in these formats:
Spike2 .smr 
Matlab .mat 
Text .txt

[data->data.csv]
Audit results from the four rater concatenated into one comma-seperated values file.

[data->number_papers_published_per_year.txt]
Results of PubMed search for number of published papers by year and journal.
   

MISCELLANEOUS FILES
------------------
[misc->descriptions.txt]
[misc->descriptions_short.txt]
Full and shortened desriptions of each audit question; used when outputing results and generating figures.


CODE FILES
----------
Python and R code files to perform final data analysis and generate figures were written by Joanna Diong and Martin Héroux (Python v3.6, R v3.4). Code has been tested and should be forward compatible.

Additional Python packages:
neo 0.5.2
quantities 0.12.1
numpy 1.14.0
matplotlib 2.1.2
scipy 1.0.0
pandas 0.22.
seaborn 0.8.1
statsmodels 0.8.0

Note: `script.py` also calls functions from a custom written Python package `biosig`, available here:
https://github.com/joannadiong/biosig

[script.py]
Main script. Import data, call functions from `process.py` and associated files. Plot figures for individual subjects, conduct group analysis, plot figures for the group.

[process.py, trials_key, emg_key]
Module containing functions used to clean data and plot figures. Calls functions from `trials_key.py` and `emg_key.py`.

[mmax.py]
Module to calculate activation proportions and submaximal torques during data collection.

[script.R]
Import `angle90.csv` and `angle0.csv`, calculate group means and 95% CI of the effect of % predicted maximal torque on angle, export data to `./data/proc/results_con_r.txt`. 
`script.py` plots mean slopes and 95% CI limits for the group using these data. 


INSTRUCTIONS TO RUN ANALYSIS
----------------------------
Download all code files and data.zip into a single folder. 
Unzip the data file into the same location.
Download the biosig package. 
In `script.py` (line <#>), change the user-specific file path to set the location of biosig.
Run `script.py`.

Note: for ease and transparency, all raw and processed data are hosted in the OSF repository. 


OUTPUTS
-------
[activations_sub.csv]
Subject activation proportions

[angle0.csv, angle90.csv]
Subject ankle angle at each % predicted maximal torque

[baseline_sub.csv]
Subject baseline raw data

[describe_emg0.csv, describe_emg90.csv]
Group descriptive data of muscle EMG at 0% predicted torque

[describe_sub.csv]
Group descriptive data

[emg0.csv, emg90.csv]
Subject data of muscle EMG at 0% predicted torque

[results_con.txt]
Group mean and 95% CI of the effect of % predicted maximal torque on angle

[activations_sub.png]
Figure 2

[angle0.png, angle90.png]
Figure 4 subplots


