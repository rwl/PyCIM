# Copyright (C) 2009 Richard W. Lincoln
# All rights reserved.

from cpsm.core import ConnectivityNodeContainer
from cpsm.core import ConductingEquipment

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_Equivalents"

class EquivalentNetwork(ConnectivityNodeContainer):
    """ A class that represents an external meshed network that has been reduced to an electrically equivalent model. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent.A class that represents an external meshed network that has been reduced to an electrically equivalent model. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent.
    """
    # <<< equivalent_network
    # @generated
    def __init__(self, equivalent_equipments=None, **kw_args):
        """ Initialises a new 'EquivalentNetwork' instance.
        """

        self._equivalent_equipments = []
        if equivalent_equipments is not None:
            self.equivalent_equipments = equivalent_equipments
        else:
            self.equivalent_equipments = []


        super(EquivalentNetwork, self).__init__(**kw_args)
    # >>> equivalent_network

    # <<< equivalent_equipments
    # @generated
    def get_equivalent_equipments(self):
        """ The associated reduced equivalents.The associated reduced equivalents.
        """
        return self._equivalent_equipments

    def set_equivalent_equipments(self, value):
        for x in self._equivalent_equipments:
            x._equivalent_network = None
        for y in value:
            y._equivalent_network = self
        self._equivalent_equipments = value

    equivalent_equipments = property(get_equivalent_equipments, set_equivalent_equipments)

    def add_equivalent_equipments(self, *equivalent_equipments):
        for obj in equivalent_equipments:
            obj._equivalent_network = self
            self._equivalent_equipments.append(obj)

    def remove_equivalent_equipments(self, *equivalent_equipments):
        for obj in equivalent_equipments:
            obj._equivalent_network = None
            self._equivalent_equipments.remove(obj)
    # >>> equivalent_equipments


    def __str__(self):
        """ Returns a string representation of the EquivalentNetwork.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< equivalent_network.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the EquivalentNetwork.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "EquivalentNetwork", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.equivalent_equipments:
            s += '%s<%s:EquivalentNetwork.equivalent_equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "EquivalentNetwork")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> equivalent_network.serialize


class EquivalentEquipment(ConductingEquipment):
    """ The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of diferent types.The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of diferent types.
    """
    # <<< equivalent_equipment
    # @generated
    def __init__(self, equivalent_network=None, **kw_args):
        """ Initialises a new 'EquivalentEquipment' instance.
        """

        self._equivalent_network = None
        self.equivalent_network = equivalent_network


        super(EquivalentEquipment, self).__init__(**kw_args)
    # >>> equivalent_equipment

    # <<< equivalent_network
    # @generated
    def get_equivalent_network(self):
        """ The equivalent where the reduced model belongs.The equivalent where the reduced model belongs.
        """
        return self._equivalent_network

    def set_equivalent_network(self, value):
        if self._equivalent_network is not None:
            filtered = [x for x in self.equivalent_network.equivalent_equipments if x != self]
            self._equivalent_network._equivalent_equipments = filtered

        self._equivalent_network = value
        if self._equivalent_network is not None:
            self._equivalent_network._equivalent_equipments.append(self)

    equivalent_network = property(get_equivalent_network, set_equivalent_network)
    # >>> equivalent_network


    def __str__(self):
        """ Returns a string representation of the EquivalentEquipment.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< equivalent_equipment.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the EquivalentEquipment.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "EquivalentEquipment", self.uri)
        if format:
            indent += ' ' * depth

        if self.equivalent_network is not None:
            s += '%s<%s:EquivalentEquipment.equivalent_network rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equivalent_network.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
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
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "EquivalentEquipment")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> equivalent_equipment.serialize


class EquivalentShunt(EquivalentEquipment):
    """ The class represents equivalent shunts.The class represents equivalent shunts.
    """
    # <<< equivalent_shunt
    # @generated
    def __init__(self, b=0.0, g=0.0, **kw_args):
        """ Initialises a new 'EquivalentShunt' instance.
        """
        # Positive sequence shunt susceptance.Positive sequence shunt susceptance. 
        self.b = b

        # Positive sequence shunt conductance.Positive sequence shunt conductance. 
        self.g = g



        super(EquivalentShunt, self).__init__(**kw_args)
    # >>> equivalent_shunt


    def __str__(self):
        """ Returns a string representation of the EquivalentShunt.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< equivalent_shunt.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the EquivalentShunt.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "EquivalentShunt", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:EquivalentShunt.b>%s</%s:EquivalentShunt.b>' % \
            (indent, ns_prefix, self.b, ns_prefix)
        s += '%s<%s:EquivalentShunt.g>%s</%s:EquivalentShunt.g>' % \
            (indent, ns_prefix, self.g, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
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
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.equivalent_network is not None:
            s += '%s<%s:EquivalentEquipment.equivalent_network rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equivalent_network.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "EquivalentShunt")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> equivalent_shunt.serialize


class EquivalentBranch(EquivalentEquipment):
    """ The class represents equivalent branches.The class represents equivalent branches.
    """
    # <<< equivalent_branch
    # @generated
    def __init__(self, x=0.0, r=0.0, **kw_args):
        """ Initialises a new 'EquivalentBranch' instance.
        """
        # Positive sequence series reactance of the reduced branch.Positive sequence series reactance of the reduced branch. 
        self.x = x

        # Positive sequence series resistance of the reduced branch.Positive sequence series resistance of the reduced branch. 
        self.r = r



        super(EquivalentBranch, self).__init__(**kw_args)
    # >>> equivalent_branch


    def __str__(self):
        """ Returns a string representation of the EquivalentBranch.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< equivalent_branch.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the EquivalentBranch.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "EquivalentBranch", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:EquivalentBranch.x>%s</%s:EquivalentBranch.x>' % \
            (indent, ns_prefix, self.x, ns_prefix)
        s += '%s<%s:EquivalentBranch.r>%s</%s:EquivalentBranch.r>' % \
            (indent, ns_prefix, self.r, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
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
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.equivalent_network is not None:
            s += '%s<%s:EquivalentEquipment.equivalent_network rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equivalent_network.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "EquivalentBranch")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> equivalent_branch.serialize


# <<< equivalents
# @generated
# >>> equivalents
