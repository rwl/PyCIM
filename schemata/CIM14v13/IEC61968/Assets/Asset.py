# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Asset(IdentifiedObject):
    """Tangible resource of the utility, including power system equipment, cabinets, buildings, etc. For electrical network equipment, the role of the asset is defined through PowerSystemResource and its subclasses, defined mainly in the Wires model (refer to IEC61970-301 and model package IEC61970::Wires). Asset description places emphasis on the physical characteristics of the equipment fulfilling that role.
    """

    def __init__(self, initialCondition='', category='', lotNumber='', application='', serialNumber='', installationDate='', corporateCode='', purchasePrice=0.0, manufacturedDate='', initialLossOfLife=0.0, utcNumber='', critical=False, Measurements=None, Hazards=None, ErpOrganisationRoles=None, DimensionsInfo=None, ScheduledEvents=None, Mediums=None, AssetFunctions=None, Properties=None, AssetContainer=None, Ratings=None, ActivityRecords=None, FromAssetRoles=None, LocationRoles=None, PowerSystemResourceRoles=None, DocumentRoles=None, ChangeItems=None, ErpItemMaster=None, ElectronicAddresses=None, WorkTask=None, ErpRecDeliveryItems=None, ReliabilityInfos=None, ToAssetRoles=None, AssetPropertyCurves=None, FinancialInfo=None, ErpInventory=None, acceptanceTest=None, status=None, **kw_args):
        """Initializes a new 'Asset' instance.

        @param initialCondition: Condition of asset in inventory or at time of installation. Examples include new, rebuilt, overhaul required, other. Refer to inspection data for information on the most current condition of the asset. 
        @param category: Extension mechanism to accommodate utility-specific categorisation of Asset and its subtypes, according to their corporate standards, practices, and existing IT systems (e.g., for management of assets, maintenance, work, outage, customers, etc.). 
        @param lotNumber: Lot number for this asset. Even for the same model and version number, many assets are manufactured in lots. 
        @param application: The way this particular asset is being used in this installation. For example, the application of a bushing when attached to a specific transformer winding would be one of the following: H1, H2, H3, H0, X1, X2, X3, X0, Y1, Y2, Y3, Y0. 
        @param serialNumber: Serial number of this asset. 
        @param installationDate: (if applicable) Date current installation was completed, which may not be the same as the in-service date. Asset may have been installed at other locations previously. Ignored if asset is (1) not currently installed (e.g., stored in a depot) or (2) not intended to be installed (e.g., vehicle, tool). 
        @param corporateCode: Code for this type of asset. 
        @param purchasePrice: Purchase price of asset. 
        @param manufacturedDate: Date this asset was manufactured. 
        @param initialLossOfLife: Whenever an asset is reconditioned, percentage of expected life for the asset when it was new; zero for new devices. 
        @param utcNumber: Uniquely Tracked Commodity (UTC) number. 
        @param critical: True if asset is considered critical for some reason (for example, a pole with critical attachments). 
        @param Measurements:
        @param Hazards:
        @param ErpOrganisationRoles:
        @param DimensionsInfo:
        @param ScheduledEvents:
        @param Mediums:
        @param AssetFunctions:
        @param Properties: UserAttributes used to specify further properties of this asset. Use 'name' to specify what kind of property it is, and 'value.value' attribute for the actual value.
        @param AssetContainer:
        @param Ratings: UserAttributes used to specify ratings of this asset. Ratings also can be used to set the initial value of operational measurement limits. Use 'name' to specify what kind of rating it is (e.g., voltage, current), and 'value' attribute for the actual value and unit information of the rating.
        @param ActivityRecords: All activity records created for this asset.
        @param FromAssetRoles:
        @param LocationRoles:
        @param PowerSystemResourceRoles:
        @param DocumentRoles:
        @param ChangeItems:
        @param ErpItemMaster:
        @param ElectronicAddresses: All electronic addresses of this asset.
        @param WorkTask:
        @param ErpRecDeliveryItems:
        @param ReliabilityInfos:
        @param ToAssetRoles:
        @param AssetPropertyCurves:
        @param FinancialInfo:
        @param ErpInventory:
        @param acceptanceTest: Information on acceptance test.
        @param status: Status of this asset.
        """
        #: Condition of asset in inventory or at time of installation. Examples include new, rebuilt, overhaul required, other. Refer to inspection data for information on the most current condition of the asset.
        self.initialCondition = initialCondition

        #: Extension mechanism to accommodate utility-specific categorisation of Asset and its subtypes, according to their corporate standards, practices, and existing IT systems (e.g., for management of assets, maintenance, work, outage, customers, etc.).
        self.category = category

        #: Lot number for this asset. Even for the same model and version number, many assets are manufactured in lots.
        self.lotNumber = lotNumber

        #: The way this particular asset is being used in this installation. For example, the application of a bushing when attached to a specific transformer winding would be one of the following: H1, H2, H3, H0, X1, X2, X3, X0, Y1, Y2, Y3, Y0.
        self.application = application

        #: Serial number of this asset.
        self.serialNumber = serialNumber

        #: (if applicable) Date current installation was completed, which may not be the same as the in-service date. Asset may have been installed at other locations previously. Ignored if asset is (1) not currently installed (e.g., stored in a depot) or (2) not intended to be installed (e.g., vehicle, tool).
        self.installationDate = installationDate

        #: Code for this type of asset.
        self.corporateCode = corporateCode

        #: Purchase price of asset.
        self.purchasePrice = purchasePrice

        #: Date this asset was manufactured.
        self.manufacturedDate = manufacturedDate

        #: Whenever an asset is reconditioned, percentage of expected life for the asset when it was new; zero for new devices.
        self.initialLossOfLife = initialLossOfLife

        #: Uniquely Tracked Commodity (UTC) number.
        self.utcNumber = utcNumber

        #: True if asset is considered critical for some reason (for example, a pole with critical attachments).
        self.critical = critical

        self._Measurements = []
        self.Measurements = [] if Measurements is None else Measurements

        self._Hazards = []
        self.Hazards = [] if Hazards is None else Hazards

        self._ErpOrganisationRoles = []
        self.ErpOrganisationRoles = [] if ErpOrganisationRoles is None else ErpOrganisationRoles

        self._DimensionsInfo = None
        self.DimensionsInfo = DimensionsInfo

        self._ScheduledEvents = []
        self.ScheduledEvents = [] if ScheduledEvents is None else ScheduledEvents

        self._Mediums = []
        self.Mediums = [] if Mediums is None else Mediums

        self._AssetFunctions = []
        self.AssetFunctions = [] if AssetFunctions is None else AssetFunctions

        self._Properties = []
        self.Properties = [] if Properties is None else Properties

        self._AssetContainer = None
        self.AssetContainer = AssetContainer

        self._Ratings = []
        self.Ratings = [] if Ratings is None else Ratings

        self._ActivityRecords = []
        self.ActivityRecords = [] if ActivityRecords is None else ActivityRecords

        self._FromAssetRoles = []
        self.FromAssetRoles = [] if FromAssetRoles is None else FromAssetRoles

        self._LocationRoles = []
        self.LocationRoles = [] if LocationRoles is None else LocationRoles

        self._PowerSystemResourceRoles = []
        self.PowerSystemResourceRoles = [] if PowerSystemResourceRoles is None else PowerSystemResourceRoles

        self._DocumentRoles = []
        self.DocumentRoles = [] if DocumentRoles is None else DocumentRoles

        self._ChangeItems = []
        self.ChangeItems = [] if ChangeItems is None else ChangeItems

        self._ErpItemMaster = None
        self.ErpItemMaster = ErpItemMaster

        self._ElectronicAddresses = []
        self.ElectronicAddresses = [] if ElectronicAddresses is None else ElectronicAddresses

        self._WorkTask = None
        self.WorkTask = WorkTask

        self._ErpRecDeliveryItems = []
        self.ErpRecDeliveryItems = [] if ErpRecDeliveryItems is None else ErpRecDeliveryItems

        self._ReliabilityInfos = []
        self.ReliabilityInfos = [] if ReliabilityInfos is None else ReliabilityInfos

        self._ToAssetRoles = []
        self.ToAssetRoles = [] if ToAssetRoles is None else ToAssetRoles

        self._AssetPropertyCurves = []
        self.AssetPropertyCurves = [] if AssetPropertyCurves is None else AssetPropertyCurves

        self._FinancialInfo = None
        self.FinancialInfo = FinancialInfo

        self._ErpInventory = None
        self.ErpInventory = ErpInventory

        self.acceptanceTest = acceptanceTest

        self.status = status

        super(Asset, self).__init__(**kw_args)

    def getMeasurements(self):
        
        return self._Measurements

    def setMeasurements(self, value):
        for x in self._Measurements:
            x._Asset = None
        for y in value:
            y._Asset = self
        self._Measurements = value

    Measurements = property(getMeasurements, setMeasurements)

    def addMeasurements(self, *Measurements):
        for obj in Measurements:
            obj._Asset = self
            self._Measurements.append(obj)

    def removeMeasurements(self, *Measurements):
        for obj in Measurements:
            obj._Asset = None
            self._Measurements.remove(obj)

    def getHazards(self):
        
        return self._Hazards

    def setHazards(self, value):
        for p in self._Hazards:
            filtered = [q for q in p.Assets if q != self]
            self._Hazards._Assets = filtered
        for r in value:
            if self not in r._Assets:
                r._Assets.append(self)
        self._Hazards = value

    Hazards = property(getHazards, setHazards)

    def addHazards(self, *Hazards):
        for obj in Hazards:
            if self not in obj._Assets:
                obj._Assets.append(self)
            self._Hazards.append(obj)

    def removeHazards(self, *Hazards):
        for obj in Hazards:
            if self in obj._Assets:
                obj._Assets.remove(self)
            self._Hazards.remove(obj)

    def getErpOrganisationRoles(self):
        
        return self._ErpOrganisationRoles

    def setErpOrganisationRoles(self, value):
        for x in self._ErpOrganisationRoles:
            x._Asset = None
        for y in value:
            y._Asset = self
        self._ErpOrganisationRoles = value

    ErpOrganisationRoles = property(getErpOrganisationRoles, setErpOrganisationRoles)

    def addErpOrganisationRoles(self, *ErpOrganisationRoles):
        for obj in ErpOrganisationRoles:
            obj._Asset = self
            self._ErpOrganisationRoles.append(obj)

    def removeErpOrganisationRoles(self, *ErpOrganisationRoles):
        for obj in ErpOrganisationRoles:
            obj._Asset = None
            self._ErpOrganisationRoles.remove(obj)

    def getDimensionsInfo(self):
        
        return self._DimensionsInfo

    def setDimensionsInfo(self, value):
        if self._DimensionsInfo is not None:
            filtered = [x for x in self.DimensionsInfo.Assets if x != self]
            self._DimensionsInfo._Assets = filtered

        self._DimensionsInfo = value
        if self._DimensionsInfo is not None:
            self._DimensionsInfo._Assets.append(self)

    DimensionsInfo = property(getDimensionsInfo, setDimensionsInfo)

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

    def getAssetFunctions(self):
        
        return self._AssetFunctions

    def setAssetFunctions(self, value):
        for x in self._AssetFunctions:
            x._Asset = None
        for y in value:
            y._Asset = self
        self._AssetFunctions = value

    AssetFunctions = property(getAssetFunctions, setAssetFunctions)

    def addAssetFunctions(self, *AssetFunctions):
        for obj in AssetFunctions:
            obj._Asset = self
            self._AssetFunctions.append(obj)

    def removeAssetFunctions(self, *AssetFunctions):
        for obj in AssetFunctions:
            obj._Asset = None
            self._AssetFunctions.remove(obj)

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

    def getAssetContainer(self):
        
        return self._AssetContainer

    def setAssetContainer(self, value):
        if self._AssetContainer is not None:
            filtered = [x for x in self.AssetContainer.Assets if x != self]
            self._AssetContainer._Assets = filtered

        self._AssetContainer = value
        if self._AssetContainer is not None:
            self._AssetContainer._Assets.append(self)

    AssetContainer = property(getAssetContainer, setAssetContainer)

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

    def getFromAssetRoles(self):
        
        return self._FromAssetRoles

    def setFromAssetRoles(self, value):
        for x in self._FromAssetRoles:
            x._ToAsset = None
        for y in value:
            y._ToAsset = self
        self._FromAssetRoles = value

    FromAssetRoles = property(getFromAssetRoles, setFromAssetRoles)

    def addFromAssetRoles(self, *FromAssetRoles):
        for obj in FromAssetRoles:
            obj._ToAsset = self
            self._FromAssetRoles.append(obj)

    def removeFromAssetRoles(self, *FromAssetRoles):
        for obj in FromAssetRoles:
            obj._ToAsset = None
            self._FromAssetRoles.remove(obj)

    def getLocationRoles(self):
        
        return self._LocationRoles

    def setLocationRoles(self, value):
        for x in self._LocationRoles:
            x._Asset = None
        for y in value:
            y._Asset = self
        self._LocationRoles = value

    LocationRoles = property(getLocationRoles, setLocationRoles)

    def addLocationRoles(self, *LocationRoles):
        for obj in LocationRoles:
            obj._Asset = self
            self._LocationRoles.append(obj)

    def removeLocationRoles(self, *LocationRoles):
        for obj in LocationRoles:
            obj._Asset = None
            self._LocationRoles.remove(obj)

    def getPowerSystemResourceRoles(self):
        
        return self._PowerSystemResourceRoles

    def setPowerSystemResourceRoles(self, value):
        for x in self._PowerSystemResourceRoles:
            x._Asset = None
        for y in value:
            y._Asset = self
        self._PowerSystemResourceRoles = value

    PowerSystemResourceRoles = property(getPowerSystemResourceRoles, setPowerSystemResourceRoles)

    def addPowerSystemResourceRoles(self, *PowerSystemResourceRoles):
        for obj in PowerSystemResourceRoles:
            obj._Asset = self
            self._PowerSystemResourceRoles.append(obj)

    def removePowerSystemResourceRoles(self, *PowerSystemResourceRoles):
        for obj in PowerSystemResourceRoles:
            obj._Asset = None
            self._PowerSystemResourceRoles.remove(obj)

    def getDocumentRoles(self):
        
        return self._DocumentRoles

    def setDocumentRoles(self, value):
        for x in self._DocumentRoles:
            x._Asset = None
        for y in value:
            y._Asset = self
        self._DocumentRoles = value

    DocumentRoles = property(getDocumentRoles, setDocumentRoles)

    def addDocumentRoles(self, *DocumentRoles):
        for obj in DocumentRoles:
            obj._Asset = self
            self._DocumentRoles.append(obj)

    def removeDocumentRoles(self, *DocumentRoles):
        for obj in DocumentRoles:
            obj._Asset = None
            self._DocumentRoles.remove(obj)

    def getChangeItems(self):
        
        return self._ChangeItems

    def setChangeItems(self, value):
        for x in self._ChangeItems:
            x._Asset = None
        for y in value:
            y._Asset = self
        self._ChangeItems = value

    ChangeItems = property(getChangeItems, setChangeItems)

    def addChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj._Asset = self
            self._ChangeItems.append(obj)

    def removeChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj._Asset = None
            self._ChangeItems.remove(obj)

    def getErpItemMaster(self):
        
        return self._ErpItemMaster

    def setErpItemMaster(self, value):
        if self._ErpItemMaster is not None:
            self._ErpItemMaster._Asset = None

        self._ErpItemMaster = value
        if self._ErpItemMaster is not None:
            self._ErpItemMaster._Asset = self

    ErpItemMaster = property(getErpItemMaster, setErpItemMaster)

    def getElectronicAddresses(self):
        """All electronic addresses of this asset.
        """
        return self._ElectronicAddresses

    def setElectronicAddresses(self, value):
        for x in self._ElectronicAddresses:
            x._Asset = None
        for y in value:
            y._Asset = self
        self._ElectronicAddresses = value

    ElectronicAddresses = property(getElectronicAddresses, setElectronicAddresses)

    def addElectronicAddresses(self, *ElectronicAddresses):
        for obj in ElectronicAddresses:
            obj._Asset = self
            self._ElectronicAddresses.append(obj)

    def removeElectronicAddresses(self, *ElectronicAddresses):
        for obj in ElectronicAddresses:
            obj._Asset = None
            self._ElectronicAddresses.remove(obj)

    def getWorkTask(self):
        
        return self._WorkTask

    def setWorkTask(self, value):
        if self._WorkTask is not None:
            filtered = [x for x in self.WorkTask.Assets if x != self]
            self._WorkTask._Assets = filtered

        self._WorkTask = value
        if self._WorkTask is not None:
            self._WorkTask._Assets.append(self)

    WorkTask = property(getWorkTask, setWorkTask)

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

    def getToAssetRoles(self):
        
        return self._ToAssetRoles

    def setToAssetRoles(self, value):
        for x in self._ToAssetRoles:
            x._FromAsset = None
        for y in value:
            y._FromAsset = self
        self._ToAssetRoles = value

    ToAssetRoles = property(getToAssetRoles, setToAssetRoles)

    def addToAssetRoles(self, *ToAssetRoles):
        for obj in ToAssetRoles:
            obj._FromAsset = self
            self._ToAssetRoles.append(obj)

    def removeToAssetRoles(self, *ToAssetRoles):
        for obj in ToAssetRoles:
            obj._FromAsset = None
            self._ToAssetRoles.remove(obj)

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

    def getFinancialInfo(self):
        
        return self._FinancialInfo

    def setFinancialInfo(self, value):
        if self._FinancialInfo is not None:
            self._FinancialInfo._Asset = None

        self._FinancialInfo = value
        if self._FinancialInfo is not None:
            self._FinancialInfo._Asset = self

    FinancialInfo = property(getFinancialInfo, setFinancialInfo)

    def getErpInventory(self):
        
        return self._ErpInventory

    def setErpInventory(self, value):
        if self._ErpInventory is not None:
            self._ErpInventory._Asset = None

        self._ErpInventory = value
        if self._ErpInventory is not None:
            self._ErpInventory._Asset = self

    ErpInventory = property(getErpInventory, setErpInventory)

    # Information on acceptance test.
    acceptanceTest = None

    # Status of this asset.
    status = None

