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

from CIM14.CDPSM.Balanced.IEC61970.Core.IdentifiedObject import IdentifiedObject

class SubGeographicalRegion(IdentifiedObject):
    """A subset of a geographical region of a power system network model.
    """

    def __init__(self, Region=None, Lines=None, Substations=None, *args, **kw_args):
        """Initialises a new 'SubGeographicalRegion' instance.

        @param Region: The association is used in the naming hierarchy.
        @param Lines: A Line can be contained by a SubGeographical Region.
        @param Substations: The association is used in the naming hierarchy.
        """
        self._Region = None
        self.Region = Region

        self._Lines = []
        self.Lines = [] if Lines is None else Lines

        self._Substations = []
        self.Substations = [] if Substations is None else Substations

        super(SubGeographicalRegion, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Region", "Lines", "Substations"]
    _many_refs = ["Lines", "Substations"]

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

