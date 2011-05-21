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

from CIM14.ENTSOE.Equipment.Wires.RegulatingCondEq import RegulatingCondEq

class SynchronousMachine(RegulatingCondEq):
    """An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.-  [R7.2] and [R9.3] are satisfied by navigation to ConnectivityNode and Substation. -  If a SynchronousMachine is not associated with a ReactiveCapabilityCurve, then the minQ and maxQ attributes will be used.   -  If a ReactiveCapabilityCurve is supplied, then the minQ and maxQ attributes are not required. -  If a synchronous condenser is being modeled so that there is no capability for real power output, the SynchronousMachine is not required to be associated with a GeneratingUnit.  In this case, the type and operatingMode attributes must both be set to “condenser”. -  Attributes qPercent, r, r0, r2, x, x0, x2, ratedS and referencePriority are not required.  SynchronousMachine.GeneratingUnit is required for this profile - need to change UML to reflect this.
    """

    def __init__(self, x0=0.0, qPercent=0.0, x2=0.0, r=0.0, referencePriority=0, operatingMode="condenser", r0=0.0, type="condenser", r2=0.0, maxQ=0.0, x=0.0, ratedS=0.0, minQ=0.0, InitialReactiveCapabilityCurve=None, HydroPump=None, GeneratingUnit=None, *args, **kw_args):
        """Initialises a new 'SynchronousMachine' instance.

        @param x0: Zero sequence reactance of the synchronous machine. 
        @param qPercent: Percent of the coordinated reactive control that comes from this machine. 
        @param x2: Negative sequence reactance. 
        @param r: Positive sequence resistance of the synchronous machine. 
        @param referencePriority: Priority of unit for reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on. 
        @param operatingMode: Current mode of operation. Values are: "condenser", "generator"
        @param r0: Zero sequence resistance of the synchronous machine. 
        @param type: Modes that this synchronous machine can operate in. Values are: "condenser", "generator_or_condenser", "generator"
        @param r2: Negative sequence resistance. 
        @param maxQ: Maximum reactive power limit. This is the maximum (nameplate) limit for the unit. 
        @param x: Positive sequence reactance of the synchronous machine. 
        @param ratedS: Nameplate apparent power rating for the unit 
        @param minQ: Minimum reactive power limit for the unit. 
        @param InitialReactiveCapabilityCurve: The default ReactiveCapabilityCurve for use by a SynchronousMachine
        @param HydroPump: The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
        @param GeneratingUnit: A synchronous machine may operate as a generator and as such becomes a member of a generating unitFor the 2010 ENTSOE IOP, this is required for Synchronous Machine.
        """
        #: Zero sequence reactance of the synchronous machine.
        self.x0 = x0

        #: Percent of the coordinated reactive control that comes from this machine.
        self.qPercent = qPercent

        #: Negative sequence reactance.
        self.x2 = x2

        #: Positive sequence resistance of the synchronous machine.
        self.r = r

        #: Priority of unit for reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on.
        self.referencePriority = referencePriority

        #: Current mode of operation. Values are: "condenser", "generator"
        self.operatingMode = operatingMode

        #: Zero sequence resistance of the synchronous machine.
        self.r0 = r0

        #: Modes that this synchronous machine can operate in. Values are: "condenser", "generator_or_condenser", "generator"
        self.type = type

        #: Negative sequence resistance.
        self.r2 = r2

        #: Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.
        self.maxQ = maxQ

        #: Positive sequence reactance of the synchronous machine.
        self.x = x

        #: Nameplate apparent power rating for the unit
        self.ratedS = ratedS

        #: Minimum reactive power limit for the unit.
        self.minQ = minQ

        self._InitialReactiveCapabilityCurve = None
        self.InitialReactiveCapabilityCurve = InitialReactiveCapabilityCurve

        self._HydroPump = None
        self.HydroPump = HydroPump

        self._GeneratingUnit = None
        self.GeneratingUnit = GeneratingUnit

        super(SynchronousMachine, self).__init__(*args, **kw_args)

    _attrs = ["x0", "qPercent", "x2", "r", "referencePriority", "operatingMode", "r0", "type", "r2", "maxQ", "x", "ratedS", "minQ"]
    _attr_types = {"x0": float, "qPercent": float, "x2": float, "r": float, "referencePriority": int, "operatingMode": str, "r0": float, "type": str, "r2": float, "maxQ": float, "x": float, "ratedS": float, "minQ": float}
    _defaults = {"x0": 0.0, "qPercent": 0.0, "x2": 0.0, "r": 0.0, "referencePriority": 0, "operatingMode": "condenser", "r0": 0.0, "type": "condenser", "r2": 0.0, "maxQ": 0.0, "x": 0.0, "ratedS": 0.0, "minQ": 0.0}
    _enums = {"operatingMode": "SynchronousMachineOperatingMode", "type": "SynchronousMachineType"}
    _refs = ["InitialReactiveCapabilityCurve", "HydroPump", "GeneratingUnit"]
    _many_refs = []

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
        """A synchronous machine may operate as a generator and as such becomes a member of a generating unitFor the 2010 ENTSOE IOP, this is required for Synchronous Machine.
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

