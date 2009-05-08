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

from CIM13r19.Core import IdentifiedObject
from CIM13r19.Core import PowerSystemResource



from enthought.traits.api import Instance, List, Property, Enum, Bool, Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
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

    MemberOf_RemoteUnit = Instance("CIM13r19.SCADA.RemoteUnit",
        transient=True,
        opposite="Contains_RemotePoints",
        editor=InstanceEditor(name="_remoteunits"))

    def _get_remoteunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.SCADA.RemoteUnit" ]
        else:
            return []

    _remoteunits = Property(fget=_get_remoteunits)

    #--------------------------------------------------------------------------
    #  Begin "RemotePoint" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "MemberOf_RemoteUnit",
                label="References"),
            dock="tab"),
        id="CIM13r19.SCADA.RemotePoint",
        title="RemotePoint",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RemotePoint" user definitions:
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
    Contain_RemoteUnits = List(Instance("CIM13r19.SCADA.RemoteUnit"),
        desc="RTUs may be attached to communication links.")

    #--------------------------------------------------------------------------
    #  Begin "CommunicationLink" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "Contain_RemoteUnits",
                label="References"),
            dock="tab"),
        id="CIM13r19.SCADA.CommunicationLink",
        title="CommunicationLink",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CommunicationLink" user definitions:
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
    MemberOf_CommunicationLinks = List(Instance("CIM13r19.SCADA.CommunicationLink"),
        desc="RTUs may be attached to communication links.")

    Contains_RemotePoints = List(Instance("CIM13r19.SCADA.RemotePoint"))

    # Type of remote unit.
    remoteUnitType = RemoteUnitType(desc="Type of remote unit.")

    #--------------------------------------------------------------------------
    #  Begin "RemoteUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "remoteUnitType",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "MemberOf_CommunicationLinks", "Contains_RemotePoints",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.SCADA.RemoteUnit",
        title="RemoteUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RemoteUnit" user definitions:
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

    Control = Instance("CIM13r19.Meas.Control",
        transient=True,
        opposite="RemoteControl",
        editor=InstanceEditor(name="_controls"))

    def _get_controls(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Meas.Control" ]
        else:
            return []

    _controls = Property(fget=_get_controls)

    # Set to true if the actuator is remotely controlled.
    remoteControlled = Bool(desc="Set to true if the actuator is remotely controlled.")

    # The minimum set point value accepted by the remote control point.
    actuatorMinimum = Float(desc="The minimum set point value accepted by the remote control point.")

    # The maximum set point value accepted by the remote control point.
    actuatorMaximum = Float(desc="The maximum set point value accepted by the remote control point.")

    #--------------------------------------------------------------------------
    #  Begin "RemoteControl" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "remoteControlled", "actuatorMinimum", "actuatorMaximum",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "MemberOf_RemoteUnit", "Control",
                label="References"),
            dock="tab"),
        id="CIM13r19.SCADA.RemoteControl",
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

    # Links to the physical telemetered point associated with this measurement.
    MeasurementValue = Instance("CIM13r19.Meas.MeasurementValue",
        desc="Links to the physical telemetered point associated with this measurement.",
        transient=True,
        opposite="RemoteSource",
        editor=InstanceEditor(name="_measurementvalues"))

    def _get_measurementvalues(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Meas.MeasurementValue" ]
        else:
            return []

    _measurementvalues = Property(fget=_get_measurementvalues)

    # The minimum value the telemetry item can return.
    sensorMinimum = Float(desc="The minimum value the telemetry item can return.")

    # The maximum value the telemetry item can return.
    sensorMaximum = Float(desc="The maximum value the telemetry item can return.")

    # The time interval between scans.
    scanInterval = Float(desc="The time interval between scans.")

    # The smallest change in value to be reported.
    deadband = Float(desc="The smallest change in value to be reported.")

    #--------------------------------------------------------------------------
    #  Begin "RemoteSource" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "sensorMinimum", "sensorMaximum", "scanInterval", "deadband",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "MemberOf_RemoteUnit", "MeasurementValue",
                label="References"),
            dock="tab"),
        id="CIM13r19.SCADA.RemoteSource",
        title="RemoteSource",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RemoteSource" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
