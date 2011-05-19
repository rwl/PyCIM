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

class OutageNotification(Document):
    """A document containing information to be sent to customers notifying that an outage will take place. This is used to generate mailing lists for customers.A document containing information to be sent to customers notifying that an outage will take place. This is used to generate mailing lists for customers.
    """

    def __init__(self, expectedInterruptionCount=0, duration=0.0, reason='', CustomerDatas=None, *args, **kw_args):
        """Initialises a new 'OutageNotification' instance.

        @param expectedInterruptionCount: Number of possible interruptions that the customer may expect for this event. 
        @param duration: Likely duration of the interruption(s). 
        @param reason: Details of the outage 'reason'. 
        @param CustomerDatas:
        """
        #: Number of possible interruptions that the customer may expect for this event.
        self.expectedInterruptionCount = expectedInterruptionCount

        #: Likely duration of the interruption(s).
        self.duration = duration

        #: Details of the outage 'reason'.
        self.reason = reason

        self._CustomerDatas = []
        self.CustomerDatas = [] if CustomerDatas is None else CustomerDatas

        super(OutageNotification, self).__init__(*args, **kw_args)

    _attrs = ["expectedInterruptionCount", "duration", "reason"]
    _attr_types = {"expectedInterruptionCount": int, "duration": float, "reason": str}
    _defaults = {"expectedInterruptionCount": 0, "duration": 0.0, "reason": ''}
    _enums = {}
    _refs = ["CustomerDatas"]
    _many_refs = ["CustomerDatas"]

    def getCustomerDatas(self):
        
        return self._CustomerDatas

    def setCustomerDatas(self, value):
        for p in self._CustomerDatas:
            filtered = [q for q in p.OutageNotifications if q != self]
            self._CustomerDatas._OutageNotifications = filtered
        for r in value:
            if self not in r._OutageNotifications:
                r._OutageNotifications.append(self)
        self._CustomerDatas = value

    CustomerDatas = property(getCustomerDatas, setCustomerDatas)

    def addCustomerDatas(self, *CustomerDatas):
        for obj in CustomerDatas:
            if self not in obj._OutageNotifications:
                obj._OutageNotifications.append(self)
            self._CustomerDatas.append(obj)

    def removeCustomerDatas(self, *CustomerDatas):
        for obj in CustomerDatas:
            if self in obj._OutageNotifications:
                obj._OutageNotifications.remove(self)
            self._CustomerDatas.remove(obj)

