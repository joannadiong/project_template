import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# import scipy.io as sio
# import seaborn as sns
# import statsmodels as sm
import statsmodels.formula.api as smf

LENOVO = '/home/joanna/Dropbox/Projects/<project>'
EXTDRV = '/media/joanna/Elements/Projects/<project>'
REPO = '.'
os.chdir(LENOVO)

path_raw = os.path.join('.', 'data', 'raw')
path_proc = os.path.join('.', 'data', 'proc')

CON = ['sub01', 'sub02', 'sub03']
EXP = ['sub31', 'sub32', 'sub33']

# create subject folders for processed data
for sub in CON + EXP:
    print(sub + '\n')
    if not os.path.exists(os.path.join('.', 'data', 'proc', sub)):
        os.chdir(path_proc)
        os.mkdir(sub)
        os.chdir(os.path.join('..', '..'))
    os.chdir(os.path.join(path_raw, sub))
    # do stuff

    os.chdir(os.path.join('..', '..', '..'))
    print(' ')

# ----------------
# Generate figures
# ----------------

os.chdir(path_proc)

fig = plt.figure(figsize=(6.8, 2.7))
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

# set x and y bins
ax1.locator_params(axis='x', nbins=7)
ax1.locator_params(axis='y', nbins=7)
# keep x and y axes
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

fig.tight_layout()
plt.savefig('figure.png', dpi=300, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None)

# --------------------
# Descriptive analysis
# --------------------

os.chdir(path_proc)

# read descriptive data of subject characteristics
df = pd.read_csv('<log>.csv')
df.groupby(df.group).describe(include='all').to_csv('describe.csv')

# --------------------
# Inferential analysis
# --------------------

os.chdir(path_proc)

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

with open(file, 'a') as file:
    file.write('\n')
    file.write('\n--------------------')
    file.write('\n' + var + ': ')
    file.write('\n--------------------')
    file.write('\n')
    file.write('\n' + str(df_describe) + '\n')
    file.write('\nUnadjusted regression: \n')
    file.write('\n' + str(md_fit.summary()) + '\n')


