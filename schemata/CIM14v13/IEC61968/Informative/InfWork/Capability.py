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

class Capability(IdentifiedObject):
    """Capabilities of a crew.
    """

    def __init__(self, performanceFactor='', category='', Crew=None, status=None, WorkTasks=None, validityInterval=None, Crafts=None, **kw_args):
        """Initializes a new 'Capability' instance.

        @param performanceFactor: Capability performance factor. 
        @param category: Category by utility's work management standards and practices. 
        @param Crew:
        @param status:
        @param WorkTasks:
        @param validityInterval: Date and time interval for which this capability is valid (when it became effective and when it expires).
        @param Crafts:
        """
        #: Capability performance factor.
        self.performanceFactor = performanceFactor

        #: Category by utility's work management standards and practices.
        self.category = category

        self._Crew = None
        self.Crew = Crew

        self.status = status

        self._WorkTasks = []
        self.WorkTasks = [] if WorkTasks is None else WorkTasks

        self.validityInterval = validityInterval

        self._Crafts = []
        self.Crafts = [] if Crafts is None else Crafts

        super(Capability, self).__init__(**kw_args)

    def getCrew(self):
        
        return self._Crew

    def setCrew(self, value):
        if self._Crew is not None:
            filtered = [x for x in self.Crew.Capabilities if x != self]
            self._Crew._Capabilities = filtered

        self._Crew = value
        if self._Crew is not None:
            self._Crew._Capabilities.append(self)

    Crew = property(getCrew, setCrew)

    status = None

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

    # Date and time interval for which this capability is valid (when it became effective and when it expires).
    validityInterval = None

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

