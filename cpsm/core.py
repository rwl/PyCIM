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

""" Contains the core PowerSystemResource and ConductingEquipment entities shared by all applications plus common collections of those entities. Not all applications require all the Core entities.Contains the core PowerSystemResource and ConductingEquipment entities shared by all applications plus common collections of those entities. Not all applications require all the Core entities.
"""

from cpsm import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_Core"

class IdentifiedObject(Element):
    """ This is a root class to provide common naming attributes for all classes needing naming attributesThis is a root class to provide common naming attributes for all classes needing naming attributes
    """
    # <<< identified_object
    # @generated
    def __init__(self, path_name='', description='', alias_name='', name='', **kw_args):
        """ Initialises a new 'IdentifiedObject' instance.
        """
        # The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root.The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root. 
        self.path_name = path_name

        # The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. 
        self.description = description

        # The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy. 
        self.alias_name = alias_name

        # The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy. 
        self.name = name



        super(IdentifiedObject, self).__init__(**kw_args)
    # >>> identified_object


    def __str__(self):
        """ Returns a string representation of the IdentifiedObject.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< identified_object.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the IdentifiedObject.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "IdentifiedObject", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "IdentifiedObject")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> identified_object.serialize


class RegularTimePoint(Element):
    """ TimePoints for a schedule where the time between the points is constant.TimePoints for a schedule where the time between the points is constant.
    """
    # <<< regular_time_point
    # @generated
    def __init__(self, value1=0.0, sequence_number=0, value2=0.0, interval_schedule=None, **kw_args):
        """ Initialises a new 'RegularTimePoint' instance.
        """
        # The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule. 
        self.value1 = value1

        # The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime.The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime. 
        self.sequence_number = sequence_number

        # The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule. 
        self.value2 = value2


        self._interval_schedule = None
        self.interval_schedule = interval_schedule


        super(RegularTimePoint, self).__init__(**kw_args)
    # >>> regular_time_point

    # <<< interval_schedule
    # @generated
    def get_interval_schedule(self):
        """ A RegularTimePoint belongs to a RegularIntervalSchedule.A RegularTimePoint belongs to a RegularIntervalSchedule.
        """
        return self._interval_schedule

    def set_interval_schedule(self, value):
        if self._interval_schedule is not None:
            filtered = [x for x in self.interval_schedule.time_points if x != self]
            self._interval_schedule._time_points = filtered

        self._interval_schedule = value
        if self._interval_schedule is not None:
            self._interval_schedule._time_points.append(self)

    interval_schedule = property(get_interval_schedule, set_interval_schedule)
    # >>> interval_schedule


    def __str__(self):
        """ Returns a string representation of the RegularTimePoint.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< regular_time_point.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RegularTimePoint.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RegularTimePoint", self.uri)
        if format:
            indent += ' ' * depth

        if self.interval_schedule is not None:
            s += '%s<%s:RegularTimePoint.interval_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.interval_schedule.uri)
        s += '%s<%s:RegularTimePoint.value1>%s</%s:RegularTimePoint.value1>' % \
            (indent, ns_prefix, self.value1, ns_prefix)
        s += '%s<%s:RegularTimePoint.sequence_number>%s</%s:RegularTimePoint.sequence_number>' % \
            (indent, ns_prefix, self.sequence_number, ns_prefix)
        s += '%s<%s:RegularTimePoint.value2>%s</%s:RegularTimePoint.value2>' % \
            (indent, ns_prefix, self.value2, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "RegularTimePoint")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> regular_time_point.serialize


class CurveData(Element):
    """ Data point values for defining a curve or scheduleData point values for defining a curve or schedule
    """
    # <<< curve_data
    # @generated
    def __init__(self, y2value=0.0, xvalue=0.0, y1value=0.0, curve_schedule=None, **kw_args):
        """ Initialises a new 'CurveData' instance.
        """
        # The data value of the second Y-axis variable (if present), depending on the Y-axis unitsThe data value of the second Y-axis variable (if present), depending on the Y-axis units 
        self.y2value = y2value

        # The data value of the X-axis variable,  depending on the X-axis unitsThe data value of the X-axis variable,  depending on the X-axis units 
        self.xvalue = xvalue

        # The data value of the  first Y-axis variable, depending on the Y-axis unitsThe data value of the  first Y-axis variable, depending on the Y-axis units 
        self.y1value = y1value


        self._curve_schedule = None
        self.curve_schedule = curve_schedule


        super(CurveData, self).__init__(**kw_args)
    # >>> curve_data

    # <<< curve_schedule
    # @generated
    def get_curve_schedule(self):
        """ The Curve defined by this CurveData.The Curve defined by this CurveData.
        """
        return self._curve_schedule

    def set_curve_schedule(self, value):
        if self._curve_schedule is not None:
            filtered = [x for x in self.curve_schedule.curve_schedule_datas if x != self]
            self._curve_schedule._curve_schedule_datas = filtered

        self._curve_schedule = value
        if self._curve_schedule is not None:
            self._curve_schedule._curve_schedule_datas.append(self)

    curve_schedule = property(get_curve_schedule, set_curve_schedule)
    # >>> curve_schedule


    def __str__(self):
        """ Returns a string representation of the CurveData.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< curve_data.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CurveData.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CurveData", self.uri)
        if format:
            indent += ' ' * depth

        if self.curve_schedule is not None:
            s += '%s<%s:CurveData.curve_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.curve_schedule.uri)
        s += '%s<%s:CurveData.y2value>%s</%s:CurveData.y2value>' % \
            (indent, ns_prefix, self.y2value, ns_prefix)
        s += '%s<%s:CurveData.xvalue>%s</%s:CurveData.xvalue>' % \
            (indent, ns_prefix, self.xvalue, ns_prefix)
        s += '%s<%s:CurveData.y1value>%s</%s:CurveData.y1value>' % \
            (indent, ns_prefix, self.y1value, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CurveData")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> curve_data.serialize


class Terminal(IdentifiedObject):
    """ An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.
    """
    # <<< terminal
    # @generated
    def __init__(self, measurements=None, regulating_control=None, connectivity_node=None, conducting_equipment=None, **kw_args):
        """ Initialises a new 'Terminal' instance.
        """

        self._measurements = []
        if measurements is not None:
            self.measurements = measurements
        else:
            self.measurements = []

        self._regulating_control = []
        if regulating_control is not None:
            self.regulating_control = regulating_control
        else:
            self.regulating_control = []

        self._connectivity_node = None
        self.connectivity_node = connectivity_node

        self._conducting_equipment = None
        self.conducting_equipment = conducting_equipment


        super(Terminal, self).__init__(**kw_args)
    # >>> terminal

    # <<< measurements
    # @generated
    def get_measurements(self):
        """ One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.
        """
        return self._measurements

    def set_measurements(self, value):
        for x in self._measurements:
            x._terminal = None
        for y in value:
            y._terminal = self
        self._measurements = value

    measurements = property(get_measurements, set_measurements)

    def add_measurements(self, *measurements):
        for obj in measurements:
            obj._terminal = self
            self._measurements.append(obj)

    def remove_measurements(self, *measurements):
        for obj in measurements:
            obj._terminal = None
            self._measurements.remove(obj)
    # >>> measurements

    # <<< regulating_control
    # @generated
    def get_regulating_control(self):
        """ The terminal is regulated by a control.The terminal is regulated by a control.
        """
        return self._regulating_control

    def set_regulating_control(self, value):
        for x in self._regulating_control:
            x._terminal = None
        for y in value:
            y._terminal = self
        self._regulating_control = value

    regulating_control = property(get_regulating_control, set_regulating_control)

    def add_regulating_control(self, *regulating_control):
        for obj in regulating_control:
            obj._terminal = self
            self._regulating_control.append(obj)

    def remove_regulating_control(self, *regulating_control):
        for obj in regulating_control:
            obj._terminal = None
            self._regulating_control.remove(obj)
    # >>> regulating_control

    # <<< connectivity_node
    # @generated
    def get_connectivity_node(self):
        """ Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
        """
        return self._connectivity_node

    def set_connectivity_node(self, value):
        if self._connectivity_node is not None:
            filtered = [x for x in self.connectivity_node.terminals if x != self]
            self._connectivity_node._terminals = filtered

        self._connectivity_node = value
        if self._connectivity_node is not None:
            self._connectivity_node._terminals.append(self)

    connectivity_node = property(get_connectivity_node, set_connectivity_node)
    # >>> connectivity_node

    # <<< conducting_equipment
    # @generated
    def get_conducting_equipment(self):
        """ ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodesConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
        """
        return self._conducting_equipment

    def set_conducting_equipment(self, value):
        if self._conducting_equipment is not None:
            filtered = [x for x in self.conducting_equipment.terminals if x != self]
            self._conducting_equipment._terminals = filtered

        self._conducting_equipment = value
        if self._conducting_equipment is not None:
            self._conducting_equipment._terminals.append(self)

    conducting_equipment = property(get_conducting_equipment, set_conducting_equipment)
    # >>> conducting_equipment


    def __str__(self):
        """ Returns a string representation of the Terminal.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< terminal.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Terminal.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Terminal", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.measurements:
            s += '%s<%s:Terminal.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.regulating_control:
            s += '%s<%s:Terminal.regulating_control rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.connectivity_node is not None:
            s += '%s<%s:Terminal.connectivity_node rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.connectivity_node.uri)
        if self.conducting_equipment is not None:
            s += '%s<%s:Terminal.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Terminal")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> terminal.serialize


class BaseVoltage(IdentifiedObject):
    """ Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.
    """
    # <<< base_voltage
    # @generated
    def __init__(self, nominal_voltage=0.0, conducting_equipment=None, voltage_level=None, **kw_args):
        """ Initialises a new 'BaseVoltage' instance.
        """
        # The PowerSystemResource's base voltage.The PowerSystemResource's base voltage. 
        self.nominal_voltage = nominal_voltage


        self._conducting_equipment = []
        if conducting_equipment is not None:
            self.conducting_equipment = conducting_equipment
        else:
            self.conducting_equipment = []

        self._voltage_level = []
        if voltage_level is not None:
            self.voltage_level = voltage_level
        else:
            self.voltage_level = []


        super(BaseVoltage, self).__init__(**kw_args)
    # >>> base_voltage

    # <<< conducting_equipment
    # @generated
    def get_conducting_equipment(self):
        """ Use association to ConductingEquipment only when there is no VoltageLevel container used.Use association to ConductingEquipment only when there is no VoltageLevel container used.
        """
        return self._conducting_equipment

    def set_conducting_equipment(self, value):
        for x in self._conducting_equipment:
            x._base_voltage = None
        for y in value:
            y._base_voltage = self
        self._conducting_equipment = value

    conducting_equipment = property(get_conducting_equipment, set_conducting_equipment)

    def add_conducting_equipment(self, *conducting_equipment):
        for obj in conducting_equipment:
            obj._base_voltage = self
            self._conducting_equipment.append(obj)

    def remove_conducting_equipment(self, *conducting_equipment):
        for obj in conducting_equipment:
            obj._base_voltage = None
            self._conducting_equipment.remove(obj)
    # >>> conducting_equipment

    # <<< voltage_level
    # @generated
    def get_voltage_level(self):
        """ The VoltageLevels having this BaseVoltage.The VoltageLevels having this BaseVoltage.
        """
        return self._voltage_level

    def set_voltage_level(self, value):
        for x in self._voltage_level:
            x._base_voltage = None
        for y in value:
            y._base_voltage = self
        self._voltage_level = value

    voltage_level = property(get_voltage_level, set_voltage_level)

    def add_voltage_level(self, *voltage_level):
        for obj in voltage_level:
            obj._base_voltage = self
            self._voltage_level.append(obj)

    def remove_voltage_level(self, *voltage_level):
        for obj in voltage_level:
            obj._base_voltage = None
            self._voltage_level.remove(obj)
    # >>> voltage_level


    def __str__(self):
        """ Returns a string representation of the BaseVoltage.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< base_voltage.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BaseVoltage.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BaseVoltage", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.conducting_equipment:
            s += '%s<%s:BaseVoltage.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.voltage_level:
            s += '%s<%s:BaseVoltage.voltage_level rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:BaseVoltage.nominal_voltage>%s</%s:BaseVoltage.nominal_voltage>' % \
            (indent, ns_prefix, self.nominal_voltage, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "BaseVoltage")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> base_voltage.serialize


class Unit(IdentifiedObject):
    """ Quantity being measured. The Unit.name shall be unique among all specified quantities and describe the quantity. The Unit.aliasName is meant to be used for localization.Quantity being measured. The Unit.name shall be unique among all specified quantities and describe the quantity. The Unit.aliasName is meant to be used for localization.
    """
    # <<< unit
    # @generated
    def __init__(self, measurements=None, **kw_args):
        """ Initialises a new 'Unit' instance.
        """

        self._measurements = []
        if measurements is not None:
            self.measurements = measurements
        else:
            self.measurements = []


        super(Unit, self).__init__(**kw_args)
    # >>> unit

    # <<< measurements
    # @generated
    def get_measurements(self):
        """ The Measurements having the UnitThe Measurements having the Unit
        """
        return self._measurements

    def set_measurements(self, value):
        for x in self._measurements:
            x._unit = None
        for y in value:
            y._unit = self
        self._measurements = value

    measurements = property(get_measurements, set_measurements)

    def add_measurements(self, *measurements):
        for obj in measurements:
            obj._unit = self
            self._measurements.append(obj)

    def remove_measurements(self, *measurements):
        for obj in measurements:
            obj._unit = None
            self._measurements.remove(obj)
    # >>> measurements


    def __str__(self):
        """ Returns a string representation of the Unit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< unit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Unit.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Unit", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.measurements:
            s += '%s<%s:Unit.measurements rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Unit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> unit.serialize


class SubGeographicalRegion(IdentifiedObject):
    """ A subset of a geographical region of a power system network model.A subset of a geographical region of a power system network model.
    """
    # <<< sub_geographical_region
    # @generated
    def __init__(self, region=None, lines=None, substations=None, **kw_args):
        """ Initialises a new 'SubGeographicalRegion' instance.
        """

        self._region = None
        self.region = region

        self._lines = []
        if lines is not None:
            self.lines = lines
        else:
            self.lines = []

        self._substations = []
        if substations is not None:
            self.substations = substations
        else:
            self.substations = []


        super(SubGeographicalRegion, self).__init__(**kw_args)
    # >>> sub_geographical_region

    # <<< region
    # @generated
    def get_region(self):
        """ The association is used in the naming hierarchy.The association is used in the naming hierarchy.
        """
        return self._region

    def set_region(self, value):
        if self._region is not None:
            filtered = [x for x in self.region.regions if x != self]
            self._region._regions = filtered

        self._region = value
        if self._region is not None:
            self._region._regions.append(self)

    region = property(get_region, set_region)
    # >>> region

    # <<< lines
    # @generated
    def get_lines(self):
        """ A Line can be contained by a SubGeographical Region.A Line can be contained by a SubGeographical Region.
        """
        return self._lines

    def set_lines(self, value):
        for x in self._lines:
            x._region = None
        for y in value:
            y._region = self
        self._lines = value

    lines = property(get_lines, set_lines)

    def add_lines(self, *lines):
        for obj in lines:
            obj._region = self
            self._lines.append(obj)

    def remove_lines(self, *lines):
        for obj in lines:
            obj._region = None
            self._lines.remove(obj)
    # >>> lines

    # <<< substations
    # @generated
    def get_substations(self):
        """ The association is used in the naming hierarchy.The association is used in the naming hierarchy.
        """
        return self._substations

    def set_substations(self, value):
        for x in self._substations:
            x._region = None
        for y in value:
            y._region = self
        self._substations = value

    substations = property(get_substations, set_substations)

    def add_substations(self, *substations):
        for obj in substations:
            obj._region = self
            self._substations.append(obj)

    def remove_substations(self, *substations):
        for obj in substations:
            obj._region = None
            self._substations.remove(obj)
    # >>> substations


    def __str__(self):
        """ Returns a string representation of the SubGeographicalRegion.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< sub_geographical_region.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SubGeographicalRegion.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SubGeographicalRegion", self.uri)
        if format:
            indent += ' ' * depth

        if self.region is not None:
            s += '%s<%s:SubGeographicalRegion.region rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.region.uri)
        for obj in self.lines:
            s += '%s<%s:SubGeographicalRegion.lines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.substations:
            s += '%s<%s:SubGeographicalRegion.substations rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "SubGeographicalRegion")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> sub_geographical_region.serialize


class Curve(IdentifiedObject):
    """ Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.
    """
    # <<< curve
    # @generated
    def __init__(self, y2_unit='w/s', x_unit='w/s', curve_style='ramp_yvalue', y1_unit='w/s', curve_schedule_datas=None, **kw_args):
        """ Initialises a new 'Curve' instance.
        """
        # The Y2-axis units of measure.The Y2-axis units of measure. Values are: "w/s", "none", "s", "h", "j/s", "va", "wh", "ohm", "m3", "hz-1", "w", "min", "rad", "g", "j", "h", "f", "kg/j", "vah", "s-1", "deg_c", "deg", "pa", "var", "s", "w/hz", "m", "m2", "hz", "a", "n", "v/var", "varh", "v"
        self.y2_unit = 'w/s'

        # The X-axis units of measure.The X-axis units of measure. Values are: "w/s", "none", "s", "h", "j/s", "va", "wh", "ohm", "m3", "hz-1", "w", "min", "rad", "g", "j", "h", "f", "kg/j", "vah", "s-1", "deg_c", "deg", "pa", "var", "s", "w/hz", "m", "m2", "hz", "a", "n", "v/var", "varh", "v"
        self.x_unit = 'w/s'

        # The style or shape of the curve.The style or shape of the curve. Values are: "ramp_yvalue", "formula", "constant_yvalue", "straight_line_yvalues"
        self.curve_style = 'ramp_yvalue'

        # The Y1-axis units of measure.The Y1-axis units of measure. Values are: "w/s", "none", "s", "h", "j/s", "va", "wh", "ohm", "m3", "hz-1", "w", "min", "rad", "g", "j", "h", "f", "kg/j", "vah", "s-1", "deg_c", "deg", "pa", "var", "s", "w/hz", "m", "m2", "hz", "a", "n", "v/var", "varh", "v"
        self.y1_unit = 'w/s'


        self._curve_schedule_datas = []
        if curve_schedule_datas is not None:
            self.curve_schedule_datas = curve_schedule_datas
        else:
            self.curve_schedule_datas = []


        super(Curve, self).__init__(**kw_args)
    # >>> curve

    # <<< curve_schedule_datas
    # @generated
    def get_curve_schedule_datas(self):
        """ The point data values that define a curveThe point data values that define a curve
        """
        return self._curve_schedule_datas

    def set_curve_schedule_datas(self, value):
        for x in self._curve_schedule_datas:
            x._curve_schedule = None
        for y in value:
            y._curve_schedule = self
        self._curve_schedule_datas = value

    curve_schedule_datas = property(get_curve_schedule_datas, set_curve_schedule_datas)

    def add_curve_schedule_datas(self, *curve_schedule_datas):
        for obj in curve_schedule_datas:
            obj._curve_schedule = self
            self._curve_schedule_datas.append(obj)

    def remove_curve_schedule_datas(self, *curve_schedule_datas):
        for obj in curve_schedule_datas:
            obj._curve_schedule = None
            self._curve_schedule_datas.remove(obj)
    # >>> curve_schedule_datas


    def __str__(self):
        """ Returns a string representation of the Curve.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< curve.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Curve.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Curve", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.curve_schedule_datas:
            s += '%s<%s:Curve.curve_schedule_datas rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Curve.y2_unit>%s</%s:Curve.y2_unit>' % \
            (indent, ns_prefix, self.y2_unit, ns_prefix)
        s += '%s<%s:Curve.x_unit>%s</%s:Curve.x_unit>' % \
            (indent, ns_prefix, self.x_unit, ns_prefix)
        s += '%s<%s:Curve.curve_style>%s</%s:Curve.curve_style>' % \
            (indent, ns_prefix, self.curve_style, ns_prefix)
        s += '%s<%s:Curve.y1_unit>%s</%s:Curve.y1_unit>' % \
            (indent, ns_prefix, self.y1_unit, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Curve")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> curve.serialize


class PowerSystemResource(IdentifiedObject):
    """ A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.
    """
    # <<< power_system_resource
    # @generated
    def __init__(self, contains_measurements=None, **kw_args):
        """ Initialises a new 'PowerSystemResource' instance.
        """

        self._contains_measurements = []
        if contains_measurements is not None:
            self.contains_measurements = contains_measurements
        else:
            self.contains_measurements = []


        super(PowerSystemResource, self).__init__(**kw_args)
    # >>> power_system_resource

    # <<< contains_measurements
    # @generated
    def get_contains_measurements(self):
        """ The Measurements that are included in the naming hierarchy where the PSR is the containing objectThe Measurements that are included in the naming hierarchy where the PSR is the containing object
        """
        return self._contains_measurements

    def set_contains_measurements(self, value):
        for x in self._contains_measurements:
            x._member_of_psr = None
        for y in value:
            y._member_of_psr = self
        self._contains_measurements = value

    contains_measurements = property(get_contains_measurements, set_contains_measurements)

    def add_contains_measurements(self, *contains_measurements):
        for obj in contains_measurements:
            obj._member_of_psr = self
            self._contains_measurements.append(obj)

    def remove_contains_measurements(self, *contains_measurements):
        for obj in contains_measurements:
            obj._member_of_psr = None
            self._contains_measurements.remove(obj)
    # >>> contains_measurements


    def __str__(self):
        """ Returns a string representation of the PowerSystemResource.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< power_system_resource.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PowerSystemResource.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PowerSystemResource", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "PowerSystemResource")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> power_system_resource.serialize


class BasicIntervalSchedule(IdentifiedObject):
    """ Schedule of values at points in time.Schedule of values at points in time.
    """
    # <<< basic_interval_schedule
    # @generated
    def __init__(self, start_time='', value1_unit='w/s', value2_unit='w/s', **kw_args):
        """ Initialises a new 'BasicIntervalSchedule' instance.
        """
        # The time for the first time point.The time for the first time point. 
        self.start_time = start_time

        # Value1 units of measure.Value1 units of measure. Values are: "w/s", "none", "s", "h", "j/s", "va", "wh", "ohm", "m3", "hz-1", "w", "min", "rad", "g", "j", "h", "f", "kg/j", "vah", "s-1", "deg_c", "deg", "pa", "var", "s", "w/hz", "m", "m2", "hz", "a", "n", "v/var", "varh", "v"
        self.value1_unit = 'w/s'

        # Value2 units of measure.Value2 units of measure. Values are: "w/s", "none", "s", "h", "j/s", "va", "wh", "ohm", "m3", "hz-1", "w", "min", "rad", "g", "j", "h", "f", "kg/j", "vah", "s-1", "deg_c", "deg", "pa", "var", "s", "w/hz", "m", "m2", "hz", "a", "n", "v/var", "varh", "v"
        self.value2_unit = 'w/s'



        super(BasicIntervalSchedule, self).__init__(**kw_args)
    # >>> basic_interval_schedule


    def __str__(self):
        """ Returns a string representation of the BasicIntervalSchedule.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< basic_interval_schedule.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BasicIntervalSchedule.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BasicIntervalSchedule", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:BasicIntervalSchedule.start_time>%s</%s:BasicIntervalSchedule.start_time>' % \
            (indent, ns_prefix, self.start_time, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value1_unit>%s</%s:BasicIntervalSchedule.value1_unit>' % \
            (indent, ns_prefix, self.value1_unit, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value2_unit>%s</%s:BasicIntervalSchedule.value2_unit>' % \
            (indent, ns_prefix, self.value2_unit, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "BasicIntervalSchedule")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> basic_interval_schedule.serialize


class GeographicalRegion(IdentifiedObject):
    """ A geographical region of a power system network model.A geographical region of a power system network model.
    """
    # <<< geographical_region
    # @generated
    def __init__(self, regions=None, **kw_args):
        """ Initialises a new 'GeographicalRegion' instance.
        """

        self._regions = []
        if regions is not None:
            self.regions = regions
        else:
            self.regions = []


        super(GeographicalRegion, self).__init__(**kw_args)
    # >>> geographical_region

    # <<< regions
    # @generated
    def get_regions(self):
        """ The association is used in the naming hierarchy.The association is used in the naming hierarchy.
        """
        return self._regions

    def set_regions(self, value):
        for x in self._regions:
            x._region = None
        for y in value:
            y._region = self
        self._regions = value

    regions = property(get_regions, set_regions)

    def add_regions(self, *regions):
        for obj in regions:
            obj._region = self
            self._regions.append(obj)

    def remove_regions(self, *regions):
        for obj in regions:
            obj._region = None
            self._regions.remove(obj)
    # >>> regions


    def __str__(self):
        """ Returns a string representation of the GeographicalRegion.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< geographical_region.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GeographicalRegion.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GeographicalRegion", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.regions:
            s += '%s<%s:GeographicalRegion.regions rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "GeographicalRegion")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> geographical_region.serialize


class RegularIntervalSchedule(BasicIntervalSchedule):
    """ The schedule has TimePoints where the time between them is constant.The schedule has TimePoints where the time between them is constant.
    """
    # <<< regular_interval_schedule
    # @generated
    def __init__(self, end_time='', time_step=0.0, time_points=None, **kw_args):
        """ Initialises a new 'RegularIntervalSchedule' instance.
        """
        # The time for the last time point.The time for the last time point. 
        self.end_time = end_time

        # The time between each pair of subsequent RegularTimePoints.The time between each pair of subsequent RegularTimePoints. 
        self.time_step = time_step


        self._time_points = []
        if time_points is not None:
            self.time_points = time_points
        else:
            self.time_points = []


        super(RegularIntervalSchedule, self).__init__(**kw_args)
    # >>> regular_interval_schedule

    # <<< time_points
    # @generated
    def get_time_points(self):
        """ The point data values that define a curveThe point data values that define a curve
        """
        return self._time_points

    def set_time_points(self, value):
        for x in self._time_points:
            x._interval_schedule = None
        for y in value:
            y._interval_schedule = self
        self._time_points = value

    time_points = property(get_time_points, set_time_points)

    def add_time_points(self, *time_points):
        for obj in time_points:
            obj._interval_schedule = self
            self._time_points.append(obj)

    def remove_time_points(self, *time_points):
        for obj in time_points:
            obj._interval_schedule = None
            self._time_points.remove(obj)
    # >>> time_points


    def __str__(self):
        """ Returns a string representation of the RegularIntervalSchedule.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< regular_interval_schedule.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RegularIntervalSchedule.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RegularIntervalSchedule", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.time_points:
            s += '%s<%s:RegularIntervalSchedule.time_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:RegularIntervalSchedule.end_time>%s</%s:RegularIntervalSchedule.end_time>' % \
            (indent, ns_prefix, self.end_time, ns_prefix)
        s += '%s<%s:RegularIntervalSchedule.time_step>%s</%s:RegularIntervalSchedule.time_step>' % \
            (indent, ns_prefix, self.time_step, ns_prefix)
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
        s += '%s<%s:BasicIntervalSchedule.start_time>%s</%s:BasicIntervalSchedule.start_time>' % \
            (indent, ns_prefix, self.start_time, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value1_unit>%s</%s:BasicIntervalSchedule.value1_unit>' % \
            (indent, ns_prefix, self.value1_unit, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value2_unit>%s</%s:BasicIntervalSchedule.value2_unit>' % \
            (indent, ns_prefix, self.value2_unit, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "RegularIntervalSchedule")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> regular_interval_schedule.serialize


class ConnectivityNodeContainer(PowerSystemResource):
    """ A base class for all objects that may contain ConnectivityNodes.A base class for all objects that may contain ConnectivityNodes.
    """
    # <<< connectivity_node_container
    # @generated
    def __init__(self, connectivity_nodes=None, **kw_args):
        """ Initialises a new 'ConnectivityNodeContainer' instance.
        """

        self._connectivity_nodes = []
        if connectivity_nodes is not None:
            self.connectivity_nodes = connectivity_nodes
        else:
            self.connectivity_nodes = []


        super(ConnectivityNodeContainer, self).__init__(**kw_args)
    # >>> connectivity_node_container

    # <<< connectivity_nodes
    # @generated
    def get_connectivity_nodes(self):
        """ Connectivity nodes contained by this container.Connectivity nodes contained by this container.
        """
        return self._connectivity_nodes

    def set_connectivity_nodes(self, value):
        for x in self._connectivity_nodes:
            x._member_of_equipment_container = None
        for y in value:
            y._member_of_equipment_container = self
        self._connectivity_nodes = value

    connectivity_nodes = property(get_connectivity_nodes, set_connectivity_nodes)

    def add_connectivity_nodes(self, *connectivity_nodes):
        for obj in connectivity_nodes:
            obj._member_of_equipment_container = self
            self._connectivity_nodes.append(obj)

    def remove_connectivity_nodes(self, *connectivity_nodes):
        for obj in connectivity_nodes:
            obj._member_of_equipment_container = None
            self._connectivity_nodes.remove(obj)
    # >>> connectivity_nodes


    def __str__(self):
        """ Returns a string representation of the ConnectivityNodeContainer.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< connectivity_node_container.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ConnectivityNodeContainer.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ConnectivityNodeContainer", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.connectivity_nodes:
            s += '%s<%s:ConnectivityNodeContainer.connectivity_nodes rdf:resource="#%s"/>' % \
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
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ConnectivityNodeContainer")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> connectivity_node_container.serialize


class EquipmentContainer(ConnectivityNodeContainer):
    """ A modeling construct to provide a root class for all Equipment classesA modeling construct to provide a root class for all Equipment classes
    """
    # <<< equipment_container
    # @generated
    def __init__(self, contains_equipments=None, **kw_args):
        """ Initialises a new 'EquipmentContainer' instance.
        """

        self._contains_equipments = []
        if contains_equipments is not None:
            self.contains_equipments = contains_equipments
        else:
            self.contains_equipments = []


        super(EquipmentContainer, self).__init__(**kw_args)
    # >>> equipment_container

    # <<< contains_equipments
    # @generated
    def get_contains_equipments(self):
        """ The association is used in the naming hierarchy.The association is used in the naming hierarchy.
        """
        return self._contains_equipments

    def set_contains_equipments(self, value):
        for x in self._contains_equipments:
            x._member_of_equipment_container = None
        for y in value:
            y._member_of_equipment_container = self
        self._contains_equipments = value

    contains_equipments = property(get_contains_equipments, set_contains_equipments)

    def add_contains_equipments(self, *contains_equipments):
        for obj in contains_equipments:
            obj._member_of_equipment_container = self
            self._contains_equipments.append(obj)

    def remove_contains_equipments(self, *contains_equipments):
        for obj in contains_equipments:
            obj._member_of_equipment_container = None
            self._contains_equipments.remove(obj)
    # >>> contains_equipments


    def __str__(self):
        """ Returns a string representation of the EquipmentContainer.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< equipment_container.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the EquipmentContainer.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "EquipmentContainer", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.contains_equipments:
            s += '%s<%s:EquipmentContainer.contains_equipments rdf:resource="#%s"/>' % \
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
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.connectivity_nodes:
            s += '%s<%s:ConnectivityNodeContainer.connectivity_nodes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "EquipmentContainer")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> equipment_container.serialize


class VoltageLevel(EquipmentContainer):
    """ A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.
    """
    # <<< voltage_level
    # @generated
    def __init__(self, low_voltage_limit=0.0, high_voltage_limit=0.0, member_of_substation=None, base_voltage=None, contains_bays=None, **kw_args):
        """ Initialises a new 'VoltageLevel' instance.
        """
        # The bus bar's low voltage limitThe bus bar's low voltage limit 
        self.low_voltage_limit = low_voltage_limit

        # The bus bar's high voltage limitThe bus bar's high voltage limit 
        self.high_voltage_limit = high_voltage_limit


        self._member_of_substation = None
        self.member_of_substation = member_of_substation

        self._base_voltage = None
        self.base_voltage = base_voltage

        self._contains_bays = []
        if contains_bays is not None:
            self.contains_bays = contains_bays
        else:
            self.contains_bays = []


        super(VoltageLevel, self).__init__(**kw_args)
    # >>> voltage_level

    # <<< member_of_substation
    # @generated
    def get_member_of_substation(self):
        """ The association is used in the naming hierarchy.The association is used in the naming hierarchy.
        """
        return self._member_of_substation

    def set_member_of_substation(self, value):
        if self._member_of_substation is not None:
            filtered = [x for x in self.member_of_substation.contains_voltage_levels if x != self]
            self._member_of_substation._contains_voltage_levels = filtered

        self._member_of_substation = value
        if self._member_of_substation is not None:
            self._member_of_substation._contains_voltage_levels.append(self)

    member_of_substation = property(get_member_of_substation, set_member_of_substation)
    # >>> member_of_substation

    # <<< base_voltage
    # @generated
    def get_base_voltage(self):
        """ The base voltage used for all equipment within the VoltageLevel.The base voltage used for all equipment within the VoltageLevel.
        """
        return self._base_voltage

    def set_base_voltage(self, value):
        if self._base_voltage is not None:
            filtered = [x for x in self.base_voltage.voltage_level if x != self]
            self._base_voltage._voltage_level = filtered

        self._base_voltage = value
        if self._base_voltage is not None:
            self._base_voltage._voltage_level.append(self)

    base_voltage = property(get_base_voltage, set_base_voltage)
    # >>> base_voltage

    # <<< contains_bays
    # @generated
    def get_contains_bays(self):
        """ The association is used in the naming hierarchy.The association is used in the naming hierarchy.
        """
        return self._contains_bays

    def set_contains_bays(self, value):
        for x in self._contains_bays:
            x._member_of_voltage_level = None
        for y in value:
            y._member_of_voltage_level = self
        self._contains_bays = value

    contains_bays = property(get_contains_bays, set_contains_bays)

    def add_contains_bays(self, *contains_bays):
        for obj in contains_bays:
            obj._member_of_voltage_level = self
            self._contains_bays.append(obj)

    def remove_contains_bays(self, *contains_bays):
        for obj in contains_bays:
            obj._member_of_voltage_level = None
            self._contains_bays.remove(obj)
    # >>> contains_bays


    def __str__(self):
        """ Returns a string representation of the VoltageLevel.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< voltage_level.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the VoltageLevel.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "VoltageLevel", self.uri)
        if format:
            indent += ' ' * depth

        if self.member_of_substation is not None:
            s += '%s<%s:VoltageLevel.member_of_substation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_substation.uri)
        if self.base_voltage is not None:
            s += '%s<%s:VoltageLevel.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        for obj in self.contains_bays:
            s += '%s<%s:VoltageLevel.contains_bays rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:VoltageLevel.low_voltage_limit>%s</%s:VoltageLevel.low_voltage_limit>' % \
            (indent, ns_prefix, self.low_voltage_limit, ns_prefix)
        s += '%s<%s:VoltageLevel.high_voltage_limit>%s</%s:VoltageLevel.high_voltage_limit>' % \
            (indent, ns_prefix, self.high_voltage_limit, ns_prefix)
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
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.connectivity_nodes:
            s += '%s<%s:ConnectivityNodeContainer.connectivity_nodes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_equipments:
            s += '%s<%s:EquipmentContainer.contains_equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "VoltageLevel")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> voltage_level.serialize


class Bay(EquipmentContainer):
    """ A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.
    """
    # <<< bay
    # @generated
    def __init__(self, member_of_voltage_level=None, **kw_args):
        """ Initialises a new 'Bay' instance.
        """

        self._member_of_voltage_level = None
        self.member_of_voltage_level = member_of_voltage_level


        super(Bay, self).__init__(**kw_args)
    # >>> bay

    # <<< member_of_voltage_level
    # @generated
    def get_member_of_voltage_level(self):
        """ The association is used in the naming hierarchy.The association is used in the naming hierarchy.
        """
        return self._member_of_voltage_level

    def set_member_of_voltage_level(self, value):
        if self._member_of_voltage_level is not None:
            filtered = [x for x in self.member_of_voltage_level.contains_bays if x != self]
            self._member_of_voltage_level._contains_bays = filtered

        self._member_of_voltage_level = value
        if self._member_of_voltage_level is not None:
            self._member_of_voltage_level._contains_bays.append(self)

    member_of_voltage_level = property(get_member_of_voltage_level, set_member_of_voltage_level)
    # >>> member_of_voltage_level


    def __str__(self):
        """ Returns a string representation of the Bay.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< bay.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Bay.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Bay", self.uri)
        if format:
            indent += ' ' * depth

        if self.member_of_voltage_level is not None:
            s += '%s<%s:Bay.member_of_voltage_level rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_voltage_level.uri)
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
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.connectivity_nodes:
            s += '%s<%s:ConnectivityNodeContainer.connectivity_nodes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_equipments:
            s += '%s<%s:EquipmentContainer.contains_equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Bay")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> bay.serialize


class Equipment(PowerSystemResource):
    """ The parts of a power system that are physical devices, electronic or mechanicalThe parts of a power system that are physical devices, electronic or mechanical
    """
    # <<< equipment
    # @generated
    def __init__(self, member_of_equipment_container=None, operational_limit_set=None, **kw_args):
        """ Initialises a new 'Equipment' instance.
        """

        self._member_of_equipment_container = None
        self.member_of_equipment_container = member_of_equipment_container

        self._operational_limit_set = []
        if operational_limit_set is not None:
            self.operational_limit_set = operational_limit_set
        else:
            self.operational_limit_set = []


        super(Equipment, self).__init__(**kw_args)
    # >>> equipment

    # <<< member_of_equipment_container
    # @generated
    def get_member_of_equipment_container(self):
        """ The association is used in the naming hierarchy.The association is used in the naming hierarchy.
        """
        return self._member_of_equipment_container

    def set_member_of_equipment_container(self, value):
        if self._member_of_equipment_container is not None:
            filtered = [x for x in self.member_of_equipment_container.contains_equipments if x != self]
            self._member_of_equipment_container._contains_equipments = filtered

        self._member_of_equipment_container = value
        if self._member_of_equipment_container is not None:
            self._member_of_equipment_container._contains_equipments.append(self)

    member_of_equipment_container = property(get_member_of_equipment_container, set_member_of_equipment_container)
    # >>> member_of_equipment_container

    # <<< operational_limit_set
    # @generated
    def get_operational_limit_set(self):
        """ The equipment limit sets associated with the equipment.The equipment limit sets associated with the equipment.
        """
        return self._operational_limit_set

    def set_operational_limit_set(self, value):
        for x in self._operational_limit_set:
            x._equipment = None
        for y in value:
            y._equipment = self
        self._operational_limit_set = value

    operational_limit_set = property(get_operational_limit_set, set_operational_limit_set)

    def add_operational_limit_set(self, *operational_limit_set):
        for obj in operational_limit_set:
            obj._equipment = self
            self._operational_limit_set.append(obj)

    def remove_operational_limit_set(self, *operational_limit_set):
        for obj in operational_limit_set:
            obj._equipment = None
            self._operational_limit_set.remove(obj)
    # >>> operational_limit_set


    def __str__(self):
        """ Returns a string representation of the Equipment.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< equipment.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Equipment.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Equipment", self.uri)
        if format:
            indent += ' ' * depth

        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        for obj in self.operational_limit_set:
            s += '%s<%s:Equipment.operational_limit_set rdf:resource="#%s"/>' % \
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
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Equipment")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> equipment.serialize


class Substation(EquipmentContainer):
    """ A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.
    """
    # <<< substation
    # @generated
    def __init__(self, region=None, contains_voltage_levels=None, **kw_args):
        """ Initialises a new 'Substation' instance.
        """

        self._region = None
        self.region = region

        self._contains_voltage_levels = []
        if contains_voltage_levels is not None:
            self.contains_voltage_levels = contains_voltage_levels
        else:
            self.contains_voltage_levels = []


        super(Substation, self).__init__(**kw_args)
    # >>> substation

    # <<< region
    # @generated
    def get_region(self):
        """ The association is used in the naming hierarchy.The association is used in the naming hierarchy.
        """
        return self._region

    def set_region(self, value):
        if self._region is not None:
            filtered = [x for x in self.region.substations if x != self]
            self._region._substations = filtered

        self._region = value
        if self._region is not None:
            self._region._substations.append(self)

    region = property(get_region, set_region)
    # >>> region

    # <<< contains_voltage_levels
    # @generated
    def get_contains_voltage_levels(self):
        """ The association is used in the naming hierarchy.The association is used in the naming hierarchy.
        """
        return self._contains_voltage_levels

    def set_contains_voltage_levels(self, value):
        for x in self._contains_voltage_levels:
            x._member_of_substation = None
        for y in value:
            y._member_of_substation = self
        self._contains_voltage_levels = value

    contains_voltage_levels = property(get_contains_voltage_levels, set_contains_voltage_levels)

    def add_contains_voltage_levels(self, *contains_voltage_levels):
        for obj in contains_voltage_levels:
            obj._member_of_substation = self
            self._contains_voltage_levels.append(obj)

    def remove_contains_voltage_levels(self, *contains_voltage_levels):
        for obj in contains_voltage_levels:
            obj._member_of_substation = None
            self._contains_voltage_levels.remove(obj)
    # >>> contains_voltage_levels


    def __str__(self):
        """ Returns a string representation of the Substation.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< substation.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Substation.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Substation", self.uri)
        if format:
            indent += ' ' * depth

        if self.region is not None:
            s += '%s<%s:Substation.region rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.region.uri)
        for obj in self.contains_voltage_levels:
            s += '%s<%s:Substation.contains_voltage_levels rdf:resource="#%s"/>' % \
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
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.connectivity_nodes:
            s += '%s<%s:ConnectivityNodeContainer.connectivity_nodes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_equipments:
            s += '%s<%s:EquipmentContainer.contains_equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Substation")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> substation.serialize


class ConductingEquipment(Equipment):
    """ The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.
    """
    # <<< conducting_equipment
    # @generated
    def __init__(self, base_voltage=None, terminals=None, **kw_args):
        """ Initialises a new 'ConductingEquipment' instance.
        """

        self._base_voltage = None
        self.base_voltage = base_voltage

        self._terminals = []
        if terminals is not None:
            self.terminals = terminals
        else:
            self.terminals = []


        super(ConductingEquipment, self).__init__(**kw_args)
    # >>> conducting_equipment

    # <<< base_voltage
    # @generated
    def get_base_voltage(self):
        """ Use association to ConductingEquipment only when there is no VoltageLevel container used.Use association to ConductingEquipment only when there is no VoltageLevel container used.
        """
        return self._base_voltage

    def set_base_voltage(self, value):
        if self._base_voltage is not None:
            filtered = [x for x in self.base_voltage.conducting_equipment if x != self]
            self._base_voltage._conducting_equipment = filtered

        self._base_voltage = value
        if self._base_voltage is not None:
            self._base_voltage._conducting_equipment.append(self)

    base_voltage = property(get_base_voltage, set_base_voltage)
    # >>> base_voltage

    # <<< terminals
    # @generated
    def get_terminals(self):
        """ ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodesConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
        """
        return self._terminals

    def set_terminals(self, value):
        for x in self._terminals:
            x._conducting_equipment = None
        for y in value:
            y._conducting_equipment = self
        self._terminals = value

    terminals = property(get_terminals, set_terminals)

    def add_terminals(self, *terminals):
        for obj in terminals:
            obj._conducting_equipment = self
            self._terminals.append(obj)

    def remove_terminals(self, *terminals):
        for obj in terminals:
            obj._conducting_equipment = None
            self._terminals.remove(obj)
    # >>> terminals


    def __str__(self):
        """ Returns a string representation of the ConductingEquipment.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< conducting_equipment.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ConductingEquipment.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ConductingEquipment", self.uri)
        if format:
            indent += ' ' * depth

        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
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
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        for obj in self.operational_limit_set:
            s += '%s<%s:Equipment.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ConductingEquipment")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> conducting_equipment.serialize


# <<< core
# @generated
# >>> core
