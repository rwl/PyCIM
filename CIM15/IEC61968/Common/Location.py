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

class Location(IdentifiedObject):
    """The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It can be defined with one or more postition points (coordinates) in a given coordinate system.The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It can be defined with one or more postition points (coordinates) in a given coordinate system.
    """

    def __init__(self, category='', geoInfoReference='', corporateCode='', direction='', mainAddress=None, phone1=None, phone2=None, PowerSystemResources=None, secondaryAddress=None, ChangeItems=None, RedLines=None, DimensionsInfo=None, LandProperties=None, Assets=None, Hazards=None, status=None, Crews=None, PositionPoints=None, electronicAddress=None, Directions=None, Measurements=None, Routes=None, CoordinateSystem=None, ErpOrganisations=None, *args, **kw_args):
        """Initialises a new 'Location' instance.

        @param category: Category by utility's corporate standards and practices, relative to the location itself (e.g., geographical, functional accounting, etc., not a given property that happens to exist at that location). 
        @param geoInfoReference: (if applicable) Reference to geographical information source, often external to the utility. 
        @param corporateCode: Utility-specific code for the location. 
        @param direction: (if applicable) Direction that allows field crews to quickly find a given asset. For a given location, such as a street address, this is the relative direction in which to find the asset. For example, a Streetlight may be located at the 'NW' (northwest) corner of the customer's site, or a ServiceDeliveryPoint may be located on the second floor of an apartment building. 
        @param mainAddress: Main address of the location.
        @param phone1: Phone number.
        @param phone2: Additional phone number.
        @param PowerSystemResources: All power system resources at this location.
        @param secondaryAddress: Secondary address of the location. For example, PO Box address may have different ZIP code than that in the 'mainAddress'.
        @param ChangeItems:
        @param RedLines:
        @param DimensionsInfo:
        @param LandProperties:
        @param Assets: All assets at this location.
        @param Hazards:
        @param status: Status of this location.
        @param Crews:
        @param PositionPoints: Sequence of position points describing this location, expressed in coordinate system 'Location.CoordinateSystem'.
        @param electronicAddress: Electronic address.
        @param Directions:
        @param Measurements:
        @param Routes:
        @param CoordinateSystem: Coordinate system used to describe position points of this location.
        @param ErpOrganisations:
        """
        #: Category by utility's corporate standards and practices, relative to the location itself (e.g., geographical, functional accounting, etc., not a given property that happens to exist at that location).
        self.category = category

        #: (if applicable) Reference to geographical information source, often external to the utility.
        self.geoInfoReference = geoInfoReference

        #: Utility-specific code for the location.
        self.corporateCode = corporateCode

        #: (if applicable) Direction that allows field crews to quickly find a given asset. For a given location, such as a street address, this is the relative direction in which to find the asset. For example, a Streetlight may be located at the 'NW' (northwest) corner of the customer's site, or a ServiceDeliveryPoint may be located on the second floor of an apartment building.
        self.direction = direction

        self.mainAddress = mainAddress

        self.phone1 = phone1

        self.phone2 = phone2

        self._PowerSystemResources = []
        self.PowerSystemResources = [] if PowerSystemResources is None else PowerSystemResources

        self.secondaryAddress = secondaryAddress

        self._ChangeItems = []
        self.ChangeItems = [] if ChangeItems is None else ChangeItems

        self._RedLines = []
        self.RedLines = [] if RedLines is None else RedLines

        self._DimensionsInfo = None
        self.DimensionsInfo = DimensionsInfo

        self._LandProperties = []
        self.LandProperties = [] if LandProperties is None else LandProperties

        self._Assets = []
        self.Assets = [] if Assets is None else Assets

        self._Hazards = []
        self.Hazards = [] if Hazards is None else Hazards

        self.status = status

        self._Crews = []
        self.Crews = [] if Crews is None else Crews

        self._PositionPoints = []
        self.PositionPoints = [] if PositionPoints is None else PositionPoints

        self.electronicAddress = electronicAddress

        self._Directions = []
        self.Directions = [] if Directions is None else Directions

        self._Measurements = []
        self.Measurements = [] if Measurements is None else Measurements

        self._Routes = []
        self.Routes = [] if Routes is None else Routes

        self._CoordinateSystem = None
        self.CoordinateSystem = CoordinateSystem

        self._ErpOrganisations = []
        self.ErpOrganisations = [] if ErpOrganisations is None else ErpOrganisations

        super(Location, self).__init__(*args, **kw_args)

    _attrs = ["category", "geoInfoReference", "corporateCode", "direction"]
    _attr_types = {"category": str, "geoInfoReference": str, "corporateCode": str, "direction": str}
    _defaults = {"category": '', "geoInfoReference": '', "corporateCode": '', "direction": ''}
    _enums = {}
    _refs = ["mainAddress", "phone1", "phone2", "PowerSystemResources", "secondaryAddress", "ChangeItems", "RedLines", "DimensionsInfo", "LandProperties", "Assets", "Hazards", "status", "Crews", "PositionPoints", "electronicAddress", "Directions", "Measurements", "Routes", "CoordinateSystem", "ErpOrganisations"]
    _many_refs = ["PowerSystemResources", "ChangeItems", "RedLines", "LandProperties", "Assets", "Hazards", "Crews", "PositionPoints", "Directions", "Measurements", "Routes", "ErpOrganisations"]

    # Main address of the location.
    mainAddress = None

    # Phone number.
    phone1 = None

    # Additional phone number.
    phone2 = None

    def getPowerSystemResources(self):
        """All power system resources at this location.
        """
        return self._PowerSystemResources

    def setPowerSystemResources(self, value):
        for x in self._PowerSystemResources:
            x.Location = None
        for y in value:
            y._Location = self
        self._PowerSystemResources = value

    PowerSystemResources = property(getPowerSystemResources, setPowerSystemResources)

    def addPowerSystemResources(self, *PowerSystemResources):
        for obj in PowerSystemResources:
            obj.Location = self

    def removePowerSystemResources(self, *PowerSystemResources):
        for obj in PowerSystemResources:
            obj.Location = None

    # Secondary address of the location. For example, PO Box address may have different ZIP code than that in the 'mainAddress'.
    secondaryAddress = None

    def getChangeItems(self):
        
        return self._ChangeItems

    def setChangeItems(self, value):
        for x in self._ChangeItems:
            x.Location = None
        for y in value:
            y._Location = self
        self._ChangeItems = value

    ChangeItems = property(getChangeItems, setChangeItems)

    def addChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj.Location = self

    def removeChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj.Location = None

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

    def getDimensionsInfo(self):
        
        return self._DimensionsInfo

    def setDimensionsInfo(self, value):
        if self._DimensionsInfo is not None:
            filtered = [x for x in self.DimensionsInfo.Locations if x != self]
            self._DimensionsInfo._Locations = filtered

        self._DimensionsInfo = value
        if self._DimensionsInfo is not None:
            if self not in self._DimensionsInfo._Locations:
                self._DimensionsInfo._Locations.append(self)

    DimensionsInfo = property(getDimensionsInfo, setDimensionsInfo)

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

    def getAssets(self):
        """All assets at this location.
        """
        return self._Assets

    def setAssets(self, value):
        for x in self._Assets:
            x.Location = None
        for y in value:
            y._Location = self
        self._Assets = value

    Assets = property(getAssets, setAssets)

    def addAssets(self, *Assets):
        for obj in Assets:
            obj.Location = self

    def removeAssets(self, *Assets):
        for obj in Assets:
            obj.Location = None

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

    # Status of this location.
    status = None

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

    def getPositionPoints(self):
        """Sequence of position points describing this location, expressed in coordinate system 'Location.CoordinateSystem'.
        """
        return self._PositionPoints

    def setPositionPoints(self, value):
        for x in self._PositionPoints:
            x.Location = None
        for y in value:
            y._Location = self
        self._PositionPoints = value

    PositionPoints = property(getPositionPoints, setPositionPoints)

    def addPositionPoints(self, *PositionPoints):
        for obj in PositionPoints:
            obj.Location = self

    def removePositionPoints(self, *PositionPoints):
        for obj in PositionPoints:
            obj.Location = None

    # Electronic address.
    electronicAddress = None

    def getDirections(self):
        
        return self._Directions

    def setDirections(self, value):
        for x in self._Directions:
            x.Location = None
        for y in value:
            y._Location = self
        self._Directions = value

    Directions = property(getDirections, setDirections)

    def addDirections(self, *Directions):
        for obj in Directions:
            obj.Location = self

    def removeDirections(self, *Directions):
        for obj in Directions:
            obj.Location = None

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

    def getCoordinateSystem(self):
        """Coordinate system used to describe position points of this location.
        """
        return self._CoordinateSystem

    def setCoordinateSystem(self, value):
        if self._CoordinateSystem is not None:
            filtered = [x for x in self.CoordinateSystem.Location if x != self]
            self._CoordinateSystem._Location = filtered

        self._CoordinateSystem = value
        if self._CoordinateSystem is not None:
            if self not in self._CoordinateSystem._Location:
                self._CoordinateSystem._Location.append(self)

    CoordinateSystem = property(getCoordinateSystem, setCoordinateSystem)

    def getErpOrganisations(self):
        
        return self._ErpOrganisations

    def setErpOrganisations(self, value):
        for p in self._ErpOrganisations:
            filtered = [q for q in p.Locations if q != self]
            self._ErpOrganisations._Locations = filtered
        for r in value:
            if self not in r._Locations:
                r._Locations.append(self)
        self._ErpOrganisations = value

    ErpOrganisations = property(getErpOrganisations, setErpOrganisations)

    def addErpOrganisations(self, *ErpOrganisations):
        for obj in ErpOrganisations:
            if self not in obj._Locations:
                obj._Locations.append(self)
            self._ErpOrganisations.append(obj)

    def removeErpOrganisations(self, *ErpOrganisations):
        for obj in ErpOrganisations:
            if self in obj._Locations:
                obj._Locations.remove(self)
            self._ErpOrganisations.remove(obj)

