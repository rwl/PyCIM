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

from CIM14v13.IEC61970.Core.Equipment import Equipment

class GeneratingUnit(Equipment):
    """A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.
    """

    def __init__(self, genOperatingMode='off', genControlMode='setpoint', genControlSource='onAGC', variableCost=0.0, shortPF=0.0, ratedGrossMinP=0.0, maxOperatingP=0.0, maximumAllowableSpinningReserve=0.0, startupTime=0.0, longPF=0.0, initialP=0.0, lowerRampRate=0.0, minimumOffTime=0.0, spinReserveRamp=0.0, fuelPriority=0, ratedGrossMaxP=0.0, modelDetail=0, efficiency=0.0, raiseRampRate=0.0, tieLinePF=0.0, penaltyFactor=0.0, minOperatingP=0.0, autoCntrlMarginP=0.0, minEconomicP=0.0, controlDeadband=0.0, dispReserveFlag=False, normalPF=0.0, highControlLimit=0.0, allocSpinResP=0.0, lowControlLimit=0.0, governorMPL=0.0, controlPulseLow=0.0, fastStartFlag=False, nominalP=0.0, baseP=0.0, ratedNetMaxP=0.0, maxEconomicP=0.0, controlResponseRate=0.0, stepChange=0.0, energyMinP=0.0, startupCost=0.0, governorSCD=0.0, controlPulseHigh=0.0, OperatedBy_GenerationProvider=None, ControlAreaGeneratingUnit=None, GenUnitOpCostCurves=None, SubControlArea=None, RegisteredGenerator=None, SynchronousMachines=None, GenUnitOpSchedule=None, GrossToNetActivePowerCurves=None, *args, **kw_args):
        """Initializes a new 'GeneratingUnit' instance.

        @param genOperatingMode: Operating mode for secondary control. Values are: "off", "AGC", "manual", "MRN", "LFC", "EDC", "fixed", "REG"
        @param genControlMode: The unit control mode. Values are: "setpoint", "pulse"
        @param genControlSource: The source of controls for a generating unit. Values are: "onAGC", "plantControl", "unavailable", "offAGC"
        @param variableCost: The variable cost component of production per unit of ActivePower. 
        @param shortPF: Generating unit economic participation factor 
        @param ratedGrossMinP: The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid 
        @param maxOperatingP: This is the maximum operating active power limit the dispatcher can enter for this unit 
        @param maximumAllowableSpinningReserve: Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point. 
        @param startupTime: Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied 
        @param longPF: Generating unit economic participation factor 
        @param initialP: Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration 
        @param lowerRampRate: 
        @param minimumOffTime: Minimum time interval between unit shutdown and startup 
        @param spinReserveRamp: 
        @param fuelPriority: 
        @param ratedGrossMaxP: The unit's gross rated maximum capacity (Book Value). 
        @param modelDetail: Detail level of the generator model data 
        @param efficiency: The efficiency of the unit in converting mechanical energy, from the prime mover, into electrical energy. 
        @param raiseRampRate: 
        @param tieLinePF: Generating unit economic participation factor 
        @param penaltyFactor: Defined as: 1 / ( 1 - Incremental Transmission Loss); with the Incremental Transmission Loss expressed as a plus or minus value. The typical range of penalty factors is (0.9 to 1.1). 
        @param minOperatingP: This is the minimum operating active power limit the dispatcher can enter for this unit. 
        @param autoCntrlMarginP: The planned unused capacity which can be used to support automatic control overruns. 
        @param minEconomicP: Low economic active power limit that must be greater than or equal to the minimum operating active power limit 
        @param controlDeadband: Unit control error deadband. When a unit's desired active power change is less than this deadband, then no control pulses will be sent to the unit. 
        @param dispReserveFlag: 
        @param normalPF: Generating unit economic participation factor 
        @param highControlLimit: High limit for secondary (AGC) control 
        @param allocSpinResP: The planned unused capacity (spinning reserve) which can be used to support emergency load 
        @param lowControlLimit: Low limit for secondary (AGC) control 
        @param governorMPL: Governor Motor Position Limit 
        @param controlPulseLow: Pulse low limit which is the smallest control pulse that the unit can respond to 
        @param fastStartFlag: 
        @param nominalP: The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute). 
        @param baseP: For dispatchable units, this value represents the economic active power basepoint, for units that are not dispatchable, this value represents the fixed generation value. The value must be between the operating low and high limits. 
        @param ratedNetMaxP: The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity 
        @param maxEconomicP: Maximum high economic active power limit, that should not exceed the maximum operating active power limit 
        @param controlResponseRate: Unit response rate which specifies the active power change for a control pulse of one second in the most responsive loading level of the unit. 
        @param stepChange: 
        @param energyMinP: 
        @param startupCost: The initial startup cost incurred for each start of the GeneratingUnit. 
        @param governorSCD: Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency. 
        @param controlPulseHigh: Pulse high limit which is the largest control pulse that the unit can respond to 
        @param OperatedBy_GenerationProvider: A GenerationProvider operates one or more GeneratingUnits.
        @param ControlAreaGeneratingUnit: ControlArea specifications for this generating unit.
        @param GenUnitOpCostCurves: A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.
        @param SubControlArea: A GeneratingUnit injects energy into a SubControlArea.
        @param RegisteredGenerator:
        @param SynchronousMachines: A synchronous machine may operate as a generator and as such becomes a member of a generating unit
        @param GenUnitOpSchedule: A generating unit may have an operating schedule, indicating the planned operation of the unit
        @param GrossToNetActivePowerCurves: A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
        """
        #: Operating mode for secondary control. Values are: "off", "AGC", "manual", "MRN", "LFC", "EDC", "fixed", "REG"
        self.genOperatingMode = genOperatingMode

        #: The unit control mode. Values are: "setpoint", "pulse"
        self.genControlMode = genControlMode

        #: The source of controls for a generating unit. Values are: "onAGC", "plantControl", "unavailable", "offAGC"
        self.genControlSource = genControlSource

        #: The variable cost component of production per unit of ActivePower. 
        self.variableCost = variableCost

        #: Generating unit economic participation factor 
        self.shortPF = shortPF

        #: The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid 
        self.ratedGrossMinP = ratedGrossMinP

        #: This is the maximum operating active power limit the dispatcher can enter for this unit 
        self.maxOperatingP = maxOperatingP

        #: Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point. 
        self.maximumAllowableSpinningReserve = maximumAllowableSpinningReserve

        #: Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied 
        self.startupTime = startupTime

        #: Generating unit economic participation factor 
        self.longPF = longPF

        #: Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration 
        self.initialP = initialP

 
        self.lowerRampRate = lowerRampRate

        #: Minimum time interval between unit shutdown and startup 
        self.minimumOffTime = minimumOffTime

 
        self.spinReserveRamp = spinReserveRamp

 
        self.fuelPriority = fuelPriority

        #: The unit's gross rated maximum capacity (Book Value). 
        self.ratedGrossMaxP = ratedGrossMaxP

        #: Detail level of the generator model data 
        self.modelDetail = modelDetail

        #: The efficiency of the unit in converting mechanical energy, from the prime mover, into electrical energy. 
        self.efficiency = efficiency

 
        self.raiseRampRate = raiseRampRate

        #: Generating unit economic participation factor 
        self.tieLinePF = tieLinePF

        #: Defined as: 1 / ( 1 - Incremental Transmission Loss); with the Incremental Transmission Loss expressed as a plus or minus value. The typical range of penalty factors is (0.9 to 1.1). 
        self.penaltyFactor = penaltyFactor

        #: This is the minimum operating active power limit the dispatcher can enter for this unit. 
        self.minOperatingP = minOperatingP

        #: The planned unused capacity which can be used to support automatic control overruns. 
        self.autoCntrlMarginP = autoCntrlMarginP

        #: Low economic active power limit that must be greater than or equal to the minimum operating active power limit 
        self.minEconomicP = minEconomicP

        #: Unit control error deadband. When a unit's desired active power change is less than this deadband, then no control pulses will be sent to the unit. 
        self.controlDeadband = controlDeadband

 
        self.dispReserveFlag = dispReserveFlag

        #: Generating unit economic participation factor 
        self.normalPF = normalPF

        #: High limit for secondary (AGC) control 
        self.highControlLimit = highControlLimit

        #: The planned unused capacity (spinning reserve) which can be used to support emergency load 
        self.allocSpinResP = allocSpinResP

        #: Low limit for secondary (AGC) control 
        self.lowControlLimit = lowControlLimit

        #: Governor Motor Position Limit 
        self.governorMPL = governorMPL

        #: Pulse low limit which is the smallest control pulse that the unit can respond to 
        self.controlPulseLow = controlPulseLow

 
        self.fastStartFlag = fastStartFlag

        #: The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute). 
        self.nominalP = nominalP

        #: For dispatchable units, this value represents the economic active power basepoint, for units that are not dispatchable, this value represents the fixed generation value. The value must be between the operating low and high limits. 
        self.baseP = baseP

        #: The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity 
        self.ratedNetMaxP = ratedNetMaxP

        #: Maximum high economic active power limit, that should not exceed the maximum operating active power limit 
        self.maxEconomicP = maxEconomicP

        #: Unit response rate which specifies the active power change for a control pulse of one second in the most responsive loading level of the unit. 
        self.controlResponseRate = controlResponseRate

 
        self.stepChange = stepChange

 
        self.energyMinP = energyMinP

        #: The initial startup cost incurred for each start of the GeneratingUnit. 
        self.startupCost = startupCost

        #: Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency. 
        self.governorSCD = governorSCD

        #: Pulse high limit which is the largest control pulse that the unit can respond to 
        self.controlPulseHigh = controlPulseHigh

        self._OperatedBy_GenerationProvider = None
        self.OperatedBy_GenerationProvider = OperatedBy_GenerationProvider

        self._ControlAreaGeneratingUnit = []
        self.ControlAreaGeneratingUnit = [] if ControlAreaGeneratingUnit is None else ControlAreaGeneratingUnit

        self._GenUnitOpCostCurves = []
        self.GenUnitOpCostCurves = [] if GenUnitOpCostCurves is None else GenUnitOpCostCurves

        self._SubControlArea = None
        self.SubControlArea = SubControlArea

        self._RegisteredGenerator = None
        self.RegisteredGenerator = RegisteredGenerator

        self._SynchronousMachines = []
        self.SynchronousMachines = [] if SynchronousMachines is None else SynchronousMachines

        self._GenUnitOpSchedule = None
        self.GenUnitOpSchedule = GenUnitOpSchedule

        self._GrossToNetActivePowerCurves = []
        self.GrossToNetActivePowerCurves = [] if GrossToNetActivePowerCurves is None else GrossToNetActivePowerCurves

        super(GeneratingUnit, self).__init__(*args, **kw_args)

    def getOperatedBy_GenerationProvider(self):
        """A GenerationProvider operates one or more GeneratingUnits.
        """
        return self._OperatedBy_GenerationProvider

    def setOperatedBy_GenerationProvider(self, value):
        if self._OperatedBy_GenerationProvider is not None:
            filtered = [x for x in self.OperatedBy_GenerationProvider.GeneratingUnits if x != self]
            self._OperatedBy_GenerationProvider._GeneratingUnits = filtered

        self._OperatedBy_GenerationProvider = value
        if self._OperatedBy_GenerationProvider is not None:
            self._OperatedBy_GenerationProvider._GeneratingUnits.append(self)

    OperatedBy_GenerationProvider = property(getOperatedBy_GenerationProvider, setOperatedBy_GenerationProvider)

    def getControlAreaGeneratingUnit(self):
        """ControlArea specifications for this generating unit.
        """
        return self._ControlAreaGeneratingUnit

    def setControlAreaGeneratingUnit(self, value):
        for x in self._ControlAreaGeneratingUnit:
            x._GeneratingUnit = None
        for y in value:
            y._GeneratingUnit = self
        self._ControlAreaGeneratingUnit = value

    ControlAreaGeneratingUnit = property(getControlAreaGeneratingUnit, setControlAreaGeneratingUnit)

    def addControlAreaGeneratingUnit(self, *ControlAreaGeneratingUnit):
        for obj in ControlAreaGeneratingUnit:
            obj._GeneratingUnit = self
            self._ControlAreaGeneratingUnit.append(obj)

    def removeControlAreaGeneratingUnit(self, *ControlAreaGeneratingUnit):
        for obj in ControlAreaGeneratingUnit:
            obj._GeneratingUnit = None
            self._ControlAreaGeneratingUnit.remove(obj)

    def getGenUnitOpCostCurves(self):
        """A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.
        """
        return self._GenUnitOpCostCurves

    def setGenUnitOpCostCurves(self, value):
        for x in self._GenUnitOpCostCurves:
            x._GeneratingUnit = None
        for y in value:
            y._GeneratingUnit = self
        self._GenUnitOpCostCurves = value

    GenUnitOpCostCurves = property(getGenUnitOpCostCurves, setGenUnitOpCostCurves)

    def addGenUnitOpCostCurves(self, *GenUnitOpCostCurves):
        for obj in GenUnitOpCostCurves:
            obj._GeneratingUnit = self
            self._GenUnitOpCostCurves.append(obj)

    def removeGenUnitOpCostCurves(self, *GenUnitOpCostCurves):
        for obj in GenUnitOpCostCurves:
            obj._GeneratingUnit = None
            self._GenUnitOpCostCurves.remove(obj)

    def getSubControlArea(self):
        """A GeneratingUnit injects energy into a SubControlArea.
        """
        return self._SubControlArea

    def setSubControlArea(self, value):
        if self._SubControlArea is not None:
            filtered = [x for x in self.SubControlArea.GeneratingUnits if x != self]
            self._SubControlArea._GeneratingUnits = filtered

        self._SubControlArea = value
        if self._SubControlArea is not None:
            self._SubControlArea._GeneratingUnits.append(self)

    SubControlArea = property(getSubControlArea, setSubControlArea)

    def getRegisteredGenerator(self):
        
        return self._RegisteredGenerator

    def setRegisteredGenerator(self, value):
        if self._RegisteredGenerator is not None:
            self._RegisteredGenerator._GeneratingUnit = None

        self._RegisteredGenerator = value
        if self._RegisteredGenerator is not None:
            self._RegisteredGenerator._GeneratingUnit = self

    RegisteredGenerator = property(getRegisteredGenerator, setRegisteredGenerator)

    def getSynchronousMachines(self):
        """A synchronous machine may operate as a generator and as such becomes a member of a generating unit
        """
        return self._SynchronousMachines

    def setSynchronousMachines(self, value):
        for x in self._SynchronousMachines:
            x._GeneratingUnit = None
        for y in value:
            y._GeneratingUnit = self
        self._SynchronousMachines = value

    SynchronousMachines = property(getSynchronousMachines, setSynchronousMachines)

    def addSynchronousMachines(self, *SynchronousMachines):
        for obj in SynchronousMachines:
            obj._GeneratingUnit = self
            self._SynchronousMachines.append(obj)

    def removeSynchronousMachines(self, *SynchronousMachines):
        for obj in SynchronousMachines:
            obj._GeneratingUnit = None
            self._SynchronousMachines.remove(obj)

    def getGenUnitOpSchedule(self):
        """A generating unit may have an operating schedule, indicating the planned operation of the unit
        """
        return self._GenUnitOpSchedule

    def setGenUnitOpSchedule(self, value):
        if self._GenUnitOpSchedule is not None:
            self._GenUnitOpSchedule._GeneratingUnit = None

        self._GenUnitOpSchedule = value
        if self._GenUnitOpSchedule is not None:
            self._GenUnitOpSchedule._GeneratingUnit = self

    GenUnitOpSchedule = property(getGenUnitOpSchedule, setGenUnitOpSchedule)

    def getGrossToNetActivePowerCurves(self):
        """A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
        """
        return self._GrossToNetActivePowerCurves

    def setGrossToNetActivePowerCurves(self, value):
        for x in self._GrossToNetActivePowerCurves:
            x._GeneratingUnit = None
        for y in value:
            y._GeneratingUnit = self
        self._GrossToNetActivePowerCurves = value

    GrossToNetActivePowerCurves = property(getGrossToNetActivePowerCurves, setGrossToNetActivePowerCurves)

    def addGrossToNetActivePowerCurves(self, *GrossToNetActivePowerCurves):
        for obj in GrossToNetActivePowerCurves:
            obj._GeneratingUnit = self
            self._GrossToNetActivePowerCurves.append(obj)

    def removeGrossToNetActivePowerCurves(self, *GrossToNetActivePowerCurves):
        for obj in GrossToNetActivePowerCurves:
            obj._GeneratingUnit = None
            self._GrossToNetActivePowerCurves.remove(obj)

