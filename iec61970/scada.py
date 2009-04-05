# @copyright: 2009 Richard W. Lincoln
# @contact: r.w.lincoln@gmail.com
# @license: GPLv3

""" Contains entities to model information used by Supervisory Control and Data Acquisition (SCADA) applications. Supervisory control supports operator control of equipment, such as opening or closing a breaker. Data acquisition gathers telemetered data from various sources.  The subtypes of the Telemetry entity deliberately match the UCA and IEC 61850 definitions.  This package also supports alarm presentation but it is not expected to be used by other applications. 
"""
from iec61970.core import PowerSystemResource
from iec61970.core import IdentifiedObject
from iec61970.domain import Float
from iec61970.domain import Seconds
from iec61970.domain import Boolean
from iec61970.domain import String
from iec61970.domain import AbsoluteDateTime



from enthought.traits.api import HasTraits, Instance, List, Enum, Float, Bool



RemoteUnitType = Enum("RTU", "SubstationControlSystem", "ControlCenter", "IED")
# Source gives information related to the origin of a value. The value may be acquired from the process, defaulted or substituted.
Source = Enum("PROCESS", "DEFAULTED", "SUBSTITUTED", desc="Source gives information related to the origin of a value. The value may be acquired from the process, defaulted or substituted.")

class CommunicationLink(PowerSystemResource):
    """ The connection to remote units is through one or more communication links. Reduntant links may exist. The CommunicationLink class inherit PowerSystemResource. The intention is to allow CommunicationLinks to have Measurements. These Measurements can be used to model link status as operational, out of service, unit failure etc.
    """
    # RTUs may be attached to communication links.
    Contain_RemoteUnits = List(Instance("iec61970.scada.RemoteUnit.RemoteUnit"))

class RemoteUnit(PowerSystemResource):
    """ A remote unit can be a RTU, IED, substation control system, control center etc. The communication with the remote unit can be through various standard protocols (e.g. IEC 61870, IEC 61850) or non standard protocols (e.g. DNP, RP570 etc.). A remote unit contain remote data points that might be telemetered, collected or calculated. The RemoteUnit class inherit PowerSystemResource. The intention is to allow RemotUnits to have Measurements. These Measurements can be used to model unit status as operational, out of service, unit failure etc.
    """
    # RTUs may be attached to communication links.
    MemberOf_CommunicationLinks = List(Instance("iec61970.scada.CommunicationLink.CommunicationLink"))
    Contains_RemotePoints = List(Instance("iec61970.scada.RemotePoint.RemotePoint"))
    # A remote unit can be a RTU, IED, substation control system, control center etc. 
    remoteUnitType = RemoteUnitType

class RemotePoint(IdentifiedObject):
    """ For a RTU remote points correspond to telemetered values or control outputs. Other units (e.g. control centers) usually also contain calculated values.
    """
    MemberOf_RemoteUnit = Instance("iec61970.scada.RemoteUnit.RemoteUnit", allow_none=False)

class SCADAVersion(HasTraits):
    version = String
    date = AbsoluteDateTime

class RemoteSource(RemotePoint):
    """ Remote sources are state variables that are telemetered or calculated within the remote unit.
    """
    # Links to the physical telemetered point associated with this measurement.
    MeasurementValue = Instance("iec61970.meas.MeasurementValue.MeasurementValue", allow_none=False)
    # The maximum value the telemetry item can return.
    sensorMaximum = Float
    # The minimum value the telemetry item can return.
    sensorMinimum = Float
    # The time interval between scans.
    scanInterval = Seconds
    # The smallest change in value to be reported.
    deadband = Float

class RemoteControl(RemotePoint):
    """ Remote controls are ouputs that are sent by the remote unit to actuators in the process.
    """
    Control = Instance("iec61970.meas.Control.Control", allow_none=False)
    remoteControlled = Boolean
    actuatorMaximum = Float
    actuatorMinimum = Float


