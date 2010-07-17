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

""" This package is an extension of Assets package and contains the core information classes that support asset management and different network and work planning applications with specialized documentation classes describing assets of a particular product model made by a manufacturer. There are typically many instances of an asset associated with a single asset model. It also contains 'lightweight' *Info classes, which hold model attributes that can be referenced by not only Assets but also by ConductingEquipments.This package is an extension of Assets package and contains the core information classes that support asset management and different network and work planning applications with specialized documentation classes describing assets of a particular product model made by a manufacturer. There are typically many instances of an asset associated with a single asset model. It also contains 'lightweight' *Info classes, which hold model attributes that can be referenced by not only Assets but also by ConductingEquipments.
"""

from cdpsm.iec61970.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_AssetModels"

class TransformerInfo(IdentifiedObject):
    """ Set of transformer data, from an equipment library.Set of transformer data, from an equipment library.
    """
    # <<< transformer_info
    # @generated
    def __init__(self, transformers=None, winding_infos=None, **kw_args):
        """ Initialises a new 'TransformerInfo' instance.
        """

        self._transformers = []
        if transformers is not None:
            self.transformers = transformers
        else:
            self.transformers = []

        self._winding_infos = []
        if winding_infos is not None:
            self.winding_infos = winding_infos
        else:
            self.winding_infos = []


        super(TransformerInfo, self).__init__(**kw_args)
    # >>> transformer_info

    # <<< transformers
    # @generated
    def get_transformers(self):
        """ All transformers that can be described with this transformer data.All transformers that can be described with this transformer data.
        """
        return self._transformers

    def set_transformers(self, value):
        for x in self._transformers:
            x._transformer_info = None
        for y in value:
            y._transformer_info = self
        self._transformers = value

    transformers = property(get_transformers, set_transformers)

    def add_transformers(self, *transformers):
        for obj in transformers:
            obj._transformer_info = self
            self._transformers.append(obj)

    def remove_transformers(self, *transformers):
        for obj in transformers:
            obj._transformer_info = None
            self._transformers.remove(obj)
    # >>> transformers

    # <<< winding_infos
    # @generated
    def get_winding_infos(self):
        """ Data for all the windings described by this transformer data.Data for all the windings described by this transformer data.
        """
        return self._winding_infos

    def set_winding_infos(self, value):
        for x in self._winding_infos:
            x._transformer_info = None
        for y in value:
            y._transformer_info = self
        self._winding_infos = value

    winding_infos = property(get_winding_infos, set_winding_infos)

    def add_winding_infos(self, *winding_infos):
        for obj in winding_infos:
            obj._transformer_info = self
            self._winding_infos.append(obj)

    def remove_winding_infos(self, *winding_infos):
        for obj in winding_infos:
            obj._transformer_info = None
            self._winding_infos.remove(obj)
    # >>> winding_infos


    def __str__(self):
        """ Returns a string representation of the TransformerInfo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< transformer_info.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TransformerInfo.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TransformerInfo", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.transformers:
            s += '%s<%s:TransformerInfo.transformers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.winding_infos:
            s += '%s<%s:TransformerInfo.winding_infos rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "TransformerInfo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> transformer_info.serialize


class ToWindingSpec(IdentifiedObject):
    """ For short-circuit tests, specifies the winding and tap for all short-circuited windings.  For open-circuit tests, specifies the winding, tap, induced voltage, and induced angle for any non-excited windings that were measured during the test. This won't apply if only the exciting current and no-load losses were measured.For short-circuit tests, specifies the winding and tap for all short-circuited windings.  For open-circuit tests, specifies the winding, tap, induced voltage, and induced angle for any non-excited windings that were measured during the test. This won't apply if only the exciting current and no-load losses were measured.
    """
    # <<< to_winding_spec
    # @generated
    def __init__(self, to_tap_step=0, voltage=0.0, phase_shift=0.0, open_circuit_tests=None, short_circuit_tests=None, to_winding=None, **kw_args):
        """ Initialises a new 'ToWindingSpec' instance.
        """
        # Tap step number for the 'to' winding of the test pair.Tap step number for the 'to' winding of the test pair. 
        self.to_tap_step = to_tap_step

        # (if open-circuit test) Voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.(if open-circuit test) Voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited. 
        self.voltage = voltage

        # (if open-circuit test) Phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.(if open-circuit test) Phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited. 
        self.phase_shift = phase_shift


        self._open_circuit_tests = []
        if open_circuit_tests is not None:
            self.open_circuit_tests = open_circuit_tests
        else:
            self.open_circuit_tests = []

        self._short_circuit_tests = []
        if short_circuit_tests is not None:
            self.short_circuit_tests = short_circuit_tests
        else:
            self.short_circuit_tests = []

        self._to_winding = None
        self.to_winding = to_winding


        super(ToWindingSpec, self).__init__(**kw_args)
    # >>> to_winding_spec

    # <<< open_circuit_tests
    # @generated
    def get_open_circuit_tests(self):
        """ All open-circuit tests in which this winding was measured.All open-circuit tests in which this winding was measured.
        """
        return self._open_circuit_tests

    def set_open_circuit_tests(self, value):
        for p in self._open_circuit_tests:
            filtered = [q for q in p.measured_winding_specs if q != self]
            self._open_circuit_tests._measured_winding_specs = filtered
        for r in value:
            if self not in r._measured_winding_specs:
                r._measured_winding_specs.append(self)
        self._open_circuit_tests = value

    open_circuit_tests = property(get_open_circuit_tests, set_open_circuit_tests)

    def add_open_circuit_tests(self, *open_circuit_tests):
        for obj in open_circuit_tests:
            if self not in obj._measured_winding_specs:
                obj._measured_winding_specs.append(self)
            self._open_circuit_tests.append(obj)

    def remove_open_circuit_tests(self, *open_circuit_tests):
        for obj in open_circuit_tests:
            if self in obj._measured_winding_specs:
                obj._measured_winding_specs.remove(self)
            self._open_circuit_tests.remove(obj)
    # >>> open_circuit_tests

    # <<< short_circuit_tests
    # @generated
    def get_short_circuit_tests(self):
        """ All short-circuit tests in which this winding was short-circuited.All short-circuit tests in which this winding was short-circuited.
        """
        return self._short_circuit_tests

    def set_short_circuit_tests(self, value):
        for p in self._short_circuit_tests:
            filtered = [q for q in p.shorted_winding_specs if q != self]
            self._short_circuit_tests._shorted_winding_specs = filtered
        for r in value:
            if self not in r._shorted_winding_specs:
                r._shorted_winding_specs.append(self)
        self._short_circuit_tests = value

    short_circuit_tests = property(get_short_circuit_tests, set_short_circuit_tests)

    def add_short_circuit_tests(self, *short_circuit_tests):
        for obj in short_circuit_tests:
            if self not in obj._shorted_winding_specs:
                obj._shorted_winding_specs.append(self)
            self._short_circuit_tests.append(obj)

    def remove_short_circuit_tests(self, *short_circuit_tests):
        for obj in short_circuit_tests:
            if self in obj._shorted_winding_specs:
                obj._shorted_winding_specs.remove(self)
            self._short_circuit_tests.remove(obj)
    # >>> short_circuit_tests

    # <<< to_winding
    # @generated
    def get_to_winding(self):
        """ Winding short-circuited in a short-circuit test, or measured for induced voltage and angle in an open-circuit test.Winding short-circuited in a short-circuit test, or measured for induced voltage and angle in an open-circuit test.
        """
        return self._to_winding

    def set_to_winding(self, value):
        if self._to_winding is not None:
            filtered = [x for x in self.to_winding.to_winding_specs if x != self]
            self._to_winding._to_winding_specs = filtered

        self._to_winding = value
        if self._to_winding is not None:
            self._to_winding._to_winding_specs.append(self)

    to_winding = property(get_to_winding, set_to_winding)
    # >>> to_winding


    def __str__(self):
        """ Returns a string representation of the ToWindingSpec.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< to_winding_spec.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ToWindingSpec.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ToWindingSpec", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.open_circuit_tests:
            s += '%s<%s:ToWindingSpec.open_circuit_tests rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.short_circuit_tests:
            s += '%s<%s:ToWindingSpec.short_circuit_tests rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.to_winding is not None:
            s += '%s<%s:ToWindingSpec.to_winding rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.to_winding.uri)
        s += '%s<%s:ToWindingSpec.to_tap_step>%s</%s:ToWindingSpec.to_tap_step>' % \
            (indent, ns_prefix, self.to_tap_step, ns_prefix)
        s += '%s<%s:ToWindingSpec.voltage>%s</%s:ToWindingSpec.voltage>' % \
            (indent, ns_prefix, self.voltage, ns_prefix)
        s += '%s<%s:ToWindingSpec.phase_shift>%s</%s:ToWindingSpec.phase_shift>' % \
            (indent, ns_prefix, self.phase_shift, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ToWindingSpec")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> to_winding_spec.serialize


class WireArrangement(IdentifiedObject):
    """ Identification, spacing and configuration of the wires of a Conductor, with reference to their type.Identification, spacing and configuration of the wires of a Conductor, with reference to their type.
    """
    # <<< wire_arrangement
    # @generated
    def __init__(self, mounting_point_x=0.0, mounting_point_y=0.0, position=0, conductor_info=None, wire_type=None, **kw_args):
        """ Initialises a new 'WireArrangement' instance.
        """
        # Signed horizontal distance from the first wire to a common reference point.Signed horizontal distance from the first wire to a common reference point. 
        self.mounting_point_x = mounting_point_x

        # Height above ground of the first wire.Height above ground of the first wire. 
        self.mounting_point_y = mounting_point_y

        # Position number on the structure corresponding to this wire. For example, use 1..3 for phases and 4 for the neutral on a 3-phase structure. The individual phase assignments matter; for example, ABC will produce a different set of unbalanced line parameters, by phase, than BAC.Position number on the structure corresponding to this wire. For example, use 1..3 for phases and 4 for the neutral on a 3-phase structure. The individual phase assignments matter; for example, ABC will produce a different set of unbalanced line parameters, by phase, than BAC. 
        self.position = position


        self._conductor_info = None
        self.conductor_info = conductor_info

        self._wire_type = None
        self.wire_type = wire_type


        super(WireArrangement, self).__init__(**kw_args)
    # >>> wire_arrangement

    # <<< conductor_info
    # @generated
    def get_conductor_info(self):
        """ Conductor data this wire arrangement belongs to.Conductor data this wire arrangement belongs to.
        """
        return self._conductor_info

    def set_conductor_info(self, value):
        if self._conductor_info is not None:
            filtered = [x for x in self.conductor_info.wire_arrangements if x != self]
            self._conductor_info._wire_arrangements = filtered

        self._conductor_info = value
        if self._conductor_info is not None:
            self._conductor_info._wire_arrangements.append(self)

    conductor_info = property(get_conductor_info, set_conductor_info)
    # >>> conductor_info

    # <<< wire_type
    # @generated
    def get_wire_type(self):
        """ Wire type used for this wire arrangement.Wire type used for this wire arrangement.
        """
        return self._wire_type

    def set_wire_type(self, value):
        if self._wire_type is not None:
            filtered = [x for x in self.wire_type.wire_arrangements if x != self]
            self._wire_type._wire_arrangements = filtered

        self._wire_type = value
        if self._wire_type is not None:
            self._wire_type._wire_arrangements.append(self)

    wire_type = property(get_wire_type, set_wire_type)
    # >>> wire_type


    def __str__(self):
        """ Returns a string representation of the WireArrangement.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< wire_arrangement.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the WireArrangement.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "WireArrangement", self.uri)
        if format:
            indent += ' ' * depth

        if self.conductor_info is not None:
            s += '%s<%s:WireArrangement.conductor_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conductor_info.uri)
        if self.wire_type is not None:
            s += '%s<%s:WireArrangement.wire_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.wire_type.uri)
        s += '%s<%s:WireArrangement.mounting_point_x>%s</%s:WireArrangement.mounting_point_x>' % \
            (indent, ns_prefix, self.mounting_point_x, ns_prefix)
        s += '%s<%s:WireArrangement.mounting_point_y>%s</%s:WireArrangement.mounting_point_y>' % \
            (indent, ns_prefix, self.mounting_point_y, ns_prefix)
        s += '%s<%s:WireArrangement.position>%s</%s:WireArrangement.position>' % \
            (indent, ns_prefix, self.position, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "WireArrangement")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> wire_arrangement.serialize


class ConductorInfo(IdentifiedObject):
    """ Conductor data.Conductor data.
    """
    # <<< conductor_info
    # @generated
    def __init__(self, phase_count=0, insulation_material='crosslinked_polyethylene', insulation_thickness=0.0, insulated=False, usage='secondary', wire_arrangements=None, conductor_segments=None, **kw_args):
        """ Initialises a new 'ConductorInfo' instance.
        """
        # Number of phases (including neutral) to be retained. Any wires beyond this number should be reduced into the earth return.Number of phases (including neutral) to be retained. Any wires beyond this number should be reduced into the earth return. 
        self.phase_count = phase_count

        # (if insulated conductor) Material used for insulation.(if insulated conductor) Material used for insulation. Values are: "crosslinked_polyethylene", "butyl", "tree_retardant_crosslinked_polyethylene", "asbestos_and_varnished_cambric", "high_pressure_fluid_filled", "ethylene_propylene_rubber", "ozone_resistant_rubber", "oil_paper", "varnished_dacron_glass", "high_molecular_weight_polyethylene", "other", "varnished_cambric_cloth", "tree_resistant_high_molecular_weight_polyethylene", "unbelted_pilc", "belted_pilc", "rubber", "low_capacitance_rubber", "silicon_rubber"
        self.insulation_material = 'crosslinked_polyethylene'

        # (if insulated conductor) Thickness of the insulation.(if insulated conductor) Thickness of the insulation. 
        self.insulation_thickness = insulation_thickness

        # True if conductor is insulated.True if conductor is insulated. 
        self.insulated = insulated

        # Usage of this conductor.Usage of this conductor. Values are: "secondary", "other", "distribution", "transmission"
        self.usage = 'secondary'


        self._wire_arrangements = []
        if wire_arrangements is not None:
            self.wire_arrangements = wire_arrangements
        else:
            self.wire_arrangements = []

        self._conductor_segments = []
        if conductor_segments is not None:
            self.conductor_segments = conductor_segments
        else:
            self.conductor_segments = []


        super(ConductorInfo, self).__init__(**kw_args)
    # >>> conductor_info

    # <<< wire_arrangements
    # @generated
    def get_wire_arrangements(self):
        """ All wire arrangements (single wires) that make this conductor.All wire arrangements (single wires) that make this conductor.
        """
        return self._wire_arrangements

    def set_wire_arrangements(self, value):
        for x in self._wire_arrangements:
            x._conductor_info = None
        for y in value:
            y._conductor_info = self
        self._wire_arrangements = value

    wire_arrangements = property(get_wire_arrangements, set_wire_arrangements)

    def add_wire_arrangements(self, *wire_arrangements):
        for obj in wire_arrangements:
            obj._conductor_info = self
            self._wire_arrangements.append(obj)

    def remove_wire_arrangements(self, *wire_arrangements):
        for obj in wire_arrangements:
            obj._conductor_info = None
            self._wire_arrangements.remove(obj)
    # >>> wire_arrangements

    # <<< conductor_segments
    # @generated
    def get_conductor_segments(self):
        """ All conductor segments described by this conductor data.All conductor segments described by this conductor data.
        """
        return self._conductor_segments

    def set_conductor_segments(self, value):
        for x in self._conductor_segments:
            x._conductor_info = None
        for y in value:
            y._conductor_info = self
        self._conductor_segments = value

    conductor_segments = property(get_conductor_segments, set_conductor_segments)

    def add_conductor_segments(self, *conductor_segments):
        for obj in conductor_segments:
            obj._conductor_info = self
            self._conductor_segments.append(obj)

    def remove_conductor_segments(self, *conductor_segments):
        for obj in conductor_segments:
            obj._conductor_info = None
            self._conductor_segments.remove(obj)
    # >>> conductor_segments


    def __str__(self):
        """ Returns a string representation of the ConductorInfo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< conductor_info.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ConductorInfo.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ConductorInfo", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.wire_arrangements:
            s += '%s<%s:ConductorInfo.wire_arrangements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.conductor_segments:
            s += '%s<%s:ConductorInfo.conductor_segments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ConductorInfo.phase_count>%s</%s:ConductorInfo.phase_count>' % \
            (indent, ns_prefix, self.phase_count, ns_prefix)
        s += '%s<%s:ConductorInfo.insulation_material>%s</%s:ConductorInfo.insulation_material>' % \
            (indent, ns_prefix, self.insulation_material, ns_prefix)
        s += '%s<%s:ConductorInfo.insulation_thickness>%s</%s:ConductorInfo.insulation_thickness>' % \
            (indent, ns_prefix, self.insulation_thickness, ns_prefix)
        s += '%s<%s:ConductorInfo.insulated>%s</%s:ConductorInfo.insulated>' % \
            (indent, ns_prefix, self.insulated, ns_prefix)
        s += '%s<%s:ConductorInfo.usage>%s</%s:ConductorInfo.usage>' % \
            (indent, ns_prefix, self.usage, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ConductorInfo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> conductor_info.serialize


class DistributionWindingTest(IdentifiedObject):
    """ Test results for one or more transformer windings. These may include short-circuit or open-circuit (excitation) tests. Short-circuit test results include load losses and leakage impedances. Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence.Test results for one or more transformer windings. These may include short-circuit or open-circuit (excitation) tests. Short-circuit test results include load losses and leakage impedances. Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence.
    """
    # <<< distribution_winding_test
    # @generated
    def __init__(self, from_tap_step=0, from_winding=None, **kw_args):
        """ Initialises a new 'DistributionWindingTest' instance.
        """
        # Tap step number for the 'from' winding of the test pair.Tap step number for the 'from' winding of the test pair. 
        self.from_tap_step = from_tap_step


        self._from_winding = None
        self.from_winding = from_winding


        super(DistributionWindingTest, self).__init__(**kw_args)
    # >>> distribution_winding_test

    # <<< from_winding
    # @generated
    def get_from_winding(self):
        """ Winding that voltage or current is applied to during the test.Winding that voltage or current is applied to during the test.
        """
        return self._from_winding

    def set_from_winding(self, value):
        if self._from_winding is not None:
            filtered = [x for x in self.from_winding.winding_tests if x != self]
            self._from_winding._winding_tests = filtered

        self._from_winding = value
        if self._from_winding is not None:
            self._from_winding._winding_tests.append(self)

    from_winding = property(get_from_winding, set_from_winding)
    # >>> from_winding


    def __str__(self):
        """ Returns a string representation of the DistributionWindingTest.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< distribution_winding_test.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the DistributionWindingTest.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "DistributionWindingTest", self.uri)
        if format:
            indent += ' ' * depth

        if self.from_winding is not None:
            s += '%s<%s:DistributionWindingTest.from_winding rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.from_winding.uri)
        s += '%s<%s:DistributionWindingTest.from_tap_step>%s</%s:DistributionWindingTest.from_tap_step>' % \
            (indent, ns_prefix, self.from_tap_step, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "DistributionWindingTest")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> distribution_winding_test.serialize


class WireType(IdentifiedObject):
    """ Wire conductor (per IEEE specs). A specific type of wire or combination of wires, not insulated from each other, suitable for carrying electrical current.Wire conductor (per IEEE specs). A specific type of wire or combination of wires, not insulated from each other, suitable for carrying electrical current.
    """
    # <<< wire_type
    # @generated
    def __init__(self, r_ac75=0.0, core_radius=0.0, core_strand_count=0, r_ac25=0.0, radius=0.0, gmr=0.0, r_dc20=0.0, r_ac50=0.0, material='steel', size_description='', strand_count=0, rated_current=0.0, concentric_neutral_cable_infos=None, wire_arrangements=None, **kw_args):
        """ Initialises a new 'WireType' instance.
        """
        # AC resistance per unit length of the conductor at 75 degrees C.AC resistance per unit length of the conductor at 75 degrees C. 
        self.r_ac75 = r_ac75

        # (if there is a different core material) Radius of the central core.(if there is a different core material) Radius of the central core. 
        self.core_radius = core_radius

        # (if used) Number of strands in the steel core.(if used) Number of strands in the steel core. 
        self.core_strand_count = core_strand_count

        # AC resistance per unit length of the conductor at 25 degrees C.AC resistance per unit length of the conductor at 25 degrees C. 
        self.r_ac25 = r_ac25

        # Outside radius of the wire.Outside radius of the wire. 
        self.radius = radius

        # Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor.Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor. 
        self.gmr = gmr

        # DC resistance per unit length of the conductor at 20 degrees C.DC resistance per unit length of the conductor at 20 degrees C. 
        self.r_dc20 = r_dc20

        # AC resistance per unit length of the conductor at 50 degrees C.AC resistance per unit length of the conductor at 50 degrees C. 
        self.r_ac50 = r_ac50

        # Wire material.Wire material. Values are: "steel", "other", "aluminum", "copper", "acsr"
        self.material = 'steel'

        # Describes the wire guage or cross section (e.g., 4/0, #2, 336.5).Describes the wire guage or cross section (e.g., 4/0, #2, 336.5). 
        self.size_description = size_description

        # Number of strands in the wire.Number of strands in the wire. 
        self.strand_count = strand_count

        # Current carrying capacity of the wire under stated thermal conditions.Current carrying capacity of the wire under stated thermal conditions. 
        self.rated_current = rated_current


        self._concentric_neutral_cable_infos = []
        if concentric_neutral_cable_infos is not None:
            self.concentric_neutral_cable_infos = concentric_neutral_cable_infos
        else:
            self.concentric_neutral_cable_infos = []

        self._wire_arrangements = []
        if wire_arrangements is not None:
            self.wire_arrangements = wire_arrangements
        else:
            self.wire_arrangements = []


        super(WireType, self).__init__(**kw_args)
    # >>> wire_type

    # <<< concentric_neutral_cable_infos
    # @generated
    def get_concentric_neutral_cable_infos(self):
        """ All concentric neutral cables using this wire type.All concentric neutral cables using this wire type.
        """
        return self._concentric_neutral_cable_infos

    def set_concentric_neutral_cable_infos(self, value):
        for x in self._concentric_neutral_cable_infos:
            x._wire_type = None
        for y in value:
            y._wire_type = self
        self._concentric_neutral_cable_infos = value

    concentric_neutral_cable_infos = property(get_concentric_neutral_cable_infos, set_concentric_neutral_cable_infos)

    def add_concentric_neutral_cable_infos(self, *concentric_neutral_cable_infos):
        for obj in concentric_neutral_cable_infos:
            obj._wire_type = self
            self._concentric_neutral_cable_infos.append(obj)

    def remove_concentric_neutral_cable_infos(self, *concentric_neutral_cable_infos):
        for obj in concentric_neutral_cable_infos:
            obj._wire_type = None
            self._concentric_neutral_cable_infos.remove(obj)
    # >>> concentric_neutral_cable_infos

    # <<< wire_arrangements
    # @generated
    def get_wire_arrangements(self):
        """ All wire arrangements using this wire type.All wire arrangements using this wire type.
        """
        return self._wire_arrangements

    def set_wire_arrangements(self, value):
        for x in self._wire_arrangements:
            x._wire_type = None
        for y in value:
            y._wire_type = self
        self._wire_arrangements = value

    wire_arrangements = property(get_wire_arrangements, set_wire_arrangements)

    def add_wire_arrangements(self, *wire_arrangements):
        for obj in wire_arrangements:
            obj._wire_type = self
            self._wire_arrangements.append(obj)

    def remove_wire_arrangements(self, *wire_arrangements):
        for obj in wire_arrangements:
            obj._wire_type = None
            self._wire_arrangements.remove(obj)
    # >>> wire_arrangements


    def __str__(self):
        """ Returns a string representation of the WireType.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< wire_type.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the WireType.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "WireType", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.concentric_neutral_cable_infos:
            s += '%s<%s:WireType.concentric_neutral_cable_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.wire_arrangements:
            s += '%s<%s:WireType.wire_arrangements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:WireType.r_ac75>%s</%s:WireType.r_ac75>' % \
            (indent, ns_prefix, self.r_ac75, ns_prefix)
        s += '%s<%s:WireType.core_radius>%s</%s:WireType.core_radius>' % \
            (indent, ns_prefix, self.core_radius, ns_prefix)
        s += '%s<%s:WireType.core_strand_count>%s</%s:WireType.core_strand_count>' % \
            (indent, ns_prefix, self.core_strand_count, ns_prefix)
        s += '%s<%s:WireType.r_ac25>%s</%s:WireType.r_ac25>' % \
            (indent, ns_prefix, self.r_ac25, ns_prefix)
        s += '%s<%s:WireType.radius>%s</%s:WireType.radius>' % \
            (indent, ns_prefix, self.radius, ns_prefix)
        s += '%s<%s:WireType.gmr>%s</%s:WireType.gmr>' % \
            (indent, ns_prefix, self.gmr, ns_prefix)
        s += '%s<%s:WireType.r_dc20>%s</%s:WireType.r_dc20>' % \
            (indent, ns_prefix, self.r_dc20, ns_prefix)
        s += '%s<%s:WireType.r_ac50>%s</%s:WireType.r_ac50>' % \
            (indent, ns_prefix, self.r_ac50, ns_prefix)
        s += '%s<%s:WireType.material>%s</%s:WireType.material>' % \
            (indent, ns_prefix, self.material, ns_prefix)
        s += '%s<%s:WireType.size_description>%s</%s:WireType.size_description>' % \
            (indent, ns_prefix, self.size_description, ns_prefix)
        s += '%s<%s:WireType.strand_count>%s</%s:WireType.strand_count>' % \
            (indent, ns_prefix, self.strand_count, ns_prefix)
        s += '%s<%s:WireType.rated_current>%s</%s:WireType.rated_current>' % \
            (indent, ns_prefix, self.rated_current, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "WireType")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> wire_type.serialize


class WindingInfo(IdentifiedObject):
    """ Winding data.Winding data.
    """
    # <<< winding_info
    # @generated
    def __init__(self, sequence_number=0, rated_s=0.0, rated_u=0.0, connection_kind='i', emergency_s=0.0, r=0.0, phase_angle=0, insulation_u=0.0, short_term_s=0.0, winding_tests=None, to_winding_specs=None, transformer_info=None, windings=None, **kw_args):
        """ Initialises a new 'WindingInfo' instance.
        """
        # Sequence number for this winding, corresponding to the winding's order in the TransformerBank.vectorGroup attribute. Highest voltage winding should be '1'.Sequence number for this winding, corresponding to the winding's order in the TransformerBank.vectorGroup attribute. Highest voltage winding should be '1'. 
        self.sequence_number = sequence_number

        # Normal apparent power rating of this winding.Normal apparent power rating of this winding. 
        self.rated_s = rated_s

        # Rated voltage of this winding: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-phase windings.Rated voltage of this winding: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-phase windings. 
        self.rated_u = rated_u

        # Kind of connection of this winding.Kind of connection of this winding. Values are: "i", "z", "yn", "y", "a", "d", "zn"
        self.connection_kind = 'i'

        # Apparent power that the winding can carry under emergency conditions.Apparent power that the winding can carry under emergency conditions. 
        self.emergency_s = emergency_s

        # DC resistance of this winding.DC resistance of this winding. 
        self.r = r

        # Winding phase angle where 360 degrees are represented with clock hours, so the valid values are {0, ..., 11}. For example, to express winding code 'Dyn11', set attributes as follows: 'connectionKind' = Yn and 'phaseAngle' = 11.Winding phase angle where 360 degrees are represented with clock hours, so the valid values are {0, ..., 11}. For example, to express winding code 'Dyn11', set attributes as follows: 'connectionKind' = Yn and 'phaseAngle' = 11. 
        self.phase_angle = phase_angle

        # Basic insulation level voltage rating.Basic insulation level voltage rating. 
        self.insulation_u = insulation_u

        # Apparent power that this winding can carry for a short period of time.Apparent power that this winding can carry for a short period of time. 
        self.short_term_s = short_term_s


        self._winding_tests = []
        if winding_tests is not None:
            self.winding_tests = winding_tests
        else:
            self.winding_tests = []

        self._to_winding_specs = []
        if to_winding_specs is not None:
            self.to_winding_specs = to_winding_specs
        else:
            self.to_winding_specs = []

        self._transformer_info = None
        self.transformer_info = transformer_info

        self._windings = []
        if windings is not None:
            self.windings = windings
        else:
            self.windings = []


        super(WindingInfo, self).__init__(**kw_args)
    # >>> winding_info

    # <<< winding_tests
    # @generated
    def get_winding_tests(self):
        """ All winding tests during which voltage or current was applied to this winding.All winding tests during which voltage or current was applied to this winding.
        """
        return self._winding_tests

    def set_winding_tests(self, value):
        for x in self._winding_tests:
            x._from_winding = None
        for y in value:
            y._from_winding = self
        self._winding_tests = value

    winding_tests = property(get_winding_tests, set_winding_tests)

    def add_winding_tests(self, *winding_tests):
        for obj in winding_tests:
            obj._from_winding = self
            self._winding_tests.append(obj)

    def remove_winding_tests(self, *winding_tests):
        for obj in winding_tests:
            obj._from_winding = None
            self._winding_tests.remove(obj)
    # >>> winding_tests

    # <<< to_winding_specs
    # @generated
    def get_to_winding_specs(self):
        """ Tap steps and induced voltage/angle measurements for tests in which this winding was not excited.Tap steps and induced voltage/angle measurements for tests in which this winding was not excited.
        """
        return self._to_winding_specs

    def set_to_winding_specs(self, value):
        for x in self._to_winding_specs:
            x._to_winding = None
        for y in value:
            y._to_winding = self
        self._to_winding_specs = value

    to_winding_specs = property(get_to_winding_specs, set_to_winding_specs)

    def add_to_winding_specs(self, *to_winding_specs):
        for obj in to_winding_specs:
            obj._to_winding = self
            self._to_winding_specs.append(obj)

    def remove_to_winding_specs(self, *to_winding_specs):
        for obj in to_winding_specs:
            obj._to_winding = None
            self._to_winding_specs.remove(obj)
    # >>> to_winding_specs

    # <<< transformer_info
    # @generated
    def get_transformer_info(self):
        """ Transformer data that this winding description is part of.Transformer data that this winding description is part of.
        """
        return self._transformer_info

    def set_transformer_info(self, value):
        if self._transformer_info is not None:
            filtered = [x for x in self.transformer_info.winding_infos if x != self]
            self._transformer_info._winding_infos = filtered

        self._transformer_info = value
        if self._transformer_info is not None:
            self._transformer_info._winding_infos.append(self)

    transformer_info = property(get_transformer_info, set_transformer_info)
    # >>> transformer_info

    # <<< windings
    # @generated
    def get_windings(self):
        """ All windings described by this winding data.All windings described by this winding data.
        """
        return self._windings

    def set_windings(self, value):
        for x in self._windings:
            x._winding_info = None
        for y in value:
            y._winding_info = self
        self._windings = value

    windings = property(get_windings, set_windings)

    def add_windings(self, *windings):
        for obj in windings:
            obj._winding_info = self
            self._windings.append(obj)

    def remove_windings(self, *windings):
        for obj in windings:
            obj._winding_info = None
            self._windings.remove(obj)
    # >>> windings


    def __str__(self):
        """ Returns a string representation of the WindingInfo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< winding_info.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the WindingInfo.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "WindingInfo", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.winding_tests:
            s += '%s<%s:WindingInfo.winding_tests rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.to_winding_specs:
            s += '%s<%s:WindingInfo.to_winding_specs rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.transformer_info is not None:
            s += '%s<%s:WindingInfo.transformer_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.transformer_info.uri)
        for obj in self.windings:
            s += '%s<%s:WindingInfo.windings rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:WindingInfo.sequence_number>%s</%s:WindingInfo.sequence_number>' % \
            (indent, ns_prefix, self.sequence_number, ns_prefix)
        s += '%s<%s:WindingInfo.rated_s>%s</%s:WindingInfo.rated_s>' % \
            (indent, ns_prefix, self.rated_s, ns_prefix)
        s += '%s<%s:WindingInfo.rated_u>%s</%s:WindingInfo.rated_u>' % \
            (indent, ns_prefix, self.rated_u, ns_prefix)
        s += '%s<%s:WindingInfo.connection_kind>%s</%s:WindingInfo.connection_kind>' % \
            (indent, ns_prefix, self.connection_kind, ns_prefix)
        s += '%s<%s:WindingInfo.emergency_s>%s</%s:WindingInfo.emergency_s>' % \
            (indent, ns_prefix, self.emergency_s, ns_prefix)
        s += '%s<%s:WindingInfo.r>%s</%s:WindingInfo.r>' % \
            (indent, ns_prefix, self.r, ns_prefix)
        s += '%s<%s:WindingInfo.phase_angle>%s</%s:WindingInfo.phase_angle>' % \
            (indent, ns_prefix, self.phase_angle, ns_prefix)
        s += '%s<%s:WindingInfo.insulation_u>%s</%s:WindingInfo.insulation_u>' % \
            (indent, ns_prefix, self.insulation_u, ns_prefix)
        s += '%s<%s:WindingInfo.short_term_s>%s</%s:WindingInfo.short_term_s>' % \
            (indent, ns_prefix, self.short_term_s, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "WindingInfo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> winding_info.serialize


class CableInfo(ConductorInfo):
    """ Cable data.Cable data.
    """
    # <<< cable_info
    # @generated
    def __init__(self, nominal_temperature=0.0, diameter_over_screen=0.0, sheath_as_neutral=False, diameter_over_jacket=0.0, diameter_over_core=0.0, construction_kind='solid', outer_jacket_kind='insulating', is_strand_fill=False, shield_material='other', diameter_over_insulation=0.0, **kw_args):
        """ Initialises a new 'CableInfo' instance.
        """
        # Maximum nominal design operating temperature.Maximum nominal design operating temperature. 
        self.nominal_temperature = nominal_temperature

        # Diameter over the outer screen; should be the shield's inside diameter..Diameter over the outer screen; should be the shield's inside diameter.. 
        self.diameter_over_screen = diameter_over_screen

        # True if sheath / shield is used as a neutral (i.e., bonded).True if sheath / shield is used as a neutral (i.e., bonded). 
        self.sheath_as_neutral = sheath_as_neutral

        # Diameter over the outermost jacketing layer.Diameter over the outermost jacketing layer. 
        self.diameter_over_jacket = diameter_over_jacket

        # Diameter over the core, including any semi-con screen; should be the insulating layer's inside diameter.Diameter over the core, including any semi-con screen; should be the insulating layer's inside diameter. 
        self.diameter_over_core = diameter_over_core

        # Kind of construction of this cable.Kind of construction of this cable. Values are: "solid", "stranded", "other", "segmental", "compacted", "sector", "compressed"
        self.construction_kind = 'solid'

        # Kind of outer jacket of this cable.Kind of outer jacket of this cable. Values are: "insulating", "other", "semiconducting", "polyethylene", "none", "linear_low_density_polyethylene", "pvc"
        self.outer_jacket_kind = 'insulating'

        # True if wire strands are extruded in a way to fill the voids in the cable.True if wire strands are extruded in a way to fill the voids in the cable. 
        self.is_strand_fill = is_strand_fill

        # Material of the shield.Material of the shield. Values are: "other", "lead", "steel", "aluminum", "copper"
        self.shield_material = 'other'

        # Diameter over the insulating layer, excluding outer screen.Diameter over the insulating layer, excluding outer screen. 
        self.diameter_over_insulation = diameter_over_insulation



        super(CableInfo, self).__init__(**kw_args)
    # >>> cable_info


    def __str__(self):
        """ Returns a string representation of the CableInfo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< cable_info.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CableInfo.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CableInfo", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:CableInfo.nominal_temperature>%s</%s:CableInfo.nominal_temperature>' % \
            (indent, ns_prefix, self.nominal_temperature, ns_prefix)
        s += '%s<%s:CableInfo.diameter_over_screen>%s</%s:CableInfo.diameter_over_screen>' % \
            (indent, ns_prefix, self.diameter_over_screen, ns_prefix)
        s += '%s<%s:CableInfo.sheath_as_neutral>%s</%s:CableInfo.sheath_as_neutral>' % \
            (indent, ns_prefix, self.sheath_as_neutral, ns_prefix)
        s += '%s<%s:CableInfo.diameter_over_jacket>%s</%s:CableInfo.diameter_over_jacket>' % \
            (indent, ns_prefix, self.diameter_over_jacket, ns_prefix)
        s += '%s<%s:CableInfo.diameter_over_core>%s</%s:CableInfo.diameter_over_core>' % \
            (indent, ns_prefix, self.diameter_over_core, ns_prefix)
        s += '%s<%s:CableInfo.construction_kind>%s</%s:CableInfo.construction_kind>' % \
            (indent, ns_prefix, self.construction_kind, ns_prefix)
        s += '%s<%s:CableInfo.outer_jacket_kind>%s</%s:CableInfo.outer_jacket_kind>' % \
            (indent, ns_prefix, self.outer_jacket_kind, ns_prefix)
        s += '%s<%s:CableInfo.is_strand_fill>%s</%s:CableInfo.is_strand_fill>' % \
            (indent, ns_prefix, self.is_strand_fill, ns_prefix)
        s += '%s<%s:CableInfo.shield_material>%s</%s:CableInfo.shield_material>' % \
            (indent, ns_prefix, self.shield_material, ns_prefix)
        s += '%s<%s:CableInfo.diameter_over_insulation>%s</%s:CableInfo.diameter_over_insulation>' % \
            (indent, ns_prefix, self.diameter_over_insulation, ns_prefix)
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
        for obj in self.wire_arrangements:
            s += '%s<%s:ConductorInfo.wire_arrangements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.conductor_segments:
            s += '%s<%s:ConductorInfo.conductor_segments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ConductorInfo.phase_count>%s</%s:ConductorInfo.phase_count>' % \
            (indent, ns_prefix, self.phase_count, ns_prefix)
        s += '%s<%s:ConductorInfo.insulation_material>%s</%s:ConductorInfo.insulation_material>' % \
            (indent, ns_prefix, self.insulation_material, ns_prefix)
        s += '%s<%s:ConductorInfo.insulation_thickness>%s</%s:ConductorInfo.insulation_thickness>' % \
            (indent, ns_prefix, self.insulation_thickness, ns_prefix)
        s += '%s<%s:ConductorInfo.insulated>%s</%s:ConductorInfo.insulated>' % \
            (indent, ns_prefix, self.insulated, ns_prefix)
        s += '%s<%s:ConductorInfo.usage>%s</%s:ConductorInfo.usage>' % \
            (indent, ns_prefix, self.usage, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CableInfo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> cable_info.serialize


class OpenCircuitTest(DistributionWindingTest):
    """ Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. For induced voltage and phase shifts, use the associated ToWindingSpec class.Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. For induced voltage and phase shifts, use the associated ToWindingSpec class.
    """
    # <<< open_circuit_test
    # @generated
    def __init__(self, no_load_loss_zero=0.0, no_load_loss=0.0, exciting_current=0.0, exciting_current_zero=0.0, measured_winding_specs=None, **kw_args):
        """ Initialises a new 'OpenCircuitTest' instance.
        """
        # Losses measured from a zero-sequence open-circuit (excitation) test.Losses measured from a zero-sequence open-circuit (excitation) test. 
        self.no_load_loss_zero = no_load_loss_zero

        # Losses measured from a positive-sequence or single-phase open-circuit (excitation) test.Losses measured from a positive-sequence or single-phase open-circuit (excitation) test. 
        self.no_load_loss = no_load_loss

        # Exciting current measured from a positive-sequence or single-phase open-circuit (excitation) test.Exciting current measured from a positive-sequence or single-phase open-circuit (excitation) test. 
        self.exciting_current = exciting_current

        # Exciting current measured from a zero-sequence open-circuit (excitation) test.Exciting current measured from a zero-sequence open-circuit (excitation) test. 
        self.exciting_current_zero = exciting_current_zero


        self._measured_winding_specs = []
        if measured_winding_specs is not None:
            self.measured_winding_specs = measured_winding_specs
        else:
            self.measured_winding_specs = []


        super(OpenCircuitTest, self).__init__(**kw_args)
    # >>> open_circuit_test

    # <<< measured_winding_specs
    # @generated
    def get_measured_winding_specs(self):
        """ All other windings measured during this test.All other windings measured during this test.
        """
        return self._measured_winding_specs

    def set_measured_winding_specs(self, value):
        for p in self._measured_winding_specs:
            filtered = [q for q in p.open_circuit_tests if q != self]
            self._measured_winding_specs._open_circuit_tests = filtered
        for r in value:
            if self not in r._open_circuit_tests:
                r._open_circuit_tests.append(self)
        self._measured_winding_specs = value

    measured_winding_specs = property(get_measured_winding_specs, set_measured_winding_specs)

    def add_measured_winding_specs(self, *measured_winding_specs):
        for obj in measured_winding_specs:
            if self not in obj._open_circuit_tests:
                obj._open_circuit_tests.append(self)
            self._measured_winding_specs.append(obj)

    def remove_measured_winding_specs(self, *measured_winding_specs):
        for obj in measured_winding_specs:
            if self in obj._open_circuit_tests:
                obj._open_circuit_tests.remove(self)
            self._measured_winding_specs.remove(obj)
    # >>> measured_winding_specs


    def __str__(self):
        """ Returns a string representation of the OpenCircuitTest.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< open_circuit_test.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OpenCircuitTest.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OpenCircuitTest", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.measured_winding_specs:
            s += '%s<%s:OpenCircuitTest.measured_winding_specs rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:OpenCircuitTest.no_load_loss_zero>%s</%s:OpenCircuitTest.no_load_loss_zero>' % \
            (indent, ns_prefix, self.no_load_loss_zero, ns_prefix)
        s += '%s<%s:OpenCircuitTest.no_load_loss>%s</%s:OpenCircuitTest.no_load_loss>' % \
            (indent, ns_prefix, self.no_load_loss, ns_prefix)
        s += '%s<%s:OpenCircuitTest.exciting_current>%s</%s:OpenCircuitTest.exciting_current>' % \
            (indent, ns_prefix, self.exciting_current, ns_prefix)
        s += '%s<%s:OpenCircuitTest.exciting_current_zero>%s</%s:OpenCircuitTest.exciting_current_zero>' % \
            (indent, ns_prefix, self.exciting_current_zero, ns_prefix)
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
        if self.from_winding is not None:
            s += '%s<%s:DistributionWindingTest.from_winding rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.from_winding.uri)
        s += '%s<%s:DistributionWindingTest.from_tap_step>%s</%s:DistributionWindingTest.from_tap_step>' % \
            (indent, ns_prefix, self.from_tap_step, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "OpenCircuitTest")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> open_circuit_test.serialize


class ConcentricNeutralCableInfo(CableInfo):
    """ Concentric neutral cable data.Concentric neutral cable data.
    """
    # <<< concentric_neutral_cable_info
    # @generated
    def __init__(self, neutral_strand_count=0, diameter_over_neutral=0.0, wire_type=None, **kw_args):
        """ Initialises a new 'ConcentricNeutralCableInfo' instance.
        """
        # Number of concentric neutral strands.Number of concentric neutral strands. 
        self.neutral_strand_count = neutral_strand_count

        # Diameter over the concentric neutral strands.Diameter over the concentric neutral strands. 
        self.diameter_over_neutral = diameter_over_neutral


        self._wire_type = None
        self.wire_type = wire_type


        super(ConcentricNeutralCableInfo, self).__init__(**kw_args)
    # >>> concentric_neutral_cable_info

    # <<< wire_type
    # @generated
    def get_wire_type(self):
        """ Wire type used for this concentric neutral cable.Wire type used for this concentric neutral cable.
        """
        return self._wire_type

    def set_wire_type(self, value):
        if self._wire_type is not None:
            filtered = [x for x in self.wire_type.concentric_neutral_cable_infos if x != self]
            self._wire_type._concentric_neutral_cable_infos = filtered

        self._wire_type = value
        if self._wire_type is not None:
            self._wire_type._concentric_neutral_cable_infos.append(self)

    wire_type = property(get_wire_type, set_wire_type)
    # >>> wire_type


    def __str__(self):
        """ Returns a string representation of the ConcentricNeutralCableInfo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< concentric_neutral_cable_info.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ConcentricNeutralCableInfo.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ConcentricNeutralCableInfo", self.uri)
        if format:
            indent += ' ' * depth

        if self.wire_type is not None:
            s += '%s<%s:ConcentricNeutralCableInfo.wire_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.wire_type.uri)
        s += '%s<%s:ConcentricNeutralCableInfo.neutral_strand_count>%s</%s:ConcentricNeutralCableInfo.neutral_strand_count>' % \
            (indent, ns_prefix, self.neutral_strand_count, ns_prefix)
        s += '%s<%s:ConcentricNeutralCableInfo.diameter_over_neutral>%s</%s:ConcentricNeutralCableInfo.diameter_over_neutral>' % \
            (indent, ns_prefix, self.diameter_over_neutral, ns_prefix)
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
        for obj in self.wire_arrangements:
            s += '%s<%s:ConductorInfo.wire_arrangements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.conductor_segments:
            s += '%s<%s:ConductorInfo.conductor_segments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ConductorInfo.phase_count>%s</%s:ConductorInfo.phase_count>' % \
            (indent, ns_prefix, self.phase_count, ns_prefix)
        s += '%s<%s:ConductorInfo.insulation_material>%s</%s:ConductorInfo.insulation_material>' % \
            (indent, ns_prefix, self.insulation_material, ns_prefix)
        s += '%s<%s:ConductorInfo.insulation_thickness>%s</%s:ConductorInfo.insulation_thickness>' % \
            (indent, ns_prefix, self.insulation_thickness, ns_prefix)
        s += '%s<%s:ConductorInfo.insulated>%s</%s:ConductorInfo.insulated>' % \
            (indent, ns_prefix, self.insulated, ns_prefix)
        s += '%s<%s:ConductorInfo.usage>%s</%s:ConductorInfo.usage>' % \
            (indent, ns_prefix, self.usage, ns_prefix)
        s += '%s<%s:CableInfo.nominal_temperature>%s</%s:CableInfo.nominal_temperature>' % \
            (indent, ns_prefix, self.nominal_temperature, ns_prefix)
        s += '%s<%s:CableInfo.diameter_over_screen>%s</%s:CableInfo.diameter_over_screen>' % \
            (indent, ns_prefix, self.diameter_over_screen, ns_prefix)
        s += '%s<%s:CableInfo.sheath_as_neutral>%s</%s:CableInfo.sheath_as_neutral>' % \
            (indent, ns_prefix, self.sheath_as_neutral, ns_prefix)
        s += '%s<%s:CableInfo.diameter_over_jacket>%s</%s:CableInfo.diameter_over_jacket>' % \
            (indent, ns_prefix, self.diameter_over_jacket, ns_prefix)
        s += '%s<%s:CableInfo.diameter_over_core>%s</%s:CableInfo.diameter_over_core>' % \
            (indent, ns_prefix, self.diameter_over_core, ns_prefix)
        s += '%s<%s:CableInfo.construction_kind>%s</%s:CableInfo.construction_kind>' % \
            (indent, ns_prefix, self.construction_kind, ns_prefix)
        s += '%s<%s:CableInfo.outer_jacket_kind>%s</%s:CableInfo.outer_jacket_kind>' % \
            (indent, ns_prefix, self.outer_jacket_kind, ns_prefix)
        s += '%s<%s:CableInfo.is_strand_fill>%s</%s:CableInfo.is_strand_fill>' % \
            (indent, ns_prefix, self.is_strand_fill, ns_prefix)
        s += '%s<%s:CableInfo.shield_material>%s</%s:CableInfo.shield_material>' % \
            (indent, ns_prefix, self.shield_material, ns_prefix)
        s += '%s<%s:CableInfo.diameter_over_insulation>%s</%s:CableInfo.diameter_over_insulation>' % \
            (indent, ns_prefix, self.diameter_over_insulation, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ConcentricNeutralCableInfo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> concentric_neutral_cable_info.serialize


class OverheadConductorInfo(ConductorInfo):
    """ Overhead conductor data.Overhead conductor data.
    """
    # <<< overhead_conductor_info
    # @generated
    def __init__(self, neutral_insulation_thickness=0.0, phase_conductor_count=0, phase_conductor_spacing=0.0, **kw_args):
        """ Initialises a new 'OverheadConductorInfo' instance.
        """
        # (if applicable) Insulation thickness of the neutral conductor.(if applicable) Insulation thickness of the neutral conductor. 
        self.neutral_insulation_thickness = neutral_insulation_thickness

        # Number of conductor strands in the symmetrical bundle (1-12).Number of conductor strands in the symmetrical bundle (1-12). 
        self.phase_conductor_count = phase_conductor_count

        # Distance between conductor strands in a symmetrical bundle.Distance between conductor strands in a symmetrical bundle. 
        self.phase_conductor_spacing = phase_conductor_spacing



        super(OverheadConductorInfo, self).__init__(**kw_args)
    # >>> overhead_conductor_info


    def __str__(self):
        """ Returns a string representation of the OverheadConductorInfo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< overhead_conductor_info.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OverheadConductorInfo.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OverheadConductorInfo", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:OverheadConductorInfo.neutral_insulation_thickness>%s</%s:OverheadConductorInfo.neutral_insulation_thickness>' % \
            (indent, ns_prefix, self.neutral_insulation_thickness, ns_prefix)
        s += '%s<%s:OverheadConductorInfo.phase_conductor_count>%s</%s:OverheadConductorInfo.phase_conductor_count>' % \
            (indent, ns_prefix, self.phase_conductor_count, ns_prefix)
        s += '%s<%s:OverheadConductorInfo.phase_conductor_spacing>%s</%s:OverheadConductorInfo.phase_conductor_spacing>' % \
            (indent, ns_prefix, self.phase_conductor_spacing, ns_prefix)
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
        for obj in self.wire_arrangements:
            s += '%s<%s:ConductorInfo.wire_arrangements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.conductor_segments:
            s += '%s<%s:ConductorInfo.conductor_segments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ConductorInfo.phase_count>%s</%s:ConductorInfo.phase_count>' % \
            (indent, ns_prefix, self.phase_count, ns_prefix)
        s += '%s<%s:ConductorInfo.insulation_material>%s</%s:ConductorInfo.insulation_material>' % \
            (indent, ns_prefix, self.insulation_material, ns_prefix)
        s += '%s<%s:ConductorInfo.insulation_thickness>%s</%s:ConductorInfo.insulation_thickness>' % \
            (indent, ns_prefix, self.insulation_thickness, ns_prefix)
        s += '%s<%s:ConductorInfo.insulated>%s</%s:ConductorInfo.insulated>' % \
            (indent, ns_prefix, self.insulated, ns_prefix)
        s += '%s<%s:ConductorInfo.usage>%s</%s:ConductorInfo.usage>' % \
            (indent, ns_prefix, self.usage, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "OverheadConductorInfo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> overhead_conductor_info.serialize


class TapeShieldCableInfo(CableInfo):
    """ Tape shield cable data.Tape shield cable data.
    """
    # <<< tape_shield_cable_info
    # @generated
    def __init__(self, tape_thickness=0.0, tape_lap=0.0, **kw_args):
        """ Initialises a new 'TapeShieldCableInfo' instance.
        """
        # Thickness of the tape shield, before wrapping.Thickness of the tape shield, before wrapping. 
        self.tape_thickness = tape_thickness

        # Percentage of the tape shield width that overlaps in each wrap, typically 10% to 25%.Percentage of the tape shield width that overlaps in each wrap, typically 10% to 25%. 
        self.tape_lap = tape_lap



        super(TapeShieldCableInfo, self).__init__(**kw_args)
    # >>> tape_shield_cable_info


    def __str__(self):
        """ Returns a string representation of the TapeShieldCableInfo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< tape_shield_cable_info.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TapeShieldCableInfo.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TapeShieldCableInfo", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:TapeShieldCableInfo.tape_thickness>%s</%s:TapeShieldCableInfo.tape_thickness>' % \
            (indent, ns_prefix, self.tape_thickness, ns_prefix)
        s += '%s<%s:TapeShieldCableInfo.tape_lap>%s</%s:TapeShieldCableInfo.tape_lap>' % \
            (indent, ns_prefix, self.tape_lap, ns_prefix)
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
        for obj in self.wire_arrangements:
            s += '%s<%s:ConductorInfo.wire_arrangements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.conductor_segments:
            s += '%s<%s:ConductorInfo.conductor_segments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ConductorInfo.phase_count>%s</%s:ConductorInfo.phase_count>' % \
            (indent, ns_prefix, self.phase_count, ns_prefix)
        s += '%s<%s:ConductorInfo.insulation_material>%s</%s:ConductorInfo.insulation_material>' % \
            (indent, ns_prefix, self.insulation_material, ns_prefix)
        s += '%s<%s:ConductorInfo.insulation_thickness>%s</%s:ConductorInfo.insulation_thickness>' % \
            (indent, ns_prefix, self.insulation_thickness, ns_prefix)
        s += '%s<%s:ConductorInfo.insulated>%s</%s:ConductorInfo.insulated>' % \
            (indent, ns_prefix, self.insulated, ns_prefix)
        s += '%s<%s:ConductorInfo.usage>%s</%s:ConductorInfo.usage>' % \
            (indent, ns_prefix, self.usage, ns_prefix)
        s += '%s<%s:CableInfo.nominal_temperature>%s</%s:CableInfo.nominal_temperature>' % \
            (indent, ns_prefix, self.nominal_temperature, ns_prefix)
        s += '%s<%s:CableInfo.diameter_over_screen>%s</%s:CableInfo.diameter_over_screen>' % \
            (indent, ns_prefix, self.diameter_over_screen, ns_prefix)
        s += '%s<%s:CableInfo.sheath_as_neutral>%s</%s:CableInfo.sheath_as_neutral>' % \
            (indent, ns_prefix, self.sheath_as_neutral, ns_prefix)
        s += '%s<%s:CableInfo.diameter_over_jacket>%s</%s:CableInfo.diameter_over_jacket>' % \
            (indent, ns_prefix, self.diameter_over_jacket, ns_prefix)
        s += '%s<%s:CableInfo.diameter_over_core>%s</%s:CableInfo.diameter_over_core>' % \
            (indent, ns_prefix, self.diameter_over_core, ns_prefix)
        s += '%s<%s:CableInfo.construction_kind>%s</%s:CableInfo.construction_kind>' % \
            (indent, ns_prefix, self.construction_kind, ns_prefix)
        s += '%s<%s:CableInfo.outer_jacket_kind>%s</%s:CableInfo.outer_jacket_kind>' % \
            (indent, ns_prefix, self.outer_jacket_kind, ns_prefix)
        s += '%s<%s:CableInfo.is_strand_fill>%s</%s:CableInfo.is_strand_fill>' % \
            (indent, ns_prefix, self.is_strand_fill, ns_prefix)
        s += '%s<%s:CableInfo.shield_material>%s</%s:CableInfo.shield_material>' % \
            (indent, ns_prefix, self.shield_material, ns_prefix)
        s += '%s<%s:CableInfo.diameter_over_insulation>%s</%s:CableInfo.diameter_over_insulation>' % \
            (indent, ns_prefix, self.diameter_over_insulation, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "TapeShieldCableInfo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> tape_shield_cable_info.serialize


class ShortCircuitTest(DistributionWindingTest):
    """ Short-circuit test results include load losses and leakage impedances. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. There must be at least one short-circuited ('to') winding.Short-circuit test results include load losses and leakage impedances. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. There must be at least one short-circuited ('to') winding.
    """
    # <<< short_circuit_test
    # @generated
    def __init__(self, load_loss_zero=0.0, leakage_impedance_zero=0.0, leakage_impedance=0.0, load_loss=0.0, shorted_winding_specs=None, **kw_args):
        """ Initialises a new 'ShortCircuitTest' instance.
        """
        # Load losses from a zero-sequence short-circuit test.Load losses from a zero-sequence short-circuit test. 
        self.load_loss_zero = load_loss_zero

        # Leakage impedance measured from a zero-sequence short-circuit test.Leakage impedance measured from a zero-sequence short-circuit test. 
        self.leakage_impedance_zero = leakage_impedance_zero

        # Leakage impedance measured from a positive-sequence or single-phase short-circuit test.Leakage impedance measured from a positive-sequence or single-phase short-circuit test. 
        self.leakage_impedance = leakage_impedance

        # Load losses from a positive-sequence or single-phase short-circuit test.Load losses from a positive-sequence or single-phase short-circuit test. 
        self.load_loss = load_loss


        self._shorted_winding_specs = []
        if shorted_winding_specs is not None:
            self.shorted_winding_specs = shorted_winding_specs
        else:
            self.shorted_winding_specs = []


        super(ShortCircuitTest, self).__init__(**kw_args)
    # >>> short_circuit_test

    # <<< shorted_winding_specs
    # @generated
    def get_shorted_winding_specs(self):
        """ All windings short-circuited during this test.All windings short-circuited during this test.
        """
        return self._shorted_winding_specs

    def set_shorted_winding_specs(self, value):
        for p in self._shorted_winding_specs:
            filtered = [q for q in p.short_circuit_tests if q != self]
            self._shorted_winding_specs._short_circuit_tests = filtered
        for r in value:
            if self not in r._short_circuit_tests:
                r._short_circuit_tests.append(self)
        self._shorted_winding_specs = value

    shorted_winding_specs = property(get_shorted_winding_specs, set_shorted_winding_specs)

    def add_shorted_winding_specs(self, *shorted_winding_specs):
        for obj in shorted_winding_specs:
            if self not in obj._short_circuit_tests:
                obj._short_circuit_tests.append(self)
            self._shorted_winding_specs.append(obj)

    def remove_shorted_winding_specs(self, *shorted_winding_specs):
        for obj in shorted_winding_specs:
            if self in obj._short_circuit_tests:
                obj._short_circuit_tests.remove(self)
            self._shorted_winding_specs.remove(obj)
    # >>> shorted_winding_specs


    def __str__(self):
        """ Returns a string representation of the ShortCircuitTest.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< short_circuit_test.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ShortCircuitTest.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ShortCircuitTest", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.shorted_winding_specs:
            s += '%s<%s:ShortCircuitTest.shorted_winding_specs rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ShortCircuitTest.load_loss_zero>%s</%s:ShortCircuitTest.load_loss_zero>' % \
            (indent, ns_prefix, self.load_loss_zero, ns_prefix)
        s += '%s<%s:ShortCircuitTest.leakage_impedance_zero>%s</%s:ShortCircuitTest.leakage_impedance_zero>' % \
            (indent, ns_prefix, self.leakage_impedance_zero, ns_prefix)
        s += '%s<%s:ShortCircuitTest.leakage_impedance>%s</%s:ShortCircuitTest.leakage_impedance>' % \
            (indent, ns_prefix, self.leakage_impedance, ns_prefix)
        s += '%s<%s:ShortCircuitTest.load_loss>%s</%s:ShortCircuitTest.load_loss>' % \
            (indent, ns_prefix, self.load_loss, ns_prefix)
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
        if self.from_winding is not None:
            s += '%s<%s:DistributionWindingTest.from_winding rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.from_winding.uri)
        s += '%s<%s:DistributionWindingTest.from_tap_step>%s</%s:DistributionWindingTest.from_tap_step>' % \
            (indent, ns_prefix, self.from_tap_step, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ShortCircuitTest")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> short_circuit_test.serialize


# <<< asset_models
# @generated
# >>> asset_models
