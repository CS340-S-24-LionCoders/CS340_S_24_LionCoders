class conservationStatus:
    def __init__(self):
        self.NY_listingStatus = []
        self.federalListingStatus = []
        self.stateRank = []
        self.globalRank = []
        self.distributionStatus = []
    #
    def addListingNY(self, status):
        self.NY_listingStatus.append(status)
    #
    def addFederalListing(self, status):
        self.federalListingStatus.append(status)
    #
    def addGtateRank(self, rank):
        self.stateRank.append(rank)
    #
    def addGlobalRank(self, rank):
        self.globalRank.append(rank)
    #
    def addDistribution(self, status):
        self.distributionStatus.append(status)
    #
