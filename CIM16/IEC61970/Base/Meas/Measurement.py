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

from CIM16.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject

class Measurement(IdentifiedObject):
    """A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  Two possible paths exist: 1) Measurement-Terminal- ConnectivityNode-Terminal-ConductingEquipment 2) Measurement-Terminal-ConductingEquipment Alternative 2 is the only allowed use.  When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  Two possible paths exist: 1) Measurement-Terminal- ConnectivityNode-Terminal-ConductingEquipment 2) Measurement-Terminal-ConductingEquipment Alternative 2 is the only allowed use.  When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.
    """

    def __init__(self, phases="s12N", measurementType='', unitMultiplier="M", unitSymbol="N", Terminal=None, PowerSystemResource=None, Locations=None, Asset=None, Documents=None, *args, **kw_args):
        """Initialises a new 'Measurement' instance.

        @param phases: Indicates to which phases the measurement applies and avoids the need to use 'measurementType' to also encode phase information (which would explode the types). Since Controls have associations with Measurements, they will have the capability to handle each phase. The phase information in Measurement, along with 'measurementType' and 'phaseConnection' uniquely defines a Measurement for a device, based on normal network phase. Their meaning will not change when the computed energizing phasing is changed due to jumpers or other reasons. Values are: "s12N", "BN", "BC", "ABN", "s2N", "N", "ACN", "BCN", "ABCN", "AC", "s1N", "AN", "B", "AB", "C", "A", "CN", "ABC"
        @param measurementType: Specifies the type of Measurement, e.g. IndoorTemperature, OutDoorTemperature, BusVoltage, GeneratorVoltage, LineFlow etc. 
        @param unitMultiplier: The unit multiplier of the measured quantity. Values are: "M", "G", "d", "micro", "c", "p", "n", "T", "k", "m", "none"
        @param unitSymbol: The unit of measure of the measured quantity. Values are: "N", "A", "rad", "VAh", "Pa", "J", "h", "Hz", "VArh", "ohm", "H", "m3", "deg", "V", "degC", "F", "Wh", "s", "g", "min", "S", "none", "W", "VAr", "m2", "m", "VA"
        @param Terminal: One or more measurements may be associated with a terminal in the network
        @param PowerSystemResource: The PowerSystemResource that contains the Measurement in the naming hierarchy
        @param Locations:
        @param Asset:
        @param Documents: Measurements are specified in types of documents, such as procedures.
        """
        #: Indicates to which phases the measurement applies and avoids the need to use 'measurementType' to also encode phase information (which would explode the types). Since Controls have associations with Measurements, they will have the capability to handle each phase. The phase information in Measurement, along with 'measurementType' and 'phaseConnection' uniquely defines a Measurement for a device, based on normal network phase. Their meaning will not change when the computed energizing phasing is changed due to jumpers or other reasons. Values are: "s12N", "BN", "BC", "ABN", "s2N", "N", "ACN", "BCN", "ABCN", "AC", "s1N", "AN", "B", "AB", "C", "A", "CN", "ABC"
        self.phases = phases

        #: Specifies the type of Measurement, e.g. IndoorTemperature, OutDoorTemperature, BusVoltage, GeneratorVoltage, LineFlow etc.
        self.measurementType = measurementType

        #: The unit multiplier of the measured quantity. Values are: "M", "G", "d", "micro", "c", "p", "n", "T", "k", "m", "none"
        self.unitMultiplier = unitMultiplier

        #: The unit of measure of the measured quantity. Values are: "N", "A", "rad", "VAh", "Pa", "J", "h", "Hz", "VArh", "ohm", "H", "m3", "deg", "V", "degC", "F", "Wh", "s", "g", "min", "S", "none", "W", "VAr", "m2", "m", "VA"
        self.unitSymbol = unitSymbol

        self._Terminal = None
        self.Terminal = Terminal

        self._PowerSystemResource = None
        self.PowerSystemResource = PowerSystemResource

        self._Locations = []
        self.Locations = [] if Locations is None else Locations

        self._Asset = None
        self.Asset = Asset

        self._Documents = []
        self.Documents = [] if Documents is None else Documents

        super(Measurement, self).__init__(*args, **kw_args)

    _attrs = ["phases", "measurementType", "unitMultiplier", "unitSymbol"]
    _attr_types = {"phases": str, "measurementType": str, "unitMultiplier": str, "unitSymbol": str}
    _defaults = {"phases": "s12N", "measurementType": '', "unitMultiplier": "M", "unitSymbol": "N"}
    _enums = {"phases": "PhaseCode", "unitMultiplier": "UnitMultiplier", "unitSymbol": "UnitSymbol"}
    _refs = ["Terminal", "PowerSystemResource", "Locations", "Asset", "Documents"]
    _many_refs = ["Locations", "Documents"]

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
            if self not in self._Terminal._Measurements:
                self._Terminal._Measurements.append(self)

    Terminal = property(getTerminal, setTerminal)

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
            if self not in self._PowerSystemResource._Measurements:
                self._PowerSystemResource._Measurements.append(self)

    PowerSystemResource = property(getPowerSystemResource, setPowerSystemResource)

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

    def getAsset(self):
        
        return self._Asset

    def setAsset(self, value):
        if self._Asset is not None:
            filtered = [x for x in self.Asset.Measurements if x != self]
            self._Asset._Measurements = filtered

        self._Asset = value
        if self._Asset is not None:
            if self not in self._Asset._Measurements:
                self._Asset._Measurements.append(self)

    Asset = property(getAsset, setAsset)

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

