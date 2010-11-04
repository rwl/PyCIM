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

class CULaborItem(IdentifiedObject):
    """Compatible unit labor item.
    """

    def __init__(self, laborRate=0.0, activityCode='', laborDuration=0.0, QualificationRequirements=None, CULaborCode=None, status=None, CompatibleUnits=None, **kw_args):
        """Initializes a new 'CULaborItem' instance.

        @param laborRate: The labor rate applied for work. 
        @param activityCode: Activity code identifies a specific and distinguishable unit of work. 
        @param laborDuration: Estimated time to perform work. 
        @param QualificationRequirements:
        @param CULaborCode:
        @param status:
        @param CompatibleUnits:
        """
        #: The labor rate applied for work.
        self.laborRate = laborRate

        #: Activity code identifies a specific and distinguishable unit of work.
        self.activityCode = activityCode

        #: Estimated time to perform work.
        self.laborDuration = laborDuration

        self._QualificationRequirements = []
        self.QualificationRequirements = [] if QualificationRequirements is None else QualificationRequirements

        self._CULaborCode = None
        self.CULaborCode = CULaborCode

        self.status = status

        self._CompatibleUnits = []
        self.CompatibleUnits = [] if CompatibleUnits is None else CompatibleUnits

        super(CULaborItem, self).__init__(**kw_args)

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

    def getCULaborCode(self):
        
        return self._CULaborCode

    def setCULaborCode(self, value):
        if self._CULaborCode is not None:
            filtered = [x for x in self.CULaborCode.CULaborItems if x != self]
            self._CULaborCode._CULaborItems = filtered

        self._CULaborCode = value
        if self._CULaborCode is not None:
            self._CULaborCode._CULaborItems.append(self)

    CULaborCode = property(getCULaborCode, setCULaborCode)

    status = None

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

