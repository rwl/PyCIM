# @copyright: 2009 Richard W. Lincoln
# @contact: r.w.lincoln@gmail.com
# @license: GPLv3

""" An extension to the Core and Wires packages that models information on the current and planned network configuration. These entities are optional within typical network applications.
"""
from iec61970.core import IdentifiedObject
from iec61970.core import IrregularIntervalSchedule
from iec61970.domain import String
from iec61970.domain import Boolean
from iec61970.domain import AbsoluteDateTime



from enthought.traits.api import HasTraits, Instance, List, Enum, Bool


# Possible states for a switch.
SwitchState = Enum("open", "close", desc="Possible states for a switch.")

class ClearanceTag(IdentifiedObject):
    """ A clearance tag that is used to authorize and schedule work on conducting equipment in the field. Tagged equipment is not available for commercial service.
    """
    # Conducting equipment may have multiple clearance tags for authorized field work
    ConductingEquipment = Instance("iec61970.core.ConductingEquipment.ConductingEquipment", allow_none=False)
    # The type of tag, depending on the purpose of the work to be performed and/or the type of supervisory control allowed.
    ClearanceTagType = Instance("iec61970.outage.ClearanceTagType.ClearanceTagType", allow_none=False)
    # The name of the person who is authorized to issue the tag
    authorityName = String
    # Flag = YES if equipment must be deenergized
    deenergizeReqFlag = Boolean
    # Flag = YES if equipment must be grounded
    groundReqFlag = Boolean
    # Flag = YES if equipment phasing must be checked
    phaseCheckReqFlag = Boolean
    # The time at which the clearance tag was issued
    tagIssueTime = AbsoluteDateTime
    # Description of the work to be performed
    workDescription = String
    # The time at which the clearance tag is scheduled to be removed
    workEndTime = AbsoluteDateTime
    # WorkStartTime
    workStartTime = AbsoluteDateTime

class OutageSchedule(IrregularIntervalSchedule):
    """ The period of time that a piece of equipment is out of service, for example, for maintenance or testing; including the equipment's active power rating while under maintenance. The X-axis represents absolute time and the Y-axis represents the equipment's available rating while out of service.
    """
    # An OutageSchedule may operate many switches.
    SwitchingOperations = List(Instance("iec61970.outage.SwitchingOperation.SwitchingOperation"))
    # A power system resource may have an outage schedule
    PSR = Instance("iec61970.core.PowerSystemResource.PowerSystemResource", allow_none=False)

class SwitchingOperation(IdentifiedObject):
    """ A SwitchingOperation is used to define individual switch operations for an OutageSchedule. This OutageSchedule may be associated with another item of Substation such as a Transformer, Line, or Generator; or with the Switch itself as a PowerSystemResource. A Switch may be referenced by many OutageSchedules.
    """
    # An OutageSchedule may operate many switches.
    OutageSchedule = Instance("iec61970.outage.OutageSchedule.OutageSchedule")
    # A switch may be operated by many schedules.
    Switches = List(Instance("iec61970.wires.Switch.Switch"))
    # Time of operation in same units as OutageSchedule.xAxixUnits.
    operationTime = AbsoluteDateTime
    newState = SwitchState

class OutageVersion(HasTraits):
    version = String
    date = AbsoluteDateTime

class ClearanceTagType(IdentifiedObject):
    """ Type of ClearanceTag. Could indicate the type of work to be performed and/or the type of supervisory control.
    """
    # The ClearanceTags currently being defined for this type.
    ClearanceTags = List(Instance("iec61970.outage.ClearanceTag.ClearanceTag"))


