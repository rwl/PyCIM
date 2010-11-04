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

class CUGroup(IdentifiedObject):
    """A Compatible Unit Group identifies a set of compatible units which may be jointly utilized for estimating and designating jobs.
    """

    def __init__(self, ParentCUGroups=None, ChildCUGroups=None, DesignLocationCUs=None, status=None, CompatibleUnits=None, **kw_args):
        """Initializes a new 'CUGroup' instance.

        @param ParentCUGroups:
        @param ChildCUGroups:
        @param DesignLocationCUs:
        @param status:
        @param CompatibleUnits:
        """
        self._ParentCUGroups = []
        self.ParentCUGroups = [] if ParentCUGroups is None else ParentCUGroups

        self._ChildCUGroups = []
        self.ChildCUGroups = [] if ChildCUGroups is None else ChildCUGroups

        self._DesignLocationCUs = []
        self.DesignLocationCUs = [] if DesignLocationCUs is None else DesignLocationCUs

        self.status = status

        self._CompatibleUnits = []
        self.CompatibleUnits = [] if CompatibleUnits is None else CompatibleUnits

        super(CUGroup, self).__init__(**kw_args)

    def getParentCUGroups(self):
        
        return self._ParentCUGroups

    def setParentCUGroups(self, value):
        for p in self._ParentCUGroups:
            filtered = [q for q in p.ChildCUGroups if q != self]
            self._ParentCUGroups._ChildCUGroups = filtered
        for r in value:
            if self not in r._ChildCUGroups:
                r._ChildCUGroups.append(self)
        self._ParentCUGroups = value

    ParentCUGroups = property(getParentCUGroups, setParentCUGroups)

    def addParentCUGroups(self, *ParentCUGroups):
        for obj in ParentCUGroups:
            if self not in obj._ChildCUGroups:
                obj._ChildCUGroups.append(self)
            self._ParentCUGroups.append(obj)

    def removeParentCUGroups(self, *ParentCUGroups):
        for obj in ParentCUGroups:
            if self in obj._ChildCUGroups:
                obj._ChildCUGroups.remove(self)
            self._ParentCUGroups.remove(obj)

    def getChildCUGroups(self):
        
        return self._ChildCUGroups

    def setChildCUGroups(self, value):
        for p in self._ChildCUGroups:
            filtered = [q for q in p.ParentCUGroups if q != self]
            self._ChildCUGroups._ParentCUGroups = filtered
        for r in value:
            if self not in r._ParentCUGroups:
                r._ParentCUGroups.append(self)
        self._ChildCUGroups = value

    ChildCUGroups = property(getChildCUGroups, setChildCUGroups)

    def addChildCUGroups(self, *ChildCUGroups):
        for obj in ChildCUGroups:
            if self not in obj._ParentCUGroups:
                obj._ParentCUGroups.append(self)
            self._ChildCUGroups.append(obj)

    def removeChildCUGroups(self, *ChildCUGroups):
        for obj in ChildCUGroups:
            if self in obj._ParentCUGroups:
                obj._ParentCUGroups.remove(self)
            self._ChildCUGroups.remove(obj)

    def getDesignLocationCUs(self):
        
        return self._DesignLocationCUs

    def setDesignLocationCUs(self, value):
        for p in self._DesignLocationCUs:
            filtered = [q for q in p.CUGroups if q != self]
            self._DesignLocationCUs._CUGroups = filtered
        for r in value:
            if self not in r._CUGroups:
                r._CUGroups.append(self)
        self._DesignLocationCUs = value

    DesignLocationCUs = property(getDesignLocationCUs, setDesignLocationCUs)

    def addDesignLocationCUs(self, *DesignLocationCUs):
        for obj in DesignLocationCUs:
            if self not in obj._CUGroups:
                obj._CUGroups.append(self)
            self._DesignLocationCUs.append(obj)

    def removeDesignLocationCUs(self, *DesignLocationCUs):
        for obj in DesignLocationCUs:
            if self in obj._CUGroups:
                obj._CUGroups.remove(self)
            self._DesignLocationCUs.remove(obj)

    status = None

    def getCompatibleUnits(self):
        
        return self._CompatibleUnits

    def setCompatibleUnits(self, value):
        for x in self._CompatibleUnits:
            x._CUGroup = None
        for y in value:
            y._CUGroup = self
        self._CompatibleUnits = value

    CompatibleUnits = property(getCompatibleUnits, setCompatibleUnits)

    def addCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            obj._CUGroup = self
            self._CompatibleUnits.append(obj)

    def removeCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            obj._CUGroup = None
            self._CompatibleUnits.remove(obj)

