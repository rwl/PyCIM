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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class CallBack(IdentifiedObject):
    """Information about a planned CallBack or a CallBack that has occurred, from the utility to a customer regarding the status and plans about resolving trouble, performing work, etc.
    """

    def __init__(self, advice='', contactDetail='', comment='', problemInfo='', dateTime='', ErpPersons=None, Appointments=None, status=None, TroubleTickets=None, *args, **kw_args):
        """Initializes a new 'CallBack' instance.

        @param advice: Advice already given to the customer during this call back. 
        @param contactDetail: Additional contact details that are not provided for ErpPerson with ErpTelephoneNumber. 
        @param comment: Comments by customer during this call back. 
        @param problemInfo: Descriptiion of the problem reported during this call back. 
        @param dateTime: (if callback already occured) Date and time when this call back occurred. 
        @param ErpPersons:
        @param Appointments:
        @param status:
        @param TroubleTickets:
        """
        #: Advice already given to the customer during this call back. 
        self.advice = advice

        #: Additional contact details that are not provided for ErpPerson with ErpTelephoneNumber. 
        self.contactDetail = contactDetail

        #: Comments by customer during this call back. 
        self.comment = comment

        #: Descriptiion of the problem reported during this call back. 
        self.problemInfo = problemInfo

        #: (if callback already occured) Date and time when this call back occurred. 
        self.dateTime = dateTime

        self._ErpPersons = []
        self.ErpPersons = [] if ErpPersons is None else ErpPersons

        self._Appointments = []
        self.Appointments = [] if Appointments is None else Appointments

        self.status = status

        self._TroubleTickets = []
        self.TroubleTickets = [] if TroubleTickets is None else TroubleTickets

        super(CallBack, self).__init__(*args, **kw_args)

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

    def getAppointments(self):
        
        return self._Appointments

    def setAppointments(self, value):
        for x in self._Appointments:
            x._CallBack = None
        for y in value:
            y._CallBack = self
        self._Appointments = value

    Appointments = property(getAppointments, setAppointments)

    def addAppointments(self, *Appointments):
        for obj in Appointments:
            obj._CallBack = self
            self._Appointments.append(obj)

    def removeAppointments(self, *Appointments):
        for obj in Appointments:
            obj._CallBack = None
            self._Appointments.remove(obj)

    status = None

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

