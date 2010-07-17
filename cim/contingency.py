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

""" Contingencies to be studied.
"""

from cim.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimContingency"

ns_uri = "http://iec.ch/TC57/CIM-generic#Contingency"

class ContingencyElement(IdentifiedObject):
    """ An element of a system event to be studied by contingency analysis, representing a change in status of a single piece of equipment.
    """
    # <<< contingency_element
    # @generated
    def __init__(self, contingency=None, **kw_args):
        """ Initialises a new 'ContingencyElement' instance.
        """

        self._contingency = None
        self.contingency = contingency


        super(ContingencyElement, self).__init__(**kw_args)
    # >>> contingency_element

    # <<< contingency
    # @generated
    def get_contingency(self):
        """ A contingency element belongs to one contingency.
        """
        return self._contingency

    def set_contingency(self, value):
        if self._contingency is not None:
            filtered = [x for x in self.contingency.contingency_element if x != self]
            self._contingency._contingency_element = filtered

        self._contingency = value
        if self._contingency is not None:
            self._contingency._contingency_element.append(self)

    contingency = property(get_contingency, set_contingency)
    # >>> contingency


    def __str__(self):
        """ Returns a string representation of the ContingencyElement.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< contingency_element.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ContingencyElement.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ContingencyElement", self.uri)
        if format:
            indent += ' ' * depth

        if self.contingency is not None:
            s += '%s<%s:ContingencyElement.contingency rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.contingency.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ContingencyElement")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> contingency_element.serialize


class Contingency(IdentifiedObject):
    """ An event threatening system reliability, consisting of one or more contingency elements.
    """
    # <<< contingency
    # @generated
    def __init__(self, must_study=False, contingency_element=None, **kw_args):
        """ Initialises a new 'Contingency' instance.
        """
        # Set true if must study this contingency. 
        self.must_study = must_study


        self._contingency_element = []
        if contingency_element is not None:
            self.contingency_element = contingency_element
        else:
            self.contingency_element = []


        super(Contingency, self).__init__(**kw_args)
    # >>> contingency

    # <<< contingency_element
    # @generated
    def get_contingency_element(self):
        """ A contingency can have any number of contingency elements.
        """
        return self._contingency_element

    def set_contingency_element(self, value):
        for x in self._contingency_element:
            x._contingency = None
        for y in value:
            y._contingency = self
        self._contingency_element = value

    contingency_element = property(get_contingency_element, set_contingency_element)

    def add_contingency_element(self, *contingency_element):
        for obj in contingency_element:
            obj._contingency = self
            self._contingency_element.append(obj)

    def remove_contingency_element(self, *contingency_element):
        for obj in contingency_element:
            obj._contingency = None
            self._contingency_element.remove(obj)
    # >>> contingency_element


    def __str__(self):
        """ Returns a string representation of the Contingency.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< contingency.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Contingency.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Contingency", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.contingency_element:
            s += '%s<%s:Contingency.contingency_element rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Contingency.must_study>%s</%s:Contingency.must_study>' % \
            (indent, ns_prefix, self.must_study, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Contingency")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> contingency.serialize


class ContingencyEquipment(ContingencyElement):
    """ A equipment to which the in service status is to change such as a power transformer or AC line segment.
    """
    # <<< contingency_equipment
    # @generated
    def __init__(self, contingent_status='out_of_service', equipment=None, **kw_args):
        """ Initialises a new 'ContingencyEquipment' instance.
        """
        # The status for the associated equipment when in the contingency state.   This status is independent of the case to which the contingency is originally applied, but defines the equipment status when the contingency is applied. Values are: "out_of_service", "in_service"
        self.contingent_status = 'out_of_service'


        self._equipment = None
        self.equipment = equipment


        super(ContingencyEquipment, self).__init__(**kw_args)
    # >>> contingency_equipment

    # <<< equipment
    # @generated
    def get_equipment(self):
        """ The single piece of equipment to which to apply the contingency.
        """
        return self._equipment

    def set_equipment(self, value):
        if self._equipment is not None:
            filtered = [x for x in self.equipment.contingency_equipment if x != self]
            self._equipment._contingency_equipment = filtered

        self._equipment = value
        if self._equipment is not None:
            self._equipment._contingency_equipment.append(self)

    equipment = property(get_equipment, set_equipment)
    # >>> equipment


    def __str__(self):
        """ Returns a string representation of the ContingencyEquipment.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< contingency_equipment.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ContingencyEquipment.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ContingencyEquipment", self.uri)
        if format:
            indent += ' ' * depth

        if self.equipment is not None:
            s += '%s<%s:ContingencyEquipment.equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment.uri)
        s += '%s<%s:ContingencyEquipment.contingent_status>%s</%s:ContingencyEquipment.contingent_status>' % \
            (indent, ns_prefix, self.contingent_status, ns_prefix)
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
        if self.contingency is not None:
            s += '%s<%s:ContingencyElement.contingency rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.contingency.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ContingencyEquipment")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> contingency_equipment.serialize


# <<< contingency
# @generated
# >>> contingency
