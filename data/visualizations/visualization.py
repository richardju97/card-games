import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("../results/sample.csv")
print(df.head())
print(df.columns)

#Relationship between player start hand and whether or not the player busted
plt.figure(1)
sns.countplot(x='Player Start Hand', hue='Player Busted', data=df)
plt.show()

#Relationship between dealer starting card and whether or not the palyer busted
plt.figure(2)
sns.countplot(x='Dealer First Card', hue='Player Busted', data=df)
plt.show()

#Relationship between dealer starting card and the outcome of the match
plt.figure(3)
sns.countplot(x='Dealer First Card', hue='Game Result', data=df)
plt.show()