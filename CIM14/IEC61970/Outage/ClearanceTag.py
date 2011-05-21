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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ClearanceTag(IdentifiedObject):
    """A clearance tag that is used to authorize and schedule work on conducting equipment in the field. Tagged equipment is not available for commercial service.
    """

    def __init__(self, workStartTime='', workDescription='', workEndTime='', authorityName='', deenergizeReqFlag=False, groundReqFlag=False, tagIssueTime='', phaseCheckReqFlag=False, ClearanceTagType=None, ConductingEquipment=None, *args, **kw_args):
        """Initialises a new 'ClearanceTag' instance.

        @param workStartTime: The time at which the clearance tag is scheduled to be set. 
        @param workDescription: Description of the work to be performed 
        @param workEndTime: The time at which the clearance tag is scheduled to be removed 
        @param authorityName: The name of the person who is authorized to issue the tag 
        @param deenergizeReqFlag: Set true if equipment must be deenergized 
        @param groundReqFlag: Set true if equipment must be grounded 
        @param tagIssueTime: The time at which the clearance tag was issued 
        @param phaseCheckReqFlag: Set true if equipment phasing must be checked 
        @param ClearanceTagType: The type of tag, depending on the purpose of the work to be performed and/or the type of supervisory control allowed.
        @param ConductingEquipment: Conducting equipment may have multiple clearance tags for authorized field work
        """
        #: The time at which the clearance tag is scheduled to be set.
        self.workStartTime = workStartTime

        #: Description of the work to be performed
        self.workDescription = workDescription

        #: The time at which the clearance tag is scheduled to be removed
        self.workEndTime = workEndTime

        #: The name of the person who is authorized to issue the tag
        self.authorityName = authorityName

        #: Set true if equipment must be deenergized
        self.deenergizeReqFlag = deenergizeReqFlag

        #: Set true if equipment must be grounded
        self.groundReqFlag = groundReqFlag

        #: The time at which the clearance tag was issued
        self.tagIssueTime = tagIssueTime

        #: Set true if equipment phasing must be checked
        self.phaseCheckReqFlag = phaseCheckReqFlag

        self._ClearanceTagType = None
        self.ClearanceTagType = ClearanceTagType

        self._ConductingEquipment = None
        self.ConductingEquipment = ConductingEquipment

        super(ClearanceTag, self).__init__(*args, **kw_args)

    _attrs = ["workStartTime", "workDescription", "workEndTime", "authorityName", "deenergizeReqFlag", "groundReqFlag", "tagIssueTime", "phaseCheckReqFlag"]
    _attr_types = {"workStartTime": str, "workDescription": str, "workEndTime": str, "authorityName": str, "deenergizeReqFlag": bool, "groundReqFlag": bool, "tagIssueTime": str, "phaseCheckReqFlag": bool}
    _defaults = {"workStartTime": '', "workDescription": '', "workEndTime": '', "authorityName": '', "deenergizeReqFlag": False, "groundReqFlag": False, "tagIssueTime": '', "phaseCheckReqFlag": False}
    _enums = {}
    _refs = ["ClearanceTagType", "ConductingEquipment"]
    _many_refs = []

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

