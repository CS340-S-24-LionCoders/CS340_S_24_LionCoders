import logging
import matplotlib.pyplot as plt
import pandas as pd

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

    def histogram():
        try:
            logger.info('Visualize data distributions in a histogram...')
            try:
                df = pd.read_csv('Root\Input\YatesBiodiversity.csv',sep=',',index_col="Taxonomic Group")
                try:
                    df['freq'] = df.groupby('Taxonomic Group')['Taxonomic Group'].transform('count')
                    grouped_taxonmic = df.groupby('Taxonomic Group').count()
                    freq_counts = df['Taxonomic Group'].value_counts()
                    print(freq_counts)
                    df['Taxonomic Group'] = df.groupby('Taxonomic Group')['Taxonomic Group'].transform('count')
                    
                    plt.hist(grouped_taxonmic, bins=0, edgecolor='k', linewidth=1)
                             #('Flowering Plants','Mosses','Amphibians','Animal Assemblages','Beetles','Birds', 'Butterflies and Moths','Ferns and Fern Allies','Fish','Freshwater Nontidal Wetlands','Mammals','Other Animals','Reptiles')
                    plt.ylabel('Taxonomic Group Frequency')
                    plt.xlabel('Taxonomic Groups')
                    plt.title('Histogram of Yates Biodiversity')
                    plt.show()
                    plt.savefig('Root\Output\histogram.png', dpi='figure', bbox_inches=None)
                    logger.info('Successfully histogram visualize.')
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

    def linePlot():
        try:
            logger.info('Visualize data distributions in a line plot...')
            plt.plot(x, y)
            plt.title('Line Plot of Yates Biodiversity')
            plt.xlabel('Taxonomic Groups')
            plt.ylabel('Taxonomic Group Frequency')
            plt.show()
            logger.info('Completed line plot...')

        #
        except:
            print('Line plot not working.')
            logger.debug('Line plot not working.')
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
    histogram()
#

#Uncomment the code below to test

#taxonomyNew = taxonomy()

#taxonomyNew.addTaxonomicGroup("Amphibians")
#taxonomyNew.addTaxonomicSubgroup("Frogs and Toads")
#taxonomyNew.addScientificName("Anaxyrus americanus")
#taxonomyNew.addCommonName("American Toad")

#print("Testing methods in class")
#print(taxonomyNew.taxonomicGroup)
#print(taxonomyNew.taxonomicSubgroup)
#print(taxonomyNew.scientificName)
#print(taxonomyNew.commonName)