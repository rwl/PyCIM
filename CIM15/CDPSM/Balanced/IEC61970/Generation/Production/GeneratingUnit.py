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

from CIM15.CDPSM.Balanced.IEC61970.Core.IdentifiedObject import IdentifiedObject

class GeneratingUnit(IdentifiedObject):
    """A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.
    """

    def __init__(self, baseP=0.0, genControlSource="plantControl", ratedNetMaxP=0.0, initialP=0.0, SynchronousMachines=None, *args, **kw_args):
        """Initialises a new 'GeneratingUnit' instance.

        @param baseP: For dispatchable units, this value represents the economic active power basepoint, for units that are not dispatchable, this value represents the fixed generation value. The value must be between the operating low and high limits. 
        @param genControlSource: The source of controls for a generating unit. Values are: "plantControl", "offAGC", "unavailable", "onAGC"
        @param ratedNetMaxP: The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity 
        @param initialP: Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration 
        @param SynchronousMachines: A synchronous machine may operate as a generator and as such becomes a member of a generating unit
        """
        #: For dispatchable units, this value represents the economic active power basepoint, for units that are not dispatchable, this value represents the fixed generation value. The value must be between the operating low and high limits.
        self.baseP = baseP

        #: The source of controls for a generating unit. Values are: "plantControl", "offAGC", "unavailable", "onAGC"
        self.genControlSource = genControlSource

        #: The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity
        self.ratedNetMaxP = ratedNetMaxP

        #: Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration
        self.initialP = initialP

        self._SynchronousMachines = []
        self.SynchronousMachines = [] if SynchronousMachines is None else SynchronousMachines

        super(GeneratingUnit, self).__init__(*args, **kw_args)

    _attrs = ["baseP", "genControlSource", "ratedNetMaxP", "initialP"]
    _attr_types = {"baseP": float, "genControlSource": str, "ratedNetMaxP": float, "initialP": float}
    _defaults = {"baseP": 0.0, "genControlSource": "plantControl", "ratedNetMaxP": 0.0, "initialP": 0.0}
    _enums = {"genControlSource": "GeneratorControlSource"}
    _refs = ["SynchronousMachines"]
    _many_refs = ["SynchronousMachines"]

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

