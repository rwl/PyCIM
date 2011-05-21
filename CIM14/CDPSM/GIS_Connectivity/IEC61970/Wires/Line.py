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

from CIM14.CDPSM.GIS_Connectivity.IEC61970.Core.EquipmentContainer import EquipmentContainer

class Line(EquipmentContainer):
    """A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.
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
            if self not in self._Region._Lines:
                self._Region._Lines.append(self)

    Region = property(getRegion, setRegion)

