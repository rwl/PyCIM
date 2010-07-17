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



# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14"

class Element(object):
    # <<< element
    # @generated
    def __init__(self, uuid='', parent=None, **kw_args):
        """ Initialises a new 'Element' instance.
        """
 
        self.uuid = uuid


        self._parent = None
        self.parent = parent


        super(Element, self).__init__(**kw_args)
    # >>> element

    # <<< parent
    # @generated
    def get_parent(self):
        """ 
        """
        return self._parent

    def set_parent(self, value):
        if self._parent is not None:
            filtered = [x for x in self.parent.elements if x != self]
            self._parent._elements = filtered

        self._parent = value
        if self._parent is not None:
            self._parent._elements.append(self)

    parent = property(get_parent, set_parent)
    # >>> parent


    def __str__(self):
        """ Returns a string representation of the Element.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< element.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Element.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Element", self.uri)
        if format:
            indent += ' ' * depth

        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Element")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> element.serialize


class Model(object):
    # <<< model
    # @generated
    def __init__(self, elements=None, **kw_args):
        """ Initialises a new 'Model' instance.
        """

        self._elements = []
        if elements is not None:
            self.elements = elements
        else:
            self.elements = []


        super(Model, self).__init__(**kw_args)
    # >>> model

    # <<< elements
    # @generated
    def get_elements(self):
        """ 
        """
        return self._elements

    def set_elements(self, value):
        for x in self._elements:
            x._parent = None
        for y in value:
            y._parent = self
        self._elements = value

    elements = property(get_elements, set_elements)

    def add_elements(self, *elements):
        for obj in elements:
            obj._parent = self
            self._elements.append(obj)

    def remove_elements(self, *elements):
        for obj in elements:
            obj._parent = None
            self._elements.remove(obj)
    # >>> elements


    def __str__(self):
        """ Returns a string representation of the Model.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< model.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Model.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Model", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.elements:
            s += '%s<%s:Model.elements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Model")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> model.serialize


class CombinedVersion(Element):
    """ The combined version denotes the versions of the subpackages that have been combined into the total CIIMmodel. This is a convenience instead of having to look at each subpackage.
    """
    # <<< combined_version
    # @generated
    def __init__(self, date='', version='', **kw_args):
        """ Initialises a new 'CombinedVersion' instance.
        """
        # Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05. 
        self.date = date

        # Form is IEC61970CIMXXvYY_IEC61968CIMXXvYY_combined where XX is the major CIM package version and the YY is the minor version, and different packages could have different major and minor versions.   For example IEC61970CIM13v18_IEC61968CIM10v16_combined.  Additional packages might be added in the future. 
        self.version = version



        super(CombinedVersion, self).__init__(**kw_args)
    # >>> combined_version


    def __str__(self):
        """ Returns a string representation of the CombinedVersion.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< combined_version.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CombinedVersion.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CombinedVersion", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:CombinedVersion.date>%s</%s:CombinedVersion.date>' % \
            (indent, ns_prefix, self.date, ns_prefix)
        s += '%s<%s:CombinedVersion.version>%s</%s:CombinedVersion.version>' % \
            (indent, ns_prefix, self.version, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CombinedVersion")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> combined_version.serialize


class PowerROCPerMin(Element):
    pass
    # <<< power_rocper_min
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'PowerROCPerMin' instance.
        """


        super(PowerROCPerMin, self).__init__(**kw_args)
    # >>> power_rocper_min


    def __str__(self):
        """ Returns a string representation of the PowerROCPerMin.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< power_rocper_min.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PowerROCPerMin.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PowerROCPerMin", self.uri)
        if format:
            indent += ' ' * depth

        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PowerROCPerMin")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> power_rocper_min.serialize


class RateOfChange(Element):
    pass
    # <<< rate_of_change
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'RateOfChange' instance.
        """


        super(RateOfChange, self).__init__(**kw_args)
    # >>> rate_of_change


    def __str__(self):
        """ Returns a string representation of the RateOfChange.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< rate_of_change.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RateOfChange.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RateOfChange", self.uri)
        if format:
            indent += ' ' * depth

        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "RateOfChange")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> rate_of_change.serialize


class EnumeratedType(Element):
    pass
    # <<< enumerated_type
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'EnumeratedType' instance.
        """


        super(EnumeratedType, self).__init__(**kw_args)
    # >>> enumerated_type


    def __str__(self):
        """ Returns a string representation of the EnumeratedType.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< enumerated_type.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the EnumeratedType.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "EnumeratedType", self.uri)
        if format:
            indent += ' ' * depth

        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "EnumeratedType")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> enumerated_type.serialize


class FreqBiasFactor(Element):
    pass
    # <<< freq_bias_factor
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'FreqBiasFactor' instance.
        """


        super(FreqBiasFactor, self).__init__(**kw_args)
    # >>> freq_bias_factor


    def __str__(self):
        """ Returns a string representation of the FreqBiasFactor.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< freq_bias_factor.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the FreqBiasFactor.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "FreqBiasFactor", self.uri)
        if format:
            indent += ' ' * depth

        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "FreqBiasFactor")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> freq_bias_factor.serialize


class FlowgateIdcType(Element):
    pass
    # <<< flowgate_idc_type
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'FlowgateIdcType' instance.
        """


        super(FlowgateIdcType, self).__init__(**kw_args)
    # >>> flowgate_idc_type


    def __str__(self):
        """ Returns a string representation of the FlowgateIdcType.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< flowgate_idc_type.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the FlowgateIdcType.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "FlowgateIdcType", self.uri)
        if format:
            indent += ' ' * depth

        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "FlowgateIdcType")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> flowgate_idc_type.serialize


class Quantity(Element):
    pass
    # <<< quantity
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'Quantity' instance.
        """


        super(Quantity, self).__init__(**kw_args)
    # >>> quantity


    def __str__(self):
        """ Returns a string representation of the Quantity.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< quantity.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Quantity.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Quantity", self.uri)
        if format:
            indent += ' ' * depth

        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Quantity")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> quantity.serialize


class EnergyAsMWh(Element):
    pass
    # <<< energy_as_mwh
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'EnergyAsMWh' instance.
        """


        super(EnergyAsMWh, self).__init__(**kw_args)
    # >>> energy_as_mwh


    def __str__(self):
        """ Returns a string representation of the EnergyAsMWh.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< energy_as_mwh.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the EnergyAsMWh.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "EnergyAsMWh", self.uri)
        if format:
            indent += ' ' * depth

        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "EnergyAsMWh")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> energy_as_mwh.serialize


class FlowgateAfcUseCode(Element):
    pass
    # <<< flowgate_afc_use_code
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'FlowgateAfcUseCode' instance.
        """


        super(FlowgateAfcUseCode, self).__init__(**kw_args)
    # >>> flowgate_afc_use_code


    def __str__(self):
        """ Returns a string representation of the FlowgateAfcUseCode.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< flowgate_afc_use_code.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the FlowgateAfcUseCode.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "FlowgateAfcUseCode", self.uri)
        if format:
            indent += ' ' * depth

        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "FlowgateAfcUseCode")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> flowgate_afc_use_code.serialize


class PenaltyFactor(Element):
    pass
    # <<< penalty_factor
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'PenaltyFactor' instance.
        """


        super(PenaltyFactor, self).__init__(**kw_args)
    # >>> penalty_factor


    def __str__(self):
        """ Returns a string representation of the PenaltyFactor.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< penalty_factor.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PenaltyFactor.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PenaltyFactor", self.uri)
        if format:
            indent += ' ' * depth

        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PenaltyFactor")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> penalty_factor.serialize


# <<< cim
# @generated
# >>> cim
