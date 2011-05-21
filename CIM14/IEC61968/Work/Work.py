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

