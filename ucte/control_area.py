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

""" The ControlArea package models area specifications which can be used for a variety of purposes.  The package as a whole models potentially overlapping control area specifications for the purpose of actual generation control, load forecast area load capture, or powerflow based analysis.The ControlArea package models area specifications which can be used for a variety of purposes.  The package as a whole models potentially overlapping control area specifications for the purpose of actual generation control, load forecast area load capture, or powerflow based analysis.
"""

from ucte.core import IdentifiedObject
from ucte import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_ControlArea"

class ControlArea(IdentifiedObject):
    """ A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.
    """
    # <<< control_area
    # @generated
    def __init__(self, p_tolerance=0.0, net_interchange=0.0, topological_node=None, tie_flow=None, control_area_generating_unit=None, **kw_args):
        """ Initialises a new 'ControlArea' instance.
        """
        # Active power net interchange toleranceActive power net interchange tolerance 
        self.p_tolerance = p_tolerance

        # The specified positive net interchange into the control area.The specified positive net interchange into the control area. 
        self.net_interchange = net_interchange


        self._topological_node = []
        if topological_node is not None:
            self.topological_node = topological_node
        else:
            self.topological_node = []

        self._tie_flow = []
        if tie_flow is not None:
            self.tie_flow = tie_flow
        else:
            self.tie_flow = []

        self._control_area_generating_unit = []
        if control_area_generating_unit is not None:
            self.control_area_generating_unit = control_area_generating_unit
        else:
            self.control_area_generating_unit = []


        super(ControlArea, self).__init__(**kw_args)
    # >>> control_area

    # <<< topological_node
    # @generated
    def get_topological_node(self):
        """ The topological nodes included in the control area.The topological nodes included in the control area.
        """
        return self._topological_node

    def set_topological_node(self, value):
        for x in self._topological_node:
            x._control_area = None
        for y in value:
            y._control_area = self
        self._topological_node = value

    topological_node = property(get_topological_node, set_topological_node)

    def add_topological_node(self, *topological_node):
        for obj in topological_node:
            obj._control_area = self
            self._topological_node.append(obj)

    def remove_topological_node(self, *topological_node):
        for obj in topological_node:
            obj._control_area = None
            self._topological_node.remove(obj)
    # >>> topological_node

    # <<< tie_flow
    # @generated
    def get_tie_flow(self):
        """ The tie flows associated with the control area.The tie flows associated with the control area.
        """
        return self._tie_flow

    def set_tie_flow(self, value):
        for x in self._tie_flow:
            x._control_area = None
        for y in value:
            y._control_area = self
        self._tie_flow = value

    tie_flow = property(get_tie_flow, set_tie_flow)

    def add_tie_flow(self, *tie_flow):
        for obj in tie_flow:
            obj._control_area = self
            self._tie_flow.append(obj)

    def remove_tie_flow(self, *tie_flow):
        for obj in tie_flow:
            obj._control_area = None
            self._tie_flow.remove(obj)
    # >>> tie_flow

    # <<< control_area_generating_unit
    # @generated
    def get_control_area_generating_unit(self):
        """ The generating unit specificaitons for the control area.The generating unit specificaitons for the control area.
        """
        return self._control_area_generating_unit

    def set_control_area_generating_unit(self, value):
        for x in self._control_area_generating_unit:
            x._control_area = None
        for y in value:
            y._control_area = self
        self._control_area_generating_unit = value

    control_area_generating_unit = property(get_control_area_generating_unit, set_control_area_generating_unit)

    def add_control_area_generating_unit(self, *control_area_generating_unit):
        for obj in control_area_generating_unit:
            obj._control_area = self
            self._control_area_generating_unit.append(obj)

    def remove_control_area_generating_unit(self, *control_area_generating_unit):
        for obj in control_area_generating_unit:
            obj._control_area = None
            self._control_area_generating_unit.remove(obj)
    # >>> control_area_generating_unit


    def __str__(self):
        """ Returns a string representation of the ControlArea.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< control_area.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ControlArea.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ControlArea", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.topological_node:
            s += '%s<%s:ControlArea.topological_node rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.tie_flow:
            s += '%s<%s:ControlArea.tie_flow rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.control_area_generating_unit:
            s += '%s<%s:ControlArea.control_area_generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ControlArea.p_tolerance>%s</%s:ControlArea.p_tolerance>' % \
            (indent, ns_prefix, self.p_tolerance, ns_prefix)
        s += '%s<%s:ControlArea.net_interchange>%s</%s:ControlArea.net_interchange>' % \
            (indent, ns_prefix, self.net_interchange, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ControlArea")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> control_area.serialize


class ControlAreaGeneratingUnit(Element):
    """ A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.
    """
    # <<< control_area_generating_unit
    # @generated
    def __init__(self, control_area=None, generating_unit=None, **kw_args):
        """ Initialises a new 'ControlAreaGeneratingUnit' instance.
        """

        self._control_area = None
        self.control_area = control_area

        self._generating_unit = None
        self.generating_unit = generating_unit


        super(ControlAreaGeneratingUnit, self).__init__(**kw_args)
    # >>> control_area_generating_unit

    # <<< control_area
    # @generated
    def get_control_area(self):
        """ The parent control area for the generating unit specifications.The parent control area for the generating unit specifications.
        """
        return self._control_area

    def set_control_area(self, value):
        if self._control_area is not None:
            filtered = [x for x in self.control_area.control_area_generating_unit if x != self]
            self._control_area._control_area_generating_unit = filtered

        self._control_area = value
        if self._control_area is not None:
            self._control_area._control_area_generating_unit.append(self)

    control_area = property(get_control_area, set_control_area)
    # >>> control_area

    # <<< generating_unit
    # @generated
    def get_generating_unit(self):
        """ The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once.The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once.
        """
        return self._generating_unit

    def set_generating_unit(self, value):
        if self._generating_unit is not None:
            filtered = [x for x in self.generating_unit.control_area_generating_unit if x != self]
            self._generating_unit._control_area_generating_unit = filtered

        self._generating_unit = value
        if self._generating_unit is not None:
            self._generating_unit._control_area_generating_unit.append(self)

    generating_unit = property(get_generating_unit, set_generating_unit)
    # >>> generating_unit


    def __str__(self):
        """ Returns a string representation of the ControlAreaGeneratingUnit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< control_area_generating_unit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ControlAreaGeneratingUnit.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ControlAreaGeneratingUnit", self.uri)
        if format:
            indent += ' ' * depth

        if self.control_area is not None:
            s += '%s<%s:ControlAreaGeneratingUnit.control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.control_area.uri)
        if self.generating_unit is not None:
            s += '%s<%s:ControlAreaGeneratingUnit.generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.generating_unit.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ControlAreaGeneratingUnit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> control_area_generating_unit.serialize


class TieFlow(Element):
    """ A flow specification in terms of location and direction for a control area.A flow specification in terms of location and direction for a control area.
    """
    # <<< tie_flow
    # @generated
    def __init__(self, positive_flow_in=False, control_area=None, terminal=None, **kw_args):
        """ Initialises a new 'TieFlow' instance.
        """
        # The flow is positive into the terminal.  A flow is positive if it is an import into the control area.The power flow is positive into the Terminal of the ConductingEquipment.The flow is positive into the terminal.  A flow is positive if it is an import into the control area.The power flow is positive into the Terminal of the ConductingEquipment. 
        self.positive_flow_in = positive_flow_in


        self._control_area = None
        self.control_area = control_area

        self._terminal = None
        self.terminal = terminal


        super(TieFlow, self).__init__(**kw_args)
    # >>> tie_flow

    # <<< control_area
    # @generated
    def get_control_area(self):
        """ The control area of the tie flows.The control area of the tie flows.
        """
        return self._control_area

    def set_control_area(self, value):
        if self._control_area is not None:
            filtered = [x for x in self.control_area.tie_flow if x != self]
            self._control_area._tie_flow = filtered

        self._control_area = value
        if self._control_area is not None:
            self._control_area._tie_flow.append(self)

    control_area = property(get_control_area, set_control_area)
    # >>> control_area

    # <<< terminal
    # @generated
    def get_terminal(self):
        """ The terminal to which this tie flow belongs.The terminal to which this tie flow belongs.
        """
        return self._terminal

    def set_terminal(self, value):
        if self._terminal is not None:
            filtered = [x for x in self.terminal.tie_flow if x != self]
            self._terminal._tie_flow = filtered

        self._terminal = value
        if self._terminal is not None:
            self._terminal._tie_flow.append(self)

    terminal = property(get_terminal, set_terminal)
    # >>> terminal


    def __str__(self):
        """ Returns a string representation of the TieFlow.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< tie_flow.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TieFlow.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TieFlow", self.uri)
        if format:
            indent += ' ' * depth

        if self.control_area is not None:
            s += '%s<%s:TieFlow.control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.control_area.uri)
        if self.terminal is not None:
            s += '%s<%s:TieFlow.terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.terminal.uri)
        s += '%s<%s:TieFlow.positive_flow_in>%s</%s:TieFlow.positive_flow_in>' % \
            (indent, ns_prefix, self.positive_flow_in, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "TieFlow")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> tie_flow.serialize


# <<< control_area
# @generated
# >>> control_area
