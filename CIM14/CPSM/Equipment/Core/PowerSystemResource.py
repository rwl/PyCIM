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

from CIM14.CPSM.Equipment.Core.IdentifiedObject import IdentifiedObject

class PowerSystemResource(IdentifiedObject):
    """A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.
    """

    def __init__(self, Measurements=None, *args, **kw_args):
        """Initialises a new 'PowerSystemResource' instance.

        @param Measurements: The Measurements that are included in the naming hierarchy where the PSR is the containing object
        """
        self._Measurements = []
        self.Measurements = [] if Measurements is None else Measurements

        super(PowerSystemResource, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Measurements"]
    _many_refs = ["Measurements"]

    def getMeasurements(self):
        """The Measurements that are included in the naming hierarchy where the PSR is the containing object
        """
        return self._Measurements

    def setMeasurements(self, value):
        for x in self._Measurements:
            x.PowerSystemResource = None
        for y in value:
            y._PowerSystemResource = self
        self._Measurements = value

    Measurements = property(getMeasurements, setMeasurements)

    def addMeasurements(self, *Measurements):
        for obj in Measurements:
            obj.PowerSystemResource = self

    def removeMeasurements(self, *Measurements):
        for obj in Measurements:
            obj.PowerSystemResource = None

