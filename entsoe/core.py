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

""" Contains the core PowerSystemResource and ConductingEquipment entities shared by all applications plus common collections of those entities. Not all applications require all the Core entities.  This package does not depend on any other package except the Domain package, but most of the other packages have associations and generalizations that depend on it.
"""

from entsoe import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Core"

class IdentifiedObject(Element):
    """ This is a root class to provide common naming attributes for all classes needing naming attributes
    """
    # <<< identified_object
    # @generated
    def __init__(self, description='', name='', alias_name='', *args, **kw_args):
        """ Initialises a new 'IdentifiedObject' instance.

        @param description: The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. 
        @param name: The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.This attribute is required on all instances in this Profile that inherit from IdentifiedObject except for the following Classes: 1) BaseVoltage; 2) Terminal; 3) TransformerWinding; 4) RatioTapChanger; 5) PhaseTapChanger; 6) OperationalLImitSet; 7) CurrentLimit; and, 8) VoltageLimit. 
        @param alias_name: The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.In the UCTE profile the aliasName is used to hold the EIC code.    The code length is 16 characters.    Not all CIM classes have an EIC code so the attribute is optional.    
        """
        # The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. 
        self.description = description

        # The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.This attribute is required on all instances in this Profile that inherit from IdentifiedObject except for the following Classes: 1) BaseVoltage; 2) Terminal; 3) TransformerWinding; 4) RatioTapChanger; 5) PhaseTapChanger; 6) OperationalLImitSet; 7) CurrentLimit; and, 8) VoltageLimit. 
        self.name = name

        # The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.In the UCTE profile the aliasName is used to hold the EIC code.    The code length is 16 characters.    Not all CIM classes have an EIC code so the attribute is optional.    
        self.alias_name = alias_name



        super(IdentifiedObject, self).__init__(*args, **kw_args)
    # >>> identified_object



class CurveData(Element):
    """ Data point values for defining a curve or schedule
    """
    # <<< curve_data
    # @generated
    def __init__(self, y1value=0.0, xvalue=0.0, y2value=0.0, curve_schedule=None, *args, **kw_args):
        """ Initialises a new 'CurveData' instance.

        @param y1value: The data value of the  first Y-axis variable, depending on the Y-axis units 
        @param xvalue: The data value of the X-axis variable,  depending on the X-axis units 
        @param y2value: The data value of the second Y-axis variable (if present), depending on the Y-axis units 
        @param curve_schedule: The Curve defined by this CurveData.
        """
        # The data value of the  first Y-axis variable, depending on the Y-axis units 
        self.y1value = y1value

        # The data value of the X-axis variable,  depending on the X-axis units 
        self.xvalue = xvalue

        # The data value of the second Y-axis variable (if present), depending on the Y-axis units 
        self.y2value = y2value


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



class Curve(IdentifiedObject):
    """ Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.
    """
    # <<< curve
    # @generated
    def __init__(self, curve_schedule_datas=None, *args, **kw_args):
        """ Initialises a new 'Curve' instance.

        @param curve_schedule_datas: The point data values that define a curve
        """

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



class ConnectivityNodeContainer(IdentifiedObject):
    """ A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.The TopologicalNode will normally belong only to a VoltageLevel instance within a Substation.   All instances of TopologicalNode that are not X-nodes will require an association to a containing VoltageLevel instance.  The BaseVoltage of the VoltageLevel should match that of the TopologicalNode itself. A TopologicalNode object used for an X-node will not be contained, thus this association is specified as optional in the profile. The TopologicalNode will normally belong only to a VoltageLevel within a Substation. In the case of X-nodes, the TopologicalNode is not contained.    
    """
    # <<< connectivity_node_container
    # @generated
    def __init__(self, topological_node=None, *args, **kw_args):
        """ Initialises a new 'ConnectivityNodeContainer' instance.

        @param topological_node: The topological nodes which belong to this connectivity node container.
        """

        self._topological_node = []
        if topological_node is not None:
            self.topological_node = topological_node
        else:
            self.topological_node = []


        super(ConnectivityNodeContainer, self).__init__(*args, **kw_args)
    # >>> connectivity_node_container

    # <<< topological_node
    # @generated
    def get_topological_node(self):
        """ The topological nodes which belong to this connectivity node container.
        """
        return self._topological_node

    def set_topological_node(self, value):
        for x in self._topological_node:
            x._connectivity_node_container = None
        for y in value:
            y._connectivity_node_container = self
        self._topological_node = value

    topological_node = property(get_topological_node, set_topological_node)

    def add_topological_node(self, *topological_node):
        for obj in topological_node:
            obj._connectivity_node_container = self
            self._topological_node.append(obj)

    def remove_topological_node(self, *topological_node):
        for obj in topological_node:
            obj._connectivity_node_container = None
            self._topological_node.remove(obj)
    # >>> topological_node



class Equipment(IdentifiedObject):
    """ The parts of a power system that are physical devices, electronic or mechanical
    """
    # <<< equipment
    # @generated
    def __init__(self, equivalent=False, member_of_equipment_container=None, *args, **kw_args):
        """ Initialises a new 'Equipment' instance.

        @param equivalent: Indicates if the equipment is real equipment (false) or an equivalent.If this is missing, it is assumed to be False.  It is required for Equipment connected to the X-Node. All classes derived from Equipment are to include this attribute except for the TransformerWinding class.     For transformers the PowerTransformer class will be used to specify the real or equivalent status and the contained TransformerWinding class instances need not and should not specify this attribute. 
        @param member_of_equipment_container: The association is used in the naming hierarchy.For a TransformerWinding and ACLineSegment, the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer association. 
        """
        # Indicates if the equipment is real equipment (false) or an equivalent.If this is missing, it is assumed to be False.  It is required for Equipment connected to the X-Node. All classes derived from Equipment are to include this attribute except for the TransformerWinding class.     For transformers the PowerTransformer class will be used to specify the real or equivalent status and the contained TransformerWinding class instances need not and should not specify this attribute. 
        self.equivalent = equivalent


        self._member_of_equipment_container = None
        self.member_of_equipment_container = member_of_equipment_container


        super(Equipment, self).__init__(*args, **kw_args)
    # >>> equipment

    # <<< member_of_equipment_container
    # @generated
    def get_member_of_equipment_container(self):
        """ The association is used in the naming hierarchy.For a TransformerWinding and ACLineSegment, the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer association. 
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



class BaseVoltage(IdentifiedObject):
    """ Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.The profile requires a BaseVoltage associaton on ConductingEquipment subtypes of classes ACLineSegment and TransformerWinding. The association is not used for any other subtypes. The base voltage of the TopologicalNode should match the BaseVoltage of the containing VoltageLevel if such a containing VoltageLevel is specified.
    """
    # <<< base_voltage
    # @generated
    def __init__(self, nominal_voltage=0.0, is_dc=False, conducting_equipment=None, voltage_level=None, topological_node=None, *args, **kw_args):
        """ Initialises a new 'BaseVoltage' instance.

        @param nominal_voltage: The PowerSystemResource's base voltage. 
        @param is_dc: If true, this is a direct current base voltage and items assigned to this base voltage are also associated with a direct current capabilities.   False indicates alternating current. 
        @param conducting_equipment: Use association to ConductingEquipment only when there is no VoltageLevel container used.
        @param voltage_level: The VoltageLevels having this BaseVoltage.
        @param topological_node: The topological nodes at the base voltage.
        """
        # The PowerSystemResource's base voltage. 
        self.nominal_voltage = nominal_voltage

        # If true, this is a direct current base voltage and items assigned to this base voltage are also associated with a direct current capabilities.   False indicates alternating current. 
        self.is_dc = is_dc


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

        self._topological_node = []
        if topological_node is not None:
            self.topological_node = topological_node
        else:
            self.topological_node = []


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

    # <<< topological_node
    # @generated
    def get_topological_node(self):
        """ The topological nodes at the base voltage.
        """
        return self._topological_node

    def set_topological_node(self, value):
        for x in self._topological_node:
            x._base_voltage = None
        for y in value:
            y._base_voltage = self
        self._topological_node = value

    topological_node = property(get_topological_node, set_topological_node)

    def add_topological_node(self, *topological_node):
        for obj in topological_node:
            obj._base_voltage = self
            self._topological_node.append(obj)

    def remove_topological_node(self, *topological_node):
        for obj in topological_node:
            obj._base_voltage = None
            self._topological_node.remove(obj)
    # >>> topological_node



class EquipmentContainer(ConnectivityNodeContainer):
    """ A modeling construct to provide a root class for all Equipment classesFor a TransformerWinding the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer Association. For a TransformerWinding and ACLineSegment, the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer association. 
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



class Substation(EquipmentContainer):
    """ A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.
    """
    # <<< substation
    # @generated
    def __init__(self, contains_voltage_levels=None, region=None, *args, **kw_args):
        """ Initialises a new 'Substation' instance.

        @param contains_voltage_levels: The association is used in the naming hierarchy.
        @param region: The association is used in the naming hierarchy.
        """

        self._contains_voltage_levels = []
        if contains_voltage_levels is not None:
            self.contains_voltage_levels = contains_voltage_levels
        else:
            self.contains_voltage_levels = []

        self._region = None
        self.region = region


        super(Substation, self).__init__(*args, **kw_args)
    # >>> substation

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



class ConductingEquipment(Equipment):
    """ The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.
    """
    # <<< conducting_equipment
    # @generated
    def __init__(self, base_voltage=None, terminals=None, *args, **kw_args):
        """ Initialises a new 'ConductingEquipment' instance.

        @param base_voltage: Use association to ConductingEquipment only when there is no VoltageLevel container used.The profile requires a BaseVoltage associaton on ConductingEquipment subtypes of classes ACLineSegment and TransformerWinding. The association is not used for any other subtypes.
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
        """ Use association to ConductingEquipment only when there is no VoltageLevel container used.The profile requires a BaseVoltage associaton on ConductingEquipment subtypes of classes ACLineSegment and TransformerWinding. The association is not used for any other subtypes.
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



class SubGeographicalRegion(IdentifiedObject):
    """ A subset of a geographical region of a power system network model.
    """
    # <<< sub_geographical_region
    # @generated
    def __init__(self, substations=None, region=None, *args, **kw_args):
        """ Initialises a new 'SubGeographicalRegion' instance.

        @param substations: The association is used in the naming hierarchy.
        @param region: The association is used in the naming hierarchy.
        """

        self._substations = []
        if substations is not None:
            self.substations = substations
        else:
            self.substations = []

        self._region = None
        self.region = region


        super(SubGeographicalRegion, self).__init__(*args, **kw_args)
    # >>> sub_geographical_region

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



class Terminal(IdentifiedObject):
    """ An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.The SvPowerFlow is only associated with the Terminal objects of shunt injection classes such as EnergyConsumer and SynchronousMachine.   The flows at any ShuntCompensator can always be computed from connected voltage magnitude, number of sections and local attributes.  Branch flows are not exchanged since they can be readily be computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  For UCTE profile, the terminal associated with the limit is always required, and thus there is no need to exchange the associated Equipment which can always be derived from the terminal. The SvPowerFlow is only associated with the Terminal objects of shunt injection classes EnergyConsumer and  SynchronousMachine.  Branch flows are not exchanged since they can be readily computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  Similarly, Switch flows are not included because they can typically be uniquely computed, except in the case of meshed networks of Switch objects.  Terminals of the ShuntCompensator class are not associated because the injection value can be computed from the solved voltage, number of sections, Termianl.connected state, and the impedance per section attributes on the ShuntCompensator. 
    """
    # <<< terminal
    # @generated
    def __init__(self, sequence_number=0, connected=False, has_first_mutual_coupling=None, operational_limit_set=None, sv_power_flow=None, regulating_control=None, tie_flow=None, conducting_equipment=None, topological_node=None, has_second_mutual_coupling=None, *args, **kw_args):
        """ Initialises a new 'Terminal' instance.

        @param sequence_number: The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.For UCTE profile, the terminal sequence number is not required.   And, when used, follows the UML description. The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1. 
        @param connected: The terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithm for topological analysis is implied. 
        @param has_first_mutual_coupling: Mutual couplings associated with the branch as the first branch.
        @param operational_limit_set: The operatinal limits sets that applie specifically to this terminal.  Other operational limits sets may apply to this terminal through the association to Equipment.
        @param sv_power_flow: The power flow state associated with the terminal.
        @param regulating_control: The terminal is regulated by a control.
        @param tie_flow: The control area tie flows to which this terminal associates.
        @param conducting_equipment: ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
        @param topological_node: The topological node associated with the terminal.   This can be used as an alternative to the connectivity node path to topological node, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.
        @param has_second_mutual_coupling: Mutual couplings with the branch associated as the first branch.
        """
        # The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.For UCTE profile, the terminal sequence number is not required.   And, when used, follows the UML description. The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1. 
        self.sequence_number = sequence_number

        # The terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithm for topological analysis is implied. 
        self.connected = connected


        self._has_first_mutual_coupling = []
        if has_first_mutual_coupling is not None:
            self.has_first_mutual_coupling = has_first_mutual_coupling
        else:
            self.has_first_mutual_coupling = []

        self._operational_limit_set = []
        if operational_limit_set is not None:
            self.operational_limit_set = operational_limit_set
        else:
            self.operational_limit_set = []

        self._sv_power_flow = None
        self.sv_power_flow = sv_power_flow

        self._regulating_control = []
        if regulating_control is not None:
            self.regulating_control = regulating_control
        else:
            self.regulating_control = []

        self._tie_flow = []
        if tie_flow is not None:
            self.tie_flow = tie_flow
        else:
            self.tie_flow = []

        self._conducting_equipment = None
        self.conducting_equipment = conducting_equipment

        self._topological_node = None
        self.topological_node = topological_node

        self._has_second_mutual_coupling = []
        if has_second_mutual_coupling is not None:
            self.has_second_mutual_coupling = has_second_mutual_coupling
        else:
            self.has_second_mutual_coupling = []


        super(Terminal, self).__init__(*args, **kw_args)
    # >>> terminal

    # <<< has_first_mutual_coupling
    # @generated
    def get_has_first_mutual_coupling(self):
        """ Mutual couplings associated with the branch as the first branch.
        """
        return self._has_first_mutual_coupling

    def set_has_first_mutual_coupling(self, value):
        for x in self._has_first_mutual_coupling:
            x._first_terminal = None
        for y in value:
            y._first_terminal = self
        self._has_first_mutual_coupling = value

    has_first_mutual_coupling = property(get_has_first_mutual_coupling, set_has_first_mutual_coupling)

    def add_has_first_mutual_coupling(self, *has_first_mutual_coupling):
        for obj in has_first_mutual_coupling:
            obj._first_terminal = self
            self._has_first_mutual_coupling.append(obj)

    def remove_has_first_mutual_coupling(self, *has_first_mutual_coupling):
        for obj in has_first_mutual_coupling:
            obj._first_terminal = None
            self._has_first_mutual_coupling.remove(obj)
    # >>> has_first_mutual_coupling

    # <<< operational_limit_set
    # @generated
    def get_operational_limit_set(self):
        """ The operatinal limits sets that applie specifically to this terminal.  Other operational limits sets may apply to this terminal through the association to Equipment.
        """
        return self._operational_limit_set

    def set_operational_limit_set(self, value):
        for x in self._operational_limit_set:
            x._terminal = None
        for y in value:
            y._terminal = self
        self._operational_limit_set = value

    operational_limit_set = property(get_operational_limit_set, set_operational_limit_set)

    def add_operational_limit_set(self, *operational_limit_set):
        for obj in operational_limit_set:
            obj._terminal = self
            self._operational_limit_set.append(obj)

    def remove_operational_limit_set(self, *operational_limit_set):
        for obj in operational_limit_set:
            obj._terminal = None
            self._operational_limit_set.remove(obj)
    # >>> operational_limit_set

    # <<< sv_power_flow
    # @generated
    def get_sv_power_flow(self):
        """ The power flow state associated with the terminal.
        """
        return self._sv_power_flow

    def set_sv_power_flow(self, value):
        if self._sv_power_flow is not None:
            self._sv_power_flow._terminal = None

        self._sv_power_flow = value
        if self._sv_power_flow is not None:
            self._sv_power_flow._terminal = self

    sv_power_flow = property(get_sv_power_flow, set_sv_power_flow)
    # >>> sv_power_flow

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

    # <<< tie_flow
    # @generated
    def get_tie_flow(self):
        """ The control area tie flows to which this terminal associates.
        """
        return self._tie_flow

    def set_tie_flow(self, value):
        for x in self._tie_flow:
            x._terminal = None
        for y in value:
            y._terminal = self
        self._tie_flow = value

    tie_flow = property(get_tie_flow, set_tie_flow)

    def add_tie_flow(self, *tie_flow):
        for obj in tie_flow:
            obj._terminal = self
            self._tie_flow.append(obj)

    def remove_tie_flow(self, *tie_flow):
        for obj in tie_flow:
            obj._terminal = None
            self._tie_flow.remove(obj)
    # >>> tie_flow

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

    # <<< topological_node
    # @generated
    def get_topological_node(self):
        """ The topological node associated with the terminal.   This can be used as an alternative to the connectivity node path to topological node, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.
        """
        return self._topological_node

    def set_topological_node(self, value):
        if self._topological_node is not None:
            filtered = [x for x in self.topological_node.terminal if x != self]
            self._topological_node._terminal = filtered

        self._topological_node = value
        if self._topological_node is not None:
            self._topological_node._terminal.append(self)

    topological_node = property(get_topological_node, set_topological_node)
    # >>> topological_node

    # <<< has_second_mutual_coupling
    # @generated
    def get_has_second_mutual_coupling(self):
        """ Mutual couplings with the branch associated as the first branch.
        """
        return self._has_second_mutual_coupling

    def set_has_second_mutual_coupling(self, value):
        for x in self._has_second_mutual_coupling:
            x._second_terminal = None
        for y in value:
            y._second_terminal = self
        self._has_second_mutual_coupling = value

    has_second_mutual_coupling = property(get_has_second_mutual_coupling, set_has_second_mutual_coupling)

    def add_has_second_mutual_coupling(self, *has_second_mutual_coupling):
        for obj in has_second_mutual_coupling:
            obj._second_terminal = self
            self._has_second_mutual_coupling.append(obj)

    def remove_has_second_mutual_coupling(self, *has_second_mutual_coupling):
        for obj in has_second_mutual_coupling:
            obj._second_terminal = None
            self._has_second_mutual_coupling.remove(obj)
    # >>> has_second_mutual_coupling



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



class VoltageLevel(EquipmentContainer):
    """ A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.
    """
    # <<< voltage_level
    # @generated
    def __init__(self, base_voltage=None, member_of_substation=None, *args, **kw_args):
        """ Initialises a new 'VoltageLevel' instance.

        @param base_voltage: The base voltage used for all equipment within the VoltageLevel.
        @param member_of_substation: The association is used in the naming hierarchy.
        """

        self._base_voltage = None
        self.base_voltage = base_voltage

        self._member_of_substation = None
        self.member_of_substation = member_of_substation


        super(VoltageLevel, self).__init__(*args, **kw_args)
    # >>> voltage_level

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



# <<< core
# @generated
# >>> core
