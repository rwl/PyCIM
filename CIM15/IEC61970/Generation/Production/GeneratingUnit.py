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

from CIM15.IEC61970.Core.Equipment import Equipment

class GeneratingUnit(Equipment):
    """A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.
    """

    def __init__(self, ratedGrossMinP=0.0, efficiency=0.0, stepChange=0.0, ratedNetMaxP=0.0, tieLinePF=0.0, dispReserveFlag=False, controlPulseHigh=0.0, startupTime=0.0, maxOperatingP=0.0, genControlSource="plantControl", normalPF=0.0, initialP=0.0, spinReserveRamp=0.0, allocSpinResP=0.0, minEconomicP=0.0, longPF=0.0, nominalP=0.0, controlResponseRate=0.0, ratedGrossMaxP=0.0, penaltyFactor=0.0, fastStartFlag=False, minimumOffTime=0.0, shortPF=0.0, governorMPL=0.0, energyMinP=0.0, fuelPriority=0, maxEconomicP=0.0, autoCntrlMarginP=0.0, highControlLimit=0.0, modelDetail="", controlPulseLow=0.0, raiseRampRate=0.0, controlDeadband=0.0, baseP=0.0, startupCost=0.0, variableCost=0.0, genOperatingMode="MRN", lowerRampRate=0.0, minOperatingP=0.0, lowControlLimit=0.0, maximumAllowableSpinningReserve=0.0, genControlMode="setpoint", governorSCD=0.0, ControlAreaGeneratingUnit=None, SynchronousMachines=None, GenUnitOpSchedule=None, GrossToNetActivePowerCurves=None, GenUnitOpCostCurves=None, *args, **kw_args):
        """Initialises a new 'GeneratingUnit' instance.

        @param ratedGrossMinP: The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid 
        @param efficiency: The efficiency of the unit in converting mechanical energy, from the prime mover, into electrical energy. 
        @param stepChange: 
        @param ratedNetMaxP: The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity 
        @param tieLinePF: Generating unit economic participation factor 
        @param dispReserveFlag: 
        @param controlPulseHigh: Pulse high limit which is the largest control pulse that the unit can respond to 
        @param startupTime: Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied 
        @param maxOperatingP: This is the maximum operating active power limit the dispatcher can enter for this unit 
        @param genControlSource: The source of controls for a generating unit. Values are: "plantControl", "offAGC", "unavailable", "onAGC"
        @param normalPF: Generating unit economic participation factor 
        @param initialP: Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration 
        @param spinReserveRamp: 
        @param allocSpinResP: The planned unused capacity (spinning reserve) which can be used to support emergency load 
        @param minEconomicP: Low economic active power limit that must be greater than or equal to the minimum operating active power limit 
        @param longPF: Generating unit economic participation factor 
        @param nominalP: The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute). 
        @param controlResponseRate: Unit response rate which specifies the active power change for a control pulse of one second in the most responsive loading level of the unit. 
        @param ratedGrossMaxP: The unit's gross rated maximum capacity (Book Value). 
        @param penaltyFactor: Defined as: 1 / ( 1 - Incremental Transmission Loss); with the Incremental Transmission Loss expressed as a plus or minus value. The typical range of penalty factors is (0.9 to 1.1). 
        @param fastStartFlag: 
        @param minimumOffTime: Minimum time interval between unit shutdown and startup 
        @param shortPF: Generating unit economic participation factor 
        @param governorMPL: Governor Motor Position Limit 
        @param energyMinP: 
        @param fuelPriority: 
        @param maxEconomicP: Maximum high economic active power limit, that should not exceed the maximum operating active power limit 
        @param autoCntrlMarginP: The planned unused capacity which can be used to support automatic control overruns. 
        @param highControlLimit: High limit for secondary (AGC) control 
        @param modelDetail: Detail level of the generator model data 
        @param controlPulseLow: Pulse low limit which is the smallest control pulse that the unit can respond to 
        @param raiseRampRate: 
        @param controlDeadband: Unit control error deadband. When a unit's desired active power change is less than this deadband, then no control pulses will be sent to the unit. 
        @param baseP: For dispatchable units, this value represents the economic active power basepoint, for units that are not dispatchable, this value represents the fixed generation value. The value must be between the operating low and high limits. 
        @param startupCost: The initial startup cost incurred for each start of the GeneratingUnit. 
        @param variableCost: The variable cost component of production per unit of ActivePower. 
        @param genOperatingMode: Operating mode for secondary control. Values are: "MRN", "EDC", "LFC", "fixed", "REG", "AGC", "manual", "off"
        @param lowerRampRate: 
        @param minOperatingP: This is the minimum operating active power limit the dispatcher can enter for this unit. 
        @param lowControlLimit: Low limit for secondary (AGC) control 
        @param maximumAllowableSpinningReserve: Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point. 
        @param genControlMode: The unit control mode. Values are: "setpoint", "pulse"
        @param governorSCD: Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency. 
        @param ControlAreaGeneratingUnit: ControlArea specifications for this generating unit.
        @param SynchronousMachines: A synchronous machine may operate as a generator and as such becomes a member of a generating unit
        @param GenUnitOpSchedule: A generating unit may have an operating schedule, indicating the planned operation of the unit
        @param GrossToNetActivePowerCurves: A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
        @param GenUnitOpCostCurves: A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.
        """
        #: The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid
        self.ratedGrossMinP = ratedGrossMinP

        #: The efficiency of the unit in converting mechanical energy, from the prime mover, into electrical energy.
        self.efficiency = efficiency


        self.stepChange = stepChange

        #: The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity
        self.ratedNetMaxP = ratedNetMaxP

        #: Generating unit economic participation factor
        self.tieLinePF = tieLinePF


        self.dispReserveFlag = dispReserveFlag

        #: Pulse high limit which is the largest control pulse that the unit can respond to
        self.controlPulseHigh = controlPulseHigh

        #: Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied
        self.startupTime = startupTime

        #: This is the maximum operating active power limit the dispatcher can enter for this unit
        self.maxOperatingP = maxOperatingP

        #: The source of controls for a generating unit. Values are: "plantControl", "offAGC", "unavailable", "onAGC"
        self.genControlSource = genControlSource

        #: Generating unit economic participation factor
        self.normalPF = normalPF

        #: Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration
        self.initialP = initialP


        self.spinReserveRamp = spinReserveRamp

        #: The planned unused capacity (spinning reserve) which can be used to support emergency load
        self.allocSpinResP = allocSpinResP

        #: Low economic active power limit that must be greater than or equal to the minimum operating active power limit
        self.minEconomicP = minEconomicP

        #: Generating unit economic participation factor
        self.longPF = longPF

        #: The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute).
        self.nominalP = nominalP

        #: Unit response rate which specifies the active power change for a control pulse of one second in the most responsive loading level of the unit.
        self.controlResponseRate = controlResponseRate

        #: The unit's gross rated maximum capacity (Book Value).
        self.ratedGrossMaxP = ratedGrossMaxP

        #: Defined as: 1 / ( 1 - Incremental Transmission Loss); with the Incremental Transmission Loss expressed as a plus or minus value. The typical range of penalty factors is (0.9 to 1.1).
        self.penaltyFactor = penaltyFactor


        self.fastStartFlag = fastStartFlag

        #: Minimum time interval between unit shutdown and startup
        self.minimumOffTime = minimumOffTime

        #: Generating unit economic participation factor
        self.shortPF = shortPF

        #: Governor Motor Position Limit
        self.governorMPL = governorMPL


        self.energyMinP = energyMinP


        self.fuelPriority = fuelPriority

        #: Maximum high economic active power limit, that should not exceed the maximum operating active power limit
        self.maxEconomicP = maxEconomicP

        #: The planned unused capacity which can be used to support automatic control overruns.
        self.autoCntrlMarginP = autoCntrlMarginP

        #: High limit for secondary (AGC) control
        self.highControlLimit = highControlLimit

        #: Detail level of the generator model data
        self.modelDetail = modelDetail

        #: Pulse low limit which is the smallest control pulse that the unit can respond to
        self.controlPulseLow = controlPulseLow


        self.raiseRampRate = raiseRampRate

        #: Unit control error deadband. When a unit's desired active power change is less than this deadband, then no control pulses will be sent to the unit.
        self.controlDeadband = controlDeadband

        #: For dispatchable units, this value represents the economic active power basepoint, for units that are not dispatchable, this value represents the fixed generation value. The value must be between the operating low and high limits.
        self.baseP = baseP

        #: The initial startup cost incurred for each start of the GeneratingUnit.
        self.startupCost = startupCost

        #: The variable cost component of production per unit of ActivePower.
        self.variableCost = variableCost

        #: Operating mode for secondary control. Values are: "MRN", "EDC", "LFC", "fixed", "REG", "AGC", "manual", "off"
        self.genOperatingMode = genOperatingMode


        self.lowerRampRate = lowerRampRate

        #: This is the minimum operating active power limit the dispatcher can enter for this unit.
        self.minOperatingP = minOperatingP

        #: Low limit for secondary (AGC) control
        self.lowControlLimit = lowControlLimit

        #: Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point.
        self.maximumAllowableSpinningReserve = maximumAllowableSpinningReserve

        #: The unit control mode. Values are: "setpoint", "pulse"
        self.genControlMode = genControlMode

        #: Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency.
        self.governorSCD = governorSCD

        self._ControlAreaGeneratingUnit = []
        self.ControlAreaGeneratingUnit = [] if ControlAreaGeneratingUnit is None else ControlAreaGeneratingUnit

        self._SynchronousMachines = []
        self.SynchronousMachines = [] if SynchronousMachines is None else SynchronousMachines

        self._GenUnitOpSchedule = None
        self.GenUnitOpSchedule = GenUnitOpSchedule

        self._GrossToNetActivePowerCurves = []
        self.GrossToNetActivePowerCurves = [] if GrossToNetActivePowerCurves is None else GrossToNetActivePowerCurves

        self._GenUnitOpCostCurves = []
        self.GenUnitOpCostCurves = [] if GenUnitOpCostCurves is None else GenUnitOpCostCurves

        super(GeneratingUnit, self).__init__(*args, **kw_args)

    _attrs = ["ratedGrossMinP", "efficiency", "stepChange", "ratedNetMaxP", "tieLinePF", "dispReserveFlag", "controlPulseHigh", "startupTime", "maxOperatingP", "genControlSource", "normalPF", "initialP", "spinReserveRamp", "allocSpinResP", "minEconomicP", "longPF", "nominalP", "controlResponseRate", "ratedGrossMaxP", "penaltyFactor", "fastStartFlag", "minimumOffTime", "shortPF", "governorMPL", "energyMinP", "fuelPriority", "maxEconomicP", "autoCntrlMarginP", "highControlLimit", "modelDetail", "controlPulseLow", "raiseRampRate", "controlDeadband", "baseP", "startupCost", "variableCost", "genOperatingMode", "lowerRampRate", "minOperatingP", "lowControlLimit", "maximumAllowableSpinningReserve", "genControlMode", "governorSCD"]
    _attr_types = {"ratedGrossMinP": float, "efficiency": float, "stepChange": float, "ratedNetMaxP": float, "tieLinePF": float, "dispReserveFlag": bool, "controlPulseHigh": float, "startupTime": float, "maxOperatingP": float, "genControlSource": str, "normalPF": float, "initialP": float, "spinReserveRamp": float, "allocSpinResP": float, "minEconomicP": float, "longPF": float, "nominalP": float, "controlResponseRate": float, "ratedGrossMaxP": float, "penaltyFactor": float, "fastStartFlag": bool, "minimumOffTime": float, "shortPF": float, "governorMPL": float, "energyMinP": float, "fuelPriority": int, "maxEconomicP": float, "autoCntrlMarginP": float, "highControlLimit": float, "modelDetail": str, "controlPulseLow": float, "raiseRampRate": float, "controlDeadband": float, "baseP": float, "startupCost": float, "variableCost": float, "genOperatingMode": str, "lowerRampRate": float, "minOperatingP": float, "lowControlLimit": float, "maximumAllowableSpinningReserve": float, "genControlMode": str, "governorSCD": float}
    _defaults = {"ratedGrossMinP": 0.0, "efficiency": 0.0, "stepChange": 0.0, "ratedNetMaxP": 0.0, "tieLinePF": 0.0, "dispReserveFlag": False, "controlPulseHigh": 0.0, "startupTime": 0.0, "maxOperatingP": 0.0, "genControlSource": "plantControl", "normalPF": 0.0, "initialP": 0.0, "spinReserveRamp": 0.0, "allocSpinResP": 0.0, "minEconomicP": 0.0, "longPF": 0.0, "nominalP": 0.0, "controlResponseRate": 0.0, "ratedGrossMaxP": 0.0, "penaltyFactor": 0.0, "fastStartFlag": False, "minimumOffTime": 0.0, "shortPF": 0.0, "governorMPL": 0.0, "energyMinP": 0.0, "fuelPriority": 0, "maxEconomicP": 0.0, "autoCntrlMarginP": 0.0, "highControlLimit": 0.0, "modelDetail": "", "controlPulseLow": 0.0, "raiseRampRate": 0.0, "controlDeadband": 0.0, "baseP": 0.0, "startupCost": 0.0, "variableCost": 0.0, "genOperatingMode": "MRN", "lowerRampRate": 0.0, "minOperatingP": 0.0, "lowControlLimit": 0.0, "maximumAllowableSpinningReserve": 0.0, "genControlMode": "setpoint", "governorSCD": 0.0}
    _enums = {"genControlSource": "GeneratorControlSource", "genOperatingMode": "GeneratorOperatingMode", "genControlMode": "GeneratorControlMode"}
    _refs = ["ControlAreaGeneratingUnit", "SynchronousMachines", "GenUnitOpSchedule", "GrossToNetActivePowerCurves", "GenUnitOpCostCurves"]
    _many_refs = ["ControlAreaGeneratingUnit", "SynchronousMachines", "GrossToNetActivePowerCurves", "GenUnitOpCostCurves"]

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

    def getGenUnitOpSchedule(self):
        """A generating unit may have an operating schedule, indicating the planned operation of the unit
        """
        return self._GenUnitOpSchedule

    def setGenUnitOpSchedule(self, value):
        if self._GenUnitOpSchedule is not None:
            self._GenUnitOpSchedule._GeneratingUnit = None

        self._GenUnitOpSchedule = value
        if self._GenUnitOpSchedule is not None:
            self._GenUnitOpSchedule.GeneratingUnit = None
            self._GenUnitOpSchedule._GeneratingUnit = self

    GenUnitOpSchedule = property(getGenUnitOpSchedule, setGenUnitOpSchedule)

    def getGrossToNetActivePowerCurves(self):
        """A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
        """
        return self._GrossToNetActivePowerCurves

    def setGrossToNetActivePowerCurves(self, value):
        for x in self._GrossToNetActivePowerCurves:
            x.GeneratingUnit = None
        for y in value:
            y._GeneratingUnit = self
        self._GrossToNetActivePowerCurves = value

    GrossToNetActivePowerCurves = property(getGrossToNetActivePowerCurves, setGrossToNetActivePowerCurves)

    def addGrossToNetActivePowerCurves(self, *GrossToNetActivePowerCurves):
        for obj in GrossToNetActivePowerCurves:
            obj.GeneratingUnit = self

    def removeGrossToNetActivePowerCurves(self, *GrossToNetActivePowerCurves):
        for obj in GrossToNetActivePowerCurves:
            obj.GeneratingUnit = None

    def getGenUnitOpCostCurves(self):
        """A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.
        """
        return self._GenUnitOpCostCurves

    def setGenUnitOpCostCurves(self, value):
        for x in self._GenUnitOpCostCurves:
            x.GeneratingUnit = None
        for y in value:
            y._GeneratingUnit = self
        self._GenUnitOpCostCurves = value

    GenUnitOpCostCurves = property(getGenUnitOpCostCurves, setGenUnitOpCostCurves)

    def addGenUnitOpCostCurves(self, *GenUnitOpCostCurves):
        for obj in GenUnitOpCostCurves:
            obj.GeneratingUnit = self

    def removeGenUnitOpCostCurves(self, *GenUnitOpCostCurves):
        for obj in GenUnitOpCostCurves:
            obj.GeneratingUnit = None

