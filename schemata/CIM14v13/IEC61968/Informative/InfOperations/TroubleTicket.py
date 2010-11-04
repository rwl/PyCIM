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

from CIM14v13.IEC61968.Common.Document import Document

class TroubleTicket(Document):
    """A document used to report electrical trouble. The trouble may either be an outage or non-outage problem, such as power quality. It must always be associated with an Incident Record. Note that a separate Activity Record is created for each call associated with an instance of Trouble Ticket. The time of a call is stored in ActivityRecord.createdOn and comments are recorded in ActivityRecord.remarks.
    """

    def __init__(self, reportingKind='letter', advice='', callBack=False, priority='', informAfterRestored=False, estimatedRestoreDateTime='', informBeforeRestored=False, hazardCode='', firstCallDateTime='', CustomerData=None, troublePeriod=None, CallBacks=None, IncidentRecord=None, *args, **kw_args):
        """Initializes a new 'TroubleTicket' instance.

        @param reportingKind: Means the customer used to report trouble (default is 'call'). Values are: "letter", "other", "call", "email"
        @param advice: Advice already given to the customer at time when trouble was first reported. 
        @param callBack: True if requested to customer when someone is about to arrive at their premises. 
        @param priority: Priority of trouble call. 
        @param informAfterRestored: True if person reporting trouble requested a call back to confirm power has been restored. The person and their contact information is maintained in the assoicated Customer informaiton. Call back results are recorded in assoicated 'ActivityRecord.Status.remarks'. 
        @param estimatedRestoreDateTime: Estimated restoration date and time last provided to the customer. 
        @param informBeforeRestored: True if person reporting trouble requested a call back when sigificant information became available about cause of the outage and the estimated restoration time. The person and their contact information are maintained in the assoicated Customer information. Call back results are recorded in assoicated 'ActivityRecord.Status.remarks'. 
        @param hazardCode: Code for a reported hazard condition. 
        @param firstCallDateTime: Date and time trouble call first received. The date and time of subsequent calls by the same customer for the same trouble are recorded in associated Activity Records. 
        @param CustomerData:
        @param troublePeriod: Period between this source of trouble started and was resolved.
        @param CallBacks:
        @param IncidentRecord:
        """
        #: Means the customer used to report trouble (default is 'call').Values are: "letter", "other", "call", "email"
        self.reportingKind = reportingKind

        #: Advice already given to the customer at time when trouble was first reported.
        self.advice = advice

        #: True if requested to customer when someone is about to arrive at their premises.
        self.callBack = callBack

        #: Priority of trouble call.
        self.priority = priority

        #: True if person reporting trouble requested a call back to confirm power has been restored. The person and their contact information is maintained in the assoicated Customer informaiton. Call back results are recorded in assoicated 'ActivityRecord.Status.remarks'.
        self.informAfterRestored = informAfterRestored

        #: Estimated restoration date and time last provided to the customer.
        self.estimatedRestoreDateTime = estimatedRestoreDateTime

        #: True if person reporting trouble requested a call back when sigificant information became available about cause of the outage and the estimated restoration time. The person and their contact information are maintained in the assoicated Customer information. Call back results are recorded in assoicated 'ActivityRecord.Status.remarks'.
        self.informBeforeRestored = informBeforeRestored

        #: Code for a reported hazard condition.
        self.hazardCode = hazardCode

        #: Date and time trouble call first received. The date and time of subsequent calls by the same customer for the same trouble are recorded in associated Activity Records.
        self.firstCallDateTime = firstCallDateTime

        self._CustomerData = None
        self.CustomerData = CustomerData

        self.troublePeriod = troublePeriod

        self._CallBacks = []
        self.CallBacks = [] if CallBacks is None else CallBacks

        self._IncidentRecord = None
        self.IncidentRecord = IncidentRecord

        super(TroubleTicket, self).__init__(*args, **kw_args)

    def getCustomerData(self):
        
        return self._CustomerData

    def setCustomerData(self, value):
        if self._CustomerData is not None:
            filtered = [x for x in self.CustomerData.TroubleTickets if x != self]
            self._CustomerData._TroubleTickets = filtered

        self._CustomerData = value
        if self._CustomerData is not None:
            self._CustomerData._TroubleTickets.append(self)

    CustomerData = property(getCustomerData, setCustomerData)

    # Period between this source of trouble started and was resolved.
    troublePeriod = None

    def getCallBacks(self):
        
        return self._CallBacks

    def setCallBacks(self, value):
        for p in self._CallBacks:
            filtered = [q for q in p.TroubleTickets if q != self]
            self._CallBacks._TroubleTickets = filtered
        for r in value:
            if self not in r._TroubleTickets:
                r._TroubleTickets.append(self)
        self._CallBacks = value

    CallBacks = property(getCallBacks, setCallBacks)

    def addCallBacks(self, *CallBacks):
        for obj in CallBacks:
            if self not in obj._TroubleTickets:
                obj._TroubleTickets.append(self)
            self._CallBacks.append(obj)

    def removeCallBacks(self, *CallBacks):
        for obj in CallBacks:
            if self in obj._TroubleTickets:
                obj._TroubleTickets.remove(self)
            self._CallBacks.remove(obj)

    def getIncidentRecord(self):
        
        return self._IncidentRecord

    def setIncidentRecord(self, value):
        if self._IncidentRecord is not None:
            filtered = [x for x in self.IncidentRecord.TroubleTickets if x != self]
            self._IncidentRecord._TroubleTickets = filtered

        self._IncidentRecord = value
        if self._IncidentRecord is not None:
            self._IncidentRecord._TroubleTickets.append(self)

    IncidentRecord = property(getIncidentRecord, setIncidentRecord)

