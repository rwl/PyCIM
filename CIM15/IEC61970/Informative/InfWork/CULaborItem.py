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

class CULaborItem(IdentifiedObject):
    """Compatible unit labor item.Compatible unit labor item.
    """

    def __init__(self, laborDuration=0.0, laborRate=0.0, activityCode='', CompatibleUnits=None, CULaborCode=None, status=None, QualificationRequirements=None, *args, **kw_args):
        """Initialises a new 'CULaborItem' instance.

        @param laborDuration: Estimated time to perform work. 
        @param laborRate: The labor rate applied for work. 
        @param activityCode: Activity code identifies a specific and distinguishable unit of work. 
        @param CompatibleUnits:
        @param CULaborCode:
        @param status:
        @param QualificationRequirements:
        """
        #: Estimated time to perform work.
        self.laborDuration = laborDuration

        #: The labor rate applied for work.
        self.laborRate = laborRate

        #: Activity code identifies a specific and distinguishable unit of work.
        self.activityCode = activityCode

        self._CompatibleUnits = []
        self.CompatibleUnits = [] if CompatibleUnits is None else CompatibleUnits

        self._CULaborCode = None
        self.CULaborCode = CULaborCode

        self.status = status

        self._QualificationRequirements = []
        self.QualificationRequirements = [] if QualificationRequirements is None else QualificationRequirements

        super(CULaborItem, self).__init__(*args, **kw_args)

    _attrs = ["laborDuration", "laborRate", "activityCode"]
    _attr_types = {"laborDuration": float, "laborRate": float, "activityCode": str}
    _defaults = {"laborDuration": 0.0, "laborRate": 0.0, "activityCode": ''}
    _enums = {}
    _refs = ["CompatibleUnits", "CULaborCode", "status", "QualificationRequirements"]
    _many_refs = ["CompatibleUnits", "QualificationRequirements"]

    def getCompatibleUnits(self):
        
        return self._CompatibleUnits

    def setCompatibleUnits(self, value):
        for p in self._CompatibleUnits:
            filtered = [q for q in p.CULaborItems if q != self]
            self._CompatibleUnits._CULaborItems = filtered
        for r in value:
            if self not in r._CULaborItems:
                r._CULaborItems.append(self)
        self._CompatibleUnits = value

    CompatibleUnits = property(getCompatibleUnits, setCompatibleUnits)

    def addCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            if self not in obj._CULaborItems:
                obj._CULaborItems.append(self)
            self._CompatibleUnits.append(obj)

    def removeCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            if self in obj._CULaborItems:
                obj._CULaborItems.remove(self)
            self._CompatibleUnits.remove(obj)

    def getCULaborCode(self):
        
        return self._CULaborCode

    def setCULaborCode(self, value):
        if self._CULaborCode is not None:
            filtered = [x for x in self.CULaborCode.CULaborItems if x != self]
            self._CULaborCode._CULaborItems = filtered

        self._CULaborCode = value
        if self._CULaborCode is not None:
            if self not in self._CULaborCode._CULaborItems:
                self._CULaborCode._CULaborItems.append(self)

    CULaborCode = property(getCULaborCode, setCULaborCode)

    status = None

    def getQualificationRequirements(self):
        
        return self._QualificationRequirements

    def setQualificationRequirements(self, value):
        for p in self._QualificationRequirements:
            filtered = [q for q in p.CULaborItems if q != self]
            self._QualificationRequirements._CULaborItems = filtered
        for r in value:
            if self not in r._CULaborItems:
                r._CULaborItems.append(self)
        self._QualificationRequirements = value

    QualificationRequirements = property(getQualificationRequirements, setQualificationRequirements)

    def addQualificationRequirements(self, *QualificationRequirements):
        for obj in QualificationRequirements:
            if self not in obj._CULaborItems:
                obj._CULaborItems.append(self)
            self._QualificationRequirements.append(obj)

    def removeQualificationRequirements(self, *QualificationRequirements):
        for obj in QualificationRequirements:
            if self in obj._CULaborItems:
                obj._CULaborItems.remove(self)
            self._QualificationRequirements.remove(obj)

