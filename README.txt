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
Python and R code files to perform final data analysis and generate figures were written by Joanna Diong and Martin Héroux (Python v3.7, R v3.4). Code has been tested and should be forward compatible.

The environment `<name>` to run Python code can be installed from the Terminal (Mac or Linux, or using the PyCharm Terminal in Windows) using `<name>.yml`. Type:

  conda env create -f <name>.yml

Additional Python packages:
numpy 1.16.4 
matplotlib 3.1.1
pandas 0.25.0

`script.py` also calls the custom-written Python package `spike2py`, available here: 
https://github.com/MartinHeroux/spike2py
Download the package and 'point' the Python interpreter towards it.

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
Download the `spike2py` package. 
Point the Python interpreter to the location of `spike2py`.
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


