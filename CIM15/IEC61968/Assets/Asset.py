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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Asset(IdentifiedObject):
    """Tangible resource of the utility, including power system equipment, cabinets, buildings, etc. For electrical network equipment, the role of the asset is defined through PowerSystemResource and its subclasses, defined mainly in the Wires model (refer to IEC61970-301 and model package IEC61970::Wires). Asset description places emphasis on the physical characteristics of the equipment fulfilling that role.Tangible resource of the utility, including power system equipment, cabinets, buildings, etc. For electrical network equipment, the role of the asset is defined through PowerSystemResource and its subclasses, defined mainly in the Wires model (refer to IEC61970-301 and model package IEC61970::Wires). Asset description places emphasis on the physical characteristics of the equipment fulfilling that role.
    """

    def __init__(self, corporateCode='', utcNumber='', initialCondition='', category='', serialNumber='', critical=False, application='', purchasePrice=0.0, initialLossOfLife=0.0, manufacturedDate='', installationDate='', lotNumber='', DocumentRoles=None, Mediums=None, ErpRecDeliveryItems=None, Ratings=None, ToAssetRoles=None, electronicAddress=None, FromAssetRoles=None, AssetFunctions=None, ErpItemMaster=None, ErpInventory=None, ReliabilityInfos=None, AssetInfo=None, WorkTask=None, acceptanceTest=None, ErpOrganisationRoles=None, ScheduledEvents=None, AssetContainer=None, AssetPropertyCurves=None, ChangeItems=None, ActivityRecords=None, Location=None, status=None, PowerSystemResources=None, FinancialInfo=None, Properties=None, Measurements=None, *args, **kw_args):
        """Initialises a new 'Asset' instance.

        @param corporateCode: Code for this type of asset. 
        @param utcNumber: Uniquely tracked commodity (UTC) number. 
        @param initialCondition: Condition of asset in inventory or at time of installation. Examples include new, rebuilt, overhaul required, other. Refer to inspection data for information on the most current condition of the asset. 
        @param category: Extension mechanism to accommodate utility-specific categorisation of Asset and its subtypes, according to their corporate standards, practices, and existing IT systems (e.g., for management of assets, maintenance, work, outage, customers, etc.). 
        @param serialNumber: Serial number of this asset. 
        @param critical: True if asset is considered critical for some reason (for example, a pole with critical attachments). 
        @param application: The way this particular asset is being used in this installation. For example, the application of a bushing when attached to a specific transformer winding would be one of the following: H1, H2, H3, H0, X1, X2, X3, X0, Y1, Y2, Y3, Y0. 
        @param purchasePrice: Purchase price of asset. 
        @param initialLossOfLife: Whenever an asset is reconditioned, percentage of expected life for the asset when it was new; zero for new devices. 
        @param manufacturedDate: Date this asset was manufactured. 
        @param installationDate: (if applicable) Date current installation was completed, which may not be the same as the in-service date. Asset may have been installed at other locations previously. Ignored if asset is (1) not currently installed (e.g., stored in a depot) or (2) not intended to be installed (e.g., vehicle, tool). 
        @param lotNumber: Lot number for this asset. Even for the same model and version number, many assets are manufactured in lots. 
        @param DocumentRoles:
        @param Mediums:
        @param ErpRecDeliveryItems:
        @param Ratings: UserAttributes used to specify ratings of this asset. Ratings also can be used to set the initial value of operational measurement limits. Use 'name' to specify what kind of rating it is (e.g., voltage, current), and 'value' attribute for the actual value and unit information of the rating.
        @param ToAssetRoles:
        @param electronicAddress: Electronic address.
        @param FromAssetRoles:
        @param AssetFunctions:
        @param ErpItemMaster:
        @param ErpInventory:
        @param ReliabilityInfos:
        @param AssetInfo: Data applicable to this asset.
        @param WorkTask:
        @param acceptanceTest: Information on acceptance test.
        @param ErpOrganisationRoles:
        @param ScheduledEvents:
        @param AssetContainer:
        @param AssetPropertyCurves:
        @param ChangeItems:
        @param ActivityRecords: All activity records created for this asset.
        @param Location: Location of this asset.
        @param status: Status of this asset.
        @param PowerSystemResources: All power system resources used to electrically model this asset. For example, transformer asset is electrically modelled with a transformer and its windings and tap changer.
        @param FinancialInfo:
        @param Properties: UserAttributes used to specify further properties of this asset. Use 'name' to specify what kind of property it is, and 'value.value' attribute for the actual value.
        @param Measurements:
        """
        #: Code for this type of asset.
        self.corporateCode = corporateCode

        #: Uniquely tracked commodity (UTC) number.
        self.utcNumber = utcNumber

        #: Condition of asset in inventory or at time of installation. Examples include new, rebuilt, overhaul required, other. Refer to inspection data for information on the most current condition of the asset.
        self.initialCondition = initialCondition

        #: Extension mechanism to accommodate utility-specific categorisation of Asset and its subtypes, according to their corporate standards, practices, and existing IT systems (e.g., for management of assets, maintenance, work, outage, customers, etc.).
        self.category = category

        #: Serial number of this asset.
        self.serialNumber = serialNumber

        #: True if asset is considered critical for some reason (for example, a pole with critical attachments).
        self.critical = critical

        #: The way this particular asset is being used in this installation. For example, the application of a bushing when attached to a specific transformer winding would be one of the following: H1, H2, H3, H0, X1, X2, X3, X0, Y1, Y2, Y3, Y0.
        self.application = application

        #: Purchase price of asset.
        self.purchasePrice = purchasePrice

        #: Whenever an asset is reconditioned, percentage of expected life for the asset when it was new; zero for new devices.
        self.initialLossOfLife = initialLossOfLife

        #: Date this asset was manufactured.
        self.manufacturedDate = manufacturedDate

        #: (if applicable) Date current installation was completed, which may not be the same as the in-service date. Asset may have been installed at other locations previously. Ignored if asset is (1) not currently installed (e.g., stored in a depot) or (2) not intended to be installed (e.g., vehicle, tool).
        self.installationDate = installationDate

        #: Lot number for this asset. Even for the same model and version number, many assets are manufactured in lots.
        self.lotNumber = lotNumber

        self._DocumentRoles = []
        self.DocumentRoles = [] if DocumentRoles is None else DocumentRoles

        self._Mediums = []
        self.Mediums = [] if Mediums is None else Mediums

        self._ErpRecDeliveryItems = []
        self.ErpRecDeliveryItems = [] if ErpRecDeliveryItems is None else ErpRecDeliveryItems

        self._Ratings = []
        self.Ratings = [] if Ratings is None else Ratings

        self._ToAssetRoles = []
        self.ToAssetRoles = [] if ToAssetRoles is None else ToAssetRoles

        self.electronicAddress = electronicAddress

        self._FromAssetRoles = []
        self.FromAssetRoles = [] if FromAssetRoles is None else FromAssetRoles

        self._AssetFunctions = []
        self.AssetFunctions = [] if AssetFunctions is None else AssetFunctions

        self._ErpItemMaster = None
        self.ErpItemMaster = ErpItemMaster

        self._ErpInventory = None
        self.ErpInventory = ErpInventory

        self._ReliabilityInfos = []
        self.ReliabilityInfos = [] if ReliabilityInfos is None else ReliabilityInfos

        self._AssetInfo = None
        self.AssetInfo = AssetInfo

        self._WorkTask = None
        self.WorkTask = WorkTask

        self.acceptanceTest = acceptanceTest

        self._ErpOrganisationRoles = []
        self.ErpOrganisationRoles = [] if ErpOrganisationRoles is None else ErpOrganisationRoles

        self._ScheduledEvents = []
        self.ScheduledEvents = [] if ScheduledEvents is None else ScheduledEvents

        self._AssetContainer = None
        self.AssetContainer = AssetContainer

        self._AssetPropertyCurves = []
        self.AssetPropertyCurves = [] if AssetPropertyCurves is None else AssetPropertyCurves

        self._ChangeItems = []
        self.ChangeItems = [] if ChangeItems is None else ChangeItems

        self._ActivityRecords = []
        self.ActivityRecords = [] if ActivityRecords is None else ActivityRecords

        self._Location = None
        self.Location = Location

        self.status = status

        self._PowerSystemResources = []
        self.PowerSystemResources = [] if PowerSystemResources is None else PowerSystemResources

        self._FinancialInfo = None
        self.FinancialInfo = FinancialInfo

        self._Properties = []
        self.Properties = [] if Properties is None else Properties

        self._Measurements = []
        self.Measurements = [] if Measurements is None else Measurements

        super(Asset, self).__init__(*args, **kw_args)

    _attrs = ["corporateCode", "utcNumber", "initialCondition", "category", "serialNumber", "critical", "application", "purchasePrice", "initialLossOfLife", "manufacturedDate", "installationDate", "lotNumber"]
    _attr_types = {"corporateCode": str, "utcNumber": str, "initialCondition": str, "category": str, "serialNumber": str, "critical": bool, "application": str, "purchasePrice": float, "initialLossOfLife": float, "manufacturedDate": str, "installationDate": str, "lotNumber": str}
    _defaults = {"corporateCode": '', "utcNumber": '', "initialCondition": '', "category": '', "serialNumber": '', "critical": False, "application": '', "purchasePrice": 0.0, "initialLossOfLife": 0.0, "manufacturedDate": '', "installationDate": '', "lotNumber": ''}
    _enums = {}
    _refs = ["DocumentRoles", "Mediums", "ErpRecDeliveryItems", "Ratings", "ToAssetRoles", "electronicAddress", "FromAssetRoles", "AssetFunctions", "ErpItemMaster", "ErpInventory", "ReliabilityInfos", "AssetInfo", "WorkTask", "acceptanceTest", "ErpOrganisationRoles", "ScheduledEvents", "AssetContainer", "AssetPropertyCurves", "ChangeItems", "ActivityRecords", "Location", "status", "PowerSystemResources", "FinancialInfo", "Properties", "Measurements"]
    _many_refs = ["DocumentRoles", "Mediums", "ErpRecDeliveryItems", "Ratings", "ToAssetRoles", "FromAssetRoles", "AssetFunctions", "ReliabilityInfos", "ErpOrganisationRoles", "ScheduledEvents", "AssetPropertyCurves", "ChangeItems", "ActivityRecords", "PowerSystemResources", "Properties", "Measurements"]

    def getDocumentRoles(self):
        
        return self._DocumentRoles

    def setDocumentRoles(self, value):
        for x in self._DocumentRoles:
            x.Asset = None
        for y in value:
            y._Asset = self
        self._DocumentRoles = value

    DocumentRoles = property(getDocumentRoles, setDocumentRoles)

    def addDocumentRoles(self, *DocumentRoles):
        for obj in DocumentRoles:
            obj.Asset = self

    def removeDocumentRoles(self, *DocumentRoles):
        for obj in DocumentRoles:
            obj.Asset = None

    def getMediums(self):
        
        return self._Mediums

    def setMediums(self, value):
        for p in self._Mediums:
            filtered = [q for q in p.Assets if q != self]
            self._Mediums._Assets = filtered
        for r in value:
            if self not in r._Assets:
                r._Assets.append(self)
        self._Mediums = value

    Mediums = property(getMediums, setMediums)

    def addMediums(self, *Mediums):
        for obj in Mediums:
            if self not in obj._Assets:
                obj._Assets.append(self)
            self._Mediums.append(obj)

    def removeMediums(self, *Mediums):
        for obj in Mediums:
            if self in obj._Assets:
                obj._Assets.remove(self)
            self._Mediums.remove(obj)

    def getErpRecDeliveryItems(self):
        
        return self._ErpRecDeliveryItems

    def setErpRecDeliveryItems(self, value):
        for p in self._ErpRecDeliveryItems:
            filtered = [q for q in p.Assets if q != self]
            self._ErpRecDeliveryItems._Assets = filtered
        for r in value:
            if self not in r._Assets:
                r._Assets.append(self)
        self._ErpRecDeliveryItems = value

    ErpRecDeliveryItems = property(getErpRecDeliveryItems, setErpRecDeliveryItems)

    def addErpRecDeliveryItems(self, *ErpRecDeliveryItems):
        for obj in ErpRecDeliveryItems:
            if self not in obj._Assets:
                obj._Assets.append(self)
            self._ErpRecDeliveryItems.append(obj)

    def removeErpRecDeliveryItems(self, *ErpRecDeliveryItems):
        for obj in ErpRecDeliveryItems:
            if self in obj._Assets:
                obj._Assets.remove(self)
            self._ErpRecDeliveryItems.remove(obj)

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

    def getToAssetRoles(self):
        
        return self._ToAssetRoles

    def setToAssetRoles(self, value):
        for x in self._ToAssetRoles:
            x.FromAsset = None
        for y in value:
            y._FromAsset = self
        self._ToAssetRoles = value

    ToAssetRoles = property(getToAssetRoles, setToAssetRoles)

    def addToAssetRoles(self, *ToAssetRoles):
        for obj in ToAssetRoles:
            obj.FromAsset = self

    def removeToAssetRoles(self, *ToAssetRoles):
        for obj in ToAssetRoles:
            obj.FromAsset = None

    # Electronic address.
    electronicAddress = None

    def getFromAssetRoles(self):
        
        return self._FromAssetRoles

    def setFromAssetRoles(self, value):
        for x in self._FromAssetRoles:
            x.ToAsset = None
        for y in value:
            y._ToAsset = self
        self._FromAssetRoles = value

    FromAssetRoles = property(getFromAssetRoles, setFromAssetRoles)

    def addFromAssetRoles(self, *FromAssetRoles):
        for obj in FromAssetRoles:
            obj.ToAsset = self

    def removeFromAssetRoles(self, *FromAssetRoles):
        for obj in FromAssetRoles:
            obj.ToAsset = None

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

    def getErpItemMaster(self):
        
        return self._ErpItemMaster

    def setErpItemMaster(self, value):
        if self._ErpItemMaster is not None:
            self._ErpItemMaster._Asset = None

        self._ErpItemMaster = value
        if self._ErpItemMaster is not None:
            self._ErpItemMaster.Asset = None
            self._ErpItemMaster._Asset = self

    ErpItemMaster = property(getErpItemMaster, setErpItemMaster)

    def getErpInventory(self):
        
        return self._ErpInventory

    def setErpInventory(self, value):
        if self._ErpInventory is not None:
            self._ErpInventory._Asset = None

        self._ErpInventory = value
        if self._ErpInventory is not None:
            self._ErpInventory.Asset = None
            self._ErpInventory._Asset = self

    ErpInventory = property(getErpInventory, setErpInventory)

    def getReliabilityInfos(self):
        
        return self._ReliabilityInfos

    def setReliabilityInfos(self, value):
        for p in self._ReliabilityInfos:
            filtered = [q for q in p.Assets if q != self]
            self._ReliabilityInfos._Assets = filtered
        for r in value:
            if self not in r._Assets:
                r._Assets.append(self)
        self._ReliabilityInfos = value

    ReliabilityInfos = property(getReliabilityInfos, setReliabilityInfos)

    def addReliabilityInfos(self, *ReliabilityInfos):
        for obj in ReliabilityInfos:
            if self not in obj._Assets:
                obj._Assets.append(self)
            self._ReliabilityInfos.append(obj)

    def removeReliabilityInfos(self, *ReliabilityInfos):
        for obj in ReliabilityInfos:
            if self in obj._Assets:
                obj._Assets.remove(self)
            self._ReliabilityInfos.remove(obj)

    def getAssetInfo(self):
        """Data applicable to this asset.
        """
        return self._AssetInfo

    def setAssetInfo(self, value):
        if self._AssetInfo is not None:
            self._AssetInfo._Assets = None

        self._AssetInfo = value
        if self._AssetInfo is not None:
            self._AssetInfo.Assets = None
            self._AssetInfo._Assets = self

    AssetInfo = property(getAssetInfo, setAssetInfo)

    def getWorkTask(self):
        
        return self._WorkTask

    def setWorkTask(self, value):
        if self._WorkTask is not None:
            filtered = [x for x in self.WorkTask.Assets if x != self]
            self._WorkTask._Assets = filtered

        self._WorkTask = value
        if self._WorkTask is not None:
            if self not in self._WorkTask._Assets:
                self._WorkTask._Assets.append(self)

    WorkTask = property(getWorkTask, setWorkTask)

    # Information on acceptance test.
    acceptanceTest = None

    def getErpOrganisationRoles(self):
        
        return self._ErpOrganisationRoles

    def setErpOrganisationRoles(self, value):
        for x in self._ErpOrganisationRoles:
            x.Asset = None
        for y in value:
            y._Asset = self
        self._ErpOrganisationRoles = value

    ErpOrganisationRoles = property(getErpOrganisationRoles, setErpOrganisationRoles)

    def addErpOrganisationRoles(self, *ErpOrganisationRoles):
        for obj in ErpOrganisationRoles:
            obj.Asset = self

    def removeErpOrganisationRoles(self, *ErpOrganisationRoles):
        for obj in ErpOrganisationRoles:
            obj.Asset = None

    def getScheduledEvents(self):
        
        return self._ScheduledEvents

    def setScheduledEvents(self, value):
        for p in self._ScheduledEvents:
            filtered = [q for q in p.Assets if q != self]
            self._ScheduledEvents._Assets = filtered
        for r in value:
            if self not in r._Assets:
                r._Assets.append(self)
        self._ScheduledEvents = value

    ScheduledEvents = property(getScheduledEvents, setScheduledEvents)

    def addScheduledEvents(self, *ScheduledEvents):
        for obj in ScheduledEvents:
            if self not in obj._Assets:
                obj._Assets.append(self)
            self._ScheduledEvents.append(obj)

    def removeScheduledEvents(self, *ScheduledEvents):
        for obj in ScheduledEvents:
            if self in obj._Assets:
                obj._Assets.remove(self)
            self._ScheduledEvents.remove(obj)

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

    def getAssetPropertyCurves(self):
        
        return self._AssetPropertyCurves

    def setAssetPropertyCurves(self, value):
        for p in self._AssetPropertyCurves:
            filtered = [q for q in p.Assets if q != self]
            self._AssetPropertyCurves._Assets = filtered
        for r in value:
            if self not in r._Assets:
                r._Assets.append(self)
        self._AssetPropertyCurves = value

    AssetPropertyCurves = property(getAssetPropertyCurves, setAssetPropertyCurves)

    def addAssetPropertyCurves(self, *AssetPropertyCurves):
        for obj in AssetPropertyCurves:
            if self not in obj._Assets:
                obj._Assets.append(self)
            self._AssetPropertyCurves.append(obj)

    def removeAssetPropertyCurves(self, *AssetPropertyCurves):
        for obj in AssetPropertyCurves:
            if self in obj._Assets:
                obj._Assets.remove(self)
            self._AssetPropertyCurves.remove(obj)

    def getChangeItems(self):
        
        return self._ChangeItems

    def setChangeItems(self, value):
        for x in self._ChangeItems:
            x.Asset = None
        for y in value:
            y._Asset = self
        self._ChangeItems = value

    ChangeItems = property(getChangeItems, setChangeItems)

    def addChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj.Asset = self

    def removeChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj.Asset = None

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

    # Status of this asset.
    status = None

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

    def getFinancialInfo(self):
        
        return self._FinancialInfo

    def setFinancialInfo(self, value):
        if self._FinancialInfo is not None:
            self._FinancialInfo._Asset = None

        self._FinancialInfo = value
        if self._FinancialInfo is not None:
            self._FinancialInfo.Asset = None
            self._FinancialInfo._Asset = self

    FinancialInfo = property(getFinancialInfo, setFinancialInfo)

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

