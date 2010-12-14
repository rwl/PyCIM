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

class LoadArea(EnergyArea):
    """The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    def __init__(self, SubLoadAreas=None, *args, **kw_args):
        """Initialises a new 'LoadArea' instance.

        @param SubLoadAreas: The SubLoadAreas in the LoadArea.
        """
        self._SubLoadAreas = []
        self.SubLoadAreas = [] if SubLoadAreas is None else SubLoadAreas

        super(LoadArea, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["SubLoadAreas"]
    _many_refs = ["SubLoadAreas"]

    def getSubLoadAreas(self):
        """The SubLoadAreas in the LoadArea.
        """
        return self._SubLoadAreas

    def setSubLoadAreas(self, value):
        for x in self._SubLoadAreas:
            x.LoadArea = None
        for y in value:
            y._LoadArea = self
        self._SubLoadAreas = value

    SubLoadAreas = property(getSubLoadAreas, setSubLoadAreas)

    def addSubLoadAreas(self, *SubLoadAreas):
        for obj in SubLoadAreas:
            obj.LoadArea = self

    def removeSubLoadAreas(self, *SubLoadAreas):
        for obj in SubLoadAreas:
            obj.LoadArea = None

