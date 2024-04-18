import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='Root\organism.log', encoding='utf-8', level=logging.DEBUG)

class organism:
    def __init__(self):
        self.category = []
        self.taxonomicGroup = []
        self.taxonomicSubgroup = [] = []
        self.scientificName = []
        self.commonName = []

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
            #this function will return either a table and or list of what the user ask for  
            return userInput
        #
        except:
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