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

from CIM15.IEC61970.Wires.Switch import Switch

class ProtectedSwitch(Switch):
    """A ProtectedSwitch is a switching device that can be operated by ProtectionEquipment.A ProtectedSwitch is a switching device that can be operated by ProtectionEquipment.
    """

    def __init__(self, breakingCapacity=0.0, ProtectionEquipments=None, RecloseSequences=None, *args, **kw_args):
        """Initialises a new 'ProtectedSwitch' instance.

        @param breakingCapacity: The maximum fault current a breaking device can break safely under prescribed conditions of use. 
        @param ProtectionEquipments: Protection equipments that operate this ProtectedSwitch.
        @param RecloseSequences: A breaker may have zero or more automatic reclosures after a trip occurs.
        """
        #: The maximum fault current a breaking device can break safely under prescribed conditions of use.
        self.breakingCapacity = breakingCapacity

        self._ProtectionEquipments = []
        self.ProtectionEquipments = [] if ProtectionEquipments is None else ProtectionEquipments

        self._RecloseSequences = []
        self.RecloseSequences = [] if RecloseSequences is None else RecloseSequences

        super(ProtectedSwitch, self).__init__(*args, **kw_args)

    _attrs = ["breakingCapacity"]
    _attr_types = {"breakingCapacity": float}
    _defaults = {"breakingCapacity": 0.0}
    _enums = {}
    _refs = ["ProtectionEquipments", "RecloseSequences"]
    _many_refs = ["ProtectionEquipments", "RecloseSequences"]

    def getProtectionEquipments(self):
        """Protection equipments that operate this ProtectedSwitch.
        """
        return self._ProtectionEquipments

    def setProtectionEquipments(self, value):
        for p in self._ProtectionEquipments:
            filtered = [q for q in p.ProtectedSwitches if q != self]
            self._ProtectionEquipments._ProtectedSwitches = filtered
        for r in value:
            if self not in r._ProtectedSwitches:
                r._ProtectedSwitches.append(self)
        self._ProtectionEquipments = value

    ProtectionEquipments = property(getProtectionEquipments, setProtectionEquipments)

    def addProtectionEquipments(self, *ProtectionEquipments):
        for obj in ProtectionEquipments:
            if self not in obj._ProtectedSwitches:
                obj._ProtectedSwitches.append(self)
            self._ProtectionEquipments.append(obj)

    def removeProtectionEquipments(self, *ProtectionEquipments):
        for obj in ProtectionEquipments:
            if self in obj._ProtectedSwitches:
                obj._ProtectedSwitches.remove(self)
            self._ProtectionEquipments.remove(obj)

    def getRecloseSequences(self):
        """A breaker may have zero or more automatic reclosures after a trip occurs.
        """
        return self._RecloseSequences

    def setRecloseSequences(self, value):
        for x in self._RecloseSequences:
            x.ProtectedSwitch = None
        for y in value:
            y._ProtectedSwitch = self
        self._RecloseSequences = value

    RecloseSequences = property(getRecloseSequences, setRecloseSequences)

    def addRecloseSequences(self, *RecloseSequences):
        for obj in RecloseSequences:
            obj.ProtectedSwitch = self

    def removeRecloseSequences(self, *RecloseSequences):
        for obj in RecloseSequences:
            obj.ProtectedSwitch = None

