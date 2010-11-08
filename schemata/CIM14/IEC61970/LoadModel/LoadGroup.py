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

class LoadGroup(IdentifiedObject):
    """The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    def __init__(self, SubLoadArea=None, *args, **kw_args):
        """Initialises a new 'LoadGroup' instance.

        @param SubLoadArea: The SubLoadArea where the Loadgroup belongs.
        """
        self._SubLoadArea = None
        self.SubLoadArea = SubLoadArea

        super(LoadGroup, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["SubLoadArea"]
    _many_refs = []

    def getSubLoadArea(self):
        """The SubLoadArea where the Loadgroup belongs.
        """
        return self._SubLoadArea

    def setSubLoadArea(self, value):
        if self._SubLoadArea is not None:
            filtered = [x for x in self.SubLoadArea.LoadGroups if x != self]
            self._SubLoadArea._LoadGroups = filtered

        self._SubLoadArea = value
        if self._SubLoadArea is not None:
            self._SubLoadArea._LoadGroups.append(self)

    SubLoadArea = property(getSubLoadArea, setSubLoadArea)

