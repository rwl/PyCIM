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
from CIM13.Core import PowerSystemResource



from enthought.traits.api import Instance, List, Enum, Bool, Float
# <<< imports

# >>> imports

#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


RemoteUnitType = Enum("RTU", "IED", "ControlCenter", "SubstationControlSystem")

Source = Enum("DEFAULTED", "SUBSTITUTED", "PROCESS")

#------------------------------------------------------------------------------
#  "RemotePoint" class:
#------------------------------------------------------------------------------

class RemotePoint(IdentifiedObject):
    """ For a RTU remote points correspond to telemetered values or control outputs. Other units (e.g. control centers) usually also contain calculated values.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    MemberOf_RemoteUnit = Instance("CIM13.SCADA.RemoteUnit")

    #--------------------------------------------------------------------------
    #  Begin remotePoint user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End remotePoint user definitions:
    #--------------------------------------------------------------------------

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
    Contain_RemoteUnits = List(Instance("CIM13.SCADA.RemoteUnit"))

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
    MemberOf_CommunicationLinks = List(Instance("CIM13.SCADA.CommunicationLink"))

    Contains_RemotePoints = List(Instance("CIM13.SCADA.RemotePoint"))

    # Type of remote unit.
    remoteUnitType = RemoteUnitType

    #--------------------------------------------------------------------------
    #  Begin remoteUnit user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End remoteUnit user definitions:
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

    Control = Instance("CIM13.Meas.Control")

    # Set to true if the actuator is remotely controlled.
    remoteControlled = Bool

    # The minimum set point value accepted by the remote control point.
    actuatorMinimum = Float

    # The maximum set point value accepted by the remote control point.
    actuatorMaximum = Float

    #--------------------------------------------------------------------------
    #  Begin remoteControl user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End remoteControl user definitions:
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
    MeasurementValue = Instance("CIM13.Meas.MeasurementValue")

    # The minimum value the telemetry item can return.
    sensorMinimum = Float

    # The maximum value the telemetry item can return.
    sensorMaximum = Float

    # The time interval between scans.
    scanInterval = Float

    # The smallest change in value to be reported.
    deadband = Float

    #--------------------------------------------------------------------------
    #  Begin remoteSource user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End remoteSource user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
