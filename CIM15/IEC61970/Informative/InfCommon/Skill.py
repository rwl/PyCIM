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

from CIM15.IEC61968.Common.Document import Document

class Skill(Document):
    """Proficiency level of a craft, which is required to operate or maintain a particular type of asset and/or perform certain types of work.Proficiency level of a craft, which is required to operate or maintain a particular type of asset and/or perform certain types of work.
    """

    def __init__(self, effectiveDateTime='', level="apprentice", Crafts=None, ErpPerson=None, QualificationRequirements=None, certificationPeriod=None, *args, **kw_args):
        """Initialises a new 'Skill' instance.

        @param effectiveDateTime: Date and time the skill became effective. 
        @param level: Level of skill for a Craft. Values are: "apprentice", "other", "master", "standard"
        @param Crafts:
        @param ErpPerson:
        @param QualificationRequirements:
        @param certificationPeriod: Interval between the certification and its expiry.
        """
        #: Date and time the skill became effective.
        self.effectiveDateTime = effectiveDateTime

        #: Level of skill for a Craft. Values are: "apprentice", "other", "master", "standard"
        self.level = level

        self._Crafts = []
        self.Crafts = [] if Crafts is None else Crafts

        self._ErpPerson = None
        self.ErpPerson = ErpPerson

        self._QualificationRequirements = []
        self.QualificationRequirements = [] if QualificationRequirements is None else QualificationRequirements

        self.certificationPeriod = certificationPeriod

        super(Skill, self).__init__(*args, **kw_args)

    _attrs = ["effectiveDateTime", "level"]
    _attr_types = {"effectiveDateTime": str, "level": str}
    _defaults = {"effectiveDateTime": '', "level": "apprentice"}
    _enums = {"level": "SkillLevelKind"}
    _refs = ["Crafts", "ErpPerson", "QualificationRequirements", "certificationPeriod"]
    _many_refs = ["Crafts", "QualificationRequirements"]

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

    def getErpPerson(self):
        
        return self._ErpPerson

    def setErpPerson(self, value):
        if self._ErpPerson is not None:
            filtered = [x for x in self.ErpPerson.Skills if x != self]
            self._ErpPerson._Skills = filtered

        self._ErpPerson = value
        if self._ErpPerson is not None:
            if self not in self._ErpPerson._Skills:
                self._ErpPerson._Skills.append(self)

    ErpPerson = property(getErpPerson, setErpPerson)

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

    # Interval between the certification and its expiry.
    certificationPeriod = None

