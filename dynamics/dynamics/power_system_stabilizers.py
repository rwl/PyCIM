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

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_PowerSystemStabilizers"

class PowerSystemStabilizer(Element):
    """ A PSS provides an input (Vs) to the excitation system model to improve damping of system oscillations.  A variety of input signals may be used depending on the particular design.A PSS provides an input (Vs) to the excitation system model to improve damping of system oscillations.  A variety of input signals may be used depending on the particular design.
    """
    pass
    # <<< power_system_stabilizer
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'PowerSystemStabilizer' instance.
        """


        super(PowerSystemStabilizer, self).__init__(**kw_args)
    # >>> power_system_stabilizer


    def __str__(self):
        """ Returns a string representation of the PowerSystemStabilizer.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< power_system_stabilizer.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PowerSystemStabilizer.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PowerSystemStabilizer", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PowerSystemStabilizer")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> power_system_stabilizer.serialize


class PssIEEE4B(PowerSystemStabilizer):
    """ PSS type IEEE PSS4BPSS type IEEE PSS4B
    """
    pass
    # <<< pss_ieee4_b
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'PssIEEE4B' instance.
        """


        super(PssIEEE4B, self).__init__(**kw_args)
    # >>> pss_ieee4_b


    def __str__(self):
        """ Returns a string representation of the PssIEEE4B.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< pss_ieee4_b.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PssIEEE4B.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PssIEEE4B", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PssIEEE4B")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> pss_ieee4_b.serialize


class PssIEEE2B(PowerSystemStabilizer):
    """ IEEE (2005) PSS2B Model  This stabilizer model is designed to represent a variety of dual-input stabilizers, which normally use combinations of power and speed or frequency to derive the stabilizing signal.IEEE (2005) PSS2B Model  This stabilizer model is designed to represent a variety of dual-input stabilizers, which normally use combinations of power and speed or frequency to derive the stabilizing signal.
    """
    # <<< pss_ieee2_b
    # @generated
    def __init__(self, t10=0.0, a=0.0, ks1=0.0, ks3=0.0, t11=0.0, ks2=0.0, vstmin=0.0, vsi1max=0.0, vsi2max=0.0, tb=0.0, t2=0.0, ta=0.0, t1=0.0, t4=0.0, n=False, t3=0.0, m=False, t6=0.0, t8=0.0, vsi1min=0.0, t7=0.0, t9=0.0, ks4=0.0, tw2=0.0, tw1=0.0, tw4=0.0, vsi2min=0.0, tw3=0.0, vstmax=0.0, **kw_args):
        """ Initialises a new 'PssIEEE2B' instance.
        """
        # Lead/lag time constantLead/lag time constant 
        self.t10 = t10

        # Numerator constantNumerator constant 
        self.a = a

        # Stabilizer gainStabilizer gain 
        self.ks1 = ks1

        # Gain on signal #2 input before ramp-tracking filterGain on signal #2 input before ramp-tracking filter 
        self.ks3 = ks3

        # Lead/lag time constantLead/lag time constant 
        self.t11 = t11

        # Gain on signal #2Gain on signal #2 
        self.ks2 = ks2

        # Stabilizer output min limitStabilizer output min limit 
        self.vstmin = vstmin

        # Input signal #1 max limitInput signal #1 max limit 
        self.vsi1max = vsi1max

        # Input signal #2 max limitInput signal #2 max limit 
        self.vsi2max = vsi2max

        # Lag time constantLag time constant 
        self.tb = tb

        # Lead/lag time constantLead/lag time constant 
        self.t2 = t2

        # Lead constantLead constant 
        self.ta = ta

        # Lead/lag time constantLead/lag time constant 
        self.t1 = t1

        # Lead/lag time constantLead/lag time constant 
        self.t4 = t4

        # Order of ramp tracking filterOrder of ramp tracking filter 
        self.n = n

        # Lead/lag time constantLead/lag time constant 
        self.t3 = t3

        # Denominator order of ramp tracking filterDenominator order of ramp tracking filter 
        self.m = m

        # Time constant on signal #1Time constant on signal #1 
        self.t6 = t6

        # Lead of ramp tracking filterLead of ramp tracking filter 
        self.t8 = t8

        # Input signal #1 min limitInput signal #1 min limit 
        self.vsi1min = vsi1min

        # Time constant on signal #2Time constant on signal #2 
        self.t7 = t7

        # Lag of ramp tracking filterLag of ramp tracking filter 
        self.t9 = t9

        # Gain on signal #2 input after ramp-tracking filterGain on signal #2 input after ramp-tracking filter 
        self.ks4 = ks4

        # Second washout on signal #1Second washout on signal #1 
        self.tw2 = tw2

        # First washout on signal #1First washout on signal #1 
        self.tw1 = tw1

        # Second washout on signal #2Second washout on signal #2 
        self.tw4 = tw4

        # Input signal #2 min limitInput signal #2 min limit 
        self.vsi2min = vsi2min

        # First washout on signal #2First washout on signal #2 
        self.tw3 = tw3

        # Stabilizer output max limitStabilizer output max limit 
        self.vstmax = vstmax



        super(PssIEEE2B, self).__init__(**kw_args)
    # >>> pss_ieee2_b


    def __str__(self):
        """ Returns a string representation of the PssIEEE2B.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< pss_ieee2_b.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PssIEEE2B.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PssIEEE2B", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:PssIEEE2B.t10>%s</%s:PssIEEE2B.t10>' % \
            (indent, ns_prefix, self.t10, ns_prefix)
        s += '%s<%s:PssIEEE2B.a>%s</%s:PssIEEE2B.a>' % \
            (indent, ns_prefix, self.a, ns_prefix)
        s += '%s<%s:PssIEEE2B.ks1>%s</%s:PssIEEE2B.ks1>' % \
            (indent, ns_prefix, self.ks1, ns_prefix)
        s += '%s<%s:PssIEEE2B.ks3>%s</%s:PssIEEE2B.ks3>' % \
            (indent, ns_prefix, self.ks3, ns_prefix)
        s += '%s<%s:PssIEEE2B.t11>%s</%s:PssIEEE2B.t11>' % \
            (indent, ns_prefix, self.t11, ns_prefix)
        s += '%s<%s:PssIEEE2B.ks2>%s</%s:PssIEEE2B.ks2>' % \
            (indent, ns_prefix, self.ks2, ns_prefix)
        s += '%s<%s:PssIEEE2B.vstmin>%s</%s:PssIEEE2B.vstmin>' % \
            (indent, ns_prefix, self.vstmin, ns_prefix)
        s += '%s<%s:PssIEEE2B.vsi1max>%s</%s:PssIEEE2B.vsi1max>' % \
            (indent, ns_prefix, self.vsi1max, ns_prefix)
        s += '%s<%s:PssIEEE2B.vsi2max>%s</%s:PssIEEE2B.vsi2max>' % \
            (indent, ns_prefix, self.vsi2max, ns_prefix)
        s += '%s<%s:PssIEEE2B.tb>%s</%s:PssIEEE2B.tb>' % \
            (indent, ns_prefix, self.tb, ns_prefix)
        s += '%s<%s:PssIEEE2B.t2>%s</%s:PssIEEE2B.t2>' % \
            (indent, ns_prefix, self.t2, ns_prefix)
        s += '%s<%s:PssIEEE2B.ta>%s</%s:PssIEEE2B.ta>' % \
            (indent, ns_prefix, self.ta, ns_prefix)
        s += '%s<%s:PssIEEE2B.t1>%s</%s:PssIEEE2B.t1>' % \
            (indent, ns_prefix, self.t1, ns_prefix)
        s += '%s<%s:PssIEEE2B.t4>%s</%s:PssIEEE2B.t4>' % \
            (indent, ns_prefix, self.t4, ns_prefix)
        s += '%s<%s:PssIEEE2B.n>%s</%s:PssIEEE2B.n>' % \
            (indent, ns_prefix, self.n, ns_prefix)
        s += '%s<%s:PssIEEE2B.t3>%s</%s:PssIEEE2B.t3>' % \
            (indent, ns_prefix, self.t3, ns_prefix)
        s += '%s<%s:PssIEEE2B.m>%s</%s:PssIEEE2B.m>' % \
            (indent, ns_prefix, self.m, ns_prefix)
        s += '%s<%s:PssIEEE2B.t6>%s</%s:PssIEEE2B.t6>' % \
            (indent, ns_prefix, self.t6, ns_prefix)
        s += '%s<%s:PssIEEE2B.t8>%s</%s:PssIEEE2B.t8>' % \
            (indent, ns_prefix, self.t8, ns_prefix)
        s += '%s<%s:PssIEEE2B.vsi1min>%s</%s:PssIEEE2B.vsi1min>' % \
            (indent, ns_prefix, self.vsi1min, ns_prefix)
        s += '%s<%s:PssIEEE2B.t7>%s</%s:PssIEEE2B.t7>' % \
            (indent, ns_prefix, self.t7, ns_prefix)
        s += '%s<%s:PssIEEE2B.t9>%s</%s:PssIEEE2B.t9>' % \
            (indent, ns_prefix, self.t9, ns_prefix)
        s += '%s<%s:PssIEEE2B.ks4>%s</%s:PssIEEE2B.ks4>' % \
            (indent, ns_prefix, self.ks4, ns_prefix)
        s += '%s<%s:PssIEEE2B.tw2>%s</%s:PssIEEE2B.tw2>' % \
            (indent, ns_prefix, self.tw2, ns_prefix)
        s += '%s<%s:PssIEEE2B.tw1>%s</%s:PssIEEE2B.tw1>' % \
            (indent, ns_prefix, self.tw1, ns_prefix)
        s += '%s<%s:PssIEEE2B.tw4>%s</%s:PssIEEE2B.tw4>' % \
            (indent, ns_prefix, self.tw4, ns_prefix)
        s += '%s<%s:PssIEEE2B.vsi2min>%s</%s:PssIEEE2B.vsi2min>' % \
            (indent, ns_prefix, self.vsi2min, ns_prefix)
        s += '%s<%s:PssIEEE2B.tw3>%s</%s:PssIEEE2B.tw3>' % \
            (indent, ns_prefix, self.tw3, ns_prefix)
        s += '%s<%s:PssIEEE2B.vstmax>%s</%s:PssIEEE2B.vstmax>' % \
            (indent, ns_prefix, self.vstmax, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PssIEEE2B")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> pss_ieee2_b.serialize


class PssSB4(PowerSystemStabilizer):
    """ Power sensitive stabilizer modelPower sensitive stabilizer model
    """
    pass
    # <<< pss_sb4
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'PssSB4' instance.
        """


        super(PssSB4, self).__init__(**kw_args)
    # >>> pss_sb4


    def __str__(self):
        """ Returns a string representation of the PssSB4.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< pss_sb4.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PssSB4.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PssSB4", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PssSB4")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> pss_sb4.serialize


class PssSB(PowerSystemStabilizer):
    """ Dual input PSS, pss2a and transient stabilizerDual input PSS, pss2a and transient stabilizer
    """
    pass
    # <<< pss_sb
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'PssSB' instance.
        """


        super(PssSB, self).__init__(**kw_args)
    # >>> pss_sb


    def __str__(self):
        """ Returns a string representation of the PssSB.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< pss_sb.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PssSB.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PssSB", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PssSB")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> pss_sb.serialize


class PssSK(PowerSystemStabilizer):
    """ PSS Slovakian type &ndash; three inputsPSS Slovakian type &ndash; three inputs
    """
    pass
    # <<< pss_sk
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'PssSK' instance.
        """


        super(PssSK, self).__init__(**kw_args)
    # >>> pss_sk


    def __str__(self):
        """ Returns a string representation of the PssSK.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< pss_sk.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PssSK.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PssSK", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PssSK")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> pss_sk.serialize


class PssPTIST3(PowerSystemStabilizer):
    """ PTI microprocessor-based stabilizer model type 3PTI microprocessor-based stabilizer model type 3
    """
    pass
    # <<< pss_ptist3
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'PssPTIST3' instance.
        """


        super(PssPTIST3, self).__init__(**kw_args)
    # >>> pss_ptist3


    def __str__(self):
        """ Returns a string representation of the PssPTIST3.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< pss_ptist3.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PssPTIST3.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PssPTIST3", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PssPTIST3")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> pss_ptist3.serialize


class PssIEEE1A(PowerSystemStabilizer):
    """ PSS type IEEE PSS1APSS type IEEE PSS1A
    """
    pass
    # <<< pss_ieee1_a
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'PssIEEE1A' instance.
        """


        super(PssIEEE1A, self).__init__(**kw_args)
    # >>> pss_ieee1_a


    def __str__(self):
        """ Returns a string representation of the PssIEEE1A.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< pss_ieee1_a.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PssIEEE1A.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PssIEEE1A", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PssIEEE1A")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> pss_ieee1_a.serialize


class PssIEEE3B(PowerSystemStabilizer):
    """ PSS type IEEE PSS3BPSS type IEEE PSS3B
    """
    pass
    # <<< pss_ieee3_b
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'PssIEEE3B' instance.
        """


        super(PssIEEE3B, self).__init__(**kw_args)
    # >>> pss_ieee3_b


    def __str__(self):
        """ Returns a string representation of the PssIEEE3B.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< pss_ieee3_b.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PssIEEE3B.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PssIEEE3B", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PssIEEE3B")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> pss_ieee3_b.serialize


class PssWSCC(PowerSystemStabilizer):
    """ Dual input PSSDual input PSS
    """
    pass
    # <<< pss_wscc
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'PssWSCC' instance.
        """


        super(PssWSCC, self).__init__(**kw_args)
    # >>> pss_wscc


    def __str__(self):
        """ Returns a string representation of the PssWSCC.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< pss_wscc.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PssWSCC.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PssWSCC", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PssWSCC")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> pss_wscc.serialize


class PssPTIST1(PowerSystemStabilizer):
    """ PTI microprocessor-based stabilizer model type 1PTI microprocessor-based stabilizer model type 1
    """
    pass
    # <<< pss_ptist1
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'PssPTIST1' instance.
        """


        super(PssPTIST1, self).__init__(**kw_args)
    # >>> pss_ptist1


    def __str__(self):
        """ Returns a string representation of the PssPTIST1.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< pss_ptist1.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PssPTIST1.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PssPTIST1", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PssPTIST1")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> pss_ptist1.serialize


class PssSH(PowerSystemStabilizer):
    """ Siemens H infinity PSSSiemens H infinity PSS
    """
    pass
    # <<< pss_sh
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'PssSH' instance.
        """


        super(PssSH, self).__init__(**kw_args)
    # >>> pss_sh


    def __str__(self):
        """ Returns a string representation of the PssSH.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< pss_sh.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PssSH.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PssSH", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PssSH")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> pss_sh.serialize


# <<< power_system_stabilizers
# @generated
# >>> power_system_stabilizers
