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

from CIM14.CDPSM.Unbalanced.IEC61970.Core.EquipmentContainer import EquipmentContainer

class Substation(EquipmentContainer):
    """A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.
    """

    def __init__(self, Region=None, VoltageLevels=None, *args, **kw_args):
        """Initialises a new 'Substation' instance.

        @param Region: The association is used in the naming hierarchy.
        @param VoltageLevels: The association is used in the naming hierarchy.
        """
        self._Region = None
        self.Region = Region

        self._VoltageLevels = []
        self.VoltageLevels = [] if VoltageLevels is None else VoltageLevels

        super(Substation, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Region", "VoltageLevels"]
    _many_refs = ["VoltageLevels"]

    def getRegion(self):
        """The association is used in the naming hierarchy.
        """
        return self._Region

    def setRegion(self, value):
        if self._Region is not None:
            filtered = [x for x in self.Region.Substations if x != self]
            self._Region._Substations = filtered

        self._Region = value
        if self._Region is not None:
            if self not in self._Region._Substations:
                self._Region._Substations.append(self)

    Region = property(getRegion, setRegion)

    def getVoltageLevels(self):
        """The association is used in the naming hierarchy.
        """
        return self._VoltageLevels

    def setVoltageLevels(self, value):
        for x in self._VoltageLevels:
            x.Substation = None
        for y in value:
            y._Substation = self
        self._VoltageLevels = value

    VoltageLevels = property(getVoltageLevels, setVoltageLevels)

    def addVoltageLevels(self, *VoltageLevels):
        for obj in VoltageLevels:
            obj.Substation = self

    def removeVoltageLevels(self, *VoltageLevels):
        for obj in VoltageLevels:
            obj.Substation = None

