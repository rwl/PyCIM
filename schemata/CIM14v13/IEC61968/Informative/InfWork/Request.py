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

class Request(Document):
    """A request for work, service or project.
    """

    def __init__(self, corporateCode='', priority='', actionNeeded='', Organisation=None, Projects=None, ErpQuoteLineItem=None, Works=None, *args, **kw_args):
        """Initializes a new 'Request' instance.

        @param corporateCode: The corporate code for this request. 
        @param priority: The priority of this request. 
        @param actionNeeded: Based on the current 'Status.status', the action that is needed before this Request can transition to the desired state, such as initiating the requested Work. For example, missing or additionally needed information may be required from the requesting organisation before a work Design may be created. 
        @param Organisation:
        @param Projects:
        @param ErpQuoteLineItem:
        @param Works:
        """
        #: The corporate code for this request. 
        self.corporateCode = corporateCode

        #: The priority of this request. 
        self.priority = priority

        #: Based on the current 'Status.status', the action that is needed before this Request can transition to the desired state, such as initiating the requested Work. For example, missing or additionally needed information may be required from the requesting organisation before a work Design may be created. 
        self.actionNeeded = actionNeeded

        self._Organisation = None
        self.Organisation = Organisation

        self._Projects = []
        self.Projects = [] if Projects is None else Projects

        self._ErpQuoteLineItem = None
        self.ErpQuoteLineItem = ErpQuoteLineItem

        self._Works = []
        self.Works = [] if Works is None else Works

        super(Request, self).__init__(*args, **kw_args)

    def getOrganisation(self):
        
        return self._Organisation

    def setOrganisation(self, value):
        if self._Organisation is not None:
            filtered = [x for x in self.Organisation.Requests if x != self]
            self._Organisation._Requests = filtered

        self._Organisation = value
        if self._Organisation is not None:
            self._Organisation._Requests.append(self)

    Organisation = property(getOrganisation, setOrganisation)

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

    def getErpQuoteLineItem(self):
        
        return self._ErpQuoteLineItem

    def setErpQuoteLineItem(self, value):
        if self._ErpQuoteLineItem is not None:
            self._ErpQuoteLineItem._Request = None

        self._ErpQuoteLineItem = value
        if self._ErpQuoteLineItem is not None:
            self._ErpQuoteLineItem._Request = self

    ErpQuoteLineItem = property(getErpQuoteLineItem, setErpQuoteLineItem)

    def getWorks(self):
        
        return self._Works

    def setWorks(self, value):
        for x in self._Works:
            x._Request = None
        for y in value:
            y._Request = self
        self._Works = value

    Works = property(getWorks, setWorks)

    def addWorks(self, *Works):
        for obj in Works:
            obj._Request = self
            self._Works.append(obj)

    def removeWorks(self, *Works):
        for obj in Works:
            obj._Request = None
            self._Works.remove(obj)

