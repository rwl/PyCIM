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

from CIM14v13.IEC61970.Wires.RegulatingCondEq import RegulatingCondEq

class SynchronousMachine(RegulatingCondEq):
    """An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.
    """

    def __init__(self, type='generator', coolantType='air', operatingMode='condenser', x2=0.0, x0=0.0, qPercent=0.0, damping=0.0, manualToAVR=0.0, x=0.0, minQ=0.0, xQuadSync=0.0, xQuadSubtrans=0.0, r2=0.0, inertia=0.0, r=0.0, xDirectSync=0.0, xQuadTrans=0.0, xDirectTrans=0.0, referencePriority=0, r0=0.0, minU=0.0, maxQ=0.0, condenserP=0.0, baseQ=0.0, xDirectSubtrans=0.0, ratedS=0.0, maxU=0.0, aVRToManualLead=0.0, aVRToManualLag=0.0, coolantCondition=0.0, ReactiveCapabilityCurves=None, HydroPump=None, PrimeMovers=None, GeneratingUnit=None, InitialReactiveCapabilityCurve=None, **kw_args):
        """Initializes a new 'SynchronousMachine' instance.

        @param type: Modes that this synchronous machine can operate in. Values are: "generator", "generator_or_condenser", "condenser"
        @param coolantType: Method of cooling the machine. Values are: "air", "hydrogenGas", "water"
        @param operatingMode: Current mode of operation. Values are: "condenser", "generator"
        @param x2: Negative sequence reactance. 
        @param x0: Zero sequence reactance of the synchronous machine. 
        @param qPercent: Percent of the coordinated reactive control that comes from this machine. 
        @param damping: Damping torque coefficient, a proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque. 
        @param manualToAVR: Time delay required when switching from Manual to Automatic Voltage Regulation. This value is used in the accelerating power reference frame for powerflow solutions 
        @param x: Positive sequence reactance of the synchronous machine. 
        @param minQ: Minimum reactive power limit for the unit. 
        @param xQuadSync: Quadrature-axis synchronous reactance (Xq) , the ratio of the component of reactive armature voltage, due to the quadrature-axis component of armature current, to this component of current, under steady state conditions and at rated frequency. 
        @param xQuadSubtrans: Quadrature-axis subtransient reactance, also known as X'q. 
        @param r2: Negative sequence resistance. 
        @param inertia: The energy stored in the rotor when operating at rated speed. This value is used in the accelerating power reference frame for  operator training simulator solutions. 
        @param r: Positive sequence resistance of the synchronous machine. 
        @param xDirectSync: Direct-axis synchronous reactance. The quotient of a sustained value of that AC component of armature voltage that is produced by the total direct-axis flux due to direct-axis armature current and the value of the AC component of this current, the machine running at rated speed. (Xd) 
        @param xQuadTrans: Quadrature-axis transient reactance, also known as X'q. 
        @param xDirectTrans: Direct-axis transient reactance, also known as X'd. 
        @param referencePriority: Priority of unit for reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on. 
        @param r0: Zero sequence resistance of the synchronous machine. 
        @param minU: Minimum voltage  limit for the unit. 
        @param maxQ: Maximum reactive power limit. This is the maximum (nameplate) limit for the unit. 
        @param condenserP: Active power consumed when in condenser mode operation. 
        @param baseQ: Default base reactive power value. This value represents the initial reactive power that can be used by any application function. 
        @param xDirectSubtrans: Direct-axis subtransient reactance, also known as X'd. 
        @param ratedS: Nameplate apparent power rating for the unit 
        @param maxU: Maximum voltage limit for the unit. 
        @param aVRToManualLead: Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a leading MVAr violation. 
        @param aVRToManualLag: Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a lagging MVAr violation. 
        @param coolantCondition: Temperature or pressure of coolant medium 
        @param ReactiveCapabilityCurves: All available Reactive capability curves for this SynchronousMachine.
        @param HydroPump: The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
        @param PrimeMovers: Prime movers that drive this SynchronousMachine.
        @param GeneratingUnit: A synchronous machine may operate as a generator and as such becomes a member of a generating unit
        @param InitialReactiveCapabilityCurve: The default ReactiveCapabilityCurve for use by a SynchronousMachine
        """
        #: Modes that this synchronous machine can operate in.Values are: "generator", "generator_or_condenser", "condenser"
        self.type = type

        #: Method of cooling the machine.Values are: "air", "hydrogenGas", "water"
        self.coolantType = coolantType

        #: Current mode of operation.Values are: "condenser", "generator"
        self.operatingMode = operatingMode

        #: Negative sequence reactance.
        self.x2 = x2

        #: Zero sequence reactance of the synchronous machine.
        self.x0 = x0

        #: Percent of the coordinated reactive control that comes from this machine.
        self.qPercent = qPercent

        #: Damping torque coefficient, a proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.
        self.damping = damping

        #: Time delay required when switching from Manual to Automatic Voltage Regulation. This value is used in the accelerating power reference frame for powerflow solutions
        self.manualToAVR = manualToAVR

        #: Positive sequence reactance of the synchronous machine.
        self.x = x

        #: Minimum reactive power limit for the unit.
        self.minQ = minQ

        #: Quadrature-axis synchronous reactance (Xq) , the ratio of the component of reactive armature voltage, due to the quadrature-axis component of armature current, to this component of current, under steady state conditions and at rated frequency.
        self.xQuadSync = xQuadSync

        #: Quadrature-axis subtransient reactance, also known as X'q.
        self.xQuadSubtrans = xQuadSubtrans

        #: Negative sequence resistance.
        self.r2 = r2

        #: The energy stored in the rotor when operating at rated speed. This value is used in the accelerating power reference frame for  operator training simulator solutions.
        self.inertia = inertia

        #: Positive sequence resistance of the synchronous machine.
        self.r = r

        #: Direct-axis synchronous reactance. The quotient of a sustained value of that AC component of armature voltage that is produced by the total direct-axis flux due to direct-axis armature current and the value of the AC component of this current, the machine running at rated speed. (Xd)
        self.xDirectSync = xDirectSync

        #: Quadrature-axis transient reactance, also known as X'q.
        self.xQuadTrans = xQuadTrans

        #: Direct-axis transient reactance, also known as X'd.
        self.xDirectTrans = xDirectTrans

        #: Priority of unit for reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on.
        self.referencePriority = referencePriority

        #: Zero sequence resistance of the synchronous machine.
        self.r0 = r0

        #: Minimum voltage  limit for the unit.
        self.minU = minU

        #: Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.
        self.maxQ = maxQ

        #: Active power consumed when in condenser mode operation.
        self.condenserP = condenserP

        #: Default base reactive power value. This value represents the initial reactive power that can be used by any application function.
        self.baseQ = baseQ

        #: Direct-axis subtransient reactance, also known as X'd.
        self.xDirectSubtrans = xDirectSubtrans

        #: Nameplate apparent power rating for the unit
        self.ratedS = ratedS

        #: Maximum voltage limit for the unit.
        self.maxU = maxU

        #: Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a leading MVAr violation.
        self.aVRToManualLead = aVRToManualLead

        #: Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a lagging MVAr violation.
        self.aVRToManualLag = aVRToManualLag

        #: Temperature or pressure of coolant medium
        self.coolantCondition = coolantCondition

        self._ReactiveCapabilityCurves = []
        self.ReactiveCapabilityCurves = [] if ReactiveCapabilityCurves is None else ReactiveCapabilityCurves

        self._HydroPump = None
        self.HydroPump = HydroPump

        self._PrimeMovers = []
        self.PrimeMovers = [] if PrimeMovers is None else PrimeMovers

        self._GeneratingUnit = None
        self.GeneratingUnit = GeneratingUnit

        self._InitialReactiveCapabilityCurve = None
        self.InitialReactiveCapabilityCurve = InitialReactiveCapabilityCurve

        super(SynchronousMachine, self).__init__(**kw_args)

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
            self._HydroPump._SynchronousMachine = self

    HydroPump = property(getHydroPump, setHydroPump)

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
            self._GeneratingUnit._SynchronousMachines.append(self)

    GeneratingUnit = property(getGeneratingUnit, setGeneratingUnit)

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
            self._InitialReactiveCapabilityCurve._InitiallyUsedBySynchronousMachines.append(self)

    InitialReactiveCapabilityCurve = property(getInitialReactiveCapabilityCurve, setInitialReactiveCapabilityCurve)

