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

from CIM14.IEC61970.LoadModel.EnergyArea import EnergyArea

class SubLoadArea(EnergyArea):
    """The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    def __init__(self, LoadGroups=None, LoadArea=None, *args, **kw_args):
        """Initialises a new 'SubLoadArea' instance.

        @param LoadGroups: The Loadgroups in the SubLoadArea.
        @param LoadArea: The LoadArea where the SubLoadArea belongs.
        """
        self._LoadGroups = []
        self.LoadGroups = [] if LoadGroups is None else LoadGroups

        self._LoadArea = None
        self.LoadArea = LoadArea

        super(SubLoadArea, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["LoadGroups", "LoadArea"]
    _many_refs = ["LoadGroups"]

    def getLoadGroups(self):
        """The Loadgroups in the SubLoadArea.
        """
        return self._LoadGroups

    def setLoadGroups(self, value):
        for x in self._LoadGroups:
            x._SubLoadArea = None
        for y in value:
            y._SubLoadArea = self
        self._LoadGroups = value

    LoadGroups = property(getLoadGroups, setLoadGroups)

    def addLoadGroups(self, *LoadGroups):
        for obj in LoadGroups:
            obj._SubLoadArea = self
            self._LoadGroups.append(obj)

    def removeLoadGroups(self, *LoadGroups):
        for obj in LoadGroups:
            obj._SubLoadArea = None
            self._LoadGroups.remove(obj)

    def getLoadArea(self):
        """The LoadArea where the SubLoadArea belongs.
        """
        return self._LoadArea

    def setLoadArea(self, value):
        if self._LoadArea is not None:
            filtered = [x for x in self.LoadArea.SubLoadAreas if x != self]
            self._LoadArea._SubLoadAreas = filtered

        self._LoadArea = value
        if self._LoadArea is not None:
            self._LoadArea._SubLoadAreas.append(self)

    LoadArea = property(getLoadArea, setLoadArea)

