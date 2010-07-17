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

""" The ControlArea package models area specifications which can be used for a variety of purposes.  The package as a whole models potentially overlapping control area specifications for the purpose of actual generation control, load forecast area load capture, or powerflow based analysis.
"""

from cim import Element
from cim.core import PowerSystemResource

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimControlArea"

ns_uri = "http://iec.ch/TC57/CIM-generic#ControlArea"

class AltTieMeas(Element):
    """ A prioritized measurement to be used for the tie flow as part of the control area specification.
    """
    # <<< alt_tie_meas
    # @generated
    def __init__(self, priority=0, tie_flow=None, analog_value=None, **kw_args):
        """ Initialises a new 'AltTieMeas' instance.
        """
        # Priority of a measurement usage.   Lower numbers have first priority. 
        self.priority = priority


        self._tie_flow = None
        self.tie_flow = tie_flow

        self._analog_value = None
        self.analog_value = analog_value


        super(AltTieMeas, self).__init__(**kw_args)
    # >>> alt_tie_meas

    # <<< tie_flow
    # @generated
    def get_tie_flow(self):
        """ The tie flow of the alternate measurements.
        """
        return self._tie_flow

    def set_tie_flow(self, value):
        if self._tie_flow is not None:
            filtered = [x for x in self.tie_flow.alt_tie_meas if x != self]
            self._tie_flow._alt_tie_meas = filtered

        self._tie_flow = value
        if self._tie_flow is not None:
            self._tie_flow._alt_tie_meas.append(self)

    tie_flow = property(get_tie_flow, set_tie_flow)
    # >>> tie_flow

    # <<< analog_value
    # @generated
    def get_analog_value(self):
        """ The specific analog value used as a source.
        """
        return self._analog_value

    def set_analog_value(self, value):
        if self._analog_value is not None:
            filtered = [x for x in self.analog_value.alt_tie_meas if x != self]
            self._analog_value._alt_tie_meas = filtered

        self._analog_value = value
        if self._analog_value is not None:
            self._analog_value._alt_tie_meas.append(self)

    analog_value = property(get_analog_value, set_analog_value)
    # >>> analog_value


    def __str__(self):
        """ Returns a string representation of the AltTieMeas.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< alt_tie_meas.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AltTieMeas.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AltTieMeas", self.uri)
        if format:
            indent += ' ' * depth

        if self.tie_flow is not None:
            s += '%s<%s:AltTieMeas.tie_flow rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.tie_flow.uri)
        if self.analog_value is not None:
            s += '%s<%s:AltTieMeas.analog_value rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.analog_value.uri)
        s += '%s<%s:AltTieMeas.priority>%s</%s:AltTieMeas.priority>' % \
            (indent, ns_prefix, self.priority, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "AltTieMeas")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> alt_tie_meas.serialize


class AltGeneratingUnitMeas(Element):
    """ A prioritized measurement to be used for the generating unit in the control area specificaiton.
    """
    # <<< alt_generating_unit_meas
    # @generated
    def __init__(self, priority=0, analog_value=None, control_area_generating_unit=None, **kw_args):
        """ Initialises a new 'AltGeneratingUnitMeas' instance.
        """
        # Priority of a measurement usage.   Lower numbers have first priority. 
        self.priority = priority


        self._analog_value = None
        self.analog_value = analog_value

        self._control_area_generating_unit = None
        self.control_area_generating_unit = control_area_generating_unit


        super(AltGeneratingUnitMeas, self).__init__(**kw_args)
    # >>> alt_generating_unit_meas

    # <<< analog_value
    # @generated
    def get_analog_value(self):
        """ The specific analog value used as a source.
        """
        return self._analog_value

    def set_analog_value(self, value):
        if self._analog_value is not None:
            filtered = [x for x in self.analog_value.alt_generating_unit if x != self]
            self._analog_value._alt_generating_unit = filtered

        self._analog_value = value
        if self._analog_value is not None:
            self._analog_value._alt_generating_unit.append(self)

    analog_value = property(get_analog_value, set_analog_value)
    # >>> analog_value

    # <<< control_area_generating_unit
    # @generated
    def get_control_area_generating_unit(self):
        """ The control aread generating unit to which the prioritized measurement assignment is applied.
        """
        return self._control_area_generating_unit

    def set_control_area_generating_unit(self, value):
        if self._control_area_generating_unit is not None:
            filtered = [x for x in self.control_area_generating_unit.alt_generating_unit_meas if x != self]
            self._control_area_generating_unit._alt_generating_unit_meas = filtered

        self._control_area_generating_unit = value
        if self._control_area_generating_unit is not None:
            self._control_area_generating_unit._alt_generating_unit_meas.append(self)

    control_area_generating_unit = property(get_control_area_generating_unit, set_control_area_generating_unit)
    # >>> control_area_generating_unit


    def __str__(self):
        """ Returns a string representation of the AltGeneratingUnitMeas.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< alt_generating_unit_meas.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AltGeneratingUnitMeas.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AltGeneratingUnitMeas", self.uri)
        if format:
            indent += ' ' * depth

        if self.analog_value is not None:
            s += '%s<%s:AltGeneratingUnitMeas.analog_value rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.analog_value.uri)
        if self.control_area_generating_unit is not None:
            s += '%s<%s:AltGeneratingUnitMeas.control_area_generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.control_area_generating_unit.uri)
        s += '%s<%s:AltGeneratingUnitMeas.priority>%s</%s:AltGeneratingUnitMeas.priority>' % \
            (indent, ns_prefix, self.priority, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "AltGeneratingUnitMeas")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> alt_generating_unit_meas.serialize


class ControlArea(PowerSystemResource):
    """ A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.
    """
    # <<< control_area
    # @generated
    def __init__(self, type='agc', p_tolerance=0.0, net_interchange=0.0, energy_area=None, tie_flow=None, control_area_generating_unit=None, bus_name_marker=None, topological_node=None, **kw_args):
        """ Initialises a new 'ControlArea' instance.
        """
        # The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes. Values are: "agc", "interchange", "forecast"
        self.type = 'agc'

        # Active power net interchange tolerance 
        self.p_tolerance = p_tolerance

        # The specified positive net interchange into the control area. 
        self.net_interchange = net_interchange


        self._energy_area = None
        self.energy_area = energy_area

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

        self._bus_name_marker = []
        if bus_name_marker is not None:
            self.bus_name_marker = bus_name_marker
        else:
            self.bus_name_marker = []

        self._topological_node = []
        if topological_node is not None:
            self.topological_node = topological_node
        else:
            self.topological_node = []


        super(ControlArea, self).__init__(**kw_args)
    # >>> control_area

    # <<< energy_area
    # @generated
    def get_energy_area(self):
        """ The energy area that is forecast from this control area specification.
        """
        return self._energy_area

    def set_energy_area(self, value):
        if self._energy_area is not None:
            self._energy_area._control_area = None

        self._energy_area = value
        if self._energy_area is not None:
            self._energy_area._control_area = self

    energy_area = property(get_energy_area, set_energy_area)
    # >>> energy_area

    # <<< tie_flow
    # @generated
    def get_tie_flow(self):
        """ The tie flows associated with the control area.
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
        """ The generating unit specificaitons for the control area.
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

    # <<< bus_name_marker
    # @generated
    def get_bus_name_marker(self):
        """ BusNameMarker objects that belong to the control area.
        """
        return self._bus_name_marker

    def set_bus_name_marker(self, value):
        for x in self._bus_name_marker:
            x._control_area = None
        for y in value:
            y._control_area = self
        self._bus_name_marker = value

    bus_name_marker = property(get_bus_name_marker, set_bus_name_marker)

    def add_bus_name_marker(self, *bus_name_marker):
        for obj in bus_name_marker:
            obj._control_area = self
            self._bus_name_marker.append(obj)

    def remove_bus_name_marker(self, *bus_name_marker):
        for obj in bus_name_marker:
            obj._control_area = None
            self._bus_name_marker.remove(obj)
    # >>> bus_name_marker

    # <<< topological_node
    # @generated
    def get_topological_node(self):
        """ The topological nodes included in the control area.
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

        if self.energy_area is not None:
            s += '%s<%s:ControlArea.energy_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.energy_area.uri)
        for obj in self.tie_flow:
            s += '%s<%s:ControlArea.tie_flow rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.control_area_generating_unit:
            s += '%s<%s:ControlArea.control_area_generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.bus_name_marker:
            s += '%s<%s:ControlArea.bus_name_marker rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.topological_node:
            s += '%s<%s:ControlArea.topological_node rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ControlArea.type>%s</%s:ControlArea.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)
        s += '%s<%s:ControlArea.p_tolerance>%s</%s:ControlArea.p_tolerance>' % \
            (indent, ns_prefix, self.p_tolerance, ns_prefix)
        s += '%s<%s:ControlArea.net_interchange>%s</%s:ControlArea.net_interchange>' % \
            (indent, ns_prefix, self.net_interchange, ns_prefix)
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
        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ControlArea")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> control_area.serialize


class TieFlow(Element):
    """ A flow specification in terms of location and direction for a control area.
    """
    # <<< tie_flow
    # @generated
    def __init__(self, positive_flow_in=False, alt_tie_meas=None, terminal=None, control_area=None, **kw_args):
        """ Initialises a new 'TieFlow' instance.
        """
        # The flow is positive into the terminal.  A flow is positive if it is an import into the control area. 
        self.positive_flow_in = positive_flow_in


        self._alt_tie_meas = []
        if alt_tie_meas is not None:
            self.alt_tie_meas = alt_tie_meas
        else:
            self.alt_tie_meas = []

        self._terminal = None
        self.terminal = terminal

        self._control_area = None
        self.control_area = control_area


        super(TieFlow, self).__init__(**kw_args)
    # >>> tie_flow

    # <<< alt_tie_meas
    # @generated
    def get_alt_tie_meas(self):
        """ The primary and alternate tie flow measurements associated with the tie flow.
        """
        return self._alt_tie_meas

    def set_alt_tie_meas(self, value):
        for x in self._alt_tie_meas:
            x._tie_flow = None
        for y in value:
            y._tie_flow = self
        self._alt_tie_meas = value

    alt_tie_meas = property(get_alt_tie_meas, set_alt_tie_meas)

    def add_alt_tie_meas(self, *alt_tie_meas):
        for obj in alt_tie_meas:
            obj._tie_flow = self
            self._alt_tie_meas.append(obj)

    def remove_alt_tie_meas(self, *alt_tie_meas):
        for obj in alt_tie_meas:
            obj._tie_flow = None
            self._alt_tie_meas.remove(obj)
    # >>> alt_tie_meas

    # <<< terminal
    # @generated
    def get_terminal(self):
        """ The terminal to which this tie flow belongs.
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

    # <<< control_area
    # @generated
    def get_control_area(self):
        """ The control area of the tie flows.
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

        for obj in self.alt_tie_meas:
            s += '%s<%s:TieFlow.alt_tie_meas rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.terminal is not None:
            s += '%s<%s:TieFlow.terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.terminal.uri)
        if self.control_area is not None:
            s += '%s<%s:TieFlow.control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.control_area.uri)
        s += '%s<%s:TieFlow.positive_flow_in>%s</%s:TieFlow.positive_flow_in>' % \
            (indent, ns_prefix, self.positive_flow_in, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "TieFlow")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> tie_flow.serialize


class ControlAreaGeneratingUnit(Element):
    """ A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.
    """
    # <<< control_area_generating_unit
    # @generated
    def __init__(self, alt_generating_unit_meas=None, control_area=None, generating_unit=None, **kw_args):
        """ Initialises a new 'ControlAreaGeneratingUnit' instance.
        """

        self._alt_generating_unit_meas = []
        if alt_generating_unit_meas is not None:
            self.alt_generating_unit_meas = alt_generating_unit_meas
        else:
            self.alt_generating_unit_meas = []

        self._control_area = None
        self.control_area = control_area

        self._generating_unit = None
        self.generating_unit = generating_unit


        super(ControlAreaGeneratingUnit, self).__init__(**kw_args)
    # >>> control_area_generating_unit

    # <<< alt_generating_unit_meas
    # @generated
    def get_alt_generating_unit_meas(self):
        """ The link to prioritized measurements for this GeneratingUnit.
        """
        return self._alt_generating_unit_meas

    def set_alt_generating_unit_meas(self, value):
        for x in self._alt_generating_unit_meas:
            x._control_area_generating_unit = None
        for y in value:
            y._control_area_generating_unit = self
        self._alt_generating_unit_meas = value

    alt_generating_unit_meas = property(get_alt_generating_unit_meas, set_alt_generating_unit_meas)

    def add_alt_generating_unit_meas(self, *alt_generating_unit_meas):
        for obj in alt_generating_unit_meas:
            obj._control_area_generating_unit = self
            self._alt_generating_unit_meas.append(obj)

    def remove_alt_generating_unit_meas(self, *alt_generating_unit_meas):
        for obj in alt_generating_unit_meas:
            obj._control_area_generating_unit = None
            self._alt_generating_unit_meas.remove(obj)
    # >>> alt_generating_unit_meas

    # <<< control_area
    # @generated
    def get_control_area(self):
        """ The parent control area for the generating unit specifications.
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
        """ The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once.
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

        for obj in self.alt_generating_unit_meas:
            s += '%s<%s:ControlAreaGeneratingUnit.alt_generating_unit_meas rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.control_area is not None:
            s += '%s<%s:ControlAreaGeneratingUnit.control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.control_area.uri)
        if self.generating_unit is not None:
            s += '%s<%s:ControlAreaGeneratingUnit.generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.generating_unit.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ControlAreaGeneratingUnit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> control_area_generating_unit.serialize


# <<< control_area
# @generated
# >>> control_area
