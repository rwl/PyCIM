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

from CIM14.ENTSOE.Equipment.Core.IdentifiedObject import IdentifiedObject

class GeographicalRegion(IdentifiedObject):
    """A geographical region of a power system network model.
    """

    def __init__(self, Regions=None, *args, **kw_args):
        """Initialises a new 'GeographicalRegion' instance.

        @param Regions: The association is used in the naming hierarchy.
        """
        self._Regions = []
        self.Regions = [] if Regions is None else Regions

        super(GeographicalRegion, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Regions"]
    _many_refs = ["Regions"]

    def getRegions(self):
        """The association is used in the naming hierarchy.
        """
        return self._Regions

    def setRegions(self, value):
        for x in self._Regions:
            x.Region = None
        for y in value:
            y._Region = self
        self._Regions = value

    Regions = property(getRegions, setRegions)

    def addRegions(self, *Regions):
        for obj in Regions:
            obj.Region = self

    def removeRegions(self, *Regions):
        for obj in Regions:
            obj.Region = None

