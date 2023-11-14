import seaborn as sns
import pandas as pd
sns.set_theme(style="whitegrid")

# Load the example planets dataset
dataset = sns.load_dataset("") # Mettre entre guillement le nom du fichier du dataset
#ou remplacer par dataset = pd.read_csv()

cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=dataset,
    x="distance", y="orbital_period",
    hue="year", size="mass",
    palette=cmap, sizes=(10, 200),
)
g.set(xscale="log", yscale="log")
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)