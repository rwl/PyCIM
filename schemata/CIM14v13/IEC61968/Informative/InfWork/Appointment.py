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

from CIM14v13.IEC61968.Informative.InfCommon.ScheduledEvent import ScheduledEvent

class Appointment(ScheduledEvent):
    """Meeting time and location.
    """

    def __init__(self, remark='', callAhead=False, ErpPersons=None, CallBack=None, address=None, meetingInterval=None, **kw_args):
        """Initializes a new 'Appointment' instance.

        @param remark: Information about the appointment. 
        @param callAhead: True if requested to call customer when someone is about to arrive at their premises. 
        @param ErpPersons:
        @param CallBack:
        @param address: Address for appointment.
        @param meetingInterval: Date and time reserved for appointment.
        """
        #: Information about the appointment.
        self.remark = remark

        #: True if requested to call customer when someone is about to arrive at their premises.
        self.callAhead = callAhead

        self._ErpPersons = []
        self.ErpPersons = [] if ErpPersons is None else ErpPersons

        self._CallBack = None
        self.CallBack = CallBack

        self.address = address

        self.meetingInterval = meetingInterval

        super(Appointment, self).__init__(**kw_args)

    def getErpPersons(self):
        
        return self._ErpPersons

    def setErpPersons(self, value):
        for p in self._ErpPersons:
            filtered = [q for q in p.Appointments if q != self]
            self._ErpPersons._Appointments = filtered
        for r in value:
            if self not in r._Appointments:
                r._Appointments.append(self)
        self._ErpPersons = value

    ErpPersons = property(getErpPersons, setErpPersons)

    def addErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            if self not in obj._Appointments:
                obj._Appointments.append(self)
            self._ErpPersons.append(obj)

    def removeErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            if self in obj._Appointments:
                obj._Appointments.remove(self)
            self._ErpPersons.remove(obj)

    def getCallBack(self):
        
        return self._CallBack

    def setCallBack(self, value):
        if self._CallBack is not None:
            filtered = [x for x in self.CallBack.Appointments if x != self]
            self._CallBack._Appointments = filtered

        self._CallBack = value
        if self._CallBack is not None:
            self._CallBack._Appointments.append(self)

    CallBack = property(getCallBack, setCallBack)

    # Address for appointment.
    address = None

    # Date and time reserved for appointment.
    meetingInterval = None

