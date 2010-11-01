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

from CIM14v13.IEC61970.Core.RegularIntervalSchedule import RegularIntervalSchedule

class DynamicSchedule(RegularIntervalSchedule):
    """A continuously variable component of a control area's active power net interchange schedule. Dynamic schedules are sent and received by control areas.
    """

    def __init__(self, dynSchedStatus='', dynSchedSignRev=False, Measurement=None, Receive_HostControlArea=None, Send_HostControlArea=None, *args, **kw_args):
        """Initializes a new 'DynamicSchedule' instance.

        @param dynSchedStatus: The 'active' or 'inactive' status of the dynamic schedule 
        @param dynSchedSignRev: Dynamic schedule sign reversal required (yes/no) 
        @param Measurement: A measurement is a data source for dynamic interchange schedules
        @param Receive_HostControlArea: A control area can receive dynamic schedules from other control areas
        @param Send_HostControlArea: A control area can send dynamic schedules to other control areas
        """
        #: The 'active' or 'inactive' status of the dynamic schedule 
        self.dynSchedStatus = dynSchedStatus

        #: Dynamic schedule sign reversal required (yes/no) 
        self.dynSchedSignRev = dynSchedSignRev

        self._Measurement = None
        self.Measurement = Measurement

        self._Receive_HostControlArea = None
        self.Receive_HostControlArea = Receive_HostControlArea

        self._Send_HostControlArea = None
        self.Send_HostControlArea = Send_HostControlArea

        super(DynamicSchedule, self).__init__(*args, **kw_args)

    def getMeasurement(self):
        """A measurement is a data source for dynamic interchange schedules
        """
        return self._Measurement

    def setMeasurement(self, value):
        if self._Measurement is not None:
            filtered = [x for x in self.Measurement.DynamicSchedules if x != self]
            self._Measurement._DynamicSchedules = filtered

        self._Measurement = value
        if self._Measurement is not None:
            self._Measurement._DynamicSchedules.append(self)

    Measurement = property(getMeasurement, setMeasurement)

    def getReceive_HostControlArea(self):
        """A control area can receive dynamic schedules from other control areas
        """
        return self._Receive_HostControlArea

    def setReceive_HostControlArea(self, value):
        if self._Receive_HostControlArea is not None:
            filtered = [x for x in self.Receive_HostControlArea.Receive_DynamicSchedules if x != self]
            self._Receive_HostControlArea._Receive_DynamicSchedules = filtered

        self._Receive_HostControlArea = value
        if self._Receive_HostControlArea is not None:
            self._Receive_HostControlArea._Receive_DynamicSchedules.append(self)

    Receive_HostControlArea = property(getReceive_HostControlArea, setReceive_HostControlArea)

    def getSend_HostControlArea(self):
        """A control area can send dynamic schedules to other control areas
        """
        return self._Send_HostControlArea

    def setSend_HostControlArea(self, value):
        if self._Send_HostControlArea is not None:
            filtered = [x for x in self.Send_HostControlArea.Send_DynamicSchedules if x != self]
            self._Send_HostControlArea._Send_DynamicSchedules = filtered

        self._Send_HostControlArea = value
        if self._Send_HostControlArea is not None:
            self._Send_HostControlArea._Send_DynamicSchedules.append(self)

    Send_HostControlArea = property(getSend_HostControlArea, setSend_HostControlArea)

