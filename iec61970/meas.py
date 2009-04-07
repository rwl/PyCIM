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

""" Contains entities that describe dynamic measurement data exchanged between applications.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from iec61970.core import IdentifiedObject
from iec61970.domain import AbsoluteDateTime
from iec61970.domain import PerCent
from iec61970.domain import Integer
from iec61970.domain import Boolean
from iec61970.scada import Source
from iec61970.domain import String
from iec61970.domain import Float



from enthought.traits.api import HasTraits, Instance, List, Enum, Int, Bool, Float
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
    """ A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of  power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  Two possible paths exist: 1) Measurement-Terminal- ConnectivityNode-Terminal-ConductingEquipment 2) Measurement-Terminal-ConductingEquipment Alternative 2 is the only allowed use.  When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The type for the Measurement
    MeasurementType = Instance("iec61970.meas.MeasurementType", allow_none=False)

    # One or more measurements may be associated with a terminal in the network
    Terminal = Instance("iec61970.core.Terminal")

    # The PowerSystemResource that contains the Measurement in the naming hierarchy
    MemberOf_PSR = Instance("iec61970.core.PowerSystemResource", allow_none=False)

    # The Unit for the Measurement
    Unit = Instance("iec61970.core.Unit", allow_none=False)

    #--------------------------------------------------------------------------
    #  Begin measurement user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End measurement user definitions:
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
    MeasurementValueQuality = Instance("iec61970.meas.MeasurementValueQuality", allow_none=False)

    # A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink, manual, etc. User conventions for the names of sources are contained in the introduction to IEC 61970-301.
    MeasurementValueSource = Instance("iec61970.meas.MeasurementValueSource", allow_none=False)

    # Links to the physical telemetered point associated with this measurement.
    RemoteSource = Instance("iec61970.scada.RemoteSource")

    # The time when the value was last updated
    timeStamp = AbsoluteDateTime

    # The limit, expressed as a percentage of the sensor maximum, that errors will not exceed when the sensor is used under  reference conditions.
    sensorAccuracy = PerCent

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

    # The ValueToAlias mappings included in the set
    Values = List(Instance("iec61970.meas.ValueToAlias"))

    # The Controls using the set for translation
    Controls = List(Instance("iec61970.meas.Command"))

    # The Measurements using the set for translation
    Measurements = List(Instance("iec61970.meas.Discrete"))

    #--------------------------------------------------------------------------
    #  Begin valueAliasSet user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End valueAliasSet user definitions:
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
    ValueAliasSet = Instance("iec61970.meas.ValueAliasSet", allow_none=False)

    # The value that is mapped
    value = Integer

    #--------------------------------------------------------------------------
    #  Begin valueToAlias user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End valueToAlias user definitions:
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
    isPercentageLimits = Boolean

    #--------------------------------------------------------------------------
    #  Begin limitSet user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End limitSet user definitions:
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
#  "Control" class:
#------------------------------------------------------------------------------

class Control(IdentifiedObject):
    """ Control is used for supervisory/device control. It represents control outputs that are used to change the state in a process, e.g. close or open breaker, a set point value or a raise lower command.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ControlledBy_RegulatingCondEq = Instance("iec61970.wires.RegulatingCondEq")

    Unit = Instance("iec61970.core.Unit", allow_none=False)

    # The type of Control
    ControlType = Instance("iec61970.meas.ControlType", allow_none=False)

    RemoteControl = Instance("iec61970.scada.RemoteControl")

    # The last time a control output was sent
    timeStamp = AbsoluteDateTime

    # Indicates that a client is currently sending control commands that has not completed
    operationInProgress = Boolean

    #--------------------------------------------------------------------------
    #  Begin control user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End control user definitions:
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
    MeasurementValues = List(Instance("iec61970.meas.MeasurementValue"))

    #--------------------------------------------------------------------------
    #  Begin measurementValueSource user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End measurementValueSource user definitions:
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

    # The measurement associated with the Type 
    Measurements = List(Instance("iec61970.meas.Measurement"))

    #--------------------------------------------------------------------------
    #  Begin measurementType user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End measurementType user definitions:
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
    Controls = List(Instance("iec61970.meas.Control"))

    #--------------------------------------------------------------------------
    #  Begin controlType user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End controlType user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Quality61850" class:
#------------------------------------------------------------------------------

class Quality61850(HasTraits):
    """ Quality flags in this class are as defined in IEC 61850, except for estimatorReplaced, which has been included in this class for convenience.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Validity may be good, questionable or invalid. Refer to the Validity enumeration for more details.
    validity = Validity

    # Measurement value is beyond the capability of being  represented properly. For example, a counter value overflows from maximum count back to a value of zero. 
    overFlow = Boolean

    # Measurement value is beyond a predefined range of value.
    outOfRange = Boolean

    # Measurement value may be incorrect due to a reference being out of calibration.
    badReference = Boolean

    # To prevent some overload of the communication it is sensible to detect and suppress oscillating (fast changing) binary inputs. If a signal changes in a defined time (tosc) twice in the same direction (from 0 to 1 or from 1 to 0) then oscillation is detected and the detail quality identifier 'oscillatory' is set. If it is detected a configured numbers of transient changes could be passed by. In this time the validity status 'questionable' is set. If after this defined numbers of changes the signal is still in the oscillating state the value shall be set either to the opposite state of the previous stable value or to a defined default value. In this case the validity status 'questionable' is reset and 'invalid' is set as long as the signal is oscillating. If it is configured such that no transient changes should be passed by then the validity status 'invalid' is set immediately in addition to the detail quality identifier 'oscillatory' (used for status information only).
    oscillatory = Boolean

    # This identifier indicates that a supervision function has detected an internal or external failure, e.g. communication failure.
    failure = Boolean

    # Measurement value is old and possibly invalid, as it has not been successfully updated during a specified time interval.
    oldData = Boolean

    # A correlation function has detected that the value is not consitent with other values. Typically set by a network State Estimator.
    suspect = Boolean

    # Measurement value is transmitted for test purposes.
    test = Boolean

    # Measurement value is blocked and hence unavailable for transmission. 
    operatorBlocked = Boolean

    # Source gives information related to the origin of a value. The value may be acquired from the process, defaulted or substituted.
    source = Source

    # Value has been replaced by State Estimator. estimatorReplaced is not an IEC61850 quality bit but has been put in this class for convenience.
    estimatorReplaced = Boolean

    #--------------------------------------------------------------------------
    #  Begin quality61850 user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End quality61850 user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MeasVersion" class:
#------------------------------------------------------------------------------

class MeasVersion(HasTraits):
    version = String

    date = AbsoluteDateTime

    #--------------------------------------------------------------------------
    #  Begin measVersion user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End measVersion user definitions:
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
    MeasurementValue = Instance("iec61970.meas.MeasurementValue", allow_none=False)

    #--------------------------------------------------------------------------
    #  Begin measurementValueQuality user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End measurementValueQuality user definitions:
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

    Contain_MeasurementValues = List(Instance("iec61970.meas.AccumulatorValue"))

    LimitSets = List(Instance("iec61970.meas.AccumulatorLimitSet"))

    # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
    maxValue = Integer

    #--------------------------------------------------------------------------
    #  Begin accumulator user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End accumulator user definitions:
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

    # A measurement may have zero or more limit ranges defined for it.
    LimitSets = List(Instance("iec61970.meas.AnalogLimitSet"))

    Contain_MeasurementValues = List(Instance("iec61970.meas.AnalogValue"))

    # The Control variable associated with the Measurement
    ControlledBy_Control = Instance("iec61970.meas.SetPoint")

    # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
    maxValue = Float

    # Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values
    minValue = Float

    # Normal measurement value, e.g., used for percentage calculations.
    normalValue = Float

    # If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource.
    positiveFlowIn = Boolean

    #--------------------------------------------------------------------------
    #  Begin analog user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End analog user definitions:
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

    Contain_MeasurementValues = List(Instance("iec61970.meas.DiscreteValue"))

    # The ValueAliasSet used for translation of a MeasurementValue.value to a name
    ValueAliasSet = Instance("iec61970.meas.ValueAliasSet")

    ControlledBy_Control = Instance("iec61970.meas.Command")

    # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
    maxValue = Integer

    # Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values
    minValue = Integer

    # Normal measurement value, e.g., used for percentage calculations.
    normalValue = Integer

    #--------------------------------------------------------------------------
    #  Begin discrete user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End discrete user definitions:
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

    MemberOf_Measurement = Instance("iec61970.meas.Analog", allow_none=False)

    value = Float

    #--------------------------------------------------------------------------
    #  Begin analogValue user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End analogValue user definitions:
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

    MemberOf_Measurement = Instance("iec61970.meas.Discrete", allow_none=False)

    # The value to supervise against.
    value = Integer

    #--------------------------------------------------------------------------
    #  Begin discreteValue user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End discreteValue user definitions:
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

    MemberOf_Measurement = Instance("iec61970.meas.Accumulator", allow_none=False)

    # The value to supervise against. The value is positive.
    value = Integer

    #--------------------------------------------------------------------------
    #  Begin accumulatorValue user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End accumulatorValue user definitions:
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

    LimitSet = Instance("iec61970.meas.AnalogLimitSet", allow_none=False)

    # The value to supervise against.
    value = Float

    #--------------------------------------------------------------------------
    #  Begin analogLimit user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End analogLimit user definitions:
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

    LimitSet = Instance("iec61970.meas.AccumulatorLimitSet", allow_none=False)

    # The value to supervise against. The value is positive.
    value = Integer

    #--------------------------------------------------------------------------
    #  Begin accumulatorLimit user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End accumulatorLimit user definitions:
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
    MeasuredBy_Measurement = Instance("iec61970.meas.Analog")

    # The value representing the actuator output
    value = Float

    # Normal value range maximum for any of the Control.value. Used for scaling, e.g. in bar graphs.
    maxValue = Float

    # Normal value range minimum for any of the Control.value. Used for scaling, e.g. in bar graphs.
    minValue = Float

    # Normal value for Control.value e.g. used for percentage scaling
    normalValue = Float

    #--------------------------------------------------------------------------
    #  Begin setPoint user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End setPoint user definitions:
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

    # The ValueAliasSet used for translation of a Control value to a name.
    ValueAliasSet = Instance("iec61970.meas.ValueAliasSet")

    MeasuredBy_Measurement = Instance("iec61970.meas.Discrete")

    # The value representing the actuator output
    value = Integer

    # Normal value for Control.value e.g. used for percentage scaling
    normalValue = Integer

    #--------------------------------------------------------------------------
    #  Begin command user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End command user definitions:
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

    # A measurement may have zero or more limit ranges defined for it.
    Measurements = List(Instance("iec61970.meas.Analog"))

    # The Limits used for supervision.  The name of each Limit shall reflect their ordering, e.g. HighAlarm, HighWarning, LowWarning, LowAlarm etc.
    Limits = List(Instance("iec61970.meas.AnalogLimit"))

    #--------------------------------------------------------------------------
    #  Begin analogLimitSet user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End analogLimitSet user definitions:
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

    Limits = List(Instance("iec61970.meas.AccumulatorLimit"))

    Measurements = List(Instance("iec61970.meas.Accumulator"))

    #--------------------------------------------------------------------------
    #  Begin accumulatorLimitSet user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End accumulatorLimitSet user definitions:
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

    pass
    #--------------------------------------------------------------------------
    #  Begin stringMeasurement user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End stringMeasurement user definitions:
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

    # The value to supervise against.
    value = String

    #--------------------------------------------------------------------------
    #  Begin stringMeasurementValue user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End stringMeasurementValue user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
