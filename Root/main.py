from organism import organism
from scientificCategory import scientificCategory
import logging
import pandas as pd

logger = logging.getLogger(__name__)
logging.basicConfig(filename='Root\main.log', encoding='utf-8', level=logging.DEBUG)

def main():
    print("Welcome to our Biodiversity By Country -Ditsribution of Animals, Plants, and Natural Communities System! Please select what action you will like to take next!")
    print("\tMenu:")
    print("\t\t1) Show Taxonomic Frequency with a graph of your choice")
    print("\t\t2) Perform a calculation")
    print("\t\t3) Find a specific Catergory, Taxonomic Group, Taxonomic Subgroup, Scientific Name, or Common Name in the dataset")
    print("\t\t4) Exit the program.")
    inTheSystem = True
    df = pd.read_csv('Root\Input\YatesBiodiversity.csv',sep=',',index_col="Taxonomic Group")

    while inTheSystem:
        userTask = input("Please choice your task: ")
        if userTask == 1:
            graphPick = input("What kind of graph would you like to see?")
            print("\t\t1) Display a histogram representation of the data.")
            print("\t\t2) Display a line plot representation of the data.")
            print("\t\t3) Display a scatter plot representation of the data.")
            print("\t\t4) Display a whisker-box plot representation of the data.")
            print("\t\t5) Display a violin plot representation of the data.")
            if userTask == 1:
                organism.histogram(scientificCategory.dataframeCSV)
            #
            elif userTask == 2:
                organism.linePlot(scientificCategory.dataframeCSV)
            #
            elif userTask == 3:
                scientificCategory.scatterPlot(scientificCategory.dataframeCSV)
            #
            elif userTask == 4:
                scientificCategory.whiskerBoxPlot(scientificCategory.dataframeCSV)
            #
            elif userTask == 5:
                scientificCategory.violinPlot(scientificCategory.dataframeCSV)
            #
        #
        elif userTask == 2:
            calcPick = input("What calculation would you like to perform")
            print("\t\t1) Calculate joint probabilities.")
            print("\t\t2) Calculate std, mean, and median.")
            print("\t\t3) Calculate joint counts.")
            print("\t\t4) Calculate conditional probabilities.")
            if calcPick == 1:
                scientificCategory.calculateJointProbabilities(scientificCategory.dataframeCSV, a='Taxonomic Subgroup',b= 'Taxonomic Group')
            #
            elif calcPick == 2:
                scientificCategory.calculations(scientificCategory.dataframeCSV)
            #
            elif calcPick == 3:
                scientificCategory.calculateJointCounts(scientificCategory.dataframeCSV, a = 'Taxonomic Subgroup', b = 'Taxonomic Group')
            #
            elif calcPick == 4:
                x = scientificCategory.calculateConditionalProbabilities(scientificCategory.dataframeCSV, 'Taxonomic Subgroup', 'Taxonomic Group')
                print(x)
            #
        #
        elif userTask == 3:
            pick = input("Enter what you'd like to find: ")
            print("\t\t1) Find category.")
            print("\t\t2) Find taxonomic group.")
            print("\t\t3) Find taxonomic Subgroup.")
            print("\t\t4) Find scientific name.")
            print("\t\t5) Find common name.")
            if pick == 1:
                organism.findCategory("category")
            #
            elif pick == 2:
                organism.findCategory("taxonomicGroup")
            #
            elif pick == 3:
                organism.findCategory("taxonomicSubgroup")
            #
            elif pick == 4:
                organism.findCategory("scientificName")
            #
            elif pick == 5:
                organism.findCategory("commonName")
            #
        #
        elif userTask == 4:
            print("Goodbye!")
            inTheSystem = False
        #
    #
#

if __name__ == "__main__":
    main()
