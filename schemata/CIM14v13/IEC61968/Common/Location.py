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

class Location(IdentifiedObject):
    """The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It may be: - Spatial location of an actual or planned structure, or a set of point-oriented structures (as a substation, structure, building, town, etc.) or diagram objects, which may be defined as a point or polygon, or, - Path of an underground or overhead conductor, or a linear diagram object.
    """

    def __init__(self, corporateCode='', direction='', isPolygon=False, category='', geoInfoReference='', DocumentRoles=None, ErpPersonRoles=None, ElectronicAddresses=None, ChangeItems=None, Routes=None, PositionPoints=None, GmlSelectors=None, mainAddress=None, FromLocationRoles=None, status=None, ToLocationRoles=None, TelephoneNumbers=None, secondaryAddress=None, LandProperties=None, Measurements=None, ErpOrganisationRoles=None, DimensionsInfo=None, AssetRoles=None, Crews=None, RedLines=None, GmlObservatins=None, Hazards=None, ActivityRecords=None, *args, **kw_args):
        """Initializes a new 'Location' instance.

        @param corporateCode: Utility-specific code for the location. 
        @param direction: (if applicable) Direction that allows field crews to quickly find a given asset. For a given location, such as a street address, this is the relative direction in which to find the asset. For example, a Streetlight may be located at the 'NW' (northwest) corner of the customer's site, or a ServiceDeliveryPoint may be located on the second floor of an apartment building. 
        @param isPolygon: True if the first and last point in the sequence of associated PositionPoints are to be connected, thus forming a polygon rather than merely a sequence of line segments. 
        @param category: Category by utility's corporate standards and practices, relative to the location itself (e.g., geographical, functional accounting, etc., not a given property that happens to exist at that location). 
        @param geoInfoReference: (if applicable) Reference to geographical information source, often external to the utility. 
        @param DocumentRoles:
        @param ErpPersonRoles:
        @param ElectronicAddresses: All electronic addresses of this location.
        @param ChangeItems:
        @param Routes:
        @param PositionPoints: Sequence of position points describing this location.
        @param GmlSelectors:
        @param mainAddress: Main address of the location.
        @param FromLocationRoles:
        @param status: Status of this location.
        @param ToLocationRoles:
        @param TelephoneNumbers: All telephone numbers of this location.
        @param secondaryAddress: Secondary address of the location. For example, PO Box address may have different ZIP code than that in the 'mainAddress'.
        @param LandProperties:
        @param Measurements:
        @param ErpOrganisationRoles:
        @param DimensionsInfo:
        @param AssetRoles:
        @param Crews:
        @param RedLines:
        @param GmlObservatins:
        @param Hazards:
        @param ActivityRecords:
        """
        #: Utility-specific code for the location. 
        self.corporateCode = corporateCode

        #: (if applicable) Direction that allows field crews to quickly find a given asset. For a given location, such as a street address, this is the relative direction in which to find the asset. For example, a Streetlight may be located at the 'NW' (northwest) corner of the customer's site, or a ServiceDeliveryPoint may be located on the second floor of an apartment building. 
        self.direction = direction

        #: True if the first and last point in the sequence of associated PositionPoints are to be connected, thus forming a polygon rather than merely a sequence of line segments. 
        self.isPolygon = isPolygon

        #: Category by utility's corporate standards and practices, relative to the location itself (e.g., geographical, functional accounting, etc., not a given property that happens to exist at that location). 
        self.category = category

        #: (if applicable) Reference to geographical information source, often external to the utility. 
        self.geoInfoReference = geoInfoReference

        self._DocumentRoles = []
        self.DocumentRoles = [] if DocumentRoles is None else DocumentRoles

        self._ErpPersonRoles = []
        self.ErpPersonRoles = [] if ErpPersonRoles is None else ErpPersonRoles

        self._ElectronicAddresses = []
        self.ElectronicAddresses = [] if ElectronicAddresses is None else ElectronicAddresses

        self._ChangeItems = []
        self.ChangeItems = [] if ChangeItems is None else ChangeItems

        self._Routes = []
        self.Routes = [] if Routes is None else Routes

        self._PositionPoints = []
        self.PositionPoints = [] if PositionPoints is None else PositionPoints

        self._GmlSelectors = []
        self.GmlSelectors = [] if GmlSelectors is None else GmlSelectors

        self.mainAddress = mainAddress

        self._FromLocationRoles = []
        self.FromLocationRoles = [] if FromLocationRoles is None else FromLocationRoles

        self.status = status

        self._ToLocationRoles = []
        self.ToLocationRoles = [] if ToLocationRoles is None else ToLocationRoles

        self._TelephoneNumbers = []
        self.TelephoneNumbers = [] if TelephoneNumbers is None else TelephoneNumbers

        self.secondaryAddress = secondaryAddress

        self._LandProperties = []
        self.LandProperties = [] if LandProperties is None else LandProperties

        self._Measurements = []
        self.Measurements = [] if Measurements is None else Measurements

        self._ErpOrganisationRoles = []
        self.ErpOrganisationRoles = [] if ErpOrganisationRoles is None else ErpOrganisationRoles

        self._DimensionsInfo = None
        self.DimensionsInfo = DimensionsInfo

        self._AssetRoles = []
        self.AssetRoles = [] if AssetRoles is None else AssetRoles

        self._Crews = []
        self.Crews = [] if Crews is None else Crews

        self._RedLines = []
        self.RedLines = [] if RedLines is None else RedLines

        self._GmlObservatins = []
        self.GmlObservatins = [] if GmlObservatins is None else GmlObservatins

        self._Hazards = []
        self.Hazards = [] if Hazards is None else Hazards

        self._ActivityRecords = []
        self.ActivityRecords = [] if ActivityRecords is None else ActivityRecords

        super(Location, self).__init__(*args, **kw_args)

    def getDocumentRoles(self):
        
        return self._DocumentRoles

    def setDocumentRoles(self, value):
        for x in self._DocumentRoles:
            x._Location = None
        for y in value:
            y._Location = self
        self._DocumentRoles = value

    DocumentRoles = property(getDocumentRoles, setDocumentRoles)

    def addDocumentRoles(self, *DocumentRoles):
        for obj in DocumentRoles:
            obj._Location = self
            self._DocumentRoles.append(obj)

    def removeDocumentRoles(self, *DocumentRoles):
        for obj in DocumentRoles:
            obj._Location = None
            self._DocumentRoles.remove(obj)

    def getErpPersonRoles(self):
        
        return self._ErpPersonRoles

    def setErpPersonRoles(self, value):
        for x in self._ErpPersonRoles:
            x._Location = None
        for y in value:
            y._Location = self
        self._ErpPersonRoles = value

    ErpPersonRoles = property(getErpPersonRoles, setErpPersonRoles)

    def addErpPersonRoles(self, *ErpPersonRoles):
        for obj in ErpPersonRoles:
            obj._Location = self
            self._ErpPersonRoles.append(obj)

    def removeErpPersonRoles(self, *ErpPersonRoles):
        for obj in ErpPersonRoles:
            obj._Location = None
            self._ErpPersonRoles.remove(obj)

    def getElectronicAddresses(self):
        """All electronic addresses of this location.
        """
        return self._ElectronicAddresses

    def setElectronicAddresses(self, value):
        for p in self._ElectronicAddresses:
            filtered = [q for q in p.Locations if q != self]
            self._ElectronicAddresses._Locations = filtered
        for r in value:
            if self not in r._Locations:
                r._Locations.append(self)
        self._ElectronicAddresses = value

    ElectronicAddresses = property(getElectronicAddresses, setElectronicAddresses)

    def addElectronicAddresses(self, *ElectronicAddresses):
        for obj in ElectronicAddresses:
            if self not in obj._Locations:
                obj._Locations.append(self)
            self._ElectronicAddresses.append(obj)

    def removeElectronicAddresses(self, *ElectronicAddresses):
        for obj in ElectronicAddresses:
            if self in obj._Locations:
                obj._Locations.remove(self)
            self._ElectronicAddresses.remove(obj)

    def getChangeItems(self):
        
        return self._ChangeItems

    def setChangeItems(self, value):
        for x in self._ChangeItems:
            x._Location = None
        for y in value:
            y._Location = self
        self._ChangeItems = value

    ChangeItems = property(getChangeItems, setChangeItems)

    def addChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj._Location = self
            self._ChangeItems.append(obj)

    def removeChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj._Location = None
            self._ChangeItems.remove(obj)

    def getRoutes(self):
        
        return self._Routes

    def setRoutes(self, value):
        for p in self._Routes:
            filtered = [q for q in p.Locations if q != self]
            self._Routes._Locations = filtered
        for r in value:
            if self not in r._Locations:
                r._Locations.append(self)
        self._Routes = value

    Routes = property(getRoutes, setRoutes)

    def addRoutes(self, *Routes):
        for obj in Routes:
            if self not in obj._Locations:
                obj._Locations.append(self)
            self._Routes.append(obj)

    def removeRoutes(self, *Routes):
        for obj in Routes:
            if self in obj._Locations:
                obj._Locations.remove(self)
            self._Routes.remove(obj)

    def getPositionPoints(self):
        """Sequence of position points describing this location.
        """
        return self._PositionPoints

    def setPositionPoints(self, value):
        for x in self._PositionPoints:
            x._Location = None
        for y in value:
            y._Location = self
        self._PositionPoints = value

    PositionPoints = property(getPositionPoints, setPositionPoints)

    def addPositionPoints(self, *PositionPoints):
        for obj in PositionPoints:
            obj._Location = self
            self._PositionPoints.append(obj)

    def removePositionPoints(self, *PositionPoints):
        for obj in PositionPoints:
            obj._Location = None
            self._PositionPoints.remove(obj)

    def getGmlSelectors(self):
        
        return self._GmlSelectors

    def setGmlSelectors(self, value):
        for p in self._GmlSelectors:
            filtered = [q for q in p.Locations if q != self]
            self._GmlSelectors._Locations = filtered
        for r in value:
            if self not in r._Locations:
                r._Locations.append(self)
        self._GmlSelectors = value

    GmlSelectors = property(getGmlSelectors, setGmlSelectors)

    def addGmlSelectors(self, *GmlSelectors):
        for obj in GmlSelectors:
            if self not in obj._Locations:
                obj._Locations.append(self)
            self._GmlSelectors.append(obj)

    def removeGmlSelectors(self, *GmlSelectors):
        for obj in GmlSelectors:
            if self in obj._Locations:
                obj._Locations.remove(self)
            self._GmlSelectors.remove(obj)

    # Main address of the location.
    mainAddress = None

    def getFromLocationRoles(self):
        
        return self._FromLocationRoles

    def setFromLocationRoles(self, value):
        for x in self._FromLocationRoles:
            x._ToLocation = None
        for y in value:
            y._ToLocation = self
        self._FromLocationRoles = value

    FromLocationRoles = property(getFromLocationRoles, setFromLocationRoles)

    def addFromLocationRoles(self, *FromLocationRoles):
        for obj in FromLocationRoles:
            obj._ToLocation = self
            self._FromLocationRoles.append(obj)

    def removeFromLocationRoles(self, *FromLocationRoles):
        for obj in FromLocationRoles:
            obj._ToLocation = None
            self._FromLocationRoles.remove(obj)

    # Status of this location.
    status = None

    def getToLocationRoles(self):
        
        return self._ToLocationRoles

    def setToLocationRoles(self, value):
        for x in self._ToLocationRoles:
            x._FromLocation = None
        for y in value:
            y._FromLocation = self
        self._ToLocationRoles = value

    ToLocationRoles = property(getToLocationRoles, setToLocationRoles)

    def addToLocationRoles(self, *ToLocationRoles):
        for obj in ToLocationRoles:
            obj._FromLocation = self
            self._ToLocationRoles.append(obj)

    def removeToLocationRoles(self, *ToLocationRoles):
        for obj in ToLocationRoles:
            obj._FromLocation = None
            self._ToLocationRoles.remove(obj)

    def getTelephoneNumbers(self):
        """All telephone numbers of this location.
        """
        return self._TelephoneNumbers

    def setTelephoneNumbers(self, value):
        for x in self._TelephoneNumbers:
            x._Location = None
        for y in value:
            y._Location = self
        self._TelephoneNumbers = value

    TelephoneNumbers = property(getTelephoneNumbers, setTelephoneNumbers)

    def addTelephoneNumbers(self, *TelephoneNumbers):
        for obj in TelephoneNumbers:
            obj._Location = self
            self._TelephoneNumbers.append(obj)

    def removeTelephoneNumbers(self, *TelephoneNumbers):
        for obj in TelephoneNumbers:
            obj._Location = None
            self._TelephoneNumbers.remove(obj)

    # Secondary address of the location. For example, PO Box address may have different ZIP code than that in the 'mainAddress'.
    secondaryAddress = None

    def getLandProperties(self):
        
        return self._LandProperties

    def setLandProperties(self, value):
        for p in self._LandProperties:
            filtered = [q for q in p.Locations if q != self]
            self._LandProperties._Locations = filtered
        for r in value:
            if self not in r._Locations:
                r._Locations.append(self)
        self._LandProperties = value

    LandProperties = property(getLandProperties, setLandProperties)

    def addLandProperties(self, *LandProperties):
        for obj in LandProperties:
            if self not in obj._Locations:
                obj._Locations.append(self)
            self._LandProperties.append(obj)

    def removeLandProperties(self, *LandProperties):
        for obj in LandProperties:
            if self in obj._Locations:
                obj._Locations.remove(self)
            self._LandProperties.remove(obj)

    def getMeasurements(self):
        
        return self._Measurements

    def setMeasurements(self, value):
        for p in self._Measurements:
            filtered = [q for q in p.Locations if q != self]
            self._Measurements._Locations = filtered
        for r in value:
            if self not in r._Locations:
                r._Locations.append(self)
        self._Measurements = value

    Measurements = property(getMeasurements, setMeasurements)

    def addMeasurements(self, *Measurements):
        for obj in Measurements:
            if self not in obj._Locations:
                obj._Locations.append(self)
            self._Measurements.append(obj)

    def removeMeasurements(self, *Measurements):
        for obj in Measurements:
            if self in obj._Locations:
                obj._Locations.remove(self)
            self._Measurements.remove(obj)

    def getErpOrganisationRoles(self):
        
        return self._ErpOrganisationRoles

    def setErpOrganisationRoles(self, value):
        for x in self._ErpOrganisationRoles:
            x._Location = None
        for y in value:
            y._Location = self
        self._ErpOrganisationRoles = value

    ErpOrganisationRoles = property(getErpOrganisationRoles, setErpOrganisationRoles)

    def addErpOrganisationRoles(self, *ErpOrganisationRoles):
        for obj in ErpOrganisationRoles:
            obj._Location = self
            self._ErpOrganisationRoles.append(obj)

    def removeErpOrganisationRoles(self, *ErpOrganisationRoles):
        for obj in ErpOrganisationRoles:
            obj._Location = None
            self._ErpOrganisationRoles.remove(obj)

    def getDimensionsInfo(self):
        
        return self._DimensionsInfo

    def setDimensionsInfo(self, value):
        if self._DimensionsInfo is not None:
            filtered = [x for x in self.DimensionsInfo.Locations if x != self]
            self._DimensionsInfo._Locations = filtered

        self._DimensionsInfo = value
        if self._DimensionsInfo is not None:
            self._DimensionsInfo._Locations.append(self)

    DimensionsInfo = property(getDimensionsInfo, setDimensionsInfo)

    def getAssetRoles(self):
        
        return self._AssetRoles

    def setAssetRoles(self, value):
        for x in self._AssetRoles:
            x._Location = None
        for y in value:
            y._Location = self
        self._AssetRoles = value

    AssetRoles = property(getAssetRoles, setAssetRoles)

    def addAssetRoles(self, *AssetRoles):
        for obj in AssetRoles:
            obj._Location = self
            self._AssetRoles.append(obj)

    def removeAssetRoles(self, *AssetRoles):
        for obj in AssetRoles:
            obj._Location = None
            self._AssetRoles.remove(obj)

    def getCrews(self):
        
        return self._Crews

    def setCrews(self, value):
        for p in self._Crews:
            filtered = [q for q in p.Locations if q != self]
            self._Crews._Locations = filtered
        for r in value:
            if self not in r._Locations:
                r._Locations.append(self)
        self._Crews = value

    Crews = property(getCrews, setCrews)

    def addCrews(self, *Crews):
        for obj in Crews:
            if self not in obj._Locations:
                obj._Locations.append(self)
            self._Crews.append(obj)

    def removeCrews(self, *Crews):
        for obj in Crews:
            if self in obj._Locations:
                obj._Locations.remove(self)
            self._Crews.remove(obj)

    def getRedLines(self):
        
        return self._RedLines

    def setRedLines(self, value):
        for p in self._RedLines:
            filtered = [q for q in p.Locations if q != self]
            self._RedLines._Locations = filtered
        for r in value:
            if self not in r._Locations:
                r._Locations.append(self)
        self._RedLines = value

    RedLines = property(getRedLines, setRedLines)

    def addRedLines(self, *RedLines):
        for obj in RedLines:
            if self not in obj._Locations:
                obj._Locations.append(self)
            self._RedLines.append(obj)

    def removeRedLines(self, *RedLines):
        for obj in RedLines:
            if self in obj._Locations:
                obj._Locations.remove(self)
            self._RedLines.remove(obj)

    def getGmlObservatins(self):
        
        return self._GmlObservatins

    def setGmlObservatins(self, value):
        for p in self._GmlObservatins:
            filtered = [q for q in p.Locations if q != self]
            self._GmlObservatins._Locations = filtered
        for r in value:
            if self not in r._Locations:
                r._Locations.append(self)
        self._GmlObservatins = value

    GmlObservatins = property(getGmlObservatins, setGmlObservatins)

    def addGmlObservatins(self, *GmlObservatins):
        for obj in GmlObservatins:
            if self not in obj._Locations:
                obj._Locations.append(self)
            self._GmlObservatins.append(obj)

    def removeGmlObservatins(self, *GmlObservatins):
        for obj in GmlObservatins:
            if self in obj._Locations:
                obj._Locations.remove(self)
            self._GmlObservatins.remove(obj)

    def getHazards(self):
        
        return self._Hazards

    def setHazards(self, value):
        for p in self._Hazards:
            filtered = [q for q in p.Locations if q != self]
            self._Hazards._Locations = filtered
        for r in value:
            if self not in r._Locations:
                r._Locations.append(self)
        self._Hazards = value

    Hazards = property(getHazards, setHazards)

    def addHazards(self, *Hazards):
        for obj in Hazards:
            if self not in obj._Locations:
                obj._Locations.append(self)
            self._Hazards.append(obj)

    def removeHazards(self, *Hazards):
        for obj in Hazards:
            if self in obj._Locations:
                obj._Locations.remove(self)
            self._Hazards.remove(obj)

    def getActivityRecords(self):
        
        return self._ActivityRecords

    def setActivityRecords(self, value):
        for p in self._ActivityRecords:
            filtered = [q for q in p.Locations if q != self]
            self._ActivityRecords._Locations = filtered
        for r in value:
            if self not in r._Locations:
                r._Locations.append(self)
        self._ActivityRecords = value

    ActivityRecords = property(getActivityRecords, setActivityRecords)

    def addActivityRecords(self, *ActivityRecords):
        for obj in ActivityRecords:
            if self not in obj._Locations:
                obj._Locations.append(self)
            self._ActivityRecords.append(obj)

    def removeActivityRecords(self, *ActivityRecords):
        for obj in ActivityRecords:
            if self in obj._Locations:
                obj._Locations.remove(self)
            self._ActivityRecords.remove(obj)

