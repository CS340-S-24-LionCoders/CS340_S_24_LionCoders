import logging
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)
logging.basicConfig(filename='Root\organism.log', encoding='utf-8', level=logging.DEBUG)

class organism:
    def __init__(self):
        self.category = ["Animal", "Plant"]
        self.taxonomicGroup = ["Birds", "Amphibians"]
        self.taxonomicSubgroup = ["Frogs and Toads", "Blackbirds and Orioles"]
        self.scientificName = ["Sturnella magna", "Ambystoma laterale"]
        self.commonName = ["Bullfrog", "Wood Frog"]

    #config dictionary 
    config =  dict()
    
    def histogram():
        try:
            logger.info('Visualize data distributions in a histogram...')
        #
        except:
            print('Histogram not working.')
            logger.debug('Histogram not working.')
        #
    #
    def linePlot():
        try:
            logger.info('Visualize data distributions in a line plot...')
            try:
                df = pd.read_csv('Root\Input\YatesBiodiversity.csv',index_col="Taxonomic Group")
                try:
                    freq_counts = df.index.value_counts() #gets the number of occurences of each Taxonomic Group 
                    freq_counts_sorted = freq_counts.sort_index() #sorts by index 
                    n = len(freq_counts)
                    x = np.arange(1,n+1)
                    y = freq_counts_sorted
                    plt.plot(x, y)
                    plt.title('Line Plot of Yates Biodiversity')
                    plt.xlabel('Taxonomic Groups')
                    plt.ylabel('Taxonomic Group Frequency')
                    plt.savefig('Root\Output\linePlot.png', dpi=300)
                    plt.show()
                    logger.info('Completed line plot...')
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
        #
    #

    #query search function
    def findCategory(self, userInput):
        try:
            logger.info('Query searching function...')
            print("Please select what action you would like to take! ")          

            #this function will return either a table and or list of what the user ask for 
            if userInput == "category":
	            #do task 1
                category = pd.DataFrame(self.category)
                print(category)                   
            elif userInput == "taxonomicGroup":
	            #do task 2
                taxonomicGroup = pd.DataFrame(self.taxonomicGroup)
                print(taxonomicGroup)
            elif userInput == "taxonomicSubgroup":
	            #do task 3
                taxonomicSubgroup = pd.DataFrame(self.taxonomicSubgroup)
                print(taxonomicSubgroup)
            elif userInput == "scientificName":
	            #do task 4
                scientificName = pd.DataFrame(self.scientificName)
                print(scientificName)
            elif userInput == "commonName":
	            #do task 5
                commonName = pd.DataFrame(self.category)
                print(commonName)
                 
        except IOError:
            print('Not querying search function.')
            logger.debug('Not querying search function.')
        #

    #
    def addCategory(self, category):
        self.category.append(category)
    #
    def addTaxonomicGroup(self, group):
        self.taxonomicGroup.append(group)
    #
    def addTaxonomicSubgroup(self, subgroup):
        self.taxonomicSubgroup.append(subgroup)
    #
    def addScientificName(self, name):
        self.scientificName.append(name)
    #
    def addCommonName(self, name):
        self.commonName.append(name)
    #
#