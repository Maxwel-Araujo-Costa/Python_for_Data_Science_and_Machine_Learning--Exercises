import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
titanic.head()

def jointplot():
    sns.jointplot(x='fare',y='age',data=titanic)
    plt.show()

def distplot():
    sns.distplot(titanic['fare'],bins=30,kde=False,color='red')
    plt.show()

def boxplot():
    sns.boxplot(x='class',y='age',data=titanic,palette='rainbow')
    plt.show()

def swarmplot():
    sns.swarmplot(x='class',y='age',data=titanic,palette='Set2')
    plt.show()

def countplot():
    sns.countplot(x='sex',data=titanic)
    plt.show()

def heatmap():
    sns.heatmap(titanic.corr(numeric_only=True),cmap='coolwarm')
    plt.title('titanic.corr()')
    plt.show()

def facetGrid():
    g = sns.FacetGrid(data=titanic,col='sex')
    g.map(plt.hist,'age')
    plt.show()

def main ():
    print("Exercise 1: jointplot")
    jointplot()

    print("Exercise 2: distplot")
    distplot()

    print("Exercise 3: boxplot")
    boxplot()

    print("Exercise 4: swarmplot")
    swarmplot()

    print("Exercise 5: countplot")
    countplot()

    print("Exercise 6: heatmap")
    heatmap()

    print("Exercise 7: FacetGrid")
    facetGrid()

if __name__ == "__main__":
    main()