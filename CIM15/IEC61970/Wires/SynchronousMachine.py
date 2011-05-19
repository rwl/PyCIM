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

from CIM15.IEC61970.Wires.RegulatingCondEq import RegulatingCondEq

class SynchronousMachine(RegulatingCondEq):
    """An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.
    """

    def __init__(self, ratedS=0.0, r2=0.0, r0=0.0, manualToAVR=0.0, qPercent=0.0, coolantCondition=0.0, condenserP=0.0, xQuadTrans=0.0, xQuadSubtrans=0.0, xQuadSync=0.0, xDirectSync=0.0, minQ=0.0, aVRToManualLag=0.0, damping=0.0, operatingMode="condenser", xDirectSubtrans=0.0, coolantType="air", aVRToManualLead=0.0, minU=0.0, maxQ=0.0, referencePriority=0, maxU=0.0, xDirectTrans=0.0, inertia=0.0, baseQ=0.0, type="condenser", r=0.0, x0=0.0, x2=0.0, x=0.0, PrimeMovers=None, GeneratingUnit=None, ReactiveCapabilityCurves=None, HydroPump=None, InitialReactiveCapabilityCurve=None, *args, **kw_args):
        """Initialises a new 'SynchronousMachine' instance.

        @param ratedS: Nameplate apparent power rating for the unit 
        @param r2: Negative sequence resistance. 
        @param r0: Zero sequence resistance of the synchronous machine. 
        @param manualToAVR: Time delay required when switching from Manual to Automatic Voltage Regulation. This value is used in the accelerating power reference frame for powerflow solutions 
        @param qPercent: Percent of the coordinated reactive control that comes from this machine. 
        @param coolantCondition: Temperature or pressure of coolant medium 
        @param condenserP: Active power consumed when in condenser mode operation. 
        @param xQuadTrans: Quadrature-axis transient reactance, also known as X'q. 
        @param xQuadSubtrans: Quadrature-axis subtransient reactance, also known as X'q. 
        @param xQuadSync: Quadrature-axis synchronous reactance (Xq) , the ratio of the component of reactive armature voltage, due to the quadrature-axis component of armature current, to this component of current, under steady state conditions and at rated frequency. 
        @param xDirectSync: Direct-axis synchronous reactance. The quotient of a sustained value of that AC component of armature voltage that is produced by the total direct-axis flux due to direct-axis armature current and the value of the AC component of this current, the machine running at rated speed. (Xd) 
        @param minQ: Minimum reactive power limit for the unit. 
        @param aVRToManualLag: Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a lagging MVAr violation. 
        @param damping: Damping torque coefficient, a proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque. 
        @param operatingMode: Current mode of operation. Values are: "condenser", "generator"
        @param xDirectSubtrans: Direct-axis subtransient reactance, also known as X'd. 
        @param coolantType: Method of cooling the machine. Values are: "air", "hydrogenGas", "water"
        @param aVRToManualLead: Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a leading MVAr violation. 
        @param minU: Minimum voltage  limit for the unit. 
        @param maxQ: Maximum reactive power limit. This is the maximum (nameplate) limit for the unit. 
        @param referencePriority: Priority of unit for reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on. 
        @param maxU: Maximum voltage limit for the unit. 
        @param xDirectTrans: Direct-axis transient reactance, also known as X'd. 
        @param inertia: The energy stored in the rotor when operating at rated speed. This value is used in the accelerating power reference frame for  operator training simulator solutions. 
        @param baseQ: Default base reactive power value. This value represents the initial reactive power that can be used by any application function. 
        @param type: Modes that this synchronous machine can operate in. Values are: "condenser", "generator_or_condenser", "generator"
        @param r: Positive sequence resistance of the synchronous machine. 
        @param x0: Zero sequence reactance of the synchronous machine. 
        @param x2: Negative sequence reactance. 
        @param x: Positive sequence reactance of the synchronous machine. 
        @param PrimeMovers: Prime movers that drive this SynchronousMachine.
        @param GeneratingUnit: A synchronous machine may operate as a generator and as such becomes a member of a generating unit
        @param ReactiveCapabilityCurves: All available Reactive capability curves for this SynchronousMachine.
        @param HydroPump: The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
        @param InitialReactiveCapabilityCurve: The default ReactiveCapabilityCurve for use by a SynchronousMachine
        """
        #: Nameplate apparent power rating for the unit
        self.ratedS = ratedS

        #: Negative sequence resistance.
        self.r2 = r2

        #: Zero sequence resistance of the synchronous machine.
        self.r0 = r0

        #: Time delay required when switching from Manual to Automatic Voltage Regulation. This value is used in the accelerating power reference frame for powerflow solutions
        self.manualToAVR = manualToAVR

        #: Percent of the coordinated reactive control that comes from this machine.
        self.qPercent = qPercent

        #: Temperature or pressure of coolant medium
        self.coolantCondition = coolantCondition

        #: Active power consumed when in condenser mode operation.
        self.condenserP = condenserP

        #: Quadrature-axis transient reactance, also known as X'q.
        self.xQuadTrans = xQuadTrans

        #: Quadrature-axis subtransient reactance, also known as X'q.
        self.xQuadSubtrans = xQuadSubtrans

        #: Quadrature-axis synchronous reactance (Xq) , the ratio of the component of reactive armature voltage, due to the quadrature-axis component of armature current, to this component of current, under steady state conditions and at rated frequency.
        self.xQuadSync = xQuadSync

        #: Direct-axis synchronous reactance. The quotient of a sustained value of that AC component of armature voltage that is produced by the total direct-axis flux due to direct-axis armature current and the value of the AC component of this current, the machine running at rated speed. (Xd)
        self.xDirectSync = xDirectSync

        #: Minimum reactive power limit for the unit.
        self.minQ = minQ

        #: Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a lagging MVAr violation.
        self.aVRToManualLag = aVRToManualLag

        #: Damping torque coefficient, a proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.
        self.damping = damping

        #: Current mode of operation. Values are: "condenser", "generator"
        self.operatingMode = operatingMode

        #: Direct-axis subtransient reactance, also known as X'd.
        self.xDirectSubtrans = xDirectSubtrans

        #: Method of cooling the machine. Values are: "air", "hydrogenGas", "water"
        self.coolantType = coolantType

        #: Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a leading MVAr violation.
        self.aVRToManualLead = aVRToManualLead

        #: Minimum voltage  limit for the unit.
        self.minU = minU

        #: Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.
        self.maxQ = maxQ

        #: Priority of unit for reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on.
        self.referencePriority = referencePriority

        #: Maximum voltage limit for the unit.
        self.maxU = maxU

        #: Direct-axis transient reactance, also known as X'd.
        self.xDirectTrans = xDirectTrans

        #: The energy stored in the rotor when operating at rated speed. This value is used in the accelerating power reference frame for  operator training simulator solutions.
        self.inertia = inertia

        #: Default base reactive power value. This value represents the initial reactive power that can be used by any application function.
        self.baseQ = baseQ

        #: Modes that this synchronous machine can operate in. Values are: "condenser", "generator_or_condenser", "generator"
        self.type = type

        #: Positive sequence resistance of the synchronous machine.
        self.r = r

        #: Zero sequence reactance of the synchronous machine.
        self.x0 = x0

        #: Negative sequence reactance.
        self.x2 = x2

        #: Positive sequence reactance of the synchronous machine.
        self.x = x

        self._PrimeMovers = []
        self.PrimeMovers = [] if PrimeMovers is None else PrimeMovers

        self._GeneratingUnit = None
        self.GeneratingUnit = GeneratingUnit

        self._ReactiveCapabilityCurves = []
        self.ReactiveCapabilityCurves = [] if ReactiveCapabilityCurves is None else ReactiveCapabilityCurves

        self._HydroPump = None
        self.HydroPump = HydroPump

        self._InitialReactiveCapabilityCurve = None
        self.InitialReactiveCapabilityCurve = InitialReactiveCapabilityCurve

        super(SynchronousMachine, self).__init__(*args, **kw_args)

    _attrs = ["ratedS", "r2", "r0", "manualToAVR", "qPercent", "coolantCondition", "condenserP", "xQuadTrans", "xQuadSubtrans", "xQuadSync", "xDirectSync", "minQ", "aVRToManualLag", "damping", "operatingMode", "xDirectSubtrans", "coolantType", "aVRToManualLead", "minU", "maxQ", "referencePriority", "maxU", "xDirectTrans", "inertia", "baseQ", "type", "r", "x0", "x2", "x"]
    _attr_types = {"ratedS": float, "r2": float, "r0": float, "manualToAVR": float, "qPercent": float, "coolantCondition": float, "condenserP": float, "xQuadTrans": float, "xQuadSubtrans": float, "xQuadSync": float, "xDirectSync": float, "minQ": float, "aVRToManualLag": float, "damping": float, "operatingMode": str, "xDirectSubtrans": float, "coolantType": str, "aVRToManualLead": float, "minU": float, "maxQ": float, "referencePriority": int, "maxU": float, "xDirectTrans": float, "inertia": float, "baseQ": float, "type": str, "r": float, "x0": float, "x2": float, "x": float}
    _defaults = {"ratedS": 0.0, "r2": 0.0, "r0": 0.0, "manualToAVR": 0.0, "qPercent": 0.0, "coolantCondition": 0.0, "condenserP": 0.0, "xQuadTrans": 0.0, "xQuadSubtrans": 0.0, "xQuadSync": 0.0, "xDirectSync": 0.0, "minQ": 0.0, "aVRToManualLag": 0.0, "damping": 0.0, "operatingMode": "condenser", "xDirectSubtrans": 0.0, "coolantType": "air", "aVRToManualLead": 0.0, "minU": 0.0, "maxQ": 0.0, "referencePriority": 0, "maxU": 0.0, "xDirectTrans": 0.0, "inertia": 0.0, "baseQ": 0.0, "type": "condenser", "r": 0.0, "x0": 0.0, "x2": 0.0, "x": 0.0}
    _enums = {"operatingMode": "SynchronousMachineOperatingMode", "coolantType": "CoolantType", "type": "SynchronousMachineType"}
    _refs = ["PrimeMovers", "GeneratingUnit", "ReactiveCapabilityCurves", "HydroPump", "InitialReactiveCapabilityCurve"]
    _many_refs = ["PrimeMovers", "ReactiveCapabilityCurves"]

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

