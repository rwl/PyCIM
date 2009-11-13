# Copyright (C) 2009 Richard W. Lincoln
# All rights reserved.

from cpsm.core import PowerSystemResource
from cpsm import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_ControlArea"

class ControlArea(PowerSystemResource):
    """ A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.
    """
    # <<< control_area
    # @generated
    def __init__(self, net_interchange=0.0, type='forecast', control_area_generating_unit=None, energy_area=None, tie_flow=None, **kw_args):
        """ Initialises a new 'ControlArea' instance.
        """
        # The specified positive net interchange into the control area.The specified positive net interchange into the control area. 
        self.net_interchange = net_interchange

        # The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes.The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes. Values are: "forecast", "interchange", "agc"
        self.type = 'forecast'


        self._control_area_generating_unit = []
        if control_area_generating_unit is not None:
            self.control_area_generating_unit = control_area_generating_unit
        else:
            self.control_area_generating_unit = []

        self._energy_area = None
        self.energy_area = energy_area

        self._tie_flow = []
        if tie_flow is not None:
            self.tie_flow = tie_flow
        else:
            self.tie_flow = []


        super(ControlArea, self).__init__(**kw_args)
    # >>> control_area

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

    # <<< energy_area
    # @generated
    def get_energy_area(self):
        """ The energy area that is forecast from this control area specification.The energy area that is forecast from this control area specification.
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

        for obj in self.control_area_generating_unit:
            s += '%s<%s:ControlArea.control_area_generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.energy_area is not None:
            s += '%s<%s:ControlArea.energy_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.energy_area.uri)
        for obj in self.tie_flow:
            s += '%s<%s:ControlArea.tie_flow rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ControlArea.net_interchange>%s</%s:ControlArea.net_interchange>' % \
            (indent, ns_prefix, self.net_interchange, ns_prefix)
        s += '%s<%s:ControlArea.type>%s</%s:ControlArea.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ControlArea")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> control_area.serialize


class TieFlow(Element):
    """ A flow specification in terms of location and direction for a control area.A flow specification in terms of location and direction for a control area.
    """
    # <<< tie_flow
    # @generated
    def __init__(self, positive_flow_in=False, control_area=None, **kw_args):
        """ Initialises a new 'TieFlow' instance.
        """
        # The flow is positive into the terminal.  A flow is positive if it is an import into the control area.The flow is positive into the terminal.  A flow is positive if it is an import into the control area. 
        self.positive_flow_in = positive_flow_in


        self._control_area = None
        self.control_area = control_area


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
        s += '%s<%s:TieFlow.positive_flow_in>%s</%s:TieFlow.positive_flow_in>' % \
            (indent, ns_prefix, self.positive_flow_in, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "TieFlow")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> tie_flow.serialize


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
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

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
