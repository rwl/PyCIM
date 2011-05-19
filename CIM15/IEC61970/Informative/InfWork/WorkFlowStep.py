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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class WorkFlowStep(IdentifiedObject):
    """A pre-defined set of work steps for a given type of work.A pre-defined set of work steps for a given type of work.
    """

    def __init__(self, sequenceNumber=0, WorkTasks=None, status=None, Work=None, *args, **kw_args):
        """Initialises a new 'WorkFlowStep' instance.

        @param sequenceNumber: Used to define dependencies of each work flow step, which is for the instance of WorkTask associated with a given instance of WorkFlow. 
        @param WorkTasks:
        @param status:
        @param Work:
        """
        #: Used to define dependencies of each work flow step, which is for the instance of WorkTask associated with a given instance of WorkFlow.
        self.sequenceNumber = sequenceNumber

        self._WorkTasks = []
        self.WorkTasks = [] if WorkTasks is None else WorkTasks

        self.status = status

        self._Work = None
        self.Work = Work

        super(WorkFlowStep, self).__init__(*args, **kw_args)

    _attrs = ["sequenceNumber"]
    _attr_types = {"sequenceNumber": int}
    _defaults = {"sequenceNumber": 0}
    _enums = {}
    _refs = ["WorkTasks", "status", "Work"]
    _many_refs = ["WorkTasks"]

    def getWorkTasks(self):
        
        return self._WorkTasks

    def setWorkTasks(self, value):
        for x in self._WorkTasks:
            x.WorkFlowStep = None
        for y in value:
            y._WorkFlowStep = self
        self._WorkTasks = value

    WorkTasks = property(getWorkTasks, setWorkTasks)

    def addWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            obj.WorkFlowStep = self

    def removeWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            obj.WorkFlowStep = None

    status = None

    def getWork(self):
        
        return self._Work

    def setWork(self, value):
        if self._Work is not None:
            filtered = [x for x in self.Work.WorkFlowSteps if x != self]
            self._Work._WorkFlowSteps = filtered

        self._Work = value
        if self._Work is not None:
            if self not in self._Work._WorkFlowSteps:
                self._Work._WorkFlowSteps.append(self)

    Work = property(getWork, setWork)

