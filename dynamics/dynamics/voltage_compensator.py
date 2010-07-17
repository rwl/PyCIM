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


from dynamics import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_VoltageCompensator"

class VoltageCompensator(Element):
    """ A voltage compensator adjusts the terminal voltage feedback to the excitation system by adding a quantity that is proportional to the terminal current of the generator. It is linked to a specific generator by the Bus number and Unit IDA voltage compensator adjusts the terminal voltage feedback to the excitation system by adding a quantity that is proportional to the terminal current of the generator. It is linked to a specific generator by the Bus number and Unit ID
    """
    # <<< voltage_compensator
    # @generated
    def __init__(self, rcomp=0.0, xcomp=0.0, **kw_args):
        """ Initialises a new 'VoltageCompensator' instance.
        """
        # Compensating (compounding) resistanceCompensating (compounding) resistance 
        self.rcomp = rcomp

        # Compensating (compounding) reactanceCompensating (compounding) reactance 
        self.xcomp = xcomp



        super(VoltageCompensator, self).__init__(**kw_args)
    # >>> voltage_compensator


    def __str__(self):
        """ Returns a string representation of the VoltageCompensator.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< voltage_compensator.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the VoltageCompensator.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "VoltageCompensator", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:VoltageCompensator.rcomp>%s</%s:VoltageCompensator.rcomp>' % \
            (indent, ns_prefix, self.rcomp, ns_prefix)
        s += '%s<%s:VoltageCompensator.xcomp>%s</%s:VoltageCompensator.xcomp>' % \
            (indent, ns_prefix, self.xcomp, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "VoltageCompensator")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> voltage_compensator.serialize


class VcompIEEE(VoltageCompensator):
    """ IEEE Voltage Compensation ModelIEEE Voltage Compensation Model
    """
    pass
    # <<< vcomp_ieee
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'VcompIEEE' instance.
        """


        super(VcompIEEE, self).__init__(**kw_args)
    # >>> vcomp_ieee


    def __str__(self):
        """ Returns a string representation of the VcompIEEE.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< vcomp_ieee.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the VcompIEEE.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "VcompIEEE", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:VoltageCompensator.rcomp>%s</%s:VoltageCompensator.rcomp>' % \
            (indent, ns_prefix, self.rcomp, ns_prefix)
        s += '%s<%s:VoltageCompensator.xcomp>%s</%s:VoltageCompensator.xcomp>' % \
            (indent, ns_prefix, self.xcomp, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "VcompIEEE")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> vcomp_ieee.serialize


class VcompCross(VoltageCompensator):
    """ Voltage Compensation Model for Cross-Compound Generating UnitVoltage Compensation Model for Cross-Compound Generating Unit
    """
    # <<< vcomp_cross
    # @generated
    def __init__(self, xcomp2=0.0, rcomp2=0.0, **kw_args):
        """ Initialises a new 'VcompCross' instance.
        """
        # Cross-Compensating (compounding) reactanceCross-Compensating (compounding) reactance 
        self.xcomp2 = xcomp2

        # Cross-Compensating (compounding) resistanceCross-Compensating (compounding) resistance 
        self.rcomp2 = rcomp2



        super(VcompCross, self).__init__(**kw_args)
    # >>> vcomp_cross


    def __str__(self):
        """ Returns a string representation of the VcompCross.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< vcomp_cross.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the VcompCross.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "VcompCross", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:VcompCross.xcomp2>%s</%s:VcompCross.xcomp2>' % \
            (indent, ns_prefix, self.xcomp2, ns_prefix)
        s += '%s<%s:VcompCross.rcomp2>%s</%s:VcompCross.rcomp2>' % \
            (indent, ns_prefix, self.rcomp2, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:VoltageCompensator.rcomp>%s</%s:VoltageCompensator.rcomp>' % \
            (indent, ns_prefix, self.rcomp, ns_prefix)
        s += '%s<%s:VoltageCompensator.xcomp>%s</%s:VoltageCompensator.xcomp>' % \
            (indent, ns_prefix, self.xcomp, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "VcompCross")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> vcomp_cross.serialize


# <<< voltage_compensator
# @generated
# >>> voltage_compensator
