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

""" Contains entities that describe dynamic measurement data exchanged between applications.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.Core import IdentifiedObject
from CIM import Element
from CIM.Domain import PerCent
from CIM.SCADA import Source



from enthought.traits.api import Instance, List, Property, Enum, Bool, Date, Int, Float, Str
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Validity for MeasurementValue.
Validity = Enum("GOOD", "INVALID", "QUESTIONABLE", desc="Validity for MeasurementValue.")

#------------------------------------------------------------------------------
#  "Control" class:
#------------------------------------------------------------------------------

class Control(IdentifiedObject):
    """ Control is used for supervisory/device control. It represents control outputs that are used to change the state in a process, e.g. close or open breaker, a set point value or a raise lower command.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The Unit for the Control.
    Unit = Instance("CIM.Core.Unit",
        desc="The Unit for the Control.",
        transient=True,
        opposite="Controls",
        editor=InstanceEditor(name="_units"))

    def _get_units(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Core.Unit" ]
        else:
            return []

    _units = Property(fget=_get_units)

    # The type of Control
    ControlType = Instance("CIM.Meas.ControlType",
        desc="The type of Control",
        transient=True,
        opposite="Controls",
        editor=InstanceEditor(name="_controltypes"))

    def _get_controltypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Meas.ControlType" ]
        else:
            return []

    _controltypes = Property(fget=_get_controltypes)

    # The remote point controlling the physical actuator.
    RemoteControl = Instance("CIM.SCADA.RemoteControl",
        desc="The remote point controlling the physical actuator.",
        transient=True,
        opposite="Control",
        editor=InstanceEditor(name="_remotecontrols"))

    def _get_remotecontrols(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.SCADA.RemoteControl" ]
        else:
            return []

    _remotecontrols = Property(fget=_get_remotecontrols)

    # Regulating device governed by this control output.
    ControlledBy_RegulatingCondEq = Instance("CIM.Wires.RegulatingCondEq",
        desc="Regulating device governed by this control output.",
        transient=True,
        opposite="Controls",
        editor=InstanceEditor(name="_regulatingcondeqs"))

    def _get_regulatingcondeqs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Wires.RegulatingCondEq" ]
        else:
            return []

    _regulatingcondeqs = Property(fget=_get_regulatingcondeqs)

    # Indicates that a client is currently sending control commands that has not completed
    operationInProgress = Bool(desc="Indicates that a client is currently sending control commands that has not completed")

    # The last time a control output was sent
    timeStamp = Date(desc="The last time a control output was sent")

    #--------------------------------------------------------------------------
    #  Begin "Control" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "operationInProgress", "timeStamp",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "Unit", "ControlType", "RemoteControl", "ControlledBy_RegulatingCondEq",
                label="References"),
            dock="tab"),
        id="CIM.Meas.Control",
        title="Control",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Control" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Measurement" class:
#------------------------------------------------------------------------------

class Measurement(IdentifiedObject):
    """ A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  Two possible paths exist: 1) Measurement-Terminal- ConnectivityNode-Terminal-ConductingEquipment 2) Measurement-Terminal-ConductingEquipment Alternative 2 is the only allowed use.  When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The Unit for the Measurement
    Unit = Instance("CIM.Core.Unit",
        desc="The Unit for the Measurement",
        transient=True,
        opposite="Measurements",
        editor=InstanceEditor(name="_units"))

    def _get_units(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Core.Unit" ]
        else:
            return []

    _units = Property(fget=_get_units)

    # The PowerSystemResource that contains the Measurement in the naming hierarchy
    MemberOf_PSR = Instance("CIM.Core.PowerSystemResource",
        desc="The PowerSystemResource that contains the Measurement in the naming hierarchy",
        transient=True,
        opposite="Contains_Measurements",
        editor=InstanceEditor(name="_powersystemresources"))

    def _get_powersystemresources(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Core.PowerSystemResource" ]
        else:
            return []

    _powersystemresources = Property(fget=_get_powersystemresources)

    # The type for the Measurement
    MeasurementType = Instance("CIM.Meas.MeasurementType",
        desc="The type for the Measurement",
        transient=True,
        opposite="Measurements",
        editor=InstanceEditor(name="_measurementtypes"))

    def _get_measurementtypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Meas.MeasurementType" ]
        else:
            return []

    _measurementtypes = Property(fget=_get_measurementtypes)

    # One or more measurements may be associated with a terminal in the network
    Terminal = Instance("CIM.Core.Terminal",
        desc="One or more measurements may be associated with a terminal in the network",
        transient=True,
        opposite="Measurements",
        editor=InstanceEditor(name="_terminals"))

    def _get_terminals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Core.Terminal" ]
        else:
            return []

    _terminals = Property(fget=_get_terminals)

    #--------------------------------------------------------------------------
    #  Begin "Measurement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "Unit", "MemberOf_PSR", "MeasurementType", "Terminal",
                label="References"),
            dock="tab"),
        id="CIM.Meas.Measurement",
        title="Measurement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Measurement" user definitions:
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

    # The Measurements using the set for translation
    Measurements = List(Instance("CIM.Meas.Discrete"),
        desc="The Measurements using the set for translation")

    # The ValueAliasSet used for translation of a Control value to a name.
    Commands = List(Instance("CIM.Meas.Command"),
        desc="The ValueAliasSet used for translation of a Control value to a name.")

    # The ValueToAlias mappings included in the set
    Values = List(Instance("CIM.Meas.ValueToAlias"),
        desc="The ValueToAlias mappings included in the set")

    #--------------------------------------------------------------------------
    #  Begin "ValueAliasSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "Measurements", "Commands", "Values",
                label="References"),
            dock="tab"),
        id="CIM.Meas.ValueAliasSet",
        title="ValueAliasSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ValueAliasSet" user definitions:
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
    MeasurementValueQuality = Instance("CIM.Meas.MeasurementValueQuality",
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
                    "CIM.Meas.MeasurementValueQuality" ]
        else:
            return []

    _measurementvaluequalitys = Property(fget=_get_measurementvaluequalitys)

    # A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink, manual, etc. User conventions for the names of sources are contained in the introduction to IEC 61970-301.
    MeasurementValueSource = Instance("CIM.Meas.MeasurementValueSource",
        desc="A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink, manual, etc. User conventions for the names of sources are contained in the introduction to IEC 61970-301.",
        transient=True,
        opposite="MeasurementValues",
        editor=InstanceEditor(name="_measurementvaluesources"))

    def _get_measurementvaluesources(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Meas.MeasurementValueSource" ]
        else:
            return []

    _measurementvaluesources = Property(fget=_get_measurementvaluesources)

    # Link to the physical telemetered point associated with this measurement.
    RemoteSource = Instance("CIM.SCADA.RemoteSource",
        desc="Link to the physical telemetered point associated with this measurement.",
        transient=True,
        opposite="MeasurementValue",
        editor=InstanceEditor(name="_remotesources"))

    def _get_remotesources(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.SCADA.RemoteSource" ]
        else:
            return []

    _remotesources = Property(fget=_get_remotesources)

    # The time when the value was last updated
    timeStamp = Date(desc="The time when the value was last updated")

    # The limit, expressed as a percentage of the sensor maximum, that errors will not exceed when the sensor is used under  reference conditions.
    sensorAccuracy = PerCent(desc="The limit, expressed as a percentage of the sensor maximum, that errors will not exceed when the sensor is used under  reference conditions.")

    #--------------------------------------------------------------------------
    #  Begin "MeasurementValue" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "timeStamp", "sensorAccuracy",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "MeasurementValueQuality", "MeasurementValueSource", "RemoteSource",
                label="References"),
            dock="tab"),
        id="CIM.Meas.MeasurementValue",
        title="MeasurementValue",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MeasurementValue" user definitions:
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
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet",
                label="References"),
            dock="tab"),
        id="CIM.Meas.Limit",
        title="Limit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Limit" user definitions:
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
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "isPercentageLimits",
                label="Attributes"),
            VGroup("ModelingAuthoritySet",
                label="References"),
            dock="tab"),
        id="CIM.Meas.LimitSet",
        title="LimitSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LimitSet" user definitions:
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

    # The ValueAliasSet having the ValueToAlias mappings
    ValueAliasSet = Instance("CIM.Meas.ValueAliasSet",
        desc="The ValueAliasSet having the ValueToAlias mappings",
        transient=True,
        opposite="Values",
        editor=InstanceEditor(name="_valuealiassets"))

    def _get_valuealiassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Meas.ValueAliasSet" ]
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
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "value",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "ValueAliasSet",
                label="References"),
            dock="tab"),
        id="CIM.Meas.ValueToAlias",
        title="ValueToAlias",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ValueToAlias" user definitions:
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

    # The Controls having the ControlType
    Controls = List(Instance("CIM.Meas.Control"),
        desc="The Controls having the ControlType")

    #--------------------------------------------------------------------------
    #  Begin "ControlType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "Controls",
                label="References"),
            dock="tab"),
        id="CIM.Meas.ControlType",
        title="ControlType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ControlType" user definitions:
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

    # The MeasurementValues updated by the source
    MeasurementValues = List(Instance("CIM.Meas.MeasurementValue"),
        desc="The MeasurementValues updated by the source")

    #--------------------------------------------------------------------------
    #  Begin "MeasurementValueSource" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "MeasurementValues",
                label="References"),
            dock="tab"),
        id="CIM.Meas.MeasurementValueSource",
        title="MeasurementValueSource",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MeasurementValueSource" user definitions:
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

    # The measurements associated with the Type
    Measurements = List(Instance("CIM.Meas.Measurement"),
        desc="The measurements associated with the Type")

    #--------------------------------------------------------------------------
    #  Begin "MeasurementType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "Measurements",
                label="References"),
            dock="tab"),
        id="CIM.Meas.MeasurementType",
        title="MeasurementType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MeasurementType" user definitions:
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

    # Validity of the measurement value.
    validity = Validity(desc="Validity of the measurement value.")

    # Source gives information related to the origin of a value. The value may be acquired from the process, defaulted or substituted.
    source = Source(desc="Source gives information related to the origin of a value. The value may be acquired from the process, defaulted or substituted.")

    # Measurement value is blocked and hence unavailable for transmission.
    operatorBlocked = Bool(desc="Measurement value is blocked and hence unavailable for transmission.")

    # To prevent some overload of the communication it is sensible to detect and suppress oscillating (fast changing) binary inputs. If a signal changes in a defined time (tosc) twice in the same direction (from 0 to 1 or from 1 to 0) then oscillation is detected and the detail quality identifier 'oscillatory' is set. If it is detected a configured numbers of transient changes could be passed by. In this time the validity status 'questionable' is set. If after this defined numbers of changes the signal is still in the oscillating state the value shall be set either to the opposite state of the previous stable value or to a defined default value. In this case the validity status 'questionable' is reset and 'invalid' is set as long as the signal is oscillating. If it is configured such that no transient changes should be passed by then the validity status 'invalid' is set immediately in addition to the detail quality identifier 'oscillatory' (used for status information only).
    oscillatory = Bool(desc="To prevent some overload of the communication it is sensible to detect and suppress oscillating (fast changing) binary inputs. If a signal changes in a defined time (tosc) twice in the same direction (from 0 to 1 or from 1 to 0) then oscillation is detected and the detail quality identifier 'oscillatory' is set. If it is detected a configured numbers of transient changes could be passed by. In this time the validity status 'questionable' is set. If after this defined numbers of changes the signal is still in the oscillating state the value shall be set either to the opposite state of the previous stable value or to a defined default value. In this case the validity status 'questionable' is reset and 'invalid' is set as long as the signal is oscillating. If it is configured such that no transient changes should be passed by then the validity status 'invalid' is set immediately in addition to the detail quality identifier 'oscillatory' (used for status information only).")

    # A correlation function has detected that the value is not consitent with other values. Typically set by a network State Estimator.
    suspect = Bool(desc="A correlation function has detected that the value is not consitent with other values. Typically set by a network State Estimator.")

    # Measurement value is beyond a predefined range of value.
    outOfRange = Bool(desc="Measurement value is beyond a predefined range of value.")

    # Measurement value is old and possibly invalid, as it has not been successfully updated during a specified time interval.
    oldData = Bool(desc="Measurement value is old and possibly invalid, as it has not been successfully updated during a specified time interval.")

    # This identifier indicates that a supervision function has detected an internal or external failure, e.g. communication failure.
    failure = Bool(desc="This identifier indicates that a supervision function has detected an internal or external failure, e.g. communication failure.")

    # Measurement value may be incorrect due to a reference being out of calibration.
    badReference = Bool(desc="Measurement value may be incorrect due to a reference being out of calibration.")

    # Measurement value is beyond the capability of being  represented properly. For example, a counter value overflows from maximum count back to a value of zero.
    overFlow = Bool(desc="Measurement value is beyond the capability of being  represented properly. For example, a counter value overflows from maximum count back to a value of zero.")

    # Measurement value is transmitted for test purposes.
    test = Bool(desc="Measurement value is transmitted for test purposes.")

    # Value has been replaced by State Estimator. estimatorReplaced is not an IEC61850 quality bit but has been put in this class for convenience.
    estimatorReplaced = Bool(desc="Value has been replaced by State Estimator. estimatorReplaced is not an IEC61850 quality bit but has been put in this class for convenience.")

    #--------------------------------------------------------------------------
    #  Begin "Quality61850" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "validity", "source", "operatorBlocked", "oscillatory", "suspect", "outOfRange", "oldData", "failure", "badReference", "overFlow", "test", "estimatorReplaced",
                label="Attributes", columns=1),
            
            dock="tab"),
        id="CIM.Meas.Quality61850",
        title="Quality61850",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Quality61850" user definitions:
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

    # The values connected to this measurement.
    Contains_MeasurementValues = List(Instance("CIM.Meas.StringMeasurementValue"),
        desc="The values connected to this measurement.")

    #--------------------------------------------------------------------------
    #  Begin "StringMeasurement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "Unit", "MemberOf_PSR", "MeasurementType", "Terminal", "Contains_MeasurementValues",
                label="References"),
            dock="tab"),
        id="CIM.Meas.StringMeasurement",
        title="StringMeasurement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StringMeasurement" user definitions:
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

    # The Control variable associated with the Measurement.
    ControlledBy_Control = Instance("CIM.Meas.Command",
        desc="The Control variable associated with the Measurement.",
        transient=True,
        opposite="MeasuredBy_Measurement",
        editor=InstanceEditor(name="_commands"))

    def _get_commands(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Meas.Command" ]
        else:
            return []

    _commands = Property(fget=_get_commands)

    # The ValueAliasSet used for translation of a MeasurementValue.value to a name
    ValueAliasSet = Instance("CIM.Meas.ValueAliasSet",
        desc="The ValueAliasSet used for translation of a MeasurementValue.value to a name",
        transient=True,
        opposite="Measurements",
        editor=InstanceEditor(name="_valuealiassets"))

    def _get_valuealiassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Meas.ValueAliasSet" ]
        else:
            return []

    _valuealiassets = Property(fget=_get_valuealiassets)

    # The values connected to this measurement.
    Contain_MeasurementValues = List(Instance("CIM.Meas.DiscreteValue"),
        desc="The values connected to this measurement.")

    # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
    maxValue = Int(desc="Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.")

    # Normal measurement value, e.g., used for percentage calculations.
    normalValue = Int(desc="Normal measurement value, e.g., used for percentage calculations.")

    # Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values
    minValue = Int(desc="Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values")

    #--------------------------------------------------------------------------
    #  Begin "Discrete" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "maxValue", "normalValue", "minValue",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "Unit", "MemberOf_PSR", "MeasurementType", "Terminal", "ControlledBy_Control", "ValueAliasSet", "Contain_MeasurementValues",
                label="References"),
            dock="tab"),
        id="CIM.Meas.Discrete",
        title="Discrete",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Discrete" user definitions:
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

    # Measurement to which this value is connected.
    MemberOf_Measurement = Instance("CIM.Meas.Discrete",
        desc="Measurement to which this value is connected.",
        transient=True,
        opposite="Contain_MeasurementValues",
        editor=InstanceEditor(name="_discretes"))

    def _get_discretes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Meas.Discrete" ]
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
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "timeStamp", "sensorAccuracy", "value",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "MeasurementValueQuality", "MeasurementValueSource", "RemoteSource", "MemberOf_Measurement",
                label="References"),
            dock="tab"),
        id="CIM.Meas.DiscreteValue",
        title="DiscreteValue",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DiscreteValue" user definitions:
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

    # The set of limits.
    LimitSet = Instance("CIM.Meas.AnalogLimitSet",
        desc="The set of limits.",
        transient=True,
        opposite="Limits",
        editor=InstanceEditor(name="_analoglimitsets"))

    def _get_analoglimitsets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Meas.AnalogLimitSet" ]
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
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "value",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "LimitSet",
                label="References"),
            dock="tab"),
        id="CIM.Meas.AnalogLimit",
        title="AnalogLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AnalogLimit" user definitions:
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

    # The limit values used for supervision of Measurements.
    Limits = List(Instance("CIM.Meas.AccumulatorLimit"),
        desc="The limit values used for supervision of Measurements.")

    # The Measurements using the LimitSet.
    Measurements = List(Instance("CIM.Meas.Accumulator"),
        desc="The Measurements using the LimitSet.")

    #--------------------------------------------------------------------------
    #  Begin "AccumulatorLimitSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "isPercentageLimits",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "Limits", "Measurements",
                label="References"),
            dock="tab"),
        id="CIM.Meas.AccumulatorLimitSet",
        title="AccumulatorLimitSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AccumulatorLimitSet" user definitions:
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

    # The Measurement variable used for control
    MeasuredBy_Measurement = Instance("CIM.Meas.Analog",
        desc="The Measurement variable used for control",
        transient=True,
        opposite="ControlledBy_Control",
        editor=InstanceEditor(name="_analogs"))

    def _get_analogs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Meas.Analog" ]
        else:
            return []

    _analogs = Property(fget=_get_analogs)

    # Normal value for Control.value e.g. used for percentage scaling
    normalValue = Float(desc="Normal value for Control.value e.g. used for percentage scaling")

    # Normal value range minimum for any of the Control.value. Used for scaling, e.g. in bar graphs.
    minValue = Float(desc="Normal value range minimum for any of the Control.value. Used for scaling, e.g. in bar graphs.")

    # The value representing the actuator output
    value = Float(desc="The value representing the actuator output")

    # Normal value range maximum for any of the Control.value. Used for scaling, e.g. in bar graphs.
    maxValue = Float(desc="Normal value range maximum for any of the Control.value. Used for scaling, e.g. in bar graphs.")

    #--------------------------------------------------------------------------
    #  Begin "SetPoint" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "operationInProgress", "timeStamp", "normalValue", "minValue", "value", "maxValue",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "Unit", "ControlType", "RemoteControl", "ControlledBy_RegulatingCondEq", "MeasuredBy_Measurement",
                label="References"),
            dock="tab"),
        id="CIM.Meas.SetPoint",
        title="SetPoint",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SetPoint" user definitions:
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

    # The Measurement variable used for control.
    MeasuredBy_Measurement = Instance("CIM.Meas.Discrete",
        desc="The Measurement variable used for control.",
        transient=True,
        opposite="ControlledBy_Control",
        editor=InstanceEditor(name="_discretes"))

    def _get_discretes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Meas.Discrete" ]
        else:
            return []

    _discretes = Property(fget=_get_discretes)

    # The Commands using the set for translation.
    ValueAliasSet = Instance("CIM.Meas.ValueAliasSet",
        desc="The Commands using the set for translation.",
        transient=True,
        opposite="Commands",
        editor=InstanceEditor(name="_valuealiassets"))

    def _get_valuealiassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Meas.ValueAliasSet" ]
        else:
            return []

    _valuealiassets = Property(fget=_get_valuealiassets)

    # Normal value for Control.value e.g. used for percentage scaling
    normalValue = Int(desc="Normal value for Control.value e.g. used for percentage scaling")

    # The value representing the actuator output
    value = Int(desc="The value representing the actuator output")

    #--------------------------------------------------------------------------
    #  Begin "Command" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "operationInProgress", "timeStamp", "normalValue", "value",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "Unit", "ControlType", "RemoteControl", "ControlledBy_RegulatingCondEq", "MeasuredBy_Measurement", "ValueAliasSet",
                label="References"),
            dock="tab"),
        id="CIM.Meas.Command",
        title="Command",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Command" user definitions:
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

    # Measurement to which this value is connected.
    MemberOf_Measurement = Instance("CIM.Meas.StringMeasurement",
        desc="Measurement to which this value is connected.",
        transient=True,
        opposite="Contains_MeasurementValues",
        editor=InstanceEditor(name="_stringmeasurements"))

    def _get_stringmeasurements(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Meas.StringMeasurement" ]
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
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "timeStamp", "sensorAccuracy", "value",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "MeasurementValueQuality", "MeasurementValueSource", "RemoteSource", "MemberOf_Measurement",
                label="References"),
            dock="tab"),
        id="CIM.Meas.StringMeasurementValue",
        title="StringMeasurementValue",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StringMeasurementValue" user definitions:
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

    # The limit values used for supervision of Measurements.
    Limits = List(Instance("CIM.Meas.AnalogLimit"),
        desc="The limit values used for supervision of Measurements.")

    # The Measurements using the LimitSet.
    Measurements = List(Instance("CIM.Meas.Analog"),
        desc="The Measurements using the LimitSet.")

    #--------------------------------------------------------------------------
    #  Begin "AnalogLimitSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "isPercentageLimits",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "Limits", "Measurements",
                label="References"),
            dock="tab"),
        id="CIM.Meas.AnalogLimitSet",
        title="AnalogLimitSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AnalogLimitSet" user definitions:
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

    # A measurement may have zero or more limit ranges defined for it.
    LimitSets = List(Instance("CIM.Meas.AccumulatorLimitSet"),
        desc="A measurement may have zero or more limit ranges defined for it.")

    # The values connected to this measurement.
    Contain_MeasurementValues = List(Instance("CIM.Meas.AccumulatorValue"),
        desc="The values connected to this measurement.")

    # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
    maxValue = Int(desc="Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.")

    #--------------------------------------------------------------------------
    #  Begin "Accumulator" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "maxValue",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "Unit", "MemberOf_PSR", "MeasurementType", "Terminal", "LimitSets", "Contain_MeasurementValues",
                label="References"),
            dock="tab"),
        id="CIM.Meas.Accumulator",
        title="Accumulator",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Accumulator" user definitions:
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

    # The set of limits.
    LimitSet = Instance("CIM.Meas.AccumulatorLimitSet",
        desc="The set of limits.",
        transient=True,
        opposite="Limits",
        editor=InstanceEditor(name="_accumulatorlimitsets"))

    def _get_accumulatorlimitsets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Meas.AccumulatorLimitSet" ]
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
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "value",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "LimitSet",
                label="References"),
            dock="tab"),
        id="CIM.Meas.AccumulatorLimit",
        title="AccumulatorLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AccumulatorLimit" user definitions:
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

    # Measurement to which this value is connected.
    MemberOf_Measurement = Instance("CIM.Meas.Analog",
        desc="Measurement to which this value is connected.",
        transient=True,
        opposite="Contain_MeasurementValues",
        editor=InstanceEditor(name="_analogs"))

    def _get_analogs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Meas.Analog" ]
        else:
            return []

    _analogs = Property(fget=_get_analogs)

    # The alternate generating unit for which this measurement value applies.
    AltGeneratingUnit = List(Instance("CIM.ControlArea.AltGeneratingUnitMeas"),
        desc="The alternate generating unit for which this measurement value applies.")

    # The usage of the measurement within the control area specification.
    AltTieMeas = List(Instance("CIM.ControlArea.AltTieMeas"),
        desc="The usage of the measurement within the control area specification.")

    # The value to supervise.
    value = Float(desc="The value to supervise.")

    #--------------------------------------------------------------------------
    #  Begin "AnalogValue" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "timeStamp", "sensorAccuracy", "value",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "MeasurementValueQuality", "MeasurementValueSource", "RemoteSource", "MemberOf_Measurement", "AltGeneratingUnit", "AltTieMeas",
                label="References"),
            dock="tab"),
        id="CIM.Meas.AnalogValue",
        title="AnalogValue",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AnalogValue" user definitions:
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

    # The values connected to this measurement.
    Contain_MeasurementValues = List(Instance("CIM.Meas.AnalogValue"),
        desc="The values connected to this measurement.")

    # A measurement may have zero or more limit ranges defined for it.
    LimitSets = List(Instance("CIM.Meas.AnalogLimitSet"),
        desc="A measurement may have zero or more limit ranges defined for it.")

    # The Control variable associated with the Measurement
    ControlledBy_Control = Instance("CIM.Meas.SetPoint",
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
                    "CIM.Meas.SetPoint" ]
        else:
            return []

    _setpoints = Property(fget=_get_setpoints)

    # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
    maxValue = Float(desc="Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.")

    # If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource.
    positiveFlowIn = Bool(desc="If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource.")

    # Normal measurement value, e.g., used for percentage calculations.
    normalValue = Float(desc="Normal measurement value, e.g., used for percentage calculations.")

    # Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values
    minValue = Float(desc="Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values")

    #--------------------------------------------------------------------------
    #  Begin "Analog" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "maxValue", "positiveFlowIn", "normalValue", "minValue",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "Unit", "MemberOf_PSR", "MeasurementType", "Terminal", "Contain_MeasurementValues", "LimitSets", "ControlledBy_Control",
                label="References"),
            dock="tab"),
        id="CIM.Meas.Analog",
        title="Analog",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Analog" user definitions:
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
    MeasurementValue = Instance("CIM.Meas.MeasurementValue",
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
                    "CIM.Meas.MeasurementValue" ]
        else:
            return []

    _measurementvalues = Property(fget=_get_measurementvalues)

    #--------------------------------------------------------------------------
    #  Begin "MeasurementValueQuality" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "validity", "source", "operatorBlocked", "oscillatory", "suspect", "outOfRange", "oldData", "failure", "badReference", "overFlow", "test", "estimatorReplaced",
                label="Attributes", columns=1),
            VGroup("MeasurementValue",
                label="References"),
            dock="tab"),
        id="CIM.Meas.MeasurementValueQuality",
        title="MeasurementValueQuality",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MeasurementValueQuality" user definitions:
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

    # Measurement to which this value is connected.
    MemberOf_Measurement = Instance("CIM.Meas.Accumulator",
        desc="Measurement to which this value is connected.",
        transient=True,
        opposite="Contain_MeasurementValues",
        editor=InstanceEditor(name="_accumulators"))

    def _get_accumulators(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Meas.Accumulator" ]
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
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "timeStamp", "sensorAccuracy", "value",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "MeasurementValueQuality", "MeasurementValueSource", "RemoteSource", "MemberOf_Measurement",
                label="References"),
            dock="tab"),
        id="CIM.Meas.AccumulatorValue",
        title="AccumulatorValue",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AccumulatorValue" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
