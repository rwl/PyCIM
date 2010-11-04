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

class Project(Document):
    """A collection of related work. For construction projects and maintenance projects, multiple phases may be performed.
    """

    def __init__(self, budget=0.0, ErpProjectAccounting=None, Works=None, BusinessCase=None, Requests=None, ParentProject=None, SubProjects=None, **kw_args):
        """Initializes a new 'Project' instance.

        @param budget: Overall project budget. 
        @param ErpProjectAccounting:
        @param Works:
        @param BusinessCase:
        @param Requests:
        @param ParentProject:
        @param SubProjects:
        """
        #: Overall project budget.
        self.budget = budget

        self._ErpProjectAccounting = None
        self.ErpProjectAccounting = ErpProjectAccounting

        self._Works = []
        self.Works = [] if Works is None else Works

        self._BusinessCase = None
        self.BusinessCase = BusinessCase

        self._Requests = []
        self.Requests = [] if Requests is None else Requests

        self._ParentProject = None
        self.ParentProject = ParentProject

        self._SubProjects = []
        self.SubProjects = [] if SubProjects is None else SubProjects

        super(Project, self).__init__(**kw_args)

    def getErpProjectAccounting(self):
        
        return self._ErpProjectAccounting

    def setErpProjectAccounting(self, value):
        if self._ErpProjectAccounting is not None:
            filtered = [x for x in self.ErpProjectAccounting.Projects if x != self]
            self._ErpProjectAccounting._Projects = filtered

        self._ErpProjectAccounting = value
        if self._ErpProjectAccounting is not None:
            self._ErpProjectAccounting._Projects.append(self)

    ErpProjectAccounting = property(getErpProjectAccounting, setErpProjectAccounting)

    def getWorks(self):
        
        return self._Works

    def setWorks(self, value):
        for x in self._Works:
            x._Project = None
        for y in value:
            y._Project = self
        self._Works = value

    Works = property(getWorks, setWorks)

    def addWorks(self, *Works):
        for obj in Works:
            obj._Project = self
            self._Works.append(obj)

    def removeWorks(self, *Works):
        for obj in Works:
            obj._Project = None
            self._Works.remove(obj)

    def getBusinessCase(self):
        
        return self._BusinessCase

    def setBusinessCase(self, value):
        if self._BusinessCase is not None:
            filtered = [x for x in self.BusinessCase.Projects if x != self]
            self._BusinessCase._Projects = filtered

        self._BusinessCase = value
        if self._BusinessCase is not None:
            self._BusinessCase._Projects.append(self)

    BusinessCase = property(getBusinessCase, setBusinessCase)

    def getRequests(self):
        
        return self._Requests

    def setRequests(self, value):
        for p in self._Requests:
            filtered = [q for q in p.Projects if q != self]
            self._Requests._Projects = filtered
        for r in value:
            if self not in r._Projects:
                r._Projects.append(self)
        self._Requests = value

    Requests = property(getRequests, setRequests)

    def addRequests(self, *Requests):
        for obj in Requests:
            if self not in obj._Projects:
                obj._Projects.append(self)
            self._Requests.append(obj)

    def removeRequests(self, *Requests):
        for obj in Requests:
            if self in obj._Projects:
                obj._Projects.remove(self)
            self._Requests.remove(obj)

    def getParentProject(self):
        
        return self._ParentProject

    def setParentProject(self, value):
        if self._ParentProject is not None:
            filtered = [x for x in self.ParentProject.SubProjects if x != self]
            self._ParentProject._SubProjects = filtered

        self._ParentProject = value
        if self._ParentProject is not None:
            self._ParentProject._SubProjects.append(self)

    ParentProject = property(getParentProject, setParentProject)

    def getSubProjects(self):
        
        return self._SubProjects

    def setSubProjects(self, value):
        for x in self._SubProjects:
            x._ParentProject = None
        for y in value:
            y._ParentProject = self
        self._SubProjects = value

    SubProjects = property(getSubProjects, setSubProjects)

    def addSubProjects(self, *SubProjects):
        for obj in SubProjects:
            obj._ParentProject = self
            self._SubProjects.append(obj)

    def removeSubProjects(self, *SubProjects):
        for obj in SubProjects:
            obj._ParentProject = None
            self._SubProjects.remove(obj)

