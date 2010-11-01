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

class Measurement(IdentifiedObject):
    """A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  Two possible paths exist: 1) Measurement-Terminal- ConnectivityNode-Terminal-ConductingEquipment 2) Measurement-Terminal-ConductingEquipment Alternative 2 is the only allowed use.  When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.
    """

    def __init__(self, measurementType='', Asset=None, For_TiePoint=None, PowerSystemResource=None, DynamicSchedules=None, Pnode=None, Terminal=None, Documents=None, Locations=None, ChangeItems=None, ViolationLimits=None, By_TiePoint=None, Unit=None, *args, **kw_args):
        """Initializes a new 'Measurement' instance.

        @param measurementType: Specifies the type of Measurement, e.g. IndoorTemperature, OutDoorTemperature, BusVoltage, GeneratorVoltage, LineFlow etc. 
        @param Asset:
        @param For_TiePoint: A measurement is made on the A side of a tie point
        @param PowerSystemResource: The PowerSystemResource that contains the Measurement in the naming hierarchy
        @param DynamicSchedules: A measurement is a data source for dynamic interchange schedules
        @param Pnode:
        @param Terminal: One or more measurements may be associated with a terminal in the network
        @param Documents: Measurements are specified in types of documents, such as procedures.
        @param Locations:
        @param ChangeItems:
        @param ViolationLimits:
        @param By_TiePoint: A measurement is made on the B side of a tie point
        @param Unit: The Unit for the Measurement
        """
        #: Specifies the type of Measurement, e.g. IndoorTemperature, OutDoorTemperature, BusVoltage, GeneratorVoltage, LineFlow etc. 
        self.measurementType = measurementType

        self._Asset = None
        self.Asset = Asset

        self._For_TiePoint = None
        self.For_TiePoint = For_TiePoint

        self._PowerSystemResource = None
        self.PowerSystemResource = PowerSystemResource

        self._DynamicSchedules = []
        self.DynamicSchedules = [] if DynamicSchedules is None else DynamicSchedules

        self._Pnode = None
        self.Pnode = Pnode

        self._Terminal = None
        self.Terminal = Terminal

        self._Documents = []
        self.Documents = [] if Documents is None else Documents

        self._Locations = []
        self.Locations = [] if Locations is None else Locations

        self._ChangeItems = []
        self.ChangeItems = [] if ChangeItems is None else ChangeItems

        self._ViolationLimits = []
        self.ViolationLimits = [] if ViolationLimits is None else ViolationLimits

        self._By_TiePoint = None
        self.By_TiePoint = By_TiePoint

        self._Unit = None
        self.Unit = Unit

        super(Measurement, self).__init__(*args, **kw_args)

    def getAsset(self):
        
        return self._Asset

    def setAsset(self, value):
        if self._Asset is not None:
            filtered = [x for x in self.Asset.Measurements if x != self]
            self._Asset._Measurements = filtered

        self._Asset = value
        if self._Asset is not None:
            self._Asset._Measurements.append(self)

    Asset = property(getAsset, setAsset)

    def getFor_TiePoint(self):
        """A measurement is made on the A side of a tie point
        """
        return self._For_TiePoint

    def setFor_TiePoint(self, value):
        if self._For_TiePoint is not None:
            filtered = [x for x in self.For_TiePoint.For_Measurements if x != self]
            self._For_TiePoint._For_Measurements = filtered

        self._For_TiePoint = value
        if self._For_TiePoint is not None:
            self._For_TiePoint._For_Measurements.append(self)

    For_TiePoint = property(getFor_TiePoint, setFor_TiePoint)

    def getPowerSystemResource(self):
        """The PowerSystemResource that contains the Measurement in the naming hierarchy
        """
        return self._PowerSystemResource

    def setPowerSystemResource(self, value):
        if self._PowerSystemResource is not None:
            filtered = [x for x in self.PowerSystemResource.Measurements if x != self]
            self._PowerSystemResource._Measurements = filtered

        self._PowerSystemResource = value
        if self._PowerSystemResource is not None:
            self._PowerSystemResource._Measurements.append(self)

    PowerSystemResource = property(getPowerSystemResource, setPowerSystemResource)

    def getDynamicSchedules(self):
        """A measurement is a data source for dynamic interchange schedules
        """
        return self._DynamicSchedules

    def setDynamicSchedules(self, value):
        for x in self._DynamicSchedules:
            x._Measurement = None
        for y in value:
            y._Measurement = self
        self._DynamicSchedules = value

    DynamicSchedules = property(getDynamicSchedules, setDynamicSchedules)

    def addDynamicSchedules(self, *DynamicSchedules):
        for obj in DynamicSchedules:
            obj._Measurement = self
            self._DynamicSchedules.append(obj)

    def removeDynamicSchedules(self, *DynamicSchedules):
        for obj in DynamicSchedules:
            obj._Measurement = None
            self._DynamicSchedules.remove(obj)

    def getPnode(self):
        
        return self._Pnode

    def setPnode(self, value):
        if self._Pnode is not None:
            filtered = [x for x in self.Pnode.Measurements if x != self]
            self._Pnode._Measurements = filtered

        self._Pnode = value
        if self._Pnode is not None:
            self._Pnode._Measurements.append(self)

    Pnode = property(getPnode, setPnode)

    def getTerminal(self):
        """One or more measurements may be associated with a terminal in the network
        """
        return self._Terminal

    def setTerminal(self, value):
        if self._Terminal is not None:
            filtered = [x for x in self.Terminal.Measurements if x != self]
            self._Terminal._Measurements = filtered

        self._Terminal = value
        if self._Terminal is not None:
            self._Terminal._Measurements.append(self)

    Terminal = property(getTerminal, setTerminal)

    def getDocuments(self):
        """Measurements are specified in types of documents, such as procedures.
        """
        return self._Documents

    def setDocuments(self, value):
        for p in self._Documents:
            filtered = [q for q in p.Measurements if q != self]
            self._Documents._Measurements = filtered
        for r in value:
            if self not in r._Measurements:
                r._Measurements.append(self)
        self._Documents = value

    Documents = property(getDocuments, setDocuments)

    def addDocuments(self, *Documents):
        for obj in Documents:
            if self not in obj._Measurements:
                obj._Measurements.append(self)
            self._Documents.append(obj)

    def removeDocuments(self, *Documents):
        for obj in Documents:
            if self in obj._Measurements:
                obj._Measurements.remove(self)
            self._Documents.remove(obj)

    def getLocations(self):
        
        return self._Locations

    def setLocations(self, value):
        for p in self._Locations:
            filtered = [q for q in p.Measurements if q != self]
            self._Locations._Measurements = filtered
        for r in value:
            if self not in r._Measurements:
                r._Measurements.append(self)
        self._Locations = value

    Locations = property(getLocations, setLocations)

    def addLocations(self, *Locations):
        for obj in Locations:
            if self not in obj._Measurements:
                obj._Measurements.append(self)
            self._Locations.append(obj)

    def removeLocations(self, *Locations):
        for obj in Locations:
            if self in obj._Measurements:
                obj._Measurements.remove(self)
            self._Locations.remove(obj)

    def getChangeItems(self):
        
        return self._ChangeItems

    def setChangeItems(self, value):
        for x in self._ChangeItems:
            x._Measurement = None
        for y in value:
            y._Measurement = self
        self._ChangeItems = value

    ChangeItems = property(getChangeItems, setChangeItems)

    def addChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj._Measurement = self
            self._ChangeItems.append(obj)

    def removeChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj._Measurement = None
            self._ChangeItems.remove(obj)

    def getViolationLimits(self):
        
        return self._ViolationLimits

    def setViolationLimits(self, value):
        for x in self._ViolationLimits:
            x._Measurement = None
        for y in value:
            y._Measurement = self
        self._ViolationLimits = value

    ViolationLimits = property(getViolationLimits, setViolationLimits)

    def addViolationLimits(self, *ViolationLimits):
        for obj in ViolationLimits:
            obj._Measurement = self
            self._ViolationLimits.append(obj)

    def removeViolationLimits(self, *ViolationLimits):
        for obj in ViolationLimits:
            obj._Measurement = None
            self._ViolationLimits.remove(obj)

    def getBy_TiePoint(self):
        """A measurement is made on the B side of a tie point
        """
        return self._By_TiePoint

    def setBy_TiePoint(self, value):
        if self._By_TiePoint is not None:
            filtered = [x for x in self.By_TiePoint.By_Measurements if x != self]
            self._By_TiePoint._By_Measurements = filtered

        self._By_TiePoint = value
        if self._By_TiePoint is not None:
            self._By_TiePoint._By_Measurements.append(self)

    By_TiePoint = property(getBy_TiePoint, setBy_TiePoint)

    def getUnit(self):
        """The Unit for the Measurement
        """
        return self._Unit

    def setUnit(self, value):
        if self._Unit is not None:
            filtered = [x for x in self.Unit.Measurements if x != self]
            self._Unit._Measurements = filtered

        self._Unit = value
        if self._Unit is not None:
            self._Unit._Measurements.append(self)

    Unit = property(getUnit, setUnit)

