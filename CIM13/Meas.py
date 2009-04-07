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
from CIM13 import Root
from CIM13.SCADA import Source



from enthought.traits.api import Instance, List, Enum, Int, Float, Bool, Str
# <<< imports

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
    Terminal = Instance("CIM13.Core.Terminal")

    # Measurement-PSR defines the measurements in the naming hierarchy.
    MemberOf_PSR = Instance("CIM13.Core.PowerSystemResource")

    Unit = Instance("CIM13.Core.Unit")

    # A measurement has a measurement type.
    MeasurementType = Instance("CIM13.Meas.MeasurementType")

    #--------------------------------------------------------------------------
    #  Begin measurement user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End measurement user definitions:
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

    Unit = Instance("CIM13.Core.Unit")

    ControlType = Instance("CIM13.Meas.ControlType")

    RemoteControl = Instance("CIM13.SCADA.RemoteControl")

    # The association gives the control output that is used to actually govern a regulating device, e.g. the magnetization of a synchronous machine or capacitor bank breaker actuators.
    ControlledBy_RegulatingCondEq = Instance("CIM13.Wires.RegulatingCondEq")

    # Indicates that a client is currently sending control commands that has not completed
    operationInProgress = EBoolean

    # The last time a control output was sent
    timeStamp = EString

    #--------------------------------------------------------------------------
    #  Begin control user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End control user definitions:
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

    Controls = List(Instance("CIM13.Meas.Control"))

    #--------------------------------------------------------------------------
    #  Begin controlType user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End controlType user definitions:
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
    isPercentageLimits = EBoolean

    #--------------------------------------------------------------------------
    #  Begin limitSet user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End limitSet user definitions:
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
    MeasurementValueQuality = Instance("CIM13.Meas.MeasurementValueQuality")

    # Links to the physical telemetered point associated with this measurement.
    RemoteSource = Instance("CIM13.SCADA.RemoteSource")

    MeasurementValueSource = Instance("CIM13.Meas.MeasurementValueSource")

    # The limit, expressed as a percentage of the sensor maximum, that errors will not exceed when the sensor is used under  reference conditions.
    sensorAccuracy = EFloat

    # The time when the value was last updated
    timeStamp = EString

    #--------------------------------------------------------------------------
    #  Begin measurementValue user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End measurementValue user definitions:
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

    Values = List(Instance("CIM13.Meas.ValueToAlias"))

    Commands = List(Instance("CIM13.Meas.Command"))

    Measurements = List(Instance("CIM13.Meas.Discrete"))

    #--------------------------------------------------------------------------
    #  Begin valueAliasSet user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End valueAliasSet user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Quality61850" class:
#------------------------------------------------------------------------------

class Quality61850(Root):
    """ Quality flags in this class are as defined in IEC 61850, except for estimatorReplaced, which has been included in this class for convenience.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Measurement value is beyond a predefined range of value.
    outOfRange = EBoolean

    # Measurement value is beyond the capability of being  represented properly. For example, a counter value overflows from maximum count back to a value of zero.
    overFlow = EBoolean

    # Measurement value is blocked and hence unavailable for transmission.
    operatorBlocked = EBoolean

    # A correlation function has detected that the value is not consitent with other values. Typically set by a network State Estimator.
    suspect = EBoolean

    # To prevent some overload of the communication it is sensible to detect and suppress oscillating (fast changing) binary inputs. If a signal changes in a defined time (tosc) twice in the same direction (from 0 to 1 or from 1 to 0) then oscillation is detected and the detail quality identifier 'oscillatory' is set. If it is detected a configured numbers of transient changes could be passed by. In this time the validity status 'questionable' is set. If after this defined numbers of changes the signal is still in the oscillating state the value shall be set either to the opposite state of the previous stable value or to a defined default value. In this case the validity status 'questionable' is reset and 'invalid' is set as long as the signal is oscillating. If it is configured such that no transient changes should be passed by then the validity status 'invalid' is set immediately in addition to the detail quality identifier 'oscillatory' (used for status information only).
    oscillatory = EBoolean

    # Measurement value is transmitted for test purposes.
    test = EBoolean

    # Value has been replaced by State Estimator. estimatorReplaced is not an IEC61850 quality bit but has been put in this class for convenience.
    estimatorReplaced = EBoolean

    # Source gives information related to the origin of a value. The value may be acquired from the process, defaulted or substituted.
    source = Source

    # This identifier indicates that a supervision function has detected an internal or external failure, e.g. communication failure.
    failure = EBoolean

    # Measurement value is old and possibly invalid, as it has not been successfully updated during a specified time interval.
    oldData = EBoolean

    # Measurement value may be incorrect due to a reference being out of calibration.
    badReference = EBoolean

    # Validity of the measurement value.
    validity = Validity

    #--------------------------------------------------------------------------
    #  Begin quality61850 user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End quality61850 user definitions:
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
    #  Begin limit user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End limit user definitions:
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
    Measurements = List(Instance("CIM13.Meas.Measurement"))

    #--------------------------------------------------------------------------
    #  Begin measurementType user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End measurementType user definitions:
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

    ValueAliasSet = Instance("CIM13.Meas.ValueAliasSet")

    # The value that is mapped
    value = EInt

    #--------------------------------------------------------------------------
    #  Begin valueToAlias user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End valueToAlias user definitions:
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

    MeasurementValues = List(Instance("CIM13.Meas.MeasurementValue"))

    #--------------------------------------------------------------------------
    #  Begin measurementValueSource user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End measurementValueSource user definitions:
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

    ValueAliasSet = Instance("CIM13.Meas.ValueAliasSet")

    ControlledBy_Control = Instance("CIM13.Meas.Command")

    Contain_MeasurementValues = List(Instance("CIM13.Meas.DiscreteValue"))

    # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
    maxValue = EInt

    # Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values
    minValue = EInt

    # Normal measurement value, e.g., used for percentage calculations.
    normalValue = EInt

    #--------------------------------------------------------------------------
    #  Begin discrete user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End discrete user definitions:
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
    MeasuredBy_Measurement = Instance("CIM13.Meas.Analog")

    # Normal value range maximum for any of the Control.value. Used for scaling, e.g. in bar graphs.
    maxValue = EFloat

    # Normal value for Control.value e.g. used for percentage scaling
    normalValue = EFloat

    # Normal value range minimum for any of the Control.value. Used for scaling, e.g. in bar graphs.
    minValue = EFloat

    # The value representing the actuator output
    value = EFloat

    #--------------------------------------------------------------------------
    #  Begin setPoint user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End setPoint user definitions:
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

    MemberOf_Measurement = Instance("CIM13.Meas.Discrete")

    # The value to supervise.
    value = EInt

    #--------------------------------------------------------------------------
    #  Begin discreteValue user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End discreteValue user definitions:
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

    Contain_MeasurementValues = List(Instance("CIM13.Meas.AccumulatorValue"))

    # A measurement may have zero or more limit ranges defined for it.
    LimitSets = List(Instance("CIM13.Meas.AccumulatorLimitSet"))

    # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
    maxValue = EInt

    #--------------------------------------------------------------------------
    #  Begin accumulator user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End accumulator user definitions:
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

    LimitSet = Instance("CIM13.Meas.AnalogLimitSet")

    # The value to supervise against.
    value = EFloat

    #--------------------------------------------------------------------------
    #  Begin analogLimit user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End analogLimit user definitions:
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

    MemberOf_Measurement = Instance("CIM13.Meas.StringMeasurement")

    # The value to supervise.
    value = EString

    #--------------------------------------------------------------------------
    #  Begin stringMeasurementValue user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End stringMeasurementValue user definitions:
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

    LimitSet = Instance("CIM13.Meas.AccumulatorLimitSet")

    # The value to supervise against. The value is positive.
    value = EInt

    #--------------------------------------------------------------------------
    #  Begin accumulatorLimit user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End accumulatorLimit user definitions:
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

    Contains_MeasurementValues = List(Instance("CIM13.Meas.StringMeasurementValue"))

    #--------------------------------------------------------------------------
    #  Begin stringMeasurement user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End stringMeasurement user definitions:
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

    MemberOf_Measurement = Instance("CIM13.Meas.Analog")

    AltGeneratingUnit = List(Instance("CIM13.ControlArea.AltGeneratingUnitMeas"))

    AltTieMeas = List(Instance("CIM13.ControlArea.AltTieMeas"))

    # The value to supervise.
    value = EFloat

    #--------------------------------------------------------------------------
    #  Begin analogValue user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End analogValue user definitions:
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
    MeasurementValue = Instance("CIM13.Meas.MeasurementValue")

    #--------------------------------------------------------------------------
    #  Begin measurementValueQuality user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End measurementValueQuality user definitions:
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
    Measurements = List(Instance("CIM13.Meas.Accumulator"))

    Limits = List(Instance("CIM13.Meas.AccumulatorLimit"))

    #--------------------------------------------------------------------------
    #  Begin accumulatorLimitSet user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End accumulatorLimitSet user definitions:
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

    Limits = List(Instance("CIM13.Meas.AnalogLimit"))

    # A measurement may have zero or more limit ranges defined for it.
    Measurements = List(Instance("CIM13.Meas.Analog"))

    #--------------------------------------------------------------------------
    #  Begin analogLimitSet user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End analogLimitSet user definitions:
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

    ValueAliasSet = Instance("CIM13.Meas.ValueAliasSet")

    MeasuredBy_Measurement = Instance("CIM13.Meas.Discrete")

    # The value representing the actuator output
    value = EInt

    # Normal value for Control.value e.g. used for percentage scaling
    normalValue = EInt

    #--------------------------------------------------------------------------
    #  Begin command user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End command user definitions:
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

    Contain_MeasurementValues = List(Instance("CIM13.Meas.AnalogValue"))

    # A measurement may have zero or more limit ranges defined for it.
    LimitSets = List(Instance("CIM13.Meas.AnalogLimitSet"))

    # The Control variable associated with the Measurement
    ControlledBy_Control = Instance("CIM13.Meas.SetPoint")

    # If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource.
    positiveFlowIn = EBoolean

    # Normal measurement value, e.g., used for percentage calculations.
    normalValue = EFloat

    # Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values
    minValue = EFloat

    # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
    maxValue = EFloat

    #--------------------------------------------------------------------------
    #  Begin analog user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End analog user definitions:
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

    MemberOf_Measurement = Instance("CIM13.Meas.Accumulator")

    # The value to supervise. The value is positive.
    value = EInt

    #--------------------------------------------------------------------------
    #  Begin accumulatorValue user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End accumulatorValue user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
