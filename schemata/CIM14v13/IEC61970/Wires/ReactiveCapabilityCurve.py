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

from CIM14v13.IEC61970.Core.Curve import Curve

class ReactiveCapabilityCurve(Curve):
    """Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.
    """

    def __init__(self, coolantTemperature=0.0, hydrogenPressure=0.0, SynchronousMachines=None, InitiallyUsedBySynchronousMachines=None, *args, **kw_args):
        """Initializes a new 'ReactiveCapabilityCurve' instance.

        @param coolantTemperature: The machine's coolant temperature (e.g., ambient air or stator circulating water). 
        @param hydrogenPressure: The hydrogen coolant pressure 
        @param SynchronousMachines: Synchronous machines using this curve.
        @param InitiallyUsedBySynchronousMachines: Synchronous machines using this curve as default.
        """
        #: The machine's coolant temperature (e.g., ambient air or stator circulating water).
        self.coolantTemperature = coolantTemperature

        #: The hydrogen coolant pressure
        self.hydrogenPressure = hydrogenPressure

        self._SynchronousMachines = []
        self.SynchronousMachines = [] if SynchronousMachines is None else SynchronousMachines

        self._InitiallyUsedBySynchronousMachines = []
        self.InitiallyUsedBySynchronousMachines = [] if InitiallyUsedBySynchronousMachines is None else InitiallyUsedBySynchronousMachines

        super(ReactiveCapabilityCurve, self).__init__(*args, **kw_args)

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

    def getInitiallyUsedBySynchronousMachines(self):
        """Synchronous machines using this curve as default.
        """
        return self._InitiallyUsedBySynchronousMachines

    def setInitiallyUsedBySynchronousMachines(self, value):
        for x in self._InitiallyUsedBySynchronousMachines:
            x._InitialReactiveCapabilityCurve = None
        for y in value:
            y._InitialReactiveCapabilityCurve = self
        self._InitiallyUsedBySynchronousMachines = value

    InitiallyUsedBySynchronousMachines = property(getInitiallyUsedBySynchronousMachines, setInitiallyUsedBySynchronousMachines)

    def addInitiallyUsedBySynchronousMachines(self, *InitiallyUsedBySynchronousMachines):
        for obj in InitiallyUsedBySynchronousMachines:
            obj._InitialReactiveCapabilityCurve = self
            self._InitiallyUsedBySynchronousMachines.append(obj)

    def removeInitiallyUsedBySynchronousMachines(self, *InitiallyUsedBySynchronousMachines):
        for obj in InitiallyUsedBySynchronousMachines:
            obj._InitialReactiveCapabilityCurve = None
            self._InitiallyUsedBySynchronousMachines.remove(obj)

