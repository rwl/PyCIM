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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class CallBack(IdentifiedObject):
    """Information about a planned CallBack or a CallBack that has occurred, from the utility to a customer regarding the status and plans about resolving trouble, performing work, etc.Information about a planned CallBack or a CallBack that has occurred, from the utility to a customer regarding the status and plans about resolving trouble, performing work, etc.
    """

    def __init__(self, dateTime='', comment='', advice='', contactDetail='', problemInfo='', Appointments=None, ErpPersons=None, TroubleTickets=None, status=None, *args, **kw_args):
        """Initialises a new 'CallBack' instance.

        @param dateTime: (if callback already occured) Date and time when this call back occurred. 
        @param comment: Comments by customer during this call back. 
        @param advice: Advice already given to the customer during this call back. 
        @param contactDetail: Additional contact details that are not provided for ErpPerson with ErpTelephoneNumber. 
        @param problemInfo: Descriptiion of the problem reported during this call back. 
        @param Appointments:
        @param ErpPersons:
        @param TroubleTickets:
        @param status:
        """
        #: (if callback already occured) Date and time when this call back occurred.
        self.dateTime = dateTime

        #: Comments by customer during this call back.
        self.comment = comment

        #: Advice already given to the customer during this call back.
        self.advice = advice

        #: Additional contact details that are not provided for ErpPerson with ErpTelephoneNumber.
        self.contactDetail = contactDetail

        #: Descriptiion of the problem reported during this call back.
        self.problemInfo = problemInfo

        self._Appointments = []
        self.Appointments = [] if Appointments is None else Appointments

        self._ErpPersons = []
        self.ErpPersons = [] if ErpPersons is None else ErpPersons

        self._TroubleTickets = []
        self.TroubleTickets = [] if TroubleTickets is None else TroubleTickets

        self.status = status

        super(CallBack, self).__init__(*args, **kw_args)

    _attrs = ["dateTime", "comment", "advice", "contactDetail", "problemInfo"]
    _attr_types = {"dateTime": str, "comment": str, "advice": str, "contactDetail": str, "problemInfo": str}
    _defaults = {"dateTime": '', "comment": '', "advice": '', "contactDetail": '', "problemInfo": ''}
    _enums = {}
    _refs = ["Appointments", "ErpPersons", "TroubleTickets", "status"]
    _many_refs = ["Appointments", "ErpPersons", "TroubleTickets"]

    def getAppointments(self):
        
        return self._Appointments

    def setAppointments(self, value):
        for x in self._Appointments:
            x.CallBack = None
        for y in value:
            y._CallBack = self
        self._Appointments = value

    Appointments = property(getAppointments, setAppointments)

    def addAppointments(self, *Appointments):
        for obj in Appointments:
            obj.CallBack = self

    def removeAppointments(self, *Appointments):
        for obj in Appointments:
            obj.CallBack = None

    def getErpPersons(self):
        
        return self._ErpPersons

    def setErpPersons(self, value):
        for p in self._ErpPersons:
            filtered = [q for q in p.CallBacks if q != self]
            self._ErpPersons._CallBacks = filtered
        for r in value:
            if self not in r._CallBacks:
                r._CallBacks.append(self)
        self._ErpPersons = value

    ErpPersons = property(getErpPersons, setErpPersons)

    def addErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            if self not in obj._CallBacks:
                obj._CallBacks.append(self)
            self._ErpPersons.append(obj)

    def removeErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            if self in obj._CallBacks:
                obj._CallBacks.remove(self)
            self._ErpPersons.remove(obj)

    def getTroubleTickets(self):
        
        return self._TroubleTickets

    def setTroubleTickets(self, value):
        for p in self._TroubleTickets:
            filtered = [q for q in p.CallBacks if q != self]
            self._TroubleTickets._CallBacks = filtered
        for r in value:
            if self not in r._CallBacks:
                r._CallBacks.append(self)
        self._TroubleTickets = value

    TroubleTickets = property(getTroubleTickets, setTroubleTickets)

    def addTroubleTickets(self, *TroubleTickets):
        for obj in TroubleTickets:
            if self not in obj._CallBacks:
                obj._CallBacks.append(self)
            self._TroubleTickets.append(obj)

    def removeTroubleTickets(self, *TroubleTickets):
        for obj in TroubleTickets:
            if self in obj._CallBacks:
                obj._CallBacks.remove(self)
            self._TroubleTickets.remove(obj)

    status = None

