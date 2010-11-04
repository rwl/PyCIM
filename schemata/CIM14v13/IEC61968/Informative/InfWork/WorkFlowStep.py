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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class WorkFlowStep(IdentifiedObject):
    """A pre-defined set of work steps for a given type of work.
    """

    def __init__(self, sequenceNumber=0, Work=None, WorkTasks=None, status=None, **kw_args):
        """Initializes a new 'WorkFlowStep' instance.

        @param sequenceNumber: Used to define dependencies of each work flow step, which is for the instance of WorkTask associated with a given instance of WorkFlow. 
        @param Work:
        @param WorkTasks:
        @param status:
        """
        #: Used to define dependencies of each work flow step, which is for the instance of WorkTask associated with a given instance of WorkFlow.
        self.sequenceNumber = sequenceNumber

        self._Work = None
        self.Work = Work

        self._WorkTasks = []
        self.WorkTasks = [] if WorkTasks is None else WorkTasks

        self.status = status

        super(WorkFlowStep, self).__init__(**kw_args)

    def getWork(self):
        
        return self._Work

    def setWork(self, value):
        if self._Work is not None:
            filtered = [x for x in self.Work.WorkFlowSteps if x != self]
            self._Work._WorkFlowSteps = filtered

        self._Work = value
        if self._Work is not None:
            self._Work._WorkFlowSteps.append(self)

    Work = property(getWork, setWork)

    def getWorkTasks(self):
        
        return self._WorkTasks

    def setWorkTasks(self, value):
        for x in self._WorkTasks:
            x._WorkFlowStep = None
        for y in value:
            y._WorkFlowStep = self
        self._WorkTasks = value

    WorkTasks = property(getWorkTasks, setWorkTasks)

    def addWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            obj._WorkFlowStep = self
            self._WorkTasks.append(obj)

    def removeWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            obj._WorkFlowStep = None
            self._WorkTasks.remove(obj)

    status = None

