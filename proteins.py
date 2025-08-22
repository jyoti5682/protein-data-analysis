import pandas as pd 
import  numpy as np 
import matplotlib.pyplot as plt

df=pd.read_csv('protein_dataset.csv')
print(df.head(30))
print(df.describe())
print(df.info())
df.isnull().sum()
print(df['Function'].unique())
print(df['Organism'].value_counts())
print(df["Length_AA"].mean())
print(df["Molecular_Weight_kDa"].median())
print(df["Isoelectric_Point_pI"].std())
new=df.groupby("Organism")["Length_AA"].mean()
new1=df.groupby("Function")["Molecular_Weight_kDa"].agg(["mean", "max", "min"])
print(new)
print(new1)

corre=df[["Length_AA", "Molecular_Weight_kDa", "Isoelectric_Point_pI", "Hydrophobicity_Index"]].corr()
print(corre)
print(df.nlargest(5, "Length_AA"))  
print(df.nsmallest(5, "Isoelectric_Point_pI"))   


df2=df[(df["Length_AA"] > 1000) & (df["Molecular_Weight_kDa"] > 100)]
print(df2)

plt.figure(figsize=(8,6))
plt.hist(df["Length_AA"], bins=40, edgecolor="black")
plt.title("Distribution of Protein Lengths")
plt.xlabel("Protein Length (Amino Acids)")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(8,6))
plt.scatter(df["Length_AA"], df["Molecular_Weight_kDa"], alpha=0.5, c="blue")
plt.title("Protein Length vs Molecular Weight")
plt.xlabel("Length (Amino Acids)")
plt.ylabel("Molecular Weight (kDa)")
plt.show()

plt.figure(figsize=(10,6))
df.boxplot(column="Hydrophobicity_Index", by="Function", rot=45)
plt.title("Hydrophobicity Index by Protein Function")
plt.suptitle("")  # remove automatic title
plt.ylabel("Hydrophobicity Index")
plt.show()

avg_length = df.groupby("Organism")["Length_AA"].mean().sort_values()

plt.figure(figsize=(8,6))
avg_length.plot(kind="bar", color="skyblue")
plt.title("Average Protein Length per Organism")
plt.ylabel("Average Length (AA)")
plt.xlabel("Organism")
plt.show()

import numpy as np

corr = df[["Length_AA","Molecular_Weight_kDa","Isoelectric_Point_pI","Hydrophobicity_Index"]].corr()

plt.figure(figsize=(6,5))
plt.imshow(corr, cmap="coolwarm", interpolation="nearest")
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns, rotation=45)
plt.yticks(range(len(corr)), corr.columns)
plt.title("Correlation Heatmap of Protein Features")
plt.show()
