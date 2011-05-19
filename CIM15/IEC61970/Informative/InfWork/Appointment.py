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

from CIM15.IEC61970.Informative.InfCommon.ScheduledEvent import ScheduledEvent

class Appointment(ScheduledEvent):
    """Meeting time and location.Meeting time and location.
    """

    def __init__(self, callAhead=False, remark='', address=None, ErpPersons=None, meetingInterval=None, CallBack=None, *args, **kw_args):
        """Initialises a new 'Appointment' instance.

        @param callAhead: True if requested to call customer when someone is about to arrive at their premises. 
        @param remark: Information about the appointment. 
        @param address: Address for appointment.
        @param ErpPersons:
        @param meetingInterval: Date and time reserved for appointment.
        @param CallBack:
        """
        #: True if requested to call customer when someone is about to arrive at their premises.
        self.callAhead = callAhead

        #: Information about the appointment.
        self.remark = remark

        self.address = address

        self._ErpPersons = []
        self.ErpPersons = [] if ErpPersons is None else ErpPersons

        self.meetingInterval = meetingInterval

        self._CallBack = None
        self.CallBack = CallBack

        super(Appointment, self).__init__(*args, **kw_args)

    _attrs = ["callAhead", "remark"]
    _attr_types = {"callAhead": bool, "remark": str}
    _defaults = {"callAhead": False, "remark": ''}
    _enums = {}
    _refs = ["address", "ErpPersons", "meetingInterval", "CallBack"]
    _many_refs = ["ErpPersons"]

    # Address for appointment.
    address = None

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

    # Date and time reserved for appointment.
    meetingInterval = None

    def getCallBack(self):
        
        return self._CallBack

    def setCallBack(self, value):
        if self._CallBack is not None:
            filtered = [x for x in self.CallBack.Appointments if x != self]
            self._CallBack._Appointments = filtered

        self._CallBack = value
        if self._CallBack is not None:
            if self not in self._CallBack._Appointments:
                self._CallBack._Appointments.append(self)

    CallBack = property(getCallBack, setCallBack)

