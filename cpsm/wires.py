# Copyright (C) 2009 Richard W. Lincoln
# All rights reserved.
""" An extension to the Core and Topology package that models information on the electrical characteristics of Transmission and Distribution networks. This package is used by network applications such as State Estimation, Load Flow and Optimal Power Flow.An extension to the Core and Topology package that models information on the electrical characteristics of Transmission and Distribution networks. This package is used by network applications such as State Estimation, Load Flow and Optimal Power Flow.
"""

from cpsm.core import Equipment
from cpsm.core import ConductingEquipment
from cpsm.core import PowerSystemResource
from cpsm.core import RegularIntervalSchedule
from cpsm.core import Curve
from cpsm.core import EquipmentContainer

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_Wires"

class PowerTransformer(Equipment):
    """ An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).
    """
    # <<< power_transformer
    # @generated
    def __init__(self, contains_transformer_windings=None, **kw_args):
        """ Initialises a new 'PowerTransformer' instance.
        """

        self._contains_transformer_windings = []
        if contains_transformer_windings is not None:
            self.contains_transformer_windings = contains_transformer_windings
        else:
            self.contains_transformer_windings = []


        super(PowerTransformer, self).__init__(**kw_args)
    # >>> power_transformer

    # <<< contains_transformer_windings
    # @generated
    def get_contains_transformer_windings(self):
        """ A transformer has windingsA transformer has windings
        """
        return self._contains_transformer_windings

    def set_contains_transformer_windings(self, value):
        for x in self._contains_transformer_windings:
            x._member_of_power_transformer = None
        for y in value:
            y._member_of_power_transformer = self
        self._contains_transformer_windings = value

    contains_transformer_windings = property(get_contains_transformer_windings, set_contains_transformer_windings)

    def add_contains_transformer_windings(self, *contains_transformer_windings):
        for obj in contains_transformer_windings:
            obj._member_of_power_transformer = self
            self._contains_transformer_windings.append(obj)

    def remove_contains_transformer_windings(self, *contains_transformer_windings):
        for obj in contains_transformer_windings:
            obj._member_of_power_transformer = None
            self._contains_transformer_windings.remove(obj)
    # >>> contains_transformer_windings


    def __str__(self):
        """ Returns a string representation of the PowerTransformer.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< power_transformer.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PowerTransformer.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PowerTransformer", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.contains_transformer_windings:
            s += '%s<%s:PowerTransformer.contains_transformer_windings rdf:resource="#%s"/>' % \
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
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        for obj in self.operational_limit_set:
            s += '%s<%s:Equipment.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PowerTransformer")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> power_transformer.serialize


class BusbarSection(ConductingEquipment):
    """ A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.
    """
    pass
    # <<< busbar_section
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'BusbarSection' instance.
        """


        super(BusbarSection, self).__init__(**kw_args)
    # >>> busbar_section


    def __str__(self):
        """ Returns a string representation of the BusbarSection.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< busbar_section.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BusbarSection.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BusbarSection", self.uri)
        if format:
            indent += ' ' * depth

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
        s += '%s</%s:%s>' % (indent, ns_prefix, "BusbarSection")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> busbar_section.serialize


class RegulatingCondEq(ConductingEquipment):
    """ RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule.RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule.
    """
    # <<< regulating_cond_eq
    # @generated
    def __init__(self, regulating_control=None, **kw_args):
        """ Initialises a new 'RegulatingCondEq' instance.
        """

        self._regulating_control = None
        self.regulating_control = regulating_control


        super(RegulatingCondEq, self).__init__(**kw_args)
    # >>> regulating_cond_eq

    # <<< regulating_control
    # @generated
    def get_regulating_control(self):
        """ copy from ...copy from ...
        """
        return self._regulating_control

    def set_regulating_control(self, value):
        if self._regulating_control is not None:
            filtered = [x for x in self.regulating_control.regulating_cond_eq if x != self]
            self._regulating_control._regulating_cond_eq = filtered

        self._regulating_control = value
        if self._regulating_control is not None:
            self._regulating_control._regulating_cond_eq.append(self)

    regulating_control = property(get_regulating_control, set_regulating_control)
    # >>> regulating_control


    def __str__(self):
        """ Returns a string representation of the RegulatingCondEq.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< regulating_cond_eq.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RegulatingCondEq.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RegulatingCondEq", self.uri)
        if format:
            indent += ' ' * depth

        if self.regulating_control is not None:
            s += '%s<%s:RegulatingCondEq.regulating_control rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.regulating_control.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "RegulatingCondEq")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> regulating_cond_eq.serialize


class EnergyConsumer(ConductingEquipment):
    """ Generic user of energy - a  point of consumption on the power system modelGeneric user of energy - a  point of consumption on the power system model
    """
    # <<< energy_consumer
    # @generated
    def __init__(self, qfixed_pct=0.0, pfixed=0.0, qfixed=0.0, pfixed_pct=0.0, load_response=None, **kw_args):
        """ Initialises a new 'EnergyConsumer' instance.
        """
        # Fixed reactive power as per cent of load group fixed reactive power.Fixed reactive power as per cent of load group fixed reactive power. 
        self.qfixed_pct = qfixed_pct

        # Active power of the load that is a fixed quantity.Active power of the load that is a fixed quantity. 
        self.pfixed = pfixed

        # Reactive power of the load that is a fixed quantity.Reactive power of the load that is a fixed quantity. 
        self.qfixed = qfixed

        # Fixed active power as per cent of load group fixed active powerFixed active power as per cent of load group fixed active power 
        self.pfixed_pct = pfixed_pct


        self._load_response = None
        self.load_response = load_response


        super(EnergyConsumer, self).__init__(**kw_args)
    # >>> energy_consumer

    # <<< load_response
    # @generated
    def get_load_response(self):
        """ The load response characteristic of this load.The load response characteristic of this load.
        """
        return self._load_response

    def set_load_response(self, value):
        if self._load_response is not None:
            filtered = [x for x in self.load_response.energy_consumer if x != self]
            self._load_response._energy_consumer = filtered

        self._load_response = value
        if self._load_response is not None:
            self._load_response._energy_consumer.append(self)

    load_response = property(get_load_response, set_load_response)
    # >>> load_response


    def __str__(self):
        """ Returns a string representation of the EnergyConsumer.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< energy_consumer.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the EnergyConsumer.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "EnergyConsumer", self.uri)
        if format:
            indent += ' ' * depth

        if self.load_response is not None:
            s += '%s<%s:EnergyConsumer.load_response rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.load_response.uri)
        s += '%s<%s:EnergyConsumer.qfixed_pct>%s</%s:EnergyConsumer.qfixed_pct>' % \
            (indent, ns_prefix, self.qfixed_pct, ns_prefix)
        s += '%s<%s:EnergyConsumer.pfixed>%s</%s:EnergyConsumer.pfixed>' % \
            (indent, ns_prefix, self.pfixed, ns_prefix)
        s += '%s<%s:EnergyConsumer.qfixed>%s</%s:EnergyConsumer.qfixed>' % \
            (indent, ns_prefix, self.qfixed, ns_prefix)
        s += '%s<%s:EnergyConsumer.pfixed_pct>%s</%s:EnergyConsumer.pfixed_pct>' % \
            (indent, ns_prefix, self.pfixed_pct, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "EnergyConsumer")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> energy_consumer.serialize


class TransformerWinding(ConductingEquipment):
    """ A winding is associated with each defined terminal of a transformer (or phase shifter).A winding is associated with each defined terminal of a transformer (or phase shifter).
    """
    # <<< transformer_winding
    # @generated
    def __init__(self, winding_type='primary', rated_s=0.0, x=0.0, rated_u=0.0, r=0.0, b=0.0, tap_changers=None, member_of_power_transformer=None, **kw_args):
        """ Initialises a new 'TransformerWinding' instance.
        """
        # The type of winding.The type of winding. Values are: "primary", "tertiary", "secondary", "quaternary"
        self.winding_type = 'primary'

        # The normal apparent power rating for the windingThe normal apparent power rating for the winding 
        self.rated_s = rated_s

        # Positive sequence series reactance of the winding.Positive sequence series reactance of the winding. 
        self.x = x

        # The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage. 
        self.rated_u = rated_u

        # Positive sequence series resistance of the winding.Positive sequence series resistance of the winding. 
        self.r = r

        # Magnetizing branch susceptance (B mag).Magnetizing branch susceptance (B mag). 
        self.b = b


        self._tap_changers = []
        if tap_changers is not None:
            self.tap_changers = tap_changers
        else:
            self.tap_changers = []

        self._member_of_power_transformer = None
        self.member_of_power_transformer = member_of_power_transformer


        super(TransformerWinding, self).__init__(**kw_args)
    # >>> transformer_winding

    # <<< tap_changers
    # @generated
    def get_tap_changers(self):
        """ A transformer winding may have tap changers, separately for voltage and phase angle.  If a TransformerWinding does not have an associated TapChanger, the winding is assumed to be fixed tap.A transformer winding may have tap changers, separately for voltage and phase angle.  If a TransformerWinding does not have an associated TapChanger, the winding is assumed to be fixed tap.
        """
        return self._tap_changers

    def set_tap_changers(self, value):
        for x in self._tap_changers:
            x._transformer_winding = None
        for y in value:
            y._transformer_winding = self
        self._tap_changers = value

    tap_changers = property(get_tap_changers, set_tap_changers)

    def add_tap_changers(self, *tap_changers):
        for obj in tap_changers:
            obj._transformer_winding = self
            self._tap_changers.append(obj)

    def remove_tap_changers(self, *tap_changers):
        for obj in tap_changers:
            obj._transformer_winding = None
            self._tap_changers.remove(obj)
    # >>> tap_changers

    # <<< member_of_power_transformer
    # @generated
    def get_member_of_power_transformer(self):
        """ A transformer has windingsA transformer has windings
        """
        return self._member_of_power_transformer

    def set_member_of_power_transformer(self, value):
        if self._member_of_power_transformer is not None:
            filtered = [x for x in self.member_of_power_transformer.contains_transformer_windings if x != self]
            self._member_of_power_transformer._contains_transformer_windings = filtered

        self._member_of_power_transformer = value
        if self._member_of_power_transformer is not None:
            self._member_of_power_transformer._contains_transformer_windings.append(self)

    member_of_power_transformer = property(get_member_of_power_transformer, set_member_of_power_transformer)
    # >>> member_of_power_transformer


    def __str__(self):
        """ Returns a string representation of the TransformerWinding.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< transformer_winding.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TransformerWinding.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TransformerWinding", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.tap_changers:
            s += '%s<%s:TransformerWinding.tap_changers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.member_of_power_transformer is not None:
            s += '%s<%s:TransformerWinding.member_of_power_transformer rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_power_transformer.uri)
        s += '%s<%s:TransformerWinding.winding_type>%s</%s:TransformerWinding.winding_type>' % \
            (indent, ns_prefix, self.winding_type, ns_prefix)
        s += '%s<%s:TransformerWinding.rated_s>%s</%s:TransformerWinding.rated_s>' % \
            (indent, ns_prefix, self.rated_s, ns_prefix)
        s += '%s<%s:TransformerWinding.x>%s</%s:TransformerWinding.x>' % \
            (indent, ns_prefix, self.x, ns_prefix)
        s += '%s<%s:TransformerWinding.rated_u>%s</%s:TransformerWinding.rated_u>' % \
            (indent, ns_prefix, self.rated_u, ns_prefix)
        s += '%s<%s:TransformerWinding.r>%s</%s:TransformerWinding.r>' % \
            (indent, ns_prefix, self.r, ns_prefix)
        s += '%s<%s:TransformerWinding.b>%s</%s:TransformerWinding.b>' % \
            (indent, ns_prefix, self.b, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "TransformerWinding")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> transformer_winding.serialize


class RegulatingControl(PowerSystemResource):
    """ Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.
    """
    # <<< regulating_control
    # @generated
    def __init__(self, terminal=None, regulation_schedule=None, tap_changer=None, regulating_cond_eq=None, **kw_args):
        """ Initialises a new 'RegulatingControl' instance.
        """

        self._terminal = None
        self.terminal = terminal

        self._regulation_schedule = None
        self.regulation_schedule = regulation_schedule

        self._tap_changer = []
        if tap_changer is not None:
            self.tap_changer = tap_changer
        else:
            self.tap_changer = []

        self._regulating_cond_eq = []
        if regulating_cond_eq is not None:
            self.regulating_cond_eq = regulating_cond_eq
        else:
            self.regulating_cond_eq = []


        super(RegulatingControl, self).__init__(**kw_args)
    # >>> regulating_control

    # <<< terminal
    # @generated
    def get_terminal(self):
        """ The terminal associated with this regulating control.The terminal associated with this regulating control.
        """
        return self._terminal

    def set_terminal(self, value):
        if self._terminal is not None:
            filtered = [x for x in self.terminal.regulating_control if x != self]
            self._terminal._regulating_control = filtered

        self._terminal = value
        if self._terminal is not None:
            self._terminal._regulating_control.append(self)

    terminal = property(get_terminal, set_terminal)
    # >>> terminal

    # <<< regulation_schedule
    # @generated
    def get_regulation_schedule(self):
        """ Schedule for this Regulating regulating control.Schedule for this Regulating regulating control.
        """
        return self._regulation_schedule

    def set_regulation_schedule(self, value):
        if self._regulation_schedule is not None:
            filtered = [x for x in self.regulation_schedule.regulating_control if x != self]
            self._regulation_schedule._regulating_control = filtered

        self._regulation_schedule = value
        if self._regulation_schedule is not None:
            self._regulation_schedule._regulating_control.append(self)

    regulation_schedule = property(get_regulation_schedule, set_regulation_schedule)
    # >>> regulation_schedule

    # <<< tap_changer
    # @generated
    def get_tap_changer(self):
        """ copy from reg conduting eqcopy from reg conduting eq
        """
        return self._tap_changer

    def set_tap_changer(self, value):
        for x in self._tap_changer:
            x._regulating_control = None
        for y in value:
            y._regulating_control = self
        self._tap_changer = value

    tap_changer = property(get_tap_changer, set_tap_changer)

    def add_tap_changer(self, *tap_changer):
        for obj in tap_changer:
            obj._regulating_control = self
            self._tap_changer.append(obj)

    def remove_tap_changer(self, *tap_changer):
        for obj in tap_changer:
            obj._regulating_control = None
            self._tap_changer.remove(obj)
    # >>> tap_changer

    # <<< regulating_cond_eq
    # @generated
    def get_regulating_cond_eq(self):
        """ copy from reg cond eqcopy from reg cond eq
        """
        return self._regulating_cond_eq

    def set_regulating_cond_eq(self, value):
        for x in self._regulating_cond_eq:
            x._regulating_control = None
        for y in value:
            y._regulating_control = self
        self._regulating_cond_eq = value

    regulating_cond_eq = property(get_regulating_cond_eq, set_regulating_cond_eq)

    def add_regulating_cond_eq(self, *regulating_cond_eq):
        for obj in regulating_cond_eq:
            obj._regulating_control = self
            self._regulating_cond_eq.append(obj)

    def remove_regulating_cond_eq(self, *regulating_cond_eq):
        for obj in regulating_cond_eq:
            obj._regulating_control = None
            self._regulating_cond_eq.remove(obj)
    # >>> regulating_cond_eq


    def __str__(self):
        """ Returns a string representation of the RegulatingControl.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< regulating_control.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RegulatingControl.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RegulatingControl", self.uri)
        if format:
            indent += ' ' * depth

        if self.terminal is not None:
            s += '%s<%s:RegulatingControl.terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.terminal.uri)
        if self.regulation_schedule is not None:
            s += '%s<%s:RegulatingControl.regulation_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.regulation_schedule.uri)
        for obj in self.tap_changer:
            s += '%s<%s:RegulatingControl.tap_changer rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.regulating_cond_eq:
            s += '%s<%s:RegulatingControl.regulating_cond_eq rdf:resource="#%s"/>' % \
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "RegulatingControl")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> regulating_control.serialize


class RegulationSchedule(RegularIntervalSchedule):
    """ A pre-established pattern over time for a controlled variable, e.g., busbar voltage.A pre-established pattern over time for a controlled variable, e.g., busbar voltage.
    """
    # <<< regulation_schedule
    # @generated
    def __init__(self, regulating_control=None, **kw_args):
        """ Initialises a new 'RegulationSchedule' instance.
        """

        self._regulating_control = []
        if regulating_control is not None:
            self.regulating_control = regulating_control
        else:
            self.regulating_control = []


        super(RegulationSchedule, self).__init__(**kw_args)
    # >>> regulation_schedule

    # <<< regulating_control
    # @generated
    def get_regulating_control(self):
        """ Regulating controls that have this Schedule.Regulating controls that have this Schedule.
        """
        return self._regulating_control

    def set_regulating_control(self, value):
        for x in self._regulating_control:
            x._regulation_schedule = None
        for y in value:
            y._regulation_schedule = self
        self._regulating_control = value

    regulating_control = property(get_regulating_control, set_regulating_control)

    def add_regulating_control(self, *regulating_control):
        for obj in regulating_control:
            obj._regulation_schedule = self
            self._regulating_control.append(obj)

    def remove_regulating_control(self, *regulating_control):
        for obj in regulating_control:
            obj._regulation_schedule = None
            self._regulating_control.remove(obj)
    # >>> regulating_control


    def __str__(self):
        """ Returns a string representation of the RegulationSchedule.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< regulation_schedule.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RegulationSchedule.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RegulationSchedule", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.regulating_control:
            s += '%s<%s:RegulationSchedule.regulating_control rdf:resource="#%s"/>' % \
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
        s += '%s<%s:BasicIntervalSchedule.start_time>%s</%s:BasicIntervalSchedule.start_time>' % \
            (indent, ns_prefix, self.start_time, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value1_unit>%s</%s:BasicIntervalSchedule.value1_unit>' % \
            (indent, ns_prefix, self.value1_unit, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value2_unit>%s</%s:BasicIntervalSchedule.value2_unit>' % \
            (indent, ns_prefix, self.value2_unit, ns_prefix)
        for obj in self.time_points:
            s += '%s<%s:RegularIntervalSchedule.time_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:RegularIntervalSchedule.end_time>%s</%s:RegularIntervalSchedule.end_time>' % \
            (indent, ns_prefix, self.end_time, ns_prefix)
        s += '%s<%s:RegularIntervalSchedule.time_step>%s</%s:RegularIntervalSchedule.time_step>' % \
            (indent, ns_prefix, self.time_step, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "RegulationSchedule")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> regulation_schedule.serialize


class Switch(ConductingEquipment):
    """ A generic device designed to close, or open, or both, one or more electric circuits.A generic device designed to close, or open, or both, one or more electric circuits.
    """
    # <<< switch
    # @generated
    def __init__(self, normal_open=False, **kw_args):
        """ Initialises a new 'Switch' instance.
        """
        # The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen.The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen. 
        self.normal_open = normal_open



        super(Switch, self).__init__(**kw_args)
    # >>> switch


    def __str__(self):
        """ Returns a string representation of the Switch.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< switch.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Switch.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Switch", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:Switch.normal_open>%s</%s:Switch.normal_open>' % \
            (indent, ns_prefix, self.normal_open, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Switch")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> switch.serialize


class Conductor(ConductingEquipment):
    """ Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.
    """
    # <<< conductor
    # @generated
    def __init__(self, r=0.0, x=0.0, bch=0.0, **kw_args):
        """ Initialises a new 'Conductor' instance.
        """
        # Positive sequence series resistance of the entire line section.Positive sequence series resistance of the entire line section. 
        self.r = r

        # Positive sequence series reactance of the entire line section.Positive sequence series reactance of the entire line section. 
        self.x = x

        # Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section. 
        self.bch = bch



        super(Conductor, self).__init__(**kw_args)
    # >>> conductor


    def __str__(self):
        """ Returns a string representation of the Conductor.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< conductor.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Conductor.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Conductor", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:Conductor.r>%s</%s:Conductor.r>' % \
            (indent, ns_prefix, self.r, ns_prefix)
        s += '%s<%s:Conductor.x>%s</%s:Conductor.x>' % \
            (indent, ns_prefix, self.x, ns_prefix)
        s += '%s<%s:Conductor.bch>%s</%s:Conductor.bch>' % \
            (indent, ns_prefix, self.bch, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Conductor")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> conductor.serialize


class ReactiveCapabilityCurve(Curve):
    """ Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.
    """
    # <<< reactive_capability_curve
    # @generated
    def __init__(self, initially_used_by_synchronous_machine=None, **kw_args):
        """ Initialises a new 'ReactiveCapabilityCurve' instance.
        """

        self._initially_used_by_synchronous_machine = []
        if initially_used_by_synchronous_machine is not None:
            self.initially_used_by_synchronous_machine = initially_used_by_synchronous_machine
        else:
            self.initially_used_by_synchronous_machine = []


        super(ReactiveCapabilityCurve, self).__init__(**kw_args)
    # >>> reactive_capability_curve

    # <<< initially_used_by_synchronous_machine
    # @generated
    def get_initially_used_by_synchronous_machine(self):
        """ Synchronous machines using this curve as default.Synchronous machines using this curve as default.
        """
        return self._initially_used_by_synchronous_machine

    def set_initially_used_by_synchronous_machine(self, value):
        for x in self._initially_used_by_synchronous_machine:
            x._initial_reactive_capability_curve = None
        for y in value:
            y._initial_reactive_capability_curve = self
        self._initially_used_by_synchronous_machine = value

    initially_used_by_synchronous_machine = property(get_initially_used_by_synchronous_machine, set_initially_used_by_synchronous_machine)

    def add_initially_used_by_synchronous_machine(self, *initially_used_by_synchronous_machine):
        for obj in initially_used_by_synchronous_machine:
            obj._initial_reactive_capability_curve = self
            self._initially_used_by_synchronous_machine.append(obj)

    def remove_initially_used_by_synchronous_machine(self, *initially_used_by_synchronous_machine):
        for obj in initially_used_by_synchronous_machine:
            obj._initial_reactive_capability_curve = None
            self._initially_used_by_synchronous_machine.remove(obj)
    # >>> initially_used_by_synchronous_machine


    def __str__(self):
        """ Returns a string representation of the ReactiveCapabilityCurve.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< reactive_capability_curve.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ReactiveCapabilityCurve.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ReactiveCapabilityCurve", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.initially_used_by_synchronous_machine:
            s += '%s<%s:ReactiveCapabilityCurve.initially_used_by_synchronous_machine rdf:resource="#%s"/>' % \
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ReactiveCapabilityCurve")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> reactive_capability_curve.serialize


class TapChanger(PowerSystemResource):
    """ Mechanism for changing transformer winding tap positions.Mechanism for changing transformer winding tap positions.
    """
    # <<< tap_changer
    # @generated
    def __init__(self, normal_step=0, high_step=0, step_phase_shift_increment=0.0, neutral_step=0, low_step=0, tcul_control_mode='local', step_voltage_increment=0.0, type='voltage_and_phase_control', neutral_u=0.0, regulating_control=None, transformer_winding=None, **kw_args):
        """ Initialises a new 'TapChanger' instance.
        """
        # The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting. 
        self.normal_step = normal_step

        # Highest possible tap step position, advance from neutralHighest possible tap step position, advance from neutral 
        self.high_step = high_step

        # Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer).Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). 
        self.step_phase_shift_increment = step_phase_shift_increment

        # The neutral tap step position for this winding.The neutral tap step position for this winding. 
        self.neutral_step = neutral_step

        # Lowest possible tap step position, retard from neutralLowest possible tap step position, retard from neutral 
        self.low_step = low_step

        # For an LTC, the tap changer control mode.For an LTC, the tap changer control mode. Values are: "local", "active", "volt", "off", "reactive"
        self.tcul_control_mode = 'local'

        # Tap step increment, in per cent of nominal voltage, per step position.Tap step increment, in per cent of nominal voltage, per step position. 
        self.step_voltage_increment = step_voltage_increment

        # The type of tap changer. Indicates the ability of the transformer to perform various regulation tasks. The tap changer must be also be associated wtih a RegulationControl object before any regulation is possible.The type of tap changer. Indicates the ability of the transformer to perform various regulation tasks. The tap changer must be also be associated wtih a RegulationControl object before any regulation is possible. Values are: "voltage_and_phase_control", "phase_control", "fixed", "voltage_control"
        self.type = 'voltage_and_phase_control'

        # Voltage at which the winding operates at the neutral tap setting.Voltage at which the winding operates at the neutral tap setting. 
        self.neutral_u = neutral_u


        self._regulating_control = None
        self.regulating_control = regulating_control

        self._transformer_winding = None
        self.transformer_winding = transformer_winding


        super(TapChanger, self).__init__(**kw_args)
    # >>> tap_changer

    # <<< regulating_control
    # @generated
    def get_regulating_control(self):
        """ 
        """
        return self._regulating_control

    def set_regulating_control(self, value):
        if self._regulating_control is not None:
            filtered = [x for x in self.regulating_control.tap_changer if x != self]
            self._regulating_control._tap_changer = filtered

        self._regulating_control = value
        if self._regulating_control is not None:
            self._regulating_control._tap_changer.append(self)

    regulating_control = property(get_regulating_control, set_regulating_control)
    # >>> regulating_control

    # <<< transformer_winding
    # @generated
    def get_transformer_winding(self):
        """ A transformer winding may have tap changers, separately for voltage and phase angleA transformer winding may have tap changers, separately for voltage and phase angle
        """
        return self._transformer_winding

    def set_transformer_winding(self, value):
        if self._transformer_winding is not None:
            filtered = [x for x in self.transformer_winding.tap_changers if x != self]
            self._transformer_winding._tap_changers = filtered

        self._transformer_winding = value
        if self._transformer_winding is not None:
            self._transformer_winding._tap_changers.append(self)

    transformer_winding = property(get_transformer_winding, set_transformer_winding)
    # >>> transformer_winding


    def __str__(self):
        """ Returns a string representation of the TapChanger.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< tap_changer.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TapChanger.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TapChanger", self.uri)
        if format:
            indent += ' ' * depth

        if self.regulating_control is not None:
            s += '%s<%s:TapChanger.regulating_control rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.regulating_control.uri)
        if self.transformer_winding is not None:
            s += '%s<%s:TapChanger.transformer_winding rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.transformer_winding.uri)
        s += '%s<%s:TapChanger.normal_step>%s</%s:TapChanger.normal_step>' % \
            (indent, ns_prefix, self.normal_step, ns_prefix)
        s += '%s<%s:TapChanger.high_step>%s</%s:TapChanger.high_step>' % \
            (indent, ns_prefix, self.high_step, ns_prefix)
        s += '%s<%s:TapChanger.step_phase_shift_increment>%s</%s:TapChanger.step_phase_shift_increment>' % \
            (indent, ns_prefix, self.step_phase_shift_increment, ns_prefix)
        s += '%s<%s:TapChanger.neutral_step>%s</%s:TapChanger.neutral_step>' % \
            (indent, ns_prefix, self.neutral_step, ns_prefix)
        s += '%s<%s:TapChanger.low_step>%s</%s:TapChanger.low_step>' % \
            (indent, ns_prefix, self.low_step, ns_prefix)
        s += '%s<%s:TapChanger.tcul_control_mode>%s</%s:TapChanger.tcul_control_mode>' % \
            (indent, ns_prefix, self.tcul_control_mode, ns_prefix)
        s += '%s<%s:TapChanger.step_voltage_increment>%s</%s:TapChanger.step_voltage_increment>' % \
            (indent, ns_prefix, self.step_voltage_increment, ns_prefix)
        s += '%s<%s:TapChanger.type>%s</%s:TapChanger.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)
        s += '%s<%s:TapChanger.neutral_u>%s</%s:TapChanger.neutral_u>' % \
            (indent, ns_prefix, self.neutral_u, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "TapChanger")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> tap_changer.serialize


class Line(EquipmentContainer):
    """ A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.
    """
    # <<< line
    # @generated
    def __init__(self, region=None, **kw_args):
        """ Initialises a new 'Line' instance.
        """

        self._region = None
        self.region = region


        super(Line, self).__init__(**kw_args)
    # >>> line

    # <<< region
    # @generated
    def get_region(self):
        """ A Line can be contained by a SubGeographical Region.A Line can be contained by a SubGeographical Region.
        """
        return self._region

    def set_region(self, value):
        if self._region is not None:
            filtered = [x for x in self.region.lines if x != self]
            self._region._lines = filtered

        self._region = value
        if self._region is not None:
            self._region._lines.append(self)

    region = property(get_region, set_region)
    # >>> region


    def __str__(self):
        """ Returns a string representation of the Line.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< line.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Line.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Line", self.uri)
        if format:
            indent += ' ' * depth

        if self.region is not None:
            s += '%s<%s:Line.region rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.region.uri)
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
        for obj in self.contains_equipments:
            s += '%s<%s:EquipmentContainer.contains_equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Line")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> line.serialize


class SeriesCompensator(ConductingEquipment):
    """ A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.
    """
    # <<< series_compensator
    # @generated
    def __init__(self, r=0.0, x=0.0, **kw_args):
        """ Initialises a new 'SeriesCompensator' instance.
        """
        # Positive sequence resistance.Positive sequence resistance. 
        self.r = r

        # Positive sequence reactance.Positive sequence reactance. 
        self.x = x



        super(SeriesCompensator, self).__init__(**kw_args)
    # >>> series_compensator


    def __str__(self):
        """ Returns a string representation of the SeriesCompensator.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< series_compensator.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SeriesCompensator.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SeriesCompensator", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:SeriesCompensator.r>%s</%s:SeriesCompensator.r>' % \
            (indent, ns_prefix, self.r, ns_prefix)
        s += '%s<%s:SeriesCompensator.x>%s</%s:SeriesCompensator.x>' % \
            (indent, ns_prefix, self.x, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "SeriesCompensator")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> series_compensator.serialize


class Disconnector(Switch):
    """ A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when negligible current is broken or made.A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when negligible current is broken or made.
    """
    pass
    # <<< disconnector
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'Disconnector' instance.
        """


        super(Disconnector, self).__init__(**kw_args)
    # >>> disconnector


    def __str__(self):
        """ Returns a string representation of the Disconnector.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< disconnector.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Disconnector.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Disconnector", self.uri)
        if format:
            indent += ' ' * depth

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
        s += '%s<%s:Switch.normal_open>%s</%s:Switch.normal_open>' % \
            (indent, ns_prefix, self.normal_open, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Disconnector")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> disconnector.serialize


class SynchronousMachine(RegulatingCondEq):
    """ An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.
    """
    # <<< synchronous_machine
    # @generated
    def __init__(self, operating_mode='generator', min_q=0.0, type='generator', max_q=0.0, initial_reactive_capability_curve=None, member_of_generating_unit=None, **kw_args):
        """ Initialises a new 'SynchronousMachine' instance.
        """
        # Current mode of operation.Current mode of operation. Values are: "generator", "condenser"
        self.operating_mode = 'generator'

        # Minimum reactive power limit for the unit.Minimum reactive power limit for the unit. 
        self.min_q = min_q

        # Modes that this synchronous machine can operate in.Modes that this synchronous machine can operate in. Values are: "generator", "generator_or_condenser", "condenser"
        self.type = 'generator'

        # Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.Maximum reactive power limit. This is the maximum (nameplate) limit for the unit. 
        self.max_q = max_q


        self._initial_reactive_capability_curve = None
        self.initial_reactive_capability_curve = initial_reactive_capability_curve

        self._member_of_generating_unit = None
        self.member_of_generating_unit = member_of_generating_unit


        super(SynchronousMachine, self).__init__(**kw_args)
    # >>> synchronous_machine

    # <<< initial_reactive_capability_curve
    # @generated
    def get_initial_reactive_capability_curve(self):
        """ The default ReactiveCapabilityCurve for use by a SynchronousMachineThe default ReactiveCapabilityCurve for use by a SynchronousMachine
        """
        return self._initial_reactive_capability_curve

    def set_initial_reactive_capability_curve(self, value):
        if self._initial_reactive_capability_curve is not None:
            filtered = [x for x in self.initial_reactive_capability_curve.initially_used_by_synchronous_machine if x != self]
            self._initial_reactive_capability_curve._initially_used_by_synchronous_machine = filtered

        self._initial_reactive_capability_curve = value
        if self._initial_reactive_capability_curve is not None:
            self._initial_reactive_capability_curve._initially_used_by_synchronous_machine.append(self)

    initial_reactive_capability_curve = property(get_initial_reactive_capability_curve, set_initial_reactive_capability_curve)
    # >>> initial_reactive_capability_curve

    # <<< member_of_generating_unit
    # @generated
    def get_member_of_generating_unit(self):
        """ A synchronous machine may operate as a generator and as such becomes a member of a generating unitA synchronous machine may operate as a generator and as such becomes a member of a generating unit
        """
        return self._member_of_generating_unit

    def set_member_of_generating_unit(self, value):
        if self._member_of_generating_unit is not None:
            filtered = [x for x in self.member_of_generating_unit.contains_synchronous_machines if x != self]
            self._member_of_generating_unit._contains_synchronous_machines = filtered

        self._member_of_generating_unit = value
        if self._member_of_generating_unit is not None:
            self._member_of_generating_unit._contains_synchronous_machines.append(self)

    member_of_generating_unit = property(get_member_of_generating_unit, set_member_of_generating_unit)
    # >>> member_of_generating_unit


    def __str__(self):
        """ Returns a string representation of the SynchronousMachine.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< synchronous_machine.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SynchronousMachine.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SynchronousMachine", self.uri)
        if format:
            indent += ' ' * depth

        if self.initial_reactive_capability_curve is not None:
            s += '%s<%s:SynchronousMachine.initial_reactive_capability_curve rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.initial_reactive_capability_curve.uri)
        if self.member_of_generating_unit is not None:
            s += '%s<%s:SynchronousMachine.member_of_generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_generating_unit.uri)
        s += '%s<%s:SynchronousMachine.operating_mode>%s</%s:SynchronousMachine.operating_mode>' % \
            (indent, ns_prefix, self.operating_mode, ns_prefix)
        s += '%s<%s:SynchronousMachine.min_q>%s</%s:SynchronousMachine.min_q>' % \
            (indent, ns_prefix, self.min_q, ns_prefix)
        s += '%s<%s:SynchronousMachine.type>%s</%s:SynchronousMachine.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)
        s += '%s<%s:SynchronousMachine.max_q>%s</%s:SynchronousMachine.max_q>' % \
            (indent, ns_prefix, self.max_q, ns_prefix)
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
        if self.regulating_control is not None:
            s += '%s<%s:RegulatingCondEq.regulating_control rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.regulating_control.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SynchronousMachine")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> synchronous_machine.serialize


class ShuntCompensator(RegulatingCondEq):
    """ A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor.A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor.
    """
    # <<< shunt_compensator
    # @generated
    def __init__(self, maximum_sections=0, normal_sections=0, nom_u=0.0, reactive_per_section=0.0, **kw_args):
        """ Initialises a new 'ShuntCompensator' instance.
        """
        # For a capacitor bank, the maximum number of sections that may be switched in.For a capacitor bank, the maximum number of sections that may be switched in. 
        self.maximum_sections = maximum_sections

        # For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ). 
        self.normal_sections = normal_sections

        # The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network. 
        self.nom_u = nom_u

        # For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage. 
        self.reactive_per_section = reactive_per_section



        super(ShuntCompensator, self).__init__(**kw_args)
    # >>> shunt_compensator


    def __str__(self):
        """ Returns a string representation of the ShuntCompensator.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< shunt_compensator.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ShuntCompensator.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ShuntCompensator", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ShuntCompensator.maximum_sections>%s</%s:ShuntCompensator.maximum_sections>' % \
            (indent, ns_prefix, self.maximum_sections, ns_prefix)
        s += '%s<%s:ShuntCompensator.normal_sections>%s</%s:ShuntCompensator.normal_sections>' % \
            (indent, ns_prefix, self.normal_sections, ns_prefix)
        s += '%s<%s:ShuntCompensator.nom_u>%s</%s:ShuntCompensator.nom_u>' % \
            (indent, ns_prefix, self.nom_u, ns_prefix)
        s += '%s<%s:ShuntCompensator.reactive_per_section>%s</%s:ShuntCompensator.reactive_per_section>' % \
            (indent, ns_prefix, self.reactive_per_section, ns_prefix)
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
        if self.regulating_control is not None:
            s += '%s<%s:RegulatingCondEq.regulating_control rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.regulating_control.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ShuntCompensator")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> shunt_compensator.serialize


class LoadBreakSwitch(Switch):
    """ A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions.A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions.
    """
    # <<< load_break_switch
    # @generated
    def __init__(self, rated_current=0.0, **kw_args):
        """ Initialises a new 'LoadBreakSwitch' instance.
        """
        # Current carrying capacity of a wire or cable under stated thermal conditions.Current carrying capacity of a wire or cable under stated thermal conditions. 
        self.rated_current = rated_current



        super(LoadBreakSwitch, self).__init__(**kw_args)
    # >>> load_break_switch


    def __str__(self):
        """ Returns a string representation of the LoadBreakSwitch.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< load_break_switch.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LoadBreakSwitch.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LoadBreakSwitch", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:LoadBreakSwitch.rated_current>%s</%s:LoadBreakSwitch.rated_current>' % \
            (indent, ns_prefix, self.rated_current, ns_prefix)
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
        s += '%s<%s:Switch.normal_open>%s</%s:Switch.normal_open>' % \
            (indent, ns_prefix, self.normal_open, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LoadBreakSwitch")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> load_break_switch.serialize


class ACLineSegment(Conductor):
    """ A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.
    """
    pass
    # <<< acline_segment
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ACLineSegment' instance.
        """


        super(ACLineSegment, self).__init__(**kw_args)
    # >>> acline_segment


    def __str__(self):
        """ Returns a string representation of the ACLineSegment.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< acline_segment.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ACLineSegment.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ACLineSegment", self.uri)
        if format:
            indent += ' ' * depth

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
        s += '%s<%s:Conductor.r>%s</%s:Conductor.r>' % \
            (indent, ns_prefix, self.r, ns_prefix)
        s += '%s<%s:Conductor.x>%s</%s:Conductor.x>' % \
            (indent, ns_prefix, self.x, ns_prefix)
        s += '%s<%s:Conductor.bch>%s</%s:Conductor.bch>' % \
            (indent, ns_prefix, self.bch, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ACLineSegment")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> acline_segment.serialize


class StaticVarCompensator(RegulatingCondEq):
    """ A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode.  When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero.A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode.  When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero.
    """
    # <<< static_var_compensator
    # @generated
    def __init__(self, voltage_set_point=0.0, s_vccontrol_mode='voltage', capacitive_rating=0.0, slope=0.0, inductive_rating=0.0, **kw_args):
        """ Initialises a new 'StaticVarCompensator' instance.
        """
        # The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero.The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero. 
        self.voltage_set_point = voltage_set_point

        # SVC control mode.SVC control mode. Values are: "voltage", "off", "reactive_power"
        self.s_vccontrol_mode = 'voltage'

        # Maximum available capacitive reactive powerMaximum available capacitive reactive power 
        self.capacitive_rating = capacitive_rating

        # The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint.The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint. 
        self.slope = slope

        # Maximum available inductive reactive powerMaximum available inductive reactive power 
        self.inductive_rating = inductive_rating



        super(StaticVarCompensator, self).__init__(**kw_args)
    # >>> static_var_compensator


    def __str__(self):
        """ Returns a string representation of the StaticVarCompensator.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< static_var_compensator.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the StaticVarCompensator.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "StaticVarCompensator", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:StaticVarCompensator.voltage_set_point>%s</%s:StaticVarCompensator.voltage_set_point>' % \
            (indent, ns_prefix, self.voltage_set_point, ns_prefix)
        s += '%s<%s:StaticVarCompensator.s_vccontrol_mode>%s</%s:StaticVarCompensator.s_vccontrol_mode>' % \
            (indent, ns_prefix, self.s_vccontrol_mode, ns_prefix)
        s += '%s<%s:StaticVarCompensator.capacitive_rating>%s</%s:StaticVarCompensator.capacitive_rating>' % \
            (indent, ns_prefix, self.capacitive_rating, ns_prefix)
        s += '%s<%s:StaticVarCompensator.slope>%s</%s:StaticVarCompensator.slope>' % \
            (indent, ns_prefix, self.slope, ns_prefix)
        s += '%s<%s:StaticVarCompensator.inductive_rating>%s</%s:StaticVarCompensator.inductive_rating>' % \
            (indent, ns_prefix, self.inductive_rating, ns_prefix)
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
        if self.regulating_control is not None:
            s += '%s<%s:RegulatingCondEq.regulating_control rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.regulating_control.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "StaticVarCompensator")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> static_var_compensator.serialize


class Breaker(Switch):
    """ A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g.  those of short circuit.A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g.  those of short circuit.
    """
    # <<< breaker
    # @generated
    def __init__(self, rated_current=0.0, **kw_args):
        """ Initialises a new 'Breaker' instance.
        """
        # Fault interrupting current rating.Fault interrupting current rating. 
        self.rated_current = rated_current



        super(Breaker, self).__init__(**kw_args)
    # >>> breaker


    def __str__(self):
        """ Returns a string representation of the Breaker.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< breaker.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Breaker.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Breaker", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:Breaker.rated_current>%s</%s:Breaker.rated_current>' % \
            (indent, ns_prefix, self.rated_current, ns_prefix)
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
        s += '%s<%s:Switch.normal_open>%s</%s:Switch.normal_open>' % \
            (indent, ns_prefix, self.normal_open, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Breaker")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> breaker.serialize


# <<< wires
# @generated
# >>> wires
