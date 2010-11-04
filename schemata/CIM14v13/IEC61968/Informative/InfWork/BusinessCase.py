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

class BusinessCase(Document):
    """Business justification for capital expenditures, usually addressing operations and maintenance costs as well.
    """

    def __init__(self, corporateCode='', Works=None, Projects=None, **kw_args):
        """Initializes a new 'BusinessCase' instance.

        @param corporateCode: A codified representation of the business case (i.e., codes for highway relocation, replace substation transformers, etc.). 
        @param Works:
        @param Projects:
        """
        #: A codified representation of the business case (i.e., codes for highway relocation, replace substation transformers, etc.).
        self.corporateCode = corporateCode

        self._Works = []
        self.Works = [] if Works is None else Works

        self._Projects = []
        self.Projects = [] if Projects is None else Projects

        super(BusinessCase, self).__init__(**kw_args)

    def getWorks(self):
        
        return self._Works

    def setWorks(self, value):
        for x in self._Works:
            x._BusinessCase = None
        for y in value:
            y._BusinessCase = self
        self._Works = value

    Works = property(getWorks, setWorks)

    def addWorks(self, *Works):
        for obj in Works:
            obj._BusinessCase = self
            self._Works.append(obj)

    def removeWorks(self, *Works):
        for obj in Works:
            obj._BusinessCase = None
            self._Works.remove(obj)

    def getProjects(self):
        
        return self._Projects

    def setProjects(self, value):
        for x in self._Projects:
            x._BusinessCase = None
        for y in value:
            y._BusinessCase = self
        self._Projects = value

    Projects = property(getProjects, setProjects)

    def addProjects(self, *Projects):
        for obj in Projects:
            obj._BusinessCase = self
            self._Projects.append(obj)

    def removeProjects(self, *Projects):
        for obj in Projects:
            obj._BusinessCase = None
            self._Projects.remove(obj)

