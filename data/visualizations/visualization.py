import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

df = pd.read_csv("../results/sample.csv")
print(df.head())
print(df.columns)

#Relationship between player start hand and whether or not the player busted
# plt.figure(1)
# sns.countplot(x='Player Start Hand', hue='Player Busted', data=df)
# plt.show()

# #Relationship between dealer starting card and whether or not the palyer busted
# plt.figure(2)
# sns.countplot(x='Dealer First Card', hue='Player Busted', data=df)
# plt.show()

# #Relationship between dealer starting card and the outcome of the match
# plt.figure(3)
# sns.countplot(x='Dealer First Card', hue='Game Result', data=df)
# plt.show()

#Plots the average ending hand of the dealer given a starting card
plt.figure(4)
sns.lineplot(x='Dealer First Card', y = df['Dealer End Hand'].apply(np.mean), data=df)
plt.xticks(np.arange(1,11,step=1))
plt.show()
