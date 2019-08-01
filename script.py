import os, sys
import numpy as np
import matplotlib.pyplot as plt

"""
# Import as needed
import neo
import scipy.io as sio
from matplotlib.widgets import Cursor
import pandas as pd
import seaborn as sns
import statsmodels as sm
import statsmodels.formula.api as smf

sys.path.insert(0, "/home/joanna/Dropbox/Sketchbook/python/biosig/")
import biosig
"""

LENOVO = '/home/joanna/Dropbox/Projects/<project>'
EXTDRV = '/media/joanna/Elements/Projects/<project>'
REPO = '.'
os.chdir(LENOVO) # set as REPO when released for OSF

path_raw = os.path.join('.', 'data', 'raw')
path_proc = os.path.join('.', 'data', 'proc')

CON = ['sub01', 'sub02', 'sub03']
STR = ['sub31', 'sub32', 'sub33']

for sub in CON + STR:
    print(sub + '\n')
    if not os.path.exists(os.path.join('.', 'data', 'proc', sub)):
        os.chdir(path_proc)
        os.mkdir(sub)
        os.chdir(os.path.join('..', '..'))  # return to base directory: src/code
    os.chdir(os.path.join(path_raw, sub))
    # do stuff

    os.chdir(os.path.join('..', '..', '..')) # return to src/code/
    print(' ')

# ----------------
# Generate figures
# ----------------

os.chdir(path_proc)

fig = plt.figure(figsize=(6.8, 2.7))
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

# set x ticks and labels
ax1.set_xticks([0, 1, 2])
ax1.set(xticklabels=order)
ax1.tick_params(axis='x', which='both', bottom='off', top='off')
# set x and y bins
ax1.locator_params(axis='x', nbins=7)
ax1.locator_params(axis='y', nbins=7)
# keep y axis
ax1.spines['top'].set_visible(False)
ax1.spines['bottom'].set_visible(False)

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

df = <dataframe>
var = <variable>

# ordinary least squares regression between independent groups
md = smf.ols(var + ' ~ group', df, groups=df.group)
md_fit = md.fit(reml=True)
llf = md_fit.llf

mdage = smf.ols(var + ' ~ group + age', df, groups=df.group)
mdage_fit = mdage.fit(reml=True)
llf_age = mdage_fit.llf

# likelihood ratio test of effect of including age
lr, p = biosig.statcalc.lrtest(llf, llf_age)

# calculate descriptive data of variables
df_describe = df[var].groupby(df.group).describe().unstack()[['count', 'mean', 'std']]
df_describe = df_describe.rename(index={0: 'CON', 1: 'STR'})

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
    file.write('\nAge-adjusted regression: \n')
    file.write('\n' + str(mdage_fit.summary()) + '\n')
    file.write('\nLR test, p value: {:.2f}, {:.4f}'.format(lr, p))


