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

""" Contains entities that describe dynamic measurement data exchanged between applications.Contains entities that describe dynamic measurement data exchanged between applications.
"""

from cpsm.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_Meas"

class Measurement(IdentifiedObject):
    """ A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of  power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  Two possible paths exist: 1) Measurement-Terminal- ConnectivityNode-Terminal-ConductingEquipment 2) Measurement-Terminal-ConductingEquipment Alternative 2 is the only allowed use.  When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of  power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  Two possible paths exist: 1) Measurement-Terminal- ConnectivityNode-Terminal-ConductingEquipment 2) Measurement-Terminal-ConductingEquipment Alternative 2 is the only allowed use.  When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.
    """
    # <<< measurement
    # @generated
    def __init__(self, member_of_psr=None, measurement_type=None, terminal=None, unit=None, **kw_args):
        """ Initialises a new 'Measurement' instance.
        """

        self._member_of_psr = None
        self.member_of_psr = member_of_psr

        self._measurement_type = None
        self.measurement_type = measurement_type

        self._terminal = None
        self.terminal = terminal

        self._unit = None
        self.unit = unit


        super(Measurement, self).__init__(**kw_args)
    # >>> measurement

    # <<< member_of_psr
    # @generated
    def get_member_of_psr(self):
        """ The PowerSystemResource that contains the Measurement in the naming hierarchyThe PowerSystemResource that contains the Measurement in the naming hierarchy
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
        """ The type for the MeasurementThe type for the Measurement
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
        """ One or more measurements may be associated with a terminal in the networkOne or more measurements may be associated with a terminal in the network
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
        """ The Unit for the MeasurementThe Unit for the Measurement
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


    def __str__(self):
        """ Returns a string representation of the Measurement.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< measurement.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Measurement.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Measurement", self.uri)
        if format:
            indent += ' ' * depth

        if self.member_of_psr is not None:
            s += '%s<%s:Measurement.member_of_psr rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_psr.uri)
        if self.measurement_type is not None:
            s += '%s<%s:Measurement.measurement_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_type.uri)
        if self.terminal is not None:
            s += '%s<%s:Measurement.terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.terminal.uri)
        if self.unit is not None:
            s += '%s<%s:Measurement.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Measurement")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> measurement.serialize


class MeasurementValue(IdentifiedObject):
    """ The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.
    """
    # <<< measurement_value
    # @generated
    def __init__(self, measurement_value_source=None, **kw_args):
        """ Initialises a new 'MeasurementValue' instance.
        """

        self._measurement_value_source = None
        self.measurement_value_source = measurement_value_source


        super(MeasurementValue, self).__init__(**kw_args)
    # >>> measurement_value

    # <<< measurement_value_source
    # @generated
    def get_measurement_value_source(self):
        """ A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink, manual, etc. User conventions for the names of sources are contained in the introduction to IEC 61970-301.A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink, manual, etc. User conventions for the names of sources are contained in the introduction to IEC 61970-301.
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


    def __str__(self):
        """ Returns a string representation of the MeasurementValue.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< measurement_value.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MeasurementValue.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MeasurementValue", self.uri)
        if format:
            indent += ' ' * depth

        if self.measurement_value_source is not None:
            s += '%s<%s:MeasurementValue.measurement_value_source rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value_source.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MeasurementValue")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> measurement_value.serialize


class MeasurementValueSource(IdentifiedObject):
    """ MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301.MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301.
    """
    # <<< measurement_value_source
    # @generated
    def __init__(self, measurement_values=None, **kw_args):
        """ Initialises a new 'MeasurementValueSource' instance.
        """

        self._measurement_values = []
        if measurement_values is not None:
            self.measurement_values = measurement_values
        else:
            self.measurement_values = []


        super(MeasurementValueSource, self).__init__(**kw_args)
    # >>> measurement_value_source

    # <<< measurement_values
    # @generated
    def get_measurement_values(self):
        """ The MeasurementValues updated by the sourceThe MeasurementValues updated by the source
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


    def __str__(self):
        """ Returns a string representation of the MeasurementValueSource.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< measurement_value_source.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MeasurementValueSource.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MeasurementValueSource", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.measurement_values:
            s += '%s<%s:MeasurementValueSource.measurement_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MeasurementValueSource")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> measurement_value_source.serialize


class MeasurementType(IdentifiedObject):
    """ Specifies the type of Measurement, e.g. IndoorTemperature, OutDoorTemperature, BusVoltage, GeneratorVoltage, LineFlow etc. The MeasurementType.name shall be unique among all specified types and describe the type. The MeasurementType.aliasName is meant to be used for localization.Specifies the type of Measurement, e.g. IndoorTemperature, OutDoorTemperature, BusVoltage, GeneratorVoltage, LineFlow etc. The MeasurementType.name shall be unique among all specified types and describe the type. The MeasurementType.aliasName is meant to be used for localization.
    """
    # <<< measurement_type
    # @generated
    def __init__(self, measurements=None, **kw_args):
        """ Initialises a new 'MeasurementType' instance.
        """

        self._measurements = []
        if measurements is not None:
            self.measurements = measurements
        else:
            self.measurements = []


        super(MeasurementType, self).__init__(**kw_args)
    # >>> measurement_type

    # <<< measurements
    # @generated
    def get_measurements(self):
        """ The measurements associated with the TypeThe measurements associated with the Type
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


    def __str__(self):
        """ Returns a string representation of the MeasurementType.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< measurement_type.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MeasurementType.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MeasurementType", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.measurements:
            s += '%s<%s:MeasurementType.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MeasurementType")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> measurement_type.serialize


class LimitSet(IdentifiedObject):
    """ Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets corresponding to seasonal or other changing conditions. The condition is captured in the name and description attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used this way.Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets corresponding to seasonal or other changing conditions. The condition is captured in the name and description attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used this way.
    """
    # <<< limit_set
    # @generated
    def __init__(self, is_percentage_limits=False, **kw_args):
        """ Initialises a new 'LimitSet' instance.
        """
        # Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls.Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls. 
        self.is_percentage_limits = is_percentage_limits



        super(LimitSet, self).__init__(**kw_args)
    # >>> limit_set


    def __str__(self):
        """ Returns a string representation of the LimitSet.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< limit_set.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LimitSet.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LimitSet", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:LimitSet.is_percentage_limits>%s</%s:LimitSet.is_percentage_limits>' % \
            (indent, ns_prefix, self.is_percentage_limits, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LimitSet")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> limit_set.serialize


class DiscreteValue(MeasurementValue):
    """ DiscreteValue represents a discrete MeasurementValue.DiscreteValue represents a discrete MeasurementValue.
    """
    # <<< discrete_value
    # @generated
    def __init__(self, member_of_measurement=None, **kw_args):
        """ Initialises a new 'DiscreteValue' instance.
        """

        self._member_of_measurement = None
        self.member_of_measurement = member_of_measurement


        super(DiscreteValue, self).__init__(**kw_args)
    # >>> discrete_value

    # <<< member_of_measurement
    # @generated
    def get_member_of_measurement(self):
        """ Measurement to which this value is connected.Measurement to which this value is connected.
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


    def __str__(self):
        """ Returns a string representation of the DiscreteValue.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< discrete_value.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the DiscreteValue.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "DiscreteValue", self.uri)
        if format:
            indent += ' ' * depth

        if self.member_of_measurement is not None:
            s += '%s<%s:DiscreteValue.member_of_measurement rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_measurement.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        if self.measurement_value_source is not None:
            s += '%s<%s:MeasurementValue.measurement_value_source rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value_source.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "DiscreteValue")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> discrete_value.serialize


class Analog(Measurement):
    """ Analog represents an analog Measurement.Analog represents an analog Measurement.
    """
    # <<< analog
    # @generated
    def __init__(self, positive_flow_in=False, contain_measurement_values=None, **kw_args):
        """ Initialises a new 'Analog' instance.
        """
        # If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource.If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource. 
        self.positive_flow_in = positive_flow_in


        self._contain_measurement_values = []
        if contain_measurement_values is not None:
            self.contain_measurement_values = contain_measurement_values
        else:
            self.contain_measurement_values = []


        super(Analog, self).__init__(**kw_args)
    # >>> analog

    # <<< contain_measurement_values
    # @generated
    def get_contain_measurement_values(self):
        """ The values connected to this measurement.The values connected to this measurement.
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


    def __str__(self):
        """ Returns a string representation of the Analog.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< analog.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Analog.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Analog", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.contain_measurement_values:
            s += '%s<%s:Analog.contain_measurement_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Analog.positive_flow_in>%s</%s:Analog.positive_flow_in>' % \
            (indent, ns_prefix, self.positive_flow_in, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        if self.member_of_psr is not None:
            s += '%s<%s:Measurement.member_of_psr rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_psr.uri)
        if self.measurement_type is not None:
            s += '%s<%s:Measurement.measurement_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_type.uri)
        if self.terminal is not None:
            s += '%s<%s:Measurement.terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.terminal.uri)
        if self.unit is not None:
            s += '%s<%s:Measurement.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Analog")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> analog.serialize


class AnalogValue(MeasurementValue):
    """ AnalogValue represents an analog MeasurementValue.AnalogValue represents an analog MeasurementValue.
    """
    # <<< analog_value
    # @generated
    def __init__(self, member_of_measurement=None, **kw_args):
        """ Initialises a new 'AnalogValue' instance.
        """

        self._member_of_measurement = None
        self.member_of_measurement = member_of_measurement


        super(AnalogValue, self).__init__(**kw_args)
    # >>> analog_value

    # <<< member_of_measurement
    # @generated
    def get_member_of_measurement(self):
        """ Measurement to which this value is connected.Measurement to which this value is connected.
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


    def __str__(self):
        """ Returns a string representation of the AnalogValue.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< analog_value.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AnalogValue.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AnalogValue", self.uri)
        if format:
            indent += ' ' * depth

        if self.member_of_measurement is not None:
            s += '%s<%s:AnalogValue.member_of_measurement rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_measurement.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        if self.measurement_value_source is not None:
            s += '%s<%s:MeasurementValue.measurement_value_source rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value_source.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "AnalogValue")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> analog_value.serialize


class Discrete(Measurement):
    """ Discrete represents a discrete Measurement, i.e. a Measurement reprsenting discrete values, e.g. a Breaker position.Discrete represents a discrete Measurement, i.e. a Measurement reprsenting discrete values, e.g. a Breaker position.
    """
    # <<< discrete
    # @generated
    def __init__(self, contain_measurement_values=None, **kw_args):
        """ Initialises a new 'Discrete' instance.
        """

        self._contain_measurement_values = []
        if contain_measurement_values is not None:
            self.contain_measurement_values = contain_measurement_values
        else:
            self.contain_measurement_values = []


        super(Discrete, self).__init__(**kw_args)
    # >>> discrete

    # <<< contain_measurement_values
    # @generated
    def get_contain_measurement_values(self):
        """ The values connected to this measurement.The values connected to this measurement.
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


    def __str__(self):
        """ Returns a string representation of the Discrete.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< discrete.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Discrete.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Discrete", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.contain_measurement_values:
            s += '%s<%s:Discrete.contain_measurement_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        if self.member_of_psr is not None:
            s += '%s<%s:Measurement.member_of_psr rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_psr.uri)
        if self.measurement_type is not None:
            s += '%s<%s:Measurement.measurement_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_type.uri)
        if self.terminal is not None:
            s += '%s<%s:Measurement.terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.terminal.uri)
        if self.unit is not None:
            s += '%s<%s:Measurement.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Discrete")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> discrete.serialize


# <<< meas
# @generated
# >>> meas
