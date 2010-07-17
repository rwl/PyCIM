#------------------------------------------------------------------------------
# Copyright (C) 2010 Richard Lincoln
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------

""" An extension to the Core and Wires packages that models information on the current and planned network configuration. These entities are optional within typical network applications.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61970.Core import IrregularIntervalSchedule



from enthought.traits.api import Instance, List, Property, Enum, Str, Date, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Possible states for a switch.
SwitchState = Enum("open", "close", desc="Possible states for a switch.")

#------------------------------------------------------------------------------
#  "ClearanceTag" class:
#------------------------------------------------------------------------------

class ClearanceTag(IdentifiedObject):
    """ A clearance tag that is used to authorize and schedule work on conducting equipment in the field. Tagged equipment is not available for commercial service.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Conducting equipment may have multiple clearance tags for authorized field work
    ConductingEquipment = Instance("CIM.IEC61970.Core.ConductingEquipment",
        desc="Conducting equipment may have multiple clearance tags for authorized field work",
        transient=True,
        opposite="ClearanceTags",
        editor=InstanceEditor(name="_conductingequipments"))

    def _get_conductingequipments(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.ConductingEquipment" ]
        else:
            return []

    _conductingequipments = Property(fget=_get_conductingequipments)

    SafetyDocument = Instance("CIM.IEC61968.Informative.InfOperations.SafetyDocument",
        transient=True,
        opposite="ClearanceTags",
        editor=InstanceEditor(name="_safetydocuments"))

    def _get_safetydocuments(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfOperations.SafetyDocument" ]
        else:
            return []

    _safetydocuments = Property(fget=_get_safetydocuments)

    # The type of tag, depending on the purpose of the work to be performed and/or the type of supervisory control allowed.
    ClearanceTagType = Instance("CIM.IEC61970.Outage.ClearanceTagType",
        desc="The type of tag, depending on the purpose of the work to be performed and/or the type of supervisory control allowed.",
        transient=True,
        opposite="ClearanceTags",
        editor=InstanceEditor(name="_clearancetagtypes"))

    def _get_clearancetagtypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Outage.ClearanceTagType" ]
        else:
            return []

    _clearancetagtypes = Property(fget=_get_clearancetagtypes)

    # The name of the person who is authorized to issue the tag
    authorityName = Str(desc="The name of the person who is authorized to issue the tag")

    # The time at which the clearance tag is scheduled to be removed
    workEndTime = Date(desc="The time at which the clearance tag is scheduled to be removed")

    # Set true if equipment phasing must be checked
    phaseCheckReqFlag = Bool(desc="Set true if equipment phasing must be checked")

    # Set true if equipment must be deenergized
    deenergizeReqFlag = Bool(desc="Set true if equipment must be deenergized")

    # The time at which the clearance tag was issued
    tagIssueTime = Date(desc="The time at which the clearance tag was issued")

    # Description of the work to be performed
    workDescription = Str(desc="Description of the work to be performed")

    # The time at which the clearance tag is scheduled to be set.
    workStartTime = Date(desc="The time at which the clearance tag is scheduled to be set.")

    # Set true if equipment must be grounded
    groundReqFlag = Bool(desc="Set true if equipment must be grounded")

    #--------------------------------------------------------------------------
    #  Begin "ClearanceTag" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "authorityName", "workEndTime", "phaseCheckReqFlag", "deenergizeReqFlag", "tagIssueTime", "workDescription", "workStartTime", "groundReqFlag",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ConductingEquipment", "SafetyDocument", "ClearanceTagType",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Outage.ClearanceTag",
        title="ClearanceTag",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ClearanceTag" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ClearanceTagType" class:
#------------------------------------------------------------------------------

class ClearanceTagType(IdentifiedObject):
    """ Type of ClearanceTag. Could indicate the type of work to be performed and/or the type of supervisory control.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The ClearanceTags currently being defined for this type.
    ClearanceTags = List(Instance("CIM.IEC61970.Outage.ClearanceTag"),
        desc="The ClearanceTags currently being defined for this type.")

    #--------------------------------------------------------------------------
    #  Begin "ClearanceTagType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ClearanceTags",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Outage.ClearanceTagType",
        title="ClearanceTagType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ClearanceTagType" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OutageSchedule" class:
#------------------------------------------------------------------------------

class OutageSchedule(IrregularIntervalSchedule):
    """ The period of time that a piece of equipment is out of service, for example, for maintenance or testing; including the equipment's active power rating while under maintenance. The X-axis represents absolute time and the Y-axis represents the equipment's available rating while out of service.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A power system resource may have an outage schedule
    PowerSystemResource = Instance("CIM.IEC61970.Core.PowerSystemResource",
        desc="A power system resource may have an outage schedule",
        transient=True,
        opposite="OutageSchedule",
        editor=InstanceEditor(name="_powersystemresources"))

    def _get_powersystemresources(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.PowerSystemResource" ]
        else:
            return []

    _powersystemresources = Property(fget=_get_powersystemresources)

    # An OutageSchedule may operate many switches.
    SwitchingOperations = List(Instance("CIM.IEC61970.Outage.SwitchingOperation"),
        desc="An OutageSchedule may operate many switches.")

    PlannedOutage = Instance("CIM.IEC61968.Informative.InfOperations.PlannedOutage",
        transient=True,
        opposite="OutageSchedules",
        editor=InstanceEditor(name="_plannedoutages"))

    def _get_plannedoutages(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfOperations.PlannedOutage" ]
        else:
            return []

    _plannedoutages = Property(fget=_get_plannedoutages)

    #--------------------------------------------------------------------------
    #  Begin "OutageSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "value2Multiplier", "value1Unit", "value2Unit", "value1Multiplier", "startTime",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints", "PowerSystemResource", "SwitchingOperations", "PlannedOutage",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Outage.OutageSchedule",
        title="OutageSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OutageSchedule" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SwitchingOperation" class:
#------------------------------------------------------------------------------

class SwitchingOperation(IdentifiedObject):
    """ A SwitchingOperation is used to define individual switch operations for an OutageSchedule. This OutageSchedule may be associated with another item of Substation such as a Transformer, Line, or Generator; or with the Switch itself as a PowerSystemResource. A Switch may be referenced by many OutageSchedules.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # An OutageSchedule may operate many switches.
    OutageSchedule = Instance("CIM.IEC61970.Outage.OutageSchedule",
        desc="An OutageSchedule may operate many switches.",
        transient=True,
        opposite="SwitchingOperations",
        editor=InstanceEditor(name="_outageschedules"))

    def _get_outageschedules(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Outage.OutageSchedule" ]
        else:
            return []

    _outageschedules = Property(fget=_get_outageschedules)

    # A switch may be operated by many schedules.
    Switches = List(Instance("CIM.IEC61970.Wires.Switch"),
        desc="A switch may be operated by many schedules.")

    # The switch position that shall result from this SwitchingOperation
    newState = SwitchState(desc="The switch position that shall result from this SwitchingOperation")

    # Time of operation in same units as OutageSchedule.xAxixUnits.
    operationTime = Date(desc="Time of operation in same units as OutageSchedule.xAxixUnits.")

    #--------------------------------------------------------------------------
    #  Begin "SwitchingOperation" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "newState", "operationTime",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "OutageSchedule", "Switches",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Outage.SwitchingOperation",
        title="SwitchingOperation",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SwitchingOperation" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
