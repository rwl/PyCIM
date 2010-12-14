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

class MeasurementValueSource(IdentifiedObject):
    """MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301.
    """

    def __init__(self, MeasurementValues=None, *args, **kw_args):
        """Initialises a new 'MeasurementValueSource' instance.

        @param MeasurementValues: The MeasurementValues updated by the source
        """
        self._MeasurementValues = []
        self.MeasurementValues = [] if MeasurementValues is None else MeasurementValues

        super(MeasurementValueSource, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["MeasurementValues"]
    _many_refs = ["MeasurementValues"]

    def getMeasurementValues(self):
        """The MeasurementValues updated by the source
        """
        return self._MeasurementValues

    def setMeasurementValues(self, value):
        for x in self._MeasurementValues:
            x.MeasurementValueSource = None
        for y in value:
            y._MeasurementValueSource = self
        self._MeasurementValues = value

    MeasurementValues = property(getMeasurementValues, setMeasurementValues)

    def addMeasurementValues(self, *MeasurementValues):
        for obj in MeasurementValues:
            obj.MeasurementValueSource = self

    def removeMeasurementValues(self, *MeasurementValues):
        for obj in MeasurementValues:
            obj.MeasurementValueSource = None

