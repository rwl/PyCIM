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

from CIM14v13.IEC61970.Core.PowerSystemResource import PowerSystemResource

class VoltageControlZone(PowerSystemResource):
    """An area of the power system network which is defined for secondary voltage control purposes. A voltage control zone consists of a collection of substations with a designated bus bar section whose voltage will be controlled.
    """

    def __init__(self, RegulationSchedule=None, BusbarSection=None, **kw_args):
        """Initializes a new 'VoltageControlZone' instance.

        @param RegulationSchedule: A VoltageControlZone may have a  voltage regulation schedule.
        @param BusbarSection: A VoltageControlZone is controlled by a designated BusbarSection.
        """
        self._RegulationSchedule = None
        self.RegulationSchedule = RegulationSchedule

        self._BusbarSection = None
        self.BusbarSection = BusbarSection

        super(VoltageControlZone, self).__init__(**kw_args)

    def getRegulationSchedule(self):
        """A VoltageControlZone may have a  voltage regulation schedule.
        """
        return self._RegulationSchedule

    def setRegulationSchedule(self, value):
        if self._RegulationSchedule is not None:
            filtered = [x for x in self.RegulationSchedule.VoltageControlZones if x != self]
            self._RegulationSchedule._VoltageControlZones = filtered

        self._RegulationSchedule = value
        if self._RegulationSchedule is not None:
            self._RegulationSchedule._VoltageControlZones.append(self)

    RegulationSchedule = property(getRegulationSchedule, setRegulationSchedule)

    def getBusbarSection(self):
        """A VoltageControlZone is controlled by a designated BusbarSection.
        """
        return self._BusbarSection

    def setBusbarSection(self, value):
        if self._BusbarSection is not None:
            self._BusbarSection._VoltageControlZone = None

        self._BusbarSection = value
        if self._BusbarSection is not None:
            self._BusbarSection._VoltageControlZone = self

    BusbarSection = property(getBusbarSection, setBusbarSection)

