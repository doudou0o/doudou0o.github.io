#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt



fruits_df = pd.read_csv("./fruit.txt", sep='\t')

#X = fruits_df[['width', 'height']]
#Y = fruits_df['fruit_name']
#plt.scatter(X['width'], X['height'], c=Y, edgecolors='k', cmap=plt.cm.Paired)
#plt.xlim(X['width'].min()-0.5)
#plt.ylim(X['height'].min()-0.5)
#plt.show()

fig = plt.figure()
ax  = plt.subplot()

labels = {'apple':'red', 'lemon':'green'}
for label in labels:
    fruits_label = fruits_df[fruits_df['fruit_name'].isin([label])]
    X = fruits_label[['width', 'height']]
    Y = fruits_label['fruit_name']
    ax.scatter(X['width'], X['height'], c=labels[label])

handles,_ = ax.get_legend_handles_labels()
ax.legend(handles, labels = labels.keys(), loc='upper right')
plt.show()

