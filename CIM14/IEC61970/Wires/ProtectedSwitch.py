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

from CIM14.IEC61970.Wires.Switch import Switch

class ProtectedSwitch(Switch):
    """A ProtectedSwitch is a switching device that can be operated by ProtectionEquipment.
    """

    def __init__(self, RecloseSequences=None, *args, **kw_args):
        """Initialises a new 'ProtectedSwitch' instance.

        @param RecloseSequences: A breaker may have zero or more automatic reclosures after a trip occurs.
        """
        self._RecloseSequences = []
        self.RecloseSequences = [] if RecloseSequences is None else RecloseSequences

        super(ProtectedSwitch, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["RecloseSequences"]
    _many_refs = ["RecloseSequences"]

    def getRecloseSequences(self):
        """A breaker may have zero or more automatic reclosures after a trip occurs.
        """
        return self._RecloseSequences

    def setRecloseSequences(self, value):
        for x in self._RecloseSequences:
            x._ProtectedSwitch = None
        for y in value:
            y._ProtectedSwitch = self
        self._RecloseSequences = value

    RecloseSequences = property(getRecloseSequences, setRecloseSequences)

    def addRecloseSequences(self, *RecloseSequences):
        for obj in RecloseSequences:
            obj._ProtectedSwitch = self
            self._RecloseSequences.append(obj)

    def removeRecloseSequences(self, *RecloseSequences):
        for obj in RecloseSequences:
            obj._ProtectedSwitch = None
            self._RecloseSequences.remove(obj)

