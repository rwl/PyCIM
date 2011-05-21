# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Asset(IdentifiedObject):
    """Tangible resource of the utility, including power system equipment, cabinets, buildings, etc. For electrical network equipment, the role of the asset is defined through PowerSystemResource and its subclasses, defined mainly in the Wires model (refer to IEC61970-301 and model package IEC61970::Wires). Asset description places emphasis on the physical characteristics of the equipment fulfilling that role.
    """

    def __init__(self, category='', serialNumber='', manufacturedDate='', lotNumber='', critical=False, application='', initialLossOfLife=0.0, corporateCode='', purchasePrice=0.0, utcNumber='', installationDate='', initialCondition='', PowerSystemResources=None, Properties=None, acceptanceTest=None, ActivityRecords=None, Location=None, AssetFunctions=None, Measurements=None, AssetContainer=None, status=None, Ratings=None, electronicAddress=None, *args, **kw_args):
        """Initialises a new 'Asset' instance.

        @param category: Extension mechanism to accommodate utility-specific categorisation of Asset and its subtypes, according to their corporate standards, practices, and existing IT systems (e.g., for management of assets, maintenance, work, outage, customers, etc.). 
        @param serialNumber: Serial number of this asset. 
        @param manufacturedDate: Date this asset was manufactured. 
        @param lotNumber: Lot number for this asset. Even for the same model and version number, many assets are manufactured in lots. 
        @param critical: True if asset is considered critical for some reason (for example, a pole with critical attachments). 
        @param application: The way this particular asset is being used in this installation. For example, the application of a bushing when attached to a specific transformer winding would be one of the following: H1, H2, H3, H0, X1, X2, X3, X0, Y1, Y2, Y3, Y0. 
        @param initialLossOfLife: Whenever an asset is reconditioned, percentage of expected life for the asset when it was new; zero for new devices. 
        @param corporateCode: Code for this type of asset. 
        @param purchasePrice: Purchase price of asset. 
        @param utcNumber: Uniquely Tracked Commodity (UTC) number. 
        @param installationDate: (if applicable) Date current installation was completed, which may not be the same as the in-service date. Asset may have been installed at other locations previously. Ignored if asset is (1) not currently installed (e.g., stored in a depot) or (2) not intended to be installed (e.g., vehicle, tool). 
        @param initialCondition: Condition of asset in inventory or at time of installation. Examples include new, rebuilt, overhaul required, other. Refer to inspection data for information on the most current condition of the asset. 
        @param PowerSystemResources: All power system resources used to electrically model this asset. For example, transformer asset is electrically modelled with a transformer and its windings and tap changer.
        @param Properties: UserAttributes used to specify further properties of this asset. Use 'name' to specify what kind of property it is, and 'value.value' attribute for the actual value.
        @param acceptanceTest: Information on acceptance test.
        @param ActivityRecords: All activity records created for this asset.
        @param Location: Location of this asset.
        @param AssetFunctions:
        @param Measurements:
        @param AssetContainer:
        @param status: Status of this asset.
        @param Ratings: UserAttributes used to specify ratings of this asset. Ratings also can be used to set the initial value of operational measurement limits. Use 'name' to specify what kind of rating it is (e.g., voltage, current), and 'value' attribute for the actual value and unit information of the rating.
        @param electronicAddress: Electronic address.
        """
        #: Extension mechanism to accommodate utility-specific categorisation of Asset and its subtypes, according to their corporate standards, practices, and existing IT systems (e.g., for management of assets, maintenance, work, outage, customers, etc.).
        self.category = category

        #: Serial number of this asset.
        self.serialNumber = serialNumber

        #: Date this asset was manufactured.
        self.manufacturedDate = manufacturedDate

        #: Lot number for this asset. Even for the same model and version number, many assets are manufactured in lots.
        self.lotNumber = lotNumber

        #: True if asset is considered critical for some reason (for example, a pole with critical attachments).
        self.critical = critical

        #: The way this particular asset is being used in this installation. For example, the application of a bushing when attached to a specific transformer winding would be one of the following: H1, H2, H3, H0, X1, X2, X3, X0, Y1, Y2, Y3, Y0.
        self.application = application

        #: Whenever an asset is reconditioned, percentage of expected life for the asset when it was new; zero for new devices.
        self.initialLossOfLife = initialLossOfLife

        #: Code for this type of asset.
        self.corporateCode = corporateCode

        #: Purchase price of asset.
        self.purchasePrice = purchasePrice

        #: Uniquely Tracked Commodity (UTC) number.
        self.utcNumber = utcNumber

        #: (if applicable) Date current installation was completed, which may not be the same as the in-service date. Asset may have been installed at other locations previously. Ignored if asset is (1) not currently installed (e.g., stored in a depot) or (2) not intended to be installed (e.g., vehicle, tool).
        self.installationDate = installationDate

        #: Condition of asset in inventory or at time of installation. Examples include new, rebuilt, overhaul required, other. Refer to inspection data for information on the most current condition of the asset.
        self.initialCondition = initialCondition

        self._PowerSystemResources = []
        self.PowerSystemResources = [] if PowerSystemResources is None else PowerSystemResources

        self._Properties = []
        self.Properties = [] if Properties is None else Properties

        self.acceptanceTest = acceptanceTest

        self._ActivityRecords = []
        self.ActivityRecords = [] if ActivityRecords is None else ActivityRecords

        self._Location = None
        self.Location = Location

        self._AssetFunctions = []
        self.AssetFunctions = [] if AssetFunctions is None else AssetFunctions

        self._Measurements = []
        self.Measurements = [] if Measurements is None else Measurements

        self._AssetContainer = None
        self.AssetContainer = AssetContainer

        self.status = status

        self._Ratings = []
        self.Ratings = [] if Ratings is None else Ratings

        self.electronicAddress = electronicAddress

        super(Asset, self).__init__(*args, **kw_args)

    _attrs = ["category", "serialNumber", "manufacturedDate", "lotNumber", "critical", "application", "initialLossOfLife", "corporateCode", "purchasePrice", "utcNumber", "installationDate", "initialCondition"]
    _attr_types = {"category": str, "serialNumber": str, "manufacturedDate": str, "lotNumber": str, "critical": bool, "application": str, "initialLossOfLife": float, "corporateCode": str, "purchasePrice": float, "utcNumber": str, "installationDate": str, "initialCondition": str}
    _defaults = {"category": '', "serialNumber": '', "manufacturedDate": '', "lotNumber": '', "critical": False, "application": '', "initialLossOfLife": 0.0, "corporateCode": '', "purchasePrice": 0.0, "utcNumber": '', "installationDate": '', "initialCondition": ''}
    _enums = {}
    _refs = ["PowerSystemResources", "Properties", "acceptanceTest", "ActivityRecords", "Location", "AssetFunctions", "Measurements", "AssetContainer", "status", "Ratings", "electronicAddress"]
    _many_refs = ["PowerSystemResources", "Properties", "ActivityRecords", "AssetFunctions", "Measurements", "Ratings"]

    def getPowerSystemResources(self):
        """All power system resources used to electrically model this asset. For example, transformer asset is electrically modelled with a transformer and its windings and tap changer.
        """
        return self._PowerSystemResources

    def setPowerSystemResources(self, value):
        for p in self._PowerSystemResources:
            filtered = [q for q in p.Assets if q != self]
            self._PowerSystemResources._Assets = filtered
        for r in value:
            if self not in r._Assets:
                r._Assets.append(self)
        self._PowerSystemResources = value

    PowerSystemResources = property(getPowerSystemResources, setPowerSystemResources)

    def addPowerSystemResources(self, *PowerSystemResources):
        for obj in PowerSystemResources:
            if self not in obj._Assets:
                obj._Assets.append(self)
            self._PowerSystemResources.append(obj)

    def removePowerSystemResources(self, *PowerSystemResources):
        for obj in PowerSystemResources:
            if self in obj._Assets:
                obj._Assets.remove(self)
            self._PowerSystemResources.remove(obj)

    def getProperties(self):
        """UserAttributes used to specify further properties of this asset. Use 'name' to specify what kind of property it is, and 'value.value' attribute for the actual value.
        """
        return self._Properties

    def setProperties(self, value):
        for p in self._Properties:
            filtered = [q for q in p.PropertyAssets if q != self]
            self._Properties._PropertyAssets = filtered
        for r in value:
            if self not in r._PropertyAssets:
                r._PropertyAssets.append(self)
        self._Properties = value

    Properties = property(getProperties, setProperties)

    def addProperties(self, *Properties):
        for obj in Properties:
            if self not in obj._PropertyAssets:
                obj._PropertyAssets.append(self)
            self._Properties.append(obj)

    def removeProperties(self, *Properties):
        for obj in Properties:
            if self in obj._PropertyAssets:
                obj._PropertyAssets.remove(self)
            self._Properties.remove(obj)

    # Information on acceptance test.
    acceptanceTest = None

    def getActivityRecords(self):
        """All activity records created for this asset.
        """
        return self._ActivityRecords

    def setActivityRecords(self, value):
        for p in self._ActivityRecords:
            filtered = [q for q in p.Assets if q != self]
            self._ActivityRecords._Assets = filtered
        for r in value:
            if self not in r._Assets:
                r._Assets.append(self)
        self._ActivityRecords = value

    ActivityRecords = property(getActivityRecords, setActivityRecords)

    def addActivityRecords(self, *ActivityRecords):
        for obj in ActivityRecords:
            if self not in obj._Assets:
                obj._Assets.append(self)
            self._ActivityRecords.append(obj)

    def removeActivityRecords(self, *ActivityRecords):
        for obj in ActivityRecords:
            if self in obj._Assets:
                obj._Assets.remove(self)
            self._ActivityRecords.remove(obj)

    def getLocation(self):
        """Location of this asset.
        """
        return self._Location

    def setLocation(self, value):
        if self._Location is not None:
            filtered = [x for x in self.Location.Assets if x != self]
            self._Location._Assets = filtered

        self._Location = value
        if self._Location is not None:
            if self not in self._Location._Assets:
                self._Location._Assets.append(self)

    Location = property(getLocation, setLocation)

    def getAssetFunctions(self):
        
        return self._AssetFunctions

    def setAssetFunctions(self, value):
        for x in self._AssetFunctions:
            x.Asset = None
        for y in value:
            y._Asset = self
        self._AssetFunctions = value

    AssetFunctions = property(getAssetFunctions, setAssetFunctions)

    def addAssetFunctions(self, *AssetFunctions):
        for obj in AssetFunctions:
            obj.Asset = self

    def removeAssetFunctions(self, *AssetFunctions):
        for obj in AssetFunctions:
            obj.Asset = None

    def getMeasurements(self):
        
        return self._Measurements

    def setMeasurements(self, value):
        for x in self._Measurements:
            x.Asset = None
        for y in value:
            y._Asset = self
        self._Measurements = value

    Measurements = property(getMeasurements, setMeasurements)

    def addMeasurements(self, *Measurements):
        for obj in Measurements:
            obj.Asset = self

    def removeMeasurements(self, *Measurements):
        for obj in Measurements:
            obj.Asset = None

    def getAssetContainer(self):
        
        return self._AssetContainer

    def setAssetContainer(self, value):
        if self._AssetContainer is not None:
            filtered = [x for x in self.AssetContainer.Assets if x != self]
            self._AssetContainer._Assets = filtered

        self._AssetContainer = value
        if self._AssetContainer is not None:
            if self not in self._AssetContainer._Assets:
                self._AssetContainer._Assets.append(self)

    AssetContainer = property(getAssetContainer, setAssetContainer)

    # Status of this asset.
    status = None

    def getRatings(self):
        """UserAttributes used to specify ratings of this asset. Ratings also can be used to set the initial value of operational measurement limits. Use 'name' to specify what kind of rating it is (e.g., voltage, current), and 'value' attribute for the actual value and unit information of the rating.
        """
        return self._Ratings

    def setRatings(self, value):
        for p in self._Ratings:
            filtered = [q for q in p.RatingAssets if q != self]
            self._Ratings._RatingAssets = filtered
        for r in value:
            if self not in r._RatingAssets:
                r._RatingAssets.append(self)
        self._Ratings = value

    Ratings = property(getRatings, setRatings)

    def addRatings(self, *Ratings):
        for obj in Ratings:
            if self not in obj._RatingAssets:
                obj._RatingAssets.append(self)
            self._Ratings.append(obj)

    def removeRatings(self, *Ratings):
        for obj in Ratings:
            if self in obj._RatingAssets:
                obj._RatingAssets.remove(self)
            self._Ratings.remove(obj)

    # Electronic address.
    electronicAddress = None

