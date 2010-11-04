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

class DesignLocationCU(IdentifiedObject):
    """Compatible unit at a given design location.
    """

    def __init__(self, cuAction='install', removalYear='', cuUsage='', cuAccount='', cuQuantity=0, energizationFlag=False, Designs=None, DesignLocation=None, CUGroups=None, ConditionFactors=None, WorkTasks=None, CompatibleUnits=None, status=None, *args, **kw_args):
        """Initializes a new 'DesignLocationCU' instance.

        @param cuAction: A code that instructs the crew what action to perform. Values are: "install", "remove", "transfer", "abandon"
        @param removalYear: Year when a CU that represents an asset is removed. 
        @param cuUsage: As the same CU can be used for different purposes and accounting purposes, usage must be specified. Examples include: distribution, transmission, substation. 
        @param cuAccount: A code that helps direct accounting (capital, expense, or accounting treatment). 
        @param cuQuantity: The quantity of the CU being assigned to this location. 
        @param energizationFlag: True if associated electrical equipment is intended to be energized while work is being performed. 
        @param Designs:
        @param DesignLocation:
        @param CUGroups:
        @param ConditionFactors:
        @param WorkTasks:
        @param CompatibleUnits:
        @param status:
        """
        #: A code that instructs the crew what action to perform.Values are: "install", "remove", "transfer", "abandon"
        self.cuAction = cuAction

        #: Year when a CU that represents an asset is removed.
        self.removalYear = removalYear

        #: As the same CU can be used for different purposes and accounting purposes, usage must be specified. Examples include: distribution, transmission, substation.
        self.cuUsage = cuUsage

        #: A code that helps direct accounting (capital, expense, or accounting treatment).
        self.cuAccount = cuAccount

        #: The quantity of the CU being assigned to this location.
        self.cuQuantity = cuQuantity

        #: True if associated electrical equipment is intended to be energized while work is being performed.
        self.energizationFlag = energizationFlag

        self._Designs = []
        self.Designs = [] if Designs is None else Designs

        self._DesignLocation = None
        self.DesignLocation = DesignLocation

        self._CUGroups = []
        self.CUGroups = [] if CUGroups is None else CUGroups

        self._ConditionFactors = []
        self.ConditionFactors = [] if ConditionFactors is None else ConditionFactors

        self._WorkTasks = []
        self.WorkTasks = [] if WorkTasks is None else WorkTasks

        self._CompatibleUnits = []
        self.CompatibleUnits = [] if CompatibleUnits is None else CompatibleUnits

        self.status = status

        super(DesignLocationCU, self).__init__(*args, **kw_args)

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

    def getDesignLocation(self):
        
        return self._DesignLocation

    def setDesignLocation(self, value):
        if self._DesignLocation is not None:
            filtered = [x for x in self.DesignLocation.DesignLocationCUs if x != self]
            self._DesignLocation._DesignLocationCUs = filtered

        self._DesignLocation = value
        if self._DesignLocation is not None:
            self._DesignLocation._DesignLocationCUs.append(self)

    DesignLocation = property(getDesignLocation, setDesignLocation)

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

    status = None

