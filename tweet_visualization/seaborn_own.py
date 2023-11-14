import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the example planets dataset
#dataset = sns.load_dataset("") # Mettre entre guillement le nom du fichier du dataset
#ou remplacer par dataset = pd.read_csv()
dataset = pd.read_pickle("dumps/df.pkl")
print(dataset.columns)
#cmap = sns.cubehelix_palette(8)
graph = sns.relplot(
    data=dataset,
    x="date", y="polarity",
    palette=None, sizes=(10, 200),
)
graph.set(xscale="log", yscale="log")
graph.ax.xaxis.grid(True, "minor", linewidth=.25)
graph.ax.yaxis.grid(True, "minor", linewidth=.25)
graph.despine(left=True, bottom=True)
plt.show()