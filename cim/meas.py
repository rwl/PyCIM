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

""" Contains entities that describe dynamic measurement data exchanged between applications.
"""

from cim.core import IdentifiedObject
from cim import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimMeas"

ns_uri = "http://iec.ch/TC57/CIM-generic#Meas"

class Control(IdentifiedObject):
    """ Control is used for supervisory/device control. It represents control outputs that are used to change the state in a process, e.g. close or open breaker, a set point value or a raise lower command.
    """
    # <<< control
    # @generated
    def __init__(self, operation_in_progress=False, time_stamp='', unit=None, control_type=None, remote_control=None, controlled_by_regulating_cond_eq=None, **kw_args):
        """ Initialises a new 'Control' instance.
        """
        # Indicates that a client is currently sending control commands that has not completed 
        self.operation_in_progress = operation_in_progress

        # The last time a control output was sent 
        self.time_stamp = time_stamp


        self._unit = None
        self.unit = unit

        self._control_type = None
        self.control_type = control_type

        self._remote_control = None
        self.remote_control = remote_control

        self._controlled_by_regulating_cond_eq = None
        self.controlled_by_regulating_cond_eq = controlled_by_regulating_cond_eq


        super(Control, self).__init__(**kw_args)
    # >>> control

    # <<< unit
    # @generated
    def get_unit(self):
        """ The Unit for the Control.
        """
        return self._unit

    def set_unit(self, value):
        if self._unit is not None:
            filtered = [x for x in self.unit.controls if x != self]
            self._unit._controls = filtered

        self._unit = value
        if self._unit is not None:
            self._unit._controls.append(self)

    unit = property(get_unit, set_unit)
    # >>> unit

    # <<< control_type
    # @generated
    def get_control_type(self):
        """ The type of Control
        """
        return self._control_type

    def set_control_type(self, value):
        if self._control_type is not None:
            filtered = [x for x in self.control_type.controls if x != self]
            self._control_type._controls = filtered

        self._control_type = value
        if self._control_type is not None:
            self._control_type._controls.append(self)

    control_type = property(get_control_type, set_control_type)
    # >>> control_type

    # <<< remote_control
    # @generated
    def get_remote_control(self):
        """ The remote point controlling the physical actuator.
        """
        return self._remote_control

    def set_remote_control(self, value):
        if self._remote_control is not None:
            self._remote_control._control = None

        self._remote_control = value
        if self._remote_control is not None:
            self._remote_control._control = self

    remote_control = property(get_remote_control, set_remote_control)
    # >>> remote_control

    # <<< controlled_by_regulating_cond_eq
    # @generated
    def get_controlled_by_regulating_cond_eq(self):
        """ Regulating device governed by this control output.
        """
        return self._controlled_by_regulating_cond_eq

    def set_controlled_by_regulating_cond_eq(self, value):
        if self._controlled_by_regulating_cond_eq is not None:
            filtered = [x for x in self.controlled_by_regulating_cond_eq.controls if x != self]
            self._controlled_by_regulating_cond_eq._controls = filtered

        self._controlled_by_regulating_cond_eq = value
        if self._controlled_by_regulating_cond_eq is not None:
            self._controlled_by_regulating_cond_eq._controls.append(self)

    controlled_by_regulating_cond_eq = property(get_controlled_by_regulating_cond_eq, set_controlled_by_regulating_cond_eq)
    # >>> controlled_by_regulating_cond_eq


    def __str__(self):
        """ Returns a string representation of the Control.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< control.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Control.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Control", self.uri)
        if format:
            indent += ' ' * depth

        if self.unit is not None:
            s += '%s<%s:Control.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)
        if self.control_type is not None:
            s += '%s<%s:Control.control_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.control_type.uri)
        if self.remote_control is not None:
            s += '%s<%s:Control.remote_control rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.remote_control.uri)
        if self.controlled_by_regulating_cond_eq is not None:
            s += '%s<%s:Control.controlled_by_regulating_cond_eq rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.controlled_by_regulating_cond_eq.uri)
        s += '%s<%s:Control.operation_in_progress>%s</%s:Control.operation_in_progress>' % \
            (indent, ns_prefix, self.operation_in_progress, ns_prefix)
        s += '%s<%s:Control.time_stamp>%s</%s:Control.time_stamp>' % \
            (indent, ns_prefix, self.time_stamp, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Control")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> control.serialize


class Measurement(IdentifiedObject):
    """ A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  Two possible paths exist: 1) Measurement-Terminal- ConnectivityNode-Terminal-ConductingEquipment 2) Measurement-Terminal-ConductingEquipment Alternative 2 is the only allowed use.  When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.
    """
    # <<< measurement
    # @generated
    def __init__(self, unit=None, member_of_psr=None, measurement_type=None, terminal=None, **kw_args):
        """ Initialises a new 'Measurement' instance.
        """

        self._unit = None
        self.unit = unit

        self._member_of_psr = None
        self.member_of_psr = member_of_psr

        self._measurement_type = None
        self.measurement_type = measurement_type

        self._terminal = None
        self.terminal = terminal


        super(Measurement, self).__init__(**kw_args)
    # >>> measurement

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

        if self.unit is not None:
            s += '%s<%s:Measurement.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)
        if self.member_of_psr is not None:
            s += '%s<%s:Measurement.member_of_psr rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_psr.uri)
        if self.measurement_type is not None:
            s += '%s<%s:Measurement.measurement_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_type.uri)
        if self.terminal is not None:
            s += '%s<%s:Measurement.terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.terminal.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
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


class ValueAliasSet(IdentifiedObject):
    """ Describes the translation of a set of values into a name and is intendend to facilitate cusom translations. Each ValueAliasSet has a name, description etc. A specific Measurement may represent a discrete state like Open, Closed, Intermediate etc. This requires a translation from the MeasurementValue.value number to a string, e.g. 0->'Invalid', 1->'Open', 2->'Closed', 3->'Intermediate'. Each ValueToAlias member in ValueAliasSet.Value describe a mapping for one particular value to a name.
    """
    # <<< value_alias_set
    # @generated
    def __init__(self, measurements=None, commands=None, values=None, **kw_args):
        """ Initialises a new 'ValueAliasSet' instance.
        """

        self._measurements = []
        if measurements is not None:
            self.measurements = measurements
        else:
            self.measurements = []

        self._commands = []
        if commands is not None:
            self.commands = commands
        else:
            self.commands = []

        self._values = []
        if values is not None:
            self.values = values
        else:
            self.values = []


        super(ValueAliasSet, self).__init__(**kw_args)
    # >>> value_alias_set

    # <<< measurements
    # @generated
    def get_measurements(self):
        """ The Measurements using the set for translation
        """
        return self._measurements

    def set_measurements(self, value):
        for x in self._measurements:
            x._value_alias_set = None
        for y in value:
            y._value_alias_set = self
        self._measurements = value

    measurements = property(get_measurements, set_measurements)

    def add_measurements(self, *measurements):
        for obj in measurements:
            obj._value_alias_set = self
            self._measurements.append(obj)

    def remove_measurements(self, *measurements):
        for obj in measurements:
            obj._value_alias_set = None
            self._measurements.remove(obj)
    # >>> measurements

    # <<< commands
    # @generated
    def get_commands(self):
        """ The ValueAliasSet used for translation of a Control value to a name.
        """
        return self._commands

    def set_commands(self, value):
        for x in self._commands:
            x._value_alias_set = None
        for y in value:
            y._value_alias_set = self
        self._commands = value

    commands = property(get_commands, set_commands)

    def add_commands(self, *commands):
        for obj in commands:
            obj._value_alias_set = self
            self._commands.append(obj)

    def remove_commands(self, *commands):
        for obj in commands:
            obj._value_alias_set = None
            self._commands.remove(obj)
    # >>> commands

    # <<< values
    # @generated
    def get_values(self):
        """ The ValueToAlias mappings included in the set
        """
        return self._values

    def set_values(self, value):
        for x in self._values:
            x._value_alias_set = None
        for y in value:
            y._value_alias_set = self
        self._values = value

    values = property(get_values, set_values)

    def add_values(self, *values):
        for obj in values:
            obj._value_alias_set = self
            self._values.append(obj)

    def remove_values(self, *values):
        for obj in values:
            obj._value_alias_set = None
            self._values.remove(obj)
    # >>> values


    def __str__(self):
        """ Returns a string representation of the ValueAliasSet.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< value_alias_set.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ValueAliasSet.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ValueAliasSet", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.measurements:
            s += '%s<%s:ValueAliasSet.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.commands:
            s += '%s<%s:ValueAliasSet.commands rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.values:
            s += '%s<%s:ValueAliasSet.values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ValueAliasSet")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> value_alias_set.serialize


class MeasurementValue(IdentifiedObject):
    """ The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.
    """
    # <<< measurement_value
    # @generated
    def __init__(self, time_stamp='', sensor_accuracy=0.0, measurement_value_quality=None, measurement_value_source=None, remote_source=None, **kw_args):
        """ Initialises a new 'MeasurementValue' instance.
        """
        # The time when the value was last updated 
        self.time_stamp = time_stamp

        # The limit, expressed as a percentage of the sensor maximum, that errors will not exceed when the sensor is used under  reference conditions. 
        self.sensor_accuracy = sensor_accuracy


        self._measurement_value_quality = None
        self.measurement_value_quality = measurement_value_quality

        self._measurement_value_source = None
        self.measurement_value_source = measurement_value_source

        self._remote_source = None
        self.remote_source = remote_source


        super(MeasurementValue, self).__init__(**kw_args)
    # >>> measurement_value

    # <<< measurement_value_quality
    # @generated
    def get_measurement_value_quality(self):
        """ A MeasurementValue has a MeasurementValueQuality associated with it.
        """
        return self._measurement_value_quality

    def set_measurement_value_quality(self, value):
        if self._measurement_value_quality is not None:
            self._measurement_value_quality._measurement_value = None

        self._measurement_value_quality = value
        if self._measurement_value_quality is not None:
            self._measurement_value_quality._measurement_value = self

    measurement_value_quality = property(get_measurement_value_quality, set_measurement_value_quality)
    # >>> measurement_value_quality

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

    # <<< remote_source
    # @generated
    def get_remote_source(self):
        """ Link to the physical telemetered point associated with this measurement.
        """
        return self._remote_source

    def set_remote_source(self, value):
        if self._remote_source is not None:
            self._remote_source._measurement_value = None

        self._remote_source = value
        if self._remote_source is not None:
            self._remote_source._measurement_value = self

    remote_source = property(get_remote_source, set_remote_source)
    # >>> remote_source


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

        if self.measurement_value_quality is not None:
            s += '%s<%s:MeasurementValue.measurement_value_quality rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value_quality.uri)
        if self.measurement_value_source is not None:
            s += '%s<%s:MeasurementValue.measurement_value_source rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value_source.uri)
        if self.remote_source is not None:
            s += '%s<%s:MeasurementValue.remote_source rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.remote_source.uri)
        s += '%s<%s:MeasurementValue.time_stamp>%s</%s:MeasurementValue.time_stamp>' % \
            (indent, ns_prefix, self.time_stamp, ns_prefix)
        s += '%s<%s:MeasurementValue.sensor_accuracy>%s</%s:MeasurementValue.sensor_accuracy>' % \
            (indent, ns_prefix, self.sensor_accuracy, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
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


class Limit(IdentifiedObject):
    """ Specifies one limit value for a Measurement. A Measurement typically has several limits that are kept together by the LimitSet class. The actual meaning and use of a Limit instance (i.e., if it is an alarm or warning limit or if it is a high or low limit) is not captured in the Limit class. However the name of a Limit instance may indicate both meaning and use.
    """
    pass
    # <<< limit
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'Limit' instance.
        """


        super(Limit, self).__init__(**kw_args)
    # >>> limit


    def __str__(self):
        """ Returns a string representation of the Limit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< limit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Limit.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Limit", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Limit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> limit.serialize


class LimitSet(IdentifiedObject):
    """ Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets corresponding to seasonal or other changing conditions. The condition is captured in the name and description attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used this way.
    """
    # <<< limit_set
    # @generated
    def __init__(self, is_percentage_limits=False, **kw_args):
        """ Initialises a new 'LimitSet' instance.
        """
        # Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls. 
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
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
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


class ValueToAlias(IdentifiedObject):
    """ Describes the translation of one particular value into a name, e.g. 1->'Open'
    """
    # <<< value_to_alias
    # @generated
    def __init__(self, value=0, value_alias_set=None, **kw_args):
        """ Initialises a new 'ValueToAlias' instance.
        """
        # The value that is mapped 
        self.value = value


        self._value_alias_set = None
        self.value_alias_set = value_alias_set


        super(ValueToAlias, self).__init__(**kw_args)
    # >>> value_to_alias

    # <<< value_alias_set
    # @generated
    def get_value_alias_set(self):
        """ The ValueAliasSet having the ValueToAlias mappings
        """
        return self._value_alias_set

    def set_value_alias_set(self, value):
        if self._value_alias_set is not None:
            filtered = [x for x in self.value_alias_set.values if x != self]
            self._value_alias_set._values = filtered

        self._value_alias_set = value
        if self._value_alias_set is not None:
            self._value_alias_set._values.append(self)

    value_alias_set = property(get_value_alias_set, set_value_alias_set)
    # >>> value_alias_set


    def __str__(self):
        """ Returns a string representation of the ValueToAlias.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< value_to_alias.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ValueToAlias.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ValueToAlias", self.uri)
        if format:
            indent += ' ' * depth

        if self.value_alias_set is not None:
            s += '%s<%s:ValueToAlias.value_alias_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.value_alias_set.uri)
        s += '%s<%s:ValueToAlias.value>%s</%s:ValueToAlias.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ValueToAlias")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> value_to_alias.serialize


class ControlType(IdentifiedObject):
    """ Specifies the type of Control, e.g. BreakerOn/Off, GeneratorVoltageSetPoint, TieLineFlow etc. The ControlType.name shall be unique among all specified types and describe the type. The ControlType.aliasName is meant to be used for localization.
    """
    # <<< control_type
    # @generated
    def __init__(self, controls=None, **kw_args):
        """ Initialises a new 'ControlType' instance.
        """

        self._controls = []
        if controls is not None:
            self.controls = controls
        else:
            self.controls = []


        super(ControlType, self).__init__(**kw_args)
    # >>> control_type

    # <<< controls
    # @generated
    def get_controls(self):
        """ The Controls having the ControlType
        """
        return self._controls

    def set_controls(self, value):
        for x in self._controls:
            x._control_type = None
        for y in value:
            y._control_type = self
        self._controls = value

    controls = property(get_controls, set_controls)

    def add_controls(self, *controls):
        for obj in controls:
            obj._control_type = self
            self._controls.append(obj)

    def remove_controls(self, *controls):
        for obj in controls:
            obj._control_type = None
            self._controls.remove(obj)
    # >>> controls


    def __str__(self):
        """ Returns a string representation of the ControlType.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< control_type.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ControlType.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ControlType", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.controls:
            s += '%s<%s:ControlType.controls rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ControlType")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> control_type.serialize


class MeasurementValueSource(IdentifiedObject):
    """ MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301.
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
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
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
    """ Specifies the type of Measurement, e.g. IndoorTemperature, OutDoorTemperature, BusVoltage, GeneratorVoltage, LineFlow etc. The MeasurementType.name shall be unique among all specified types and describe the type. The MeasurementType.aliasName is meant to be used for localization.
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
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
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


class Quality61850(Element):
    """ Quality flags in this class are as defined in IEC 61850, except for estimatorReplaced, which has been included in this class for convenience.
    """
    # <<< quality61850
    # @generated
    def __init__(self, validity='good', source='defaulted', operator_blocked=False, oscillatory=False, suspect=False, out_of_range=False, old_data=False, failure=False, bad_reference=False, over_flow=False, test=False, estimator_replaced=False, **kw_args):
        """ Initialises a new 'Quality61850' instance.
        """
        # Validity of the measurement value. Values are: "good", "invalid", "questionable"
        self.validity = 'good'

        # Source gives information related to the origin of a value. The value may be acquired from the process, defaulted or substituted. Values are: "defaulted", "substituted", "process"
        self.source = 'defaulted'

        # Measurement value is blocked and hence unavailable for transmission. 
        self.operator_blocked = operator_blocked

        # To prevent some overload of the communication it is sensible to detect and suppress oscillating (fast changing) binary inputs. If a signal changes in a defined time (tosc) twice in the same direction (from 0 to 1 or from 1 to 0) then oscillation is detected and the detail quality identifier 'oscillatory' is set. If it is detected a configured numbers of transient changes could be passed by. In this time the validity status 'questionable' is set. If after this defined numbers of changes the signal is still in the oscillating state the value shall be set either to the opposite state of the previous stable value or to a defined default value. In this case the validity status 'questionable' is reset and 'invalid' is set as long as the signal is oscillating. If it is configured such that no transient changes should be passed by then the validity status 'invalid' is set immediately in addition to the detail quality identifier 'oscillatory' (used for status information only). 
        self.oscillatory = oscillatory

        # A correlation function has detected that the value is not consitent with other values. Typically set by a network State Estimator. 
        self.suspect = suspect

        # Measurement value is beyond a predefined range of value. 
        self.out_of_range = out_of_range

        # Measurement value is old and possibly invalid, as it has not been successfully updated during a specified time interval. 
        self.old_data = old_data

        # This identifier indicates that a supervision function has detected an internal or external failure, e.g. communication failure. 
        self.failure = failure

        # Measurement value may be incorrect due to a reference being out of calibration. 
        self.bad_reference = bad_reference

        # Measurement value is beyond the capability of being  represented properly. For example, a counter value overflows from maximum count back to a value of zero. 
        self.over_flow = over_flow

        # Measurement value is transmitted for test purposes. 
        self.test = test

        # Value has been replaced by State Estimator. estimatorReplaced is not an IEC61850 quality bit but has been put in this class for convenience. 
        self.estimator_replaced = estimator_replaced



        super(Quality61850, self).__init__(**kw_args)
    # >>> quality61850


    def __str__(self):
        """ Returns a string representation of the Quality61850.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< quality61850.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Quality61850.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Quality61850", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:Quality61850.validity>%s</%s:Quality61850.validity>' % \
            (indent, ns_prefix, self.validity, ns_prefix)
        s += '%s<%s:Quality61850.source>%s</%s:Quality61850.source>' % \
            (indent, ns_prefix, self.source, ns_prefix)
        s += '%s<%s:Quality61850.operator_blocked>%s</%s:Quality61850.operator_blocked>' % \
            (indent, ns_prefix, self.operator_blocked, ns_prefix)
        s += '%s<%s:Quality61850.oscillatory>%s</%s:Quality61850.oscillatory>' % \
            (indent, ns_prefix, self.oscillatory, ns_prefix)
        s += '%s<%s:Quality61850.suspect>%s</%s:Quality61850.suspect>' % \
            (indent, ns_prefix, self.suspect, ns_prefix)
        s += '%s<%s:Quality61850.out_of_range>%s</%s:Quality61850.out_of_range>' % \
            (indent, ns_prefix, self.out_of_range, ns_prefix)
        s += '%s<%s:Quality61850.old_data>%s</%s:Quality61850.old_data>' % \
            (indent, ns_prefix, self.old_data, ns_prefix)
        s += '%s<%s:Quality61850.failure>%s</%s:Quality61850.failure>' % \
            (indent, ns_prefix, self.failure, ns_prefix)
        s += '%s<%s:Quality61850.bad_reference>%s</%s:Quality61850.bad_reference>' % \
            (indent, ns_prefix, self.bad_reference, ns_prefix)
        s += '%s<%s:Quality61850.over_flow>%s</%s:Quality61850.over_flow>' % \
            (indent, ns_prefix, self.over_flow, ns_prefix)
        s += '%s<%s:Quality61850.test>%s</%s:Quality61850.test>' % \
            (indent, ns_prefix, self.test, ns_prefix)
        s += '%s<%s:Quality61850.estimator_replaced>%s</%s:Quality61850.estimator_replaced>' % \
            (indent, ns_prefix, self.estimator_replaced, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Quality61850")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> quality61850.serialize


class StringMeasurement(Measurement):
    """ StringMeasurement represents a measurement with values of type string.
    """
    # <<< string_measurement
    # @generated
    def __init__(self, contains_measurement_values=None, **kw_args):
        """ Initialises a new 'StringMeasurement' instance.
        """

        self._contains_measurement_values = []
        if contains_measurement_values is not None:
            self.contains_measurement_values = contains_measurement_values
        else:
            self.contains_measurement_values = []


        super(StringMeasurement, self).__init__(**kw_args)
    # >>> string_measurement

    # <<< contains_measurement_values
    # @generated
    def get_contains_measurement_values(self):
        """ The values connected to this measurement.
        """
        return self._contains_measurement_values

    def set_contains_measurement_values(self, value):
        for x in self._contains_measurement_values:
            x._member_of_measurement = None
        for y in value:
            y._member_of_measurement = self
        self._contains_measurement_values = value

    contains_measurement_values = property(get_contains_measurement_values, set_contains_measurement_values)

    def add_contains_measurement_values(self, *contains_measurement_values):
        for obj in contains_measurement_values:
            obj._member_of_measurement = self
            self._contains_measurement_values.append(obj)

    def remove_contains_measurement_values(self, *contains_measurement_values):
        for obj in contains_measurement_values:
            obj._member_of_measurement = None
            self._contains_measurement_values.remove(obj)
    # >>> contains_measurement_values


    def __str__(self):
        """ Returns a string representation of the StringMeasurement.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< string_measurement.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the StringMeasurement.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "StringMeasurement", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.contains_measurement_values:
            s += '%s<%s:StringMeasurement.contains_measurement_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        if self.unit is not None:
            s += '%s<%s:Measurement.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)
        if self.member_of_psr is not None:
            s += '%s<%s:Measurement.member_of_psr rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_psr.uri)
        if self.measurement_type is not None:
            s += '%s<%s:Measurement.measurement_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_type.uri)
        if self.terminal is not None:
            s += '%s<%s:Measurement.terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.terminal.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "StringMeasurement")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> string_measurement.serialize


class Discrete(Measurement):
    """ Discrete represents a discrete Measurement, i.e. a Measurement reprsenting discrete values, e.g. a Breaker position.
    """
    # <<< discrete
    # @generated
    def __init__(self, max_value=0, normal_value=0, min_value=0, controlled_by_control=None, value_alias_set=None, contain_measurement_values=None, **kw_args):
        """ Initialises a new 'Discrete' instance.
        """
        # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values. 
        self.max_value = max_value

        # Normal measurement value, e.g., used for percentage calculations. 
        self.normal_value = normal_value

        # Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values 
        self.min_value = min_value


        self._controlled_by_control = None
        self.controlled_by_control = controlled_by_control

        self._value_alias_set = None
        self.value_alias_set = value_alias_set

        self._contain_measurement_values = []
        if contain_measurement_values is not None:
            self.contain_measurement_values = contain_measurement_values
        else:
            self.contain_measurement_values = []


        super(Discrete, self).__init__(**kw_args)
    # >>> discrete

    # <<< controlled_by_control
    # @generated
    def get_controlled_by_control(self):
        """ The Control variable associated with the Measurement.
        """
        return self._controlled_by_control

    def set_controlled_by_control(self, value):
        if self._controlled_by_control is not None:
            self._controlled_by_control._measured_by_measurement = None

        self._controlled_by_control = value
        if self._controlled_by_control is not None:
            self._controlled_by_control._measured_by_measurement = self

    controlled_by_control = property(get_controlled_by_control, set_controlled_by_control)
    # >>> controlled_by_control

    # <<< value_alias_set
    # @generated
    def get_value_alias_set(self):
        """ The ValueAliasSet used for translation of a MeasurementValue.value to a name
        """
        return self._value_alias_set

    def set_value_alias_set(self, value):
        if self._value_alias_set is not None:
            filtered = [x for x in self.value_alias_set.measurements if x != self]
            self._value_alias_set._measurements = filtered

        self._value_alias_set = value
        if self._value_alias_set is not None:
            self._value_alias_set._measurements.append(self)

    value_alias_set = property(get_value_alias_set, set_value_alias_set)
    # >>> value_alias_set

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

        if self.controlled_by_control is not None:
            s += '%s<%s:Discrete.controlled_by_control rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.controlled_by_control.uri)
        if self.value_alias_set is not None:
            s += '%s<%s:Discrete.value_alias_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.value_alias_set.uri)
        for obj in self.contain_measurement_values:
            s += '%s<%s:Discrete.contain_measurement_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Discrete.max_value>%s</%s:Discrete.max_value>' % \
            (indent, ns_prefix, self.max_value, ns_prefix)
        s += '%s<%s:Discrete.normal_value>%s</%s:Discrete.normal_value>' % \
            (indent, ns_prefix, self.normal_value, ns_prefix)
        s += '%s<%s:Discrete.min_value>%s</%s:Discrete.min_value>' % \
            (indent, ns_prefix, self.min_value, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        if self.unit is not None:
            s += '%s<%s:Measurement.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)
        if self.member_of_psr is not None:
            s += '%s<%s:Measurement.member_of_psr rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_psr.uri)
        if self.measurement_type is not None:
            s += '%s<%s:Measurement.measurement_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_type.uri)
        if self.terminal is not None:
            s += '%s<%s:Measurement.terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.terminal.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Discrete")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> discrete.serialize


class DiscreteValue(MeasurementValue):
    """ DiscreteValue represents a discrete MeasurementValue.
    """
    # <<< discrete_value
    # @generated
    def __init__(self, value=0, member_of_measurement=None, **kw_args):
        """ Initialises a new 'DiscreteValue' instance.
        """
        # The value to supervise. 
        self.value = value


        self._member_of_measurement = None
        self.member_of_measurement = member_of_measurement


        super(DiscreteValue, self).__init__(**kw_args)
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
        s += '%s<%s:DiscreteValue.value>%s</%s:DiscreteValue.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        if self.measurement_value_quality is not None:
            s += '%s<%s:MeasurementValue.measurement_value_quality rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value_quality.uri)
        if self.measurement_value_source is not None:
            s += '%s<%s:MeasurementValue.measurement_value_source rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value_source.uri)
        if self.remote_source is not None:
            s += '%s<%s:MeasurementValue.remote_source rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.remote_source.uri)
        s += '%s<%s:MeasurementValue.time_stamp>%s</%s:MeasurementValue.time_stamp>' % \
            (indent, ns_prefix, self.time_stamp, ns_prefix)
        s += '%s<%s:MeasurementValue.sensor_accuracy>%s</%s:MeasurementValue.sensor_accuracy>' % \
            (indent, ns_prefix, self.sensor_accuracy, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "DiscreteValue")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> discrete_value.serialize


class AnalogLimit(Limit):
    """ Limit values for Analog measurements
    """
    # <<< analog_limit
    # @generated
    def __init__(self, value=0.0, limit_set=None, **kw_args):
        """ Initialises a new 'AnalogLimit' instance.
        """
        # The value to supervise against. 
        self.value = value


        self._limit_set = None
        self.limit_set = limit_set


        super(AnalogLimit, self).__init__(**kw_args)
    # >>> analog_limit

    # <<< limit_set
    # @generated
    def get_limit_set(self):
        """ The set of limits.
        """
        return self._limit_set

    def set_limit_set(self, value):
        if self._limit_set is not None:
            filtered = [x for x in self.limit_set.limits if x != self]
            self._limit_set._limits = filtered

        self._limit_set = value
        if self._limit_set is not None:
            self._limit_set._limits.append(self)

    limit_set = property(get_limit_set, set_limit_set)
    # >>> limit_set


    def __str__(self):
        """ Returns a string representation of the AnalogLimit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< analog_limit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AnalogLimit.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AnalogLimit", self.uri)
        if format:
            indent += ' ' * depth

        if self.limit_set is not None:
            s += '%s<%s:AnalogLimit.limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.limit_set.uri)
        s += '%s<%s:AnalogLimit.value>%s</%s:AnalogLimit.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "AnalogLimit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> analog_limit.serialize


class AccumulatorLimitSet(LimitSet):
    """ An AccumulatorLimitSet specifies a set of Limits that are associated with an Accumulator measurement.
    """
    # <<< accumulator_limit_set
    # @generated
    def __init__(self, limits=None, measurements=None, **kw_args):
        """ Initialises a new 'AccumulatorLimitSet' instance.
        """

        self._limits = []
        if limits is not None:
            self.limits = limits
        else:
            self.limits = []

        self._measurements = []
        if measurements is not None:
            self.measurements = measurements
        else:
            self.measurements = []


        super(AccumulatorLimitSet, self).__init__(**kw_args)
    # >>> accumulator_limit_set

    # <<< limits
    # @generated
    def get_limits(self):
        """ The limit values used for supervision of Measurements.
        """
        return self._limits

    def set_limits(self, value):
        for x in self._limits:
            x._limit_set = None
        for y in value:
            y._limit_set = self
        self._limits = value

    limits = property(get_limits, set_limits)

    def add_limits(self, *limits):
        for obj in limits:
            obj._limit_set = self
            self._limits.append(obj)

    def remove_limits(self, *limits):
        for obj in limits:
            obj._limit_set = None
            self._limits.remove(obj)
    # >>> limits

    # <<< measurements
    # @generated
    def get_measurements(self):
        """ The Measurements using the LimitSet.
        """
        return self._measurements

    def set_measurements(self, value):
        for p in self._measurements:
            filtered = [q for q in p.limit_sets if q != self]
            self._measurements._limit_sets = filtered
        for r in value:
            if self not in r._limit_sets:
                r._limit_sets.append(self)
        self._measurements = value

    measurements = property(get_measurements, set_measurements)

    def add_measurements(self, *measurements):
        for obj in measurements:
            if self not in obj._limit_sets:
                obj._limit_sets.append(self)
            self._measurements.append(obj)

    def remove_measurements(self, *measurements):
        for obj in measurements:
            if self in obj._limit_sets:
                obj._limit_sets.remove(self)
            self._measurements.remove(obj)
    # >>> measurements


    def __str__(self):
        """ Returns a string representation of the AccumulatorLimitSet.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< accumulator_limit_set.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AccumulatorLimitSet.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AccumulatorLimitSet", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.limits:
            s += '%s<%s:AccumulatorLimitSet.limits rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:AccumulatorLimitSet.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:LimitSet.is_percentage_limits>%s</%s:LimitSet.is_percentage_limits>' % \
            (indent, ns_prefix, self.is_percentage_limits, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "AccumulatorLimitSet")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> accumulator_limit_set.serialize


class SetPoint(Control):
    """ A SetPoint is an analog control used for supervisory control.
    """
    # <<< set_point
    # @generated
    def __init__(self, normal_value=0.0, min_value=0.0, value=0.0, max_value=0.0, measured_by_measurement=None, **kw_args):
        """ Initialises a new 'SetPoint' instance.
        """
        # Normal value for Control.value e.g. used for percentage scaling 
        self.normal_value = normal_value

        # Normal value range minimum for any of the Control.value. Used for scaling, e.g. in bar graphs. 
        self.min_value = min_value

        # The value representing the actuator output 
        self.value = value

        # Normal value range maximum for any of the Control.value. Used for scaling, e.g. in bar graphs. 
        self.max_value = max_value


        self._measured_by_measurement = None
        self.measured_by_measurement = measured_by_measurement


        super(SetPoint, self).__init__(**kw_args)
    # >>> set_point

    # <<< measured_by_measurement
    # @generated
    def get_measured_by_measurement(self):
        """ The Measurement variable used for control
        """
        return self._measured_by_measurement

    def set_measured_by_measurement(self, value):
        if self._measured_by_measurement is not None:
            self._measured_by_measurement._controlled_by_control = None

        self._measured_by_measurement = value
        if self._measured_by_measurement is not None:
            self._measured_by_measurement._controlled_by_control = self

    measured_by_measurement = property(get_measured_by_measurement, set_measured_by_measurement)
    # >>> measured_by_measurement


    def __str__(self):
        """ Returns a string representation of the SetPoint.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< set_point.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SetPoint.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SetPoint", self.uri)
        if format:
            indent += ' ' * depth

        if self.measured_by_measurement is not None:
            s += '%s<%s:SetPoint.measured_by_measurement rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measured_by_measurement.uri)
        s += '%s<%s:SetPoint.normal_value>%s</%s:SetPoint.normal_value>' % \
            (indent, ns_prefix, self.normal_value, ns_prefix)
        s += '%s<%s:SetPoint.min_value>%s</%s:SetPoint.min_value>' % \
            (indent, ns_prefix, self.min_value, ns_prefix)
        s += '%s<%s:SetPoint.value>%s</%s:SetPoint.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        s += '%s<%s:SetPoint.max_value>%s</%s:SetPoint.max_value>' % \
            (indent, ns_prefix, self.max_value, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        if self.unit is not None:
            s += '%s<%s:Control.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)
        if self.control_type is not None:
            s += '%s<%s:Control.control_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.control_type.uri)
        if self.remote_control is not None:
            s += '%s<%s:Control.remote_control rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.remote_control.uri)
        if self.controlled_by_regulating_cond_eq is not None:
            s += '%s<%s:Control.controlled_by_regulating_cond_eq rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.controlled_by_regulating_cond_eq.uri)
        s += '%s<%s:Control.operation_in_progress>%s</%s:Control.operation_in_progress>' % \
            (indent, ns_prefix, self.operation_in_progress, ns_prefix)
        s += '%s<%s:Control.time_stamp>%s</%s:Control.time_stamp>' % \
            (indent, ns_prefix, self.time_stamp, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SetPoint")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> set_point.serialize


class Command(Control):
    """ A Command is a discrete control used for supervisory control.
    """
    # <<< command
    # @generated
    def __init__(self, normal_value=0, value=0, measured_by_measurement=None, value_alias_set=None, **kw_args):
        """ Initialises a new 'Command' instance.
        """
        # Normal value for Control.value e.g. used for percentage scaling 
        self.normal_value = normal_value

        # The value representing the actuator output 
        self.value = value


        self._measured_by_measurement = None
        self.measured_by_measurement = measured_by_measurement

        self._value_alias_set = None
        self.value_alias_set = value_alias_set


        super(Command, self).__init__(**kw_args)
    # >>> command

    # <<< measured_by_measurement
    # @generated
    def get_measured_by_measurement(self):
        """ The Measurement variable used for control.
        """
        return self._measured_by_measurement

    def set_measured_by_measurement(self, value):
        if self._measured_by_measurement is not None:
            self._measured_by_measurement._controlled_by_control = None

        self._measured_by_measurement = value
        if self._measured_by_measurement is not None:
            self._measured_by_measurement._controlled_by_control = self

    measured_by_measurement = property(get_measured_by_measurement, set_measured_by_measurement)
    # >>> measured_by_measurement

    # <<< value_alias_set
    # @generated
    def get_value_alias_set(self):
        """ The Commands using the set for translation.
        """
        return self._value_alias_set

    def set_value_alias_set(self, value):
        if self._value_alias_set is not None:
            filtered = [x for x in self.value_alias_set.commands if x != self]
            self._value_alias_set._commands = filtered

        self._value_alias_set = value
        if self._value_alias_set is not None:
            self._value_alias_set._commands.append(self)

    value_alias_set = property(get_value_alias_set, set_value_alias_set)
    # >>> value_alias_set


    def __str__(self):
        """ Returns a string representation of the Command.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< command.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Command.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Command", self.uri)
        if format:
            indent += ' ' * depth

        if self.measured_by_measurement is not None:
            s += '%s<%s:Command.measured_by_measurement rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measured_by_measurement.uri)
        if self.value_alias_set is not None:
            s += '%s<%s:Command.value_alias_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.value_alias_set.uri)
        s += '%s<%s:Command.normal_value>%s</%s:Command.normal_value>' % \
            (indent, ns_prefix, self.normal_value, ns_prefix)
        s += '%s<%s:Command.value>%s</%s:Command.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        if self.unit is not None:
            s += '%s<%s:Control.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)
        if self.control_type is not None:
            s += '%s<%s:Control.control_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.control_type.uri)
        if self.remote_control is not None:
            s += '%s<%s:Control.remote_control rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.remote_control.uri)
        if self.controlled_by_regulating_cond_eq is not None:
            s += '%s<%s:Control.controlled_by_regulating_cond_eq rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.controlled_by_regulating_cond_eq.uri)
        s += '%s<%s:Control.operation_in_progress>%s</%s:Control.operation_in_progress>' % \
            (indent, ns_prefix, self.operation_in_progress, ns_prefix)
        s += '%s<%s:Control.time_stamp>%s</%s:Control.time_stamp>' % \
            (indent, ns_prefix, self.time_stamp, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Command")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> command.serialize


class StringMeasurementValue(MeasurementValue):
    """ StringMeasurementValue represents a measurement value of type string.
    """
    # <<< string_measurement_value
    # @generated
    def __init__(self, value='', member_of_measurement=None, **kw_args):
        """ Initialises a new 'StringMeasurementValue' instance.
        """
        # The value to supervise. 
        self.value = value


        self._member_of_measurement = None
        self.member_of_measurement = member_of_measurement


        super(StringMeasurementValue, self).__init__(**kw_args)
    # >>> string_measurement_value

    # <<< member_of_measurement
    # @generated
    def get_member_of_measurement(self):
        """ Measurement to which this value is connected.
        """
        return self._member_of_measurement

    def set_member_of_measurement(self, value):
        if self._member_of_measurement is not None:
            filtered = [x for x in self.member_of_measurement.contains_measurement_values if x != self]
            self._member_of_measurement._contains_measurement_values = filtered

        self._member_of_measurement = value
        if self._member_of_measurement is not None:
            self._member_of_measurement._contains_measurement_values.append(self)

    member_of_measurement = property(get_member_of_measurement, set_member_of_measurement)
    # >>> member_of_measurement


    def __str__(self):
        """ Returns a string representation of the StringMeasurementValue.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< string_measurement_value.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the StringMeasurementValue.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "StringMeasurementValue", self.uri)
        if format:
            indent += ' ' * depth

        if self.member_of_measurement is not None:
            s += '%s<%s:StringMeasurementValue.member_of_measurement rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_measurement.uri)
        s += '%s<%s:StringMeasurementValue.value>%s</%s:StringMeasurementValue.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        if self.measurement_value_quality is not None:
            s += '%s<%s:MeasurementValue.measurement_value_quality rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value_quality.uri)
        if self.measurement_value_source is not None:
            s += '%s<%s:MeasurementValue.measurement_value_source rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value_source.uri)
        if self.remote_source is not None:
            s += '%s<%s:MeasurementValue.remote_source rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.remote_source.uri)
        s += '%s<%s:MeasurementValue.time_stamp>%s</%s:MeasurementValue.time_stamp>' % \
            (indent, ns_prefix, self.time_stamp, ns_prefix)
        s += '%s<%s:MeasurementValue.sensor_accuracy>%s</%s:MeasurementValue.sensor_accuracy>' % \
            (indent, ns_prefix, self.sensor_accuracy, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "StringMeasurementValue")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> string_measurement_value.serialize


class AnalogLimitSet(LimitSet):
    """ An AnalogLimitSet specifies a set of Limits that are associated with an Analog measurement.
    """
    # <<< analog_limit_set
    # @generated
    def __init__(self, limits=None, measurements=None, **kw_args):
        """ Initialises a new 'AnalogLimitSet' instance.
        """

        self._limits = []
        if limits is not None:
            self.limits = limits
        else:
            self.limits = []

        self._measurements = []
        if measurements is not None:
            self.measurements = measurements
        else:
            self.measurements = []


        super(AnalogLimitSet, self).__init__(**kw_args)
    # >>> analog_limit_set

    # <<< limits
    # @generated
    def get_limits(self):
        """ The limit values used for supervision of Measurements.
        """
        return self._limits

    def set_limits(self, value):
        for x in self._limits:
            x._limit_set = None
        for y in value:
            y._limit_set = self
        self._limits = value

    limits = property(get_limits, set_limits)

    def add_limits(self, *limits):
        for obj in limits:
            obj._limit_set = self
            self._limits.append(obj)

    def remove_limits(self, *limits):
        for obj in limits:
            obj._limit_set = None
            self._limits.remove(obj)
    # >>> limits

    # <<< measurements
    # @generated
    def get_measurements(self):
        """ The Measurements using the LimitSet.
        """
        return self._measurements

    def set_measurements(self, value):
        for p in self._measurements:
            filtered = [q for q in p.limit_sets if q != self]
            self._measurements._limit_sets = filtered
        for r in value:
            if self not in r._limit_sets:
                r._limit_sets.append(self)
        self._measurements = value

    measurements = property(get_measurements, set_measurements)

    def add_measurements(self, *measurements):
        for obj in measurements:
            if self not in obj._limit_sets:
                obj._limit_sets.append(self)
            self._measurements.append(obj)

    def remove_measurements(self, *measurements):
        for obj in measurements:
            if self in obj._limit_sets:
                obj._limit_sets.remove(self)
            self._measurements.remove(obj)
    # >>> measurements


    def __str__(self):
        """ Returns a string representation of the AnalogLimitSet.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< analog_limit_set.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AnalogLimitSet.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AnalogLimitSet", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.limits:
            s += '%s<%s:AnalogLimitSet.limits rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:AnalogLimitSet.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:LimitSet.is_percentage_limits>%s</%s:LimitSet.is_percentage_limits>' % \
            (indent, ns_prefix, self.is_percentage_limits, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "AnalogLimitSet")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> analog_limit_set.serialize


class Accumulator(Measurement):
    """ Accumulator represents a accumulated (counted) Measurement, e.g. an energy value.
    """
    # <<< accumulator
    # @generated
    def __init__(self, max_value=0, limit_sets=None, contain_measurement_values=None, **kw_args):
        """ Initialises a new 'Accumulator' instance.
        """
        # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values. 
        self.max_value = max_value


        self._limit_sets = []
        if limit_sets is not None:
            self.limit_sets = limit_sets
        else:
            self.limit_sets = []

        self._contain_measurement_values = []
        if contain_measurement_values is not None:
            self.contain_measurement_values = contain_measurement_values
        else:
            self.contain_measurement_values = []


        super(Accumulator, self).__init__(**kw_args)
    # >>> accumulator

    # <<< limit_sets
    # @generated
    def get_limit_sets(self):
        """ A measurement may have zero or more limit ranges defined for it.
        """
        return self._limit_sets

    def set_limit_sets(self, value):
        for p in self._limit_sets:
            filtered = [q for q in p.measurements if q != self]
            self._limit_sets._measurements = filtered
        for r in value:
            if self not in r._measurements:
                r._measurements.append(self)
        self._limit_sets = value

    limit_sets = property(get_limit_sets, set_limit_sets)

    def add_limit_sets(self, *limit_sets):
        for obj in limit_sets:
            if self not in obj._measurements:
                obj._measurements.append(self)
            self._limit_sets.append(obj)

    def remove_limit_sets(self, *limit_sets):
        for obj in limit_sets:
            if self in obj._measurements:
                obj._measurements.remove(self)
            self._limit_sets.remove(obj)
    # >>> limit_sets

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


    def __str__(self):
        """ Returns a string representation of the Accumulator.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< accumulator.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Accumulator.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Accumulator", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.limit_sets:
            s += '%s<%s:Accumulator.limit_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contain_measurement_values:
            s += '%s<%s:Accumulator.contain_measurement_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Accumulator.max_value>%s</%s:Accumulator.max_value>' % \
            (indent, ns_prefix, self.max_value, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        if self.unit is not None:
            s += '%s<%s:Measurement.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)
        if self.member_of_psr is not None:
            s += '%s<%s:Measurement.member_of_psr rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_psr.uri)
        if self.measurement_type is not None:
            s += '%s<%s:Measurement.measurement_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_type.uri)
        if self.terminal is not None:
            s += '%s<%s:Measurement.terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.terminal.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Accumulator")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> accumulator.serialize


class AccumulatorLimit(Limit):
    """ Limit values for Accumulator measurements
    """
    # <<< accumulator_limit
    # @generated
    def __init__(self, value=0, limit_set=None, **kw_args):
        """ Initialises a new 'AccumulatorLimit' instance.
        """
        # The value to supervise against. The value is positive. 
        self.value = value


        self._limit_set = None
        self.limit_set = limit_set


        super(AccumulatorLimit, self).__init__(**kw_args)
    # >>> accumulator_limit

    # <<< limit_set
    # @generated
    def get_limit_set(self):
        """ The set of limits.
        """
        return self._limit_set

    def set_limit_set(self, value):
        if self._limit_set is not None:
            filtered = [x for x in self.limit_set.limits if x != self]
            self._limit_set._limits = filtered

        self._limit_set = value
        if self._limit_set is not None:
            self._limit_set._limits.append(self)

    limit_set = property(get_limit_set, set_limit_set)
    # >>> limit_set


    def __str__(self):
        """ Returns a string representation of the AccumulatorLimit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< accumulator_limit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AccumulatorLimit.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AccumulatorLimit", self.uri)
        if format:
            indent += ' ' * depth

        if self.limit_set is not None:
            s += '%s<%s:AccumulatorLimit.limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.limit_set.uri)
        s += '%s<%s:AccumulatorLimit.value>%s</%s:AccumulatorLimit.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "AccumulatorLimit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> accumulator_limit.serialize


class AnalogValue(MeasurementValue):
    """ AnalogValue represents an analog MeasurementValue.
    """
    # <<< analog_value
    # @generated
    def __init__(self, value=0.0, member_of_measurement=None, alt_generating_unit=None, alt_tie_meas=None, **kw_args):
        """ Initialises a new 'AnalogValue' instance.
        """
        # The value to supervise. 
        self.value = value


        self._member_of_measurement = None
        self.member_of_measurement = member_of_measurement

        self._alt_generating_unit = []
        if alt_generating_unit is not None:
            self.alt_generating_unit = alt_generating_unit
        else:
            self.alt_generating_unit = []

        self._alt_tie_meas = []
        if alt_tie_meas is not None:
            self.alt_tie_meas = alt_tie_meas
        else:
            self.alt_tie_meas = []


        super(AnalogValue, self).__init__(**kw_args)
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

    # <<< alt_generating_unit
    # @generated
    def get_alt_generating_unit(self):
        """ The alternate generating unit for which this measurement value applies.
        """
        return self._alt_generating_unit

    def set_alt_generating_unit(self, value):
        for x in self._alt_generating_unit:
            x._analog_value = None
        for y in value:
            y._analog_value = self
        self._alt_generating_unit = value

    alt_generating_unit = property(get_alt_generating_unit, set_alt_generating_unit)

    def add_alt_generating_unit(self, *alt_generating_unit):
        for obj in alt_generating_unit:
            obj._analog_value = self
            self._alt_generating_unit.append(obj)

    def remove_alt_generating_unit(self, *alt_generating_unit):
        for obj in alt_generating_unit:
            obj._analog_value = None
            self._alt_generating_unit.remove(obj)
    # >>> alt_generating_unit

    # <<< alt_tie_meas
    # @generated
    def get_alt_tie_meas(self):
        """ The usage of the measurement within the control area specification.
        """
        return self._alt_tie_meas

    def set_alt_tie_meas(self, value):
        for x in self._alt_tie_meas:
            x._analog_value = None
        for y in value:
            y._analog_value = self
        self._alt_tie_meas = value

    alt_tie_meas = property(get_alt_tie_meas, set_alt_tie_meas)

    def add_alt_tie_meas(self, *alt_tie_meas):
        for obj in alt_tie_meas:
            obj._analog_value = self
            self._alt_tie_meas.append(obj)

    def remove_alt_tie_meas(self, *alt_tie_meas):
        for obj in alt_tie_meas:
            obj._analog_value = None
            self._alt_tie_meas.remove(obj)
    # >>> alt_tie_meas


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
        for obj in self.alt_generating_unit:
            s += '%s<%s:AnalogValue.alt_generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.alt_tie_meas:
            s += '%s<%s:AnalogValue.alt_tie_meas rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:AnalogValue.value>%s</%s:AnalogValue.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        if self.measurement_value_quality is not None:
            s += '%s<%s:MeasurementValue.measurement_value_quality rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value_quality.uri)
        if self.measurement_value_source is not None:
            s += '%s<%s:MeasurementValue.measurement_value_source rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value_source.uri)
        if self.remote_source is not None:
            s += '%s<%s:MeasurementValue.remote_source rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.remote_source.uri)
        s += '%s<%s:MeasurementValue.time_stamp>%s</%s:MeasurementValue.time_stamp>' % \
            (indent, ns_prefix, self.time_stamp, ns_prefix)
        s += '%s<%s:MeasurementValue.sensor_accuracy>%s</%s:MeasurementValue.sensor_accuracy>' % \
            (indent, ns_prefix, self.sensor_accuracy, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "AnalogValue")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> analog_value.serialize


class Analog(Measurement):
    """ Analog represents an analog Measurement.
    """
    # <<< analog
    # @generated
    def __init__(self, max_value=0.0, positive_flow_in=False, normal_value=0.0, min_value=0.0, contain_measurement_values=None, limit_sets=None, controlled_by_control=None, **kw_args):
        """ Initialises a new 'Analog' instance.
        """
        # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values. 
        self.max_value = max_value

        # If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource. 
        self.positive_flow_in = positive_flow_in

        # Normal measurement value, e.g., used for percentage calculations. 
        self.normal_value = normal_value

        # Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values 
        self.min_value = min_value


        self._contain_measurement_values = []
        if contain_measurement_values is not None:
            self.contain_measurement_values = contain_measurement_values
        else:
            self.contain_measurement_values = []

        self._limit_sets = []
        if limit_sets is not None:
            self.limit_sets = limit_sets
        else:
            self.limit_sets = []

        self._controlled_by_control = None
        self.controlled_by_control = controlled_by_control


        super(Analog, self).__init__(**kw_args)
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

    # <<< limit_sets
    # @generated
    def get_limit_sets(self):
        """ A measurement may have zero or more limit ranges defined for it.
        """
        return self._limit_sets

    def set_limit_sets(self, value):
        for p in self._limit_sets:
            filtered = [q for q in p.measurements if q != self]
            self._limit_sets._measurements = filtered
        for r in value:
            if self not in r._measurements:
                r._measurements.append(self)
        self._limit_sets = value

    limit_sets = property(get_limit_sets, set_limit_sets)

    def add_limit_sets(self, *limit_sets):
        for obj in limit_sets:
            if self not in obj._measurements:
                obj._measurements.append(self)
            self._limit_sets.append(obj)

    def remove_limit_sets(self, *limit_sets):
        for obj in limit_sets:
            if self in obj._measurements:
                obj._measurements.remove(self)
            self._limit_sets.remove(obj)
    # >>> limit_sets

    # <<< controlled_by_control
    # @generated
    def get_controlled_by_control(self):
        """ The Control variable associated with the Measurement
        """
        return self._controlled_by_control

    def set_controlled_by_control(self, value):
        if self._controlled_by_control is not None:
            self._controlled_by_control._measured_by_measurement = None

        self._controlled_by_control = value
        if self._controlled_by_control is not None:
            self._controlled_by_control._measured_by_measurement = self

    controlled_by_control = property(get_controlled_by_control, set_controlled_by_control)
    # >>> controlled_by_control


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
        for obj in self.limit_sets:
            s += '%s<%s:Analog.limit_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.controlled_by_control is not None:
            s += '%s<%s:Analog.controlled_by_control rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.controlled_by_control.uri)
        s += '%s<%s:Analog.max_value>%s</%s:Analog.max_value>' % \
            (indent, ns_prefix, self.max_value, ns_prefix)
        s += '%s<%s:Analog.positive_flow_in>%s</%s:Analog.positive_flow_in>' % \
            (indent, ns_prefix, self.positive_flow_in, ns_prefix)
        s += '%s<%s:Analog.normal_value>%s</%s:Analog.normal_value>' % \
            (indent, ns_prefix, self.normal_value, ns_prefix)
        s += '%s<%s:Analog.min_value>%s</%s:Analog.min_value>' % \
            (indent, ns_prefix, self.min_value, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        if self.unit is not None:
            s += '%s<%s:Measurement.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)
        if self.member_of_psr is not None:
            s += '%s<%s:Measurement.member_of_psr rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_psr.uri)
        if self.measurement_type is not None:
            s += '%s<%s:Measurement.measurement_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_type.uri)
        if self.terminal is not None:
            s += '%s<%s:Measurement.terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.terminal.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Analog")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> analog.serialize


class MeasurementValueQuality(Quality61850):
    """ Measurement quality flags. Bits 0-10 are defined for substation automation in draft IEC 61850 part 7-3. Bits 11-15 are reserved for future expansion by that document. Bits 16-31 are reserved for EMS applications.
    """
    # <<< measurement_value_quality
    # @generated
    def __init__(self, measurement_value=None, **kw_args):
        """ Initialises a new 'MeasurementValueQuality' instance.
        """

        self._measurement_value = None
        self.measurement_value = measurement_value


        super(MeasurementValueQuality, self).__init__(**kw_args)
    # >>> measurement_value_quality

    # <<< measurement_value
    # @generated
    def get_measurement_value(self):
        """ A MeasurementValue has a MeasurementValueQuality associated with it.
        """
        return self._measurement_value

    def set_measurement_value(self, value):
        if self._measurement_value is not None:
            self._measurement_value._measurement_value_quality = None

        self._measurement_value = value
        if self._measurement_value is not None:
            self._measurement_value._measurement_value_quality = self

    measurement_value = property(get_measurement_value, set_measurement_value)
    # >>> measurement_value


    def __str__(self):
        """ Returns a string representation of the MeasurementValueQuality.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< measurement_value_quality.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MeasurementValueQuality.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MeasurementValueQuality", self.uri)
        if format:
            indent += ' ' * depth

        if self.measurement_value is not None:
            s += '%s<%s:MeasurementValueQuality.measurement_value rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:Quality61850.validity>%s</%s:Quality61850.validity>' % \
            (indent, ns_prefix, self.validity, ns_prefix)
        s += '%s<%s:Quality61850.source>%s</%s:Quality61850.source>' % \
            (indent, ns_prefix, self.source, ns_prefix)
        s += '%s<%s:Quality61850.operator_blocked>%s</%s:Quality61850.operator_blocked>' % \
            (indent, ns_prefix, self.operator_blocked, ns_prefix)
        s += '%s<%s:Quality61850.oscillatory>%s</%s:Quality61850.oscillatory>' % \
            (indent, ns_prefix, self.oscillatory, ns_prefix)
        s += '%s<%s:Quality61850.suspect>%s</%s:Quality61850.suspect>' % \
            (indent, ns_prefix, self.suspect, ns_prefix)
        s += '%s<%s:Quality61850.out_of_range>%s</%s:Quality61850.out_of_range>' % \
            (indent, ns_prefix, self.out_of_range, ns_prefix)
        s += '%s<%s:Quality61850.old_data>%s</%s:Quality61850.old_data>' % \
            (indent, ns_prefix, self.old_data, ns_prefix)
        s += '%s<%s:Quality61850.failure>%s</%s:Quality61850.failure>' % \
            (indent, ns_prefix, self.failure, ns_prefix)
        s += '%s<%s:Quality61850.bad_reference>%s</%s:Quality61850.bad_reference>' % \
            (indent, ns_prefix, self.bad_reference, ns_prefix)
        s += '%s<%s:Quality61850.over_flow>%s</%s:Quality61850.over_flow>' % \
            (indent, ns_prefix, self.over_flow, ns_prefix)
        s += '%s<%s:Quality61850.test>%s</%s:Quality61850.test>' % \
            (indent, ns_prefix, self.test, ns_prefix)
        s += '%s<%s:Quality61850.estimator_replaced>%s</%s:Quality61850.estimator_replaced>' % \
            (indent, ns_prefix, self.estimator_replaced, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MeasurementValueQuality")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> measurement_value_quality.serialize


class AccumulatorValue(MeasurementValue):
    """ AccumulatorValue represents a accumulated (counted) MeasurementValue.
    """
    # <<< accumulator_value
    # @generated
    def __init__(self, value=0, member_of_measurement=None, **kw_args):
        """ Initialises a new 'AccumulatorValue' instance.
        """
        # The value to supervise. The value is positive. 
        self.value = value


        self._member_of_measurement = None
        self.member_of_measurement = member_of_measurement


        super(AccumulatorValue, self).__init__(**kw_args)
    # >>> accumulator_value

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


    def __str__(self):
        """ Returns a string representation of the AccumulatorValue.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< accumulator_value.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AccumulatorValue.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AccumulatorValue", self.uri)
        if format:
            indent += ' ' * depth

        if self.member_of_measurement is not None:
            s += '%s<%s:AccumulatorValue.member_of_measurement rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_measurement.uri)
        s += '%s<%s:AccumulatorValue.value>%s</%s:AccumulatorValue.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        if self.measurement_value_quality is not None:
            s += '%s<%s:MeasurementValue.measurement_value_quality rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value_quality.uri)
        if self.measurement_value_source is not None:
            s += '%s<%s:MeasurementValue.measurement_value_source rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value_source.uri)
        if self.remote_source is not None:
            s += '%s<%s:MeasurementValue.remote_source rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.remote_source.uri)
        s += '%s<%s:MeasurementValue.time_stamp>%s</%s:MeasurementValue.time_stamp>' % \
            (indent, ns_prefix, self.time_stamp, ns_prefix)
        s += '%s<%s:MeasurementValue.sensor_accuracy>%s</%s:MeasurementValue.sensor_accuracy>' % \
            (indent, ns_prefix, self.sensor_accuracy, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "AccumulatorValue")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> accumulator_value.serialize


# <<< meas
# @generated
# >>> meas
