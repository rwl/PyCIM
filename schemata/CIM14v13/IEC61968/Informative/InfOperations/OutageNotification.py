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

class OutageNotification(Document):
    """A document containing information to be sent to customers notifying that an outage will take place. This is used to generate mailing lists for customers.
    """

    def __init__(self, duration=0.0, reason='', expectedInterruptionCount=0, CustomerDatas=None, *args, **kw_args):
        """Initializes a new 'OutageNotification' instance.

        @param duration: Likely duration of the interruption(s). 
        @param reason: Details of the outage 'reason'. 
        @param expectedInterruptionCount: Number of possible interruptions that the customer may expect for this event. 
        @param CustomerDatas:
        """
        #: Likely duration of the interruption(s).
        self.duration = duration

        #: Details of the outage 'reason'.
        self.reason = reason

        #: Number of possible interruptions that the customer may expect for this event.
        self.expectedInterruptionCount = expectedInterruptionCount

        self._CustomerDatas = []
        self.CustomerDatas = [] if CustomerDatas is None else CustomerDatas

        super(OutageNotification, self).__init__(*args, **kw_args)

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

