from organism import organism


def main():
    print("Hello, World!")

    #test code 

    #call parent class
    testOrganism = organism()

    #testing Visiual Distributions method
    testOrganism.histogram()

    
    #testing other class methods
    testOrganism.addTaxonomicGroup("Amphibians")
    testOrganism.addTaxonomicSubgroup("Frogs and Toads")
    testOrganism.addScientificName("Anaxyrus americanus")
    testOrganism.addCommonName("American Toad")

    #Testing class variables 
    print(testOrganism.taxonomicGroup)
    print(testOrganism.taxonomicSubgroup)
    print(testOrganism.scientificName)
    print(testOrganism.commonName)

    #Testing searching 
    print("Welcome to our Biodiversity By Country -Ditsribution of Animals, Plants, and Natural Communities System! Please select what group you will like to view more closely! ")
    print("Options: category, taxonomicGroup, taxonomicSubgroup, scientificName, commonName ")
    userInput = input("Enter what group you will like to view: ")
    print(testOrganism.findCategory(userInput))





if __name__ == "__main__":
    main()
