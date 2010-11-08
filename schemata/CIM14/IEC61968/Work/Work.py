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

from CIM14.IEC61968.Common.Document import Document

class Work(Document):
    """Document used to request, initiate, track and record work. This is synonymous with Work Breakdown Structure (WBS), which is traversed through the (currently informative) recursive association of Work. Note that the work name is equal to the WBS name, which is given in the inherited 'name' attribute.
    """

    def __init__(self, kind="construction", priority='', requestDateTime='', Customers=None, *args, **kw_args):
        """Initialises a new 'Work' instance.

        @param kind: Kind of work. Values are: "construction", "maintenance", "reconnect", "meter", "service", "disconnect", "inspection", "other"
        @param priority: Priority of work. 
        @param requestDateTime: Date and time work was requested. 
        @param Customers: All the customers for which this work is performed.
        """
        #: Kind of work. Values are: "construction", "maintenance", "reconnect", "meter", "service", "disconnect", "inspection", "other"
        self.kind = kind

        #: Priority of work.
        self.priority = priority

        #: Date and time work was requested.
        self.requestDateTime = requestDateTime

        self._Customers = []
        self.Customers = [] if Customers is None else Customers

        super(Work, self).__init__(*args, **kw_args)

    _attrs = ["kind", "priority", "requestDateTime"]
    _attr_types = {"kind": str, "priority": str, "requestDateTime": str}
    _defaults = {"kind": "construction", "priority": '', "requestDateTime": ''}
    _enums = {"kind": "WorkKind"}
    _refs = ["Customers"]
    _many_refs = ["Customers"]

    def getCustomers(self):
        """All the customers for which this work is performed.
        """
        return self._Customers

    def setCustomers(self, value):
        for p in self._Customers:
            filtered = [q for q in p.Works if q != self]
            self._Customers._Works = filtered
        for r in value:
            if self not in r._Works:
                r._Works.append(self)
        self._Customers = value

    Customers = property(getCustomers, setCustomers)

    def addCustomers(self, *Customers):
        for obj in Customers:
            if self not in obj._Works:
                obj._Works.append(self)
            self._Customers.append(obj)

    def removeCustomers(self, *Customers):
        for obj in Customers:
            if self in obj._Works:
                obj._Works.remove(self)
            self._Customers.remove(obj)

