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

from CIM14.ENTSOE.Equipment.Core.Equipment import Equipment

class GeneratingUnit(Equipment):
    """A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.For the 2010 ENTSOE IOP, this is required for Synchronous Machine. -  To define a GeneratingUnit requires defining the initial real power injection, net real power limits, and the status of the unit.  The initial injection is defined using  the attribute “initialP”. -  The net real power limits can be defined in three ways; 1) with the attributes “maxOperatingP” and “minOperatingP”, or 2) with the attribute  “ratedNetMaxP” or 3) with the attributes “ratedGrossMinP” and “ratedGrossMaxP” used in conjunction with an associated GrossToNetActivePowerCurve. -  The control status of the unit is defined with the attribute “genControlSource”, but it is not required.  The participation factor attributes “longPF”, “normalPF”, and “shortPF” are not required. -  The GeneratingUnit class should only be used in cases where the more specific classes, HydroGeneratingUnit and ThermalGeneratingUnit, do not apply. -  The attributes governorSCD, maximumAllowableSpinningReserve, nominalP, startupCost, and variableCost are not required. 
    """

    def __init__(self, maxOperatingP=0.0, ratedGrossMaxP=0.0, variableCost=0.0, minOperatingP=0.0, ratedGrossMinP=0.0, shortPF=0.0, ratedNetMaxP=0.0, longPF=0.0, startupCost=0.0, genControlSource="onAGC", nominalP=0.0, governorSCD=0.0, maximumAllowableSpinningReserve=0.0, initialP=0.0, normalPF=0.0, SynchronousMachines=None, ControlAreaGeneratingUnit=None, *args, **kw_args):
        """Initialises a new 'GeneratingUnit' instance.

        @param maxOperatingP: This is the maximum operating active power limit the dispatcher can enter for this unit 
        @param ratedGrossMaxP: The unit's gross rated maximum capacity (Book Value). 
        @param variableCost: The variable cost component of production per unit of ActivePower. 
        @param minOperatingP: This is the minimum operating active power limit the dispatcher can enter for this unit. 
        @param ratedGrossMinP: The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid 
        @param shortPF: Generating unit economic participation factor 
        @param ratedNetMaxP: The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity 
        @param longPF: Generating unit economic participation factor 
        @param startupCost: The initial startup cost incurred for each start of the GeneratingUnit. 
        @param genControlSource: The source of controls for a generating unit. Values are: "onAGC", "unavailable", "plantControl", "offAGC"
        @param nominalP: The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute).Should not be null or zero. 
        @param governorSCD: Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency. 
        @param maximumAllowableSpinningReserve: Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point. 
        @param initialP: Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration 
        @param normalPF: Generating unit economic participation factor 
        @param SynchronousMachines: A synchronous machine may operate as a generator and as such becomes a member of a generating unit
        @param ControlAreaGeneratingUnit: ControlArea specifications for this generating unit.
        """
        #: This is the maximum operating active power limit the dispatcher can enter for this unit
        self.maxOperatingP = maxOperatingP

        #: The unit's gross rated maximum capacity (Book Value).
        self.ratedGrossMaxP = ratedGrossMaxP

        #: The variable cost component of production per unit of ActivePower.
        self.variableCost = variableCost

        #: This is the minimum operating active power limit the dispatcher can enter for this unit.
        self.minOperatingP = minOperatingP

        #: The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid
        self.ratedGrossMinP = ratedGrossMinP

        #: Generating unit economic participation factor
        self.shortPF = shortPF

        #: The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity
        self.ratedNetMaxP = ratedNetMaxP

        #: Generating unit economic participation factor
        self.longPF = longPF

        #: The initial startup cost incurred for each start of the GeneratingUnit.
        self.startupCost = startupCost

        #: The source of controls for a generating unit. Values are: "onAGC", "unavailable", "plantControl", "offAGC"
        self.genControlSource = genControlSource

        #: The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute).Should not be null or zero.
        self.nominalP = nominalP

        #: Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency.
        self.governorSCD = governorSCD

        #: Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point.
        self.maximumAllowableSpinningReserve = maximumAllowableSpinningReserve

        #: Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration
        self.initialP = initialP

        #: Generating unit economic participation factor
        self.normalPF = normalPF

        self._SynchronousMachines = []
        self.SynchronousMachines = [] if SynchronousMachines is None else SynchronousMachines

        self._ControlAreaGeneratingUnit = []
        self.ControlAreaGeneratingUnit = [] if ControlAreaGeneratingUnit is None else ControlAreaGeneratingUnit

        super(GeneratingUnit, self).__init__(*args, **kw_args)

    _attrs = ["maxOperatingP", "ratedGrossMaxP", "variableCost", "minOperatingP", "ratedGrossMinP", "shortPF", "ratedNetMaxP", "longPF", "startupCost", "genControlSource", "nominalP", "governorSCD", "maximumAllowableSpinningReserve", "initialP", "normalPF"]
    _attr_types = {"maxOperatingP": float, "ratedGrossMaxP": float, "variableCost": float, "minOperatingP": float, "ratedGrossMinP": float, "shortPF": float, "ratedNetMaxP": float, "longPF": float, "startupCost": float, "genControlSource": str, "nominalP": float, "governorSCD": float, "maximumAllowableSpinningReserve": float, "initialP": float, "normalPF": float}
    _defaults = {"maxOperatingP": 0.0, "ratedGrossMaxP": 0.0, "variableCost": 0.0, "minOperatingP": 0.0, "ratedGrossMinP": 0.0, "shortPF": 0.0, "ratedNetMaxP": 0.0, "longPF": 0.0, "startupCost": 0.0, "genControlSource": "onAGC", "nominalP": 0.0, "governorSCD": 0.0, "maximumAllowableSpinningReserve": 0.0, "initialP": 0.0, "normalPF": 0.0}
    _enums = {"genControlSource": "GeneratorControlSource"}
    _refs = ["SynchronousMachines", "ControlAreaGeneratingUnit"]
    _many_refs = ["SynchronousMachines", "ControlAreaGeneratingUnit"]

    def getSynchronousMachines(self):
        """A synchronous machine may operate as a generator and as such becomes a member of a generating unit
        """
        return self._SynchronousMachines

    def setSynchronousMachines(self, value):
        for x in self._SynchronousMachines:
            x.GeneratingUnit = None
        for y in value:
            y._GeneratingUnit = self
        self._SynchronousMachines = value

    SynchronousMachines = property(getSynchronousMachines, setSynchronousMachines)

    def addSynchronousMachines(self, *SynchronousMachines):
        for obj in SynchronousMachines:
            obj.GeneratingUnit = self

    def removeSynchronousMachines(self, *SynchronousMachines):
        for obj in SynchronousMachines:
            obj.GeneratingUnit = None

    def getControlAreaGeneratingUnit(self):
        """ControlArea specifications for this generating unit.
        """
        return self._ControlAreaGeneratingUnit

    def setControlAreaGeneratingUnit(self, value):
        for x in self._ControlAreaGeneratingUnit:
            x.GeneratingUnit = None
        for y in value:
            y._GeneratingUnit = self
        self._ControlAreaGeneratingUnit = value

    ControlAreaGeneratingUnit = property(getControlAreaGeneratingUnit, setControlAreaGeneratingUnit)

    def addControlAreaGeneratingUnit(self, *ControlAreaGeneratingUnit):
        for obj in ControlAreaGeneratingUnit:
            obj.GeneratingUnit = self

    def removeControlAreaGeneratingUnit(self, *ControlAreaGeneratingUnit):
        for obj in ControlAreaGeneratingUnit:
            obj.GeneratingUnit = None

