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

from CIM14.IEC61970.Core.Equipment import Equipment

class GeneratingUnit(Equipment):
    """A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.
    """

    def __init__(self, genControlMode="setpoint", genOperatingMode="fixed", genControlSource="unavailable", startupTime=0.0, minimumOffTime=0.0, spinReserveRamp=0.0, controlDeadband=0.0, maxOperatingP=0.0, fastStartFlag=False, lowControlLimit=0.0, baseP=0.0, maxEconomicP=0.0, efficiency=0.0, shortPF=0.0, lowerRampRate=0.0, stepChange=0.0, penaltyFactor=0.0, longPF=0.0, ratedGrossMinP=0.0, ratedGrossMaxP=0.0, dispReserveFlag=False, variableCost=0.0, modelDetail=0, energyMinP=0.0, maximumAllowableSpinningReserve=0.0, fuelPriority=0, raiseRampRate=0.0, nominalP=0.0, normalPF=0.0, governorMPL=0.0, ratedNetMaxP=0.0, controlResponseRate=0.0, tieLinePF=0.0, governorSCD=0.0, controlPulseLow=0.0, highControlLimit=0.0, initialP=0.0, minEconomicP=0.0, autoCntrlMarginP=0.0, allocSpinResP=0.0, startupCost=0.0, minOperatingP=0.0, controlPulseHigh=0.0, SynchronousMachines=None, GrossToNetActivePowerCurves=None, GenUnitOpCostCurves=None, GenUnitOpSchedule=None, ControlAreaGeneratingUnit=None, *args, **kw_args):
        """Initialises a new 'GeneratingUnit' instance.

        @param genControlMode: The unit control mode. Values are: "setpoint", "pulse"
        @param genOperatingMode: Operating mode for secondary control. Values are: "fixed", "EDC", "manual", "off", "MRN", "LFC", "AGC", "REG"
        @param genControlSource: The source of controls for a generating unit. Values are: "unavailable", "onAGC", "plantControl", "offAGC"
        @param startupTime: Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied 
        @param minimumOffTime: Minimum time interval between unit shutdown and startup 
        @param spinReserveRamp: 
        @param controlDeadband: Unit control error deadband. When a unit's desired active power change is less than this deadband, then no control pulses will be sent to the unit. 
        @param maxOperatingP: This is the maximum operating active power limit the dispatcher can enter for this unit 
        @param fastStartFlag: 
        @param lowControlLimit: Low limit for secondary (AGC) control 
        @param baseP: For dispatchable units, this value represents the economic active power basepoint, for units that are not dispatchable, this value represents the fixed generation value. The value must be between the operating low and high limits. 
        @param maxEconomicP: Maximum high economic active power limit, that should not exceed the maximum operating active power limit 
        @param efficiency: The efficiency of the unit in converting mechanical energy, from the prime mover, into electrical energy. 
        @param shortPF: Generating unit economic participation factor 
        @param lowerRampRate: 
        @param stepChange: 
        @param penaltyFactor: Defined as: 1 / ( 1 - Incremental Transmission Loss); with the Incremental Transmission Loss expressed as a plus or minus value. The typical range of penalty factors is (0.9 to 1.1). 
        @param longPF: Generating unit economic participation factor 
        @param ratedGrossMinP: The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid 
        @param ratedGrossMaxP: The unit's gross rated maximum capacity (Book Value). 
        @param dispReserveFlag: 
        @param variableCost: The variable cost component of production per unit of ActivePower. 
        @param modelDetail: Detail level of the generator model data 
        @param energyMinP: 
        @param maximumAllowableSpinningReserve: Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point. 
        @param fuelPriority: 
        @param raiseRampRate: 
        @param nominalP: The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute). 
        @param normalPF: Generating unit economic participation factor 
        @param governorMPL: Governor Motor Position Limit 
        @param ratedNetMaxP: The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity 
        @param controlResponseRate: Unit response rate which specifies the active power change for a control pulse of one second in the most responsive loading level of the unit. 
        @param tieLinePF: Generating unit economic participation factor 
        @param governorSCD: Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency. 
        @param controlPulseLow: Pulse low limit which is the smallest control pulse that the unit can respond to 
        @param highControlLimit: High limit for secondary (AGC) control 
        @param initialP: Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration 
        @param minEconomicP: Low economic active power limit that must be greater than or equal to the minimum operating active power limit 
        @param autoCntrlMarginP: The planned unused capacity which can be used to support automatic control overruns. 
        @param allocSpinResP: The planned unused capacity (spinning reserve) which can be used to support emergency load 
        @param startupCost: The initial startup cost incurred for each start of the GeneratingUnit. 
        @param minOperatingP: This is the minimum operating active power limit the dispatcher can enter for this unit. 
        @param controlPulseHigh: Pulse high limit which is the largest control pulse that the unit can respond to 
        @param SynchronousMachines: A synchronous machine may operate as a generator and as such becomes a member of a generating unit
        @param GrossToNetActivePowerCurves: A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
        @param GenUnitOpCostCurves: A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.
        @param GenUnitOpSchedule: A generating unit may have an operating schedule, indicating the planned operation of the unit
        @param ControlAreaGeneratingUnit: ControlArea specifications for this generating unit.
        """
        #: The unit control mode. Values are: "setpoint", "pulse"
        self.genControlMode = genControlMode

        #: Operating mode for secondary control. Values are: "fixed", "EDC", "manual", "off", "MRN", "LFC", "AGC", "REG"
        self.genOperatingMode = genOperatingMode

        #: The source of controls for a generating unit. Values are: "unavailable", "onAGC", "plantControl", "offAGC"
        self.genControlSource = genControlSource

        #: Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied
        self.startupTime = startupTime

        #: Minimum time interval between unit shutdown and startup
        self.minimumOffTime = minimumOffTime


        self.spinReserveRamp = spinReserveRamp

        #: Unit control error deadband. When a unit's desired active power change is less than this deadband, then no control pulses will be sent to the unit.
        self.controlDeadband = controlDeadband

        #: This is the maximum operating active power limit the dispatcher can enter for this unit
        self.maxOperatingP = maxOperatingP


        self.fastStartFlag = fastStartFlag

        #: Low limit for secondary (AGC) control
        self.lowControlLimit = lowControlLimit

        #: For dispatchable units, this value represents the economic active power basepoint, for units that are not dispatchable, this value represents the fixed generation value. The value must be between the operating low and high limits.
        self.baseP = baseP

        #: Maximum high economic active power limit, that should not exceed the maximum operating active power limit
        self.maxEconomicP = maxEconomicP

        #: The efficiency of the unit in converting mechanical energy, from the prime mover, into electrical energy.
        self.efficiency = efficiency

        #: Generating unit economic participation factor
        self.shortPF = shortPF


        self.lowerRampRate = lowerRampRate


        self.stepChange = stepChange

        #: Defined as: 1 / ( 1 - Incremental Transmission Loss); with the Incremental Transmission Loss expressed as a plus or minus value. The typical range of penalty factors is (0.9 to 1.1).
        self.penaltyFactor = penaltyFactor

        #: Generating unit economic participation factor
        self.longPF = longPF

        #: The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid
        self.ratedGrossMinP = ratedGrossMinP

        #: The unit's gross rated maximum capacity (Book Value).
        self.ratedGrossMaxP = ratedGrossMaxP


        self.dispReserveFlag = dispReserveFlag

        #: The variable cost component of production per unit of ActivePower.
        self.variableCost = variableCost

        #: Detail level of the generator model data
        self.modelDetail = modelDetail


        self.energyMinP = energyMinP

        #: Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point.
        self.maximumAllowableSpinningReserve = maximumAllowableSpinningReserve


        self.fuelPriority = fuelPriority


        self.raiseRampRate = raiseRampRate

        #: The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute).
        self.nominalP = nominalP

        #: Generating unit economic participation factor
        self.normalPF = normalPF

        #: Governor Motor Position Limit
        self.governorMPL = governorMPL

        #: The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity
        self.ratedNetMaxP = ratedNetMaxP

        #: Unit response rate which specifies the active power change for a control pulse of one second in the most responsive loading level of the unit.
        self.controlResponseRate = controlResponseRate

        #: Generating unit economic participation factor
        self.tieLinePF = tieLinePF

        #: Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency.
        self.governorSCD = governorSCD

        #: Pulse low limit which is the smallest control pulse that the unit can respond to
        self.controlPulseLow = controlPulseLow

        #: High limit for secondary (AGC) control
        self.highControlLimit = highControlLimit

        #: Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration
        self.initialP = initialP

        #: Low economic active power limit that must be greater than or equal to the minimum operating active power limit
        self.minEconomicP = minEconomicP

        #: The planned unused capacity which can be used to support automatic control overruns.
        self.autoCntrlMarginP = autoCntrlMarginP

        #: The planned unused capacity (spinning reserve) which can be used to support emergency load
        self.allocSpinResP = allocSpinResP

        #: The initial startup cost incurred for each start of the GeneratingUnit.
        self.startupCost = startupCost

        #: This is the minimum operating active power limit the dispatcher can enter for this unit.
        self.minOperatingP = minOperatingP

        #: Pulse high limit which is the largest control pulse that the unit can respond to
        self.controlPulseHigh = controlPulseHigh

        self._SynchronousMachines = []
        self.SynchronousMachines = [] if SynchronousMachines is None else SynchronousMachines

        self._GrossToNetActivePowerCurves = []
        self.GrossToNetActivePowerCurves = [] if GrossToNetActivePowerCurves is None else GrossToNetActivePowerCurves

        self._GenUnitOpCostCurves = []
        self.GenUnitOpCostCurves = [] if GenUnitOpCostCurves is None else GenUnitOpCostCurves

        self._GenUnitOpSchedule = None
        self.GenUnitOpSchedule = GenUnitOpSchedule

        self._ControlAreaGeneratingUnit = []
        self.ControlAreaGeneratingUnit = [] if ControlAreaGeneratingUnit is None else ControlAreaGeneratingUnit

        super(GeneratingUnit, self).__init__(*args, **kw_args)

    _attrs = ["genControlMode", "genOperatingMode", "genControlSource", "startupTime", "minimumOffTime", "spinReserveRamp", "controlDeadband", "maxOperatingP", "fastStartFlag", "lowControlLimit", "baseP", "maxEconomicP", "efficiency", "shortPF", "lowerRampRate", "stepChange", "penaltyFactor", "longPF", "ratedGrossMinP", "ratedGrossMaxP", "dispReserveFlag", "variableCost", "modelDetail", "energyMinP", "maximumAllowableSpinningReserve", "fuelPriority", "raiseRampRate", "nominalP", "normalPF", "governorMPL", "ratedNetMaxP", "controlResponseRate", "tieLinePF", "governorSCD", "controlPulseLow", "highControlLimit", "initialP", "minEconomicP", "autoCntrlMarginP", "allocSpinResP", "startupCost", "minOperatingP", "controlPulseHigh"]
    _attr_types = {"genControlMode": str, "genOperatingMode": str, "genControlSource": str, "startupTime": float, "minimumOffTime": float, "spinReserveRamp": float, "controlDeadband": float, "maxOperatingP": float, "fastStartFlag": bool, "lowControlLimit": float, "baseP": float, "maxEconomicP": float, "efficiency": float, "shortPF": float, "lowerRampRate": float, "stepChange": float, "penaltyFactor": float, "longPF": float, "ratedGrossMinP": float, "ratedGrossMaxP": float, "dispReserveFlag": bool, "variableCost": float, "modelDetail": int, "energyMinP": float, "maximumAllowableSpinningReserve": float, "fuelPriority": int, "raiseRampRate": float, "nominalP": float, "normalPF": float, "governorMPL": float, "ratedNetMaxP": float, "controlResponseRate": float, "tieLinePF": float, "governorSCD": float, "controlPulseLow": float, "highControlLimit": float, "initialP": float, "minEconomicP": float, "autoCntrlMarginP": float, "allocSpinResP": float, "startupCost": float, "minOperatingP": float, "controlPulseHigh": float}
    _defaults = {"genControlMode": "setpoint", "genOperatingMode": "fixed", "genControlSource": "unavailable", "startupTime": 0.0, "minimumOffTime": 0.0, "spinReserveRamp": 0.0, "controlDeadband": 0.0, "maxOperatingP": 0.0, "fastStartFlag": False, "lowControlLimit": 0.0, "baseP": 0.0, "maxEconomicP": 0.0, "efficiency": 0.0, "shortPF": 0.0, "lowerRampRate": 0.0, "stepChange": 0.0, "penaltyFactor": 0.0, "longPF": 0.0, "ratedGrossMinP": 0.0, "ratedGrossMaxP": 0.0, "dispReserveFlag": False, "variableCost": 0.0, "modelDetail": 0, "energyMinP": 0.0, "maximumAllowableSpinningReserve": 0.0, "fuelPriority": 0, "raiseRampRate": 0.0, "nominalP": 0.0, "normalPF": 0.0, "governorMPL": 0.0, "ratedNetMaxP": 0.0, "controlResponseRate": 0.0, "tieLinePF": 0.0, "governorSCD": 0.0, "controlPulseLow": 0.0, "highControlLimit": 0.0, "initialP": 0.0, "minEconomicP": 0.0, "autoCntrlMarginP": 0.0, "allocSpinResP": 0.0, "startupCost": 0.0, "minOperatingP": 0.0, "controlPulseHigh": 0.0}
    _enums = {"genControlMode": "GeneratorControlMode", "genOperatingMode": "GeneratorOperatingMode", "genControlSource": "GeneratorControlSource"}
    _refs = ["SynchronousMachines", "GrossToNetActivePowerCurves", "GenUnitOpCostCurves", "GenUnitOpSchedule", "ControlAreaGeneratingUnit"]
    _many_refs = ["SynchronousMachines", "GrossToNetActivePowerCurves", "GenUnitOpCostCurves", "ControlAreaGeneratingUnit"]

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

