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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class RecloseSequence(IdentifiedObject):
    """A reclose sequence (open and close) is defined for each possible reclosure of a breaker.
    """

    def __init__(self, recloseDelay=0.0, recloseStep=0, ProtectedSwitch=None, *args, **kw_args):
        """Initialises a new 'RecloseSequence' instance.

        @param recloseDelay: Indicates the time lapse before the reclose step will execute a reclose. 
        @param recloseStep: Indicates the ordinal position of the reclose step relative to other steps in the sequence. 
        @param ProtectedSwitch: A breaker may have zero or more automatic reclosures after a trip occurs.
        """
        #: Indicates the time lapse before the reclose step will execute a reclose.
        self.recloseDelay = recloseDelay

        #: Indicates the ordinal position of the reclose step relative to other steps in the sequence.
        self.recloseStep = recloseStep

        self._ProtectedSwitch = None
        self.ProtectedSwitch = ProtectedSwitch

        super(RecloseSequence, self).__init__(*args, **kw_args)

    _attrs = ["recloseDelay", "recloseStep"]
    _attr_types = {"recloseDelay": float, "recloseStep": int}
    _defaults = {"recloseDelay": 0.0, "recloseStep": 0}
    _enums = {}
    _refs = ["ProtectedSwitch"]
    _many_refs = []

    def getProtectedSwitch(self):
        """A breaker may have zero or more automatic reclosures after a trip occurs.
        """
        return self._ProtectedSwitch

    def setProtectedSwitch(self, value):
        if self._ProtectedSwitch is not None:
            filtered = [x for x in self.ProtectedSwitch.RecloseSequences if x != self]
            self._ProtectedSwitch._RecloseSequences = filtered

        self._ProtectedSwitch = value
        if self._ProtectedSwitch is not None:
            self._ProtectedSwitch._RecloseSequences.append(self)

    ProtectedSwitch = property(getProtectedSwitch, setProtectedSwitch)

