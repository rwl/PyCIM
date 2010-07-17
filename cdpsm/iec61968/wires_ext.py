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

""" Contains only diagrams to be discussed with WG13, for consolidating T&amp;D models.Contains only diagrams to be discussed with WG13, for consolidating T&amp;D models.
"""

from cdpsm.iec61970.core import ConductingEquipment
from cdpsm.iec61970.wires import ACLineSegment
from cdpsm.iec61970.core import IdentifiedObject
from cdpsm.iec61970.wires import RatioTapChanger
from cdpsm.iec61970.core import Equipment
from cdpsm import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_WiresExt"

class DistributionTransformerWinding(ConductingEquipment):
    """ Conducting connection point of a distribution / unbalanced transformer winding instance. This class differs from Wires::TransformerWinding as follows: - the eight Pi model attributes are moved into separate class, that can be optionally referred to from several winding instances. - the three grounding attributes can differ per winding instance, even for windings that use the same TransformerInfo, so they are kept on DistributionTransformerWinding. 'sequenceNumber' attribute replaces 'windingType' attribute.  All the other attributes come from the WindingInfo (and its relationships). TransformerInfo is associated to the DistributionTransformer as referenceable data, so it can be defined once and referred to from instances, instead of being specified with each instance.Conducting connection point of a distribution / unbalanced transformer winding instance. This class differs from Wires::TransformerWinding as follows: - the eight Pi model attributes are moved into separate class, that can be optionally referred to from several winding instances. - the three grounding attributes can differ per winding instance, even for windings that use the same TransformerInfo, so they are kept on DistributionTransformerWinding. 'sequenceNumber' attribute replaces 'windingType' attribute.  All the other attributes come from the WindingInfo (and its relationships). TransformerInfo is associated to the DistributionTransformer as referenceable data, so it can be defined once and referred to from instances, instead of being specified with each instance.
    """
    # <<< distribution_transformer_winding
    # @generated
    def __init__(self, rground=0.0, xground=0.0, grounded=False, winding_info=None, transformer=None, ratio_tap_changer=None, pi_impedance=None, **kw_args):
        """ Initialises a new 'DistributionTransformerWinding' instance.
        """
        # (for Yn and Zn connections) Resistance part of neutral impedance where 'grounded' is true.(for Yn and Zn connections) Resistance part of neutral impedance where 'grounded' is true. 
        self.rground = rground

        # (for Yn and Zn connections) Reactive part of neutral impedance where 'grounded' is true.(for Yn and Zn connections) Reactive part of neutral impedance where 'grounded' is true. 
        self.xground = xground

        # (for Yn and Zn connections) True if the neutral is solidly grounded.(for Yn and Zn connections) True if the neutral is solidly grounded. 
        self.grounded = grounded


        self._winding_info = None
        self.winding_info = winding_info

        self._transformer = None
        self.transformer = transformer

        self._ratio_tap_changer = None
        self.ratio_tap_changer = ratio_tap_changer

        self._pi_impedance = None
        self.pi_impedance = pi_impedance


        super(DistributionTransformerWinding, self).__init__(**kw_args)
    # >>> distribution_transformer_winding

    # <<< winding_info
    # @generated
    def get_winding_info(self):
        """ Data for this winding.Data for this winding.
        """
        return self._winding_info

    def set_winding_info(self, value):
        if self._winding_info is not None:
            filtered = [x for x in self.winding_info.windings if x != self]
            self._winding_info._windings = filtered

        self._winding_info = value
        if self._winding_info is not None:
            self._winding_info._windings.append(self)

    winding_info = property(get_winding_info, set_winding_info)
    # >>> winding_info

    # <<< transformer
    # @generated
    def get_transformer(self):
        """ Transformer this winding belongs to.Transformer this winding belongs to.
        """
        return self._transformer

    def set_transformer(self, value):
        if self._transformer is not None:
            filtered = [x for x in self.transformer.windings if x != self]
            self._transformer._windings = filtered

        self._transformer = value
        if self._transformer is not None:
            self._transformer._windings.append(self)

    transformer = property(get_transformer, set_transformer)
    # >>> transformer

    # <<< ratio_tap_changer
    # @generated
    def get_ratio_tap_changer(self):
        """ Ratio tap changer associated with this winding.Ratio tap changer associated with this winding.
        """
        return self._ratio_tap_changer

    def set_ratio_tap_changer(self, value):
        if self._ratio_tap_changer is not None:
            self._ratio_tap_changer._winding = None

        self._ratio_tap_changer = value
        if self._ratio_tap_changer is not None:
            self._ratio_tap_changer._winding = self

    ratio_tap_changer = property(get_ratio_tap_changer, set_ratio_tap_changer)
    # >>> ratio_tap_changer

    # <<< pi_impedance
    # @generated
    def get_pi_impedance(self):
        """ (accurate for 2- or 3-winding transformers only) Pi-model impedances of this winding.(accurate for 2- or 3-winding transformers only) Pi-model impedances of this winding.
        """
        return self._pi_impedance

    def set_pi_impedance(self, value):
        if self._pi_impedance is not None:
            filtered = [x for x in self.pi_impedance.windings if x != self]
            self._pi_impedance._windings = filtered

        self._pi_impedance = value
        if self._pi_impedance is not None:
            self._pi_impedance._windings.append(self)

    pi_impedance = property(get_pi_impedance, set_pi_impedance)
    # >>> pi_impedance


    def __str__(self):
        """ Returns a string representation of the DistributionTransformerWinding.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< distribution_transformer_winding.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the DistributionTransformerWinding.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "DistributionTransformerWinding", self.uri)
        if format:
            indent += ' ' * depth

        if self.winding_info is not None:
            s += '%s<%s:DistributionTransformerWinding.winding_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.winding_info.uri)
        if self.transformer is not None:
            s += '%s<%s:DistributionTransformerWinding.transformer rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.transformer.uri)
        if self.ratio_tap_changer is not None:
            s += '%s<%s:DistributionTransformerWinding.ratio_tap_changer rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.ratio_tap_changer.uri)
        if self.pi_impedance is not None:
            s += '%s<%s:DistributionTransformerWinding.pi_impedance rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.pi_impedance.uri)
        s += '%s<%s:DistributionTransformerWinding.rground>%s</%s:DistributionTransformerWinding.rground>' % \
            (indent, ns_prefix, self.rground, ns_prefix)
        s += '%s<%s:DistributionTransformerWinding.xground>%s</%s:DistributionTransformerWinding.xground>' % \
            (indent, ns_prefix, self.xground, ns_prefix)
        s += '%s<%s:DistributionTransformerWinding.grounded>%s</%s:DistributionTransformerWinding.grounded>' % \
            (indent, ns_prefix, self.grounded, ns_prefix)
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
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        s += '%s<%s:ConductingEquipment.phases>%s</%s:ConductingEquipment.phases>' % \
            (indent, ns_prefix, self.phases, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "DistributionTransformerWinding")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> distribution_transformer_winding.serialize


class DistributionLineSegment(ACLineSegment):
    """ Extends ACLineSegment with references to a library of standard types from which electrical parameters can be calculated, as follows: - calculate electrical parameters from asset data, using associated ConductorInfo, with values then multiplied by Conductor.length to produce a matrix model. - calculate unbalanced electrical parameters from associated PerLengthPhaseImpedance, then multiplied by Conductor.length to produce a matrix model. - calculate transposed electrical parameters from associated PerLengthSequenceImpedance, then multiplied by Conductor.length to produce a sequence model. For symmetrical, transposed 3ph lines, it is sufficient to use inherited ACLineSegment attributes, which describe sequence impedances and admittances for the entire length of the segment.  Known issue: Attributes expressing impedances and admittances in PerLengthSequenceImpedance and PhaseImpedanceData use Resistance, etc., which describe pre-calculated, full length of segment, while we should have a longitudinal unit, per length. Taking 'r' as example, its 'unit'=Ohm, but the value is effectively in Ohm/m, so the value needs to be multiplied by Conductor.length. This is against the whole idea of unit data types and is semantically wrong, but base CIM does not have the required data types at this moment. Until the revision of unit modelling in CIM, applications need to deduce and locally handle appending '/m' for units and ensure they multiply the values by Conductor.length.At least one of the Associations must exist.Extends ACLineSegment with references to a library of standard types from which electrical parameters can be calculated, as follows: - calculate electrical parameters from asset data, using associated ConductorInfo, with values then multiplied by Conductor.length to produce a matrix model. - calculate unbalanced electrical parameters from associated PerLengthPhaseImpedance, then multiplied by Conductor.length to produce a matrix model. - calculate transposed electrical parameters from associated PerLengthSequenceImpedance, then multiplied by Conductor.length to produce a sequence model. For symmetrical, transposed 3ph lines, it is sufficient to use inherited ACLineSegment attributes, which describe sequence impedances and admittances for the entire length of the segment.  Known issue: Attributes expressing impedances and admittances in PerLengthSequenceImpedance and PhaseImpedanceData use Resistance, etc., which describe pre-calculated, full length of segment, while we should have a longitudinal unit, per length. Taking 'r' as example, its 'unit'=Ohm, but the value is effectively in Ohm/m, so the value needs to be multiplied by Conductor.length. This is against the whole idea of unit data types and is semantically wrong, but base CIM does not have the required data types at this moment. Until the revision of unit modelling in CIM, applications need to deduce and locally handle appending '/m' for units and ensure they multiply the values by Conductor.length.At least one of the Associations must exist.
    """
    # <<< distribution_line_segment
    # @generated
    def __init__(self, conductor_info=None, sequence_impedance=None, phase_impedance=None, **kw_args):
        """ Initialises a new 'DistributionLineSegment' instance.
        """

        self._conductor_info = None
        self.conductor_info = conductor_info

        self._sequence_impedance = None
        self.sequence_impedance = sequence_impedance

        self._phase_impedance = None
        self.phase_impedance = phase_impedance


        super(DistributionLineSegment, self).__init__(**kw_args)
    # >>> distribution_line_segment

    # <<< conductor_info
    # @generated
    def get_conductor_info(self):
        """ Conductor data of this conductor segment.Conductor data of this conductor segment.
        """
        return self._conductor_info

    def set_conductor_info(self, value):
        if self._conductor_info is not None:
            filtered = [x for x in self.conductor_info.conductor_segments if x != self]
            self._conductor_info._conductor_segments = filtered

        self._conductor_info = value
        if self._conductor_info is not None:
            self._conductor_info._conductor_segments.append(self)

    conductor_info = property(get_conductor_info, set_conductor_info)
    # >>> conductor_info

    # <<< sequence_impedance
    # @generated
    def get_sequence_impedance(self):
        """ Sequence impedance of this conductor segment; used for balanced model.Sequence impedance of this conductor segment; used for balanced model.
        """
        return self._sequence_impedance

    def set_sequence_impedance(self, value):
        if self._sequence_impedance is not None:
            filtered = [x for x in self.sequence_impedance.conductor_segments if x != self]
            self._sequence_impedance._conductor_segments = filtered

        self._sequence_impedance = value
        if self._sequence_impedance is not None:
            self._sequence_impedance._conductor_segments.append(self)

    sequence_impedance = property(get_sequence_impedance, set_sequence_impedance)
    # >>> sequence_impedance

    # <<< phase_impedance
    # @generated
    def get_phase_impedance(self):
        """ Phase impedance of this conductor segment; used for unbalanced model.Phase impedance of this conductor segment; used for unbalanced model.
        """
        return self._phase_impedance

    def set_phase_impedance(self, value):
        if self._phase_impedance is not None:
            filtered = [x for x in self.phase_impedance.conductor_segments if x != self]
            self._phase_impedance._conductor_segments = filtered

        self._phase_impedance = value
        if self._phase_impedance is not None:
            self._phase_impedance._conductor_segments.append(self)

    phase_impedance = property(get_phase_impedance, set_phase_impedance)
    # >>> phase_impedance


    def __str__(self):
        """ Returns a string representation of the DistributionLineSegment.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< distribution_line_segment.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the DistributionLineSegment.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "DistributionLineSegment", self.uri)
        if format:
            indent += ' ' * depth

        if self.conductor_info is not None:
            s += '%s<%s:DistributionLineSegment.conductor_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conductor_info.uri)
        if self.sequence_impedance is not None:
            s += '%s<%s:DistributionLineSegment.sequence_impedance rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.sequence_impedance.uri)
        if self.phase_impedance is not None:
            s += '%s<%s:DistributionLineSegment.phase_impedance rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.phase_impedance.uri)
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
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        s += '%s<%s:ConductingEquipment.phases>%s</%s:ConductingEquipment.phases>' % \
            (indent, ns_prefix, self.phases, ns_prefix)
        s += '%s<%s:Conductor.length>%s</%s:Conductor.length>' % \
            (indent, ns_prefix, self.length, ns_prefix)
        s += '%s<%s:ACLineSegment.r>%s</%s:ACLineSegment.r>' % \
            (indent, ns_prefix, self.r, ns_prefix)
        s += '%s<%s:ACLineSegment.x0>%s</%s:ACLineSegment.x0>' % \
            (indent, ns_prefix, self.x0, ns_prefix)
        s += '%s<%s:ACLineSegment.bch>%s</%s:ACLineSegment.bch>' % \
            (indent, ns_prefix, self.bch, ns_prefix)
        s += '%s<%s:ACLineSegment.x>%s</%s:ACLineSegment.x>' % \
            (indent, ns_prefix, self.x, ns_prefix)
        s += '%s<%s:ACLineSegment.b0ch>%s</%s:ACLineSegment.b0ch>' % \
            (indent, ns_prefix, self.b0ch, ns_prefix)
        s += '%s<%s:ACLineSegment.r0>%s</%s:ACLineSegment.r0>' % \
            (indent, ns_prefix, self.r0, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "DistributionLineSegment")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> distribution_line_segment.serialize


class WindingPiImpedance(IdentifiedObject):
    """ Transformer Pi-model impedance that accurately reflects impedance for transformers with 2 or 3 windings. For transformers with 4 or more windings, you must use TransformerInfo.Transformer Pi-model impedance that accurately reflects impedance for transformers with 2 or 3 windings. For transformers with 4 or more windings, you must use TransformerInfo.
    """
    # <<< winding_pi_impedance
    # @generated
    def __init__(self, x=0.0, g=0.0, r0=0.0, r=0.0, b=0.0, g0=0.0, x0=0.0, b0=0.0, windings=None, **kw_args):
        """ Initialises a new 'WindingPiImpedance' instance.
        """
        # Positive sequence series reactance of the winding.  For a two winding transformer, the full reactance of the transformer should be entered on the primary (high voltage) winding.Positive sequence series reactance of the winding.  For a two winding transformer, the full reactance of the transformer should be entered on the primary (high voltage) winding. 
        self.x = x

        # Magnetizing branch conductance (G mag).Magnetizing branch conductance (G mag). 
        self.g = g

        # Zero sequence series resistance of the winding.Zero sequence series resistance of the winding. 
        self.r0 = r0

        # DC resistance of the winding.DC resistance of the winding. 
        self.r = r

        # Magnetizing branch susceptance (B mag).  The value can be positive or negative.Magnetizing branch susceptance (B mag).  The value can be positive or negative. 
        self.b = b

        # Zero sequence magnetizing branch conductance.Zero sequence magnetizing branch conductance. 
        self.g0 = g0

        # Zero sequence series reactance of the winding.Zero sequence series reactance of the winding. 
        self.x0 = x0

        # Zero sequence magnetizing branch susceptance.Zero sequence magnetizing branch susceptance. 
        self.b0 = b0


        self._windings = []
        if windings is not None:
            self.windings = windings
        else:
            self.windings = []


        super(WindingPiImpedance, self).__init__(**kw_args)
    # >>> winding_pi_impedance

    # <<< windings
    # @generated
    def get_windings(self):
        """ All windings having this Pi impedance.All windings having this Pi impedance.
        """
        return self._windings

    def set_windings(self, value):
        for x in self._windings:
            x._pi_impedance = None
        for y in value:
            y._pi_impedance = self
        self._windings = value

    windings = property(get_windings, set_windings)

    def add_windings(self, *windings):
        for obj in windings:
            obj._pi_impedance = self
            self._windings.append(obj)

    def remove_windings(self, *windings):
        for obj in windings:
            obj._pi_impedance = None
            self._windings.remove(obj)
    # >>> windings


    def __str__(self):
        """ Returns a string representation of the WindingPiImpedance.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< winding_pi_impedance.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the WindingPiImpedance.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "WindingPiImpedance", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.windings:
            s += '%s<%s:WindingPiImpedance.windings rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:WindingPiImpedance.x>%s</%s:WindingPiImpedance.x>' % \
            (indent, ns_prefix, self.x, ns_prefix)
        s += '%s<%s:WindingPiImpedance.g>%s</%s:WindingPiImpedance.g>' % \
            (indent, ns_prefix, self.g, ns_prefix)
        s += '%s<%s:WindingPiImpedance.r0>%s</%s:WindingPiImpedance.r0>' % \
            (indent, ns_prefix, self.r0, ns_prefix)
        s += '%s<%s:WindingPiImpedance.r>%s</%s:WindingPiImpedance.r>' % \
            (indent, ns_prefix, self.r, ns_prefix)
        s += '%s<%s:WindingPiImpedance.b>%s</%s:WindingPiImpedance.b>' % \
            (indent, ns_prefix, self.b, ns_prefix)
        s += '%s<%s:WindingPiImpedance.g0>%s</%s:WindingPiImpedance.g0>' % \
            (indent, ns_prefix, self.g0, ns_prefix)
        s += '%s<%s:WindingPiImpedance.x0>%s</%s:WindingPiImpedance.x0>' % \
            (indent, ns_prefix, self.x0, ns_prefix)
        s += '%s<%s:WindingPiImpedance.b0>%s</%s:WindingPiImpedance.b0>' % \
            (indent, ns_prefix, self.b0, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "WindingPiImpedance")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> winding_pi_impedance.serialize


class DistributionTapChanger(RatioTapChanger):
    """ Additional ratio tap changer parameters common to distribution line regulators. 'tculControlMode' would always be 'volt'. If 'monitoredPhase' is not specified, then if the controlled DistributionTransformerWinding is single-phase, the PT primary is assumed to be connected across that winding, which is the normal case. If the controlled winding is three-phase, then the 'monitoredPhase' is assumed to be 'AN', unless otherwise specified. Whenever 'ctRatio' and 'ptRatio' are specified, it's customary to specify the R and X in 'volts' referred to the PT secondary circuit, otherwise R and X are in feeder primary ohms. If 'ptRatio' is not specified, then 'targetVoltage', 'limitVoltage', and 'bandVoltage' are on the feeder primary base, phase-neutral or phase-phase depending on the 'monitoredPhase'. Otherwise, these attributes are all on the PT secondary base.Additional ratio tap changer parameters common to distribution line regulators. 'tculControlMode' would always be 'volt'. If 'monitoredPhase' is not specified, then if the controlled DistributionTransformerWinding is single-phase, the PT primary is assumed to be connected across that winding, which is the normal case. If the controlled winding is three-phase, then the 'monitoredPhase' is assumed to be 'AN', unless otherwise specified. Whenever 'ctRatio' and 'ptRatio' are specified, it's customary to specify the R and X in 'volts' referred to the PT secondary circuit, otherwise R and X are in feeder primary ohms. If 'ptRatio' is not specified, then 'targetVoltage', 'limitVoltage', and 'bandVoltage' are on the feeder primary base, phase-neutral or phase-phase depending on the 'monitoredPhase'. Otherwise, these attributes are all on the PT secondary base.
    """
    # <<< distribution_tap_changer
    # @generated
    def __init__(self, line_drop_r=0.0, monitored_phase='abc', line_drop_compensation=False, pt_ratio=0.0, ct_ratio=0.0, reverse_line_drop_r=0.0, limit_voltage=0.0, reverse_line_drop_x=0.0, band_voltage=0.0, target_voltage=0.0, line_drop_x=0.0, **kw_args):
        """ Initialises a new 'DistributionTapChanger' instance.
        """
        # Line drop compensator resistance setting for normal (forward) power flow.Line drop compensator resistance setting for normal (forward) power flow. 
        self.line_drop_r = line_drop_r

        # Phase voltage controlling this regulator, measured at regulator location.Phase voltage controlling this regulator, measured at regulator location. Values are: "abc", "split_secondary2_n", "abn", "cn", "acn", "bc", "an", "bn", "ab", "split_secondary1_n", "n", "c", "ac", "abcn", "split_secondary12_n", "a", "b", "bcn"
        self.monitored_phase = 'abc'

        # If true, the line drop compensation is to be applied.If true, the line drop compensation is to be applied. 
        self.line_drop_compensation = line_drop_compensation

        # Built-in voltage transducer ratio.Built-in voltage transducer ratio. 
        self.pt_ratio = pt_ratio

        # Built-in current transducer ratio.Built-in current transducer ratio. 
        self.ct_ratio = ct_ratio

        # Line drop compensator resistance setting for reverse power flow.Line drop compensator resistance setting for reverse power flow. 
        self.reverse_line_drop_r = reverse_line_drop_r

        # Maximum allowed regulated voltage on the PT secondary base, regardless of line drop compensation. Sometimes referred to as first-house protection.Maximum allowed regulated voltage on the PT secondary base, regardless of line drop compensation. Sometimes referred to as first-house protection. 
        self.limit_voltage = limit_voltage

        # Line drop compensator reactance setting for reverse power flow.Line drop compensator reactance setting for reverse power flow. 
        self.reverse_line_drop_x = reverse_line_drop_x

        # Voltage range (max - min) on the PT secondary base, centered on 'targetVoltage'.Voltage range (max - min) on the PT secondary base, centered on 'targetVoltage'. 
        self.band_voltage = band_voltage

        # Target voltage on the PT secondary base.Target voltage on the PT secondary base. 
        self.target_voltage = target_voltage

        # Line drop compensator reactance setting for normal (forward) power flow.Line drop compensator reactance setting for normal (forward) power flow. 
        self.line_drop_x = line_drop_x



        super(DistributionTapChanger, self).__init__(**kw_args)
    # >>> distribution_tap_changer


    def __str__(self):
        """ Returns a string representation of the DistributionTapChanger.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< distribution_tap_changer.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the DistributionTapChanger.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "DistributionTapChanger", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:DistributionTapChanger.line_drop_r>%s</%s:DistributionTapChanger.line_drop_r>' % \
            (indent, ns_prefix, self.line_drop_r, ns_prefix)
        s += '%s<%s:DistributionTapChanger.monitored_phase>%s</%s:DistributionTapChanger.monitored_phase>' % \
            (indent, ns_prefix, self.monitored_phase, ns_prefix)
        s += '%s<%s:DistributionTapChanger.line_drop_compensation>%s</%s:DistributionTapChanger.line_drop_compensation>' % \
            (indent, ns_prefix, self.line_drop_compensation, ns_prefix)
        s += '%s<%s:DistributionTapChanger.pt_ratio>%s</%s:DistributionTapChanger.pt_ratio>' % \
            (indent, ns_prefix, self.pt_ratio, ns_prefix)
        s += '%s<%s:DistributionTapChanger.ct_ratio>%s</%s:DistributionTapChanger.ct_ratio>' % \
            (indent, ns_prefix, self.ct_ratio, ns_prefix)
        s += '%s<%s:DistributionTapChanger.reverse_line_drop_r>%s</%s:DistributionTapChanger.reverse_line_drop_r>' % \
            (indent, ns_prefix, self.reverse_line_drop_r, ns_prefix)
        s += '%s<%s:DistributionTapChanger.limit_voltage>%s</%s:DistributionTapChanger.limit_voltage>' % \
            (indent, ns_prefix, self.limit_voltage, ns_prefix)
        s += '%s<%s:DistributionTapChanger.reverse_line_drop_x>%s</%s:DistributionTapChanger.reverse_line_drop_x>' % \
            (indent, ns_prefix, self.reverse_line_drop_x, ns_prefix)
        s += '%s<%s:DistributionTapChanger.band_voltage>%s</%s:DistributionTapChanger.band_voltage>' % \
            (indent, ns_prefix, self.band_voltage, ns_prefix)
        s += '%s<%s:DistributionTapChanger.target_voltage>%s</%s:DistributionTapChanger.target_voltage>' % \
            (indent, ns_prefix, self.target_voltage, ns_prefix)
        s += '%s<%s:DistributionTapChanger.line_drop_x>%s</%s:DistributionTapChanger.line_drop_x>' % \
            (indent, ns_prefix, self.line_drop_x, ns_prefix)
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
        if self.sv_tap_step is not None:
            s += '%s<%s:TapChanger.sv_tap_step rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.sv_tap_step.uri)
        s += '%s<%s:TapChanger.step_voltage_increment>%s</%s:TapChanger.step_voltage_increment>' % \
            (indent, ns_prefix, self.step_voltage_increment, ns_prefix)
        s += '%s<%s:TapChanger.subsequent_delay>%s</%s:TapChanger.subsequent_delay>' % \
            (indent, ns_prefix, self.subsequent_delay, ns_prefix)
        s += '%s<%s:TapChanger.neutral_step>%s</%s:TapChanger.neutral_step>' % \
            (indent, ns_prefix, self.neutral_step, ns_prefix)
        s += '%s<%s:TapChanger.normal_step>%s</%s:TapChanger.normal_step>' % \
            (indent, ns_prefix, self.normal_step, ns_prefix)
        s += '%s<%s:TapChanger.ltc_flag>%s</%s:TapChanger.ltc_flag>' % \
            (indent, ns_prefix, self.ltc_flag, ns_prefix)
        s += '%s<%s:TapChanger.neutral_u>%s</%s:TapChanger.neutral_u>' % \
            (indent, ns_prefix, self.neutral_u, ns_prefix)
        s += '%s<%s:TapChanger.low_step>%s</%s:TapChanger.low_step>' % \
            (indent, ns_prefix, self.low_step, ns_prefix)
        s += '%s<%s:TapChanger.initial_delay>%s</%s:TapChanger.initial_delay>' % \
            (indent, ns_prefix, self.initial_delay, ns_prefix)
        s += '%s<%s:TapChanger.regulation_status>%s</%s:TapChanger.regulation_status>' % \
            (indent, ns_prefix, self.regulation_status, ns_prefix)
        s += '%s<%s:TapChanger.high_step>%s</%s:TapChanger.high_step>' % \
            (indent, ns_prefix, self.high_step, ns_prefix)
        if self.winding is not None:
            s += '%s<%s:RatioTapChanger.winding rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.winding.uri)
        s += '%s<%s:RatioTapChanger.tcul_control_mode>%s</%s:RatioTapChanger.tcul_control_mode>' % \
            (indent, ns_prefix, self.tcul_control_mode, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "DistributionTapChanger")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> distribution_tap_changer.serialize


class PerLengthSequenceImpedance(IdentifiedObject):
    """ Sequence impedance and admittance parameters per unit length, for transposed lines of 1, 2, or 3 phases. For 1-phase lines, define x=x0=xself. For 2-phase lines, define x=xs-xm and x0=xs+xm.Sequence impedance and admittance parameters per unit length, for transposed lines of 1, 2, or 3 phases. For 1-phase lines, define x=x0=xself. For 2-phase lines, define x=xs-xm and x0=xs+xm.
    """
    # <<< per_length_sequence_impedance
    # @generated
    def __init__(self, x=0.0, gch=0.0, r0=0.0, x0=0.0, g0ch=0.0, b0ch=0.0, r=0.0, bch=0.0, conductor_segments=None, **kw_args):
        """ Initialises a new 'PerLengthSequenceImpedance' instance.
        """
        # Positive sequence series reactance, per unit of length.Positive sequence series reactance, per unit of length. 
        self.x = x

        # Positive sequence shunt (charging) conductance, per unit of length.Positive sequence shunt (charging) conductance, per unit of length. 
        self.gch = gch

        # Zero sequence series resistance, per unit of length.Zero sequence series resistance, per unit of length. 
        self.r0 = r0

        # Zero sequence series reactance, per unit of length.Zero sequence series reactance, per unit of length. 
        self.x0 = x0

        # Zero sequence shunt (charging) conductance, per unit of length.Zero sequence shunt (charging) conductance, per unit of length. 
        self.g0ch = g0ch

        # Zero sequence shunt (charging) susceptance, per unit of length.Zero sequence shunt (charging) susceptance, per unit of length. 
        self.b0ch = b0ch

        # Positive sequence series resistance, per unit of length.Positive sequence series resistance, per unit of length. 
        self.r = r

        # Positive sequence shunt (charging) susceptance, per unit of length.Positive sequence shunt (charging) susceptance, per unit of length. 
        self.bch = bch


        self._conductor_segments = []
        if conductor_segments is not None:
            self.conductor_segments = conductor_segments
        else:
            self.conductor_segments = []


        super(PerLengthSequenceImpedance, self).__init__(**kw_args)
    # >>> per_length_sequence_impedance

    # <<< conductor_segments
    # @generated
    def get_conductor_segments(self):
        """ All conductor segments described by this sequence impedance.All conductor segments described by this sequence impedance.
        """
        return self._conductor_segments

    def set_conductor_segments(self, value):
        for x in self._conductor_segments:
            x._sequence_impedance = None
        for y in value:
            y._sequence_impedance = self
        self._conductor_segments = value

    conductor_segments = property(get_conductor_segments, set_conductor_segments)

    def add_conductor_segments(self, *conductor_segments):
        for obj in conductor_segments:
            obj._sequence_impedance = self
            self._conductor_segments.append(obj)

    def remove_conductor_segments(self, *conductor_segments):
        for obj in conductor_segments:
            obj._sequence_impedance = None
            self._conductor_segments.remove(obj)
    # >>> conductor_segments


    def __str__(self):
        """ Returns a string representation of the PerLengthSequenceImpedance.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< per_length_sequence_impedance.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PerLengthSequenceImpedance.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PerLengthSequenceImpedance", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.conductor_segments:
            s += '%s<%s:PerLengthSequenceImpedance.conductor_segments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:PerLengthSequenceImpedance.x>%s</%s:PerLengthSequenceImpedance.x>' % \
            (indent, ns_prefix, self.x, ns_prefix)
        s += '%s<%s:PerLengthSequenceImpedance.gch>%s</%s:PerLengthSequenceImpedance.gch>' % \
            (indent, ns_prefix, self.gch, ns_prefix)
        s += '%s<%s:PerLengthSequenceImpedance.r0>%s</%s:PerLengthSequenceImpedance.r0>' % \
            (indent, ns_prefix, self.r0, ns_prefix)
        s += '%s<%s:PerLengthSequenceImpedance.x0>%s</%s:PerLengthSequenceImpedance.x0>' % \
            (indent, ns_prefix, self.x0, ns_prefix)
        s += '%s<%s:PerLengthSequenceImpedance.g0ch>%s</%s:PerLengthSequenceImpedance.g0ch>' % \
            (indent, ns_prefix, self.g0ch, ns_prefix)
        s += '%s<%s:PerLengthSequenceImpedance.b0ch>%s</%s:PerLengthSequenceImpedance.b0ch>' % \
            (indent, ns_prefix, self.b0ch, ns_prefix)
        s += '%s<%s:PerLengthSequenceImpedance.r>%s</%s:PerLengthSequenceImpedance.r>' % \
            (indent, ns_prefix, self.r, ns_prefix)
        s += '%s<%s:PerLengthSequenceImpedance.bch>%s</%s:PerLengthSequenceImpedance.bch>' % \
            (indent, ns_prefix, self.bch, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "PerLengthSequenceImpedance")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> per_length_sequence_impedance.serialize


class TransformerBank(Equipment):
    """ An assembly of transformers that are connected together. For three-phase transformers, there would be one transformer per bank. For banks of single-phase transformers, there will be more than one transformer per bank, and they need not be identical.An assembly of transformers that are connected together. For three-phase transformers, there would be one transformer per bank. For banks of single-phase transformers, there will be more than one transformer per bank, and they need not be identical.
    """
    # <<< transformer_bank
    # @generated
    def __init__(self, vector_group='', transformers=None, **kw_args):
        """ Initialises a new 'TransformerBank' instance.
        """
        # Vector group of the bank for protective relaying, e.g., Dyn1. For unbalanced transformers, this may not be simply determined from the constituent winding connections.Vector group of the bank for protective relaying, e.g., Dyn1. For unbalanced transformers, this may not be simply determined from the constituent winding connections. 
        self.vector_group = vector_group


        self._transformers = []
        if transformers is not None:
            self.transformers = transformers
        else:
            self.transformers = []


        super(TransformerBank, self).__init__(**kw_args)
    # >>> transformer_bank

    # <<< transformers
    # @generated
    def get_transformers(self):
        """ All transformers that belong to this bank.All transformers that belong to this bank.
        """
        return self._transformers

    def set_transformers(self, value):
        for x in self._transformers:
            x._transformer_bank = None
        for y in value:
            y._transformer_bank = self
        self._transformers = value

    transformers = property(get_transformers, set_transformers)

    def add_transformers(self, *transformers):
        for obj in transformers:
            obj._transformer_bank = self
            self._transformers.append(obj)

    def remove_transformers(self, *transformers):
        for obj in transformers:
            obj._transformer_bank = None
            self._transformers.remove(obj)
    # >>> transformers


    def __str__(self):
        """ Returns a string representation of the TransformerBank.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< transformer_bank.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TransformerBank.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TransformerBank", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.transformers:
            s += '%s<%s:TransformerBank.transformers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:TransformerBank.vector_group>%s</%s:TransformerBank.vector_group>' % \
            (indent, ns_prefix, self.vector_group, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "TransformerBank")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> transformer_bank.serialize


class PerLengthPhaseImpedance(IdentifiedObject):
    """ Impedance and admittance parameters per unit length for n-wire unbalanced lines, in matrix form.Impedance and admittance parameters per unit length for n-wire unbalanced lines, in matrix form.
    """
    # <<< per_length_phase_impedance
    # @generated
    def __init__(self, conductor_count=0, phase_impedance_data=None, conductor_segments=None, **kw_args):
        """ Initialises a new 'PerLengthPhaseImpedance' instance.
        """
        # Number of phase, neutral, and other wires retained. Constrains the number of matrix elements and the phase codes that can be used with this matrix.Number of phase, neutral, and other wires retained. Constrains the number of matrix elements and the phase codes that can be used with this matrix. 
        self.conductor_count = conductor_count


        self._phase_impedance_data = []
        if phase_impedance_data is not None:
            self.phase_impedance_data = phase_impedance_data
        else:
            self.phase_impedance_data = []

        self._conductor_segments = []
        if conductor_segments is not None:
            self.conductor_segments = conductor_segments
        else:
            self.conductor_segments = []


        super(PerLengthPhaseImpedance, self).__init__(**kw_args)
    # >>> per_length_phase_impedance

    # <<< phase_impedance_data
    # @generated
    def get_phase_impedance_data(self):
        """ All data that belong to this conductor phase impedance.All data that belong to this conductor phase impedance.
        """
        return self._phase_impedance_data

    def set_phase_impedance_data(self, value):
        for x in self._phase_impedance_data:
            x._phase_impedance = None
        for y in value:
            y._phase_impedance = self
        self._phase_impedance_data = value

    phase_impedance_data = property(get_phase_impedance_data, set_phase_impedance_data)

    def add_phase_impedance_data(self, *phase_impedance_data):
        for obj in phase_impedance_data:
            obj._phase_impedance = self
            self._phase_impedance_data.append(obj)

    def remove_phase_impedance_data(self, *phase_impedance_data):
        for obj in phase_impedance_data:
            obj._phase_impedance = None
            self._phase_impedance_data.remove(obj)
    # >>> phase_impedance_data

    # <<< conductor_segments
    # @generated
    def get_conductor_segments(self):
        """ All conductor segments described by this phase impedance.All conductor segments described by this phase impedance.
        """
        return self._conductor_segments

    def set_conductor_segments(self, value):
        for x in self._conductor_segments:
            x._phase_impedance = None
        for y in value:
            y._phase_impedance = self
        self._conductor_segments = value

    conductor_segments = property(get_conductor_segments, set_conductor_segments)

    def add_conductor_segments(self, *conductor_segments):
        for obj in conductor_segments:
            obj._phase_impedance = self
            self._conductor_segments.append(obj)

    def remove_conductor_segments(self, *conductor_segments):
        for obj in conductor_segments:
            obj._phase_impedance = None
            self._conductor_segments.remove(obj)
    # >>> conductor_segments


    def __str__(self):
        """ Returns a string representation of the PerLengthPhaseImpedance.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< per_length_phase_impedance.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PerLengthPhaseImpedance.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PerLengthPhaseImpedance", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.phase_impedance_data:
            s += '%s<%s:PerLengthPhaseImpedance.phase_impedance_data rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.conductor_segments:
            s += '%s<%s:PerLengthPhaseImpedance.conductor_segments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:PerLengthPhaseImpedance.conductor_count>%s</%s:PerLengthPhaseImpedance.conductor_count>' % \
            (indent, ns_prefix, self.conductor_count, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "PerLengthPhaseImpedance")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> per_length_phase_impedance.serialize


class DistributionTransformer(Equipment):
    """ An assembly of two or more coupled windings that transform electrical power between voltage levels. Supports both balanced and unbalanced winding connections. This class differs from Wires::PowerTransformer as follows: - it is part of a TransformerBank - it draws parameters exclusively from TransformerInfo and its associated classes.An assembly of two or more coupled windings that transform electrical power between voltage levels. Supports both balanced and unbalanced winding connections. This class differs from Wires::PowerTransformer as follows: - it is part of a TransformerBank - it draws parameters exclusively from TransformerInfo and its associated classes.
    """
    # <<< distribution_transformer
    # @generated
    def __init__(self, transformer_info=None, windings=None, transformer_bank=None, **kw_args):
        """ Initialises a new 'DistributionTransformer' instance.
        """

        self._transformer_info = None
        self.transformer_info = transformer_info

        self._windings = []
        if windings is not None:
            self.windings = windings
        else:
            self.windings = []

        self._transformer_bank = None
        self.transformer_bank = transformer_bank


        super(DistributionTransformer, self).__init__(**kw_args)
    # >>> distribution_transformer

    # <<< transformer_info
    # @generated
    def get_transformer_info(self):
        """ Transformer data.Transformer data.
        """
        return self._transformer_info

    def set_transformer_info(self, value):
        if self._transformer_info is not None:
            filtered = [x for x in self.transformer_info.transformers if x != self]
            self._transformer_info._transformers = filtered

        self._transformer_info = value
        if self._transformer_info is not None:
            self._transformer_info._transformers.append(self)

    transformer_info = property(get_transformer_info, set_transformer_info)
    # >>> transformer_info

    # <<< windings
    # @generated
    def get_windings(self):
        """ All windings of this transformer.All windings of this transformer.
        """
        return self._windings

    def set_windings(self, value):
        for x in self._windings:
            x._transformer = None
        for y in value:
            y._transformer = self
        self._windings = value

    windings = property(get_windings, set_windings)

    def add_windings(self, *windings):
        for obj in windings:
            obj._transformer = self
            self._windings.append(obj)

    def remove_windings(self, *windings):
        for obj in windings:
            obj._transformer = None
            self._windings.remove(obj)
    # >>> windings

    # <<< transformer_bank
    # @generated
    def get_transformer_bank(self):
        """ Bank this transformer belongs to.Bank this transformer belongs to.
        """
        return self._transformer_bank

    def set_transformer_bank(self, value):
        if self._transformer_bank is not None:
            filtered = [x for x in self.transformer_bank.transformers if x != self]
            self._transformer_bank._transformers = filtered

        self._transformer_bank = value
        if self._transformer_bank is not None:
            self._transformer_bank._transformers.append(self)

    transformer_bank = property(get_transformer_bank, set_transformer_bank)
    # >>> transformer_bank


    def __str__(self):
        """ Returns a string representation of the DistributionTransformer.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< distribution_transformer.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the DistributionTransformer.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "DistributionTransformer", self.uri)
        if format:
            indent += ' ' * depth

        if self.transformer_info is not None:
            s += '%s<%s:DistributionTransformer.transformer_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.transformer_info.uri)
        for obj in self.windings:
            s += '%s<%s:DistributionTransformer.windings rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.transformer_bank is not None:
            s += '%s<%s:DistributionTransformer.transformer_bank rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.transformer_bank.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "DistributionTransformer")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> distribution_transformer.serialize


class PhaseImpedanceData(Element):
    """ Triplet of resistance, reactance, and susceptance matrix element values.Triplet of resistance, reactance, and susceptance matrix element values.
    """
    # <<< phase_impedance_data
    # @generated
    def __init__(self, x=0.0, sequence_number=0, b=0.0, r=0.0, phase_impedance=None, **kw_args):
        """ Initialises a new 'PhaseImpedanceData' instance.
        """
        # Reactance matrix element value, per length of unit.Reactance matrix element value, per length of unit. 
        self.x = x

        # Column-wise element index, assuming a symmetrical matrix. Ranges from 1 to N + N*(N-1)/2.Column-wise element index, assuming a symmetrical matrix. Ranges from 1 to N + N*(N-1)/2. 
        self.sequence_number = sequence_number

        # Susceptance matrix element value, per length of unit.Susceptance matrix element value, per length of unit. 
        self.b = b

        # Resistance matrix element value, per length of unit.Resistance matrix element value, per length of unit. 
        self.r = r


        self._phase_impedance = None
        self.phase_impedance = phase_impedance


        super(PhaseImpedanceData, self).__init__(**kw_args)
    # >>> phase_impedance_data

    # <<< phase_impedance
    # @generated
    def get_phase_impedance(self):
        """ Conductor phase impedance to which this data belongs.Conductor phase impedance to which this data belongs.
        """
        return self._phase_impedance

    def set_phase_impedance(self, value):
        if self._phase_impedance is not None:
            filtered = [x for x in self.phase_impedance.phase_impedance_data if x != self]
            self._phase_impedance._phase_impedance_data = filtered

        self._phase_impedance = value
        if self._phase_impedance is not None:
            self._phase_impedance._phase_impedance_data.append(self)

    phase_impedance = property(get_phase_impedance, set_phase_impedance)
    # >>> phase_impedance


    def __str__(self):
        """ Returns a string representation of the PhaseImpedanceData.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< phase_impedance_data.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PhaseImpedanceData.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PhaseImpedanceData", self.uri)
        if format:
            indent += ' ' * depth

        if self.phase_impedance is not None:
            s += '%s<%s:PhaseImpedanceData.phase_impedance rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.phase_impedance.uri)
        s += '%s<%s:PhaseImpedanceData.x>%s</%s:PhaseImpedanceData.x>' % \
            (indent, ns_prefix, self.x, ns_prefix)
        s += '%s<%s:PhaseImpedanceData.sequence_number>%s</%s:PhaseImpedanceData.sequence_number>' % \
            (indent, ns_prefix, self.sequence_number, ns_prefix)
        s += '%s<%s:PhaseImpedanceData.b>%s</%s:PhaseImpedanceData.b>' % \
            (indent, ns_prefix, self.b, ns_prefix)
        s += '%s<%s:PhaseImpedanceData.r>%s</%s:PhaseImpedanceData.r>' % \
            (indent, ns_prefix, self.r, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PhaseImpedanceData")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> phase_impedance_data.serialize


# <<< wires_ext
# @generated
# >>> wires_ext
