from organism import organism
from scientificCategory import scientificCategory
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='Root\main.log', encoding='utf-8', level=logging.DEBUG)

def main():
    print("Welcome to our Biodiversity By Country -Ditsribution of Animals, Plants, and Natural Communities System! Please select what action you will like to take next!")
    inTheSystem = True

    while inTheSystem:
        print("\tMenu:")
        print("\t\t1) Show Taxonomic Frequency with a graph of your choice")
        print("\t\t2) Perform a calculation")
        print("\t\t3) Find a specific Catergory, Taxonomic Group, Taxonomic Subgroup, Scientific Name, or Common Name in the dataset")
        print("\t\t4) Exit the program.")
        userTask = int(input("Please choice your task: "))
        if userTask == 1:
            print("\tGraph Menu:")
            print("\t\t1) Display a histogram representation of the data.")
            print("\t\t2) Display a line plot representation of the data.")
            print("\t\t3) Display a scatter plot representation of the data.")
            print("\t\t4) Display a whisker-box plot representation of the data.")
            print("\t\t5) Display a violin plot representation of the data.")
            graphPick = input("What kind of graph would you like to see? ")
            
            if graphPick == 1:
                organism.histogram(scientificCategory.dataframeCSV)
            #
            elif graphPick == 2:
                organism.linePlot(scientificCategory.dataframeCSV)
            #
            elif graphPick == 3:
                scientificCategory.scatterPlot(scientificCategory.dataframeCSV)
            #
            elif graphPick == 4:
                scientificCategory.whiskerBoxPlot(scientificCategory.dataframeCSV)
            #
            elif graphPick == 5:
                scientificCategory.violinPlot(scientificCategory.dataframeCSV)
            #
        #
        elif userTask == 2:
            print("\Calculation Menu:")
            print("\t\t1) Calculate joint probabilities.")
            print("\t\t2) Calculate std, mean, and median.")
            print("\t\t3) Calculate joint counts.")
            print("\t\t4) Calculate conditional probabilities.")
            calcPick = int(input("What calculation would you like to perform? "))
            
            if calcPick == 1: # works
                scientificCategory.calculateJointProbabilities(scientificCategory.dataframeCSV,'Taxonomic Subgroup','Taxonomic Group')
            #
            elif calcPick == 2: # in progress
                scientificCategory.calculations(scientificCategory.dataframeCSV, "Scientific Category")
            #
            elif calcPick == 3: # works
                scientificCategory.calculateJointCounts(scientificCategory.dataframeCSV, 'Taxonomic Subgroup', 'Taxonomic Group')
            #
            elif calcPick == 4: # works
                x = scientificCategory.calculateConditionalProbabilities(scientificCategory.dataframeCSV, 'Taxonomic Subgroup', 'Taxonomic Group')
                print(x)
            #
        #
        elif userTask == 3:
            print("\t\t1) Find category.")
            print("\t\t2) Find taxonomic group.")
            print("\t\t3) Find taxonomic Subgroup.")
            print("\t\t4) Find scientific name.")
            print("\t\t5) Find common name.")
            finding = int(input("Enter what you'd like to find: "))
            
            if finding == 1:
                x = organism.findCategory(scientificCategory.dataframeCSV, "category")
                print(x)
            #
            elif finding == 2:
                organism.findCategory(scientificCategory.dataframeCSV, "taxonomicGroup")
            #
            elif finding == 3:
                organism.findCategory(scientificCategory.dataframeCSV, "taxonomicSubgroup")
            #
            elif finding == 4:
                organism.findCategory(scientificCategory.dataframeCSV, "scientificName")
            #
            elif finding == 5:
                organism.findCategory(scientificCategory.dataframeCSV, "commonName")
            #
        #
        elif userTask == 4: # works
            print("Goodbye!")
            inTheSystem = False
        #
    #
#

if __name__ == "__main__":
    main()
