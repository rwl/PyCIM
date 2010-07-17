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

""" Contains entities that describe dynamic measurement data exchanged between applications.
"""

from cim.iec61970.core import IdentifiedObject
from cim.iec61970.core import Equipment
from cim import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.meas"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Meas"

class LimitSet(IdentifiedObject):
    """ Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets corresponding to seasonal or other changing conditions. The condition is captured in the name and description attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used this way.
    """
    # <<< limit_set
    # @generated
    def __init__(self, is_percentage_limits=False, **kw_args):
        """ Initialises a new 'LimitSet' instance.
        """
        # Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls. 
        self.is_percentage_limits = is_percentage_limits



        super(LimitSet, self).__init__(**kw_args)
    # >>> limit_set


    def __str__(self):
        """ Returns a string representation of the LimitSet.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< limit_set.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LimitSet.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LimitSet", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:LimitSet.is_percentage_limits>%s</%s:LimitSet.is_percentage_limits>' % \
            (indent, ns_prefix, self.is_percentage_limits, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LimitSet")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> limit_set.serialize


class MeasurementValue(IdentifiedObject):
    """ The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.
    """
    # <<< measurement_value
    # @generated
    def __init__(self, sensor_accuracy=0.0, time_stamp='', gml_values=None, measurement_value_source=None, erp_person=None, procedure_data_sets=None, remote_source=None, measurement_value_quality=None, **kw_args):
        """ Initialises a new 'MeasurementValue' instance.
        """
        # The limit, expressed as a percentage of the sensor maximum, that errors will not exceed when the sensor is used under  reference conditions. 
        self.sensor_accuracy = sensor_accuracy

        # The time when the value was last updated 
        self.time_stamp = time_stamp


        self._gml_values = []
        if gml_values is not None:
            self.gml_values = gml_values
        else:
            self.gml_values = []

        self._measurement_value_source = None
        self.measurement_value_source = measurement_value_source

        self._erp_person = None
        self.erp_person = erp_person

        self._procedure_data_sets = []
        if procedure_data_sets is not None:
            self.procedure_data_sets = procedure_data_sets
        else:
            self.procedure_data_sets = []

        self._remote_source = None
        self.remote_source = remote_source

        self._measurement_value_quality = None
        self.measurement_value_quality = measurement_value_quality


        super(MeasurementValue, self).__init__(**kw_args)
    # >>> measurement_value

    # <<< gml_values
    # @generated
    def get_gml_values(self):
        """ 
        """
        return self._gml_values

    def set_gml_values(self, value):
        for x in self._gml_values:
            x._measurement_value = None
        for y in value:
            y._measurement_value = self
        self._gml_values = value

    gml_values = property(get_gml_values, set_gml_values)

    def add_gml_values(self, *gml_values):
        for obj in gml_values:
            obj._measurement_value = self
            self._gml_values.append(obj)

    def remove_gml_values(self, *gml_values):
        for obj in gml_values:
            obj._measurement_value = None
            self._gml_values.remove(obj)
    # >>> gml_values

    # <<< measurement_value_source
    # @generated
    def get_measurement_value_source(self):
        """ A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink, manual, etc. User conventions for the names of sources are contained in the introduction to IEC 61970-301.
        """
        return self._measurement_value_source

    def set_measurement_value_source(self, value):
        if self._measurement_value_source is not None:
            filtered = [x for x in self.measurement_value_source.measurement_values if x != self]
            self._measurement_value_source._measurement_values = filtered

        self._measurement_value_source = value
        if self._measurement_value_source is not None:
            self._measurement_value_source._measurement_values.append(self)

    measurement_value_source = property(get_measurement_value_source, set_measurement_value_source)
    # >>> measurement_value_source

    # <<< erp_person
    # @generated
    def get_erp_person(self):
        """ 
        """
        return self._erp_person

    def set_erp_person(self, value):
        if self._erp_person is not None:
            filtered = [x for x in self.erp_person.measurement_values if x != self]
            self._erp_person._measurement_values = filtered

        self._erp_person = value
        if self._erp_person is not None:
            self._erp_person._measurement_values.append(self)

    erp_person = property(get_erp_person, set_erp_person)
    # >>> erp_person

    # <<< procedure_data_sets
    # @generated
    def get_procedure_data_sets(self):
        """ 
        """
        return self._procedure_data_sets

    def set_procedure_data_sets(self, value):
        for p in self._procedure_data_sets:
            filtered = [q for q in p.measurement_values if q != self]
            self._procedure_data_sets._measurement_values = filtered
        for r in value:
            if self not in r._measurement_values:
                r._measurement_values.append(self)
        self._procedure_data_sets = value

    procedure_data_sets = property(get_procedure_data_sets, set_procedure_data_sets)

    def add_procedure_data_sets(self, *procedure_data_sets):
        for obj in procedure_data_sets:
            if self not in obj._measurement_values:
                obj._measurement_values.append(self)
            self._procedure_data_sets.append(obj)

    def remove_procedure_data_sets(self, *procedure_data_sets):
        for obj in procedure_data_sets:
            if self in obj._measurement_values:
                obj._measurement_values.remove(self)
            self._procedure_data_sets.remove(obj)
    # >>> procedure_data_sets

    # <<< remote_source
    # @generated
    def get_remote_source(self):
        """ Link to the physical telemetered point associated with this measurement.
        """
        return self._remote_source

    def set_remote_source(self, value):
        if self._remote_source is not None:
            self._remote_source._measurement_value = None

        self._remote_source = value
        if self._remote_source is not None:
            self._remote_source._measurement_value = self

    remote_source = property(get_remote_source, set_remote_source)
    # >>> remote_source

    # <<< measurement_value_quality
    # @generated
    def get_measurement_value_quality(self):
        """ A MeasurementValue has a MeasurementValueQuality associated with it.
        """
        return self._measurement_value_quality

    def set_measurement_value_quality(self, value):
        if self._measurement_value_quality is not None:
            self._measurement_value_quality._measurement_value = None

        self._measurement_value_quality = value
        if self._measurement_value_quality is not None:
            self._measurement_value_quality._measurement_value = self

    measurement_value_quality = property(get_measurement_value_quality, set_measurement_value_quality)
    # >>> measurement_value_quality


    def __str__(self):
        """ Returns a string representation of the MeasurementValue.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< measurement_value.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MeasurementValue.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MeasurementValue", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.gml_values:
            s += '%s<%s:MeasurementValue.gml_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.measurement_value_source is not None:
            s += '%s<%s:MeasurementValue.measurement_value_source rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value_source.uri)
        if self.erp_person is not None:
            s += '%s<%s:MeasurementValue.erp_person rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_person.uri)
        for obj in self.procedure_data_sets:
            s += '%s<%s:MeasurementValue.procedure_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.remote_source is not None:
            s += '%s<%s:MeasurementValue.remote_source rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.remote_source.uri)
        if self.measurement_value_quality is not None:
            s += '%s<%s:MeasurementValue.measurement_value_quality rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value_quality.uri)
        s += '%s<%s:MeasurementValue.sensor_accuracy>%s</%s:MeasurementValue.sensor_accuracy>' % \
            (indent, ns_prefix, self.sensor_accuracy, ns_prefix)
        s += '%s<%s:MeasurementValue.time_stamp>%s</%s:MeasurementValue.time_stamp>' % \
            (indent, ns_prefix, self.time_stamp, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MeasurementValue")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> measurement_value.serialize


class ValueAliasSet(IdentifiedObject):
    """ Describes the translation of a set of values into a name and is intendend to facilitate cusom translations. Each ValueAliasSet has a name, description etc. A specific Measurement may represent a discrete state like Open, Closed, Intermediate etc. This requires a translation from the MeasurementValue.value number to a string, e.g. 0->'Invalid', 1->'Open', 2->'Closed', 3->'Intermediate'. Each ValueToAlias member in ValueAliasSet.Value describe a mapping for one particular value to a name.
    """
    # <<< value_alias_set
    # @generated
    def __init__(self, discretes=None, commands=None, values=None, **kw_args):
        """ Initialises a new 'ValueAliasSet' instance.
        """

        self._discretes = []
        if discretes is not None:
            self.discretes = discretes
        else:
            self.discretes = []

        self._commands = []
        if commands is not None:
            self.commands = commands
        else:
            self.commands = []

        self._values = []
        if values is not None:
            self.values = values
        else:
            self.values = []


        super(ValueAliasSet, self).__init__(**kw_args)
    # >>> value_alias_set

    # <<< discretes
    # @generated
    def get_discretes(self):
        """ The Measurements using the set for translation
        """
        return self._discretes

    def set_discretes(self, value):
        for x in self._discretes:
            x._value_alias_set = None
        for y in value:
            y._value_alias_set = self
        self._discretes = value

    discretes = property(get_discretes, set_discretes)

    def add_discretes(self, *discretes):
        for obj in discretes:
            obj._value_alias_set = self
            self._discretes.append(obj)

    def remove_discretes(self, *discretes):
        for obj in discretes:
            obj._value_alias_set = None
            self._discretes.remove(obj)
    # >>> discretes

    # <<< commands
    # @generated
    def get_commands(self):
        """ The ValueAliasSet used for translation of a Control value to a name.
        """
        return self._commands

    def set_commands(self, value):
        for x in self._commands:
            x._value_alias_set = None
        for y in value:
            y._value_alias_set = self
        self._commands = value

    commands = property(get_commands, set_commands)

    def add_commands(self, *commands):
        for obj in commands:
            obj._value_alias_set = self
            self._commands.append(obj)

    def remove_commands(self, *commands):
        for obj in commands:
            obj._value_alias_set = None
            self._commands.remove(obj)
    # >>> commands

    # <<< values
    # @generated
    def get_values(self):
        """ The ValueToAlias mappings included in the set
        """
        return self._values

    def set_values(self, value):
        for x in self._values:
            x._value_alias_set = None
        for y in value:
            y._value_alias_set = self
        self._values = value

    values = property(get_values, set_values)

    def add_values(self, *values):
        for obj in values:
            obj._value_alias_set = self
            self._values.append(obj)

    def remove_values(self, *values):
        for obj in values:
            obj._value_alias_set = None
            self._values.remove(obj)
    # >>> values


    def __str__(self):
        """ Returns a string representation of the ValueAliasSet.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< value_alias_set.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ValueAliasSet.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ValueAliasSet", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.discretes:
            s += '%s<%s:ValueAliasSet.discretes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.commands:
            s += '%s<%s:ValueAliasSet.commands rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.values:
            s += '%s<%s:ValueAliasSet.values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ValueAliasSet")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> value_alias_set.serialize


class PotentialTransformer(Equipment):
    """ Instrument transformer (also known as Voltage Transformer) used to measure electrical qualities of the circuit that is being protected and/or monitored. Typically used as voltage transducer for the purpose of metering, protection, or sometimes auxiliary substation supply. A typical secondary voltage rating would be 120V.
    """
    # <<< potential_transformer
    # @generated
    def __init__(self, accuracy_class='', pt_class='', nominal_ratio=0.0, potential_transformer_asset=None, potential_transformer_type_asset=None, **kw_args):
        """ Initialises a new 'PotentialTransformer' instance.
        """
        # PT accuracy classification. 
        self.accuracy_class = accuracy_class

        # PT classification. 
        self.pt_class = pt_class

        # Nominal ratio between the primary and secondary voltage. 
        self.nominal_ratio = nominal_ratio


        self._potential_transformer_asset = None
        self.potential_transformer_asset = potential_transformer_asset

        self._potential_transformer_type_asset = None
        self.potential_transformer_type_asset = potential_transformer_type_asset


        super(PotentialTransformer, self).__init__(**kw_args)
    # >>> potential_transformer

    # <<< potential_transformer_asset
    # @generated
    def get_potential_transformer_asset(self):
        """ 
        """
        return self._potential_transformer_asset

    def set_potential_transformer_asset(self, value):
        if self._potential_transformer_asset is not None:
            self._potential_transformer_asset._potential_transformer = None

        self._potential_transformer_asset = value
        if self._potential_transformer_asset is not None:
            self._potential_transformer_asset._potential_transformer = self

    potential_transformer_asset = property(get_potential_transformer_asset, set_potential_transformer_asset)
    # >>> potential_transformer_asset

    # <<< potential_transformer_type_asset
    # @generated
    def get_potential_transformer_type_asset(self):
        """ 
        """
        return self._potential_transformer_type_asset

    def set_potential_transformer_type_asset(self, value):
        if self._potential_transformer_type_asset is not None:
            filtered = [x for x in self.potential_transformer_type_asset.potential_transformers if x != self]
            self._potential_transformer_type_asset._potential_transformers = filtered

        self._potential_transformer_type_asset = value
        if self._potential_transformer_type_asset is not None:
            self._potential_transformer_type_asset._potential_transformers.append(self)

    potential_transformer_type_asset = property(get_potential_transformer_type_asset, set_potential_transformer_type_asset)
    # >>> potential_transformer_type_asset


    def __str__(self):
        """ Returns a string representation of the PotentialTransformer.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< potential_transformer.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PotentialTransformer.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PotentialTransformer", self.uri)
        if format:
            indent += ' ' * depth

        if self.potential_transformer_asset is not None:
            s += '%s<%s:PotentialTransformer.potential_transformer_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.potential_transformer_asset.uri)
        if self.potential_transformer_type_asset is not None:
            s += '%s<%s:PotentialTransformer.potential_transformer_type_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.potential_transformer_type_asset.uri)
        s += '%s<%s:PotentialTransformer.accuracy_class>%s</%s:PotentialTransformer.accuracy_class>' % \
            (indent, ns_prefix, self.accuracy_class, ns_prefix)
        s += '%s<%s:PotentialTransformer.pt_class>%s</%s:PotentialTransformer.pt_class>' % \
            (indent, ns_prefix, self.pt_class, ns_prefix)
        s += '%s<%s:PotentialTransformer.nominal_ratio>%s</%s:PotentialTransformer.nominal_ratio>' % \
            (indent, ns_prefix, self.nominal_ratio, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.change_items:
            s += '%s<%s:PowerSystemResource.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.asset_roles:
            s += '%s<%s:PowerSystemResource.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        for obj in self.safety_documents:
            s += '%s<%s:PowerSystemResource.safety_documents rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.measurements:
            s += '%s<%s:PowerSystemResource.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:PowerSystemResource.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psrevent:
            s += '%s<%s:PowerSystemResource.psrevent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.schedule_steps:
            s += '%s<%s:PowerSystemResource.schedule_steps rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.document_roles:
            s += '%s<%s:PowerSystemResource.document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.circuit_sections:
            s += '%s<%s:PowerSystemResource.circuit_sections rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:PowerSystemResource.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contingency_equipment:
            s += '%s<%s:Equipment.contingency_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.customer_agreements:
            s += '%s<%s:Equipment.customer_agreements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operational_limit_set:
            s += '%s<%s:Equipment.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PotentialTransformer")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> potential_transformer.serialize


class Limit(IdentifiedObject):
    """ Specifies one limit value for a Measurement. A Measurement typically has several limits that are kept together by the LimitSet class. The actual meaning and use of a Limit instance (i.e., if it is an alarm or warning limit or if it is a high or low limit) is not captured in the Limit class. However the name of a Limit instance may indicate both meaning and use.
    """
    # <<< limit
    # @generated
    def __init__(self, procedures=None, **kw_args):
        """ Initialises a new 'Limit' instance.
        """

        self._procedures = []
        if procedures is not None:
            self.procedures = procedures
        else:
            self.procedures = []


        super(Limit, self).__init__(**kw_args)
    # >>> limit

    # <<< procedures
    # @generated
    def get_procedures(self):
        """ 
        """
        return self._procedures

    def set_procedures(self, value):
        for p in self._procedures:
            filtered = [q for q in p.limits if q != self]
            self._procedures._limits = filtered
        for r in value:
            if self not in r._limits:
                r._limits.append(self)
        self._procedures = value

    procedures = property(get_procedures, set_procedures)

    def add_procedures(self, *procedures):
        for obj in procedures:
            if self not in obj._limits:
                obj._limits.append(self)
            self._procedures.append(obj)

    def remove_procedures(self, *procedures):
        for obj in procedures:
            if self in obj._limits:
                obj._limits.remove(self)
            self._procedures.remove(obj)
    # >>> procedures


    def __str__(self):
        """ Returns a string representation of the Limit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< limit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Limit.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Limit", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.procedures:
            s += '%s<%s:Limit.procedures rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Limit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> limit.serialize


class Measurement(IdentifiedObject):
    """ A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  Two possible paths exist: 1) Measurement-Terminal- ConnectivityNode-Terminal-ConductingEquipment 2) Measurement-Terminal-ConductingEquipment Alternative 2 is the only allowed use.  When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.
    """
    # <<< measurement
    # @generated
    def __init__(self, measurement_type='', asset=None, for_tie_point=None, power_system_resource=None, dynamic_schedules=None, pnode=None, terminal=None, documents=None, locations=None, change_items=None, violation_limits=None, by_tie_point=None, unit=None, **kw_args):
        """ Initialises a new 'Measurement' instance.
        """
        # Specifies the type of Measurement, e.g. IndoorTemperature, OutDoorTemperature, BusVoltage, GeneratorVoltage, LineFlow etc. 
        self.measurement_type = measurement_type


        self._asset = None
        self.asset = asset

        self._for_tie_point = None
        self.for_tie_point = for_tie_point

        self._power_system_resource = None
        self.power_system_resource = power_system_resource

        self._dynamic_schedules = []
        if dynamic_schedules is not None:
            self.dynamic_schedules = dynamic_schedules
        else:
            self.dynamic_schedules = []

        self._pnode = None
        self.pnode = pnode

        self._terminal = None
        self.terminal = terminal

        self._documents = []
        if documents is not None:
            self.documents = documents
        else:
            self.documents = []

        self._locations = []
        if locations is not None:
            self.locations = locations
        else:
            self.locations = []

        self._change_items = []
        if change_items is not None:
            self.change_items = change_items
        else:
            self.change_items = []

        self._violation_limits = []
        if violation_limits is not None:
            self.violation_limits = violation_limits
        else:
            self.violation_limits = []

        self._by_tie_point = None
        self.by_tie_point = by_tie_point

        self._unit = None
        self.unit = unit


        super(Measurement, self).__init__(**kw_args)
    # >>> measurement

    # <<< asset
    # @generated
    def get_asset(self):
        """ 
        """
        return self._asset

    def set_asset(self, value):
        if self._asset is not None:
            filtered = [x for x in self.asset.measurements if x != self]
            self._asset._measurements = filtered

        self._asset = value
        if self._asset is not None:
            self._asset._measurements.append(self)

    asset = property(get_asset, set_asset)
    # >>> asset

    # <<< for_tie_point
    # @generated
    def get_for_tie_point(self):
        """ A measurement is made on the A side of a tie point
        """
        return self._for_tie_point

    def set_for_tie_point(self, value):
        if self._for_tie_point is not None:
            filtered = [x for x in self.for_tie_point.for_measurements if x != self]
            self._for_tie_point._for_measurements = filtered

        self._for_tie_point = value
        if self._for_tie_point is not None:
            self._for_tie_point._for_measurements.append(self)

    for_tie_point = property(get_for_tie_point, set_for_tie_point)
    # >>> for_tie_point

    # <<< power_system_resource
    # @generated
    def get_power_system_resource(self):
        """ The PowerSystemResource that contains the Measurement in the naming hierarchy
        """
        return self._power_system_resource

    def set_power_system_resource(self, value):
        if self._power_system_resource is not None:
            filtered = [x for x in self.power_system_resource.measurements if x != self]
            self._power_system_resource._measurements = filtered

        self._power_system_resource = value
        if self._power_system_resource is not None:
            self._power_system_resource._measurements.append(self)

    power_system_resource = property(get_power_system_resource, set_power_system_resource)
    # >>> power_system_resource

    # <<< dynamic_schedules
    # @generated
    def get_dynamic_schedules(self):
        """ A measurement is a data source for dynamic interchange schedules
        """
        return self._dynamic_schedules

    def set_dynamic_schedules(self, value):
        for x in self._dynamic_schedules:
            x._measurement = None
        for y in value:
            y._measurement = self
        self._dynamic_schedules = value

    dynamic_schedules = property(get_dynamic_schedules, set_dynamic_schedules)

    def add_dynamic_schedules(self, *dynamic_schedules):
        for obj in dynamic_schedules:
            obj._measurement = self
            self._dynamic_schedules.append(obj)

    def remove_dynamic_schedules(self, *dynamic_schedules):
        for obj in dynamic_schedules:
            obj._measurement = None
            self._dynamic_schedules.remove(obj)
    # >>> dynamic_schedules

    # <<< pnode
    # @generated
    def get_pnode(self):
        """ 
        """
        return self._pnode

    def set_pnode(self, value):
        if self._pnode is not None:
            filtered = [x for x in self.pnode.measurements if x != self]
            self._pnode._measurements = filtered

        self._pnode = value
        if self._pnode is not None:
            self._pnode._measurements.append(self)

    pnode = property(get_pnode, set_pnode)
    # >>> pnode

    # <<< terminal
    # @generated
    def get_terminal(self):
        """ One or more measurements may be associated with a terminal in the network
        """
        return self._terminal

    def set_terminal(self, value):
        if self._terminal is not None:
            filtered = [x for x in self.terminal.measurements if x != self]
            self._terminal._measurements = filtered

        self._terminal = value
        if self._terminal is not None:
            self._terminal._measurements.append(self)

    terminal = property(get_terminal, set_terminal)
    # >>> terminal

    # <<< documents
    # @generated
    def get_documents(self):
        """ Measurements are specified in types of documents, such as procedures.
        """
        return self._documents

    def set_documents(self, value):
        for p in self._documents:
            filtered = [q for q in p.measurements if q != self]
            self._documents._measurements = filtered
        for r in value:
            if self not in r._measurements:
                r._measurements.append(self)
        self._documents = value

    documents = property(get_documents, set_documents)

    def add_documents(self, *documents):
        for obj in documents:
            if self not in obj._measurements:
                obj._measurements.append(self)
            self._documents.append(obj)

    def remove_documents(self, *documents):
        for obj in documents:
            if self in obj._measurements:
                obj._measurements.remove(self)
            self._documents.remove(obj)
    # >>> documents

    # <<< locations
    # @generated
    def get_locations(self):
        """ 
        """
        return self._locations

    def set_locations(self, value):
        for p in self._locations:
            filtered = [q for q in p.measurements if q != self]
            self._locations._measurements = filtered
        for r in value:
            if self not in r._measurements:
                r._measurements.append(self)
        self._locations = value

    locations = property(get_locations, set_locations)

    def add_locations(self, *locations):
        for obj in locations:
            if self not in obj._measurements:
                obj._measurements.append(self)
            self._locations.append(obj)

    def remove_locations(self, *locations):
        for obj in locations:
            if self in obj._measurements:
                obj._measurements.remove(self)
            self._locations.remove(obj)
    # >>> locations

    # <<< change_items
    # @generated
    def get_change_items(self):
        """ 
        """
        return self._change_items

    def set_change_items(self, value):
        for x in self._change_items:
            x._measurement = None
        for y in value:
            y._measurement = self
        self._change_items = value

    change_items = property(get_change_items, set_change_items)

    def add_change_items(self, *change_items):
        for obj in change_items:
            obj._measurement = self
            self._change_items.append(obj)

    def remove_change_items(self, *change_items):
        for obj in change_items:
            obj._measurement = None
            self._change_items.remove(obj)
    # >>> change_items

    # <<< violation_limits
    # @generated
    def get_violation_limits(self):
        """ 
        """
        return self._violation_limits

    def set_violation_limits(self, value):
        for x in self._violation_limits:
            x._measurement = None
        for y in value:
            y._measurement = self
        self._violation_limits = value

    violation_limits = property(get_violation_limits, set_violation_limits)

    def add_violation_limits(self, *violation_limits):
        for obj in violation_limits:
            obj._measurement = self
            self._violation_limits.append(obj)

    def remove_violation_limits(self, *violation_limits):
        for obj in violation_limits:
            obj._measurement = None
            self._violation_limits.remove(obj)
    # >>> violation_limits

    # <<< by_tie_point
    # @generated
    def get_by_tie_point(self):
        """ A measurement is made on the B side of a tie point
        """
        return self._by_tie_point

    def set_by_tie_point(self, value):
        if self._by_tie_point is not None:
            filtered = [x for x in self.by_tie_point.by_measurements if x != self]
            self._by_tie_point._by_measurements = filtered

        self._by_tie_point = value
        if self._by_tie_point is not None:
            self._by_tie_point._by_measurements.append(self)

    by_tie_point = property(get_by_tie_point, set_by_tie_point)
    # >>> by_tie_point

    # <<< unit
    # @generated
    def get_unit(self):
        """ The Unit for the Measurement
        """
        return self._unit

    def set_unit(self, value):
        if self._unit is not None:
            filtered = [x for x in self.unit.measurements if x != self]
            self._unit._measurements = filtered

        self._unit = value
        if self._unit is not None:
            self._unit._measurements.append(self)

    unit = property(get_unit, set_unit)
    # >>> unit


    def __str__(self):
        """ Returns a string representation of the Measurement.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< measurement.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Measurement.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Measurement", self.uri)
        if format:
            indent += ' ' * depth

        if self.asset is not None:
            s += '%s<%s:Measurement.asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset.uri)
        if self.for_tie_point is not None:
            s += '%s<%s:Measurement.for_tie_point rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.for_tie_point.uri)
        if self.power_system_resource is not None:
            s += '%s<%s:Measurement.power_system_resource rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.power_system_resource.uri)
        for obj in self.dynamic_schedules:
            s += '%s<%s:Measurement.dynamic_schedules rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.pnode is not None:
            s += '%s<%s:Measurement.pnode rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.pnode.uri)
        if self.terminal is not None:
            s += '%s<%s:Measurement.terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.terminal.uri)
        for obj in self.documents:
            s += '%s<%s:Measurement.documents rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.locations:
            s += '%s<%s:Measurement.locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Measurement.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.violation_limits:
            s += '%s<%s:Measurement.violation_limits rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.by_tie_point is not None:
            s += '%s<%s:Measurement.by_tie_point rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.by_tie_point.uri)
        if self.unit is not None:
            s += '%s<%s:Measurement.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)
        s += '%s<%s:Measurement.measurement_type>%s</%s:Measurement.measurement_type>' % \
            (indent, ns_prefix, self.measurement_type, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Measurement")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> measurement.serialize


class Control(IdentifiedObject):
    """ Control is used for supervisory/device control. It represents control outputs that are used to change the state in a process, e.g. close or open breaker, a set point value or a raise lower command.
    """
    # <<< control
    # @generated
    def __init__(self, time_stamp='', operation_in_progress=False, remote_control=None, unit=None, regulating_cond_eq=None, control_type=None, **kw_args):
        """ Initialises a new 'Control' instance.
        """
        # The last time a control output was sent 
        self.time_stamp = time_stamp

        # Indicates that a client is currently sending control commands that has not completed 
        self.operation_in_progress = operation_in_progress


        self._remote_control = None
        self.remote_control = remote_control

        self._unit = None
        self.unit = unit

        self._regulating_cond_eq = None
        self.regulating_cond_eq = regulating_cond_eq

        self._control_type = None
        self.control_type = control_type


        super(Control, self).__init__(**kw_args)
    # >>> control

    # <<< remote_control
    # @generated
    def get_remote_control(self):
        """ The remote point controlling the physical actuator.
        """
        return self._remote_control

    def set_remote_control(self, value):
        if self._remote_control is not None:
            self._remote_control._control = None

        self._remote_control = value
        if self._remote_control is not None:
            self._remote_control._control = self

    remote_control = property(get_remote_control, set_remote_control)
    # >>> remote_control

    # <<< unit
    # @generated
    def get_unit(self):
        """ The Unit for the Control.
        """
        return self._unit

    def set_unit(self, value):
        if self._unit is not None:
            filtered = [x for x in self.unit.controls if x != self]
            self._unit._controls = filtered

        self._unit = value
        if self._unit is not None:
            self._unit._controls.append(self)

    unit = property(get_unit, set_unit)
    # >>> unit

    # <<< regulating_cond_eq
    # @generated
    def get_regulating_cond_eq(self):
        """ Regulating device governed by this control output.
        """
        return self._regulating_cond_eq

    def set_regulating_cond_eq(self, value):
        if self._regulating_cond_eq is not None:
            filtered = [x for x in self.regulating_cond_eq.controls if x != self]
            self._regulating_cond_eq._controls = filtered

        self._regulating_cond_eq = value
        if self._regulating_cond_eq is not None:
            self._regulating_cond_eq._controls.append(self)

    regulating_cond_eq = property(get_regulating_cond_eq, set_regulating_cond_eq)
    # >>> regulating_cond_eq

    # <<< control_type
    # @generated
    def get_control_type(self):
        """ The type of Control
        """
        return self._control_type

    def set_control_type(self, value):
        if self._control_type is not None:
            filtered = [x for x in self.control_type.controls if x != self]
            self._control_type._controls = filtered

        self._control_type = value
        if self._control_type is not None:
            self._control_type._controls.append(self)

    control_type = property(get_control_type, set_control_type)
    # >>> control_type


    def __str__(self):
        """ Returns a string representation of the Control.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< control.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Control.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Control", self.uri)
        if format:
            indent += ' ' * depth

        if self.remote_control is not None:
            s += '%s<%s:Control.remote_control rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.remote_control.uri)
        if self.unit is not None:
            s += '%s<%s:Control.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)
        if self.regulating_cond_eq is not None:
            s += '%s<%s:Control.regulating_cond_eq rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.regulating_cond_eq.uri)
        if self.control_type is not None:
            s += '%s<%s:Control.control_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.control_type.uri)
        s += '%s<%s:Control.time_stamp>%s</%s:Control.time_stamp>' % \
            (indent, ns_prefix, self.time_stamp, ns_prefix)
        s += '%s<%s:Control.operation_in_progress>%s</%s:Control.operation_in_progress>' % \
            (indent, ns_prefix, self.operation_in_progress, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Control")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> control.serialize


class ValueToAlias(IdentifiedObject):
    """ Describes the translation of one particular value into a name, e.g. 1->'Open'
    """
    # <<< value_to_alias
    # @generated
    def __init__(self, value=0, value_alias_set=None, **kw_args):
        """ Initialises a new 'ValueToAlias' instance.
        """
        # The value that is mapped 
        self.value = value


        self._value_alias_set = None
        self.value_alias_set = value_alias_set


        super(ValueToAlias, self).__init__(**kw_args)
    # >>> value_to_alias

    # <<< value_alias_set
    # @generated
    def get_value_alias_set(self):
        """ The ValueAliasSet having the ValueToAlias mappings
        """
        return self._value_alias_set

    def set_value_alias_set(self, value):
        if self._value_alias_set is not None:
            filtered = [x for x in self.value_alias_set.values if x != self]
            self._value_alias_set._values = filtered

        self._value_alias_set = value
        if self._value_alias_set is not None:
            self._value_alias_set._values.append(self)

    value_alias_set = property(get_value_alias_set, set_value_alias_set)
    # >>> value_alias_set


    def __str__(self):
        """ Returns a string representation of the ValueToAlias.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< value_to_alias.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ValueToAlias.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ValueToAlias", self.uri)
        if format:
            indent += ' ' * depth

        if self.value_alias_set is not None:
            s += '%s<%s:ValueToAlias.value_alias_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.value_alias_set.uri)
        s += '%s<%s:ValueToAlias.value>%s</%s:ValueToAlias.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ValueToAlias")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> value_to_alias.serialize


class Quality61850(Element):
    """ Quality flags in this class are as defined in IEC 61850, except for estimatorReplaced, which has been included in this class for convenience.
    """
    # <<< quality61850
    # @generated
    def __init__(self, source='substituted', validity='good', test=False, over_flow=False, estimator_replaced=False, suspect=False, bad_reference=False, operator_blocked=False, oscillatory=False, failure=False, old_data=False, out_of_range=False, **kw_args):
        """ Initialises a new 'Quality61850' instance.
        """
        # Source gives information related to the origin of a value. The value may be acquired from the process, defaulted or substituted. Values are: "substituted", "process", "defaulted"
        self.source = 'substituted'

        # Validity of the measurement value. Values are: "good", "invalid", "questionable"
        self.validity = 'good'

        # Measurement value is transmitted for test purposes. 
        self.test = test

        # Measurement value is beyond the capability of being  represented properly. For example, a counter value overflows from maximum count back to a value of zero. 
        self.over_flow = over_flow

        # Value has been replaced by State Estimator. estimatorReplaced is not an IEC61850 quality bit but has been put in this class for convenience. 
        self.estimator_replaced = estimator_replaced

        # A correlation function has detected that the value is not consitent with other values. Typically set by a network State Estimator. 
        self.suspect = suspect

        # Measurement value may be incorrect due to a reference being out of calibration. 
        self.bad_reference = bad_reference

        # Measurement value is blocked and hence unavailable for transmission. 
        self.operator_blocked = operator_blocked

        # To prevent some overload of the communication it is sensible to detect and suppress oscillating (fast changing) binary inputs. If a signal changes in a defined time (tosc) twice in the same direction (from 0 to 1 or from 1 to 0) then oscillation is detected and the detail quality identifier 'oscillatory' is set. If it is detected a configured numbers of transient changes could be passed by. In this time the validity status 'questionable' is set. If after this defined numbers of changes the signal is still in the oscillating state the value shall be set either to the opposite state of the previous stable value or to a defined default value. In this case the validity status 'questionable' is reset and 'invalid' is set as long as the signal is oscillating. If it is configured such that no transient changes should be passed by then the validity status 'invalid' is set immediately in addition to the detail quality identifier 'oscillatory' (used for status information only). 
        self.oscillatory = oscillatory

        # This identifier indicates that a supervision function has detected an internal or external failure, e.g. communication failure. 
        self.failure = failure

        # Measurement value is old and possibly invalid, as it has not been successfully updated during a specified time interval. 
        self.old_data = old_data

        # Measurement value is beyond a predefined range of value. 
        self.out_of_range = out_of_range



        super(Quality61850, self).__init__(**kw_args)
    # >>> quality61850


    def __str__(self):
        """ Returns a string representation of the Quality61850.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< quality61850.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Quality61850.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Quality61850", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:Quality61850.source>%s</%s:Quality61850.source>' % \
            (indent, ns_prefix, self.source, ns_prefix)
        s += '%s<%s:Quality61850.validity>%s</%s:Quality61850.validity>' % \
            (indent, ns_prefix, self.validity, ns_prefix)
        s += '%s<%s:Quality61850.test>%s</%s:Quality61850.test>' % \
            (indent, ns_prefix, self.test, ns_prefix)
        s += '%s<%s:Quality61850.over_flow>%s</%s:Quality61850.over_flow>' % \
            (indent, ns_prefix, self.over_flow, ns_prefix)
        s += '%s<%s:Quality61850.estimator_replaced>%s</%s:Quality61850.estimator_replaced>' % \
            (indent, ns_prefix, self.estimator_replaced, ns_prefix)
        s += '%s<%s:Quality61850.suspect>%s</%s:Quality61850.suspect>' % \
            (indent, ns_prefix, self.suspect, ns_prefix)
        s += '%s<%s:Quality61850.bad_reference>%s</%s:Quality61850.bad_reference>' % \
            (indent, ns_prefix, self.bad_reference, ns_prefix)
        s += '%s<%s:Quality61850.operator_blocked>%s</%s:Quality61850.operator_blocked>' % \
            (indent, ns_prefix, self.operator_blocked, ns_prefix)
        s += '%s<%s:Quality61850.oscillatory>%s</%s:Quality61850.oscillatory>' % \
            (indent, ns_prefix, self.oscillatory, ns_prefix)
        s += '%s<%s:Quality61850.failure>%s</%s:Quality61850.failure>' % \
            (indent, ns_prefix, self.failure, ns_prefix)
        s += '%s<%s:Quality61850.old_data>%s</%s:Quality61850.old_data>' % \
            (indent, ns_prefix, self.old_data, ns_prefix)
        s += '%s<%s:Quality61850.out_of_range>%s</%s:Quality61850.out_of_range>' % \
            (indent, ns_prefix, self.out_of_range, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Quality61850")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> quality61850.serialize


class MeasurementValueSource(IdentifiedObject):
    """ MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301.
    """
    # <<< measurement_value_source
    # @generated
    def __init__(self, measurement_values=None, **kw_args):
        """ Initialises a new 'MeasurementValueSource' instance.
        """

        self._measurement_values = []
        if measurement_values is not None:
            self.measurement_values = measurement_values
        else:
            self.measurement_values = []


        super(MeasurementValueSource, self).__init__(**kw_args)
    # >>> measurement_value_source

    # <<< measurement_values
    # @generated
    def get_measurement_values(self):
        """ The MeasurementValues updated by the source
        """
        return self._measurement_values

    def set_measurement_values(self, value):
        for x in self._measurement_values:
            x._measurement_value_source = None
        for y in value:
            y._measurement_value_source = self
        self._measurement_values = value

    measurement_values = property(get_measurement_values, set_measurement_values)

    def add_measurement_values(self, *measurement_values):
        for obj in measurement_values:
            obj._measurement_value_source = self
            self._measurement_values.append(obj)

    def remove_measurement_values(self, *measurement_values):
        for obj in measurement_values:
            obj._measurement_value_source = None
            self._measurement_values.remove(obj)
    # >>> measurement_values


    def __str__(self):
        """ Returns a string representation of the MeasurementValueSource.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< measurement_value_source.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MeasurementValueSource.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MeasurementValueSource", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.measurement_values:
            s += '%s<%s:MeasurementValueSource.measurement_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MeasurementValueSource")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> measurement_value_source.serialize


class CurrentTransformer(Equipment):
    """ Instrument transformer used to measure electrical qualities of the circuit that is being protected and/or monitored. Typically used as current transducer for the purpose of metering or protection. A typical secondary current rating would be 5A.
    """
    # <<< current_transformer
    # @generated
    def __init__(self, accuracy_class='', accuracy_limit='', usage='', core_count=0, max_ratio=0.0, ct_class='', current_transformer_type_asset=None, current_transformer_asset=None, **kw_args):
        """ Initialises a new 'CurrentTransformer' instance.
        """
        # CT accuracy classification. 
        self.accuracy_class = accuracy_class

        # Percent of rated current for which the CT remains accurate within specified limits. 
        self.accuracy_limit = accuracy_limit

        # Intended usage of the CT; i.e. metering, protection. 
        self.usage = usage

        # Number of cores. 
        self.core_count = core_count

        # For multi-ratio CT's, the maximum permissable ratio attainable. 
        self.max_ratio = max_ratio

        # CT classification; i.e. class 10P. 
        self.ct_class = ct_class


        self._current_transformer_type_asset = None
        self.current_transformer_type_asset = current_transformer_type_asset

        self._current_transformer_asset = None
        self.current_transformer_asset = current_transformer_asset


        super(CurrentTransformer, self).__init__(**kw_args)
    # >>> current_transformer

    # <<< current_transformer_type_asset
    # @generated
    def get_current_transformer_type_asset(self):
        """ 
        """
        return self._current_transformer_type_asset

    def set_current_transformer_type_asset(self, value):
        if self._current_transformer_type_asset is not None:
            filtered = [x for x in self.current_transformer_type_asset.current_transformers if x != self]
            self._current_transformer_type_asset._current_transformers = filtered

        self._current_transformer_type_asset = value
        if self._current_transformer_type_asset is not None:
            self._current_transformer_type_asset._current_transformers.append(self)

    current_transformer_type_asset = property(get_current_transformer_type_asset, set_current_transformer_type_asset)
    # >>> current_transformer_type_asset

    # <<< current_transformer_asset
    # @generated
    def get_current_transformer_asset(self):
        """ 
        """
        return self._current_transformer_asset

    def set_current_transformer_asset(self, value):
        if self._current_transformer_asset is not None:
            self._current_transformer_asset._current_transformer = None

        self._current_transformer_asset = value
        if self._current_transformer_asset is not None:
            self._current_transformer_asset._current_transformer = self

    current_transformer_asset = property(get_current_transformer_asset, set_current_transformer_asset)
    # >>> current_transformer_asset


    def __str__(self):
        """ Returns a string representation of the CurrentTransformer.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< current_transformer.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CurrentTransformer.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CurrentTransformer", self.uri)
        if format:
            indent += ' ' * depth

        if self.current_transformer_type_asset is not None:
            s += '%s<%s:CurrentTransformer.current_transformer_type_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.current_transformer_type_asset.uri)
        if self.current_transformer_asset is not None:
            s += '%s<%s:CurrentTransformer.current_transformer_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.current_transformer_asset.uri)
        s += '%s<%s:CurrentTransformer.accuracy_class>%s</%s:CurrentTransformer.accuracy_class>' % \
            (indent, ns_prefix, self.accuracy_class, ns_prefix)
        s += '%s<%s:CurrentTransformer.accuracy_limit>%s</%s:CurrentTransformer.accuracy_limit>' % \
            (indent, ns_prefix, self.accuracy_limit, ns_prefix)
        s += '%s<%s:CurrentTransformer.usage>%s</%s:CurrentTransformer.usage>' % \
            (indent, ns_prefix, self.usage, ns_prefix)
        s += '%s<%s:CurrentTransformer.core_count>%s</%s:CurrentTransformer.core_count>' % \
            (indent, ns_prefix, self.core_count, ns_prefix)
        s += '%s<%s:CurrentTransformer.max_ratio>%s</%s:CurrentTransformer.max_ratio>' % \
            (indent, ns_prefix, self.max_ratio, ns_prefix)
        s += '%s<%s:CurrentTransformer.ct_class>%s</%s:CurrentTransformer.ct_class>' % \
            (indent, ns_prefix, self.ct_class, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.change_items:
            s += '%s<%s:PowerSystemResource.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.asset_roles:
            s += '%s<%s:PowerSystemResource.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        for obj in self.safety_documents:
            s += '%s<%s:PowerSystemResource.safety_documents rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.measurements:
            s += '%s<%s:PowerSystemResource.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:PowerSystemResource.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psrevent:
            s += '%s<%s:PowerSystemResource.psrevent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.schedule_steps:
            s += '%s<%s:PowerSystemResource.schedule_steps rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.document_roles:
            s += '%s<%s:PowerSystemResource.document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.circuit_sections:
            s += '%s<%s:PowerSystemResource.circuit_sections rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:PowerSystemResource.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contingency_equipment:
            s += '%s<%s:Equipment.contingency_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.customer_agreements:
            s += '%s<%s:Equipment.customer_agreements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operational_limit_set:
            s += '%s<%s:Equipment.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CurrentTransformer")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> current_transformer.serialize


class ControlType(IdentifiedObject):
    """ Specifies the type of Control, e.g. BreakerOn/Off, GeneratorVoltageSetPoint, TieLineFlow etc. The ControlType.name shall be unique among all specified types and describe the type. The ControlType.aliasName is meant to be used for localization.
    """
    # <<< control_type
    # @generated
    def __init__(self, controls=None, **kw_args):
        """ Initialises a new 'ControlType' instance.
        """

        self._controls = []
        if controls is not None:
            self.controls = controls
        else:
            self.controls = []


        super(ControlType, self).__init__(**kw_args)
    # >>> control_type

    # <<< controls
    # @generated
    def get_controls(self):
        """ The Controls having the ControlType
        """
        return self._controls

    def set_controls(self, value):
        for x in self._controls:
            x._control_type = None
        for y in value:
            y._control_type = self
        self._controls = value

    controls = property(get_controls, set_controls)

    def add_controls(self, *controls):
        for obj in controls:
            obj._control_type = self
            self._controls.append(obj)

    def remove_controls(self, *controls):
        for obj in controls:
            obj._control_type = None
            self._controls.remove(obj)
    # >>> controls


    def __str__(self):
        """ Returns a string representation of the ControlType.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< control_type.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ControlType.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ControlType", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.controls:
            s += '%s<%s:ControlType.controls rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ControlType")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> control_type.serialize


class AccumulatorLimitSet(LimitSet):
    """ An AccumulatorLimitSet specifies a set of Limits that are associated with an Accumulator measurement.
    """
    # <<< accumulator_limit_set
    # @generated
    def __init__(self, measurements=None, limits=None, **kw_args):
        """ Initialises a new 'AccumulatorLimitSet' instance.
        """

        self._measurements = []
        if measurements is not None:
            self.measurements = measurements
        else:
            self.measurements = []

        self._limits = []
        if limits is not None:
            self.limits = limits
        else:
            self.limits = []


        super(AccumulatorLimitSet, self).__init__(**kw_args)
    # >>> accumulator_limit_set

    # <<< measurements
    # @generated
    def get_measurements(self):
        """ The Measurements using the LimitSet.
        """
        return self._measurements

    def set_measurements(self, value):
        for p in self._measurements:
            filtered = [q for q in p.limit_sets if q != self]
            self._measurements._limit_sets = filtered
        for r in value:
            if self not in r._limit_sets:
                r._limit_sets.append(self)
        self._measurements = value

    measurements = property(get_measurements, set_measurements)

    def add_measurements(self, *measurements):
        for obj in measurements:
            if self not in obj._limit_sets:
                obj._limit_sets.append(self)
            self._measurements.append(obj)

    def remove_measurements(self, *measurements):
        for obj in measurements:
            if self in obj._limit_sets:
                obj._limit_sets.remove(self)
            self._measurements.remove(obj)
    # >>> measurements

    # <<< limits
    # @generated
    def get_limits(self):
        """ The limit values used for supervision of Measurements.
        """
        return self._limits

    def set_limits(self, value):
        for x in self._limits:
            x._limit_set = None
        for y in value:
            y._limit_set = self
        self._limits = value

    limits = property(get_limits, set_limits)

    def add_limits(self, *limits):
        for obj in limits:
            obj._limit_set = self
            self._limits.append(obj)

    def remove_limits(self, *limits):
        for obj in limits:
            obj._limit_set = None
            self._limits.remove(obj)
    # >>> limits


    def __str__(self):
        """ Returns a string representation of the AccumulatorLimitSet.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< accumulator_limit_set.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AccumulatorLimitSet.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AccumulatorLimitSet", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.measurements:
            s += '%s<%s:AccumulatorLimitSet.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.limits:
            s += '%s<%s:AccumulatorLimitSet.limits rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:LimitSet.is_percentage_limits>%s</%s:LimitSet.is_percentage_limits>' % \
            (indent, ns_prefix, self.is_percentage_limits, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "AccumulatorLimitSet")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> accumulator_limit_set.serialize


class AnalogLimitSet(LimitSet):
    """ An AnalogLimitSet specifies a set of Limits that are associated with an Analog measurement.
    """
    # <<< analog_limit_set
    # @generated
    def __init__(self, limits=None, measurements=None, **kw_args):
        """ Initialises a new 'AnalogLimitSet' instance.
        """

        self._limits = []
        if limits is not None:
            self.limits = limits
        else:
            self.limits = []

        self._measurements = []
        if measurements is not None:
            self.measurements = measurements
        else:
            self.measurements = []


        super(AnalogLimitSet, self).__init__(**kw_args)
    # >>> analog_limit_set

    # <<< limits
    # @generated
    def get_limits(self):
        """ The limit values used for supervision of Measurements.
        """
        return self._limits

    def set_limits(self, value):
        for x in self._limits:
            x._limit_set = None
        for y in value:
            y._limit_set = self
        self._limits = value

    limits = property(get_limits, set_limits)

    def add_limits(self, *limits):
        for obj in limits:
            obj._limit_set = self
            self._limits.append(obj)

    def remove_limits(self, *limits):
        for obj in limits:
            obj._limit_set = None
            self._limits.remove(obj)
    # >>> limits

    # <<< measurements
    # @generated
    def get_measurements(self):
        """ The Measurements using the LimitSet.
        """
        return self._measurements

    def set_measurements(self, value):
        for p in self._measurements:
            filtered = [q for q in p.limit_sets if q != self]
            self._measurements._limit_sets = filtered
        for r in value:
            if self not in r._limit_sets:
                r._limit_sets.append(self)
        self._measurements = value

    measurements = property(get_measurements, set_measurements)

    def add_measurements(self, *measurements):
        for obj in measurements:
            if self not in obj._limit_sets:
                obj._limit_sets.append(self)
            self._measurements.append(obj)

    def remove_measurements(self, *measurements):
        for obj in measurements:
            if self in obj._limit_sets:
                obj._limit_sets.remove(self)
            self._measurements.remove(obj)
    # >>> measurements


    def __str__(self):
        """ Returns a string representation of the AnalogLimitSet.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< analog_limit_set.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AnalogLimitSet.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AnalogLimitSet", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.limits:
            s += '%s<%s:AnalogLimitSet.limits rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:AnalogLimitSet.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:LimitSet.is_percentage_limits>%s</%s:LimitSet.is_percentage_limits>' % \
            (indent, ns_prefix, self.is_percentage_limits, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "AnalogLimitSet")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> analog_limit_set.serialize


class AccumulatorValue(MeasurementValue):
    """ AccumulatorValue represents a accumulated (counted) MeasurementValue.
    """
    # <<< accumulator_value
    # @generated
    def __init__(self, value=0, accumulator=None, **kw_args):
        """ Initialises a new 'AccumulatorValue' instance.
        """
        # The value to supervise. The value is positive. 
        self.value = value


        self._accumulator = None
        self.accumulator = accumulator


        super(AccumulatorValue, self).__init__(**kw_args)
    # >>> accumulator_value

    # <<< accumulator
    # @generated
    def get_accumulator(self):
        """ Measurement to which this value is connected.
        """
        return self._accumulator

    def set_accumulator(self, value):
        if self._accumulator is not None:
            filtered = [x for x in self.accumulator.accumulator_values if x != self]
            self._accumulator._accumulator_values = filtered

        self._accumulator = value
        if self._accumulator is not None:
            self._accumulator._accumulator_values.append(self)

    accumulator = property(get_accumulator, set_accumulator)
    # >>> accumulator


    def __str__(self):
        """ Returns a string representation of the AccumulatorValue.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< accumulator_value.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AccumulatorValue.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AccumulatorValue", self.uri)
        if format:
            indent += ' ' * depth

        if self.accumulator is not None:
            s += '%s<%s:AccumulatorValue.accumulator rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.accumulator.uri)
        s += '%s<%s:AccumulatorValue.value>%s</%s:AccumulatorValue.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.gml_values:
            s += '%s<%s:MeasurementValue.gml_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.measurement_value_source is not None:
            s += '%s<%s:MeasurementValue.measurement_value_source rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value_source.uri)
        if self.erp_person is not None:
            s += '%s<%s:MeasurementValue.erp_person rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_person.uri)
        for obj in self.procedure_data_sets:
            s += '%s<%s:MeasurementValue.procedure_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.remote_source is not None:
            s += '%s<%s:MeasurementValue.remote_source rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.remote_source.uri)
        if self.measurement_value_quality is not None:
            s += '%s<%s:MeasurementValue.measurement_value_quality rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value_quality.uri)
        s += '%s<%s:MeasurementValue.sensor_accuracy>%s</%s:MeasurementValue.sensor_accuracy>' % \
            (indent, ns_prefix, self.sensor_accuracy, ns_prefix)
        s += '%s<%s:MeasurementValue.time_stamp>%s</%s:MeasurementValue.time_stamp>' % \
            (indent, ns_prefix, self.time_stamp, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "AccumulatorValue")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> accumulator_value.serialize


class AccumulatorLimit(Limit):
    """ Limit values for Accumulator measurements
    """
    # <<< accumulator_limit
    # @generated
    def __init__(self, value=0, limit_set=None, **kw_args):
        """ Initialises a new 'AccumulatorLimit' instance.
        """
        # The value to supervise against. The value is positive. 
        self.value = value


        self._limit_set = None
        self.limit_set = limit_set


        super(AccumulatorLimit, self).__init__(**kw_args)
    # >>> accumulator_limit

    # <<< limit_set
    # @generated
    def get_limit_set(self):
        """ The set of limits.
        """
        return self._limit_set

    def set_limit_set(self, value):
        if self._limit_set is not None:
            filtered = [x for x in self.limit_set.limits if x != self]
            self._limit_set._limits = filtered

        self._limit_set = value
        if self._limit_set is not None:
            self._limit_set._limits.append(self)

    limit_set = property(get_limit_set, set_limit_set)
    # >>> limit_set


    def __str__(self):
        """ Returns a string representation of the AccumulatorLimit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< accumulator_limit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AccumulatorLimit.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AccumulatorLimit", self.uri)
        if format:
            indent += ' ' * depth

        if self.limit_set is not None:
            s += '%s<%s:AccumulatorLimit.limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.limit_set.uri)
        s += '%s<%s:AccumulatorLimit.value>%s</%s:AccumulatorLimit.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.procedures:
            s += '%s<%s:Limit.procedures rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "AccumulatorLimit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> accumulator_limit.serialize


class Analog(Measurement):
    """ Analog represents an analog Measurement.
    """
    # <<< analog
    # @generated
    def __init__(self, max_value=0.0, positive_flow_in=False, normal_value=0.0, min_value=0.0, analog_values=None, limit_sets=None, set_point=None, **kw_args):
        """ Initialises a new 'Analog' instance.
        """
        # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values. 
        self.max_value = max_value

        # If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource. 
        self.positive_flow_in = positive_flow_in

        # Normal measurement value, e.g., used for percentage calculations. 
        self.normal_value = normal_value

        # Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values 
        self.min_value = min_value


        self._analog_values = []
        if analog_values is not None:
            self.analog_values = analog_values
        else:
            self.analog_values = []

        self._limit_sets = []
        if limit_sets is not None:
            self.limit_sets = limit_sets
        else:
            self.limit_sets = []

        self._set_point = None
        self.set_point = set_point


        super(Analog, self).__init__(**kw_args)
    # >>> analog

    # <<< analog_values
    # @generated
    def get_analog_values(self):
        """ The values connected to this measurement.
        """
        return self._analog_values

    def set_analog_values(self, value):
        for x in self._analog_values:
            x._analog = None
        for y in value:
            y._analog = self
        self._analog_values = value

    analog_values = property(get_analog_values, set_analog_values)

    def add_analog_values(self, *analog_values):
        for obj in analog_values:
            obj._analog = self
            self._analog_values.append(obj)

    def remove_analog_values(self, *analog_values):
        for obj in analog_values:
            obj._analog = None
            self._analog_values.remove(obj)
    # >>> analog_values

    # <<< limit_sets
    # @generated
    def get_limit_sets(self):
        """ A measurement may have zero or more limit ranges defined for it.
        """
        return self._limit_sets

    def set_limit_sets(self, value):
        for p in self._limit_sets:
            filtered = [q for q in p.measurements if q != self]
            self._limit_sets._measurements = filtered
        for r in value:
            if self not in r._measurements:
                r._measurements.append(self)
        self._limit_sets = value

    limit_sets = property(get_limit_sets, set_limit_sets)

    def add_limit_sets(self, *limit_sets):
        for obj in limit_sets:
            if self not in obj._measurements:
                obj._measurements.append(self)
            self._limit_sets.append(obj)

    def remove_limit_sets(self, *limit_sets):
        for obj in limit_sets:
            if self in obj._measurements:
                obj._measurements.remove(self)
            self._limit_sets.remove(obj)
    # >>> limit_sets

    # <<< set_point
    # @generated
    def get_set_point(self):
        """ The Control variable associated with the Measurement
        """
        return self._set_point

    def set_set_point(self, value):
        if self._set_point is not None:
            self._set_point._analog = None

        self._set_point = value
        if self._set_point is not None:
            self._set_point._analog = self

    set_point = property(get_set_point, set_set_point)
    # >>> set_point


    def __str__(self):
        """ Returns a string representation of the Analog.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< analog.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Analog.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Analog", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.analog_values:
            s += '%s<%s:Analog.analog_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.limit_sets:
            s += '%s<%s:Analog.limit_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.set_point is not None:
            s += '%s<%s:Analog.set_point rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.set_point.uri)
        s += '%s<%s:Analog.max_value>%s</%s:Analog.max_value>' % \
            (indent, ns_prefix, self.max_value, ns_prefix)
        s += '%s<%s:Analog.positive_flow_in>%s</%s:Analog.positive_flow_in>' % \
            (indent, ns_prefix, self.positive_flow_in, ns_prefix)
        s += '%s<%s:Analog.normal_value>%s</%s:Analog.normal_value>' % \
            (indent, ns_prefix, self.normal_value, ns_prefix)
        s += '%s<%s:Analog.min_value>%s</%s:Analog.min_value>' % \
            (indent, ns_prefix, self.min_value, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.asset is not None:
            s += '%s<%s:Measurement.asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset.uri)
        if self.for_tie_point is not None:
            s += '%s<%s:Measurement.for_tie_point rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.for_tie_point.uri)
        if self.power_system_resource is not None:
            s += '%s<%s:Measurement.power_system_resource rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.power_system_resource.uri)
        for obj in self.dynamic_schedules:
            s += '%s<%s:Measurement.dynamic_schedules rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.pnode is not None:
            s += '%s<%s:Measurement.pnode rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.pnode.uri)
        if self.terminal is not None:
            s += '%s<%s:Measurement.terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.terminal.uri)
        for obj in self.documents:
            s += '%s<%s:Measurement.documents rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.locations:
            s += '%s<%s:Measurement.locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Measurement.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.violation_limits:
            s += '%s<%s:Measurement.violation_limits rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.by_tie_point is not None:
            s += '%s<%s:Measurement.by_tie_point rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.by_tie_point.uri)
        if self.unit is not None:
            s += '%s<%s:Measurement.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)
        s += '%s<%s:Measurement.measurement_type>%s</%s:Measurement.measurement_type>' % \
            (indent, ns_prefix, self.measurement_type, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Analog")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> analog.serialize


class SetPoint(Control):
    """ A SetPoint is an analog control used for supervisory control.
    """
    # <<< set_point
    # @generated
    def __init__(self, min_value=0.0, normal_value=0.0, value=0.0, max_value=0.0, analog=None, **kw_args):
        """ Initialises a new 'SetPoint' instance.
        """
        # Normal value range minimum for any of the Control.value. Used for scaling, e.g. in bar graphs. 
        self.min_value = min_value

        # Normal value for Control.value e.g. used for percentage scaling 
        self.normal_value = normal_value

        # The value representing the actuator output 
        self.value = value

        # Normal value range maximum for any of the Control.value. Used for scaling, e.g. in bar graphs. 
        self.max_value = max_value


        self._analog = None
        self.analog = analog


        super(SetPoint, self).__init__(**kw_args)
    # >>> set_point

    # <<< analog
    # @generated
    def get_analog(self):
        """ The Measurement variable used for control
        """
        return self._analog

    def set_analog(self, value):
        if self._analog is not None:
            self._analog._set_point = None

        self._analog = value
        if self._analog is not None:
            self._analog._set_point = self

    analog = property(get_analog, set_analog)
    # >>> analog


    def __str__(self):
        """ Returns a string representation of the SetPoint.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< set_point.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SetPoint.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SetPoint", self.uri)
        if format:
            indent += ' ' * depth

        if self.analog is not None:
            s += '%s<%s:SetPoint.analog rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.analog.uri)
        s += '%s<%s:SetPoint.min_value>%s</%s:SetPoint.min_value>' % \
            (indent, ns_prefix, self.min_value, ns_prefix)
        s += '%s<%s:SetPoint.normal_value>%s</%s:SetPoint.normal_value>' % \
            (indent, ns_prefix, self.normal_value, ns_prefix)
        s += '%s<%s:SetPoint.value>%s</%s:SetPoint.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        s += '%s<%s:SetPoint.max_value>%s</%s:SetPoint.max_value>' % \
            (indent, ns_prefix, self.max_value, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.remote_control is not None:
            s += '%s<%s:Control.remote_control rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.remote_control.uri)
        if self.unit is not None:
            s += '%s<%s:Control.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)
        if self.regulating_cond_eq is not None:
            s += '%s<%s:Control.regulating_cond_eq rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.regulating_cond_eq.uri)
        if self.control_type is not None:
            s += '%s<%s:Control.control_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.control_type.uri)
        s += '%s<%s:Control.time_stamp>%s</%s:Control.time_stamp>' % \
            (indent, ns_prefix, self.time_stamp, ns_prefix)
        s += '%s<%s:Control.operation_in_progress>%s</%s:Control.operation_in_progress>' % \
            (indent, ns_prefix, self.operation_in_progress, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SetPoint")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> set_point.serialize


class AnalogLimit(Limit):
    """ Limit values for Analog measurements
    """
    # <<< analog_limit
    # @generated
    def __init__(self, value=0.0, limit_set=None, **kw_args):
        """ Initialises a new 'AnalogLimit' instance.
        """
        # The value to supervise against. 
        self.value = value


        self._limit_set = None
        self.limit_set = limit_set


        super(AnalogLimit, self).__init__(**kw_args)
    # >>> analog_limit

    # <<< limit_set
    # @generated
    def get_limit_set(self):
        """ The set of limits.
        """
        return self._limit_set

    def set_limit_set(self, value):
        if self._limit_set is not None:
            filtered = [x for x in self.limit_set.limits if x != self]
            self._limit_set._limits = filtered

        self._limit_set = value
        if self._limit_set is not None:
            self._limit_set._limits.append(self)

    limit_set = property(get_limit_set, set_limit_set)
    # >>> limit_set


    def __str__(self):
        """ Returns a string representation of the AnalogLimit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< analog_limit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AnalogLimit.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AnalogLimit", self.uri)
        if format:
            indent += ' ' * depth

        if self.limit_set is not None:
            s += '%s<%s:AnalogLimit.limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.limit_set.uri)
        s += '%s<%s:AnalogLimit.value>%s</%s:AnalogLimit.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.procedures:
            s += '%s<%s:Limit.procedures rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "AnalogLimit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> analog_limit.serialize


class Discrete(Measurement):
    """ Discrete represents a discrete Measurement, i.e. a Measurement reprsenting discrete values, e.g. a Breaker position.
    """
    # <<< discrete
    # @generated
    def __init__(self, normal_value=0, min_value=0, max_value=0, command=None, value_alias_set=None, discrete_values=None, **kw_args):
        """ Initialises a new 'Discrete' instance.
        """
        # Normal measurement value, e.g., used for percentage calculations. 
        self.normal_value = normal_value

        # Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values 
        self.min_value = min_value

        # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values. 
        self.max_value = max_value


        self._command = None
        self.command = command

        self._value_alias_set = None
        self.value_alias_set = value_alias_set

        self._discrete_values = []
        if discrete_values is not None:
            self.discrete_values = discrete_values
        else:
            self.discrete_values = []


        super(Discrete, self).__init__(**kw_args)
    # >>> discrete

    # <<< command
    # @generated
    def get_command(self):
        """ The Control variable associated with the Measurement.
        """
        return self._command

    def set_command(self, value):
        if self._command is not None:
            self._command._discrete = None

        self._command = value
        if self._command is not None:
            self._command._discrete = self

    command = property(get_command, set_command)
    # >>> command

    # <<< value_alias_set
    # @generated
    def get_value_alias_set(self):
        """ The ValueAliasSet used for translation of a MeasurementValue.value to a name
        """
        return self._value_alias_set

    def set_value_alias_set(self, value):
        if self._value_alias_set is not None:
            filtered = [x for x in self.value_alias_set.discretes if x != self]
            self._value_alias_set._discretes = filtered

        self._value_alias_set = value
        if self._value_alias_set is not None:
            self._value_alias_set._discretes.append(self)

    value_alias_set = property(get_value_alias_set, set_value_alias_set)
    # >>> value_alias_set

    # <<< discrete_values
    # @generated
    def get_discrete_values(self):
        """ The values connected to this measurement.
        """
        return self._discrete_values

    def set_discrete_values(self, value):
        for x in self._discrete_values:
            x._discrete = None
        for y in value:
            y._discrete = self
        self._discrete_values = value

    discrete_values = property(get_discrete_values, set_discrete_values)

    def add_discrete_values(self, *discrete_values):
        for obj in discrete_values:
            obj._discrete = self
            self._discrete_values.append(obj)

    def remove_discrete_values(self, *discrete_values):
        for obj in discrete_values:
            obj._discrete = None
            self._discrete_values.remove(obj)
    # >>> discrete_values


    def __str__(self):
        """ Returns a string representation of the Discrete.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< discrete.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Discrete.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Discrete", self.uri)
        if format:
            indent += ' ' * depth

        if self.command is not None:
            s += '%s<%s:Discrete.command rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.command.uri)
        if self.value_alias_set is not None:
            s += '%s<%s:Discrete.value_alias_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.value_alias_set.uri)
        for obj in self.discrete_values:
            s += '%s<%s:Discrete.discrete_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Discrete.normal_value>%s</%s:Discrete.normal_value>' % \
            (indent, ns_prefix, self.normal_value, ns_prefix)
        s += '%s<%s:Discrete.min_value>%s</%s:Discrete.min_value>' % \
            (indent, ns_prefix, self.min_value, ns_prefix)
        s += '%s<%s:Discrete.max_value>%s</%s:Discrete.max_value>' % \
            (indent, ns_prefix, self.max_value, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.asset is not None:
            s += '%s<%s:Measurement.asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset.uri)
        if self.for_tie_point is not None:
            s += '%s<%s:Measurement.for_tie_point rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.for_tie_point.uri)
        if self.power_system_resource is not None:
            s += '%s<%s:Measurement.power_system_resource rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.power_system_resource.uri)
        for obj in self.dynamic_schedules:
            s += '%s<%s:Measurement.dynamic_schedules rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.pnode is not None:
            s += '%s<%s:Measurement.pnode rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.pnode.uri)
        if self.terminal is not None:
            s += '%s<%s:Measurement.terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.terminal.uri)
        for obj in self.documents:
            s += '%s<%s:Measurement.documents rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.locations:
            s += '%s<%s:Measurement.locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Measurement.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.violation_limits:
            s += '%s<%s:Measurement.violation_limits rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.by_tie_point is not None:
            s += '%s<%s:Measurement.by_tie_point rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.by_tie_point.uri)
        if self.unit is not None:
            s += '%s<%s:Measurement.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)
        s += '%s<%s:Measurement.measurement_type>%s</%s:Measurement.measurement_type>' % \
            (indent, ns_prefix, self.measurement_type, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Discrete")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> discrete.serialize


class Accumulator(Measurement):
    """ Accumulator represents a accumulated (counted) Measurement, e.g. an energy value.
    """
    # <<< accumulator
    # @generated
    def __init__(self, max_value=0, accumulator_values=None, limit_sets=None, **kw_args):
        """ Initialises a new 'Accumulator' instance.
        """
        # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values. 
        self.max_value = max_value


        self._accumulator_values = []
        if accumulator_values is not None:
            self.accumulator_values = accumulator_values
        else:
            self.accumulator_values = []

        self._limit_sets = []
        if limit_sets is not None:
            self.limit_sets = limit_sets
        else:
            self.limit_sets = []


        super(Accumulator, self).__init__(**kw_args)
    # >>> accumulator

    # <<< accumulator_values
    # @generated
    def get_accumulator_values(self):
        """ The values connected to this measurement.
        """
        return self._accumulator_values

    def set_accumulator_values(self, value):
        for x in self._accumulator_values:
            x._accumulator = None
        for y in value:
            y._accumulator = self
        self._accumulator_values = value

    accumulator_values = property(get_accumulator_values, set_accumulator_values)

    def add_accumulator_values(self, *accumulator_values):
        for obj in accumulator_values:
            obj._accumulator = self
            self._accumulator_values.append(obj)

    def remove_accumulator_values(self, *accumulator_values):
        for obj in accumulator_values:
            obj._accumulator = None
            self._accumulator_values.remove(obj)
    # >>> accumulator_values

    # <<< limit_sets
    # @generated
    def get_limit_sets(self):
        """ A measurement may have zero or more limit ranges defined for it.
        """
        return self._limit_sets

    def set_limit_sets(self, value):
        for p in self._limit_sets:
            filtered = [q for q in p.measurements if q != self]
            self._limit_sets._measurements = filtered
        for r in value:
            if self not in r._measurements:
                r._measurements.append(self)
        self._limit_sets = value

    limit_sets = property(get_limit_sets, set_limit_sets)

    def add_limit_sets(self, *limit_sets):
        for obj in limit_sets:
            if self not in obj._measurements:
                obj._measurements.append(self)
            self._limit_sets.append(obj)

    def remove_limit_sets(self, *limit_sets):
        for obj in limit_sets:
            if self in obj._measurements:
                obj._measurements.remove(self)
            self._limit_sets.remove(obj)
    # >>> limit_sets


    def __str__(self):
        """ Returns a string representation of the Accumulator.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< accumulator.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Accumulator.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Accumulator", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.accumulator_values:
            s += '%s<%s:Accumulator.accumulator_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.limit_sets:
            s += '%s<%s:Accumulator.limit_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Accumulator.max_value>%s</%s:Accumulator.max_value>' % \
            (indent, ns_prefix, self.max_value, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.asset is not None:
            s += '%s<%s:Measurement.asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset.uri)
        if self.for_tie_point is not None:
            s += '%s<%s:Measurement.for_tie_point rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.for_tie_point.uri)
        if self.power_system_resource is not None:
            s += '%s<%s:Measurement.power_system_resource rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.power_system_resource.uri)
        for obj in self.dynamic_schedules:
            s += '%s<%s:Measurement.dynamic_schedules rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.pnode is not None:
            s += '%s<%s:Measurement.pnode rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.pnode.uri)
        if self.terminal is not None:
            s += '%s<%s:Measurement.terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.terminal.uri)
        for obj in self.documents:
            s += '%s<%s:Measurement.documents rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.locations:
            s += '%s<%s:Measurement.locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Measurement.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.violation_limits:
            s += '%s<%s:Measurement.violation_limits rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.by_tie_point is not None:
            s += '%s<%s:Measurement.by_tie_point rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.by_tie_point.uri)
        if self.unit is not None:
            s += '%s<%s:Measurement.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)
        s += '%s<%s:Measurement.measurement_type>%s</%s:Measurement.measurement_type>' % \
            (indent, ns_prefix, self.measurement_type, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Accumulator")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> accumulator.serialize


class StringMeasurementValue(MeasurementValue):
    """ StringMeasurementValue represents a measurement value of type string.
    """
    # <<< string_measurement_value
    # @generated
    def __init__(self, value='', string_measurement=None, **kw_args):
        """ Initialises a new 'StringMeasurementValue' instance.
        """
        # The value to supervise. 
        self.value = value


        self._string_measurement = None
        self.string_measurement = string_measurement


        super(StringMeasurementValue, self).__init__(**kw_args)
    # >>> string_measurement_value

    # <<< string_measurement
    # @generated
    def get_string_measurement(self):
        """ Measurement to which this value is connected.
        """
        return self._string_measurement

    def set_string_measurement(self, value):
        if self._string_measurement is not None:
            filtered = [x for x in self.string_measurement.string_measurement_values if x != self]
            self._string_measurement._string_measurement_values = filtered

        self._string_measurement = value
        if self._string_measurement is not None:
            self._string_measurement._string_measurement_values.append(self)

    string_measurement = property(get_string_measurement, set_string_measurement)
    # >>> string_measurement


    def __str__(self):
        """ Returns a string representation of the StringMeasurementValue.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< string_measurement_value.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the StringMeasurementValue.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "StringMeasurementValue", self.uri)
        if format:
            indent += ' ' * depth

        if self.string_measurement is not None:
            s += '%s<%s:StringMeasurementValue.string_measurement rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.string_measurement.uri)
        s += '%s<%s:StringMeasurementValue.value>%s</%s:StringMeasurementValue.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.gml_values:
            s += '%s<%s:MeasurementValue.gml_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.measurement_value_source is not None:
            s += '%s<%s:MeasurementValue.measurement_value_source rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value_source.uri)
        if self.erp_person is not None:
            s += '%s<%s:MeasurementValue.erp_person rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_person.uri)
        for obj in self.procedure_data_sets:
            s += '%s<%s:MeasurementValue.procedure_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.remote_source is not None:
            s += '%s<%s:MeasurementValue.remote_source rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.remote_source.uri)
        if self.measurement_value_quality is not None:
            s += '%s<%s:MeasurementValue.measurement_value_quality rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value_quality.uri)
        s += '%s<%s:MeasurementValue.sensor_accuracy>%s</%s:MeasurementValue.sensor_accuracy>' % \
            (indent, ns_prefix, self.sensor_accuracy, ns_prefix)
        s += '%s<%s:MeasurementValue.time_stamp>%s</%s:MeasurementValue.time_stamp>' % \
            (indent, ns_prefix, self.time_stamp, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "StringMeasurementValue")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> string_measurement_value.serialize


class Command(Control):
    """ A Command is a discrete control used for supervisory control.
    """
    # <<< command
    # @generated
    def __init__(self, normal_value=0, value=0, discrete=None, value_alias_set=None, **kw_args):
        """ Initialises a new 'Command' instance.
        """
        # Normal value for Control.value e.g. used for percentage scaling 
        self.normal_value = normal_value

        # The value representing the actuator output 
        self.value = value


        self._discrete = None
        self.discrete = discrete

        self._value_alias_set = None
        self.value_alias_set = value_alias_set


        super(Command, self).__init__(**kw_args)
    # >>> command

    # <<< discrete
    # @generated
    def get_discrete(self):
        """ The Measurement variable used for control.
        """
        return self._discrete

    def set_discrete(self, value):
        if self._discrete is not None:
            self._discrete._command = None

        self._discrete = value
        if self._discrete is not None:
            self._discrete._command = self

    discrete = property(get_discrete, set_discrete)
    # >>> discrete

    # <<< value_alias_set
    # @generated
    def get_value_alias_set(self):
        """ The Commands using the set for translation.
        """
        return self._value_alias_set

    def set_value_alias_set(self, value):
        if self._value_alias_set is not None:
            filtered = [x for x in self.value_alias_set.commands if x != self]
            self._value_alias_set._commands = filtered

        self._value_alias_set = value
        if self._value_alias_set is not None:
            self._value_alias_set._commands.append(self)

    value_alias_set = property(get_value_alias_set, set_value_alias_set)
    # >>> value_alias_set


    def __str__(self):
        """ Returns a string representation of the Command.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< command.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Command.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Command", self.uri)
        if format:
            indent += ' ' * depth

        if self.discrete is not None:
            s += '%s<%s:Command.discrete rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.discrete.uri)
        if self.value_alias_set is not None:
            s += '%s<%s:Command.value_alias_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.value_alias_set.uri)
        s += '%s<%s:Command.normal_value>%s</%s:Command.normal_value>' % \
            (indent, ns_prefix, self.normal_value, ns_prefix)
        s += '%s<%s:Command.value>%s</%s:Command.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.remote_control is not None:
            s += '%s<%s:Control.remote_control rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.remote_control.uri)
        if self.unit is not None:
            s += '%s<%s:Control.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)
        if self.regulating_cond_eq is not None:
            s += '%s<%s:Control.regulating_cond_eq rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.regulating_cond_eq.uri)
        if self.control_type is not None:
            s += '%s<%s:Control.control_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.control_type.uri)
        s += '%s<%s:Control.time_stamp>%s</%s:Control.time_stamp>' % \
            (indent, ns_prefix, self.time_stamp, ns_prefix)
        s += '%s<%s:Control.operation_in_progress>%s</%s:Control.operation_in_progress>' % \
            (indent, ns_prefix, self.operation_in_progress, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Command")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> command.serialize


class DiscreteValue(MeasurementValue):
    """ DiscreteValue represents a discrete MeasurementValue.
    """
    # <<< discrete_value
    # @generated
    def __init__(self, value=0, discrete=None, **kw_args):
        """ Initialises a new 'DiscreteValue' instance.
        """
        # The value to supervise. 
        self.value = value


        self._discrete = None
        self.discrete = discrete


        super(DiscreteValue, self).__init__(**kw_args)
    # >>> discrete_value

    # <<< discrete
    # @generated
    def get_discrete(self):
        """ Measurement to which this value is connected.
        """
        return self._discrete

    def set_discrete(self, value):
        if self._discrete is not None:
            filtered = [x for x in self.discrete.discrete_values if x != self]
            self._discrete._discrete_values = filtered

        self._discrete = value
        if self._discrete is not None:
            self._discrete._discrete_values.append(self)

    discrete = property(get_discrete, set_discrete)
    # >>> discrete


    def __str__(self):
        """ Returns a string representation of the DiscreteValue.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< discrete_value.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the DiscreteValue.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "DiscreteValue", self.uri)
        if format:
            indent += ' ' * depth

        if self.discrete is not None:
            s += '%s<%s:DiscreteValue.discrete rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.discrete.uri)
        s += '%s<%s:DiscreteValue.value>%s</%s:DiscreteValue.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.gml_values:
            s += '%s<%s:MeasurementValue.gml_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.measurement_value_source is not None:
            s += '%s<%s:MeasurementValue.measurement_value_source rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value_source.uri)
        if self.erp_person is not None:
            s += '%s<%s:MeasurementValue.erp_person rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_person.uri)
        for obj in self.procedure_data_sets:
            s += '%s<%s:MeasurementValue.procedure_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.remote_source is not None:
            s += '%s<%s:MeasurementValue.remote_source rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.remote_source.uri)
        if self.measurement_value_quality is not None:
            s += '%s<%s:MeasurementValue.measurement_value_quality rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value_quality.uri)
        s += '%s<%s:MeasurementValue.sensor_accuracy>%s</%s:MeasurementValue.sensor_accuracy>' % \
            (indent, ns_prefix, self.sensor_accuracy, ns_prefix)
        s += '%s<%s:MeasurementValue.time_stamp>%s</%s:MeasurementValue.time_stamp>' % \
            (indent, ns_prefix, self.time_stamp, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "DiscreteValue")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> discrete_value.serialize


class MeasurementValueQuality(Quality61850):
    """ Measurement quality flags. Bits 0-10 are defined for substation automation in draft IEC 61850 part 7-3. Bits 11-15 are reserved for future expansion by that document. Bits 16-31 are reserved for EMS applications.
    """
    # <<< measurement_value_quality
    # @generated
    def __init__(self, measurement_value=None, **kw_args):
        """ Initialises a new 'MeasurementValueQuality' instance.
        """

        self._measurement_value = None
        self.measurement_value = measurement_value


        super(MeasurementValueQuality, self).__init__(**kw_args)
    # >>> measurement_value_quality

    # <<< measurement_value
    # @generated
    def get_measurement_value(self):
        """ A MeasurementValue has a MeasurementValueQuality associated with it.
        """
        return self._measurement_value

    def set_measurement_value(self, value):
        if self._measurement_value is not None:
            self._measurement_value._measurement_value_quality = None

        self._measurement_value = value
        if self._measurement_value is not None:
            self._measurement_value._measurement_value_quality = self

    measurement_value = property(get_measurement_value, set_measurement_value)
    # >>> measurement_value


    def __str__(self):
        """ Returns a string representation of the MeasurementValueQuality.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< measurement_value_quality.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MeasurementValueQuality.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MeasurementValueQuality", self.uri)
        if format:
            indent += ' ' * depth

        if self.measurement_value is not None:
            s += '%s<%s:MeasurementValueQuality.measurement_value rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:Quality61850.source>%s</%s:Quality61850.source>' % \
            (indent, ns_prefix, self.source, ns_prefix)
        s += '%s<%s:Quality61850.validity>%s</%s:Quality61850.validity>' % \
            (indent, ns_prefix, self.validity, ns_prefix)
        s += '%s<%s:Quality61850.test>%s</%s:Quality61850.test>' % \
            (indent, ns_prefix, self.test, ns_prefix)
        s += '%s<%s:Quality61850.over_flow>%s</%s:Quality61850.over_flow>' % \
            (indent, ns_prefix, self.over_flow, ns_prefix)
        s += '%s<%s:Quality61850.estimator_replaced>%s</%s:Quality61850.estimator_replaced>' % \
            (indent, ns_prefix, self.estimator_replaced, ns_prefix)
        s += '%s<%s:Quality61850.suspect>%s</%s:Quality61850.suspect>' % \
            (indent, ns_prefix, self.suspect, ns_prefix)
        s += '%s<%s:Quality61850.bad_reference>%s</%s:Quality61850.bad_reference>' % \
            (indent, ns_prefix, self.bad_reference, ns_prefix)
        s += '%s<%s:Quality61850.operator_blocked>%s</%s:Quality61850.operator_blocked>' % \
            (indent, ns_prefix, self.operator_blocked, ns_prefix)
        s += '%s<%s:Quality61850.oscillatory>%s</%s:Quality61850.oscillatory>' % \
            (indent, ns_prefix, self.oscillatory, ns_prefix)
        s += '%s<%s:Quality61850.failure>%s</%s:Quality61850.failure>' % \
            (indent, ns_prefix, self.failure, ns_prefix)
        s += '%s<%s:Quality61850.old_data>%s</%s:Quality61850.old_data>' % \
            (indent, ns_prefix, self.old_data, ns_prefix)
        s += '%s<%s:Quality61850.out_of_range>%s</%s:Quality61850.out_of_range>' % \
            (indent, ns_prefix, self.out_of_range, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MeasurementValueQuality")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> measurement_value_quality.serialize


class AnalogValue(MeasurementValue):
    """ AnalogValue represents an analog MeasurementValue.
    """
    # <<< analog_value
    # @generated
    def __init__(self, value=0.0, alt_tie_meas=None, analog=None, alt_generating_unit=None, **kw_args):
        """ Initialises a new 'AnalogValue' instance.
        """
        # The value to supervise. 
        self.value = value


        self._alt_tie_meas = []
        if alt_tie_meas is not None:
            self.alt_tie_meas = alt_tie_meas
        else:
            self.alt_tie_meas = []

        self._analog = None
        self.analog = analog

        self._alt_generating_unit = []
        if alt_generating_unit is not None:
            self.alt_generating_unit = alt_generating_unit
        else:
            self.alt_generating_unit = []


        super(AnalogValue, self).__init__(**kw_args)
    # >>> analog_value

    # <<< alt_tie_meas
    # @generated
    def get_alt_tie_meas(self):
        """ The usage of the measurement within the control area specification.
        """
        return self._alt_tie_meas

    def set_alt_tie_meas(self, value):
        for x in self._alt_tie_meas:
            x._analog_value = None
        for y in value:
            y._analog_value = self
        self._alt_tie_meas = value

    alt_tie_meas = property(get_alt_tie_meas, set_alt_tie_meas)

    def add_alt_tie_meas(self, *alt_tie_meas):
        for obj in alt_tie_meas:
            obj._analog_value = self
            self._alt_tie_meas.append(obj)

    def remove_alt_tie_meas(self, *alt_tie_meas):
        for obj in alt_tie_meas:
            obj._analog_value = None
            self._alt_tie_meas.remove(obj)
    # >>> alt_tie_meas

    # <<< analog
    # @generated
    def get_analog(self):
        """ Measurement to which this value is connected.
        """
        return self._analog

    def set_analog(self, value):
        if self._analog is not None:
            filtered = [x for x in self.analog.analog_values if x != self]
            self._analog._analog_values = filtered

        self._analog = value
        if self._analog is not None:
            self._analog._analog_values.append(self)

    analog = property(get_analog, set_analog)
    # >>> analog

    # <<< alt_generating_unit
    # @generated
    def get_alt_generating_unit(self):
        """ The alternate generating unit for which this measurement value applies.
        """
        return self._alt_generating_unit

    def set_alt_generating_unit(self, value):
        for x in self._alt_generating_unit:
            x._analog_value = None
        for y in value:
            y._analog_value = self
        self._alt_generating_unit = value

    alt_generating_unit = property(get_alt_generating_unit, set_alt_generating_unit)

    def add_alt_generating_unit(self, *alt_generating_unit):
        for obj in alt_generating_unit:
            obj._analog_value = self
            self._alt_generating_unit.append(obj)

    def remove_alt_generating_unit(self, *alt_generating_unit):
        for obj in alt_generating_unit:
            obj._analog_value = None
            self._alt_generating_unit.remove(obj)
    # >>> alt_generating_unit


    def __str__(self):
        """ Returns a string representation of the AnalogValue.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< analog_value.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AnalogValue.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AnalogValue", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.alt_tie_meas:
            s += '%s<%s:AnalogValue.alt_tie_meas rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.analog is not None:
            s += '%s<%s:AnalogValue.analog rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.analog.uri)
        for obj in self.alt_generating_unit:
            s += '%s<%s:AnalogValue.alt_generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:AnalogValue.value>%s</%s:AnalogValue.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.gml_values:
            s += '%s<%s:MeasurementValue.gml_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.measurement_value_source is not None:
            s += '%s<%s:MeasurementValue.measurement_value_source rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value_source.uri)
        if self.erp_person is not None:
            s += '%s<%s:MeasurementValue.erp_person rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_person.uri)
        for obj in self.procedure_data_sets:
            s += '%s<%s:MeasurementValue.procedure_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.remote_source is not None:
            s += '%s<%s:MeasurementValue.remote_source rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.remote_source.uri)
        if self.measurement_value_quality is not None:
            s += '%s<%s:MeasurementValue.measurement_value_quality rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value_quality.uri)
        s += '%s<%s:MeasurementValue.sensor_accuracy>%s</%s:MeasurementValue.sensor_accuracy>' % \
            (indent, ns_prefix, self.sensor_accuracy, ns_prefix)
        s += '%s<%s:MeasurementValue.time_stamp>%s</%s:MeasurementValue.time_stamp>' % \
            (indent, ns_prefix, self.time_stamp, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "AnalogValue")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> analog_value.serialize


class StringMeasurement(Measurement):
    """ StringMeasurement represents a measurement with values of type string.
    """
    # <<< string_measurement
    # @generated
    def __init__(self, string_measurement_values=None, **kw_args):
        """ Initialises a new 'StringMeasurement' instance.
        """

        self._string_measurement_values = []
        if string_measurement_values is not None:
            self.string_measurement_values = string_measurement_values
        else:
            self.string_measurement_values = []


        super(StringMeasurement, self).__init__(**kw_args)
    # >>> string_measurement

    # <<< string_measurement_values
    # @generated
    def get_string_measurement_values(self):
        """ The values connected to this measurement.
        """
        return self._string_measurement_values

    def set_string_measurement_values(self, value):
        for x in self._string_measurement_values:
            x._string_measurement = None
        for y in value:
            y._string_measurement = self
        self._string_measurement_values = value

    string_measurement_values = property(get_string_measurement_values, set_string_measurement_values)

    def add_string_measurement_values(self, *string_measurement_values):
        for obj in string_measurement_values:
            obj._string_measurement = self
            self._string_measurement_values.append(obj)

    def remove_string_measurement_values(self, *string_measurement_values):
        for obj in string_measurement_values:
            obj._string_measurement = None
            self._string_measurement_values.remove(obj)
    # >>> string_measurement_values


    def __str__(self):
        """ Returns a string representation of the StringMeasurement.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< string_measurement.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the StringMeasurement.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "StringMeasurement", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.string_measurement_values:
            s += '%s<%s:StringMeasurement.string_measurement_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.asset is not None:
            s += '%s<%s:Measurement.asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset.uri)
        if self.for_tie_point is not None:
            s += '%s<%s:Measurement.for_tie_point rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.for_tie_point.uri)
        if self.power_system_resource is not None:
            s += '%s<%s:Measurement.power_system_resource rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.power_system_resource.uri)
        for obj in self.dynamic_schedules:
            s += '%s<%s:Measurement.dynamic_schedules rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.pnode is not None:
            s += '%s<%s:Measurement.pnode rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.pnode.uri)
        if self.terminal is not None:
            s += '%s<%s:Measurement.terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.terminal.uri)
        for obj in self.documents:
            s += '%s<%s:Measurement.documents rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.locations:
            s += '%s<%s:Measurement.locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Measurement.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.violation_limits:
            s += '%s<%s:Measurement.violation_limits rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.by_tie_point is not None:
            s += '%s<%s:Measurement.by_tie_point rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.by_tie_point.uri)
        if self.unit is not None:
            s += '%s<%s:Measurement.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)
        s += '%s<%s:Measurement.measurement_type>%s</%s:Measurement.measurement_type>' % \
            (indent, ns_prefix, self.measurement_type, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "StringMeasurement")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> string_measurement.serialize


# <<< meas
# @generated
# >>> meas
