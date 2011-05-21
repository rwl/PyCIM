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

from CIM14.CPSM.Equipment.Core.Curve import Curve

class ReactiveCapabilityCurve(Curve):
    """Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.-  ReactiveCapabilityCurves are not required if the reactive power limits of the SynchronousMachine do not vary with real power output. -  By convention, the Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum. -  Because the x value will always be specified in MW and the y values will always be specified in MVAr, the xMultiplier, y1Multiplier, and y2Multiplier attributes do not need to be supplied. 
    """

    def __init__(self, InitiallyUsedBySynchronousMachines=None, *args, **kw_args):
        """Initialises a new 'ReactiveCapabilityCurve' instance.

        @param InitiallyUsedBySynchronousMachines: Synchronous machines using this curve as default.
        """
        self._InitiallyUsedBySynchronousMachines = []
        self.InitiallyUsedBySynchronousMachines = [] if InitiallyUsedBySynchronousMachines is None else InitiallyUsedBySynchronousMachines

        super(ReactiveCapabilityCurve, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["InitiallyUsedBySynchronousMachines"]
    _many_refs = ["InitiallyUsedBySynchronousMachines"]

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

