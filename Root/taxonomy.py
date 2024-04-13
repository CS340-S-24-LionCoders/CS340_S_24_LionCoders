class taxonomy:
    def __init__(self):
        self.category = []
        self.taxonomicGroup = []
        self.taxonomicSubgroup = [] = []
        self.scientificName = []
        self.commonName = []
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