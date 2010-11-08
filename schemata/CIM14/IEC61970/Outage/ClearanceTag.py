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
            self._ConductingEquipment._ClearanceTags.append(self)

    ConductingEquipment = property(getConductingEquipment, setConductingEquipment)

