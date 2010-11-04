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

class QualificationRequirement(IdentifiedObject):
    """Certain skills are required and must be certified in order for a person (typically a member of a crew) to be qualified to work on types of equipment.
    """

    def __init__(self, qualificationID='', Specifications=None, WorkTasks=None, CULaborItems=None, Skills=None, **kw_args):
        """Initializes a new 'QualificationRequirement' instance.

        @param qualificationID: Qualification identifier. 
        @param Specifications:
        @param WorkTasks:
        @param CULaborItems:
        @param Skills:
        """
        #: Qualification identifier.
        self.qualificationID = qualificationID

        self._Specifications = []
        self.Specifications = [] if Specifications is None else Specifications

        self._WorkTasks = []
        self.WorkTasks = [] if WorkTasks is None else WorkTasks

        self._CULaborItems = []
        self.CULaborItems = [] if CULaborItems is None else CULaborItems

        self._Skills = []
        self.Skills = [] if Skills is None else Skills

        super(QualificationRequirement, self).__init__(**kw_args)

    def getSpecifications(self):
        
        return self._Specifications

    def setSpecifications(self, value):
        for p in self._Specifications:
            filtered = [q for q in p.QualificationRequirements if q != self]
            self._Specifications._QualificationRequirements = filtered
        for r in value:
            if self not in r._QualificationRequirements:
                r._QualificationRequirements.append(self)
        self._Specifications = value

    Specifications = property(getSpecifications, setSpecifications)

    def addSpecifications(self, *Specifications):
        for obj in Specifications:
            if self not in obj._QualificationRequirements:
                obj._QualificationRequirements.append(self)
            self._Specifications.append(obj)

    def removeSpecifications(self, *Specifications):
        for obj in Specifications:
            if self in obj._QualificationRequirements:
                obj._QualificationRequirements.remove(self)
            self._Specifications.remove(obj)

    def getWorkTasks(self):
        
        return self._WorkTasks

    def setWorkTasks(self, value):
        for p in self._WorkTasks:
            filtered = [q for q in p.QualificationRequirements if q != self]
            self._WorkTasks._QualificationRequirements = filtered
        for r in value:
            if self not in r._QualificationRequirements:
                r._QualificationRequirements.append(self)
        self._WorkTasks = value

    WorkTasks = property(getWorkTasks, setWorkTasks)

    def addWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            if self not in obj._QualificationRequirements:
                obj._QualificationRequirements.append(self)
            self._WorkTasks.append(obj)

    def removeWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            if self in obj._QualificationRequirements:
                obj._QualificationRequirements.remove(self)
            self._WorkTasks.remove(obj)

    def getCULaborItems(self):
        
        return self._CULaborItems

    def setCULaborItems(self, value):
        for p in self._CULaborItems:
            filtered = [q for q in p.QualificationRequirements if q != self]
            self._CULaborItems._QualificationRequirements = filtered
        for r in value:
            if self not in r._QualificationRequirements:
                r._QualificationRequirements.append(self)
        self._CULaborItems = value

    CULaborItems = property(getCULaborItems, setCULaborItems)

    def addCULaborItems(self, *CULaborItems):
        for obj in CULaborItems:
            if self not in obj._QualificationRequirements:
                obj._QualificationRequirements.append(self)
            self._CULaborItems.append(obj)

    def removeCULaborItems(self, *CULaborItems):
        for obj in CULaborItems:
            if self in obj._QualificationRequirements:
                obj._QualificationRequirements.remove(self)
            self._CULaborItems.remove(obj)

    def getSkills(self):
        
        return self._Skills

    def setSkills(self, value):
        for p in self._Skills:
            filtered = [q for q in p.QualificationRequirements if q != self]
            self._Skills._QualificationRequirements = filtered
        for r in value:
            if self not in r._QualificationRequirements:
                r._QualificationRequirements.append(self)
        self._Skills = value

    Skills = property(getSkills, setSkills)

    def addSkills(self, *Skills):
        for obj in Skills:
            if self not in obj._QualificationRequirements:
                obj._QualificationRequirements.append(self)
            self._Skills.append(obj)

    def removeSkills(self, *Skills):
        for obj in Skills:
            if self in obj._QualificationRequirements:
                obj._QualificationRequirements.remove(self)
            self._Skills.remove(obj)

