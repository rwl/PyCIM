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

from CIM14v13.IEC61970.Core.IrregularIntervalSchedule import IrregularIntervalSchedule

class OutageSchedule(IrregularIntervalSchedule):
    """The period of time that a piece of equipment is out of service, for example, for maintenance or testing; including the equipment's active power rating while under maintenance. The X-axis represents absolute time and the Y-axis represents the equipment's available rating while out of service.
    """

    def __init__(self, PowerSystemResource=None, SwitchingOperations=None, PlannedOutage=None, *args, **kw_args):
        """Initializes a new 'OutageSchedule' instance.

        @param PowerSystemResource: A power system resource may have an outage schedule
        @param SwitchingOperations: An OutageSchedule may operate many switches.
        @param PlannedOutage:
        """
        self._PowerSystemResource = None
        self.PowerSystemResource = PowerSystemResource

        self._SwitchingOperations = []
        self.SwitchingOperations = [] if SwitchingOperations is None else SwitchingOperations

        self._PlannedOutage = None
        self.PlannedOutage = PlannedOutage

        super(OutageSchedule, self).__init__(*args, **kw_args)

    def getPowerSystemResource(self):
        """A power system resource may have an outage schedule
        """
        return self._PowerSystemResource

    def setPowerSystemResource(self, value):
        if self._PowerSystemResource is not None:
            self._PowerSystemResource._OutageSchedule = None

        self._PowerSystemResource = value
        if self._PowerSystemResource is not None:
            self._PowerSystemResource._OutageSchedule = self

    PowerSystemResource = property(getPowerSystemResource, setPowerSystemResource)

    def getSwitchingOperations(self):
        """An OutageSchedule may operate many switches.
        """
        return self._SwitchingOperations

    def setSwitchingOperations(self, value):
        for x in self._SwitchingOperations:
            x._OutageSchedule = None
        for y in value:
            y._OutageSchedule = self
        self._SwitchingOperations = value

    SwitchingOperations = property(getSwitchingOperations, setSwitchingOperations)

    def addSwitchingOperations(self, *SwitchingOperations):
        for obj in SwitchingOperations:
            obj._OutageSchedule = self
            self._SwitchingOperations.append(obj)

    def removeSwitchingOperations(self, *SwitchingOperations):
        for obj in SwitchingOperations:
            obj._OutageSchedule = None
            self._SwitchingOperations.remove(obj)

    def getPlannedOutage(self):
        
        return self._PlannedOutage

    def setPlannedOutage(self, value):
        if self._PlannedOutage is not None:
            filtered = [x for x in self.PlannedOutage.OutageSchedules if x != self]
            self._PlannedOutage._OutageSchedules = filtered

        self._PlannedOutage = value
        if self._PlannedOutage is not None:
            self._PlannedOutage._OutageSchedules.append(self)

    PlannedOutage = property(getPlannedOutage, setPlannedOutage)

