from organism import organism
from scientificCategory import scientificCategory
import logging
import pandas as pd

logger = logging.getLogger(__name__)
logging.basicConfig(filename='Root\main.log', encoding='utf-8', level=logging.DEBUG)

def main():
    print("Welcome to our Biodiversity By Country -Ditsribution of Animals, Plants, and Natural Communities System! Please select what action you will like to take next!")
    print("\tMenu:")
    print("\t\t1) Show Taxonomic Frequency with a histogram")
    print("\t\t2) Show Taxonomic Frequency with a line plot")
    print("\t\t3) Show Taxonomic Frequency with a scatter plot")
    print("\t\t4) Show mean, median, and std calculations")
    print("\t\t5) Find a specific Catergory in the dataset")
    print("\t\t6) Find a specific Taxonomic Group in the dataset")
    print("\t\t7) Find a specific Taxonomic Subgroup in the dataset")
    print("\t\t8) Find a specific Scientific Name in the dataset")
    print("\t\t9) Find a specific Common Name in the dataset")
    print("\t\t10) Exit the program.")
    inTheSystem = True
    df = pd.read_csv('Root\Input\YatesBiodiversity.csv',sep=',',index_col="Taxonomic Group")

    try:
        while inTheSystem:
            userTask = input("Please choice your task: ")
            if userTask == 1:
                organism.histogram(df)
            #
            elif userTask == 2:
                organism.linePlot(df)
            #
            elif userTask == 3:
                scientificCategory.scatterPlot(df)
            #
            elif userTask == 4:
                scientificCategory.calculations(df)
            #
            elif userTask == 5:
                organism.findCategory("category")
            #
            elif userTask == 6:
                organism.findCategory("taxonomicGroup")
            #
            elif userTask == 7:
                organism.findCategory("taxonomicSubgroup")
            #
            elif userTask == 8:
                organism.findCategory("scientificName")
            #
            elif userTask == 9:
                organism.findCategory("commonName")
            #
            elif userTask == 10:
                print("Goodbye!")
                inTheSystem = False
            #
        #
    #
    except:
        logger.debug('User menu not working.')
    #
#

if __name__ == "__main__":
    main()
