import logging
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)
logging.basicConfig(filename='Root\organism.log', encoding='utf-8', level=logging.DEBUG)

class organism:
    def __init__(self):
        self.taxonomicSubgroup = ["Frogs and Toads", "Blackbirds and Orioles"]
        self.scientificName = ["Sturnella magna", "Ambystoma laterale"]
        self.commonName = ["Bullfrog", "Wood Frog"]
        self.category = ["Animal", "Plant"]
        self.taxonomicGroup = ["Birds", "Amphibians"]
    #

    #config dictionary 
    config =  dict()

    def histogram(dataFrame):
        try:
            logger.info('Visualize data distributions in a histogram...')
            try:
                try:
                    logger.info('Getting frequency of taxonomic groups...')
                    grouped_taxonmic = dataFrame["Taxonomic Group"].value_counts()
                    logger.info('Sorting frequency of taxonomic groups...')
                    freq_counts_sorted = grouped_taxonmic.sort_index()

                    plt.hist(freq_counts_sorted.index,bins=30,weights = freq_counts_sorted.values,alpha = 0.45, color = 'red')
                    plt.ylabel('Taxonomic Group Frequency')
                    plt.xlabel('Taxonomic Groups')
                    plt.title('Histogram of Yates Taxonomic Group Biodiversity')
                    plt.savefig('Root\Output\histogram.png')
                    logger.info('Successfully histogram visualize.')
                    return plt
                #
                except:
                    print("Not displaying histogram.")
                    logger.debug('Not displaying histogram.')
                #
            #
            except:
                print("Not reading dataset.")
                logger.debug('Not reading dataset.')
            #
        #
        except:
            print('Histogram not working.')
            logger.debug('Histogram not working.')
        #   
    #

    def linePlot(dataFrame):
        try:
            logger.info('Visualize data distributions in a line plot...')
            try:
                try:
                    freq_counts = dataFrame["Taxonomic Group"].value_counts() #gets the number of occurences of each Taxonomic Group 
                    freq_counts_sorted = freq_counts.sort_index() #sorts by index 
                    n = len(freq_counts)
                    x = np.arange(1,n+1)
                    y = freq_counts_sorted
                    plt.plot(x, y)
                    plt.title('Line Plot of Yates Biodiversity')
                    plt.xlabel('Taxonomic Groups')
                    plt.ylabel('Taxonomic Group Frequency')
                    plt.savefig('Root\Output\linePlot.png')
                    logger.info('Completed line plot...')
                    return plt
                #
                except:
                    print("Not displaying line plot.")
                    logger.debug('Not displaying line plot.')
                #
            #
            except:
                print("Not reading dataset.")
                logger.debug('Not reading dataset.')
            #
        #
        except:
            print('Line plot not working.')
            logger.debug('Line plot not working.')
        #
    #
    
    #query search function
    def findCategory(dataFrame, userInput,outputFile): # in progress
        try:
            logger.info('Query searching function...')         
            #this function will return either a table and or list of what the user ask for 
            if userInput == "category":
                category = dataFrame["Category"]
                print("\tMenu:")
                print("\t\t1) Find all the plants.")
                print("\t\t2) Find all the animals.")
                print("\t\t3) Find all the beetles.")
                categoryPick = int(input("Enter what you'd like to find: "))
                if categoryPick == 1:
                    target = "Plant"
                    filtered_df = (dataFrame[category == target])
                #
                elif categoryPick == 2:
                    target = "Animal"
                    filtered_df = (dataFrame[category == target])
                #
                elif categoryPick == 3:
                    target = "Beetles"
                    filtered_df=dataFrame[category == target]
                #
                filtered_df.to_csv(outputFile, index=False)
            #
        #
        except IOError:
            print('Not querying search function.')
            logger.debug('Not querying search function.')
        #
    #
#
