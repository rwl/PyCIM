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

class Request(Document):
    """A request for work, service or project.A request for work, service or project.
    """

    def __init__(self, actionNeeded='', priority='', corporateCode='', ErpQuoteLineItem=None, Projects=None, Organisation=None, Works=None, *args, **kw_args):
        """Initialises a new 'Request' instance.

        @param actionNeeded: Based on the current 'Status.status', the action that is needed before this Request can transition to the desired state, such as initiating the requested Work. For example, missing or additionally needed information may be required from the requesting organisation before a work Design may be created. 
        @param priority: The priority of this request. 
        @param corporateCode: The corporate code for this request. 
        @param ErpQuoteLineItem:
        @param Projects:
        @param Organisation:
        @param Works:
        """
        #: Based on the current 'Status.status', the action that is needed before this Request can transition to the desired state, such as initiating the requested Work. For example, missing or additionally needed information may be required from the requesting organisation before a work Design may be created.
        self.actionNeeded = actionNeeded

        #: The priority of this request.
        self.priority = priority

        #: The corporate code for this request.
        self.corporateCode = corporateCode

        self._ErpQuoteLineItem = None
        self.ErpQuoteLineItem = ErpQuoteLineItem

        self._Projects = []
        self.Projects = [] if Projects is None else Projects

        self._Organisation = None
        self.Organisation = Organisation

        self._Works = []
        self.Works = [] if Works is None else Works

        super(Request, self).__init__(*args, **kw_args)

    _attrs = ["actionNeeded", "priority", "corporateCode"]
    _attr_types = {"actionNeeded": str, "priority": str, "corporateCode": str}
    _defaults = {"actionNeeded": '', "priority": '', "corporateCode": ''}
    _enums = {}
    _refs = ["ErpQuoteLineItem", "Projects", "Organisation", "Works"]
    _many_refs = ["Projects", "Works"]

    def getErpQuoteLineItem(self):
        
        return self._ErpQuoteLineItem

    def setErpQuoteLineItem(self, value):
        if self._ErpQuoteLineItem is not None:
            self._ErpQuoteLineItem._Request = None

        self._ErpQuoteLineItem = value
        if self._ErpQuoteLineItem is not None:
            self._ErpQuoteLineItem.Request = None
            self._ErpQuoteLineItem._Request = self

    ErpQuoteLineItem = property(getErpQuoteLineItem, setErpQuoteLineItem)

    def getProjects(self):
        
        return self._Projects

    def setProjects(self, value):
        for p in self._Projects:
            filtered = [q for q in p.Requests if q != self]
            self._Projects._Requests = filtered
        for r in value:
            if self not in r._Requests:
                r._Requests.append(self)
        self._Projects = value

    Projects = property(getProjects, setProjects)

    def addProjects(self, *Projects):
        for obj in Projects:
            if self not in obj._Requests:
                obj._Requests.append(self)
            self._Projects.append(obj)

    def removeProjects(self, *Projects):
        for obj in Projects:
            if self in obj._Requests:
                obj._Requests.remove(self)
            self._Projects.remove(obj)

    def getOrganisation(self):
        
        return self._Organisation

    def setOrganisation(self, value):
        if self._Organisation is not None:
            filtered = [x for x in self.Organisation.Requests if x != self]
            self._Organisation._Requests = filtered

        self._Organisation = value
        if self._Organisation is not None:
            if self not in self._Organisation._Requests:
                self._Organisation._Requests.append(self)

    Organisation = property(getOrganisation, setOrganisation)

    def getWorks(self):
        
        return self._Works

    def setWorks(self, value):
        for x in self._Works:
            x.Request = None
        for y in value:
            y._Request = self
        self._Works = value

    Works = property(getWorks, setWorks)

    def addWorks(self, *Works):
        for obj in Works:
            obj.Request = self

    def removeWorks(self, *Works):
        for obj in Works:
            obj.Request = None

