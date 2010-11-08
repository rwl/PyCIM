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

class ContingencyElement(IdentifiedObject):
    """An element of a system event to be studied by contingency analysis, representing a change in status of a single piece of equipment.
    """

    def __init__(self, Contingency=None, *args, **kw_args):
        """Initialises a new 'ContingencyElement' instance.

        @param Contingency: A contingency element belongs to one contingency.
        """
        self._Contingency = None
        self.Contingency = Contingency

        super(ContingencyElement, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Contingency"]
    _many_refs = []

    def getContingency(self):
        """A contingency element belongs to one contingency.
        """
        return self._Contingency

    def setContingency(self, value):
        if self._Contingency is not None:
            filtered = [x for x in self.Contingency.ContingencyElement if x != self]
            self._Contingency._ContingencyElement = filtered

        self._Contingency = value
        if self._Contingency is not None:
            self._Contingency._ContingencyElement.append(self)

    Contingency = property(getContingency, setContingency)

