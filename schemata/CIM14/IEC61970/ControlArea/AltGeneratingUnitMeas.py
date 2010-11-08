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

from CIM14.Element import Element

class AltGeneratingUnitMeas(Element):
    """A prioritized measurement to be used for the generating unit in the control area specificaiton.
    """

    def __init__(self, priority=0, ControlAreaGeneratingUnit=None, AnalogValue=None, *args, **kw_args):
        """Initialises a new 'AltGeneratingUnitMeas' instance.

        @param priority: Priority of a measurement usage.   Lower numbers have first priority. 
        @param ControlAreaGeneratingUnit: The control aread generating unit to which the prioritized measurement assignment is applied.
        @param AnalogValue: The specific analog value used as a source.
        """
        #: Priority of a measurement usage.   Lower numbers have first priority.
        self.priority = priority

        self._ControlAreaGeneratingUnit = None
        self.ControlAreaGeneratingUnit = ControlAreaGeneratingUnit

        self._AnalogValue = None
        self.AnalogValue = AnalogValue

        super(AltGeneratingUnitMeas, self).__init__(*args, **kw_args)

    _attrs = ["priority"]
    _attr_types = {"priority": int}
    _defaults = {"priority": 0}
    _enums = {}
    _refs = ["ControlAreaGeneratingUnit", "AnalogValue"]
    _many_refs = []

    def getControlAreaGeneratingUnit(self):
        """The control aread generating unit to which the prioritized measurement assignment is applied.
        """
        return self._ControlAreaGeneratingUnit

    def setControlAreaGeneratingUnit(self, value):
        if self._ControlAreaGeneratingUnit is not None:
            filtered = [x for x in self.ControlAreaGeneratingUnit.AltGeneratingUnitMeas if x != self]
            self._ControlAreaGeneratingUnit._AltGeneratingUnitMeas = filtered

        self._ControlAreaGeneratingUnit = value
        if self._ControlAreaGeneratingUnit is not None:
            self._ControlAreaGeneratingUnit._AltGeneratingUnitMeas.append(self)

    ControlAreaGeneratingUnit = property(getControlAreaGeneratingUnit, setControlAreaGeneratingUnit)

    def getAnalogValue(self):
        """The specific analog value used as a source.
        """
        return self._AnalogValue

    def setAnalogValue(self, value):
        if self._AnalogValue is not None:
            filtered = [x for x in self.AnalogValue.AltGeneratingUnit if x != self]
            self._AnalogValue._AltGeneratingUnit = filtered

        self._AnalogValue = value
        if self._AnalogValue is not None:
            self._AnalogValue._AltGeneratingUnit.append(self)

    AnalogValue = property(getAnalogValue, setAnalogValue)

