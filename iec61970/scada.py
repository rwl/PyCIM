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

""" Contains entities to model information used by Supervisory Control and Data Acquisition (SCADA) applications. Supervisory control supports operator control of equipment, such as opening or closing a breaker. Data acquisition gathers telemetered data from various sources.  The subtypes of the Telemetry entity deliberately match the UCA and IEC 61850 definitions.  This package also supports alarm presentation but it is not expected to be used by other applications. 
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from iec61970.core import PowerSystemResource
from iec61970.core import IdentifiedObject
from iec61970.domain import Float
from iec61970.domain import Seconds
from iec61970.domain import Boolean
from iec61970.domain import String
from iec61970.domain import AbsoluteDateTime



from enthought.traits.api import HasTraits, Instance, List, Enum, Float, Bool
# <<< imports

# >>> imports

#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


RemoteUnitType = Enum("RTU", "SubstationControlSystem", "ControlCenter", "IED")
# Source gives information related to the origin of a value. The value may be acquired from the process, defaulted or substituted.
Source = Enum("PROCESS", "DEFAULTED", "SUBSTITUTED", desc="Source gives information related to the origin of a value. The value may be acquired from the process, defaulted or substituted.")

#------------------------------------------------------------------------------
#  "CommunicationLink" class:
#------------------------------------------------------------------------------

class CommunicationLink(PowerSystemResource):
    """ The connection to remote units is through one or more communication links. Reduntant links may exist. The CommunicationLink class inherit PowerSystemResource. The intention is to allow CommunicationLinks to have Measurements. These Measurements can be used to model link status as operational, out of service, unit failure etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # RTUs may be attached to communication links.
    Contain_RemoteUnits = List(Instance("iec61970.scada.RemoteUnit"))

    #--------------------------------------------------------------------------
    #  Begin communicationLink user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End communicationLink user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RemoteUnit" class:
#------------------------------------------------------------------------------

class RemoteUnit(PowerSystemResource):
    """ A remote unit can be a RTU, IED, substation control system, control center etc. The communication with the remote unit can be through various standard protocols (e.g. IEC 61870, IEC 61850) or non standard protocols (e.g. DNP, RP570 etc.). A remote unit contain remote data points that might be telemetered, collected or calculated. The RemoteUnit class inherit PowerSystemResource. The intention is to allow RemotUnits to have Measurements. These Measurements can be used to model unit status as operational, out of service, unit failure etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # RTUs may be attached to communication links.
    MemberOf_CommunicationLinks = List(Instance("iec61970.scada.CommunicationLink"))

    Contains_RemotePoints = List(Instance("iec61970.scada.RemotePoint"))

    # A remote unit can be a RTU, IED, substation control system, control center etc. 
    remoteUnitType = RemoteUnitType

    #--------------------------------------------------------------------------
    #  Begin remoteUnit user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End remoteUnit user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RemotePoint" class:
#------------------------------------------------------------------------------

class RemotePoint(IdentifiedObject):
    """ For a RTU remote points correspond to telemetered values or control outputs. Other units (e.g. control centers) usually also contain calculated values.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    MemberOf_RemoteUnit = Instance("iec61970.scada.RemoteUnit", allow_none=False)

    #--------------------------------------------------------------------------
    #  Begin remotePoint user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End remotePoint user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SCADAVersion" class:
#------------------------------------------------------------------------------

class SCADAVersion(HasTraits):
    version = String

    date = AbsoluteDateTime

    #--------------------------------------------------------------------------
    #  Begin sCADAVersion user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End sCADAVersion user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RemoteSource" class:
#------------------------------------------------------------------------------

class RemoteSource(RemotePoint):
    """ Remote sources are state variables that are telemetered or calculated within the remote unit.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Links to the physical telemetered point associated with this measurement.
    MeasurementValue = Instance("iec61970.meas.MeasurementValue", allow_none=False)

    # The maximum value the telemetry item can return.
    sensorMaximum = Float

    # The minimum value the telemetry item can return.
    sensorMinimum = Float

    # The time interval between scans.
    scanInterval = Seconds

    # The smallest change in value to be reported.
    deadband = Float

    #--------------------------------------------------------------------------
    #  Begin remoteSource user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End remoteSource user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RemoteControl" class:
#------------------------------------------------------------------------------

class RemoteControl(RemotePoint):
    """ Remote controls are ouputs that are sent by the remote unit to actuators in the process.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Control = Instance("iec61970.meas.Control", allow_none=False)

    remoteControlled = Boolean

    actuatorMaximum = Float

    actuatorMinimum = Float

    #--------------------------------------------------------------------------
    #  Begin remoteControl user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End remoteControl user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
