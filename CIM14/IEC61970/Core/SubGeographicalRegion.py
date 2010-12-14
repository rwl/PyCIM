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

class SubGeographicalRegion(IdentifiedObject):
    """A subset of a geographical region of a power system network model.
    """

    def __init__(self, Region=None, Substations=None, Lines=None, *args, **kw_args):
        """Initialises a new 'SubGeographicalRegion' instance.

        @param Region: The association is used in the naming hierarchy.
        @param Substations: The association is used in the naming hierarchy.
        @param Lines: A Line can be contained by a SubGeographical Region.
        """
        self._Region = None
        self.Region = Region

        self._Substations = []
        self.Substations = [] if Substations is None else Substations

        self._Lines = []
        self.Lines = [] if Lines is None else Lines

        super(SubGeographicalRegion, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Region", "Substations", "Lines"]
    _many_refs = ["Substations", "Lines"]

    def getRegion(self):
        """The association is used in the naming hierarchy.
        """
        return self._Region

    def setRegion(self, value):
        if self._Region is not None:
            filtered = [x for x in self.Region.Regions if x != self]
            self._Region._Regions = filtered

        self._Region = value
        if self._Region is not None:
            if self not in self._Region._Regions:
                self._Region._Regions.append(self)

    Region = property(getRegion, setRegion)

    def getSubstations(self):
        """The association is used in the naming hierarchy.
        """
        return self._Substations

    def setSubstations(self, value):
        for x in self._Substations:
            x.Region = None
        for y in value:
            y._Region = self
        self._Substations = value

    Substations = property(getSubstations, setSubstations)

    def addSubstations(self, *Substations):
        for obj in Substations:
            obj.Region = self

    def removeSubstations(self, *Substations):
        for obj in Substations:
            obj.Region = None

    def getLines(self):
        """A Line can be contained by a SubGeographical Region.
        """
        return self._Lines

    def setLines(self, value):
        for x in self._Lines:
            x.Region = None
        for y in value:
            y._Region = self
        self._Lines = value

    Lines = property(getLines, setLines)

    def addLines(self, *Lines):
        for obj in Lines:
            obj.Region = self

    def removeLines(self, *Lines):
        for obj in Lines:
            obj.Region = None

