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

class Capability(IdentifiedObject):
    """Capabilities of a crew.Capabilities of a crew.
    """

    def __init__(self, category='', performanceFactor='', Crew=None, WorkTasks=None, status=None, Crafts=None, validityInterval=None, *args, **kw_args):
        """Initialises a new 'Capability' instance.

        @param category: Category by utility's work management standards and practices. 
        @param performanceFactor: Capability performance factor. 
        @param Crew:
        @param WorkTasks:
        @param status:
        @param Crafts:
        @param validityInterval: Date and time interval for which this capability is valid (when it became effective and when it expires).
        """
        #: Category by utility's work management standards and practices.
        self.category = category

        #: Capability performance factor.
        self.performanceFactor = performanceFactor

        self._Crew = None
        self.Crew = Crew

        self._WorkTasks = []
        self.WorkTasks = [] if WorkTasks is None else WorkTasks

        self.status = status

        self._Crafts = []
        self.Crafts = [] if Crafts is None else Crafts

        self.validityInterval = validityInterval

        super(Capability, self).__init__(*args, **kw_args)

    _attrs = ["category", "performanceFactor"]
    _attr_types = {"category": str, "performanceFactor": str}
    _defaults = {"category": '', "performanceFactor": ''}
    _enums = {}
    _refs = ["Crew", "WorkTasks", "status", "Crafts", "validityInterval"]
    _many_refs = ["WorkTasks", "Crafts"]

    def getCrew(self):
        
        return self._Crew

    def setCrew(self, value):
        if self._Crew is not None:
            filtered = [x for x in self.Crew.Capabilities if x != self]
            self._Crew._Capabilities = filtered

        self._Crew = value
        if self._Crew is not None:
            if self not in self._Crew._Capabilities:
                self._Crew._Capabilities.append(self)

    Crew = property(getCrew, setCrew)

    def getWorkTasks(self):
        
        return self._WorkTasks

    def setWorkTasks(self, value):
        for p in self._WorkTasks:
            filtered = [q for q in p.Capabilities if q != self]
            self._WorkTasks._Capabilities = filtered
        for r in value:
            if self not in r._Capabilities:
                r._Capabilities.append(self)
        self._WorkTasks = value

    WorkTasks = property(getWorkTasks, setWorkTasks)

    def addWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            if self not in obj._Capabilities:
                obj._Capabilities.append(self)
            self._WorkTasks.append(obj)

    def removeWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            if self in obj._Capabilities:
                obj._Capabilities.remove(self)
            self._WorkTasks.remove(obj)

    status = None

    def getCrafts(self):
        
        return self._Crafts

    def setCrafts(self, value):
        for p in self._Crafts:
            filtered = [q for q in p.Capabilities if q != self]
            self._Crafts._Capabilities = filtered
        for r in value:
            if self not in r._Capabilities:
                r._Capabilities.append(self)
        self._Crafts = value

    Crafts = property(getCrafts, setCrafts)

    def addCrafts(self, *Crafts):
        for obj in Crafts:
            if self not in obj._Capabilities:
                obj._Capabilities.append(self)
            self._Crafts.append(obj)

    def removeCrafts(self, *Crafts):
        for obj in Crafts:
            if self in obj._Capabilities:
                obj._Capabilities.remove(self)
            self._Crafts.remove(obj)

    # Date and time interval for which this capability is valid (when it became effective and when it expires).
    validityInterval = None

