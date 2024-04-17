import pandas as pd
import seaborn

class scientificCategory(organisim):
    def __init__(self, config):
        super(config)
        self.category = []
        self.taxonomicGroup = []
        self.taxonomicSubgroup = [] = []
        self.scientificName = []
        self.commonName = []
        self.config = ()

    #read dataframe 
    df = pd.read_csv('Input\Biodiversity_by_County_-_Distribution_of_Animals_Plants_and_Natural_Communities.csv', index_col='county')
    data = pd.DataFrame(df)


    #visuial display section
    def violinPlot():
        seaborn.set(style='whitegrid')
        dataset = seaborn.load_dataset(data)
        #seaborn.violinplot(x="an x-axis value" , y = "an y-axis value" data=dataset) //something is wrong with this line

    ## visual data in whisker-box plot
    def whiskerBoxPlot():
        plt.boxplot(dataset)
        plt.show()
	#
    def scatterPlot():
    ## visual data in scatter plot
        plt.scatter(x,y)
        plt.show()
    #

    #calculations section 
    def calculateJointCounts(self,holder):
		##will calculate joint counts and return result
        return holder
	#
    def calculateJointCounts(self, holder):
		##will calculate joint counts and return result
        return holder 
    #
    def calculateJointProbabilities(self, holder):
		##will calculate joint probabilities and return result
        return holder
	#
    def calculateConditionalProbabilities(self, holder):
		##will calculate conditional probabilities and return result
        return holder
    #
    def calculateMean(self, holder):
		##will calculate mean and return result
        return holder
    #
    def calculateMedian(self, holder):
		##will calculate median and return result
        return holder
    #
    def calculateSTD(self, holder):
		##will calculate STD and return result
        return holder 
    #


    #categorial attribute section
    def obtainSpecificValue(self, askedValue):
		##will return the asked value
        return askedValue
	#
    
    def generatePermutationsOfNames(self, holder):
		##will return an ordered arrangement of names
        return holder
    #
    def generateCombinationsOfNames(self, holder):
		##will return a unordered arrangement of names
        return holder
	#

    

    #query search function
    def findOrganisim(self, userInput):
        #this function will return an organisim that user wants or will return 'NOT FOUND' if not in dataset
        return userInput 

    
#