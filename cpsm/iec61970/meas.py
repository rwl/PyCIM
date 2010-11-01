# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

""" Contains entities that describe dynamic measurement data exchanged between applications.
"""

from cpsm.iec61970.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_Meas"

class Measurement(IdentifiedObject):
    """ A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of  power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  Two possible paths exist: 1) Measurement-Terminal- ConnectivityNode-Terminal-ConductingEquipment 2) Measurement-Terminal-ConductingEquipment Alternative 2 is the only allowed use.  When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.
    """
    # <<< measurement
    # @generated
    def __init__(self, member_of_psr=None, measurement_type=None, terminal=None, unit=None, *args, **kw_args):
        """ Initialises a new 'Measurement' instance.

        @param member_of_psr: The PowerSystemResource that contains the Measurement in the naming hierarchy
        @param measurement_type: The type for the Measurement
        @param terminal: One or more measurements may be associated with a terminal in the network
        @param unit: The Unit for the Measurement
        """

        self._member_of_psr = None
        self.member_of_psr = member_of_psr

        self._measurement_type = None
        self.measurement_type = measurement_type

        self._terminal = None
        self.terminal = terminal

        self._unit = None
        self.unit = unit


        super(Measurement, self).__init__(*args, **kw_args)
    # >>> measurement

    # <<< member_of_psr
    # @generated
    def get_member_of_psr(self):
        """ The PowerSystemResource that contains the Measurement in the naming hierarchy
        """
        return self._member_of_psr

    def set_member_of_psr(self, value):
        if self._member_of_psr is not None:
            filtered = [x for x in self.member_of_psr.contains_measurements if x != self]
            self._member_of_psr._contains_measurements = filtered

        self._member_of_psr = value
        if self._member_of_psr is not None:
            self._member_of_psr._contains_measurements.append(self)

    member_of_psr = property(get_member_of_psr, set_member_of_psr)
    # >>> member_of_psr

    # <<< measurement_type
    # @generated
    def get_measurement_type(self):
        """ The type for the Measurement
        """
        return self._measurement_type

    def set_measurement_type(self, value):
        if self._measurement_type is not None:
            filtered = [x for x in self.measurement_type.measurements if x != self]
            self._measurement_type._measurements = filtered

        self._measurement_type = value
        if self._measurement_type is not None:
            self._measurement_type._measurements.append(self)

    measurement_type = property(get_measurement_type, set_measurement_type)
    # >>> measurement_type

    # <<< terminal
    # @generated
    def get_terminal(self):
        """ One or more measurements may be associated with a terminal in the network
        """
        return self._terminal

    def set_terminal(self, value):
        if self._terminal is not None:
            filtered = [x for x in self.terminal.measurements if x != self]
            self._terminal._measurements = filtered

        self._terminal = value
        if self._terminal is not None:
            self._terminal._measurements.append(self)

    terminal = property(get_terminal, set_terminal)
    # >>> terminal

    # <<< unit
    # @generated
    def get_unit(self):
        """ The Unit for the Measurement
        """
        return self._unit

    def set_unit(self, value):
        if self._unit is not None:
            filtered = [x for x in self.unit.measurements if x != self]
            self._unit._measurements = filtered

        self._unit = value
        if self._unit is not None:
            self._unit._measurements.append(self)

    unit = property(get_unit, set_unit)
    # >>> unit



class MeasurementValue(IdentifiedObject):
    """ The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.
    """
    # <<< measurement_value
    # @generated
    def __init__(self, measurement_value_source=None, *args, **kw_args):
        """ Initialises a new 'MeasurementValue' instance.

        @param measurement_value_source: A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink, manual, etc. User conventions for the names of sources are contained in the introduction to IEC 61970-301.
        """

        self._measurement_value_source = None
        self.measurement_value_source = measurement_value_source


        super(MeasurementValue, self).__init__(*args, **kw_args)
    # >>> measurement_value

    # <<< measurement_value_source
    # @generated
    def get_measurement_value_source(self):
        """ A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink, manual, etc. User conventions for the names of sources are contained in the introduction to IEC 61970-301.
        """
        return self._measurement_value_source

    def set_measurement_value_source(self, value):
        if self._measurement_value_source is not None:
            filtered = [x for x in self.measurement_value_source.measurement_values if x != self]
            self._measurement_value_source._measurement_values = filtered

        self._measurement_value_source = value
        if self._measurement_value_source is not None:
            self._measurement_value_source._measurement_values.append(self)

    measurement_value_source = property(get_measurement_value_source, set_measurement_value_source)
    # >>> measurement_value_source



class MeasurementValueSource(IdentifiedObject):
    """ MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301.
    """
    # <<< measurement_value_source
    # @generated
    def __init__(self, measurement_values=None, *args, **kw_args):
        """ Initialises a new 'MeasurementValueSource' instance.

        @param measurement_values: The MeasurementValues updated by the source
        """

        self._measurement_values = []
        if measurement_values is not None:
            self.measurement_values = measurement_values
        else:
            self.measurement_values = []


        super(MeasurementValueSource, self).__init__(*args, **kw_args)
    # >>> measurement_value_source

    # <<< measurement_values
    # @generated
    def get_measurement_values(self):
        """ The MeasurementValues updated by the source
        """
        return self._measurement_values

    def set_measurement_values(self, value):
        for x in self._measurement_values:
            x._measurement_value_source = None
        for y in value:
            y._measurement_value_source = self
        self._measurement_values = value

    measurement_values = property(get_measurement_values, set_measurement_values)

    def add_measurement_values(self, *measurement_values):
        for obj in measurement_values:
            obj._measurement_value_source = self
            self._measurement_values.append(obj)

    def remove_measurement_values(self, *measurement_values):
        for obj in measurement_values:
            obj._measurement_value_source = None
            self._measurement_values.remove(obj)
    # >>> measurement_values



class MeasurementType(IdentifiedObject):
    """ Specifies the type of Measurement, e.g. IndoorTemperature, OutDoorTemperature, BusVoltage, GeneratorVoltage, LineFlow etc. The MeasurementType.name shall be unique among all specified types and describe the type. The MeasurementType.aliasName is meant to be used for localization.
    """
    # <<< measurement_type
    # @generated
    def __init__(self, measurements=None, *args, **kw_args):
        """ Initialises a new 'MeasurementType' instance.

        @param measurements: The measurements associated with the Type
        """

        self._measurements = []
        if measurements is not None:
            self.measurements = measurements
        else:
            self.measurements = []


        super(MeasurementType, self).__init__(*args, **kw_args)
    # >>> measurement_type

    # <<< measurements
    # @generated
    def get_measurements(self):
        """ The measurements associated with the Type
        """
        return self._measurements

    def set_measurements(self, value):
        for x in self._measurements:
            x._measurement_type = None
        for y in value:
            y._measurement_type = self
        self._measurements = value

    measurements = property(get_measurements, set_measurements)

    def add_measurements(self, *measurements):
        for obj in measurements:
            obj._measurement_type = self
            self._measurements.append(obj)

    def remove_measurements(self, *measurements):
        for obj in measurements:
            obj._measurement_type = None
            self._measurements.remove(obj)
    # >>> measurements



class LimitSet(IdentifiedObject):
    """ Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets corresponding to seasonal or other changing conditions. The condition is captured in the name and description attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used this way.
    """
    # <<< limit_set
    # @generated
    def __init__(self, is_percentage_limits=False, *args, **kw_args):
        """ Initialises a new 'LimitSet' instance.

        @param is_percentage_limits: Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls. 
        """
        # Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls. 
        self.is_percentage_limits = is_percentage_limits



        super(LimitSet, self).__init__(*args, **kw_args)
    # >>> limit_set



class DiscreteValue(MeasurementValue):
    """ DiscreteValue represents a discrete MeasurementValue.
    """
    # <<< discrete_value
    # @generated
    def __init__(self, member_of_measurement=None, *args, **kw_args):
        """ Initialises a new 'DiscreteValue' instance.

        @param member_of_measurement: Measurement to which this value is connected.
        """

        self._member_of_measurement = None
        self.member_of_measurement = member_of_measurement


        super(DiscreteValue, self).__init__(*args, **kw_args)
    # >>> discrete_value

    # <<< member_of_measurement
    # @generated
    def get_member_of_measurement(self):
        """ Measurement to which this value is connected.
        """
        return self._member_of_measurement

    def set_member_of_measurement(self, value):
        if self._member_of_measurement is not None:
            filtered = [x for x in self.member_of_measurement.contain_measurement_values if x != self]
            self._member_of_measurement._contain_measurement_values = filtered

        self._member_of_measurement = value
        if self._member_of_measurement is not None:
            self._member_of_measurement._contain_measurement_values.append(self)

    member_of_measurement = property(get_member_of_measurement, set_member_of_measurement)
    # >>> member_of_measurement



class Analog(Measurement):
    """ Analog represents an analog Measurement.
    """
    # <<< analog
    # @generated
    def __init__(self, positive_flow_in=False, contain_measurement_values=None, *args, **kw_args):
        """ Initialises a new 'Analog' instance.

        @param positive_flow_in: If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource. 
        @param contain_measurement_values: The values connected to this measurement.
        """
        # If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource. 
        self.positive_flow_in = positive_flow_in


        self._contain_measurement_values = []
        if contain_measurement_values is not None:
            self.contain_measurement_values = contain_measurement_values
        else:
            self.contain_measurement_values = []


        super(Analog, self).__init__(*args, **kw_args)
    # >>> analog

    # <<< contain_measurement_values
    # @generated
    def get_contain_measurement_values(self):
        """ The values connected to this measurement.
        """
        return self._contain_measurement_values

    def set_contain_measurement_values(self, value):
        for x in self._contain_measurement_values:
            x._member_of_measurement = None
        for y in value:
            y._member_of_measurement = self
        self._contain_measurement_values = value

    contain_measurement_values = property(get_contain_measurement_values, set_contain_measurement_values)

    def add_contain_measurement_values(self, *contain_measurement_values):
        for obj in contain_measurement_values:
            obj._member_of_measurement = self
            self._contain_measurement_values.append(obj)

    def remove_contain_measurement_values(self, *contain_measurement_values):
        for obj in contain_measurement_values:
            obj._member_of_measurement = None
            self._contain_measurement_values.remove(obj)
    # >>> contain_measurement_values



class AnalogValue(MeasurementValue):
    """ AnalogValue represents an analog MeasurementValue.
    """
    # <<< analog_value
    # @generated
    def __init__(self, member_of_measurement=None, *args, **kw_args):
        """ Initialises a new 'AnalogValue' instance.

        @param member_of_measurement: Measurement to which this value is connected.
        """

        self._member_of_measurement = None
        self.member_of_measurement = member_of_measurement


        super(AnalogValue, self).__init__(*args, **kw_args)
    # >>> analog_value

    # <<< member_of_measurement
    # @generated
    def get_member_of_measurement(self):
        """ Measurement to which this value is connected.
        """
        return self._member_of_measurement

    def set_member_of_measurement(self, value):
        if self._member_of_measurement is not None:
            filtered = [x for x in self.member_of_measurement.contain_measurement_values if x != self]
            self._member_of_measurement._contain_measurement_values = filtered

        self._member_of_measurement = value
        if self._member_of_measurement is not None:
            self._member_of_measurement._contain_measurement_values.append(self)

    member_of_measurement = property(get_member_of_measurement, set_member_of_measurement)
    # >>> member_of_measurement



class Discrete(Measurement):
    """ Discrete represents a discrete Measurement, i.e. a Measurement reprsenting discrete values, e.g. a Breaker position.
    """
    # <<< discrete
    # @generated
    def __init__(self, contain_measurement_values=None, *args, **kw_args):
        """ Initialises a new 'Discrete' instance.

        @param contain_measurement_values: The values connected to this measurement.
        """

        self._contain_measurement_values = []
        if contain_measurement_values is not None:
            self.contain_measurement_values = contain_measurement_values
        else:
            self.contain_measurement_values = []


        super(Discrete, self).__init__(*args, **kw_args)
    # >>> discrete

    # <<< contain_measurement_values
    # @generated
    def get_contain_measurement_values(self):
        """ The values connected to this measurement.
        """
        return self._contain_measurement_values

    def set_contain_measurement_values(self, value):
        for x in self._contain_measurement_values:
            x._member_of_measurement = None
        for y in value:
            y._member_of_measurement = self
        self._contain_measurement_values = value

    contain_measurement_values = property(get_contain_measurement_values, set_contain_measurement_values)

    def add_contain_measurement_values(self, *contain_measurement_values):
        for obj in contain_measurement_values:
            obj._member_of_measurement = self
            self._contain_measurement_values.append(obj)

    def remove_contain_measurement_values(self, *contain_measurement_values):
        for obj in contain_measurement_values:
            obj._member_of_measurement = None
            self._contain_measurement_values.remove(obj)
    # >>> contain_measurement_values



# <<< meas
# @generated
# >>> meas
