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

class ConditionFactor(IdentifiedObject):
    """This is to specify the various condition factors for a design that may alter the cost estimate or the allocation.This is to specify the various condition factors for a design that may alter the cost estimate or the allocation.
    """

    def __init__(self, kind="material", cfValue='', Designs=None, DesignLocations=None, status=None, DesignLocationCUs=None, *args, **kw_args):
        """Initialises a new 'ConditionFactor' instance.

        @param kind: Kind of this condition factor. Values are: "material", "travel", "accountAllocation", "labor", "other"
        @param cfValue: The actual value of the condition factor, such as labor flat fee or percentage. 
        @param Designs:
        @param DesignLocations:
        @param status:
        @param DesignLocationCUs:
        """
        #: Kind of this condition factor. Values are: "material", "travel", "accountAllocation", "labor", "other"
        self.kind = kind

        #: The actual value of the condition factor, such as labor flat fee or percentage.
        self.cfValue = cfValue

        self._Designs = []
        self.Designs = [] if Designs is None else Designs

        self._DesignLocations = []
        self.DesignLocations = [] if DesignLocations is None else DesignLocations

        self.status = status

        self._DesignLocationCUs = []
        self.DesignLocationCUs = [] if DesignLocationCUs is None else DesignLocationCUs

        super(ConditionFactor, self).__init__(*args, **kw_args)

    _attrs = ["kind", "cfValue"]
    _attr_types = {"kind": str, "cfValue": str}
    _defaults = {"kind": "material", "cfValue": ''}
    _enums = {"kind": "ConditionFactorKind"}
    _refs = ["Designs", "DesignLocations", "status", "DesignLocationCUs"]
    _many_refs = ["Designs", "DesignLocations", "DesignLocationCUs"]

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

