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

class ControlAreaGeneratingUnit(Element):
    """A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.
    """

    def __init__(self, AltGeneratingUnitMeas=None, ControlArea=None, GeneratingUnit=None, *args, **kw_args):
        """Initialises a new 'ControlAreaGeneratingUnit' instance.

        @param AltGeneratingUnitMeas: The link to prioritized measurements for this GeneratingUnit.
        @param ControlArea: The parent control area for the generating unit specifications.
        @param GeneratingUnit: The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once.
        """
        self._AltGeneratingUnitMeas = []
        self.AltGeneratingUnitMeas = [] if AltGeneratingUnitMeas is None else AltGeneratingUnitMeas

        self._ControlArea = None
        self.ControlArea = ControlArea

        self._GeneratingUnit = None
        self.GeneratingUnit = GeneratingUnit

        super(ControlAreaGeneratingUnit, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["AltGeneratingUnitMeas", "ControlArea", "GeneratingUnit"]
    _many_refs = ["AltGeneratingUnitMeas"]

    def getAltGeneratingUnitMeas(self):
        """The link to prioritized measurements for this GeneratingUnit.
        """
        return self._AltGeneratingUnitMeas

    def setAltGeneratingUnitMeas(self, value):
        for x in self._AltGeneratingUnitMeas:
            x._ControlAreaGeneratingUnit = None
        for y in value:
            y._ControlAreaGeneratingUnit = self
        self._AltGeneratingUnitMeas = value

    AltGeneratingUnitMeas = property(getAltGeneratingUnitMeas, setAltGeneratingUnitMeas)

    def addAltGeneratingUnitMeas(self, *AltGeneratingUnitMeas):
        for obj in AltGeneratingUnitMeas:
            obj._ControlAreaGeneratingUnit = self
            self._AltGeneratingUnitMeas.append(obj)

    def removeAltGeneratingUnitMeas(self, *AltGeneratingUnitMeas):
        for obj in AltGeneratingUnitMeas:
            obj._ControlAreaGeneratingUnit = None
            self._AltGeneratingUnitMeas.remove(obj)

    def getControlArea(self):
        """The parent control area for the generating unit specifications.
        """
        return self._ControlArea

    def setControlArea(self, value):
        if self._ControlArea is not None:
            filtered = [x for x in self.ControlArea.ControlAreaGeneratingUnit if x != self]
            self._ControlArea._ControlAreaGeneratingUnit = filtered

        self._ControlArea = value
        if self._ControlArea is not None:
            self._ControlArea._ControlAreaGeneratingUnit.append(self)

    ControlArea = property(getControlArea, setControlArea)

    def getGeneratingUnit(self):
        """The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once.
        """
        return self._GeneratingUnit

    def setGeneratingUnit(self, value):
        if self._GeneratingUnit is not None:
            filtered = [x for x in self.GeneratingUnit.ControlAreaGeneratingUnit if x != self]
            self._GeneratingUnit._ControlAreaGeneratingUnit = filtered

        self._GeneratingUnit = value
        if self._GeneratingUnit is not None:
            self._GeneratingUnit._ControlAreaGeneratingUnit.append(self)

    GeneratingUnit = property(getGeneratingUnit, setGeneratingUnit)

