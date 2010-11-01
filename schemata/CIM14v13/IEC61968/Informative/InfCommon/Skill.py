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

from CIM14v13.IEC61968.Common.Document import Document

class Skill(Document):
    """Proficiency level of a craft, which is required to operate or maintain a particular type of asset and/or perform certain types of work.
    """

    def __init__(self, level='master', effectiveDateTime='', Crafts=None, QualificationRequirements=None, ErpPerson=None, certificationPeriod=None, *args, **kw_args):
        """Initializes a new 'Skill' instance.

        @param level: Level of skill for a Craft. Values are: "master", "other", "standard", "apprentice"
        @param effectiveDateTime: Date and time the skill became effective. 
        @param Crafts:
        @param QualificationRequirements:
        @param ErpPerson:
        @param certificationPeriod: Interval between the certification and its expiry.
        """
        #: Level of skill for a Craft. Values are: "master", "other", "standard", "apprentice"
        self.level = level

        #: Date and time the skill became effective. 
        self.effectiveDateTime = effectiveDateTime

        self._Crafts = []
        self.Crafts = [] if Crafts is None else Crafts

        self._QualificationRequirements = []
        self.QualificationRequirements = [] if QualificationRequirements is None else QualificationRequirements

        self._ErpPerson = None
        self.ErpPerson = ErpPerson

        self.certificationPeriod = certificationPeriod

        super(Skill, self).__init__(*args, **kw_args)

    def getCrafts(self):
        
        return self._Crafts

    def setCrafts(self, value):
        for p in self._Crafts:
            filtered = [q for q in p.Skills if q != self]
            self._Crafts._Skills = filtered
        for r in value:
            if self not in r._Skills:
                r._Skills.append(self)
        self._Crafts = value

    Crafts = property(getCrafts, setCrafts)

    def addCrafts(self, *Crafts):
        for obj in Crafts:
            if self not in obj._Skills:
                obj._Skills.append(self)
            self._Crafts.append(obj)

    def removeCrafts(self, *Crafts):
        for obj in Crafts:
            if self in obj._Skills:
                obj._Skills.remove(self)
            self._Crafts.remove(obj)

    def getQualificationRequirements(self):
        
        return self._QualificationRequirements

    def setQualificationRequirements(self, value):
        for p in self._QualificationRequirements:
            filtered = [q for q in p.Skills if q != self]
            self._QualificationRequirements._Skills = filtered
        for r in value:
            if self not in r._Skills:
                r._Skills.append(self)
        self._QualificationRequirements = value

    QualificationRequirements = property(getQualificationRequirements, setQualificationRequirements)

    def addQualificationRequirements(self, *QualificationRequirements):
        for obj in QualificationRequirements:
            if self not in obj._Skills:
                obj._Skills.append(self)
            self._QualificationRequirements.append(obj)

    def removeQualificationRequirements(self, *QualificationRequirements):
        for obj in QualificationRequirements:
            if self in obj._Skills:
                obj._Skills.remove(self)
            self._QualificationRequirements.remove(obj)

    def getErpPerson(self):
        
        return self._ErpPerson

    def setErpPerson(self, value):
        if self._ErpPerson is not None:
            filtered = [x for x in self.ErpPerson.Skills if x != self]
            self._ErpPerson._Skills = filtered

        self._ErpPerson = value
        if self._ErpPerson is not None:
            self._ErpPerson._Skills.append(self)

    ErpPerson = property(getErpPerson, setErpPerson)

    # Interval between the certification and its expiry.
    certificationPeriod = None

