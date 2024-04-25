import logging
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

logger = logging.getLogger(__name__)
logging.basicConfig(filename='Root\scientificCategory.log', encoding='utf-8', level=logging.DEBUG)

class scientificCategory():
    def __init__(self, config):
        super(config)
        self.category = []
        self.taxonomicGroup = []
        self.taxonomicSubgroup = [] = []
        self.scientificName = []
        self.commonName = []
        self.config = ()
    #
    try:
        logger.info('Reading csv file and storing into a dataframe...')
        dataframeCSV = pd.read_csv('Root\Input\data.csv',sep=',', index_col=0)
        logger.info('Reading csv file and storing into a dataframe successful!')
    except:
        print('Not loading csv file.')
        logger.debug('Not loading csv file.')
    #
    try:
        logger.info('Reading pickle file and storing into a dataframe...')
        dafaframePickle = pd.read_pickle('Root\Input\AlbanyBiodiversity.pkl',sep=',', index_col=0)
        dataPickle = pd.DataFrame(dafaframePickle)
        logger.info('Reading pickle file and storing into a dataframe successful!')
    except:
        print('Not loading pickle file.')
        logger.debug('Not loading pickle file.')
    #
    
    def violinPlot(data):
        try:
            logger.info('Displaying data as violin plot...')
            sns.set(style='whitegrid')
            dataset = sns.load_dataset(data)
            #seaborn.violinplot(x="an x-axis value" , y = "an y-axis value" data=dataset) //something is wrong with this line
        #
        except:
            print('Violin plot not working.')
            logger.debug('Violin plot not working.')
        #
    #
 
    def whiskerBoxPlot(data): 
        try:
            logger.info('Displaying data as whisker-box plot...')
             # Drop rows with missing values (NaNs)
            data["Taxonomic Subgroup"].dropna(inplace=True)
            
            # Convert data to numeric type (if necessary)
            sciCat = data.apply(pd.to_numeric, errors='coerce')
            
            # Check if data is empty after dropping NaNs
            if sciCat.empty:
                raise ValueError("DataFrame is empty after dropping NaNs")
            #
            plt.gca().tick_params(axis='x', labelsize=4) # Adjust font size of tick labels on x-axis
            plt.xticks(rotation=90)
            # Visualize data
            sns.boxplot(data=sciCat, notch=True, sym='b+', orient='vertical', whis=1.5)
            plt.xlabel("Category")
            plt.ylabel("Values")
            plt.title("Box-and-Whisker Plot")
            plt.savefig('Root\Output\whiskerBoxPlot.png')
            plt.show()
        #
        except Exception as e:
            print('Error occurred while creating whisker-box plot:', e)
            logger.error('Error occurred while creating whisker-box plot: %s', e)
        #
	#
 
    def scatterPlot(data):
        try:
            logger.info('Visualize data distributions in a scatter plot...')
            try:
                try:
                    # Calculate frequency counts of scientific categories
                    freq_counts = data["Taxonomic Subgroup"].index.value_counts() 
                    freq_counts_sorted = freq_counts.sort_index() 
                    n = len(freq_counts)
                    x = np.arange(1,n+1)
                    y = freq_counts_sorted
                    
                    # Visual dataset
                    plt.scatter(x, y)
                    plt.title('Scatter Plot of Yates Taxonomic Subgroup Biodiversity')
                    plt.xlabel('Taxonomic Subgroup')
                    plt.ylabel('Taxonomic Subgroup Frequency')
                    plt.savefig('Root\Output\scatterPlot.png')
                    plt.show()

                    logger.info('Completed scatter plot...')
                #
                except:
                    print("Not displaying scatter plot.")
                    logger.debug('Not displaying scatter plot.')
                #
            #
            except:
                print("Not reading dataset for scatter plot.")
                logger.debug('Not reading dataset for scatter plot.')
            #
        #
        except:
            print('Scatter plot not working.')
            logger.debug('Scatter plot not working.')
        #
    #
    
    #calculations section 
    
    def calculateJointCounts(df,a,b):
        try:
            logger.info('Calculating the joint counts...')
            grouped = df.groupby([a, b]).size().reset_index(name='Count')
            grouped = grouped.rename_axis("Joint Count Index")
            # Create a bar plot
            plt.figure(figsize=(10, 6))
            plt.bar(grouped.index, grouped['Count'])
            plt.xlabel('Taxonomic Combinations')
            plt.ylabel('Count')
            plt.title('Joint Counts for Taxonomic Combinations')
            plt.tight_layout()
            plt.show()
        #
        except:
            print('Not calculating the joint counts.')
            logger.debug('Not calculating the joint counts.')
        #
	#

    def calculateJointProbabilities(df, a, b):
        try:
            logger.info('Calculating the joint probabilities...')
            # Group by Subgroup and Taxonomic Group, then count occurrences
            grouped = df.groupby([a, b]).size().reset_index(name='Count')
            
            # Normalize counts to get proportions
            grouped['Proportion'] = grouped.groupby('Taxonomic Subgroup')['Count'].transform(lambda x: x / x.sum())
            
            # Visualize the results
            sns.barplot(data=grouped, x='Taxonomic Subgroup', y='Count', hue='Taxonomic Group',dodge=False)
            plt.title('Frequency of Taxonomic Groups by Taxonomic Subgroup')
            plt.xlabel('Taxonomic Subgroup')
            plt.ylabel('Count')
            plt.legend(title='Taxonomic Group')

            # Adjust width and heigh of png
            taxGroup = len(df['Taxonomic Group'].unique())
            plt.gcf().set_size_inches(taxGroup * 0.5, 6)  
            subgroup = len(df['Taxonomic Subgroup'].unique())
            plt.gcf().set_size_inches(subgroup * 0.5, 6)
            
            plt.gca().tick_params(axis='x', labelsize=8) # Adjust font size of tick labels on x-axis
            plt.xticks(rotation=90)

            plt.savefig('Root\Output\jointProbabilities.png')  # Save the plot as an image
            plt.show()
        #
        except Exception as e:
            print('Error occurred while calculating the joint probabilities:', e)
            logger.error('Error occurred while calculating the joint probabilities: %s', e)
        #
    #
    
    def calculateConditionalProbabilities(data, a, b):
        try:
            logger.info('Calculating the conditional probabilities...')
            prob = pd.crosstab(data[a], data[b], normalize='columns')
            return prob
        #
        except:
            print('Not calculating the conditional probabilities.')
            logger.debug('Not calculating the conditional probabilities.')
        #
    #
    
    def calculations():
        try:
            sciCat = pd.read_csv('Root\Input\YatesBiodiversity.csv',index_col="Scientific Category")
            try: 
                print("The mean is: ")
                print(sciCat.mean())

                print("The median is: ")
                print(sciCat.median())

                print("The standard deviation is ")
                print(sciCat.std())

            except:
                print('Caluculating mean, median, and standard deviation is not working.')
                logger.debug('Caluculating mean, median, and standard deviation is not working.')
        #
        except:
            print("Not reading dataset.")
            logger.debug('Not reading dataset.')
        #
    #

    #categorial attribute section

    def obtainSpecificValue(self, askedValue):
        try:
            logger.info('Obtaining a specific value...')
            ##will return the asked value
            return askedValue
        #
        except:
            print('Not obtaining a specific value.')
            logger.debug('Not obtaining a specific value.')
        #
	#
    
    def generatePermutationsOfNames(self, holder):
        try:
            logger.info('Generating ordered arrangement of names...')
            ##will return an ordered arrangement of names
            return holder
        #
        except:
            print('Not generating ordered arrangement of names.')
            logger.debug('Not generating ordered arrangement of names.')
        #
    #

    def generateCombinationsOfNames(self, holder):
        try:
            logger.info('Generating unordered arrangement of names...')
            ##will return a unordered arrangement of names
            return holder
        #
        except:
            print('Not generating unordered arrangement of names.')
            logger.debug('Not generating unordered arrangement of names.')
        #
	#
    
    def findOrganisim(self, userInput):
        try:
            logger.info('Querying search function...')
            #this function will return an organisim that user wants or will return 'NOT FOUND' if not in dataset
            return userInput 
        #
        except:
            print('Not querying search function.')
            logger.debug('Not querying search function.')
        #
	#
    x = calculateConditionalProbabilities(dataframeCSV, 'Taxonomic Subgroup', 'Taxonomic Group')
    print(x)
#