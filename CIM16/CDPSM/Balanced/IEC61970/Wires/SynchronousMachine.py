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

from CIM16.CDPSM.Balanced.IEC61970.Core.IdentifiedObject import IdentifiedObject

class SynchronousMachine(IdentifiedObject):
    """An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.
    """

    def __init__(self, operatingMode="condenser", maxQ=0.0, baseQ=0.0, minQ=0.0, type="condenser", GeneratingUnit=None, *args, **kw_args):
        """Initialises a new 'SynchronousMachine' instance.

        @param operatingMode: Current mode of operation. Values are: "condenser", "generator"
        @param maxQ: Maximum reactive power limit. This is the maximum (nameplate) limit for the unit. 
        @param baseQ: Default base reactive power value. This value represents the initial reactive power that can be used by any application function. 
        @param minQ: Minimum reactive power limit for the unit. 
        @param type: Modes that this synchronous machine can operate in. Values are: "condenser", "generator_or_condenser", "generator"
        @param GeneratingUnit: A synchronous machine may operate as a generator and as such becomes a member of a generating unit
        """
        #: Current mode of operation. Values are: "condenser", "generator"
        self.operatingMode = operatingMode

        #: Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.
        self.maxQ = maxQ

        #: Default base reactive power value. This value represents the initial reactive power that can be used by any application function.
        self.baseQ = baseQ

        #: Minimum reactive power limit for the unit.
        self.minQ = minQ

        #: Modes that this synchronous machine can operate in. Values are: "condenser", "generator_or_condenser", "generator"
        self.type = type

        self._GeneratingUnit = None
        self.GeneratingUnit = GeneratingUnit

        super(SynchronousMachine, self).__init__(*args, **kw_args)

    _attrs = ["operatingMode", "maxQ", "baseQ", "minQ", "type"]
    _attr_types = {"operatingMode": str, "maxQ": float, "baseQ": float, "minQ": float, "type": str}
    _defaults = {"operatingMode": "condenser", "maxQ": 0.0, "baseQ": 0.0, "minQ": 0.0, "type": "condenser"}
    _enums = {"operatingMode": "SynchronousMachineOperatingMode", "type": "SynchronousMachineType"}
    _refs = ["GeneratingUnit"]
    _many_refs = []

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

