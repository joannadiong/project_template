# <Title>

First A. Author^1^, Second B. Author^2^, Third Author^3^, Last  Author^1,2,3^, New LastAuthor^2^

1. University of Pandoc, Randwick, NSW, Australia
2. Markdown Institute, Ottawa, ON, Canada
3. LaTeX Research Institute, Kingston, On, Canada

## Suggested citation

<Citation>

## Data

Raw data to generate Fig <fig> are stored in the **data** folder in these formats:
    Spike2 .smr 
    Matlab .mat 
    Text .txt

Processed data for statistical analysis and Stata code files are stored in the **stats** folder in these formats: 
    Text .csv
    Text .txt
    Stata .do

**stats -> data -> subjects_data.csv**
The Stata .do file analyses processed data in this dataset.

## Code

Python code files were written by <name> (Python v3.7). 

Stata code files were written by <name> (Stata 16). 

### Python

Python code is run in the **<venv>** environment that contains the dependency files. 
The activation environment can be installed from the Terminal (Mac or Linux, or using the PyCharm Terminal in Windows) using `<venv>.yml`. To install, type in Terminal:

  `conda env create -f <venv>.yml`

**process.py** calls the Python package **spike2py** written by Martin Héroux, available from the [spike2py GitHub page][spike2py]. 
Download the package and point the Python interpreter towards it.

**fig-1.py**: Generate SVG file of single participant trial data (Fig 2) in **data -> proc -> sub01**

**fig-2.py**: Generate SVG file of predicted on observed EMG data (Fig 7) in **data -> proc**

**process.py, utilities.py, trials_key.py**: Modules containing functions used to clean data and plot figures. 

### Running Python code

Download all code files, data.zip, and stats.zip into a single folder. Unzip the data file into the same location.
Download the **spike2py** package. Point the Python interpreter to the location of **spike2py**.
Set file path for `REPO` to local directory:

1. **process.py** line <#>
2. **fig-7.py** line <#>

Run each file separately: **fig-1.py**, **fig-2.py**

### Stata

Running **stats -> script.do** imports **subjects_data.csv** and models activation and EMG. Output and locations: 

1. **stats -> log_files**: log files of results
2. **stats -> graphs**: figures

Fig 3 and 4 are generated from the Stata do file.

### Running Stata code

Open **stats -> script.do**.

File paths to generate results and figures are currently configured for Linux or Mac using forward single slashes `/`. To configure for Windows, use double backslashes `\\` (**script.do**, lines <#>). 

In line 28 of **script.do**, set file path to local directory.

Uncomment line <#> of `ssc install <package>` to install `<package>` package, unless already installed.

Uncomment lines <#> to save a log file in **stats -> log_files**.

Run **script.do**.


[spike2py]: https://github.com/MartinHeroux/spike2py
