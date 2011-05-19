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

class QualificationRequirement(IdentifiedObject):
    """Certain skills are required and must be certified in order for a person (typically a member of a crew) to be qualified to work on types of equipment.Certain skills are required and must be certified in order for a person (typically a member of a crew) to be qualified to work on types of equipment.
    """

    def __init__(self, qualificationID='', WorkTasks=None, Skills=None, CULaborItems=None, Specifications=None, *args, **kw_args):
        """Initialises a new 'QualificationRequirement' instance.

        @param qualificationID: Qualification identifier. 
        @param WorkTasks:
        @param Skills:
        @param CULaborItems:
        @param Specifications:
        """
        #: Qualification identifier.
        self.qualificationID = qualificationID

        self._WorkTasks = []
        self.WorkTasks = [] if WorkTasks is None else WorkTasks

        self._Skills = []
        self.Skills = [] if Skills is None else Skills

        self._CULaborItems = []
        self.CULaborItems = [] if CULaborItems is None else CULaborItems

        self._Specifications = []
        self.Specifications = [] if Specifications is None else Specifications

        super(QualificationRequirement, self).__init__(*args, **kw_args)

    _attrs = ["qualificationID"]
    _attr_types = {"qualificationID": str}
    _defaults = {"qualificationID": ''}
    _enums = {}
    _refs = ["WorkTasks", "Skills", "CULaborItems", "Specifications"]
    _many_refs = ["WorkTasks", "Skills", "CULaborItems", "Specifications"]

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

