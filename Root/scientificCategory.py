import logging
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from organism import organism
import statistics as st
import itertools

logger = logging.getLogger(__name__)
logging.basicConfig(filename='Root\scientificCategory.log', encoding='utf-8', level=logging.DEBUG)

class scientificCategory(organism):
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
        ComplexCSV = pd.read_csv('Root\Input\YatesBiodiversity.csv',sep=',', index_col=0)
        logger.info('Reading csv file and storing into a dataframe successful!')
    #
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
            #data['Year Last Documented'] = data['Year Last Documented'].fillna(0)
            sns.violinplot(x = data['Category'], y = data['Year Last Documented'], data = data)
            plt.xlabel("Category")
            plt.ylabel("Year Last Documented")
            plt.title("Violin Plot for Year Last Documented")
            plt.savefig('Root\Output\ViolinPlot.png', dpi = 300)
            return plt
            #
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
            return plt
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
                    freq_counts = data['Taxonomic Subgroup'].value_counts()
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
                    logger.info('Completed scatter plot...')
                    return plt
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
            plt.savefig('Root\Output\jointCount.png')  # Save the plot as an image
            return plt
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
            return plt
        #
        except Exception as e:
            print('Error occurred while calculating the joint probabilities:', e)
            logger.error('Error occurred while calculating the joint probabilities: %s', e)
        #
    #
    
    def calculateConditionalProbabilities(data, a, b, outputFile):
        try:
            logger.info('Calculating the conditional probabilities...')
            prob = pd.crosstab(data[a], data[b], normalize='columns')
            prob.to_csv(outputFile, index=False)
        #
        except:
            print('Not calculating the conditional probabilities.')
            logger.debug('Not calculating the conditional probabilities.')
        #
    #

    def calculations(data, a, b):
        try: 
            grouped = data.groupby([a, b]).size().reset_index(name='Count')
            try:
                print("The mean is: ")
                print(grouped['Count'].mean())
            #
            except:
                print('Calculating mean is not working.')
                logger.debug('Calculating mean is not working.')
            #
            try:
                print("The median is: ")
                print(grouped['Count'].median())
            #
            except:
                print('Calculating median is not working.')
                logger.debug('Calculating median is not working.')
            #
            try:
                print("The standard deviation is ")
                print(grouped['Count'].std())
            #
            except:
                print('Calculating standard deviation is not working.')
                logger.debug('Calculating deviation is not working.')
            #
        #
        except:
            print('Calculating mean, median, and standard deviation is not working.')
            logger.debug('Calculating mean, median, and standard deviation is not working.')
        #
    #
    

    #categorial attribute section

    def obtainSpecificValue(data):
        try:
            logger.info('Obtaining a specific value...')

            # making sure that we know all the unique values of are columns
            uniqueCategory = data["Category"].unique()
            uniqueGroup = data["Taxonomic Group"].unique()
            uniqueSubgroup = data["Taxonomic Subgroup"].unique()
            uniqueScientificName = data["Scientific Name"].unique()
            uniqueCommonName = data["Common Name"].unique()
            uniqueYearLastDocumented = data["Year Last Documented"].unique()
            uniqueNYListingStatus = data["NY Listing Status"].unique()
            uniqueFederalListingStatus = data["Federal Listing Status"].unique()
            uniqueStateConservationRank = data["State Conservation Rank"].unique()
            uniqueGlobalConservationRank = data["Global Conservation Rank"].unique()
            uniqueDistributionStatus = data["Distribution Status"].unique()
            
            print("\tMenu:")
            print("\t\t 1) Look at the unique values available")
            print("\t\t 2) Find if a specific value exist")
            pick = int(input("Enter what you want to be: "))
            if pick == 1:
                print("\t Menu:")
                print("\t\t 1) Unique values for Category")
                print("\t\t 2) Unique values for Taxonomic Group")
                print("\t\t 3) Unique values for Taxonomic Subgroup")
                print("\t\t 4) Unique values for Scientific Name")
                print("\t\t 5) Unique values for Common Name")
                print("\t\t 6) Unique values for Year Last Documented")
                print("\t\t 7) Unique values for NY Listing Status")
                print("\t\t 8) Unique values for Federal Listing Status")
                print("\t\t 9) Unique values for State Conservation Rank")
                print("\t\t 10) Unique values for Global Conservation Rank")
                print("\t\t 11) Unique values for Distribution Status")
                
                askedValue = int(input("Enter what value you're looking for: "))
                if askedValue == 1:
                    print(uniqueCategory)
                #
                elif askedValue == 2:
                    print(uniqueGroup)
                #
                elif askedValue == 3:
                    print(uniqueSubgroup)
                #
                elif askedValue == 4:
                    print(uniqueScientificName)
                #
                elif askedValue == 5:
                    print(uniqueCommonName)
                #
                elif askedValue == 6:
                    print(uniqueYearLastDocumented)
                #
                elif askedValue == 7:
                    print(uniqueNYListingStatus)
                #
                elif askedValue == 8:
                    print(uniqueFederalListingStatus)
                # 
                elif askedValue == 9:
                    print(uniqueStateConservationRank)
                #
                elif askedValue == 10:
                    print(uniqueGlobalConservationRank)
                #
                elif askedValue == 11:
                    print(uniqueDistributionStatus)
                #
            #
            elif pick == 2:
                askedValue = str(input("What is the name of the value you want to find? "))

                array = [uniqueCategory, uniqueGroup, uniqueSubgroup, uniqueScientificName, uniqueCommonName, uniqueYearLastDocumented, uniqueNYListingStatus, uniqueFederalListingStatus, uniqueStateConservationRank, uniqueGlobalConservationRank, uniqueDistributionStatus]
                column_names = ['Category', 'Group', 'Subgroup', 'ScientificName', 'CommonName', 'YearLastDocumented', 'NYListingStatus', 'FederalListingStatus', 'StateConservationRank', 'GlobalConservationRank', 'DistributionStatus']

                value_found = False # flag so we know where to stop

                # Iterate over each array in the main array
                for column_name, unique_values in zip(column_names,array):
                    if askedValue in unique_values: # Check if the value exists in the current array
                        print(f"'{askedValue}' exists in the dataset. It can be found under the column '{column_name}'")
                        value_found = True
                        break
                    #
                #
                if not value_found: # If the value is not found in any array
                    print(f"'{askedValue}' does not exist in dataset.")
                #
            #
        #
        except:
            print('Not obtaining a specific value.')
            logger.debug('Not obtaining a specific value.')
        #
	#
    
    def generatePermutationsOfNames(data, length):
        try:
            logger.info('Generating ordered arrangement of names...')
            input = data['Common Name'].tolist()
            perm = list(itertools.permutations(input, r=length))
            for element in perm:
                print(element)
            #
        #
        except:
            print('Not generating ordered arrangement of names.')
            logger.debug('Not generating ordered arrangement of names.')
        #
    #

    def generateCombinationsOfNames(data, length):
        try:
            logger.info('Generating unordered arrangement of names...')
            names = data['Common Name'].tolist()
            all_combinations = list(itertools.combinations(names, length))
            print(all_combinations)
        #
        except:
            print('Not generating unordered arrangement of names.')
            logger.debug('Not generating unordered arrangement of names.')
        #
	#
    
    def findGroup(dataFrame, userInput, outputFile):
        try:
            logger.info('Querying search function...')
            #this is a boolean index series that goes by the Sub Taxonomic Group
            if userInput == "taxonomicGroup":
                taxonomicGroup = dataFrame["Taxonomic Group"]
                print("\tMenu:")
                print("\t\t1) Find all the Butterflies and Moths.")
                print("\t\t2) Find all the Fish.")
                print("\t\t3) Find all the Mammals.")
                print("\t\t4) Find all the  Other Animals.")
                print("\t\t5) Find all the Birds.")
                print("\t\t6) Find all the Lady Beetles.")
                print("\t\t7) Find all the  Amphibians.")
                print("\t\t8) Find all the Reptiles.")
                print("\t\t9) Find all the Flowering Plants.")
                print("\t\t10) Find all the Ferns and Fern Allies.")
                print("\t\t11) Find all the Mosses.")
                taxonomicGroupPick = int(input("Enter what you'd like to find: "))
                if taxonomicGroupPick == 1:
                    try:
                        target = "Butterflies and Moths"
                        filtered_df = (dataFrame[taxonomicGroup == target])
                    #
                    except:
                        print("Searching for taxonmic group Butterflies and Moths not working")
                        logger.debug("Searching for taxonmic group Butterflies and Moths not working")
                    #
                #
                elif taxonomicGroupPick == 2:
                    try:
                        target = "Fish"
                        filtered_df = (dataFrame[taxonomicGroup == target])
                    #
                    except:
                        print("Searching for taxonmic group Fish not working")
                        logger.debug("Searching for taxonmic group Fish not working")
                    #
                #
                elif taxonomicGroupPick == 3:
                    try:
                        target = "Mammals"
                        filtered_df = (dataFrame[taxonomicGroup == target])
                    #
                    except:
                        print("Searching for taxonmic group Mammals not working")
                        logger.debug("Searching for taxonmic group Mammals not working")
                    #
                #
                elif taxonomicGroupPick == 4:
                    try:
                        target = "Other Animals"
                        filtered_df = (dataFrame[taxonomicGroup == target])
                    #
                    except:
                        print("Searching for taxonmic group Other Animals not working")
                        logger.debug("Searching for taxonmic group Other Animals not working")
                    #
                #
                elif taxonomicGroupPick == 5:
                    try:
                        target = "Birds"
                        filtered_df = (dataFrame[taxonomicGroup == target])
                    #
                    except:
                        print("Searching for taxonmic group Birds not working")
                        logger.debug("Searching for taxonmic group Birds not working")
                    #
                #
                elif taxonomicGroupPick == 6:
                    try:
                        target = "Lady Beetles"
                        filtered_df = (dataFrame[taxonomicGroup == target])
                    #
                    except:
                        print("Searching for taxonmic group Lady Beetles not working")
                        logger.debug("Searching for taxonmic group Lady Beetles not working")
                    #
                #
                elif taxonomicGroupPick == 7:
                    try:
                        target = "Amphibians"
                        filtered_df = (dataFrame[taxonomicGroup == target])
                    #
                    except:
                        print("Searching for taxonmic group Amphibians not working")
                        logger.debug("Searching for taxonmic group Amphibians not working")
                    #
                #
                elif taxonomicGroupPick == 8:
                    try:
                        target = "Reptiles"
                        filtered_df = (dataFrame[taxonomicGroup == target])
                    #
                    except:
                        print("Searching for taxonmic group Reptiles not working")
                        logger.debug("Searching for taxonmic group Reptiles not working")
                    #
                #
                elif taxonomicGroupPick == 9:
                    try:
                        target = "Flowering Plants"
                        filtered_df = (dataFrame[taxonomicGroup == target])
                    #
                    except:
                        print("Searching for taxonmic group Flowering Plants not working")
                        logger.debug("Searching for taxonmic group Flowering Plants not working")
                    #
                #
                elif taxonomicGroupPick == 10:
                    try:
                        target = "Ferns and Fern Allies"
                        filtered_df = (dataFrame[taxonomicGroup == target])
                    #
                    except:
                        print("Searching for taxonmic group Fish not working")
                        logger.debug("Searching for taxonmic group Fish not working")
                    #
                #
                elif taxonomicGroupPick == 11:
                    try:
                        target = "Mosses"
                        filtered_df = (dataFrame[taxonomicGroup == target])
                    #
                    except:
                        print("Searching for taxonmic group Mosses not working")
                        logger.debug("Searching for taxonmic group Mosses not working")
                    #
                #
            #
            elif userInput == "taxonomicSubgroup":
                taxonomicSubgroup = dataFrame["Taxonomic Subgroup"]
                print("\tMenu:")
                print("\t\t1) Find all the Other Mosses.")
                print("\t\t2) Find all the Grasses.")
                print("\t\t3) Find all the Asters, Goldenrods and Daisies.")
                print("\t\t4) Find all the Ferns.")
                print("\t\t5) Find all the Snakes.")
                print("\t\t6) Find all the Lizards.")
                print("\t\t7) Find all the Other Animals.")
                print("\t\t8) Find all the Bats.")
                print("\t\t9) Find all the Butterflies and Skippers.")
                print("\t\t10) Find all the Cardinals and Buntings.")
                print("\t\t11) Find all the Blackbirds and Orioles.")
                print("\t\t12) Find all the Frogs and Toads.")
                taxonomicSubgroupPick = int(input("Enter what you'd like to find: "))

                if taxonomicSubgroupPick == 1:
                    try:
                        target = "Other Mosses"
                        filtered_df = (dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Other Mosses not working")
                        logger.debug("Searching for taxonmic subgroup Other Mosses not working")
                    #
                #
                elif taxonomicSubgroupPick == 2:
                    try:
                        target = "Grasses"
                        filtered_df = (dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Grasses not working")
                        logger.debug("Searching for taxonmic subgroup Grasses not working")
                    #
                #
                elif taxonomicSubgroupPick == 3:
                    try:
                        target = "Asters, Goldenrods and Daisies"
                        filtered_df = (dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Asters, Goldenrods and Daisies not working")
                        logger.debug("Searching for taxonmic subgroup Asters, Goldenrods and Daisies not working")
                    #
                #
                elif taxonomicSubgroupPick == 4:
                    try:
                        target = "Ferns"
                        filtered_df = (dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Ferns not working")
                        logger.debug("Searching for taxonmic subgroup Ferns not working")
                    #
                #
                elif taxonomicSubgroupPick == 5:
                    try:
                        target = "Snakes"
                        filtered_df = (dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Snakes not working")
                        logger.debug("Searching for taxonmic subgroup Snakes not working")
                    #
                #
                elif taxonomicSubgroupPick == 6:
                    try:
                        target = "Lizards"
                        filtered_df = (dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Lizards not working")
                        logger.debug("Searching for taxonmic subgroup Lizards not working")
                    #
                #
                elif taxonomicSubgroupPick == 7:
                    try:
                        target = "Other Animals"
                        filtered_df = (dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Other Animals not working")
                        logger.debug("Searching for taxonmic subgroup Other Animals not working")
                    #
                #
                elif taxonomicSubgroupPick == 8:
                    try:
                        target = "Bats"
                        filtered_df = (dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Bats not working")
                        logger.debug("Searching for taxonmic subgroup Bats not working")
                    #
                #
                elif taxonomicSubgroupPick == 9:
                    try:
                        target = "Butterflies and Skippers"
                        filtered_df = (dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Butterflies and Skippers not working")
                        logger.debug("Searching for taxonmic subgroup Butterflies and Skippers not working")
                    #
                #
                elif taxonomicSubgroupPick == 10:
                    try:
                        target = "Cardinals and Buntings"
                        filtered_df = (dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Cardinals and Buntings not working")
                        logger.debug("Searching for taxonmic subgroup Cardinals and Buntings not working")
                    #
                #
                elif taxonomicSubgroupPick == 11:
                    try:
                        target = "Blackbirds and Orioles"
                        filtered_df = (dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Blackbirds and Orioles not working")
                        logger.debug("Searching for taxonmic subgroup Blackbirds and Orioles not working")
                    #
                #
                elif taxonomicSubgroupPick == 12:
                    try:
                        target = "Frogs and Toads"
                        filtered_df = (dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Frogs and Toads not working")
                        logger.debug("Searching for taxonmic subgroup Frogs and Toads not working")
                    #
                #
            #
            else:
                print("Taxonomix Group Not Found")
                logger.debug("Taxonomix Group Not Found")
            #
            filtered_df.to_csv(outputFile, index=False)
        # 
        except:
            print('Not querying search function.')
            logger.debug('Not querying search function.')
        #
	#
#