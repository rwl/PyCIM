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

""" Contains entities to model information used by Supervisory Control and Data Acquisition (SCADA) applications. Supervisory control supports operator control of equipment, such as opening or closing a breaker. Data acquisition gathers telemetered data from various sources.  The subtypes of the Telemetry entity deliberately match the UCA and IEC 61850 definitions.  This package also supports alarm presentation but it is not expected to be used by other applications.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.Core import IdentifiedObject
from CIM.Core import PowerSystemResource
from CIM.Domain import Seconds



from enthought.traits.api import Instance, List, Property, Enum, Float, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Type of remote unit.
RemoteUnitType = Enum("IED", "SubstationControlSystem", "RTU", "ControlCenter", desc="Type of remote unit.")
# Source gives information related to the origin of a value.
Source = Enum("DEFAULTED", "SUBSTITUTED", "PROCESS", desc="Source gives information related to the origin of a value.")

#------------------------------------------------------------------------------
#  "RemotePoint" class:
#------------------------------------------------------------------------------

class RemotePoint(IdentifiedObject):
    """ For a RTU remote points correspond to telemetered values or control outputs. Other units (e.g. control centers) usually also contain calculated values.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Remote unit this point belongs to.
    MemberOf_RemoteUnit = Instance("CIM.SCADA.RemoteUnit",
        desc="Remote unit this point belongs to.",
        transient=True,
        opposite="Contains_RemotePoints",
        editor=InstanceEditor(name="_remoteunits"))

    def _get_remoteunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.SCADA.RemoteUnit" ]
        else:
            return []

    _remoteunits = Property(fget=_get_remoteunits)

    #--------------------------------------------------------------------------
    #  Begin "RemotePoint" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "MemberOf_RemoteUnit",
                label="References"),
            dock="tab"),
        id="CIM.SCADA.RemotePoint",
        title="RemotePoint",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RemotePoint" user definitions:
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
    MemberOf_CommunicationLinks = List(Instance("CIM.SCADA.CommunicationLink"),
        desc="RTUs may be attached to communication links.")

    # Remote points this Remote unit contains.
    Contains_RemotePoints = List(Instance("CIM.SCADA.RemotePoint"),
        desc="Remote points this Remote unit contains.")

    # Type of remote unit.
    remoteUnitType = RemoteUnitType(desc="Type of remote unit.")

    #--------------------------------------------------------------------------
    #  Begin "RemoteUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "remoteUnitType",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "MemberOf_CommunicationLinks", "Contains_RemotePoints",
                label="References"),
            dock="tab"),
        id="CIM.SCADA.RemoteUnit",
        title="RemoteUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RemoteUnit" user definitions:
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
    Contain_RemoteUnits = List(Instance("CIM.SCADA.RemoteUnit"),
        desc="RTUs may be attached to communication links.")

    #--------------------------------------------------------------------------
    #  Begin "CommunicationLink" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "Contain_RemoteUnits",
                label="References"),
            dock="tab"),
        id="CIM.SCADA.CommunicationLink",
        title="CommunicationLink",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CommunicationLink" user definitions:
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

    # The Control for the RemoteControl point.
    Control = Instance("CIM.Meas.Control",
        desc="The Control for the RemoteControl point.",
        transient=True,
        opposite="RemoteControl",
        editor=InstanceEditor(name="_controls"))

    def _get_controls(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Meas.Control" ]
        else:
            return []

    _controls = Property(fget=_get_controls)

    # The maximum set point value accepted by the remote control point.
    actuatorMaximum = Float(desc="The maximum set point value accepted by the remote control point.")

    # The minimum set point value accepted by the remote control point.
    actuatorMinimum = Float(desc="The minimum set point value accepted by the remote control point.")

    # Set to true if the actuator is remotely controlled.
    remoteControlled = Bool(desc="Set to true if the actuator is remotely controlled.")

    #--------------------------------------------------------------------------
    #  Begin "RemoteControl" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "actuatorMaximum", "actuatorMinimum", "remoteControlled",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "MemberOf_RemoteUnit", "Control",
                label="References"),
            dock="tab"),
        id="CIM.SCADA.RemoteControl",
        title="RemoteControl",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RemoteControl" user definitions:
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

    # Link to the physical telemetered point associated with this measurement.
    MeasurementValue = Instance("CIM.Meas.MeasurementValue",
        desc="Link to the physical telemetered point associated with this measurement.",
        transient=True,
        opposite="RemoteSource",
        editor=InstanceEditor(name="_measurementvalues"))

    def _get_measurementvalues(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Meas.MeasurementValue" ]
        else:
            return []

    _measurementvalues = Property(fget=_get_measurementvalues)

    # The maximum value the telemetry item can return.
    sensorMaximum = Float(desc="The maximum value the telemetry item can return.")

    # The time interval between scans.
    scanInterval = Seconds(desc="The time interval between scans.")

    # The minimum value the telemetry item can return.
    sensorMinimum = Float(desc="The minimum value the telemetry item can return.")

    # The smallest change in value to be reported.
    deadband = Float(desc="The smallest change in value to be reported.")

    #--------------------------------------------------------------------------
    #  Begin "RemoteSource" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "sensorMaximum", "scanInterval", "sensorMinimum", "deadband",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "MemberOf_RemoteUnit", "MeasurementValue",
                label="References"),
            dock="tab"),
        id="CIM.SCADA.RemoteSource",
        title="RemoteSource",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RemoteSource" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
