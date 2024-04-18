from organism import organism


def main():
    print("Hello, World!")

    #test code 
    testOrganism = organism()

    testOrganism.addTaxonomicGroup("Amphibians")
    testOrganism.addTaxonomicSubgroup("Frogs and Toads")
    testOrganism.addScientificName("Anaxyrus americanus")
    testOrganism.addCommonName("American Toad")

    print("Testing methods in class")
    print(testOrganism.taxonomicGroup)
    print(testOrganism.taxonomicSubgroup)
    print(testOrganism.scientificName)
    print(testOrganism.commonName)

    print("Testing searching")
    print(testOrganism.findCategory("category"))





if __name__ == "__main__":
    main()
