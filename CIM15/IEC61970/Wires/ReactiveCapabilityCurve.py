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

from CIM15.IEC61970.Core.Curve import Curve

class ReactiveCapabilityCurve(Curve):
    """Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.
    """

    def __init__(self, hydrogenPressure=0.0, coolantTemperature=0.0, InitiallyUsedBySynchronousMachines=None, SynchronousMachines=None, *args, **kw_args):
        """Initialises a new 'ReactiveCapabilityCurve' instance.

        @param hydrogenPressure: The hydrogen coolant pressure 
        @param coolantTemperature: The machine's coolant temperature (e.g., ambient air or stator circulating water). 
        @param InitiallyUsedBySynchronousMachines: Synchronous machines using this curve as default.
        @param SynchronousMachines: Synchronous machines using this curve.
        """
        #: The hydrogen coolant pressure
        self.hydrogenPressure = hydrogenPressure

        #: The machine's coolant temperature (e.g., ambient air or stator circulating water).
        self.coolantTemperature = coolantTemperature

        self._InitiallyUsedBySynchronousMachines = []
        self.InitiallyUsedBySynchronousMachines = [] if InitiallyUsedBySynchronousMachines is None else InitiallyUsedBySynchronousMachines

        self._SynchronousMachines = []
        self.SynchronousMachines = [] if SynchronousMachines is None else SynchronousMachines

        super(ReactiveCapabilityCurve, self).__init__(*args, **kw_args)

    _attrs = ["hydrogenPressure", "coolantTemperature"]
    _attr_types = {"hydrogenPressure": float, "coolantTemperature": float}
    _defaults = {"hydrogenPressure": 0.0, "coolantTemperature": 0.0}
    _enums = {}
    _refs = ["InitiallyUsedBySynchronousMachines", "SynchronousMachines"]
    _many_refs = ["InitiallyUsedBySynchronousMachines", "SynchronousMachines"]

    def getInitiallyUsedBySynchronousMachines(self):
        """Synchronous machines using this curve as default.
        """
        return self._InitiallyUsedBySynchronousMachines

    def setInitiallyUsedBySynchronousMachines(self, value):
        for x in self._InitiallyUsedBySynchronousMachines:
            x.InitialReactiveCapabilityCurve = None
        for y in value:
            y._InitialReactiveCapabilityCurve = self
        self._InitiallyUsedBySynchronousMachines = value

    InitiallyUsedBySynchronousMachines = property(getInitiallyUsedBySynchronousMachines, setInitiallyUsedBySynchronousMachines)

    def addInitiallyUsedBySynchronousMachines(self, *InitiallyUsedBySynchronousMachines):
        for obj in InitiallyUsedBySynchronousMachines:
            obj.InitialReactiveCapabilityCurve = self

    def removeInitiallyUsedBySynchronousMachines(self, *InitiallyUsedBySynchronousMachines):
        for obj in InitiallyUsedBySynchronousMachines:
            obj.InitialReactiveCapabilityCurve = None

    def getSynchronousMachines(self):
        """Synchronous machines using this curve.
        """
        return self._SynchronousMachines

    def setSynchronousMachines(self, value):
        for p in self._SynchronousMachines:
            filtered = [q for q in p.ReactiveCapabilityCurves if q != self]
            self._SynchronousMachines._ReactiveCapabilityCurves = filtered
        for r in value:
            if self not in r._ReactiveCapabilityCurves:
                r._ReactiveCapabilityCurves.append(self)
        self._SynchronousMachines = value

    SynchronousMachines = property(getSynchronousMachines, setSynchronousMachines)

    def addSynchronousMachines(self, *SynchronousMachines):
        for obj in SynchronousMachines:
            if self not in obj._ReactiveCapabilityCurves:
                obj._ReactiveCapabilityCurves.append(self)
            self._SynchronousMachines.append(obj)

    def removeSynchronousMachines(self, *SynchronousMachines):
        for obj in SynchronousMachines:
            if self in obj._ReactiveCapabilityCurves:
                obj._ReactiveCapabilityCurves.remove(self)
            self._SynchronousMachines.remove(obj)

