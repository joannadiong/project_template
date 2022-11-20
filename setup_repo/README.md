# <Title>

First A. Author<sup>1</sup>, 
Second B. Author<sup>2</sup>, 
Third Author<sup>3</sup>, 
Last  Author<sup>1,2,3</sup>

<sup>1</sup> University of Pandoc, Randwick, NSW, Australia \
<sup>2</sup> Markdown Institute, Ottawa, ON, Canada \
<sup>3</sup> LaTeX Research Institute, Kingston, On, Canada

## Suggested citation

<Citation>

## Protocol registration

The protocol for this study was registered on the Open Science Framework (OSF): [<link>][rego]

## Data

Raw data to generate Fig <fig> are available in the zipped folder "<folder>"
from the Open Science Foundation repository <link> in these formats:
* Spike2 .smr 
* Matlab .mat 
* Text .txt

Unzip the subject data folder and place it in __data -> raw__. 

Processed data to generate Fig <fig> are available in __data -> proc__ as the files: 
* subjects_data.csv
* subjects_data.json
* subjects_times_mvc.csv

Processed data for statistical analysis and Stata code files are stored in __stats -> data__ in these formats: 
    Text .csv
    Stata .do

## Code

Python code files were written by <name> (Python v3.9). 

Stata code files were written by <name> (Stata 16). 

### Python files

`script`: Main script to run analysis.

`fig`: Script to generate PNG and SVG figures, saved in __data -> proc__

`process`, `utilities`: Modules containing functions used to clean data and plot figures.

`process` calls the deprecated Python package `spike2py` written by Martin Héroux.
The deprecated package is bundled with this repo as "spike2py.zip"
Download the package, save it in a location outside of this project folder,
and point the Python interpreter (i.e. add the root) towards that location.

(For the new and revised packaged, see the [spike2py GitHub page][spike2py].)

### Running Python code

A reliable way to reproduce the analysis would be to run the code in an
integrated development environment for Python (e.g. [PyCharm][pycharm]). 

Create a virtual environment and install dependencies.
Using the Terminal (Mac or Linux, or PyCharm Terminal), 

```bash 
python -m venv env
```
Next, activate the virtual environment. 

For Mac or Linux, 

```bash
source env/bin/activate
```

For Windows, 

```bash
.\env\Scripts\activate
```

Then, install dependencies,

```bash
pip install -r requirements.txt
```

Download all code files and data.zip into a single folder.
Unzip the data file into the same location.
Download the `spike2py` package. Point the Python interpreter to the location of `spike2py`.

Run each file separately: 

1. `script.py`
2. `fig.py`

### Stata files

Running __stats -> script.do__ imports __subjects_data.csv__ and models activation and EMG.
Output and locations: 

1. __stats -> log_files__: log files of results
2. __stats -> graphs__: figures

Fig 3 and 4 are generated from the Stata do file.

### Running Stata code

Open __stats -> script.do__.

File paths to generate results and figures are currently configured for
Linux or Mac using forward single slashes `/`. To configure for
Windows, use double backslashes `\\` (__script.do__, lines <#>). 

In line 28 of __script.do__, set file path to local directory.

Uncomment line <#> of `ssc install <package>` to install `<package>` package, unless already installed.

Uncomment lines <#> to save a log file in __stats -> log_files__.

Run __script.do__.

## Output

Table 1. is generated using data from "results.txt", saved in __data -> proc__

Table 2. is generated using data from "subjects_data_describe.csv", saved in __data -> proc__

Fig 1. is generated using data from sub22, and saved in __data -> proc -> sub22__

Fig 2. is generated using data from "subjects_data.csv",
saved as PNG and SVG files labelled "emg_torque" in __data -> proc__

Fig 3. is generated using data from "subjects_data.csv",
saved as PNG and SVG files labelled "emg_normalised" in __data -> proc__


[rego]: <protocol_registration_link>
[spike2py]: https://github.com/MartinHeroux/spike2py
[pycharm]: https://www.jetbrains.com/pycharm/promo/?gclid=Cj0KCQiAtqL-BRC0ARIsAF4K3WFahh-pzcvf6kmWnmuONEZxi544-Ty-UUqKa4EelnOxa5pAC9C4_d4aAisxEALw_wcB 

