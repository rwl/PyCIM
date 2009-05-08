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
from CIM13r19 import Element
from CIM13r19.SCADA import Source



from enthought.traits.api import Instance, List, Property, Enum, Int, Float, Bool, Str
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


Validity = Enum("GOOD", "QUESTIONABLE", "INVALID")

#------------------------------------------------------------------------------
#  "Measurement" class:
#------------------------------------------------------------------------------

class Measurement(IdentifiedObject):
    """ A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  Two possible paths exist: 1) Measurement-Terminal- ConnectivityNode-Terminal-ConductingEquipment 2) Measurement-Terminal-ConductingEquipment Alternative 2 is the only allowed use.  When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.
    Terminal = Instance("CIM13r19.Core.Terminal",
        desc="One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.",
        transient=True,
        opposite="Measurements",
        editor=InstanceEditor(name="_terminals"))

    def _get_terminals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.Terminal" ]
        else:
            return []

    _terminals = Property(fget=_get_terminals)

    # Measurement-PSR defines the measurements in the naming hierarchy.
    MemberOf_PSR = Instance("CIM13r19.Core.PowerSystemResource",
        desc="Measurement-PSR defines the measurements in the naming hierarchy.",
        transient=True,
        opposite="Contains_Measurements",
        editor=InstanceEditor(name="_powersystemresources"))

    def _get_powersystemresources(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.PowerSystemResource" ]
        else:
            return []

    _powersystemresources = Property(fget=_get_powersystemresources)

    Unit = Instance("CIM13r19.Core.Unit",
        transient=True,
        opposite="Measurements",
        editor=InstanceEditor(name="_units"))

    def _get_units(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.Unit" ]
        else:
            return []

    _units = Property(fget=_get_units)

    # A measurement has a measurement type.
    MeasurementType = Instance("CIM13r19.Meas.MeasurementType",
        desc="A measurement has a measurement type.",
        transient=True,
        opposite="Measurements",
        editor=InstanceEditor(name="_measurementtypes"))

    def _get_measurementtypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Meas.MeasurementType" ]
        else:
            return []

    _measurementtypes = Property(fget=_get_measurementtypes)

    #--------------------------------------------------------------------------
    #  Begin "Measurement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Terminal", "MemberOf_PSR", "Unit", "MeasurementType",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.Measurement",
        title="Measurement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Measurement" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Control" class:
#------------------------------------------------------------------------------

class Control(IdentifiedObject):
    """ Control is used for supervisory/device control. It represents control outputs that are used to change the state in a process, e.g. close or open breaker, a set point value or a raise lower command.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Unit = Instance("CIM13r19.Core.Unit",
        transient=True,
        opposite="Controls",
        editor=InstanceEditor(name="_units"))

    def _get_units(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.Unit" ]
        else:
            return []

    _units = Property(fget=_get_units)

    ControlType = Instance("CIM13r19.Meas.ControlType",
        transient=True,
        opposite="Controls",
        editor=InstanceEditor(name="_controltypes"))

    def _get_controltypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Meas.ControlType" ]
        else:
            return []

    _controltypes = Property(fget=_get_controltypes)

    RemoteControl = Instance("CIM13r19.SCADA.RemoteControl",
        transient=True,
        opposite="Control",
        editor=InstanceEditor(name="_remotecontrols"))

    def _get_remotecontrols(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.SCADA.RemoteControl" ]
        else:
            return []

    _remotecontrols = Property(fget=_get_remotecontrols)

    # The association gives the control output that is used to actually govern a regulating device, e.g. the magnetization of a synchronous machine or capacitor bank breaker actuators.
    ControlledBy_RegulatingCondEq = Instance("CIM13r19.Wires.RegulatingCondEq",
        desc="The association gives the control output that is used to actually govern a regulating device, e.g. the magnetization of a synchronous machine or capacitor bank breaker actuators.",
        transient=True,
        opposite="Controls",
        editor=InstanceEditor(name="_regulatingcondeqs"))

    def _get_regulatingcondeqs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Wires.RegulatingCondEq" ]
        else:
            return []

    _regulatingcondeqs = Property(fget=_get_regulatingcondeqs)

    # Indicates that a client is currently sending control commands that has not completed
    operationInProgress = Bool(desc="Indicates that a client is currently sending control commands that has not completed")

    # The last time a control output was sent
    timeStamp = Str(desc="The last time a control output was sent")

    #--------------------------------------------------------------------------
    #  Begin "Control" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "operationInProgress", "timeStamp",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Unit", "ControlType", "RemoteControl", "ControlledBy_RegulatingCondEq",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.Control",
        title="Control",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Control" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ControlType" class:
#------------------------------------------------------------------------------

class ControlType(IdentifiedObject):
    """ Specifies the type of Control, e.g. BreakerOn/Off, GeneratorVoltageSetPoint, TieLineFlow etc. The ControlType.name shall be unique among all specified types and describe the type. The ControlType.aliasName is meant to be used for localization.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Controls = List(Instance("CIM13r19.Meas.Control"))

    #--------------------------------------------------------------------------
    #  Begin "ControlType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Controls",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.ControlType",
        title="ControlType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ControlType" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LimitSet" class:
#------------------------------------------------------------------------------

class LimitSet(IdentifiedObject):
    """ Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets corresponding to seasonal or other changing conditions. The condition is captured in the name and description attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used this way.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls.
    isPercentageLimits = Bool(desc="Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls.")

    #--------------------------------------------------------------------------
    #  Begin "LimitSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "isPercentageLimits",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.LimitSet",
        title="LimitSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LimitSet" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MeasurementValue" class:
#------------------------------------------------------------------------------

class MeasurementValue(IdentifiedObject):
    """ The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A MeasurementValue has a MeasurementValueQuality associated with it.
    MeasurementValueQuality = Instance("CIM13r19.Meas.MeasurementValueQuality",
        desc="A MeasurementValue has a MeasurementValueQuality associated with it.",
        transient=True,
        opposite="MeasurementValue",
        editor=InstanceEditor(name="_measurementvaluequalitys"))

    def _get_measurementvaluequalitys(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Meas.MeasurementValueQuality" ]
        else:
            return []

    _measurementvaluequalitys = Property(fget=_get_measurementvaluequalitys)

    # Links to the physical telemetered point associated with this measurement.
    RemoteSource = Instance("CIM13r19.SCADA.RemoteSource",
        desc="Links to the physical telemetered point associated with this measurement.",
        transient=True,
        opposite="MeasurementValue",
        editor=InstanceEditor(name="_remotesources"))

    def _get_remotesources(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.SCADA.RemoteSource" ]
        else:
            return []

    _remotesources = Property(fget=_get_remotesources)

    MeasurementValueSource = Instance("CIM13r19.Meas.MeasurementValueSource",
        transient=True,
        opposite="MeasurementValues",
        editor=InstanceEditor(name="_measurementvaluesources"))

    def _get_measurementvaluesources(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Meas.MeasurementValueSource" ]
        else:
            return []

    _measurementvaluesources = Property(fget=_get_measurementvaluesources)

    # The limit, expressed as a percentage of the sensor maximum, that errors will not exceed when the sensor is used under  reference conditions.
    sensorAccuracy = Float(desc="The limit, expressed as a percentage of the sensor maximum, that errors will not exceed when the sensor is used under  reference conditions.")

    # The time when the value was last updated
    timeStamp = Str(desc="The time when the value was last updated")

    #--------------------------------------------------------------------------
    #  Begin "MeasurementValue" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "sensorAccuracy", "timeStamp",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "MeasurementValueQuality", "RemoteSource", "MeasurementValueSource",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.MeasurementValue",
        title="MeasurementValue",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MeasurementValue" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ValueAliasSet" class:
#------------------------------------------------------------------------------

class ValueAliasSet(IdentifiedObject):
    """ Describes the translation of a set of values into a name and is intendend to facilitate cusom translations. Each ValueAliasSet has a name, description etc. A specific Measurement may represent a discrete state like Open, Closed, Intermediate etc. This requires a translation from the MeasurementValue.value number to a string, e.g. 0->'Invalid', 1->'Open', 2->'Closed', 3->'Intermediate'. Each ValueToAlias member in ValueAliasSet.Value describe a mapping for one particular value to a name.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Values = List(Instance("CIM13r19.Meas.ValueToAlias"))

    Commands = List(Instance("CIM13r19.Meas.Command"))

    Measurements = List(Instance("CIM13r19.Meas.Discrete"))

    #--------------------------------------------------------------------------
    #  Begin "ValueAliasSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Values", "Commands", "Measurements",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.ValueAliasSet",
        title="ValueAliasSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ValueAliasSet" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Quality61850" class:
#------------------------------------------------------------------------------

class Quality61850(Element):
    """ Quality flags in this class are as defined in IEC 61850, except for estimatorReplaced, which has been included in this class for convenience.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Measurement value is beyond a predefined range of value.
    outOfRange = Bool(desc="Measurement value is beyond a predefined range of value.")

    # Measurement value is beyond the capability of being  represented properly. For example, a counter value overflows from maximum count back to a value of zero.
    overFlow = Bool(desc="Measurement value is beyond the capability of being  represented properly. For example, a counter value overflows from maximum count back to a value of zero.")

    # Measurement value is blocked and hence unavailable for transmission.
    operatorBlocked = Bool(desc="Measurement value is blocked and hence unavailable for transmission.")

    # A correlation function has detected that the value is not consitent with other values. Typically set by a network State Estimator.
    suspect = Bool(desc="A correlation function has detected that the value is not consitent with other values. Typically set by a network State Estimator.")

    # To prevent some overload of the communication it is sensible to detect and suppress oscillating (fast changing) binary inputs. If a signal changes in a defined time (tosc) twice in the same direction (from 0 to 1 or from 1 to 0) then oscillation is detected and the detail quality identifier 'oscillatory' is set. If it is detected a configured numbers of transient changes could be passed by. In this time the validity status 'questionable' is set. If after this defined numbers of changes the signal is still in the oscillating state the value shall be set either to the opposite state of the previous stable value or to a defined default value. In this case the validity status 'questionable' is reset and 'invalid' is set as long as the signal is oscillating. If it is configured such that no transient changes should be passed by then the validity status 'invalid' is set immediately in addition to the detail quality identifier 'oscillatory' (used for status information only).
    oscillatory = Bool(desc="To prevent some overload of the communication it is sensible to detect and suppress oscillating (fast changing) binary inputs. If a signal changes in a defined time (tosc) twice in the same direction (from 0 to 1 or from 1 to 0) then oscillation is detected and the detail quality identifier 'oscillatory' is set. If it is detected a configured numbers of transient changes could be passed by. In this time the validity status 'questionable' is set. If after this defined numbers of changes the signal is still in the oscillating state the value shall be set either to the opposite state of the previous stable value or to a defined default value. In this case the validity status 'questionable' is reset and 'invalid' is set as long as the signal is oscillating. If it is configured such that no transient changes should be passed by then the validity status 'invalid' is set immediately in addition to the detail quality identifier 'oscillatory' (used for status information only).")

    # Measurement value is transmitted for test purposes.
    test = Bool(desc="Measurement value is transmitted for test purposes.")

    # Value has been replaced by State Estimator. estimatorReplaced is not an IEC61850 quality bit but has been put in this class for convenience.
    estimatorReplaced = Bool(desc="Value has been replaced by State Estimator. estimatorReplaced is not an IEC61850 quality bit but has been put in this class for convenience.")

    # Source gives information related to the origin of a value. The value may be acquired from the process, defaulted or substituted.
    source = Source(desc="Source gives information related to the origin of a value. The value may be acquired from the process, defaulted or substituted.")

    # This identifier indicates that a supervision function has detected an internal or external failure, e.g. communication failure.
    failure = Bool(desc="This identifier indicates that a supervision function has detected an internal or external failure, e.g. communication failure.")

    # Measurement value is old and possibly invalid, as it has not been successfully updated during a specified time interval.
    oldData = Bool(desc="Measurement value is old and possibly invalid, as it has not been successfully updated during a specified time interval.")

    # Measurement value may be incorrect due to a reference being out of calibration.
    badReference = Bool(desc="Measurement value may be incorrect due to a reference being out of calibration.")

    # Validity of the measurement value.
    validity = Validity(desc="Validity of the measurement value.")

    #--------------------------------------------------------------------------
    #  Begin "Quality61850" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("outOfRange", "overFlow", "operatorBlocked", "suspect", "oscillatory", "test", "estimatorReplaced", "source", "failure", "oldData", "badReference", "validity",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.Quality61850",
        title="Quality61850",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Quality61850" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Limit" class:
#------------------------------------------------------------------------------

class Limit(IdentifiedObject):
    """ Specifies one limit value for a Measurement. A Measurement typically has several limits that are kept together by the LimitSet class. The actual meaning and use of a Limit instance (i.e., if it is an alarm or warning limit or if it is a high or low limit) is not captured in the Limit class. However the name of a Limit instance may indicate both meaning and use.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "Limit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.Limit",
        title="Limit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Limit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MeasurementType" class:
#------------------------------------------------------------------------------

class MeasurementType(IdentifiedObject):
    """ Specifies the type of Measurement, e.g. IndoorTemperature, OutDoorTemperature, BusVoltage, GeneratorVoltage, LineFlow etc. The MeasurementType.name shall be unique among all specified types and describe the type. The MeasurementType.aliasName is meant to be used for localization.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A measurement has a measurement type.
    Measurements = List(Instance("CIM13r19.Meas.Measurement"),
        desc="A measurement has a measurement type.")

    #--------------------------------------------------------------------------
    #  Begin "MeasurementType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.MeasurementType",
        title="MeasurementType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MeasurementType" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ValueToAlias" class:
#------------------------------------------------------------------------------

class ValueToAlias(IdentifiedObject):
    """ Describes the translation of one particular value into a name, e.g. 1->'Open'
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ValueAliasSet = Instance("CIM13r19.Meas.ValueAliasSet",
        transient=True,
        opposite="Values",
        editor=InstanceEditor(name="_valuealiassets"))

    def _get_valuealiassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Meas.ValueAliasSet" ]
        else:
            return []

    _valuealiassets = Property(fget=_get_valuealiassets)

    # The value that is mapped
    value = Int(desc="The value that is mapped")

    #--------------------------------------------------------------------------
    #  Begin "ValueToAlias" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "value",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ValueAliasSet",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.ValueToAlias",
        title="ValueToAlias",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ValueToAlias" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MeasurementValueSource" class:
#------------------------------------------------------------------------------

class MeasurementValueSource(IdentifiedObject):
    """ MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    MeasurementValues = List(Instance("CIM13r19.Meas.MeasurementValue"))

    #--------------------------------------------------------------------------
    #  Begin "MeasurementValueSource" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "MeasurementValues",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.MeasurementValueSource",
        title="MeasurementValueSource",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MeasurementValueSource" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Discrete" class:
#------------------------------------------------------------------------------

class Discrete(Measurement):
    """ Discrete represents a discrete Measurement, i.e. a Measurement reprsenting discrete values, e.g. a Breaker position.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ValueAliasSet = Instance("CIM13r19.Meas.ValueAliasSet",
        transient=True,
        opposite="Measurements",
        editor=InstanceEditor(name="_valuealiassets"))

    def _get_valuealiassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Meas.ValueAliasSet" ]
        else:
            return []

    _valuealiassets = Property(fget=_get_valuealiassets)

    ControlledBy_Control = Instance("CIM13r19.Meas.Command",
        transient=True,
        opposite="MeasuredBy_Measurement",
        editor=InstanceEditor(name="_commands"))

    def _get_commands(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Meas.Command" ]
        else:
            return []

    _commands = Property(fget=_get_commands)

    Contain_MeasurementValues = List(Instance("CIM13r19.Meas.DiscreteValue"))

    # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
    maxValue = Int(desc="Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.")

    # Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values
    minValue = Int(desc="Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values")

    # Normal measurement value, e.g., used for percentage calculations.
    normalValue = Int(desc="Normal measurement value, e.g., used for percentage calculations.")

    #--------------------------------------------------------------------------
    #  Begin "Discrete" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "maxValue", "minValue", "normalValue",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Terminal", "MemberOf_PSR", "Unit", "MeasurementType", "ValueAliasSet", "ControlledBy_Control", "Contain_MeasurementValues",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.Discrete",
        title="Discrete",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Discrete" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SetPoint" class:
#------------------------------------------------------------------------------

class SetPoint(Control):
    """ A SetPoint is an analog control used for supervisory control.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The Control variable associated with the Measurement
    MeasuredBy_Measurement = Instance("CIM13r19.Meas.Analog",
        desc="The Control variable associated with the Measurement",
        transient=True,
        opposite="ControlledBy_Control",
        editor=InstanceEditor(name="_analogs"))

    def _get_analogs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Meas.Analog" ]
        else:
            return []

    _analogs = Property(fget=_get_analogs)

    # Normal value range maximum for any of the Control.value. Used for scaling, e.g. in bar graphs.
    maxValue = Float(desc="Normal value range maximum for any of the Control.value. Used for scaling, e.g. in bar graphs.")

    # Normal value for Control.value e.g. used for percentage scaling
    normalValue = Float(desc="Normal value for Control.value e.g. used for percentage scaling")

    # Normal value range minimum for any of the Control.value. Used for scaling, e.g. in bar graphs.
    minValue = Float(desc="Normal value range minimum for any of the Control.value. Used for scaling, e.g. in bar graphs.")

    # The value representing the actuator output
    value = Float(desc="The value representing the actuator output")

    #--------------------------------------------------------------------------
    #  Begin "SetPoint" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "operationInProgress", "timeStamp", "maxValue", "normalValue", "minValue", "value",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Unit", "ControlType", "RemoteControl", "ControlledBy_RegulatingCondEq", "MeasuredBy_Measurement",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.SetPoint",
        title="SetPoint",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SetPoint" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DiscreteValue" class:
#------------------------------------------------------------------------------

class DiscreteValue(MeasurementValue):
    """ DiscreteValue represents a discrete MeasurementValue.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    MemberOf_Measurement = Instance("CIM13r19.Meas.Discrete",
        transient=True,
        opposite="Contain_MeasurementValues",
        editor=InstanceEditor(name="_discretes"))

    def _get_discretes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Meas.Discrete" ]
        else:
            return []

    _discretes = Property(fget=_get_discretes)

    # The value to supervise.
    value = Int(desc="The value to supervise.")

    #--------------------------------------------------------------------------
    #  Begin "DiscreteValue" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "sensorAccuracy", "timeStamp", "value",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "MeasurementValueQuality", "RemoteSource", "MeasurementValueSource", "MemberOf_Measurement",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.DiscreteValue",
        title="DiscreteValue",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DiscreteValue" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Accumulator" class:
#------------------------------------------------------------------------------

class Accumulator(Measurement):
    """ Accumulator represents a accumulated (counted) Measurement, e.g. an energy value.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Contain_MeasurementValues = List(Instance("CIM13r19.Meas.AccumulatorValue"))

    # A measurement may have zero or more limit ranges defined for it.
    LimitSets = List(Instance("CIM13r19.Meas.AccumulatorLimitSet"),
        desc="A measurement may have zero or more limit ranges defined for it.")

    # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
    maxValue = Int(desc="Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.")

    #--------------------------------------------------------------------------
    #  Begin "Accumulator" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "maxValue",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Terminal", "MemberOf_PSR", "Unit", "MeasurementType", "Contain_MeasurementValues", "LimitSets",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.Accumulator",
        title="Accumulator",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Accumulator" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AnalogLimit" class:
#------------------------------------------------------------------------------

class AnalogLimit(Limit):
    """ Limit values for Analog measurements
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    LimitSet = Instance("CIM13r19.Meas.AnalogLimitSet",
        transient=True,
        opposite="Limits",
        editor=InstanceEditor(name="_analoglimitsets"))

    def _get_analoglimitsets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Meas.AnalogLimitSet" ]
        else:
            return []

    _analoglimitsets = Property(fget=_get_analoglimitsets)

    # The value to supervise against.
    value = Float(desc="The value to supervise against.")

    #--------------------------------------------------------------------------
    #  Begin "AnalogLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "value",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "LimitSet",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.AnalogLimit",
        title="AnalogLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AnalogLimit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StringMeasurementValue" class:
#------------------------------------------------------------------------------

class StringMeasurementValue(MeasurementValue):
    """ StringMeasurementValue represents a measurement value of type string.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    MemberOf_Measurement = Instance("CIM13r19.Meas.StringMeasurement",
        transient=True,
        opposite="Contains_MeasurementValues",
        editor=InstanceEditor(name="_stringmeasurements"))

    def _get_stringmeasurements(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Meas.StringMeasurement" ]
        else:
            return []

    _stringmeasurements = Property(fget=_get_stringmeasurements)

    # The value to supervise.
    value = Str(desc="The value to supervise.")

    #--------------------------------------------------------------------------
    #  Begin "StringMeasurementValue" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "sensorAccuracy", "timeStamp", "value",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "MeasurementValueQuality", "RemoteSource", "MeasurementValueSource", "MemberOf_Measurement",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.StringMeasurementValue",
        title="StringMeasurementValue",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StringMeasurementValue" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AccumulatorLimit" class:
#------------------------------------------------------------------------------

class AccumulatorLimit(Limit):
    """ Limit values for Accumulator measurements
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    LimitSet = Instance("CIM13r19.Meas.AccumulatorLimitSet",
        transient=True,
        opposite="Limits",
        editor=InstanceEditor(name="_accumulatorlimitsets"))

    def _get_accumulatorlimitsets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Meas.AccumulatorLimitSet" ]
        else:
            return []

    _accumulatorlimitsets = Property(fget=_get_accumulatorlimitsets)

    # The value to supervise against. The value is positive.
    value = Int(desc="The value to supervise against. The value is positive.")

    #--------------------------------------------------------------------------
    #  Begin "AccumulatorLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "value",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "LimitSet",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.AccumulatorLimit",
        title="AccumulatorLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AccumulatorLimit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StringMeasurement" class:
#------------------------------------------------------------------------------

class StringMeasurement(Measurement):
    """ StringMeasurement represents a measurement with values of type string.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Contains_MeasurementValues = List(Instance("CIM13r19.Meas.StringMeasurementValue"))

    #--------------------------------------------------------------------------
    #  Begin "StringMeasurement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Terminal", "MemberOf_PSR", "Unit", "MeasurementType", "Contains_MeasurementValues",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.StringMeasurement",
        title="StringMeasurement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StringMeasurement" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AnalogValue" class:
#------------------------------------------------------------------------------

class AnalogValue(MeasurementValue):
    """ AnalogValue represents an analog MeasurementValue.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    MemberOf_Measurement = Instance("CIM13r19.Meas.Analog",
        transient=True,
        opposite="Contain_MeasurementValues",
        editor=InstanceEditor(name="_analogs"))

    def _get_analogs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Meas.Analog" ]
        else:
            return []

    _analogs = Property(fget=_get_analogs)

    AltGeneratingUnit = List(Instance("CIM13r19.ControlArea.AltGeneratingUnitMeas"))

    AltTieMeas = List(Instance("CIM13r19.ControlArea.AltTieMeas"))

    # The value to supervise.
    value = Float(desc="The value to supervise.")

    #--------------------------------------------------------------------------
    #  Begin "AnalogValue" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "sensorAccuracy", "timeStamp", "value",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "MeasurementValueQuality", "RemoteSource", "MeasurementValueSource", "MemberOf_Measurement", "AltGeneratingUnit", "AltTieMeas",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.AnalogValue",
        title="AnalogValue",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AnalogValue" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MeasurementValueQuality" class:
#------------------------------------------------------------------------------

class MeasurementValueQuality(Quality61850):
    """ Measurement quality flags. Bits 0-10 are defined for substation automation in draft IEC 61850 part 7-3. Bits 11-15 are reserved for future expansion by that document. Bits 16-31 are reserved for EMS applications.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A MeasurementValue has a MeasurementValueQuality associated with it.
    MeasurementValue = Instance("CIM13r19.Meas.MeasurementValue",
        desc="A MeasurementValue has a MeasurementValueQuality associated with it.",
        transient=True,
        opposite="MeasurementValueQuality",
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

    #--------------------------------------------------------------------------
    #  Begin "MeasurementValueQuality" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("outOfRange", "overFlow", "operatorBlocked", "suspect", "oscillatory", "test", "estimatorReplaced", "source", "failure", "oldData", "badReference", "validity",
                label="Attributes"),
            VGroup("Parent", "MeasurementValue",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.MeasurementValueQuality",
        title="MeasurementValueQuality",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MeasurementValueQuality" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AccumulatorLimitSet" class:
#------------------------------------------------------------------------------

class AccumulatorLimitSet(LimitSet):
    """ An AccumulatorLimitSet specifies a set of Limits that are associated with an Accumulator measurement.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A measurement may have zero or more limit ranges defined for it.
    Measurements = List(Instance("CIM13r19.Meas.Accumulator"),
        desc="A measurement may have zero or more limit ranges defined for it.")

    Limits = List(Instance("CIM13r19.Meas.AccumulatorLimit"))

    #--------------------------------------------------------------------------
    #  Begin "AccumulatorLimitSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "isPercentageLimits",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Limits",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.AccumulatorLimitSet",
        title="AccumulatorLimitSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AccumulatorLimitSet" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AnalogLimitSet" class:
#------------------------------------------------------------------------------

class AnalogLimitSet(LimitSet):
    """ An AnalogLimitSet specifies a set of Limits that are associated with an Analog measurement.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Limits = List(Instance("CIM13r19.Meas.AnalogLimit"))

    # A measurement may have zero or more limit ranges defined for it.
    Measurements = List(Instance("CIM13r19.Meas.Analog"),
        desc="A measurement may have zero or more limit ranges defined for it.")

    #--------------------------------------------------------------------------
    #  Begin "AnalogLimitSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "isPercentageLimits",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Limits", "Measurements",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.AnalogLimitSet",
        title="AnalogLimitSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AnalogLimitSet" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Command" class:
#------------------------------------------------------------------------------

class Command(Control):
    """ A Command is a discrete control used for supervisory control.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ValueAliasSet = Instance("CIM13r19.Meas.ValueAliasSet",
        transient=True,
        opposite="Commands",
        editor=InstanceEditor(name="_valuealiassets"))

    def _get_valuealiassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Meas.ValueAliasSet" ]
        else:
            return []

    _valuealiassets = Property(fget=_get_valuealiassets)

    MeasuredBy_Measurement = Instance("CIM13r19.Meas.Discrete",
        transient=True,
        opposite="ControlledBy_Control",
        editor=InstanceEditor(name="_discretes"))

    def _get_discretes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Meas.Discrete" ]
        else:
            return []

    _discretes = Property(fget=_get_discretes)

    # The value representing the actuator output
    value = Int(desc="The value representing the actuator output")

    # Normal value for Control.value e.g. used for percentage scaling
    normalValue = Int(desc="Normal value for Control.value e.g. used for percentage scaling")

    #--------------------------------------------------------------------------
    #  Begin "Command" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "operationInProgress", "timeStamp", "value", "normalValue",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Unit", "ControlType", "RemoteControl", "ControlledBy_RegulatingCondEq", "ValueAliasSet", "MeasuredBy_Measurement",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.Command",
        title="Command",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Command" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Analog" class:
#------------------------------------------------------------------------------

class Analog(Measurement):
    """ Analog represents an analog Measurement.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Contain_MeasurementValues = List(Instance("CIM13r19.Meas.AnalogValue"))

    # A measurement may have zero or more limit ranges defined for it.
    LimitSets = List(Instance("CIM13r19.Meas.AnalogLimitSet"),
        desc="A measurement may have zero or more limit ranges defined for it.")

    # The Control variable associated with the Measurement
    ControlledBy_Control = Instance("CIM13r19.Meas.SetPoint",
        desc="The Control variable associated with the Measurement",
        transient=True,
        opposite="MeasuredBy_Measurement",
        editor=InstanceEditor(name="_setpoints"))

    def _get_setpoints(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Meas.SetPoint" ]
        else:
            return []

    _setpoints = Property(fget=_get_setpoints)

    # If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource.
    positiveFlowIn = Bool(desc="If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource.")

    # Normal measurement value, e.g., used for percentage calculations.
    normalValue = Float(desc="Normal measurement value, e.g., used for percentage calculations.")

    # Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values
    minValue = Float(desc="Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values")

    # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
    maxValue = Float(desc="Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.")

    #--------------------------------------------------------------------------
    #  Begin "Analog" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "positiveFlowIn", "normalValue", "minValue", "maxValue",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Terminal", "MemberOf_PSR", "Unit", "MeasurementType", "Contain_MeasurementValues", "LimitSets", "ControlledBy_Control",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.Analog",
        title="Analog",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Analog" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AccumulatorValue" class:
#------------------------------------------------------------------------------

class AccumulatorValue(MeasurementValue):
    """ AccumulatorValue represents a accumulated (counted) MeasurementValue.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    MemberOf_Measurement = Instance("CIM13r19.Meas.Accumulator",
        transient=True,
        opposite="Contain_MeasurementValues",
        editor=InstanceEditor(name="_accumulators"))

    def _get_accumulators(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Meas.Accumulator" ]
        else:
            return []

    _accumulators = Property(fget=_get_accumulators)

    # The value to supervise. The value is positive.
    value = Int(desc="The value to supervise. The value is positive.")

    #--------------------------------------------------------------------------
    #  Begin "AccumulatorValue" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "sensorAccuracy", "timeStamp", "value",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "MeasurementValueQuality", "RemoteSource", "MeasurementValueSource", "MemberOf_Measurement",
                label="References"),
            dock="tab"),
        id="CIM13r19.Meas.AccumulatorValue",
        title="AccumulatorValue",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AccumulatorValue" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
