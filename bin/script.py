"""
In PyCharm Settings/Preferences | Build, Execution, Deployment | Console | Python Console, 
add `code/bin` path to `sys.path.extend(['route_to_first_project', 'route_to_second_project']`
e.g. `sys.path.extend([WORKING_DIR_AND_PYTHON_PATHS, '/home/joanna/Dropbox/Projects/<project>/src/code/bin/'])`
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf
from pathlib import Path

LENOVO = '/home/joanna/Dropbox/Projects/<project>'
EXTDRV = '/media/joanna/Elements/Projects/<project>'
REPO = '.'
os.chdir(LENOVO)

project_path = Path('/home/joanna/Dropbox/Projects/<project>/data')
path_raw = project_path / 'raw'
path_proc = project_path / 'proc'

CON = ['sub01', 'sub02', 'sub03']
EXP = ['sub31', 'sub32', 'sub33']

# create subject folders for processed data
for sub in CON + EXP:
    if not os.path.exists(path_proc / sub):
    os.mkdir(path_proc / sub))

# ----------------
# Generate figures
# ----------------

sub = 'sub01'
fig = plt.figure(figsize=(6.8, 2.7))
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

# set y axis properties
ax1.set_ylim([0, 5])
ax1.set_xticks([0, 1, 2])
ax1.set_xticklabels(['small', 'medium', 'large'])
ax1.set_ylabel('Outcome')
# set x and y bins
ax1.locator_params(axis='x', nbins=7)
ax1.locator_params(axis='y', nbins=7)
# keep x and y axes
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

fig.tight_layout()
plt.savefig(path_proc / f'figure_{sub}.png', dpi=300)

# --------------------
# Descriptive analysis
# --------------------

# read descriptive data of subject characteristics
df = pd.read_csv('<log>.csv')
df.groupby(df.group).describe(include='all').to_csv('describe.csv')

# --------------------
# Inferential analysis
# --------------------

var = 'var'

# ordinary least squares regression between independent groups
md = smf.ols(var + ' ~ group', df, groups=df.group)
md_fit = md.fit(reml=True)
llf = md_fit.llf

# calculate descriptive data of variables
df_describe = df[var].groupby(df.group).describe().unstack()[['count', 'mean', 'std']]
df_describe = df_describe.rename(index={0: 'CON', 1: 'EXP'})

file = 'results.txt'
open(file, 'w').close()
outfile = open(file, 'w')
outfile.write('\n----------------------------------------')
outfile.write('\nIndependent tests between groups')
outfile.write('\n----------------------------------------')
outfile.close()

with open(file, 'a') as f:
    f.write('\n')
    f.write('\n--------------------')
    f.write('\n' + var + ': ')
    f.write('\n--------------------')
    f.write('\n')
    f.write('\n' + str(df_describe) + '\n')
    f.write('\nUnadjusted regression: \n')
    f.write('\n' + str(md_fit.summary()) + '\n')


