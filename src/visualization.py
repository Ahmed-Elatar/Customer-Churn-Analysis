import matplotlib.pyplot as plt
import seaborn as sns

def save_countplot(df, col, outpath, order=None, title=None):
    plt.figure(figsize=(6,4))
    sns.countplot(x=col, data=df, order=order)
    if title: plt.title(title)
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()

def save_boxplot(df, x, y, outpath, title=None):
    plt.figure(figsize=(8,5))
    sns.boxplot(x=x, y=y, data=df)
    if title: plt.title(title)
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()

def save_hist(df, col, outpath, bins=30, title=None):
    plt.figure(figsize=(8,4))
    sns.histplot(df[col], bins=bins, kde=True)
    if title: plt.title(title)
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()