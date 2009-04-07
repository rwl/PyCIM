#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM13.Core import IdentifiedObject
from CIM13.Core import IrregularIntervalSchedule



from enthought.traits.api import Instance, List, Enum, Str, Bool
# <<< imports

# >>> imports

#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


SwitchState = Enum("close", "open")

#------------------------------------------------------------------------------
#  "ClearanceTagType" class:
#------------------------------------------------------------------------------

class ClearanceTagType(IdentifiedObject):
    """ Type of ClearanceTag. Could indicate the type of work to be performed and/or the type of supervisory control.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ClearanceTags = List(Instance("CIM13.Outage.ClearanceTag"))

    #--------------------------------------------------------------------------
    #  Begin clearanceTagType user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End clearanceTagType user definitions:
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

    # A switch may be operated by many schedules.
    Switches = List(Instance("CIM13.Wires.Switch"))

    # An OutageSchedule may operate many switches.
    OutageSchedule = Instance("CIM13.Outage.OutageSchedule")

    # The switch position that shall result from this SwitchingOperation
    newState = SwitchState

    # Time of operation in same units as OutageSchedule.xAxixUnits.
    operationTime = Str

    #--------------------------------------------------------------------------
    #  Begin switchingOperation user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End switchingOperation user definitions:
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

    # An OutageSchedule may operate many switches.
    SwitchingOperations = List(Instance("CIM13.Outage.SwitchingOperation"))

    # A power system resource may have an outage schedule
    PSR = Instance("CIM13.Core.PowerSystemResource")

    #--------------------------------------------------------------------------
    #  Begin outageSchedule user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End outageSchedule user definitions:
    #--------------------------------------------------------------------------

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
    ConductingEquipment = Instance("CIM13.Core.ConductingEquipment")

    ClearanceTagType = Instance("CIM13.Outage.ClearanceTagType")

    # Description of the work to be performed
    workDescription = Str

    # The time at which the clearance tag is scheduled to be set.
    workStartTime = Str

    # The name of the person who is authorized to issue the tag
    authorityName = Str

    # Set true if equipment must be deenergized
    deenergizeReqFlag = Bool

    # The time at which the clearance tag is scheduled to be removed
    workEndTime = Str

    # The time at which the clearance tag was issued
    tagIssueTime = Str

    # Set true if equipment must be grounded
    groundReqFlag = Bool

    # Set true if equipment phasing must be checked
    phaseCheckReqFlag = Bool

    #--------------------------------------------------------------------------
    #  Begin clearanceTag user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End clearanceTag user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
