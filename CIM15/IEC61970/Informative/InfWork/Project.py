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

class Project(Document):
    """A collection of related work. For construction projects and maintenance projects, multiple phases may be performed.A collection of related work. For construction projects and maintenance projects, multiple phases may be performed.
    """

    def __init__(self, budget=0.0, BusinessCase=None, SubProjects=None, ErpProjectAccounting=None, Requests=None, Works=None, ParentProject=None, *args, **kw_args):
        """Initialises a new 'Project' instance.

        @param budget: Overall project budget. 
        @param BusinessCase:
        @param SubProjects:
        @param ErpProjectAccounting:
        @param Requests:
        @param Works:
        @param ParentProject:
        """
        #: Overall project budget.
        self.budget = budget

        self._BusinessCase = None
        self.BusinessCase = BusinessCase

        self._SubProjects = []
        self.SubProjects = [] if SubProjects is None else SubProjects

        self._ErpProjectAccounting = None
        self.ErpProjectAccounting = ErpProjectAccounting

        self._Requests = []
        self.Requests = [] if Requests is None else Requests

        self._Works = []
        self.Works = [] if Works is None else Works

        self._ParentProject = None
        self.ParentProject = ParentProject

        super(Project, self).__init__(*args, **kw_args)

    _attrs = ["budget"]
    _attr_types = {"budget": float}
    _defaults = {"budget": 0.0}
    _enums = {}
    _refs = ["BusinessCase", "SubProjects", "ErpProjectAccounting", "Requests", "Works", "ParentProject"]
    _many_refs = ["SubProjects", "Requests", "Works"]

    def getBusinessCase(self):
        
        return self._BusinessCase

    def setBusinessCase(self, value):
        if self._BusinessCase is not None:
            filtered = [x for x in self.BusinessCase.Projects if x != self]
            self._BusinessCase._Projects = filtered

        self._BusinessCase = value
        if self._BusinessCase is not None:
            if self not in self._BusinessCase._Projects:
                self._BusinessCase._Projects.append(self)

    BusinessCase = property(getBusinessCase, setBusinessCase)

    def getSubProjects(self):
        
        return self._SubProjects

    def setSubProjects(self, value):
        for x in self._SubProjects:
            x.ParentProject = None
        for y in value:
            y._ParentProject = self
        self._SubProjects = value

    SubProjects = property(getSubProjects, setSubProjects)

    def addSubProjects(self, *SubProjects):
        for obj in SubProjects:
            obj.ParentProject = self

    def removeSubProjects(self, *SubProjects):
        for obj in SubProjects:
            obj.ParentProject = None

    def getErpProjectAccounting(self):
        
        return self._ErpProjectAccounting

    def setErpProjectAccounting(self, value):
        if self._ErpProjectAccounting is not None:
            filtered = [x for x in self.ErpProjectAccounting.Projects if x != self]
            self._ErpProjectAccounting._Projects = filtered

        self._ErpProjectAccounting = value
        if self._ErpProjectAccounting is not None:
            if self not in self._ErpProjectAccounting._Projects:
                self._ErpProjectAccounting._Projects.append(self)

    ErpProjectAccounting = property(getErpProjectAccounting, setErpProjectAccounting)

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

    def getWorks(self):
        
        return self._Works

    def setWorks(self, value):
        for x in self._Works:
            x.Project = None
        for y in value:
            y._Project = self
        self._Works = value

    Works = property(getWorks, setWorks)

    def addWorks(self, *Works):
        for obj in Works:
            obj.Project = self

    def removeWorks(self, *Works):
        for obj in Works:
            obj.Project = None

    def getParentProject(self):
        
        return self._ParentProject

    def setParentProject(self, value):
        if self._ParentProject is not None:
            filtered = [x for x in self.ParentProject.SubProjects if x != self]
            self._ParentProject._SubProjects = filtered

        self._ParentProject = value
        if self._ParentProject is not None:
            if self not in self._ParentProject._SubProjects:
                self._ParentProject._SubProjects.append(self)

    ParentProject = property(getParentProject, setParentProject)

