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

class DesignLocationCU(IdentifiedObject):
    """Compatible unit at a given design location.Compatible unit at a given design location.
    """

    def __init__(self, energizationFlag=False, cuUsage='', removalDate='', cuAction="install", cuAccount='', cuQuantity="", ConditionFactors=None, CompatibleUnits=None, WorkTasks=None, Designs=None, CUGroups=None, DesignLocation=None, status=None, *args, **kw_args):
        """Initialises a new 'DesignLocationCU' instance.

        @param energizationFlag: True if associated electrical equipment is intended to be energized while work is being performed. 
        @param cuUsage: As the same CU can be used for different purposes and accounting purposes, usage must be specified. Examples include: distribution, transmission, substation. 
        @param removalDate: Year when a CU that represents an asset is removed. 
        @param cuAction: A code that instructs the crew what action to perform. Values are: "install", "remove", "transfer", "abandon"
        @param cuAccount: A code that helps direct accounting (capital, expense, or accounting treatment). 
        @param cuQuantity: The quantity of the CU being assigned to this location. 
        @param ConditionFactors:
        @param CompatibleUnits:
        @param WorkTasks:
        @param Designs:
        @param CUGroups:
        @param DesignLocation:
        @param status:
        """
        #: True if associated electrical equipment is intended to be energized while work is being performed.
        self.energizationFlag = energizationFlag

        #: As the same CU can be used for different purposes and accounting purposes, usage must be specified. Examples include: distribution, transmission, substation.
        self.cuUsage = cuUsage

        #: Year when a CU that represents an asset is removed.
        self.removalDate = removalDate

        #: A code that instructs the crew what action to perform. Values are: "install", "remove", "transfer", "abandon"
        self.cuAction = cuAction

        #: A code that helps direct accounting (capital, expense, or accounting treatment).
        self.cuAccount = cuAccount

        #: The quantity of the CU being assigned to this location.
        self.cuQuantity = cuQuantity

        self._ConditionFactors = []
        self.ConditionFactors = [] if ConditionFactors is None else ConditionFactors

        self._CompatibleUnits = []
        self.CompatibleUnits = [] if CompatibleUnits is None else CompatibleUnits

        self._WorkTasks = []
        self.WorkTasks = [] if WorkTasks is None else WorkTasks

        self._Designs = []
        self.Designs = [] if Designs is None else Designs

        self._CUGroups = []
        self.CUGroups = [] if CUGroups is None else CUGroups

        self._DesignLocation = None
        self.DesignLocation = DesignLocation

        self.status = status

        super(DesignLocationCU, self).__init__(*args, **kw_args)

    _attrs = ["energizationFlag", "cuUsage", "removalDate", "cuAction", "cuAccount", "cuQuantity"]
    _attr_types = {"energizationFlag": bool, "cuUsage": str, "removalDate": str, "cuAction": str, "cuAccount": str, "cuQuantity": str}
    _defaults = {"energizationFlag": False, "cuUsage": '', "removalDate": '', "cuAction": "install", "cuAccount": '', "cuQuantity": ""}
    _enums = {"cuAction": "WorkActionKind"}
    _refs = ["ConditionFactors", "CompatibleUnits", "WorkTasks", "Designs", "CUGroups", "DesignLocation", "status"]
    _many_refs = ["ConditionFactors", "CompatibleUnits", "WorkTasks", "Designs", "CUGroups"]

    def getConditionFactors(self):
        
        return self._ConditionFactors

    def setConditionFactors(self, value):
        for p in self._ConditionFactors:
            filtered = [q for q in p.DesignLocationCUs if q != self]
            self._ConditionFactors._DesignLocationCUs = filtered
        for r in value:
            if self not in r._DesignLocationCUs:
                r._DesignLocationCUs.append(self)
        self._ConditionFactors = value

    ConditionFactors = property(getConditionFactors, setConditionFactors)

    def addConditionFactors(self, *ConditionFactors):
        for obj in ConditionFactors:
            if self not in obj._DesignLocationCUs:
                obj._DesignLocationCUs.append(self)
            self._ConditionFactors.append(obj)

    def removeConditionFactors(self, *ConditionFactors):
        for obj in ConditionFactors:
            if self in obj._DesignLocationCUs:
                obj._DesignLocationCUs.remove(self)
            self._ConditionFactors.remove(obj)

    def getCompatibleUnits(self):
        
        return self._CompatibleUnits

    def setCompatibleUnits(self, value):
        for p in self._CompatibleUnits:
            filtered = [q for q in p.DesignLocationCUs if q != self]
            self._CompatibleUnits._DesignLocationCUs = filtered
        for r in value:
            if self not in r._DesignLocationCUs:
                r._DesignLocationCUs.append(self)
        self._CompatibleUnits = value

    CompatibleUnits = property(getCompatibleUnits, setCompatibleUnits)

    def addCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            if self not in obj._DesignLocationCUs:
                obj._DesignLocationCUs.append(self)
            self._CompatibleUnits.append(obj)

    def removeCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            if self in obj._DesignLocationCUs:
                obj._DesignLocationCUs.remove(self)
            self._CompatibleUnits.remove(obj)

    def getWorkTasks(self):
        
        return self._WorkTasks

    def setWorkTasks(self, value):
        for p in self._WorkTasks:
            filtered = [q for q in p.DesignLocationCUs if q != self]
            self._WorkTasks._DesignLocationCUs = filtered
        for r in value:
            if self not in r._DesignLocationCUs:
                r._DesignLocationCUs.append(self)
        self._WorkTasks = value

    WorkTasks = property(getWorkTasks, setWorkTasks)

    def addWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            if self not in obj._DesignLocationCUs:
                obj._DesignLocationCUs.append(self)
            self._WorkTasks.append(obj)

    def removeWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            if self in obj._DesignLocationCUs:
                obj._DesignLocationCUs.remove(self)
            self._WorkTasks.remove(obj)

    def getDesigns(self):
        
        return self._Designs

    def setDesigns(self, value):
        for p in self._Designs:
            filtered = [q for q in p.DesignLocationsCUs if q != self]
            self._Designs._DesignLocationsCUs = filtered
        for r in value:
            if self not in r._DesignLocationsCUs:
                r._DesignLocationsCUs.append(self)
        self._Designs = value

    Designs = property(getDesigns, setDesigns)

    def addDesigns(self, *Designs):
        for obj in Designs:
            if self not in obj._DesignLocationsCUs:
                obj._DesignLocationsCUs.append(self)
            self._Designs.append(obj)

    def removeDesigns(self, *Designs):
        for obj in Designs:
            if self in obj._DesignLocationsCUs:
                obj._DesignLocationsCUs.remove(self)
            self._Designs.remove(obj)

    def getCUGroups(self):
        
        return self._CUGroups

    def setCUGroups(self, value):
        for p in self._CUGroups:
            filtered = [q for q in p.DesignLocationCUs if q != self]
            self._CUGroups._DesignLocationCUs = filtered
        for r in value:
            if self not in r._DesignLocationCUs:
                r._DesignLocationCUs.append(self)
        self._CUGroups = value

    CUGroups = property(getCUGroups, setCUGroups)

    def addCUGroups(self, *CUGroups):
        for obj in CUGroups:
            if self not in obj._DesignLocationCUs:
                obj._DesignLocationCUs.append(self)
            self._CUGroups.append(obj)

    def removeCUGroups(self, *CUGroups):
        for obj in CUGroups:
            if self in obj._DesignLocationCUs:
                obj._DesignLocationCUs.remove(self)
            self._CUGroups.remove(obj)

    def getDesignLocation(self):
        
        return self._DesignLocation

    def setDesignLocation(self, value):
        if self._DesignLocation is not None:
            filtered = [x for x in self.DesignLocation.DesignLocationCUs if x != self]
            self._DesignLocation._DesignLocationCUs = filtered

        self._DesignLocation = value
        if self._DesignLocation is not None:
            if self not in self._DesignLocation._DesignLocationCUs:
                self._DesignLocation._DesignLocationCUs.append(self)

    DesignLocation = property(getDesignLocation, setDesignLocation)

    status = None

