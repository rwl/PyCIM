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

from CIM14.IEC61970.Core.EquipmentContainer import EquipmentContainer

class Line(EquipmentContainer):
    """Contains equipment beyond a substation belonging to a power transmission line.
    """

    def __init__(self, Region=None, *args, **kw_args):
        """Initialises a new 'Line' instance.

        @param Region: A Line can be contained by a SubGeographical Region.
        """
        self._Region = None
        self.Region = Region

        super(Line, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Region"]
    _many_refs = []

    def getRegion(self):
        """A Line can be contained by a SubGeographical Region.
        """
        return self._Region

    def setRegion(self, value):
        if self._Region is not None:
            filtered = [x for x in self.Region.Lines if x != self]
            self._Region._Lines = filtered

        self._Region = value
        if self._Region is not None:
            self._Region._Lines.append(self)

    Region = property(getRegion, setRegion)

