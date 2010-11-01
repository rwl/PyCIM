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

class ClearanceTag(IdentifiedObject):
    """A clearance tag that is used to authorize and schedule work on conducting equipment in the field. Tagged equipment is not available for commercial service.
    """

    def __init__(self, authorityName='', workEndTime='', phaseCheckReqFlag=False, deenergizeReqFlag=False, tagIssueTime='', workDescription='', workStartTime='', groundReqFlag=False, ConductingEquipment=None, SafetyDocument=None, ClearanceTagType=None, *args, **kw_args):
        """Initializes a new 'ClearanceTag' instance.

        @param authorityName: The name of the person who is authorized to issue the tag 
        @param workEndTime: The time at which the clearance tag is scheduled to be removed 
        @param phaseCheckReqFlag: Set true if equipment phasing must be checked 
        @param deenergizeReqFlag: Set true if equipment must be deenergized 
        @param tagIssueTime: The time at which the clearance tag was issued 
        @param workDescription: Description of the work to be performed 
        @param workStartTime: The time at which the clearance tag is scheduled to be set. 
        @param groundReqFlag: Set true if equipment must be grounded 
        @param ConductingEquipment: Conducting equipment may have multiple clearance tags for authorized field work
        @param SafetyDocument:
        @param ClearanceTagType: The type of tag, depending on the purpose of the work to be performed and/or the type of supervisory control allowed.
        """
        #: The name of the person who is authorized to issue the tag 
        self.authorityName = authorityName

        #: The time at which the clearance tag is scheduled to be removed 
        self.workEndTime = workEndTime

        #: Set true if equipment phasing must be checked 
        self.phaseCheckReqFlag = phaseCheckReqFlag

        #: Set true if equipment must be deenergized 
        self.deenergizeReqFlag = deenergizeReqFlag

        #: The time at which the clearance tag was issued 
        self.tagIssueTime = tagIssueTime

        #: Description of the work to be performed 
        self.workDescription = workDescription

        #: The time at which the clearance tag is scheduled to be set. 
        self.workStartTime = workStartTime

        #: Set true if equipment must be grounded 
        self.groundReqFlag = groundReqFlag

        self._ConductingEquipment = None
        self.ConductingEquipment = ConductingEquipment

        self._SafetyDocument = None
        self.SafetyDocument = SafetyDocument

        self._ClearanceTagType = None
        self.ClearanceTagType = ClearanceTagType

        super(ClearanceTag, self).__init__(*args, **kw_args)

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

    def getSafetyDocument(self):
        
        return self._SafetyDocument

    def setSafetyDocument(self, value):
        if self._SafetyDocument is not None:
            filtered = [x for x in self.SafetyDocument.ClearanceTags if x != self]
            self._SafetyDocument._ClearanceTags = filtered

        self._SafetyDocument = value
        if self._SafetyDocument is not None:
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
            self._ClearanceTagType._ClearanceTags.append(self)

    ClearanceTagType = property(getClearanceTagType, setClearanceTagType)

