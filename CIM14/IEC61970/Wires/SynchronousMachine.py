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

from CIM14.IEC61970.Dynamics.RotatingMachine import RotatingMachine

class SynchronousMachine(RotatingMachine):
    """An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.
    """

    def __init__(self, operatingMode="condenser", type="generator_or_condenser", coolantType="air", xQuadTrans=0.0, condenserP=0.0, referencePriority=0, damping=0.0, x0=0.0, r2=0.0, minQ=0.0, xDirectSync=0.0, maxQ=0.0, r0=0.0, aVRToManualLead=0.0, x=0.0, inertia=0.0, coolantCondition=0.0, manualToAVR=0.0, r=0.0, maxU=0.0, xQuadSync=0.0, qPercent=0.0, xQuadSubtrans=0.0, minU=0.0, aVRToManualLag=0.0, baseQ=0.0, xDirectTrans=0.0, x2=0.0, xDirectSubtrans=0.0, genLoad0=None, HydroPump=None, GeneratingUnit=None, govHydro10=None, PrimeMovers=None, InitialReactiveCapabilityCurve=None, genEquiv0=None, ReactiveCapabilityCurves=None, *args, **kw_args):
        """Initialises a new 'SynchronousMachine' instance.

        @param operatingMode: Current mode of operation. Values are: "condenser", "generator"
        @param type: Modes that this synchronous machine can operate in. Values are: "generator_or_condenser", "generator", "condenser"
        @param coolantType: Method of cooling the machine. Values are: "air", "hydrogenGas", "water"
        @param xQuadTrans: Quadrature-axis transient reactance, also known as X'q. 
        @param condenserP: Active power consumed when in condenser mode operation. 
        @param referencePriority: Priority of unit for reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on. 
        @param damping: Damping torque coefficient, a proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque. 
        @param x0: Zero sequence reactance of the synchronous machine. 
        @param r2: Negative sequence resistance. 
        @param minQ: Minimum reactive power limit for the unit. 
        @param xDirectSync: Direct-axis synchronous reactance. The quotient of a sustained value of that AC component of armature voltage that is produced by the total direct-axis flux due to direct-axis armature current and the value of the AC component of this current, the machine running at rated speed. (Xd) 
        @param maxQ: Maximum reactive power limit. This is the maximum (nameplate) limit for the unit. 
        @param r0: Zero sequence resistance of the synchronous machine. 
        @param aVRToManualLead: Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a leading MVAr violation. 
        @param x: Positive sequence reactance of the synchronous machine. 
        @param inertia: The energy stored in the rotor when operating at rated speed. This value is used in the accelerating power reference frame for  operator training simulator solutions. 
        @param coolantCondition: Temperature or pressure of coolant medium 
        @param manualToAVR: Time delay required when switching from Manual to Automatic Voltage Regulation. This value is used in the accelerating power reference frame for powerflow solutions 
        @param r: Positive sequence resistance of the synchronous machine. 
        @param maxU: Maximum voltage limit for the unit. 
        @param xQuadSync: Quadrature-axis synchronous reactance (Xq) , the ratio of the component of reactive armature voltage, due to the quadrature-axis component of armature current, to this component of current, under steady state conditions and at rated frequency. 
        @param qPercent: Percent of the coordinated reactive control that comes from this machine. 
        @param xQuadSubtrans: Quadrature-axis subtransient reactance, also known as X'q. 
        @param minU: Minimum voltage  limit for the unit. 
        @param aVRToManualLag: Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a lagging MVAr violation. 
        @param baseQ: Default base reactive power value. This value represents the initial reactive power that can be used by any application function. 
        @param xDirectTrans: Direct-axis transient reactance, also known as X'd. 
        @param x2: Negative sequence reactance. 
        @param xDirectSubtrans: Direct-axis subtransient reactance, also known as X'd. 
        @param genLoad0:
        @param HydroPump: The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
        @param GeneratingUnit: A synchronous machine may operate as a generator and as such becomes a member of a generating unit
        @param govHydro10:
        @param PrimeMovers: Prime movers that drive this SynchronousMachine.
        @param InitialReactiveCapabilityCurve: The default ReactiveCapabilityCurve for use by a SynchronousMachine
        @param genEquiv0:
        @param ReactiveCapabilityCurves: All available Reactive capability curves for this SynchronousMachine.
        """
        #: Current mode of operation. Values are: "condenser", "generator"
        self.operatingMode = operatingMode

        #: Modes that this synchronous machine can operate in. Values are: "generator_or_condenser", "generator", "condenser"
        self.type = type

        #: Method of cooling the machine. Values are: "air", "hydrogenGas", "water"
        self.coolantType = coolantType

        #: Quadrature-axis transient reactance, also known as X'q.
        self.xQuadTrans = xQuadTrans

        #: Active power consumed when in condenser mode operation.
        self.condenserP = condenserP

        #: Priority of unit for reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on.
        self.referencePriority = referencePriority

        #: Damping torque coefficient, a proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.
        self.damping = damping

        #: Zero sequence reactance of the synchronous machine.
        self.x0 = x0

        #: Negative sequence resistance.
        self.r2 = r2

        #: Minimum reactive power limit for the unit.
        self.minQ = minQ

        #: Direct-axis synchronous reactance. The quotient of a sustained value of that AC component of armature voltage that is produced by the total direct-axis flux due to direct-axis armature current and the value of the AC component of this current, the machine running at rated speed. (Xd)
        self.xDirectSync = xDirectSync

        #: Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.
        self.maxQ = maxQ

        #: Zero sequence resistance of the synchronous machine.
        self.r0 = r0

        #: Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a leading MVAr violation.
        self.aVRToManualLead = aVRToManualLead

        #: Positive sequence reactance of the synchronous machine.
        self.x = x

        #: The energy stored in the rotor when operating at rated speed. This value is used in the accelerating power reference frame for  operator training simulator solutions.
        self.inertia = inertia

        #: Temperature or pressure of coolant medium
        self.coolantCondition = coolantCondition

        #: Time delay required when switching from Manual to Automatic Voltage Regulation. This value is used in the accelerating power reference frame for powerflow solutions
        self.manualToAVR = manualToAVR

        #: Positive sequence resistance of the synchronous machine.
        self.r = r

        #: Maximum voltage limit for the unit.
        self.maxU = maxU

        #: Quadrature-axis synchronous reactance (Xq) , the ratio of the component of reactive armature voltage, due to the quadrature-axis component of armature current, to this component of current, under steady state conditions and at rated frequency.
        self.xQuadSync = xQuadSync

        #: Percent of the coordinated reactive control that comes from this machine.
        self.qPercent = qPercent

        #: Quadrature-axis subtransient reactance, also known as X'q.
        self.xQuadSubtrans = xQuadSubtrans

        #: Minimum voltage  limit for the unit.
        self.minU = minU

        #: Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a lagging MVAr violation.
        self.aVRToManualLag = aVRToManualLag

        #: Default base reactive power value. This value represents the initial reactive power that can be used by any application function.
        self.baseQ = baseQ

        #: Direct-axis transient reactance, also known as X'd.
        self.xDirectTrans = xDirectTrans

        #: Negative sequence reactance.
        self.x2 = x2

        #: Direct-axis subtransient reactance, also known as X'd.
        self.xDirectSubtrans = xDirectSubtrans

        self._genLoad0 = []
        self.genLoad0 = [] if genLoad0 is None else genLoad0

        self._HydroPump = None
        self.HydroPump = HydroPump

        self._GeneratingUnit = None
        self.GeneratingUnit = GeneratingUnit

        self._govHydro10 = []
        self.govHydro10 = [] if govHydro10 is None else govHydro10

        self._PrimeMovers = []
        self.PrimeMovers = [] if PrimeMovers is None else PrimeMovers

        self._InitialReactiveCapabilityCurve = None
        self.InitialReactiveCapabilityCurve = InitialReactiveCapabilityCurve

        self._genEquiv0 = []
        self.genEquiv0 = [] if genEquiv0 is None else genEquiv0

        self._ReactiveCapabilityCurves = []
        self.ReactiveCapabilityCurves = [] if ReactiveCapabilityCurves is None else ReactiveCapabilityCurves

        super(SynchronousMachine, self).__init__(*args, **kw_args)

    _attrs = ["operatingMode", "type", "coolantType", "xQuadTrans", "condenserP", "referencePriority", "damping", "x0", "r2", "minQ", "xDirectSync", "maxQ", "r0", "aVRToManualLead", "x", "inertia", "coolantCondition", "manualToAVR", "r", "maxU", "xQuadSync", "qPercent", "xQuadSubtrans", "minU", "aVRToManualLag", "baseQ", "xDirectTrans", "x2", "xDirectSubtrans"]
    _attr_types = {"operatingMode": str, "type": str, "coolantType": str, "xQuadTrans": float, "condenserP": float, "referencePriority": int, "damping": float, "x0": float, "r2": float, "minQ": float, "xDirectSync": float, "maxQ": float, "r0": float, "aVRToManualLead": float, "x": float, "inertia": float, "coolantCondition": float, "manualToAVR": float, "r": float, "maxU": float, "xQuadSync": float, "qPercent": float, "xQuadSubtrans": float, "minU": float, "aVRToManualLag": float, "baseQ": float, "xDirectTrans": float, "x2": float, "xDirectSubtrans": float}
    _defaults = {"operatingMode": "condenser", "type": "generator_or_condenser", "coolantType": "air", "xQuadTrans": 0.0, "condenserP": 0.0, "referencePriority": 0, "damping": 0.0, "x0": 0.0, "r2": 0.0, "minQ": 0.0, "xDirectSync": 0.0, "maxQ": 0.0, "r0": 0.0, "aVRToManualLead": 0.0, "x": 0.0, "inertia": 0.0, "coolantCondition": 0.0, "manualToAVR": 0.0, "r": 0.0, "maxU": 0.0, "xQuadSync": 0.0, "qPercent": 0.0, "xQuadSubtrans": 0.0, "minU": 0.0, "aVRToManualLag": 0.0, "baseQ": 0.0, "xDirectTrans": 0.0, "x2": 0.0, "xDirectSubtrans": 0.0}
    _enums = {"operatingMode": "SynchronousMachineOperatingMode", "type": "SynchronousMachineType", "coolantType": "CoolantType"}
    _refs = ["genLoad0", "HydroPump", "GeneratingUnit", "govHydro10", "PrimeMovers", "InitialReactiveCapabilityCurve", "genEquiv0", "ReactiveCapabilityCurves"]
    _many_refs = ["genLoad0", "govHydro10", "PrimeMovers", "genEquiv0", "ReactiveCapabilityCurves"]

    def getgenLoad0(self):
        
        return self._genLoad0

    def setgenLoad0(self, value):
        for p in self._genLoad0:
            filtered = [q for q in p.synchronousMachine0 if q != self]
            self._genLoad0._synchronousMachine0 = filtered
        for r in value:
            if self not in r._synchronousMachine0:
                r._synchronousMachine0.append(self)
        self._genLoad0 = value

    genLoad0 = property(getgenLoad0, setgenLoad0)

    def addgenLoad0(self, *genLoad0):
        for obj in genLoad0:
            if self not in obj._synchronousMachine0:
                obj._synchronousMachine0.append(self)
            self._genLoad0.append(obj)

    def removegenLoad0(self, *genLoad0):
        for obj in genLoad0:
            if self in obj._synchronousMachine0:
                obj._synchronousMachine0.remove(self)
            self._genLoad0.remove(obj)

    def getHydroPump(self):
        """The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
        """
        return self._HydroPump

    def setHydroPump(self, value):
        if self._HydroPump is not None:
            self._HydroPump._SynchronousMachine = None

        self._HydroPump = value
        if self._HydroPump is not None:
            self._HydroPump.SynchronousMachine = None
            self._HydroPump._SynchronousMachine = self

    HydroPump = property(getHydroPump, setHydroPump)

    def getGeneratingUnit(self):
        """A synchronous machine may operate as a generator and as such becomes a member of a generating unit
        """
        return self._GeneratingUnit

    def setGeneratingUnit(self, value):
        if self._GeneratingUnit is not None:
            filtered = [x for x in self.GeneratingUnit.SynchronousMachines if x != self]
            self._GeneratingUnit._SynchronousMachines = filtered

        self._GeneratingUnit = value
        if self._GeneratingUnit is not None:
            if self not in self._GeneratingUnit._SynchronousMachines:
                self._GeneratingUnit._SynchronousMachines.append(self)

    GeneratingUnit = property(getGeneratingUnit, setGeneratingUnit)

    def getgovHydro10(self):
        
        return self._govHydro10

    def setgovHydro10(self, value):
        for p in self._govHydro10:
            filtered = [q for q in p.synchronousMachine0 if q != self]
            self._govHydro10._synchronousMachine0 = filtered
        for r in value:
            if self not in r._synchronousMachine0:
                r._synchronousMachine0.append(self)
        self._govHydro10 = value

    govHydro10 = property(getgovHydro10, setgovHydro10)

    def addgovHydro10(self, *govHydro10):
        for obj in govHydro10:
            if self not in obj._synchronousMachine0:
                obj._synchronousMachine0.append(self)
            self._govHydro10.append(obj)

    def removegovHydro10(self, *govHydro10):
        for obj in govHydro10:
            if self in obj._synchronousMachine0:
                obj._synchronousMachine0.remove(self)
            self._govHydro10.remove(obj)

    def getPrimeMovers(self):
        """Prime movers that drive this SynchronousMachine.
        """
        return self._PrimeMovers

    def setPrimeMovers(self, value):
        for p in self._PrimeMovers:
            filtered = [q for q in p.SynchronousMachines if q != self]
            self._PrimeMovers._SynchronousMachines = filtered
        for r in value:
            if self not in r._SynchronousMachines:
                r._SynchronousMachines.append(self)
        self._PrimeMovers = value

    PrimeMovers = property(getPrimeMovers, setPrimeMovers)

    def addPrimeMovers(self, *PrimeMovers):
        for obj in PrimeMovers:
            if self not in obj._SynchronousMachines:
                obj._SynchronousMachines.append(self)
            self._PrimeMovers.append(obj)

    def removePrimeMovers(self, *PrimeMovers):
        for obj in PrimeMovers:
            if self in obj._SynchronousMachines:
                obj._SynchronousMachines.remove(self)
            self._PrimeMovers.remove(obj)

    def getInitialReactiveCapabilityCurve(self):
        """The default ReactiveCapabilityCurve for use by a SynchronousMachine
        """
        return self._InitialReactiveCapabilityCurve

    def setInitialReactiveCapabilityCurve(self, value):
        if self._InitialReactiveCapabilityCurve is not None:
            filtered = [x for x in self.InitialReactiveCapabilityCurve.InitiallyUsedBySynchronousMachines if x != self]
            self._InitialReactiveCapabilityCurve._InitiallyUsedBySynchronousMachines = filtered

        self._InitialReactiveCapabilityCurve = value
        if self._InitialReactiveCapabilityCurve is not None:
            if self not in self._InitialReactiveCapabilityCurve._InitiallyUsedBySynchronousMachines:
                self._InitialReactiveCapabilityCurve._InitiallyUsedBySynchronousMachines.append(self)

    InitialReactiveCapabilityCurve = property(getInitialReactiveCapabilityCurve, setInitialReactiveCapabilityCurve)

    def getgenEquiv0(self):
        
        return self._genEquiv0

    def setgenEquiv0(self, value):
        for p in self._genEquiv0:
            filtered = [q for q in p.synchronousMachine0 if q != self]
            self._genEquiv0._synchronousMachine0 = filtered
        for r in value:
            if self not in r._synchronousMachine0:
                r._synchronousMachine0.append(self)
        self._genEquiv0 = value

    genEquiv0 = property(getgenEquiv0, setgenEquiv0)

    def addgenEquiv0(self, *genEquiv0):
        for obj in genEquiv0:
            if self not in obj._synchronousMachine0:
                obj._synchronousMachine0.append(self)
            self._genEquiv0.append(obj)

    def removegenEquiv0(self, *genEquiv0):
        for obj in genEquiv0:
            if self in obj._synchronousMachine0:
                obj._synchronousMachine0.remove(self)
            self._genEquiv0.remove(obj)

    def getReactiveCapabilityCurves(self):
        """All available Reactive capability curves for this SynchronousMachine.
        """
        return self._ReactiveCapabilityCurves

    def setReactiveCapabilityCurves(self, value):
        for p in self._ReactiveCapabilityCurves:
            filtered = [q for q in p.SynchronousMachines if q != self]
            self._ReactiveCapabilityCurves._SynchronousMachines = filtered
        for r in value:
            if self not in r._SynchronousMachines:
                r._SynchronousMachines.append(self)
        self._ReactiveCapabilityCurves = value

    ReactiveCapabilityCurves = property(getReactiveCapabilityCurves, setReactiveCapabilityCurves)

    def addReactiveCapabilityCurves(self, *ReactiveCapabilityCurves):
        for obj in ReactiveCapabilityCurves:
            if self not in obj._SynchronousMachines:
                obj._SynchronousMachines.append(self)
            self._ReactiveCapabilityCurves.append(obj)

    def removeReactiveCapabilityCurves(self, *ReactiveCapabilityCurves):
        for obj in ReactiveCapabilityCurves:
            if self in obj._SynchronousMachines:
                obj._SynchronousMachines.remove(self)
            self._ReactiveCapabilityCurves.remove(obj)

