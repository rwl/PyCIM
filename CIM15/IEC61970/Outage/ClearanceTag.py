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

class ClearanceTag(IdentifiedObject):
    """A clearance tag that is used to authorize and schedule work on conducting equipment in the field. Tagged equipment is not available for commercial service.A clearance tag that is used to authorize and schedule work on conducting equipment in the field. Tagged equipment is not available for commercial service.
    """

    def __init__(self, workStartTime='', phaseCheckReqFlag=False, deenergizeReqFlag=False, authorityName='', tagIssueTime='', groundReqFlag=False, workDescription='', workEndTime='', ConductingEquipment=None, SafetyDocument=None, ClearanceTagType=None, *args, **kw_args):
        """Initialises a new 'ClearanceTag' instance.

        @param workStartTime: The time at which the clearance tag is scheduled to be set. 
        @param phaseCheckReqFlag: Set true if equipment phasing must be checked 
        @param deenergizeReqFlag: Set true if equipment must be deenergized 
        @param authorityName: The name of the person who is authorized to issue the tag 
        @param tagIssueTime: The time at which the clearance tag was issued 
        @param groundReqFlag: Set true if equipment must be grounded 
        @param workDescription: Description of the work to be performed 
        @param workEndTime: The time at which the clearance tag is scheduled to be removed 
        @param ConductingEquipment: Conducting equipment may have multiple clearance tags for authorized field work
        @param SafetyDocument:
        @param ClearanceTagType: The type of tag, depending on the purpose of the work to be performed and/or the type of supervisory control allowed.
        """
        #: The time at which the clearance tag is scheduled to be set.
        self.workStartTime = workStartTime

        #: Set true if equipment phasing must be checked
        self.phaseCheckReqFlag = phaseCheckReqFlag

        #: Set true if equipment must be deenergized
        self.deenergizeReqFlag = deenergizeReqFlag

        #: The name of the person who is authorized to issue the tag
        self.authorityName = authorityName

        #: The time at which the clearance tag was issued
        self.tagIssueTime = tagIssueTime

        #: Set true if equipment must be grounded
        self.groundReqFlag = groundReqFlag

        #: Description of the work to be performed
        self.workDescription = workDescription

        #: The time at which the clearance tag is scheduled to be removed
        self.workEndTime = workEndTime

        self._ConductingEquipment = None
        self.ConductingEquipment = ConductingEquipment

        self._SafetyDocument = None
        self.SafetyDocument = SafetyDocument

        self._ClearanceTagType = None
        self.ClearanceTagType = ClearanceTagType

        super(ClearanceTag, self).__init__(*args, **kw_args)

    _attrs = ["workStartTime", "phaseCheckReqFlag", "deenergizeReqFlag", "authorityName", "tagIssueTime", "groundReqFlag", "workDescription", "workEndTime"]
    _attr_types = {"workStartTime": str, "phaseCheckReqFlag": bool, "deenergizeReqFlag": bool, "authorityName": str, "tagIssueTime": str, "groundReqFlag": bool, "workDescription": str, "workEndTime": str}
    _defaults = {"workStartTime": '', "phaseCheckReqFlag": False, "deenergizeReqFlag": False, "authorityName": '', "tagIssueTime": '', "groundReqFlag": False, "workDescription": '', "workEndTime": ''}
    _enums = {}
    _refs = ["ConductingEquipment", "SafetyDocument", "ClearanceTagType"]
    _many_refs = []

    def getConductingEquipment(self):
        """Conducting equipment may have multiple clearance tags for authorized field work
        """
        return self._ConductingEquipment

    def setConductingEquipment(self, value):
        if self._ConductingEquipment is not None:
            filtered = [x for x in self.ConductingEquipment.ClearanceTags if x != self]
            self._ConductingEquipment._ClearanceTags = filtered

        self._ConductingEquipment = value
        if self._ConductingEquipment is not None:
            if self not in self._ConductingEquipment._ClearanceTags:
                self._ConductingEquipment._ClearanceTags.append(self)

    ConductingEquipment = property(getConductingEquipment, setConductingEquipment)

    def getSafetyDocument(self):
        
        return self._SafetyDocument

    def setSafetyDocument(self, value):
        if self._SafetyDocument is not None:
            filtered = [x for x in self.SafetyDocument.ClearanceTags if x != self]
            self._SafetyDocument._ClearanceTags = filtered

        self._SafetyDocument = value
        if self._SafetyDocument is not None:
            if self not in self._SafetyDocument._ClearanceTags:
                self._SafetyDocument._ClearanceTags.append(self)

    SafetyDocument = property(getSafetyDocument, setSafetyDocument)

    def getClearanceTagType(self):
        """The type of tag, depending on the purpose of the work to be performed and/or the type of supervisory control allowed.
        """
        return self._ClearanceTagType

    def setClearanceTagType(self, value):
        if self._ClearanceTagType is not None:
            filtered = [x for x in self.ClearanceTagType.ClearanceTags if x != self]
            self._ClearanceTagType._ClearanceTags = filtered

        self._ClearanceTagType = value
        if self._ClearanceTagType is not None:
            if self not in self._ClearanceTagType._ClearanceTags:
                self._ClearanceTagType._ClearanceTags.append(self)

    ClearanceTagType = property(getClearanceTagType, setClearanceTagType)

