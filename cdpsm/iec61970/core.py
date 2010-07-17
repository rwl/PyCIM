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

""" Contains the core PowerSystemResource and ConductingEquipment entities shared by all applications plus common collections of those entities. Not all applications require all the Core entities.  This package does not depend on any other package except the Domain package, but most of the other packages have associations and generalizations that depend on it.Contains the core PowerSystemResource and ConductingEquipment entities shared by all applications plus common collections of those entities. Not all applications require all the Core entities.  This package does not depend on any other package except the Domain package, but most of the other packages have associations and generalizations that depend on it.
"""

from cdpsm import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Core"

class IdentifiedObject(Element):
    """ This is a root class to provide common naming attributes for all classes needing naming attributesThis is a root class to provide common naming attributes for all classes needing naming attributes
    """
    # <<< identified_object
    # @generated
    def __init__(self, m_rid='', description='', name='', local_name='', alias_name='', **kw_args):
        """ Initialises a new 'IdentifiedObject' instance.
        """
        # A Model Authority issues mRIDs. Given that each Model Authority has a unique id and this id is part of the mRID, then the mRID is globally unique.This attribute is only used when generating XSD Profiles.  For RDF Profiles, the RDF ID is used.A Model Authority issues mRIDs. Given that each Model Authority has a unique id and this id is part of the mRID, then the mRID is globally unique.This attribute is only used when generating XSD Profiles.  For RDF Profiles, the RDF ID is used. 
        self.m_rid = m_rid

        # The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. 
        self.description = description

        # The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy. 
        self.name = name

        # The localName is a human readable name of the object. It is only used with objects organized in a naming hierarchy. The simplest naming hierarchy has just one parent (the root) giving a flat naming hierarchy. However, the naming hierarchy usually has several levels, e.g. Substation, VoltageLevel, Equipment etc. Children of the same parent have names that are unique among them. If the uniqueness requirement cannot be met IdentifiedObject.localName shall not be used, use IdentifiedObject.name  instead.The localName is a human readable name of the object. It is only used with objects organized in a naming hierarchy. The simplest naming hierarchy has just one parent (the root) giving a flat naming hierarchy. However, the naming hierarchy usually has several levels, e.g. Substation, VoltageLevel, Equipment etc. Children of the same parent have names that are unique among them. If the uniqueness requirement cannot be met IdentifiedObject.localName shall not be used, use IdentifiedObject.name  instead. 
        self.local_name = local_name

        # The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy. 
        self.alias_name = alias_name



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

        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
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
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "BaseVoltage")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> base_voltage.serialize


class PSRType(IdentifiedObject):
    """ Classifying instances of the same class, e.g. overhead and underground ACLineSegments. This classification mechanism is intended to provide flexibility outside the scope of this standard, i.e. provide customisation that is non standard.Classifying instances of the same class, e.g. overhead and underground ACLineSegments. This classification mechanism is intended to provide flexibility outside the scope of this standard, i.e. provide customisation that is non standard.
    """
    # <<< psrtype
    # @generated
    def __init__(self, power_system_resources=None, **kw_args):
        """ Initialises a new 'PSRType' instance.
        """

        self._power_system_resources = []
        if power_system_resources is not None:
            self.power_system_resources = power_system_resources
        else:
            self.power_system_resources = []


        super(PSRType, self).__init__(**kw_args)
    # >>> psrtype

    # <<< power_system_resources
    # @generated
    def get_power_system_resources(self):
        """ Power system resources classified with this PSRType.Power system resources classified with this PSRType.
        """
        return self._power_system_resources

    def set_power_system_resources(self, value):
        for x in self._power_system_resources:
            x._psrtype = None
        for y in value:
            y._psrtype = self
        self._power_system_resources = value

    power_system_resources = property(get_power_system_resources, set_power_system_resources)

    def add_power_system_resources(self, *power_system_resources):
        for obj in power_system_resources:
            obj._psrtype = self
            self._power_system_resources.append(obj)

    def remove_power_system_resources(self, *power_system_resources):
        for obj in power_system_resources:
            obj._psrtype = None
            self._power_system_resources.remove(obj)
    # >>> power_system_resources


    def __str__(self):
        """ Returns a string representation of the PSRType.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< psrtype.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PSRType.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PSRType", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.power_system_resources:
            s += '%s<%s:PSRType.power_system_resources rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PSRType")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> psrtype.serialize


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
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SubGeographicalRegion")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> sub_geographical_region.serialize


class Terminal(IdentifiedObject):
    """ An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.
    """
    # <<< terminal
    # @generated
    def __init__(self, sequence_number=0, connected=False, conducting_equipment=None, connectivity_node=None, **kw_args):
        """ Initialises a new 'Terminal' instance.
        """
        # The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1. 
        self.sequence_number = sequence_number

        # The terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithmThe terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithm 
        self.connected = connected


        self._conducting_equipment = None
        self.conducting_equipment = conducting_equipment

        self._connectivity_node = None
        self.connectivity_node = connectivity_node


        super(Terminal, self).__init__(**kw_args)
    # >>> terminal

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

        if self.conducting_equipment is not None:
            s += '%s<%s:Terminal.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
        if self.connectivity_node is not None:
            s += '%s<%s:Terminal.connectivity_node rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.connectivity_node.uri)
        s += '%s<%s:Terminal.sequence_number>%s</%s:Terminal.sequence_number>' % \
            (indent, ns_prefix, self.sequence_number, ns_prefix)
        s += '%s<%s:Terminal.connected>%s</%s:Terminal.connected>' % \
            (indent, ns_prefix, self.connected, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Terminal")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> terminal.serialize


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
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GeographicalRegion")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> geographical_region.serialize


class PowerSystemResource(IdentifiedObject):
    """ A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.
    """
    # <<< power_system_resource
    # @generated
    def __init__(self, geo_location=None, psrtype=None, **kw_args):
        """ Initialises a new 'PowerSystemResource' instance.
        """

        self._geo_location = None
        self.geo_location = geo_location

        self._psrtype = None
        self.psrtype = psrtype


        super(PowerSystemResource, self).__init__(**kw_args)
    # >>> power_system_resource

    # <<< geo_location
    # @generated
    def get_geo_location(self):
        """ Geographical location of this power system resource.Geographical location of this power system resource.
        """
        return self._geo_location

    def set_geo_location(self, value):
        if self._geo_location is not None:
            filtered = [x for x in self.geo_location.power_system_resources if x != self]
            self._geo_location._power_system_resources = filtered

        self._geo_location = value
        if self._geo_location is not None:
            self._geo_location._power_system_resources.append(self)

    geo_location = property(get_geo_location, set_geo_location)
    # >>> geo_location

    # <<< psrtype
    # @generated
    def get_psrtype(self):
        """ PSRType (custom classification) for this PowerSystemResource.PSRType (custom classification) for this PowerSystemResource.
        """
        return self._psrtype

    def set_psrtype(self, value):
        if self._psrtype is not None:
            filtered = [x for x in self.psrtype.power_system_resources if x != self]
            self._psrtype._power_system_resources = filtered

        self._psrtype = value
        if self._psrtype is not None:
            self._psrtype._power_system_resources.append(self)

    psrtype = property(get_psrtype, set_psrtype)
    # >>> psrtype


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

        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PowerSystemResource")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> power_system_resource.serialize


class ConnectivityNodeContainer(PowerSystemResource):
    """ A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.
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
            x._connectivity_node_container = None
        for y in value:
            y._connectivity_node_container = self
        self._connectivity_nodes = value

    connectivity_nodes = property(get_connectivity_nodes, set_connectivity_nodes)

    def add_connectivity_nodes(self, *connectivity_nodes):
        for obj in connectivity_nodes:
            obj._connectivity_node_container = self
            self._connectivity_nodes.append(obj)

    def remove_connectivity_nodes(self, *connectivity_nodes):
        for obj in connectivity_nodes:
            obj._connectivity_node_container = None
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
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ConnectivityNodeContainer")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> connectivity_node_container.serialize


class Equipment(PowerSystemResource):
    """ The parts of a power system that are physical devices, electronic or mechanicalThe parts of a power system that are physical devices, electronic or mechanical
    """
    # <<< equipment
    # @generated
    def __init__(self, norma_ily_in_service=False, equipment_container=None, **kw_args):
        """ Initialises a new 'Equipment' instance.
        """
        # The equipment is normally in service.The equipment is normally in service. 
        self.norma_ily_in_service = norma_ily_in_service


        self._equipment_container = None
        self.equipment_container = equipment_container


        super(Equipment, self).__init__(**kw_args)
    # >>> equipment

    # <<< equipment_container
    # @generated
    def get_equipment_container(self):
        """ The association is used in the naming hierarchy.The association is used in the naming hierarchy.
        """
        return self._equipment_container

    def set_equipment_container(self, value):
        if self._equipment_container is not None:
            filtered = [x for x in self.equipment_container.equipments if x != self]
            self._equipment_container._equipments = filtered

        self._equipment_container = value
        if self._equipment_container is not None:
            self._equipment_container._equipments.append(self)

    equipment_container = property(get_equipment_container, set_equipment_container)
    # >>> equipment_container


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

        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Equipment")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> equipment.serialize


class EquipmentContainer(ConnectivityNodeContainer):
    """ A modeling construct to provide a root class for all Equipment classesA modeling construct to provide a root class for all Equipment classes
    """
    # <<< equipment_container
    # @generated
    def __init__(self, equipments=None, **kw_args):
        """ Initialises a new 'EquipmentContainer' instance.
        """

        self._equipments = []
        if equipments is not None:
            self.equipments = equipments
        else:
            self.equipments = []


        super(EquipmentContainer, self).__init__(**kw_args)
    # >>> equipment_container

    # <<< equipments
    # @generated
    def get_equipments(self):
        """ The association is used in the naming hierarchy.The association is used in the naming hierarchy.
        """
        return self._equipments

    def set_equipments(self, value):
        for x in self._equipments:
            x._equipment_container = None
        for y in value:
            y._equipment_container = self
        self._equipments = value

    equipments = property(get_equipments, set_equipments)

    def add_equipments(self, *equipments):
        for obj in equipments:
            obj._equipment_container = self
            self._equipments.append(obj)

    def remove_equipments(self, *equipments):
        for obj in equipments:
            obj._equipment_container = None
            self._equipments.remove(obj)
    # >>> equipments


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

        for obj in self.equipments:
            s += '%s<%s:EquipmentContainer.equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
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


class Substation(EquipmentContainer):
    """ A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.
    """
    # <<< substation
    # @generated
    def __init__(self, region=None, voltage_levels=None, **kw_args):
        """ Initialises a new 'Substation' instance.
        """

        self._region = None
        self.region = region

        self._voltage_levels = []
        if voltage_levels is not None:
            self.voltage_levels = voltage_levels
        else:
            self.voltage_levels = []


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

    # <<< voltage_levels
    # @generated
    def get_voltage_levels(self):
        """ The association is used in the naming hierarchy.The association is used in the naming hierarchy.
        """
        return self._voltage_levels

    def set_voltage_levels(self, value):
        for x in self._voltage_levels:
            x._substation = None
        for y in value:
            y._substation = self
        self._voltage_levels = value

    voltage_levels = property(get_voltage_levels, set_voltage_levels)

    def add_voltage_levels(self, *voltage_levels):
        for obj in voltage_levels:
            obj._substation = self
            self._voltage_levels.append(obj)

    def remove_voltage_levels(self, *voltage_levels):
        for obj in voltage_levels:
            obj._substation = None
            self._voltage_levels.remove(obj)
    # >>> voltage_levels


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
        for obj in self.voltage_levels:
            s += '%s<%s:Substation.voltage_levels rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.connectivity_nodes:
            s += '%s<%s:ConnectivityNodeContainer.connectivity_nodes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.equipments:
            s += '%s<%s:EquipmentContainer.equipments rdf:resource="#%s"/>' % \
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
    def __init__(self, phases='abc', terminals=None, base_voltage=None, **kw_args):
        """ Initialises a new 'ConductingEquipment' instance.
        """
        # Describes the phases carried by a conducting equipment.Describes the phases carried by a conducting equipment. Values are: "abc", "split_secondary2_n", "abn", "cn", "acn", "bc", "an", "bn", "ab", "split_secondary1_n", "n", "c", "ac", "abcn", "split_secondary12_n", "a", "b", "bcn"
        self.phases = 'abc'


        self._terminals = []
        if terminals is not None:
            self.terminals = terminals
        else:
            self.terminals = []

        self._base_voltage = None
        self.base_voltage = base_voltage


        super(ConductingEquipment, self).__init__(**kw_args)
    # >>> conducting_equipment

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

        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        s += '%s<%s:ConductingEquipment.phases>%s</%s:ConductingEquipment.phases>' % \
            (indent, ns_prefix, self.phases, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ConductingEquipment")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> conducting_equipment.serialize


class VoltageLevel(EquipmentContainer):
    """ A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.
    """
    # <<< voltage_level
    # @generated
    def __init__(self, low_voltage_limit=0.0, high_voltage_limit=0.0, base_voltage=None, bays=None, substation=None, **kw_args):
        """ Initialises a new 'VoltageLevel' instance.
        """
        # The bus bar's low voltage limitThe bus bar's low voltage limit 
        self.low_voltage_limit = low_voltage_limit

        # The bus bar's high voltage limitThe bus bar's high voltage limit 
        self.high_voltage_limit = high_voltage_limit


        self._base_voltage = None
        self.base_voltage = base_voltage

        self._bays = []
        if bays is not None:
            self.bays = bays
        else:
            self.bays = []

        self._substation = None
        self.substation = substation


        super(VoltageLevel, self).__init__(**kw_args)
    # >>> voltage_level

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

    # <<< bays
    # @generated
    def get_bays(self):
        """ The association is used in the naming hierarchy.The association is used in the naming hierarchy.
        """
        return self._bays

    def set_bays(self, value):
        for x in self._bays:
            x._voltage_level = None
        for y in value:
            y._voltage_level = self
        self._bays = value

    bays = property(get_bays, set_bays)

    def add_bays(self, *bays):
        for obj in bays:
            obj._voltage_level = self
            self._bays.append(obj)

    def remove_bays(self, *bays):
        for obj in bays:
            obj._voltage_level = None
            self._bays.remove(obj)
    # >>> bays

    # <<< substation
    # @generated
    def get_substation(self):
        """ The association is used in the naming hierarchy.The association is used in the naming hierarchy.
        """
        return self._substation

    def set_substation(self, value):
        if self._substation is not None:
            filtered = [x for x in self.substation.voltage_levels if x != self]
            self._substation._voltage_levels = filtered

        self._substation = value
        if self._substation is not None:
            self._substation._voltage_levels.append(self)

    substation = property(get_substation, set_substation)
    # >>> substation


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

        if self.base_voltage is not None:
            s += '%s<%s:VoltageLevel.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        for obj in self.bays:
            s += '%s<%s:VoltageLevel.bays rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.substation is not None:
            s += '%s<%s:VoltageLevel.substation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.substation.uri)
        s += '%s<%s:VoltageLevel.low_voltage_limit>%s</%s:VoltageLevel.low_voltage_limit>' % \
            (indent, ns_prefix, self.low_voltage_limit, ns_prefix)
        s += '%s<%s:VoltageLevel.high_voltage_limit>%s</%s:VoltageLevel.high_voltage_limit>' % \
            (indent, ns_prefix, self.high_voltage_limit, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.connectivity_nodes:
            s += '%s<%s:ConnectivityNodeContainer.connectivity_nodes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.equipments:
            s += '%s<%s:EquipmentContainer.equipments rdf:resource="#%s"/>' % \
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
    def __init__(self, voltage_level=None, **kw_args):
        """ Initialises a new 'Bay' instance.
        """

        self._voltage_level = None
        self.voltage_level = voltage_level


        super(Bay, self).__init__(**kw_args)
    # >>> bay

    # <<< voltage_level
    # @generated
    def get_voltage_level(self):
        """ The association is used in the naming hierarchy.The association is used in the naming hierarchy.
        """
        return self._voltage_level

    def set_voltage_level(self, value):
        if self._voltage_level is not None:
            filtered = [x for x in self.voltage_level.bays if x != self]
            self._voltage_level._bays = filtered

        self._voltage_level = value
        if self._voltage_level is not None:
            self._voltage_level._bays.append(self)

    voltage_level = property(get_voltage_level, set_voltage_level)
    # >>> voltage_level


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

        if self.voltage_level is not None:
            s += '%s<%s:Bay.voltage_level rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.voltage_level.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.connectivity_nodes:
            s += '%s<%s:ConnectivityNodeContainer.connectivity_nodes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.equipments:
            s += '%s<%s:EquipmentContainer.equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Bay")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> bay.serialize


# <<< core
# @generated
# >>> core
