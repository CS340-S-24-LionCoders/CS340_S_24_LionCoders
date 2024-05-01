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
                    freq_counts = dataFrame.index.value_counts() #gets the number of occurences of each Taxonomic Group 
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
    def findCategory(dataFrame, userInput): # in progress
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
                    print(dataFrame[category == target])
                #
                elif categoryPick == 2:
                    target = "Animal"
                    print(dataFrame[category == target])
                #
                elif categoryPick == 3:
                    target = "Beetles"
                    print(dataFrame[category == target])
                #
            #
            elif userInput == "taxonomicGroup":
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
                        print(dataFrame[taxonomicGroup == target])
                    #
                    except:
                        print("Searching for taxonmic group Butterflies and Moths not working")
                        logger.debug("Searching for taxonmic group Butterflies and Moths not working")
                    #
                #
                elif taxonomicGroupPick == 2:
                    try:
                        target = "Fish"
                        print(dataFrame[taxonomicGroup == target])
                    #
                    except:
                        print("Searching for taxonmic group Fish not working")
                        logger.debug("Searching for taxonmic group Fish not working")
                    #
                #
                elif taxonomicGroupPick == 3:
                    try:
                        target = "Mammals"
                        print(dataFrame[taxonomicGroup == target])
                    #
                    except:
                        print("Searching for taxonmic group Mammals not working")
                        logger.debug("Searching for taxonmic group Mammals not working")
                    #
                #
                elif taxonomicGroupPick == 4:
                    try:
                        target = "Other Animals"
                        print(dataFrame[taxonomicGroup == target])
                    #
                    except:
                        print("Searching for taxonmic group Other Animals not working")
                        logger.debug("Searching for taxonmic group Other Animals not working")
                    #
                #
                elif taxonomicGroupPick == 5:
                    try:
                        target = "Birds"
                        print(dataFrame[taxonomicGroup == target])
                    #
                    except:
                        print("Searching for taxonmic group Birds not working")
                        logger.debug("Searching for taxonmic group Birds not working")
                    #
                #
                elif taxonomicGroupPick == 6:
                    try:
                        target = "Lady Beetles"
                        print(dataFrame[taxonomicGroup == target])
                    #
                    except:
                        print("Searching for taxonmic group Lady Beetles not working")
                        logger.debug("Searching for taxonmic group Lady Beetles not working")
                    #
                #
                elif taxonomicGroupPick == 7:
                    try:
                        target = "Amphibians"
                        print(dataFrame[taxonomicGroup == target])
                    #
                    except:
                        print("Searching for taxonmic group Amphibians not working")
                        logger.debug("Searching for taxonmic group Amphibians not working")
                    #
                #
                elif taxonomicGroupPick == 8:
                    try:
                        target = "Reptiles"
                        print(dataFrame[taxonomicGroup == target])
                    #
                    except:
                        print("Searching for taxonmic group Reptiles not working")
                        logger.debug("Searching for taxonmic group Reptiles not working")
                    #
                #
                elif taxonomicGroupPick == 9:
                    try:
                        target = "Flowering Plants"
                        print(dataFrame[taxonomicGroup == target])
                    #
                    except:
                        print("Searching for taxonmic group Flowering Plants not working")
                        logger.debug("Searching for taxonmic group Flowering Plants not working")
                    #
                #
                elif taxonomicGroupPick == 10:
                    try:
                        target = "Ferns and Fern Allies"
                        print(dataFrame[taxonomicGroup == target])
                    #
                    except:
                        print("Searching for taxonmic group Fish not working")
                        logger.debug("Searching for taxonmic group Fish not working")
                    #
                #
                elif taxonomicGroupPick == 11:
                    try:
                        target = "Mosses"
                        print(dataFrame[taxonomicGroup == target])
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
                        print(dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Other Mosses not working")
                        logger.debug("Searching for taxonmic subgroup Other Mosses not working")
                    #
                #
                elif taxonomicSubgroupPick == 2:
                    try:
                        target = "Grasses"
                        print(dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Grasses not working")
                        logger.debug("Searching for taxonmic subgroup Grasses not working")
                    #
                #
                elif taxonomicSubgroupPick == 3:
                    try:
                        target = "Asters, Goldenrods and Daisies"
                        print(dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Asters, Goldenrods and Daisies not working")
                        logger.debug("Searching for taxonmic subgroup Asters, Goldenrods and Daisies not working")
                    #
                #
                elif taxonomicSubgroupPick == 4:
                    try:
                        target = "Ferns"
                        print(dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Ferns not working")
                        logger.debug("Searching for taxonmic subgroup Ferns not working")
                    #
                #
                elif taxonomicSubgroupPick == 5:
                    try:
                        target = "Snakes"
                        print(dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Snakes not working")
                        logger.debug("Searching for taxonmic subgroup Snakes not working")
                    #
                #
                elif taxonomicSubgroupPick == 6:
                    try:
                        target = "Lizards"
                        print(dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Lizards not working")
                        logger.debug("Searching for taxonmic subgroup Lizards not working")
                    #
                #
                elif taxonomicSubgroupPick == 7:
                    try:
                        target = "Other Animals"
                        print(dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Other Animals not working")
                        logger.debug("Searching for taxonmic subgroup Other Animals not working")
                    #
                #
                elif taxonomicSubgroupPick == 8:
                    try:
                        target = "Bats"
                        print(dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Bats not working")
                        logger.debug("Searching for taxonmic subgroup Bats not working")
                    #
                #
                elif taxonomicSubgroupPick == 9:
                    try:
                        target = "Butterflies and Skippers"
                        print(dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Butterflies and Skippers not working")
                        logger.debug("Searching for taxonmic subgroup Butterflies and Skippers not working")
                    #
                #
                elif taxonomicSubgroupPick == 10:
                    try:
                        target = "Cardinals and Buntings"
                        print(dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Cardinals and Buntings not working")
                        logger.debug("Searching for taxonmic subgroup Cardinals and Buntings not working")
                    #
                #
                elif taxonomicSubgroupPick == 11:
                    try:
                        target = "Blackbirds and Orioles"
                        print(dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Blackbirds and Orioles not working")
                        logger.debug("Searching for taxonmic subgroup Blackbirds and Orioles not working")
                    #
                #
                elif taxonomicSubgroupPick == 12:
                    try:
                        target = "Frogs and Toads"
                        print(dataFrame[taxonomicSubgroup == target])
                    #
                    except:
                        print("Searching for taxonmic subgroup Frogs and Toads not working")
                        logger.debug("Searching for taxonmic subgroup Frogs and Toads not working")
                    #
                #
            #
        #   
        except IOError:
            print('Not querying search function.')
            logger.debug('Not querying search function.')
        #
    #
#
