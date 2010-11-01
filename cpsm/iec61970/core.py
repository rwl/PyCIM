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

""" Contains the core PowerSystemResource and ConductingEquipment entities shared by all applications plus common collections of those entities. Not all applications require all the Core entities.
"""

from cpsm import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_Core"

class IdentifiedObject(Element):
    """ This is a root class to provide common naming attributes for all classes needing naming attributes
    """
    # <<< identified_object
    # @generated
    def __init__(self, path_name='', description='', alias_name='', name='', *args, **kw_args):
        """ Initialises a new 'IdentifiedObject' instance.

        @param path_name: The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root. 
        @param description: The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. 
        @param alias_name: The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy. 
        @param name: The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy. 
        """
        # The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root. 
        self.path_name = path_name

        # The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. 
        self.description = description

        # The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy. 
        self.alias_name = alias_name

        # The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy. 
        self.name = name



        super(IdentifiedObject, self).__init__(*args, **kw_args)
    # >>> identified_object



class RegularTimePoint(Element):
    """ TimePoints for a schedule where the time between the points is constant.
    """
    # <<< regular_time_point
    # @generated
    def __init__(self, value1=0.0, sequence_number=0, value2=0.0, interval_schedule=None, *args, **kw_args):
        """ Initialises a new 'RegularTimePoint' instance.

        @param value1: The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule. 
        @param sequence_number: The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime. 
        @param value2: The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule. 
        @param interval_schedule: A RegularTimePoint belongs to a RegularIntervalSchedule.
        """
        # The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule. 
        self.value1 = value1

        # The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime. 
        self.sequence_number = sequence_number

        # The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule. 
        self.value2 = value2


        self._interval_schedule = None
        self.interval_schedule = interval_schedule


        super(RegularTimePoint, self).__init__(*args, **kw_args)
    # >>> regular_time_point

    # <<< interval_schedule
    # @generated
    def get_interval_schedule(self):
        """ A RegularTimePoint belongs to a RegularIntervalSchedule.
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



class CurveData(Element):
    """ Data point values for defining a curve or schedule
    """
    # <<< curve_data
    # @generated
    def __init__(self, y2value=0.0, xvalue=0.0, y1value=0.0, curve_schedule=None, *args, **kw_args):
        """ Initialises a new 'CurveData' instance.

        @param y2value: The data value of the second Y-axis variable (if present), depending on the Y-axis units 
        @param xvalue: The data value of the X-axis variable,  depending on the X-axis units 
        @param y1value: The data value of the  first Y-axis variable, depending on the Y-axis units 
        @param curve_schedule: The Curve defined by this CurveData.
        """
        # The data value of the second Y-axis variable (if present), depending on the Y-axis units 
        self.y2value = y2value

        # The data value of the X-axis variable,  depending on the X-axis units 
        self.xvalue = xvalue

        # The data value of the  first Y-axis variable, depending on the Y-axis units 
        self.y1value = y1value


        self._curve_schedule = None
        self.curve_schedule = curve_schedule


        super(CurveData, self).__init__(*args, **kw_args)
    # >>> curve_data

    # <<< curve_schedule
    # @generated
    def get_curve_schedule(self):
        """ The Curve defined by this CurveData.
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



class Terminal(IdentifiedObject):
    """ An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.
    """
    # <<< terminal
    # @generated
    def __init__(self, measurements=None, regulating_control=None, connectivity_node=None, conducting_equipment=None, *args, **kw_args):
        """ Initialises a new 'Terminal' instance.

        @param measurements: One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.
        @param regulating_control: The terminal is regulated by a control.
        @param connectivity_node: Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
        @param conducting_equipment: ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
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


        super(Terminal, self).__init__(*args, **kw_args)
    # >>> terminal

    # <<< measurements
    # @generated
    def get_measurements(self):
        """ One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.
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
        """ The terminal is regulated by a control.
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
        """ Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
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
        """ ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
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



class BaseVoltage(IdentifiedObject):
    """ Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.
    """
    # <<< base_voltage
    # @generated
    def __init__(self, nominal_voltage=0.0, conducting_equipment=None, voltage_level=None, *args, **kw_args):
        """ Initialises a new 'BaseVoltage' instance.

        @param nominal_voltage: The PowerSystemResource's base voltage. 
        @param conducting_equipment: Use association to ConductingEquipment only when there is no VoltageLevel container used.
        @param voltage_level: The VoltageLevels having this BaseVoltage.
        """
        # The PowerSystemResource's base voltage. 
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


        super(BaseVoltage, self).__init__(*args, **kw_args)
    # >>> base_voltage

    # <<< conducting_equipment
    # @generated
    def get_conducting_equipment(self):
        """ Use association to ConductingEquipment only when there is no VoltageLevel container used.
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
        """ The VoltageLevels having this BaseVoltage.
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



class Unit(IdentifiedObject):
    """ Quantity being measured. The Unit.name shall be unique among all specified quantities and describe the quantity. The Unit.aliasName is meant to be used for localization.
    """
    # <<< unit
    # @generated
    def __init__(self, measurements=None, *args, **kw_args):
        """ Initialises a new 'Unit' instance.

        @param measurements: The Measurements having the Unit
        """

        self._measurements = []
        if measurements is not None:
            self.measurements = measurements
        else:
            self.measurements = []


        super(Unit, self).__init__(*args, **kw_args)
    # >>> unit

    # <<< measurements
    # @generated
    def get_measurements(self):
        """ The Measurements having the Unit
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



class SubGeographicalRegion(IdentifiedObject):
    """ A subset of a geographical region of a power system network model.
    """
    # <<< sub_geographical_region
    # @generated
    def __init__(self, region=None, lines=None, substations=None, *args, **kw_args):
        """ Initialises a new 'SubGeographicalRegion' instance.

        @param region: The association is used in the naming hierarchy.
        @param lines: A Line can be contained by a SubGeographical Region.
        @param substations: The association is used in the naming hierarchy.
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


        super(SubGeographicalRegion, self).__init__(*args, **kw_args)
    # >>> sub_geographical_region

    # <<< region
    # @generated
    def get_region(self):
        """ The association is used in the naming hierarchy.
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
        """ A Line can be contained by a SubGeographical Region.
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
        """ The association is used in the naming hierarchy.
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



class Curve(IdentifiedObject):
    """ Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.
    """
    # <<< curve
    # @generated
    def __init__(self, y2_unit='w/s', x_unit='w/s', curve_style='ramp_yvalue', y1_unit='w/s', curve_schedule_datas=None, *args, **kw_args):
        """ Initialises a new 'Curve' instance.

        @param y2_unit: The Y2-axis units of measure. Values are: "w/s", "none", "s", "h", "j/s", "va", "wh", "ohm", "m3", "hz-1", "w", "min", "rad", "g", "j", "h", "f", "kg/j", "vah", "s-1", "º_c", "deg", "pa", "var", "s", "w/hz", "m", "m2", "hz", "a", "n", "v/var", "varh", "v"
        @param x_unit: The X-axis units of measure. Values are: "w/s", "none", "s", "h", "j/s", "va", "wh", "ohm", "m3", "hz-1", "w", "min", "rad", "g", "j", "h", "f", "kg/j", "vah", "s-1", "º_c", "deg", "pa", "var", "s", "w/hz", "m", "m2", "hz", "a", "n", "v/var", "varh", "v"
        @param curve_style: The style or shape of the curve. Values are: "ramp_yvalue", "formula", "constant_yvalue", "straight_line_yvalues"
        @param y1_unit: The Y1-axis units of measure. Values are: "w/s", "none", "s", "h", "j/s", "va", "wh", "ohm", "m3", "hz-1", "w", "min", "rad", "g", "j", "h", "f", "kg/j", "vah", "s-1", "º_c", "deg", "pa", "var", "s", "w/hz", "m", "m2", "hz", "a", "n", "v/var", "varh", "v"
        @param curve_schedule_datas: The point data values that define a curve
        """
        # The Y2-axis units of measure. Values are: "w/s", "none", "s", "h", "j/s", "va", "wh", "ohm", "m3", "hz-1", "w", "min", "rad", "g", "j", "h", "f", "kg/j", "vah", "s-1", "º_c", "deg", "pa", "var", "s", "w/hz", "m", "m2", "hz", "a", "n", "v/var", "varh", "v"
        self.y2_unit = y2_unit

        # The X-axis units of measure. Values are: "w/s", "none", "s", "h", "j/s", "va", "wh", "ohm", "m3", "hz-1", "w", "min", "rad", "g", "j", "h", "f", "kg/j", "vah", "s-1", "º_c", "deg", "pa", "var", "s", "w/hz", "m", "m2", "hz", "a", "n", "v/var", "varh", "v"
        self.x_unit = x_unit

        # The style or shape of the curve. Values are: "ramp_yvalue", "formula", "constant_yvalue", "straight_line_yvalues"
        self.curve_style = curve_style

        # The Y1-axis units of measure. Values are: "w/s", "none", "s", "h", "j/s", "va", "wh", "ohm", "m3", "hz-1", "w", "min", "rad", "g", "j", "h", "f", "kg/j", "vah", "s-1", "º_c", "deg", "pa", "var", "s", "w/hz", "m", "m2", "hz", "a", "n", "v/var", "varh", "v"
        self.y1_unit = y1_unit


        self._curve_schedule_datas = []
        if curve_schedule_datas is not None:
            self.curve_schedule_datas = curve_schedule_datas
        else:
            self.curve_schedule_datas = []


        super(Curve, self).__init__(*args, **kw_args)
    # >>> curve

    # <<< curve_schedule_datas
    # @generated
    def get_curve_schedule_datas(self):
        """ The point data values that define a curve
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



class PowerSystemResource(IdentifiedObject):
    """ A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.
    """
    # <<< power_system_resource
    # @generated
    def __init__(self, contains_measurements=None, *args, **kw_args):
        """ Initialises a new 'PowerSystemResource' instance.

        @param contains_measurements: The Measurements that are included in the naming hierarchy where the PSR is the containing object
        """

        self._contains_measurements = []
        if contains_measurements is not None:
            self.contains_measurements = contains_measurements
        else:
            self.contains_measurements = []


        super(PowerSystemResource, self).__init__(*args, **kw_args)
    # >>> power_system_resource

    # <<< contains_measurements
    # @generated
    def get_contains_measurements(self):
        """ The Measurements that are included in the naming hierarchy where the PSR is the containing object
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



class BasicIntervalSchedule(IdentifiedObject):
    """ Schedule of values at points in time.
    """
    # <<< basic_interval_schedule
    # @generated
    def __init__(self, start_time='', value1_unit='w/s', value2_unit='w/s', *args, **kw_args):
        """ Initialises a new 'BasicIntervalSchedule' instance.

        @param start_time: The time for the first time point. 
        @param value1_unit: Value1 units of measure. Values are: "w/s", "none", "s", "h", "j/s", "va", "wh", "ohm", "m3", "hz-1", "w", "min", "rad", "g", "j", "h", "f", "kg/j", "vah", "s-1", "º_c", "deg", "pa", "var", "s", "w/hz", "m", "m2", "hz", "a", "n", "v/var", "varh", "v"
        @param value2_unit: Value2 units of measure. Values are: "w/s", "none", "s", "h", "j/s", "va", "wh", "ohm", "m3", "hz-1", "w", "min", "rad", "g", "j", "h", "f", "kg/j", "vah", "s-1", "º_c", "deg", "pa", "var", "s", "w/hz", "m", "m2", "hz", "a", "n", "v/var", "varh", "v"
        """
        # The time for the first time point. 
        self.start_time = start_time

        # Value1 units of measure. Values are: "w/s", "none", "s", "h", "j/s", "va", "wh", "ohm", "m3", "hz-1", "w", "min", "rad", "g", "j", "h", "f", "kg/j", "vah", "s-1", "º_c", "deg", "pa", "var", "s", "w/hz", "m", "m2", "hz", "a", "n", "v/var", "varh", "v"
        self.value1_unit = value1_unit

        # Value2 units of measure. Values are: "w/s", "none", "s", "h", "j/s", "va", "wh", "ohm", "m3", "hz-1", "w", "min", "rad", "g", "j", "h", "f", "kg/j", "vah", "s-1", "º_c", "deg", "pa", "var", "s", "w/hz", "m", "m2", "hz", "a", "n", "v/var", "varh", "v"
        self.value2_unit = value2_unit



        super(BasicIntervalSchedule, self).__init__(*args, **kw_args)
    # >>> basic_interval_schedule



class GeographicalRegion(IdentifiedObject):
    """ A geographical region of a power system network model.
    """
    # <<< geographical_region
    # @generated
    def __init__(self, regions=None, *args, **kw_args):
        """ Initialises a new 'GeographicalRegion' instance.

        @param regions: The association is used in the naming hierarchy.
        """

        self._regions = []
        if regions is not None:
            self.regions = regions
        else:
            self.regions = []


        super(GeographicalRegion, self).__init__(*args, **kw_args)
    # >>> geographical_region

    # <<< regions
    # @generated
    def get_regions(self):
        """ The association is used in the naming hierarchy.
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



class RegularIntervalSchedule(BasicIntervalSchedule):
    """ The schedule has TimePoints where the time between them is constant.
    """
    # <<< regular_interval_schedule
    # @generated
    def __init__(self, end_time='', time_step=0.0, time_points=None, *args, **kw_args):
        """ Initialises a new 'RegularIntervalSchedule' instance.

        @param end_time: The time for the last time point. 
        @param time_step: The time between each pair of subsequent RegularTimePoints. 
        @param time_points: The point data values that define a curve
        """
        # The time for the last time point. 
        self.end_time = end_time

        # The time between each pair of subsequent RegularTimePoints. 
        self.time_step = time_step


        self._time_points = []
        if time_points is not None:
            self.time_points = time_points
        else:
            self.time_points = []


        super(RegularIntervalSchedule, self).__init__(*args, **kw_args)
    # >>> regular_interval_schedule

    # <<< time_points
    # @generated
    def get_time_points(self):
        """ The point data values that define a curve
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



class ConnectivityNodeContainer(PowerSystemResource):
    """ A base class for all objects that may contain ConnectivityNodes.
    """
    # <<< connectivity_node_container
    # @generated
    def __init__(self, connectivity_nodes=None, *args, **kw_args):
        """ Initialises a new 'ConnectivityNodeContainer' instance.

        @param connectivity_nodes: Connectivity nodes contained by this container.
        """

        self._connectivity_nodes = []
        if connectivity_nodes is not None:
            self.connectivity_nodes = connectivity_nodes
        else:
            self.connectivity_nodes = []


        super(ConnectivityNodeContainer, self).__init__(*args, **kw_args)
    # >>> connectivity_node_container

    # <<< connectivity_nodes
    # @generated
    def get_connectivity_nodes(self):
        """ Connectivity nodes contained by this container.
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



class EquipmentContainer(ConnectivityNodeContainer):
    """ A modeling construct to provide a root class for all Equipment classes
    """
    # <<< equipment_container
    # @generated
    def __init__(self, contains_equipments=None, *args, **kw_args):
        """ Initialises a new 'EquipmentContainer' instance.

        @param contains_equipments: The association is used in the naming hierarchy.
        """

        self._contains_equipments = []
        if contains_equipments is not None:
            self.contains_equipments = contains_equipments
        else:
            self.contains_equipments = []


        super(EquipmentContainer, self).__init__(*args, **kw_args)
    # >>> equipment_container

    # <<< contains_equipments
    # @generated
    def get_contains_equipments(self):
        """ The association is used in the naming hierarchy.
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



class VoltageLevel(EquipmentContainer):
    """ A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.
    """
    # <<< voltage_level
    # @generated
    def __init__(self, low_voltage_limit=0.0, high_voltage_limit=0.0, member_of_substation=None, base_voltage=None, contains_bays=None, *args, **kw_args):
        """ Initialises a new 'VoltageLevel' instance.

        @param low_voltage_limit: The bus bar's low voltage limit 
        @param high_voltage_limit: The bus bar's high voltage limit 
        @param member_of_substation: The association is used in the naming hierarchy.
        @param base_voltage: The base voltage used for all equipment within the VoltageLevel.
        @param contains_bays: The association is used in the naming hierarchy.
        """
        # The bus bar's low voltage limit 
        self.low_voltage_limit = low_voltage_limit

        # The bus bar's high voltage limit 
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


        super(VoltageLevel, self).__init__(*args, **kw_args)
    # >>> voltage_level

    # <<< member_of_substation
    # @generated
    def get_member_of_substation(self):
        """ The association is used in the naming hierarchy.
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
        """ The base voltage used for all equipment within the VoltageLevel.
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
        """ The association is used in the naming hierarchy.
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



class Bay(EquipmentContainer):
    """ A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.
    """
    # <<< bay
    # @generated
    def __init__(self, member_of_voltage_level=None, *args, **kw_args):
        """ Initialises a new 'Bay' instance.

        @param member_of_voltage_level: The association is used in the naming hierarchy.
        """

        self._member_of_voltage_level = None
        self.member_of_voltage_level = member_of_voltage_level


        super(Bay, self).__init__(*args, **kw_args)
    # >>> bay

    # <<< member_of_voltage_level
    # @generated
    def get_member_of_voltage_level(self):
        """ The association is used in the naming hierarchy.
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



class Equipment(PowerSystemResource):
    """ The parts of a power system that are physical devices, electronic or mechanical
    """
    # <<< equipment
    # @generated
    def __init__(self, member_of_equipment_container=None, operational_limit_set=None, *args, **kw_args):
        """ Initialises a new 'Equipment' instance.

        @param member_of_equipment_container: The association is used in the naming hierarchy.
        @param operational_limit_set: The equipment limit sets associated with the equipment.
        """

        self._member_of_equipment_container = None
        self.member_of_equipment_container = member_of_equipment_container

        self._operational_limit_set = []
        if operational_limit_set is not None:
            self.operational_limit_set = operational_limit_set
        else:
            self.operational_limit_set = []


        super(Equipment, self).__init__(*args, **kw_args)
    # >>> equipment

    # <<< member_of_equipment_container
    # @generated
    def get_member_of_equipment_container(self):
        """ The association is used in the naming hierarchy.
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
        """ The equipment limit sets associated with the equipment.
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



class Substation(EquipmentContainer):
    """ A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.
    """
    # <<< substation
    # @generated
    def __init__(self, region=None, contains_voltage_levels=None, *args, **kw_args):
        """ Initialises a new 'Substation' instance.

        @param region: The association is used in the naming hierarchy.
        @param contains_voltage_levels: The association is used in the naming hierarchy.
        """

        self._region = None
        self.region = region

        self._contains_voltage_levels = []
        if contains_voltage_levels is not None:
            self.contains_voltage_levels = contains_voltage_levels
        else:
            self.contains_voltage_levels = []


        super(Substation, self).__init__(*args, **kw_args)
    # >>> substation

    # <<< region
    # @generated
    def get_region(self):
        """ The association is used in the naming hierarchy.
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
        """ The association is used in the naming hierarchy.
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



class ConductingEquipment(Equipment):
    """ The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.
    """
    # <<< conducting_equipment
    # @generated
    def __init__(self, base_voltage=None, terminals=None, *args, **kw_args):
        """ Initialises a new 'ConductingEquipment' instance.

        @param base_voltage: Use association to ConductingEquipment only when there is no VoltageLevel container used.
        @param terminals: ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
        """

        self._base_voltage = None
        self.base_voltage = base_voltage

        self._terminals = []
        if terminals is not None:
            self.terminals = terminals
        else:
            self.terminals = []


        super(ConductingEquipment, self).__init__(*args, **kw_args)
    # >>> conducting_equipment

    # <<< base_voltage
    # @generated
    def get_base_voltage(self):
        """ Use association to ConductingEquipment only when there is no VoltageLevel container used.
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
        """ ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
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



# <<< core
# @generated
# >>> core
