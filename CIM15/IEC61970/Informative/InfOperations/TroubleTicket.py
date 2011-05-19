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

from CIM15.IEC61968.Common.Document import Document

class TroubleTicket(Document):
    """A document used to report electrical trouble. The trouble may either be an outage or non-outage problem, such as power quality. It must always be associated with an incident record. Note that a separate activity record is created for each call associated with an instance of trouble ticket. The time of a call is stored in 'ActivityRecord.createdOn' and comments are recorded in 'ActivityRecord.remarks'.A document used to report electrical trouble. The trouble may either be an outage or non-outage problem, such as power quality. It must always be associated with an incident record. Note that a separate activity record is created for each call associated with an instance of trouble ticket. The time of a call is stored in 'ActivityRecord.createdOn' and comments are recorded in 'ActivityRecord.remarks'.
    """

    def __init__(self, firstCallDateTime='', estimatedRestoreDateTime='', informBeforeRestored=False, reportingKind="email", priority='', informAfterRestored=False, advice='', hazardCode='', callBack=False, CallBacks=None, troublePeriod=None, CustomerData=None, IncidentRecord=None, *args, **kw_args):
        """Initialises a new 'TroubleTicket' instance.

        @param firstCallDateTime: Date and time trouble call first received. The date and time of subsequent calls by the same customer for the same trouble are recorded in associated Activity Records. 
        @param estimatedRestoreDateTime: Estimated restoration date and time last provided to the customer. 
        @param informBeforeRestored: True if person reporting trouble requested a call back when sigificant information became available about cause of the outage and the estimated restoration time. The person and their contact information are maintained in the assoicated Customer information. Call back results are recorded in assoicated 'ActivityRecord.Status.remarks'. 
        @param reportingKind: Means the customer used to report trouble (default is 'call'). Values are: "email", "call", "letter", "other"
        @param priority: Priority of trouble call. 
        @param informAfterRestored: True if person reporting trouble requested a call back to confirm power has been restored. The person and their contact information is maintained in the assoicated Customer informaiton. Call back results are recorded in assoicated 'ActivityRecord.Status.remarks'. 
        @param advice: True if advice already given to the customer at time when trouble was first reported. 
        @param hazardCode: Code for a reported hazard condition. 
        @param callBack: True if requested to customer when someone is about to arrive at their premises. 
        @param CallBacks:
        @param troublePeriod: Period between this source of trouble started and was resolved.
        @param CustomerData:
        @param IncidentRecord:
        """
        #: Date and time trouble call first received. The date and time of subsequent calls by the same customer for the same trouble are recorded in associated Activity Records.
        self.firstCallDateTime = firstCallDateTime

        #: Estimated restoration date and time last provided to the customer.
        self.estimatedRestoreDateTime = estimatedRestoreDateTime

        #: True if person reporting trouble requested a call back when sigificant information became available about cause of the outage and the estimated restoration time. The person and their contact information are maintained in the assoicated Customer information. Call back results are recorded in assoicated 'ActivityRecord.Status.remarks'.
        self.informBeforeRestored = informBeforeRestored

        #: Means the customer used to report trouble (default is 'call'). Values are: "email", "call", "letter", "other"
        self.reportingKind = reportingKind

        #: Priority of trouble call.
        self.priority = priority

        #: True if person reporting trouble requested a call back to confirm power has been restored. The person and their contact information is maintained in the assoicated Customer informaiton. Call back results are recorded in assoicated 'ActivityRecord.Status.remarks'.
        self.informAfterRestored = informAfterRestored

        #: True if advice already given to the customer at time when trouble was first reported.
        self.advice = advice

        #: Code for a reported hazard condition.
        self.hazardCode = hazardCode

        #: True if requested to customer when someone is about to arrive at their premises.
        self.callBack = callBack

        self._CallBacks = []
        self.CallBacks = [] if CallBacks is None else CallBacks

        self.troublePeriod = troublePeriod

        self._CustomerData = None
        self.CustomerData = CustomerData

        self._IncidentRecord = None
        self.IncidentRecord = IncidentRecord

        super(TroubleTicket, self).__init__(*args, **kw_args)

    _attrs = ["firstCallDateTime", "estimatedRestoreDateTime", "informBeforeRestored", "reportingKind", "priority", "informAfterRestored", "advice", "hazardCode", "callBack"]
    _attr_types = {"firstCallDateTime": str, "estimatedRestoreDateTime": str, "informBeforeRestored": bool, "reportingKind": str, "priority": str, "informAfterRestored": bool, "advice": str, "hazardCode": str, "callBack": bool}
    _defaults = {"firstCallDateTime": '', "estimatedRestoreDateTime": '', "informBeforeRestored": False, "reportingKind": "email", "priority": '', "informAfterRestored": False, "advice": '', "hazardCode": '', "callBack": False}
    _enums = {"reportingKind": "TroubleReportingKind"}
    _refs = ["CallBacks", "troublePeriod", "CustomerData", "IncidentRecord"]
    _many_refs = ["CallBacks"]

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

    # Period between this source of trouble started and was resolved.
    troublePeriod = None

    def getCustomerData(self):
        
        return self._CustomerData

    def setCustomerData(self, value):
        if self._CustomerData is not None:
            filtered = [x for x in self.CustomerData.TroubleTickets if x != self]
            self._CustomerData._TroubleTickets = filtered

        self._CustomerData = value
        if self._CustomerData is not None:
            if self not in self._CustomerData._TroubleTickets:
                self._CustomerData._TroubleTickets.append(self)

    CustomerData = property(getCustomerData, setCustomerData)

    def getIncidentRecord(self):
        
        return self._IncidentRecord

    def setIncidentRecord(self, value):
        if self._IncidentRecord is not None:
            filtered = [x for x in self.IncidentRecord.TroubleTickets if x != self]
            self._IncidentRecord._TroubleTickets = filtered

        self._IncidentRecord = value
        if self._IncidentRecord is not None:
            if self not in self._IncidentRecord._TroubleTickets:
                self._IncidentRecord._TroubleTickets.append(self)

    IncidentRecord = property(getIncidentRecord, setIncidentRecord)

