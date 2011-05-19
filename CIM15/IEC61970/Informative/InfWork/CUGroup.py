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

class CUGroup(IdentifiedObject):
    """A Compatible Unit Group identifies a set of compatible units which may be jointly utilized for estimating and designating jobs.A Compatible Unit Group identifies a set of compatible units which may be jointly utilized for estimating and designating jobs.
    """

    def __init__(self, CompatibleUnits=None, ParentCUGroups=None, ChildCUGroups=None, status=None, DesignLocationCUs=None, *args, **kw_args):
        """Initialises a new 'CUGroup' instance.

        @param CompatibleUnits:
        @param ParentCUGroups:
        @param ChildCUGroups:
        @param status:
        @param DesignLocationCUs:
        """
        self._CompatibleUnits = []
        self.CompatibleUnits = [] if CompatibleUnits is None else CompatibleUnits

        self._ParentCUGroups = []
        self.ParentCUGroups = [] if ParentCUGroups is None else ParentCUGroups

        self._ChildCUGroups = []
        self.ChildCUGroups = [] if ChildCUGroups is None else ChildCUGroups

        self.status = status

        self._DesignLocationCUs = []
        self.DesignLocationCUs = [] if DesignLocationCUs is None else DesignLocationCUs

        super(CUGroup, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["CompatibleUnits", "ParentCUGroups", "ChildCUGroups", "status", "DesignLocationCUs"]
    _many_refs = ["CompatibleUnits", "ParentCUGroups", "ChildCUGroups", "DesignLocationCUs"]

    def getCompatibleUnits(self):
        
        return self._CompatibleUnits

    def setCompatibleUnits(self, value):
        for x in self._CompatibleUnits:
            x.CUGroup = None
        for y in value:
            y._CUGroup = self
        self._CompatibleUnits = value

    CompatibleUnits = property(getCompatibleUnits, setCompatibleUnits)

    def addCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            obj.CUGroup = self

    def removeCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            obj.CUGroup = None

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

    status = None

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

