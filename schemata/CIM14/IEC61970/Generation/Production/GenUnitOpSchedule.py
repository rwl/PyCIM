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

from CIM14.IEC61970.Core.RegularIntervalSchedule import RegularIntervalSchedule

class GenUnitOpSchedule(RegularIntervalSchedule):
    """The generating unit's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses. The X-axis represents absolute time. The Y1-axis represents the status (0=off-line and unavailable: 1=available: 2=must run: 3=must run at fixed power value: etc.). The Y2-axis represents the must run fixed power value where required.
    """

    def __init__(self, GeneratingUnit=None, **kw_args):
        """Initializes a new 'GenUnitOpSchedule' instance.

        @param GeneratingUnit: A generating unit may have an operating schedule, indicating the planned operation of the unit
        """
        self._GeneratingUnit = None
        self.GeneratingUnit = GeneratingUnit

        super(GenUnitOpSchedule, self).__init__(**kw_args)

    def getGeneratingUnit(self):
        """A generating unit may have an operating schedule, indicating the planned operation of the unit
        """
        return self._GeneratingUnit

    def setGeneratingUnit(self, value):
        if self._GeneratingUnit is not None:
            self._GeneratingUnit._GenUnitOpSchedule = None

        self._GeneratingUnit = value
        if self._GeneratingUnit is not None:
            self._GeneratingUnit._GenUnitOpSchedule = self

    GeneratingUnit = property(getGeneratingUnit, setGeneratingUnit)

