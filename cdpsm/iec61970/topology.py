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

""" An extension to the Core Package that in association with the Terminal class models Connectivity, that is the physical definition of how equipment is connected together. In addition it models Topology, that is the logical definition of how equipment is connected via closed switches. The Topology definition is independent of the other electrical characteristics.An extension to the Core Package that in association with the Terminal class models Connectivity, that is the physical definition of how equipment is connected together. In addition it models Topology, that is the logical definition of how equipment is connected via closed switches. The Topology definition is independent of the other electrical characteristics.
"""

from cdpsm.iec61970.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Topology"

class ConnectivityNode(IdentifiedObject):
    """ Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance.Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance.
    """
    # <<< connectivity_node
    # @generated
    def __init__(self, terminals=None, connectivity_node_container=None, **kw_args):
        """ Initialises a new 'ConnectivityNode' instance.
        """

        self._terminals = []
        if terminals is not None:
            self.terminals = terminals
        else:
            self.terminals = []

        self._connectivity_node_container = None
        self.connectivity_node_container = connectivity_node_container


        super(ConnectivityNode, self).__init__(**kw_args)
    # >>> connectivity_node

    # <<< terminals
    # @generated
    def get_terminals(self):
        """ Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
        """
        return self._terminals

    def set_terminals(self, value):
        for x in self._terminals:
            x._connectivity_node = None
        for y in value:
            y._connectivity_node = self
        self._terminals = value

    terminals = property(get_terminals, set_terminals)

    def add_terminals(self, *terminals):
        for obj in terminals:
            obj._connectivity_node = self
            self._terminals.append(obj)

    def remove_terminals(self, *terminals):
        for obj in terminals:
            obj._connectivity_node = None
            self._terminals.remove(obj)
    # >>> terminals

    # <<< connectivity_node_container
    # @generated
    def get_connectivity_node_container(self):
        """ Container of this connectivity node.Container of this connectivity node.
        """
        return self._connectivity_node_container

    def set_connectivity_node_container(self, value):
        if self._connectivity_node_container is not None:
            filtered = [x for x in self.connectivity_node_container.connectivity_nodes if x != self]
            self._connectivity_node_container._connectivity_nodes = filtered

        self._connectivity_node_container = value
        if self._connectivity_node_container is not None:
            self._connectivity_node_container._connectivity_nodes.append(self)

    connectivity_node_container = property(get_connectivity_node_container, set_connectivity_node_container)
    # >>> connectivity_node_container


    def __str__(self):
        """ Returns a string representation of the ConnectivityNode.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< connectivity_node.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ConnectivityNode.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ConnectivityNode", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.terminals:
            s += '%s<%s:ConnectivityNode.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.connectivity_node_container is not None:
            s += '%s<%s:ConnectivityNode.connectivity_node_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.connectivity_node_container.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ConnectivityNode")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> connectivity_node.serialize


# <<< topology
# @generated
# >>> topology
