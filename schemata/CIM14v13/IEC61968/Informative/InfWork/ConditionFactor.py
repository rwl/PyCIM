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

class ConditionFactor(IdentifiedObject):
    """This is to specify the various condition factors for a design that may alter the cost estimate or the allocation.
    """

    def __init__(self, kind='labor', cfValue='', status=None, DesignLocationCUs=None, DesignLocations=None, Designs=None, *args, **kw_args):
        """Initializes a new 'ConditionFactor' instance.

        @param kind: Kind of this condition factor. Values are: "labor", "accountAllocation", "travel", "other", "material"
        @param cfValue: The actual value of the condition factor, such as labor flat fee or percentage. 
        @param status:
        @param DesignLocationCUs:
        @param DesignLocations:
        @param Designs:
        """
        #: Kind of this condition factor.Values are: "labor", "accountAllocation", "travel", "other", "material"
        self.kind = kind

        #: The actual value of the condition factor, such as labor flat fee or percentage.
        self.cfValue = cfValue

        self.status = status

        self._DesignLocationCUs = []
        self.DesignLocationCUs = [] if DesignLocationCUs is None else DesignLocationCUs

        self._DesignLocations = []
        self.DesignLocations = [] if DesignLocations is None else DesignLocations

        self._Designs = []
        self.Designs = [] if Designs is None else Designs

        super(ConditionFactor, self).__init__(*args, **kw_args)

    status = None

    def getDesignLocationCUs(self):
        
        return self._DesignLocationCUs

    def setDesignLocationCUs(self, value):
        for p in self._DesignLocationCUs:
            filtered = [q for q in p.ConditionFactors if q != self]
            self._DesignLocationCUs._ConditionFactors = filtered
        for r in value:
            if self not in r._ConditionFactors:
                r._ConditionFactors.append(self)
        self._DesignLocationCUs = value

    DesignLocationCUs = property(getDesignLocationCUs, setDesignLocationCUs)

    def addDesignLocationCUs(self, *DesignLocationCUs):
        for obj in DesignLocationCUs:
            if self not in obj._ConditionFactors:
                obj._ConditionFactors.append(self)
            self._DesignLocationCUs.append(obj)

    def removeDesignLocationCUs(self, *DesignLocationCUs):
        for obj in DesignLocationCUs:
            if self in obj._ConditionFactors:
                obj._ConditionFactors.remove(self)
            self._DesignLocationCUs.remove(obj)

    def getDesignLocations(self):
        
        return self._DesignLocations

    def setDesignLocations(self, value):
        for p in self._DesignLocations:
            filtered = [q for q in p.ConditionFactors if q != self]
            self._DesignLocations._ConditionFactors = filtered
        for r in value:
            if self not in r._ConditionFactors:
                r._ConditionFactors.append(self)
        self._DesignLocations = value

    DesignLocations = property(getDesignLocations, setDesignLocations)

    def addDesignLocations(self, *DesignLocations):
        for obj in DesignLocations:
            if self not in obj._ConditionFactors:
                obj._ConditionFactors.append(self)
            self._DesignLocations.append(obj)

    def removeDesignLocations(self, *DesignLocations):
        for obj in DesignLocations:
            if self in obj._ConditionFactors:
                obj._ConditionFactors.remove(self)
            self._DesignLocations.remove(obj)

    def getDesigns(self):
        
        return self._Designs

    def setDesigns(self, value):
        for p in self._Designs:
            filtered = [q for q in p.ConditionFactors if q != self]
            self._Designs._ConditionFactors = filtered
        for r in value:
            if self not in r._ConditionFactors:
                r._ConditionFactors.append(self)
        self._Designs = value

    Designs = property(getDesigns, setDesigns)

    def addDesigns(self, *Designs):
        for obj in Designs:
            if self not in obj._ConditionFactors:
                obj._ConditionFactors.append(self)
            self._Designs.append(obj)

    def removeDesigns(self, *Designs):
        for obj in Designs:
            if self in obj._ConditionFactors:
                obj._ConditionFactors.remove(self)
            self._Designs.remove(obj)

