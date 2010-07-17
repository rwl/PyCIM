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

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_ExcitationSystems"

class ExcitationSystem(Element):
    """ An excitation system provides the field voltage (Efd) for a synchronous machine model. It is linked to a specific generator by the Bus number and Unit ID.An excitation system provides the field voltage (Efd) for a synchronous machine model. It is linked to a specific generator by the Bus number and Unit ID.
    """
    pass
    # <<< excitation_system
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ExcitationSystem' instance.
        """


        super(ExcitationSystem, self).__init__(**kw_args)
    # >>> excitation_system


    def __str__(self):
        """ Returns a string representation of the ExcitationSystem.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< excitation_system.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcitationSystem.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcitationSystem", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcitationSystem")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> excitation_system.serialize


class ExcBAS(ExcitationSystem):
    """ Basler static voltage regulator feeding dc or ac rotating exciter modelBasler static voltage regulator feeding dc or ac rotating exciter model
    """
    pass
    # <<< exc_bas
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ExcBAS' instance.
        """


        super(ExcBAS, self).__init__(**kw_args)
    # >>> exc_bas


    def __str__(self):
        """ Returns a string representation of the ExcBAS.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_bas.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcBAS.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcBAS", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcBAS")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_bas.serialize


class ExcDC2A(ExcitationSystem):
    """ IEEE (1992/2005) DC2A Model  The model is used to represent field-controlled dc commutator exciters with continuously acting voltage regulators having supplies obtained from the generator or auxiliary bus. It differs from the Type DC1A model only in the voltage regulator output limits, which are now proportional to terminal voltage <i>V</i><i><sub>T</sub></i>. It is representative of solid-state replacements for various forms of older mechanical and rotating amplifier regulating equipment connected to dc commutator exciters.IEEE (1992/2005) DC2A Model  The model is used to represent field-controlled dc commutator exciters with continuously acting voltage regulators having supplies obtained from the generator or auxiliary bus. It differs from the Type DC1A model only in the voltage regulator output limits, which are now proportional to terminal voltage <i>V</i><i><sub>T</sub></i>. It is representative of solid-state replacements for various forms of older mechanical and rotating amplifier regulating equipment connected to dc commutator exciters.
    """
    # <<< exc_dc2_a
    # @generated
    def __init__(self, te=0.0, tf=0.0, ka=0.0, tc=0.0, vrmin=0.0, ta=0.0, tb=0.0, vrmax=0.0, kf=0.0, ke=0.0, uelin=0.0, se1=0.0, tr=0.0, se2=0.0, exclim=0.0, e2=0.0, e1=0.0, **kw_args):
        """ Initialises a new 'ExcDC2A' instance.
        """
        # Exciter time constant (&gt; 0.)Exciter time constant (&gt; 0.) 
        self.te = te

        # Rate feedback time constant, sec. (&gt; 0.)Rate feedback time constant, sec. (&gt; 0.) 
        self.tf = tf

        # Gain (&gt; 0.)Gain (&gt; 0.) 
        self.ka = ka

        # Lead time constantLead time constant 
        self.tc = tc

        # Minimum controller output (&lt; 0.)Minimum controller output (&lt; 0.) 
        self.vrmin = vrmin

        # Time constant (&gt; 0.)Time constant (&gt; 0.) 
        self.ta = ta

        # Lag time constant (&gt;= 0.)Lag time constant (&gt;= 0.) 
        self.tb = tb

        # Maximum controller outputMaximum controller output 
        self.vrmax = vrmax

        # Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.) 
        self.kf = kf

        # Exciter field resistance line slopeExciter field resistance line slope 
        self.ke = ke

        # UEL input: if &lt; 2, HV gate; if = 2, add to error signalUEL input: if &lt; 2, HV gate; if = 2, add to error signal 
        self.uelin = uelin

        # Saturation factor at e1  (&gt;= 0.)Saturation factor at e1  (&gt;= 0.) 
        self.se1 = se1

        # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Saturation factor at e2  (&gt;= 0.)Saturation factor at e2  (&gt;= 0.) 
        self.se2 = se2

        # If not 0, apply lower limit of 0. to exciter outputIf not 0, apply lower limit of 0. to exciter output 
        self.exclim = exclim

        # Field voltage value 2.    (&gt; 0.)Field voltage value 2.    (&gt; 0.) 
        self.e2 = e2

        # Field voltage value 1     (&gt; 0.)Field voltage value 1     (&gt; 0.) 
        self.e1 = e1



        super(ExcDC2A, self).__init__(**kw_args)
    # >>> exc_dc2_a


    def __str__(self):
        """ Returns a string representation of the ExcDC2A.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_dc2_a.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcDC2A.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcDC2A", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ExcDC2A.te>%s</%s:ExcDC2A.te>' % \
            (indent, ns_prefix, self.te, ns_prefix)
        s += '%s<%s:ExcDC2A.tf>%s</%s:ExcDC2A.tf>' % \
            (indent, ns_prefix, self.tf, ns_prefix)
        s += '%s<%s:ExcDC2A.ka>%s</%s:ExcDC2A.ka>' % \
            (indent, ns_prefix, self.ka, ns_prefix)
        s += '%s<%s:ExcDC2A.tc>%s</%s:ExcDC2A.tc>' % \
            (indent, ns_prefix, self.tc, ns_prefix)
        s += '%s<%s:ExcDC2A.vrmin>%s</%s:ExcDC2A.vrmin>' % \
            (indent, ns_prefix, self.vrmin, ns_prefix)
        s += '%s<%s:ExcDC2A.ta>%s</%s:ExcDC2A.ta>' % \
            (indent, ns_prefix, self.ta, ns_prefix)
        s += '%s<%s:ExcDC2A.tb>%s</%s:ExcDC2A.tb>' % \
            (indent, ns_prefix, self.tb, ns_prefix)
        s += '%s<%s:ExcDC2A.vrmax>%s</%s:ExcDC2A.vrmax>' % \
            (indent, ns_prefix, self.vrmax, ns_prefix)
        s += '%s<%s:ExcDC2A.kf>%s</%s:ExcDC2A.kf>' % \
            (indent, ns_prefix, self.kf, ns_prefix)
        s += '%s<%s:ExcDC2A.ke>%s</%s:ExcDC2A.ke>' % \
            (indent, ns_prefix, self.ke, ns_prefix)
        s += '%s<%s:ExcDC2A.uelin>%s</%s:ExcDC2A.uelin>' % \
            (indent, ns_prefix, self.uelin, ns_prefix)
        s += '%s<%s:ExcDC2A.se1>%s</%s:ExcDC2A.se1>' % \
            (indent, ns_prefix, self.se1, ns_prefix)
        s += '%s<%s:ExcDC2A.tr>%s</%s:ExcDC2A.tr>' % \
            (indent, ns_prefix, self.tr, ns_prefix)
        s += '%s<%s:ExcDC2A.se2>%s</%s:ExcDC2A.se2>' % \
            (indent, ns_prefix, self.se2, ns_prefix)
        s += '%s<%s:ExcDC2A.exclim>%s</%s:ExcDC2A.exclim>' % \
            (indent, ns_prefix, self.exclim, ns_prefix)
        s += '%s<%s:ExcDC2A.e2>%s</%s:ExcDC2A.e2>' % \
            (indent, ns_prefix, self.e2, ns_prefix)
        s += '%s<%s:ExcDC2A.e1>%s</%s:ExcDC2A.e1>' % \
            (indent, ns_prefix, self.e1, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcDC2A")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_dc2_a.serialize


class ExcSEXS(ExcitationSystem):
    """ Simplified Excitation System ModelSimplified Excitation System Model
    """
    # <<< exc_sexs
    # @generated
    def __init__(self, k=0.0, tatb=0.0, efdmin=0.0, te=0.0, tc=0.0, kc=0.0, tb=0.0, emin=0.0, emax=0.0, efdmax=0.0, **kw_args):
        """ Initialises a new 'ExcSEXS' instance.
        """
        # Gain (&gt; 0.)Gain (&gt; 0.) 
        self.k = k

        # Ta/Tb - gain reduction ratio of lag-lead elementTa/Tb - gain reduction ratio of lag-lead element 
        self.tatb = tatb

        # Field voltage clipping minimum limitField voltage clipping minimum limit 
        self.efdmin = efdmin

        # Time constant of gain block (&gt; 0.)Time constant of gain block (&gt; 0.) 
        self.te = te

        # PI controller phase lead time constantPI controller phase lead time constant 
        self.tc = tc

        # PI controller gain (&gt; 0. if Tc &gt; 0.)PI controller gain (&gt; 0. if Tc &gt; 0.) 
        self.kc = kc

        # Denominator time constant of lag-lead blockDenominator time constant of lag-lead block 
        self.tb = tb

        # Minimum field voltage outputMinimum field voltage output 
        self.emin = emin

        # Maximum field voltage outputMaximum field voltage output 
        self.emax = emax

        # Field voltage clipping maximum limitField voltage clipping maximum limit 
        self.efdmax = efdmax



        super(ExcSEXS, self).__init__(**kw_args)
    # >>> exc_sexs


    def __str__(self):
        """ Returns a string representation of the ExcSEXS.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_sexs.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcSEXS.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcSEXS", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ExcSEXS.k>%s</%s:ExcSEXS.k>' % \
            (indent, ns_prefix, self.k, ns_prefix)
        s += '%s<%s:ExcSEXS.tatb>%s</%s:ExcSEXS.tatb>' % \
            (indent, ns_prefix, self.tatb, ns_prefix)
        s += '%s<%s:ExcSEXS.efdmin>%s</%s:ExcSEXS.efdmin>' % \
            (indent, ns_prefix, self.efdmin, ns_prefix)
        s += '%s<%s:ExcSEXS.te>%s</%s:ExcSEXS.te>' % \
            (indent, ns_prefix, self.te, ns_prefix)
        s += '%s<%s:ExcSEXS.tc>%s</%s:ExcSEXS.tc>' % \
            (indent, ns_prefix, self.tc, ns_prefix)
        s += '%s<%s:ExcSEXS.kc>%s</%s:ExcSEXS.kc>' % \
            (indent, ns_prefix, self.kc, ns_prefix)
        s += '%s<%s:ExcSEXS.tb>%s</%s:ExcSEXS.tb>' % \
            (indent, ns_prefix, self.tb, ns_prefix)
        s += '%s<%s:ExcSEXS.emin>%s</%s:ExcSEXS.emin>' % \
            (indent, ns_prefix, self.emin, ns_prefix)
        s += '%s<%s:ExcSEXS.emax>%s</%s:ExcSEXS.emax>' % \
            (indent, ns_prefix, self.emax, ns_prefix)
        s += '%s<%s:ExcSEXS.efdmax>%s</%s:ExcSEXS.efdmax>' % \
            (indent, ns_prefix, self.efdmax, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcSEXS")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_sexs.serialize


class ExcELIN2(ExcitationSystem):
    """ Detailed Excitation System Model - ELIN (VATECH)Detailed Excitation System Model - ELIN (VATECH)
    """
    pass
    # <<< exc_elin2
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ExcELIN2' instance.
        """


        super(ExcELIN2, self).__init__(**kw_args)
    # >>> exc_elin2


    def __str__(self):
        """ Returns a string representation of the ExcELIN2.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_elin2.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcELIN2.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcELIN2", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcELIN2")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_elin2.serialize


class ExcAC4A(ExcitationSystem):
    """ IEEE (1992/2005) AC4A Model  The Type AC4A alternator-supplied controlled-rectifier excitation system is quite different from the other type ac systems. This high initial response excitation system utilizes a full thyristor bridge in the exciter output circuit. The voltage regulator controls the firing of the thyristor bridges. The exciter alternator uses an independent voltage regulator to control its output voltage to a constant value. These effects are not modeled; however, transient loading effects on the exciter alternator are included.IEEE (1992/2005) AC4A Model  The Type AC4A alternator-supplied controlled-rectifier excitation system is quite different from the other type ac systems. This high initial response excitation system utilizes a full thyristor bridge in the exciter output circuit. The voltage regulator controls the firing of the thyristor bridges. The exciter alternator uses an independent voltage regulator to control its output voltage to a constant value. These effects are not modeled; however, transient loading effects on the exciter alternator are included.
    """
    # <<< exc_ac4_a
    # @generated
    def __init__(self, tb=0.0, ta=0.0, tc=0.0, vrmin=0.0, vimax=0.0, vrmax=0.0, tr=0.0, kc=0.0, vimin=0.0, ka=0.0, **kw_args):
        """ Initialises a new 'ExcAC4A' instance.
        """
        # Lag time constant (&gt;= 0.)Lag time constant (&gt;= 0.) 
        self.tb = tb

        # Time constant (&gt; 0.)Time constant (&gt; 0.) 
        self.ta = ta

        # Lead time constantLead time constant 
        self.tc = tc

        # Minimum controller output (&lt; 0.)Minimum controller output (&lt; 0.) 
        self.vrmin = vrmin

        # Maximum error signal ( &gt; 0.)Maximum error signal ( &gt; 0.) 
        self.vimax = vimax

        # Maximum controller output (&gt; 0.)Maximum controller output (&gt; 0.) 
        self.vrmax = vrmax

        # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Excitation system regulation (&gt;= 0.)Excitation system regulation (&gt;= 0.) 
        self.kc = kc

        # Minimum error signal (&lt; 0.)Minimum error signal (&lt; 0.) 
        self.vimin = vimin

        # Gain (&gt; 0.)Gain (&gt; 0.) 
        self.ka = ka



        super(ExcAC4A, self).__init__(**kw_args)
    # >>> exc_ac4_a


    def __str__(self):
        """ Returns a string representation of the ExcAC4A.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_ac4_a.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcAC4A.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcAC4A", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ExcAC4A.tb>%s</%s:ExcAC4A.tb>' % \
            (indent, ns_prefix, self.tb, ns_prefix)
        s += '%s<%s:ExcAC4A.ta>%s</%s:ExcAC4A.ta>' % \
            (indent, ns_prefix, self.ta, ns_prefix)
        s += '%s<%s:ExcAC4A.tc>%s</%s:ExcAC4A.tc>' % \
            (indent, ns_prefix, self.tc, ns_prefix)
        s += '%s<%s:ExcAC4A.vrmin>%s</%s:ExcAC4A.vrmin>' % \
            (indent, ns_prefix, self.vrmin, ns_prefix)
        s += '%s<%s:ExcAC4A.vimax>%s</%s:ExcAC4A.vimax>' % \
            (indent, ns_prefix, self.vimax, ns_prefix)
        s += '%s<%s:ExcAC4A.vrmax>%s</%s:ExcAC4A.vrmax>' % \
            (indent, ns_prefix, self.vrmax, ns_prefix)
        s += '%s<%s:ExcAC4A.tr>%s</%s:ExcAC4A.tr>' % \
            (indent, ns_prefix, self.tr, ns_prefix)
        s += '%s<%s:ExcAC4A.kc>%s</%s:ExcAC4A.kc>' % \
            (indent, ns_prefix, self.kc, ns_prefix)
        s += '%s<%s:ExcAC4A.vimin>%s</%s:ExcAC4A.vimin>' % \
            (indent, ns_prefix, self.vimin, ns_prefix)
        s += '%s<%s:ExcAC4A.ka>%s</%s:ExcAC4A.ka>' % \
            (indent, ns_prefix, self.ka, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcAC4A")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_ac4_a.serialize


class ExcSK(ExcitationSystem):
    """ Slovakian Excitation System Model (UEL, secondary voltage control)Slovakian Excitation System Model (UEL, secondary voltage control)
    """
    pass
    # <<< exc_sk
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ExcSK' instance.
        """


        super(ExcSK, self).__init__(**kw_args)
    # >>> exc_sk


    def __str__(self):
        """ Returns a string representation of the ExcSK.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_sk.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcSK.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcSK", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcSK")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_sk.serialize


class ExcAC2A(ExcitationSystem):
    """ IEEE (1992/2005) AC2A Model The model designated as Type AC2A, represents a high initial response fieldcontrolled alternator-rectifier excitation system. The alternator main exciter is used with non-controlled rectifiers. The Type AC2A model is similar to that of Type AC1A except for the inclusion of exciter time constant compensation and exciter field current limiting elements.IEEE (1992/2005) AC2A Model The model designated as Type AC2A, represents a high initial response fieldcontrolled alternator-rectifier excitation system. The alternator main exciter is used with non-controlled rectifiers. The Type AC2A model is similar to that of Type AC1A except for the inclusion of exciter time constant compensation and exciter field current limiting elements.
    """
    # <<< exc_ac2_a
    # @generated
    def __init__(self, tb=0.0, e1=0.0, ta=0.0, vrmin=0.0, e2=0.0, vfemax=0.0, vrmax=0.0, ka=0.0, se1=0.0, se2=0.0, kf=0.0, kh=0.0, kc=0.0, vamin=0.0, kb=0.0, ke=0.0, tr=0.0, kd=0.0, te=0.0, tc=0.0, vamax=0.0, tf=0.0, **kw_args):
        """ Initialises a new 'ExcAC2A' instance.
        """
        # TGR lag time constant (&gt;= 0.)TGR lag time constant (&gt;= 0.) 
        self.tb = tb

        # Field voltage value 1     (&gt; 0.)Field voltage value 1     (&gt; 0.) 
        self.e1 = e1

        # AVR time constant (&gt; 0.)AVR time constant (&gt; 0.) 
        self.ta = ta

        # Minimum exciter control signal (&lt; 0.)Minimum exciter control signal (&lt; 0.) 
        self.vrmin = vrmin

        # Field voltage value 2.    (&gt; 0.)Field voltage value 2.    (&gt; 0.) 
        self.e2 = e2

        # Exciter field current limit parameter (&gt;= 0.)Exciter field current limit parameter (&gt;= 0.) 
        self.vfemax = vfemax

        # Maximum exciter control signal (&gt; 0.)Maximum exciter control signal (&gt; 0.) 
        self.vrmax = vrmax

        # AVR gain (&gt; 0.)AVR gain (&gt; 0.) 
        self.ka = ka

        # Saturation factor at e1  (&gt;= 0.)Saturation factor at e1  (&gt;= 0.) 
        self.se1 = se1

        # Saturation factor at e2   (&gt;= 0.)Saturation factor at e2   (&gt;= 0.) 
        self.se2 = se2

        # Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.) 
        self.kf = kf

        # Exciter field current feedback gain (&gt;= 0.)Exciter field current feedback gain (&gt;= 0.) 
        self.kh = kh

        # Rectifier regulation factor (&gt;= 0.)Rectifier regulation factor (&gt;= 0.) 
        self.kc = kc

        # Minimum AVR output (&lt; 0.)Minimum AVR output (&lt; 0.) 
        self.vamin = vamin

        # Exciter field current controller gain (&gt; 0.)Exciter field current controller gain (&gt; 0.) 
        self.kb = kb

        # Exciter field resistance constantExciter field resistance constant 
        self.ke = ke

        # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Exciter internal reactance (&gt;= 0.)Exciter internal reactance (&gt;= 0.) 
        self.kd = kd

        # Exciter time constant (&gt; 0.)Exciter time constant (&gt; 0.) 
        self.te = te

        # TGR lead time constantTGR lead time constant 
        self.tc = tc

        # Maximum AVR output (&gt; 0.)Maximum AVR output (&gt; 0.) 
        self.vamax = vamax

        # Rate feedback time constant (&gt; 0.)Rate feedback time constant (&gt; 0.) 
        self.tf = tf



        super(ExcAC2A, self).__init__(**kw_args)
    # >>> exc_ac2_a


    def __str__(self):
        """ Returns a string representation of the ExcAC2A.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_ac2_a.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcAC2A.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcAC2A", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ExcAC2A.tb>%s</%s:ExcAC2A.tb>' % \
            (indent, ns_prefix, self.tb, ns_prefix)
        s += '%s<%s:ExcAC2A.e1>%s</%s:ExcAC2A.e1>' % \
            (indent, ns_prefix, self.e1, ns_prefix)
        s += '%s<%s:ExcAC2A.ta>%s</%s:ExcAC2A.ta>' % \
            (indent, ns_prefix, self.ta, ns_prefix)
        s += '%s<%s:ExcAC2A.vrmin>%s</%s:ExcAC2A.vrmin>' % \
            (indent, ns_prefix, self.vrmin, ns_prefix)
        s += '%s<%s:ExcAC2A.e2>%s</%s:ExcAC2A.e2>' % \
            (indent, ns_prefix, self.e2, ns_prefix)
        s += '%s<%s:ExcAC2A.vfemax>%s</%s:ExcAC2A.vfemax>' % \
            (indent, ns_prefix, self.vfemax, ns_prefix)
        s += '%s<%s:ExcAC2A.vrmax>%s</%s:ExcAC2A.vrmax>' % \
            (indent, ns_prefix, self.vrmax, ns_prefix)
        s += '%s<%s:ExcAC2A.ka>%s</%s:ExcAC2A.ka>' % \
            (indent, ns_prefix, self.ka, ns_prefix)
        s += '%s<%s:ExcAC2A.se1>%s</%s:ExcAC2A.se1>' % \
            (indent, ns_prefix, self.se1, ns_prefix)
        s += '%s<%s:ExcAC2A.se2>%s</%s:ExcAC2A.se2>' % \
            (indent, ns_prefix, self.se2, ns_prefix)
        s += '%s<%s:ExcAC2A.kf>%s</%s:ExcAC2A.kf>' % \
            (indent, ns_prefix, self.kf, ns_prefix)
        s += '%s<%s:ExcAC2A.kh>%s</%s:ExcAC2A.kh>' % \
            (indent, ns_prefix, self.kh, ns_prefix)
        s += '%s<%s:ExcAC2A.kc>%s</%s:ExcAC2A.kc>' % \
            (indent, ns_prefix, self.kc, ns_prefix)
        s += '%s<%s:ExcAC2A.vamin>%s</%s:ExcAC2A.vamin>' % \
            (indent, ns_prefix, self.vamin, ns_prefix)
        s += '%s<%s:ExcAC2A.kb>%s</%s:ExcAC2A.kb>' % \
            (indent, ns_prefix, self.kb, ns_prefix)
        s += '%s<%s:ExcAC2A.ke>%s</%s:ExcAC2A.ke>' % \
            (indent, ns_prefix, self.ke, ns_prefix)
        s += '%s<%s:ExcAC2A.tr>%s</%s:ExcAC2A.tr>' % \
            (indent, ns_prefix, self.tr, ns_prefix)
        s += '%s<%s:ExcAC2A.kd>%s</%s:ExcAC2A.kd>' % \
            (indent, ns_prefix, self.kd, ns_prefix)
        s += '%s<%s:ExcAC2A.te>%s</%s:ExcAC2A.te>' % \
            (indent, ns_prefix, self.te, ns_prefix)
        s += '%s<%s:ExcAC2A.tc>%s</%s:ExcAC2A.tc>' % \
            (indent, ns_prefix, self.tc, ns_prefix)
        s += '%s<%s:ExcAC2A.vamax>%s</%s:ExcAC2A.vamax>' % \
            (indent, ns_prefix, self.vamax, ns_prefix)
        s += '%s<%s:ExcAC2A.tf>%s</%s:ExcAC2A.tf>' % \
            (indent, ns_prefix, self.tf, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcAC2A")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_ac2_a.serialize


class ExcELIN1(ExcitationSystem):
    """ Simplified Excitation System Model - ELIN (VATECH)Simplified Excitation System Model - ELIN (VATECH)
    """
    pass
    # <<< exc_elin1
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ExcELIN1' instance.
        """


        super(ExcELIN1, self).__init__(**kw_args)
    # >>> exc_elin1


    def __str__(self):
        """ Returns a string representation of the ExcELIN1.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_elin1.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcELIN1.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcELIN1", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcELIN1")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_elin1.serialize


class ExcST6B(ExcitationSystem):
    """ IEEE (2005) ST6B Model  The AVR consists of a PI voltage regulator with an inner loop field voltage regulator and pre-control. The field voltage regulator implements a proportional control. The pre-control and the delay in the feedback circuit increase the dynamic response.IEEE (2005) ST6B Model  The AVR consists of a PI voltage regulator with an inner loop field voltage regulator and pre-control. The field voltage regulator implements a proportional control. The pre-control and the delay in the feedback circuit increase the dynamic response.
    """
    # <<< exc_st6_b
    # @generated
    def __init__(self, vamin=0.0, vrmin=0.0, km=0.0, ts=0.0, kg=0.0, tr=0.0, kcl=0.0, klr=0.0, vrmax=0.0, ilr=0.0, kpa=0.0, tg=0.0, vamax=0.0, oelin=0.0, kff=0.0, vmult=0.0, kia=0.0, **kw_args):
        """ Initialises a new 'ExcST6B' instance.
        """
        # PI minimum output (&lt; 0.)PI minimum output (&lt; 0.) 
        self.vamin = vamin

        # Minimum regulator output (&lt; 0.)Minimum regulator output (&lt; 0.) 
        self.vrmin = vrmin

        # Main gainMain gain 
        self.km = km

        # Rectifier firing time constant (not in IEEE model) (&gt;= 0.)Rectifier firing time constant (not in IEEE model) (&gt;= 0.) 
        self.ts = ts

        # Feedback gain (&gt;= 0.)Feedback gain (&gt;= 0.) 
        self.kg = kg

        # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Field current limiter conversion factor (&gt; 0.)Field current limiter conversion factor (&gt; 0.) 
        self.kcl = kcl

        # Field current limiter gain (&gt; 0.)Field current limiter gain (&gt; 0.) 
        self.klr = klr

        # Maximum regulator output (&gt; 0.)Maximum regulator output (&gt; 0.) 
        self.vrmax = vrmax

        # Field current limiter setpoint (&gt; 0.)Field current limiter setpoint (&gt; 0.) 
        self.ilr = ilr

        # Regulator proportional gain (&gt; 0.)Regulator proportional gain (&gt; 0.) 
        self.kpa = kpa

        # Feedback time constant (&gt;= 0.)Feedback time constant (&gt;= 0.) 
        self.tg = tg

        # PI maximum output. (&gt; 0.)PI maximum output. (&gt; 0.) 
        self.vamax = vamax

        # OEL input selector: 1 ? before UEL, 2 ? after UEL, 0 ? no OEL inputOEL input selector: 1 ? before UEL, 2 ? after UEL, 0 ? no OEL input 
        self.oelin = oelin

        # Feedforward gainFeedforward gain 
        self.kff = kff

        # If non-zero, multiply regulator output by terminal voltageIf non-zero, multiply regulator output by terminal voltage 
        self.vmult = vmult

        # Regulator integral gain (&gt; 0.)Regulator integral gain (&gt; 0.) 
        self.kia = kia



        super(ExcST6B, self).__init__(**kw_args)
    # >>> exc_st6_b


    def __str__(self):
        """ Returns a string representation of the ExcST6B.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_st6_b.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcST6B.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcST6B", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ExcST6B.vamin>%s</%s:ExcST6B.vamin>' % \
            (indent, ns_prefix, self.vamin, ns_prefix)
        s += '%s<%s:ExcST6B.vrmin>%s</%s:ExcST6B.vrmin>' % \
            (indent, ns_prefix, self.vrmin, ns_prefix)
        s += '%s<%s:ExcST6B.km>%s</%s:ExcST6B.km>' % \
            (indent, ns_prefix, self.km, ns_prefix)
        s += '%s<%s:ExcST6B.ts>%s</%s:ExcST6B.ts>' % \
            (indent, ns_prefix, self.ts, ns_prefix)
        s += '%s<%s:ExcST6B.kg>%s</%s:ExcST6B.kg>' % \
            (indent, ns_prefix, self.kg, ns_prefix)
        s += '%s<%s:ExcST6B.tr>%s</%s:ExcST6B.tr>' % \
            (indent, ns_prefix, self.tr, ns_prefix)
        s += '%s<%s:ExcST6B.kcl>%s</%s:ExcST6B.kcl>' % \
            (indent, ns_prefix, self.kcl, ns_prefix)
        s += '%s<%s:ExcST6B.klr>%s</%s:ExcST6B.klr>' % \
            (indent, ns_prefix, self.klr, ns_prefix)
        s += '%s<%s:ExcST6B.vrmax>%s</%s:ExcST6B.vrmax>' % \
            (indent, ns_prefix, self.vrmax, ns_prefix)
        s += '%s<%s:ExcST6B.ilr>%s</%s:ExcST6B.ilr>' % \
            (indent, ns_prefix, self.ilr, ns_prefix)
        s += '%s<%s:ExcST6B.kpa>%s</%s:ExcST6B.kpa>' % \
            (indent, ns_prefix, self.kpa, ns_prefix)
        s += '%s<%s:ExcST6B.tg>%s</%s:ExcST6B.tg>' % \
            (indent, ns_prefix, self.tg, ns_prefix)
        s += '%s<%s:ExcST6B.vamax>%s</%s:ExcST6B.vamax>' % \
            (indent, ns_prefix, self.vamax, ns_prefix)
        s += '%s<%s:ExcST6B.oelin>%s</%s:ExcST6B.oelin>' % \
            (indent, ns_prefix, self.oelin, ns_prefix)
        s += '%s<%s:ExcST6B.kff>%s</%s:ExcST6B.kff>' % \
            (indent, ns_prefix, self.kff, ns_prefix)
        s += '%s<%s:ExcST6B.vmult>%s</%s:ExcST6B.vmult>' % \
            (indent, ns_prefix, self.vmult, ns_prefix)
        s += '%s<%s:ExcST6B.kia>%s</%s:ExcST6B.kia>' % \
            (indent, ns_prefix, self.kia, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcST6B")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_st6_b.serialize


class ExcST4B(ExcitationSystem):
    """ IEEE (2005) ST4B Model  This model is a variation of the Type ST3A model, with a proportional plus integral (PI) regulator block replacing the lag-lead regulator characteristic that was in the ST3A model. Both potential- and compoundsource rectifier excitation systems are modeled. The PI regulator blocks have nonwindup limits that are represented. The voltage regulator of this model is typically implemented digitally.IEEE (2005) ST4B Model  This model is a variation of the Type ST3A model, with a proportional plus integral (PI) regulator block replacing the lag-lead regulator characteristic that was in the ST3A model. Both potential- and compoundsource rectifier excitation systems are modeled. The PI regulator blocks have nonwindup limits that are represented. The voltage regulator of this model is typically implemented digitally.
    """
    # <<< exc_st4_b
    # @generated
    def __init__(self, kp=0.0, xl=0.0, vbmax=0.0, ki=0.0, kir=0.0, vrmin=0.0, vmmin=0.0, kim=0.0, ta=0.0, kg=0.0, tr=0.0, kc=0.0, vrmax=0.0, angp=0.0, kpr=0.0, vgmax=0.0, kpm=0.0, vmmax=0.0, **kw_args):
        """ Initialises a new 'ExcST4B' instance.
        """
        # Potential source gain (&gt; 0.)Potential source gain (&gt; 0.) 
        self.kp = kp

        # P-bar leakage reactance (&gt;= 0.)P-bar leakage reactance (&gt;= 0.) 
        self.xl = xl

        # Maximum excitation voltage (&gt; 0.)Maximum excitation voltage (&gt; 0.) 
        self.vbmax = vbmax

        # Current source gain (&gt;= 0.)Current source gain (&gt;= 0.) 
        self.ki = ki

        # AVR Integral gainAVR Integral gain 
        self.kir = kir

        # Minimum AVR output (&lt; 0.)Minimum AVR output (&lt; 0.) 
        self.vrmin = vrmin

        # Minimum inner loop regulator outputMinimum inner loop regulator output 
        self.vmmin = vmmin

        # Integral gain of inner loop regulatorIntegral gain of inner loop regulator 
        self.kim = kim

        # AVR time constant (&gt;= 0.)AVR time constant (&gt;= 0.) 
        self.ta = ta

        # Inner loop feedback gain (&gt;= 0.)Inner loop feedback gain (&gt;= 0.) 
        self.kg = kg

        # Voltage transducer time constant (&gt;= 0.)Voltage transducer time constant (&gt;= 0.) 
        self.tr = tr

        # Exciter regulation factor (&gt;= 0.)Exciter regulation factor (&gt;= 0.) 
        self.kc = kc

        # Maximum AVR output (&gt; 0.)Maximum AVR output (&gt; 0.) 
        self.vrmax = vrmax

        # Phase angle of potential sourcePhase angle of potential source 
        self.angp = angp

        # AVR proportional gainAVR proportional gain 
        self.kpr = kpr

        # Maximum inner loop feedback gain (&gt;= 0.)Maximum inner loop feedback gain (&gt;= 0.) 
        self.vgmax = vgmax

        # Prop. gain of inner loop regulatorProp. gain of inner loop regulator 
        self.kpm = kpm

        # Maximum inner loop regulator outputMaximum inner loop regulator output 
        self.vmmax = vmmax



        super(ExcST4B, self).__init__(**kw_args)
    # >>> exc_st4_b


    def __str__(self):
        """ Returns a string representation of the ExcST4B.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_st4_b.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcST4B.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcST4B", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ExcST4B.kp>%s</%s:ExcST4B.kp>' % \
            (indent, ns_prefix, self.kp, ns_prefix)
        s += '%s<%s:ExcST4B.xl>%s</%s:ExcST4B.xl>' % \
            (indent, ns_prefix, self.xl, ns_prefix)
        s += '%s<%s:ExcST4B.vbmax>%s</%s:ExcST4B.vbmax>' % \
            (indent, ns_prefix, self.vbmax, ns_prefix)
        s += '%s<%s:ExcST4B.ki>%s</%s:ExcST4B.ki>' % \
            (indent, ns_prefix, self.ki, ns_prefix)
        s += '%s<%s:ExcST4B.kir>%s</%s:ExcST4B.kir>' % \
            (indent, ns_prefix, self.kir, ns_prefix)
        s += '%s<%s:ExcST4B.vrmin>%s</%s:ExcST4B.vrmin>' % \
            (indent, ns_prefix, self.vrmin, ns_prefix)
        s += '%s<%s:ExcST4B.vmmin>%s</%s:ExcST4B.vmmin>' % \
            (indent, ns_prefix, self.vmmin, ns_prefix)
        s += '%s<%s:ExcST4B.kim>%s</%s:ExcST4B.kim>' % \
            (indent, ns_prefix, self.kim, ns_prefix)
        s += '%s<%s:ExcST4B.ta>%s</%s:ExcST4B.ta>' % \
            (indent, ns_prefix, self.ta, ns_prefix)
        s += '%s<%s:ExcST4B.kg>%s</%s:ExcST4B.kg>' % \
            (indent, ns_prefix, self.kg, ns_prefix)
        s += '%s<%s:ExcST4B.tr>%s</%s:ExcST4B.tr>' % \
            (indent, ns_prefix, self.tr, ns_prefix)
        s += '%s<%s:ExcST4B.kc>%s</%s:ExcST4B.kc>' % \
            (indent, ns_prefix, self.kc, ns_prefix)
        s += '%s<%s:ExcST4B.vrmax>%s</%s:ExcST4B.vrmax>' % \
            (indent, ns_prefix, self.vrmax, ns_prefix)
        s += '%s<%s:ExcST4B.angp>%s</%s:ExcST4B.angp>' % \
            (indent, ns_prefix, self.angp, ns_prefix)
        s += '%s<%s:ExcST4B.kpr>%s</%s:ExcST4B.kpr>' % \
            (indent, ns_prefix, self.kpr, ns_prefix)
        s += '%s<%s:ExcST4B.vgmax>%s</%s:ExcST4B.vgmax>' % \
            (indent, ns_prefix, self.vgmax, ns_prefix)
        s += '%s<%s:ExcST4B.kpm>%s</%s:ExcST4B.kpm>' % \
            (indent, ns_prefix, self.kpm, ns_prefix)
        s += '%s<%s:ExcST4B.vmmax>%s</%s:ExcST4B.vmmax>' % \
            (indent, ns_prefix, self.vmmax, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcST4B")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_st4_b.serialize


class ExcWT3E(ExcitationSystem):
    """ Type 3 standard wind turbine converter control modelType 3 standard wind turbine converter control model
    """
    pass
    # <<< exc_wt3_e
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ExcWT3E' instance.
        """


        super(ExcWT3E, self).__init__(**kw_args)
    # >>> exc_wt3_e


    def __str__(self):
        """ Returns a string representation of the ExcWT3E.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_wt3_e.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcWT3E.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcWT3E", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcWT3E")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_wt3_e.serialize


class ExcPIC(ExcitationSystem):
    """ Excitation System Model with PI voltage regulatorExcitation System Model with PI voltage regulator
    """
    pass
    # <<< exc_pic
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ExcPIC' instance.
        """


        super(ExcPIC, self).__init__(**kw_args)
    # >>> exc_pic


    def __str__(self):
        """ Returns a string representation of the ExcPIC.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_pic.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcPIC.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcPIC", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcPIC")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_pic.serialize


class ExcSK2(ExcitationSystem):
    """ Slovakian alternator-rectifier Excitation System Model (UEL, secondary voltage control)Slovakian alternator-rectifier Excitation System Model (UEL, secondary voltage control)
    """
    pass
    # <<< exc_sk2
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ExcSK2' instance.
        """


        super(ExcSK2, self).__init__(**kw_args)
    # >>> exc_sk2


    def __str__(self):
        """ Returns a string representation of the ExcSK2.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_sk2.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcSK2.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcSK2", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcSK2")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_sk2.serialize


class ExcST2A(ExcitationSystem):
    """ IEEE (1992/2005) ST2A Model  Some static systems utilize both current and voltage sources (generator terminal quantities) to comprise the power source. These compound-source rectifier excitation systems are designated Type ST2A. The regulator controls the exciter output through controlled saturation of the power transformer components.IEEE (1992/2005) ST2A Model  Some static systems utilize both current and voltage sources (generator terminal quantities) to comprise the power source. These compound-source rectifier excitation systems are designated Type ST2A. The regulator controls the exciter output through controlled saturation of the power transformer components.
    """
    # <<< exc_st2_a
    # @generated
    def __init__(self, vrmin=0.0, tc=0.0, tb=0.0, ta=0.0, ka=0.0, ke=0.0, uelin=0.0, kc=0.0, te=0.0, ki=0.0, kf=0.0, tf=0.0, vrmax=0.0, efdmax=0.0, tr=0.0, kp=0.0, **kw_args):
        """ Initialises a new 'ExcST2A' instance.
        """
        # Minimum controller output (&lt; 0.)Minimum controller output (&lt; 0.) 
        self.vrmin = vrmin

        # Time constantTime constant 
        self.tc = tc

        # Time constant (&gt;=0.)Time constant (&gt;=0.) 
        self.tb = tb

        # Time constant (&gt; 0.)Time constant (&gt; 0.) 
        self.ta = ta

        # Gain (&gt; 0.)Gain (&gt; 0.) 
        self.ka = ka

        # Time constant feedbackTime constant feedback 
        self.ke = ke

        # UEL input: if = 1, HV gate; if = 2, add to error signalUEL input: if = 1, HV gate; if = 2, add to error signal 
        self.uelin = uelin

        # Rectifier loading factor (&gt;= 0.)Rectifier loading factor (&gt;= 0.) 
        self.kc = kc

        # Transformer saturation control time constant (&gt; 0.)Transformer saturation control time constant (&gt; 0.) 
        self.te = te

        # Current source gain (&gt;= 0.)Current source gain (&gt;= 0.) 
        self.ki = ki

        # Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.) 
        self.kf = kf

        # Rate feedback time constant (&gt;= 0.)Rate feedback time constant (&gt;= 0.) 
        self.tf = tf

        # Maximum controller output (&gt; 0.)Maximum controller output (&gt; 0.) 
        self.vrmax = vrmax

        # Maximum field voltage (&gt;=0.)Maximum field voltage (&gt;=0.) 
        self.efdmax = efdmax

        # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Potential source gain (&gt;= 0.)Potential source gain (&gt;= 0.) 
        self.kp = kp



        super(ExcST2A, self).__init__(**kw_args)
    # >>> exc_st2_a


    def __str__(self):
        """ Returns a string representation of the ExcST2A.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_st2_a.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcST2A.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcST2A", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ExcST2A.vrmin>%s</%s:ExcST2A.vrmin>' % \
            (indent, ns_prefix, self.vrmin, ns_prefix)
        s += '%s<%s:ExcST2A.tc>%s</%s:ExcST2A.tc>' % \
            (indent, ns_prefix, self.tc, ns_prefix)
        s += '%s<%s:ExcST2A.tb>%s</%s:ExcST2A.tb>' % \
            (indent, ns_prefix, self.tb, ns_prefix)
        s += '%s<%s:ExcST2A.ta>%s</%s:ExcST2A.ta>' % \
            (indent, ns_prefix, self.ta, ns_prefix)
        s += '%s<%s:ExcST2A.ka>%s</%s:ExcST2A.ka>' % \
            (indent, ns_prefix, self.ka, ns_prefix)
        s += '%s<%s:ExcST2A.ke>%s</%s:ExcST2A.ke>' % \
            (indent, ns_prefix, self.ke, ns_prefix)
        s += '%s<%s:ExcST2A.uelin>%s</%s:ExcST2A.uelin>' % \
            (indent, ns_prefix, self.uelin, ns_prefix)
        s += '%s<%s:ExcST2A.kc>%s</%s:ExcST2A.kc>' % \
            (indent, ns_prefix, self.kc, ns_prefix)
        s += '%s<%s:ExcST2A.te>%s</%s:ExcST2A.te>' % \
            (indent, ns_prefix, self.te, ns_prefix)
        s += '%s<%s:ExcST2A.ki>%s</%s:ExcST2A.ki>' % \
            (indent, ns_prefix, self.ki, ns_prefix)
        s += '%s<%s:ExcST2A.kf>%s</%s:ExcST2A.kf>' % \
            (indent, ns_prefix, self.kf, ns_prefix)
        s += '%s<%s:ExcST2A.tf>%s</%s:ExcST2A.tf>' % \
            (indent, ns_prefix, self.tf, ns_prefix)
        s += '%s<%s:ExcST2A.vrmax>%s</%s:ExcST2A.vrmax>' % \
            (indent, ns_prefix, self.vrmax, ns_prefix)
        s += '%s<%s:ExcST2A.efdmax>%s</%s:ExcST2A.efdmax>' % \
            (indent, ns_prefix, self.efdmax, ns_prefix)
        s += '%s<%s:ExcST2A.tr>%s</%s:ExcST2A.tr>' % \
            (indent, ns_prefix, self.tr, ns_prefix)
        s += '%s<%s:ExcST2A.kp>%s</%s:ExcST2A.kp>' % \
            (indent, ns_prefix, self.kp, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcST2A")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_st2_a.serialize


class ExcHU(ExcitationSystem):
    """ Hungarian Excitation System ModelHungarian Excitation System Model
    """
    pass
    # <<< exc_hu
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ExcHU' instance.
        """


        super(ExcHU, self).__init__(**kw_args)
    # >>> exc_hu


    def __str__(self):
        """ Returns a string representation of the ExcHU.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_hu.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcHU.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcHU", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcHU")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_hu.serialize


class ExcREXS(ExcitationSystem):
    """ General Purpose Rotating Excitation System ModelGeneral Purpose Rotating Excitation System Model
    """
    pass
    # <<< exc_rexs
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ExcREXS' instance.
        """


        super(ExcREXS, self).__init__(**kw_args)
    # >>> exc_rexs


    def __str__(self):
        """ Returns a string representation of the ExcREXS.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_rexs.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcREXS.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcREXS", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcREXS")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_rexs.serialize


class ExcST7B(ExcitationSystem):
    """ IEEE (2005) ST7B Model  The model ST7B is representative of static potential-source excitation systems. In this system, the AVR consists of a PI voltage regulator. A phase lead-lag filter in series allows introduction of a derivative function, typically used with brushless excitation systems. In that case, the regulator is of the PID type. In addition, the terminal voltage channel includes a phase lead-lag filter. The AVR includes the appropriate inputs on its reference for overexcitation limiter (OEL1), underexcitation limiter (UEL), stator current limiter (SCL), and current compensator (DROOP). All these limitations, when they work at voltage reference level, keep the PSS (VS signal from Type PSS1A, PSS2A, or PSS2B) in operation. However, the UEL limitation can also be transferred to the high value (HV) gate acting on the output signal. In addition, the output signal passes through a low value (LV) gate for a ceiling overexcitation limiter (OEL2).IEEE (2005) ST7B Model  The model ST7B is representative of static potential-source excitation systems. In this system, the AVR consists of a PI voltage regulator. A phase lead-lag filter in series allows introduction of a derivative function, typically used with brushless excitation systems. In that case, the regulator is of the PID type. In addition, the terminal voltage channel includes a phase lead-lag filter. The AVR includes the appropriate inputs on its reference for overexcitation limiter (OEL1), underexcitation limiter (UEL), stator current limiter (SCL), and current compensator (DROOP). All these limitations, when they work at voltage reference level, keep the PSS (VS signal from Type PSS1A, PSS2A, or PSS2B) in operation. However, the UEL limitation can also be transferred to the high value (HV) gate acting on the output signal. In addition, the output signal passes through a low value (LV) gate for a ceiling overexcitation limiter (OEL2).
    """
    # <<< exc_st7_b
    # @generated
    def __init__(self, tg=0.0, kpa=0.0, vmin=0.0, vrmax=0.0, kl=0.0, tr=0.0, kh=0.0, ts=0.0, vrmin=0.0, oelin=0.0, uelin=0.0, tia=0.0, tb=0.0, tc=0.0, tf=0.0, kia=0.0, vmax=0.0, **kw_args):
        """ Initialises a new 'ExcST7B' instance.
        """
        # Input lead-lag numerator time constant (&gt;= 0.)Input lead-lag numerator time constant (&gt;= 0.) 
        self.tg = tg

        # Regulator proportional gain (&gt; 0.)Regulator proportional gain (&gt; 0.) 
        self.kpa = kpa

        # Minimum voltage reference signal (&gt; 0.)Minimum voltage reference signal (&gt; 0.) 
        self.vmin = vmin

        # Maximum field voltage output (&gt; 0.)Maximum field voltage output (&gt; 0.) 
        self.vrmax = vrmax

        # Low-value gate feedback gain (&gt;= 0.)Low-value gate feedback gain (&gt;= 0.) 
        self.kl = kl

        # Filter time constantFilter time constant 
        self.tr = tr

        # High-value gate feedback gain (&gt;= 0.)High-value gate feedback gain (&gt;= 0.) 
        self.kh = kh

        # Rectifier firing time constant (&gt;= 0.) (not in IEEE model)Rectifier firing time constant (&gt;= 0.) (not in IEEE model) 
        self.ts = ts

        # Minimum field voltage output (&lt; 0.)Minimum field voltage output (&lt; 0.) 
        self.vrmin = vrmin

        # OEL input selector: 1 ? add to Vref, 2 ? input LV gate,  2 ? output LV gate, 0 ? no OEL inputOEL input selector: 1 ? add to Vref, 2 ? input LV gate,  2 ? output LV gate, 0 ? no OEL input 
        self.oelin = oelin

        # UEL input selector: 1 ? add to Vref, 2 ? input HV gate,  3 ? output HV gate, 0 ? no UEL inputUEL input selector: 1 ? add to Vref, 2 ? input HV gate,  3 ? output HV gate, 0 ? no UEL input 
        self.uelin = uelin

        # Feedback time constant (&gt;= 0.)Feedback time constant (&gt;= 0.) 
        self.tia = tia

        # Lead-lag denominator time constant (&gt;= 0.)Lead-lag denominator time constant (&gt;= 0.) 
        self.tb = tb

        # Lead-lag numerator time constant (&gt;= 0.)Lead-lag numerator time constant (&gt;= 0.) 
        self.tc = tc

        # Input lead-lag denominator time constant (&gt;= 0.)Input lead-lag denominator time constant (&gt;= 0.) 
        self.tf = tf

        # Feedback gain (&gt;= 0.)Feedback gain (&gt;= 0.) 
        self.kia = kia

        # Maximum voltage reference signal (&gt; 0.)Maximum voltage reference signal (&gt; 0.) 
        self.vmax = vmax



        super(ExcST7B, self).__init__(**kw_args)
    # >>> exc_st7_b


    def __str__(self):
        """ Returns a string representation of the ExcST7B.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_st7_b.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcST7B.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcST7B", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ExcST7B.tg>%s</%s:ExcST7B.tg>' % \
            (indent, ns_prefix, self.tg, ns_prefix)
        s += '%s<%s:ExcST7B.kpa>%s</%s:ExcST7B.kpa>' % \
            (indent, ns_prefix, self.kpa, ns_prefix)
        s += '%s<%s:ExcST7B.vmin>%s</%s:ExcST7B.vmin>' % \
            (indent, ns_prefix, self.vmin, ns_prefix)
        s += '%s<%s:ExcST7B.vrmax>%s</%s:ExcST7B.vrmax>' % \
            (indent, ns_prefix, self.vrmax, ns_prefix)
        s += '%s<%s:ExcST7B.kl>%s</%s:ExcST7B.kl>' % \
            (indent, ns_prefix, self.kl, ns_prefix)
        s += '%s<%s:ExcST7B.tr>%s</%s:ExcST7B.tr>' % \
            (indent, ns_prefix, self.tr, ns_prefix)
        s += '%s<%s:ExcST7B.kh>%s</%s:ExcST7B.kh>' % \
            (indent, ns_prefix, self.kh, ns_prefix)
        s += '%s<%s:ExcST7B.ts>%s</%s:ExcST7B.ts>' % \
            (indent, ns_prefix, self.ts, ns_prefix)
        s += '%s<%s:ExcST7B.vrmin>%s</%s:ExcST7B.vrmin>' % \
            (indent, ns_prefix, self.vrmin, ns_prefix)
        s += '%s<%s:ExcST7B.oelin>%s</%s:ExcST7B.oelin>' % \
            (indent, ns_prefix, self.oelin, ns_prefix)
        s += '%s<%s:ExcST7B.uelin>%s</%s:ExcST7B.uelin>' % \
            (indent, ns_prefix, self.uelin, ns_prefix)
        s += '%s<%s:ExcST7B.tia>%s</%s:ExcST7B.tia>' % \
            (indent, ns_prefix, self.tia, ns_prefix)
        s += '%s<%s:ExcST7B.tb>%s</%s:ExcST7B.tb>' % \
            (indent, ns_prefix, self.tb, ns_prefix)
        s += '%s<%s:ExcST7B.tc>%s</%s:ExcST7B.tc>' % \
            (indent, ns_prefix, self.tc, ns_prefix)
        s += '%s<%s:ExcST7B.tf>%s</%s:ExcST7B.tf>' % \
            (indent, ns_prefix, self.tf, ns_prefix)
        s += '%s<%s:ExcST7B.kia>%s</%s:ExcST7B.kia>' % \
            (indent, ns_prefix, self.kia, ns_prefix)
        s += '%s<%s:ExcST7B.vmax>%s</%s:ExcST7B.vmax>' % \
            (indent, ns_prefix, self.vmax, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcST7B")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_st7_b.serialize


class ExcAC1A(ExcitationSystem):
    """ IEEE (1992/2005) AC1A Model The model represents the field-controlled alternator-rectifier excitation systems designated Type AC1A. These excitation systems consist of an alternator main exciter with non-controlled rectifiers.IEEE (1992/2005) AC1A Model The model represents the field-controlled alternator-rectifier excitation systems designated Type AC1A. These excitation systems consist of an alternator main exciter with non-controlled rectifiers.
    """
    # <<< exc_ac1_a
    # @generated
    def __init__(self, se1=0.0, se2=0.0, e2=0.0, e1=0.0, tr=0.0, vamin=0.0, vamax=0.0, vrmax=0.0, tb=0.0, kd=0.0, tc=0.0, kc=0.0, kf=0.0, ta=0.0, vrmin=0.0, ke=0.0, te=0.0, tf=0.0, ka=0.0, **kw_args):
        """ Initialises a new 'ExcAC1A' instance.
        """
        # Saturation factor at e1  (&gt;= 0.)Saturation factor at e1  (&gt;= 0.) 
        self.se1 = se1

        # Saturation factor at e2   (&gt;= 0.)Saturation factor at e2   (&gt;= 0.) 
        self.se2 = se2

        # Field voltage value 2.   (&gt; 0.)Field voltage value 2.   (&gt; 0.) 
        self.e2 = e2

        # Field voltage value 1    (&gt; 0.)Field voltage value 1    (&gt; 0.) 
        self.e1 = e1

        # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Minimum AVR output (&lt; 0.)Minimum AVR output (&lt; 0.) 
        self.vamin = vamin

        # Maximum AVR output (&gt; 0.)Maximum AVR output (&gt; 0.) 
        self.vamax = vamax

        # Maximum exciter control signal (&gt; 0.)Maximum exciter control signal (&gt; 0.) 
        self.vrmax = vrmax

        # TGR lag time constant (&gt;= 0.)TGR lag time constant (&gt;= 0.) 
        self.tb = tb

        # Exciter internal reactance  (&gt;= 0.)Exciter internal reactance  (&gt;= 0.) 
        self.kd = kd

        # TGR lead time constantTGR lead time constant 
        self.tc = tc

        # Rectifier regulation factor (&gt;= 0.)Rectifier regulation factor (&gt;= 0.) 
        self.kc = kc

        # Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.) 
        self.kf = kf

        # AVR time constant (&gt; 0.)AVR time constant (&gt; 0.) 
        self.ta = ta

        # Minimum exciter control signal  (&lt; 0.)Minimum exciter control signal  (&lt; 0.) 
        self.vrmin = vrmin

        # Exciter field resistance constantExciter field resistance constant 
        self.ke = ke

        # Exciter time constant (&gt; 0.)Exciter time constant (&gt; 0.) 
        self.te = te

        # Rate feedback time constant (&gt; 0.)Rate feedback time constant (&gt; 0.) 
        self.tf = tf

        # AVR gain (&gt; 0.)AVR gain (&gt; 0.) 
        self.ka = ka



        super(ExcAC1A, self).__init__(**kw_args)
    # >>> exc_ac1_a


    def __str__(self):
        """ Returns a string representation of the ExcAC1A.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_ac1_a.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcAC1A.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcAC1A", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ExcAC1A.se1>%s</%s:ExcAC1A.se1>' % \
            (indent, ns_prefix, self.se1, ns_prefix)
        s += '%s<%s:ExcAC1A.se2>%s</%s:ExcAC1A.se2>' % \
            (indent, ns_prefix, self.se2, ns_prefix)
        s += '%s<%s:ExcAC1A.e2>%s</%s:ExcAC1A.e2>' % \
            (indent, ns_prefix, self.e2, ns_prefix)
        s += '%s<%s:ExcAC1A.e1>%s</%s:ExcAC1A.e1>' % \
            (indent, ns_prefix, self.e1, ns_prefix)
        s += '%s<%s:ExcAC1A.tr>%s</%s:ExcAC1A.tr>' % \
            (indent, ns_prefix, self.tr, ns_prefix)
        s += '%s<%s:ExcAC1A.vamin>%s</%s:ExcAC1A.vamin>' % \
            (indent, ns_prefix, self.vamin, ns_prefix)
        s += '%s<%s:ExcAC1A.vamax>%s</%s:ExcAC1A.vamax>' % \
            (indent, ns_prefix, self.vamax, ns_prefix)
        s += '%s<%s:ExcAC1A.vrmax>%s</%s:ExcAC1A.vrmax>' % \
            (indent, ns_prefix, self.vrmax, ns_prefix)
        s += '%s<%s:ExcAC1A.tb>%s</%s:ExcAC1A.tb>' % \
            (indent, ns_prefix, self.tb, ns_prefix)
        s += '%s<%s:ExcAC1A.kd>%s</%s:ExcAC1A.kd>' % \
            (indent, ns_prefix, self.kd, ns_prefix)
        s += '%s<%s:ExcAC1A.tc>%s</%s:ExcAC1A.tc>' % \
            (indent, ns_prefix, self.tc, ns_prefix)
        s += '%s<%s:ExcAC1A.kc>%s</%s:ExcAC1A.kc>' % \
            (indent, ns_prefix, self.kc, ns_prefix)
        s += '%s<%s:ExcAC1A.kf>%s</%s:ExcAC1A.kf>' % \
            (indent, ns_prefix, self.kf, ns_prefix)
        s += '%s<%s:ExcAC1A.ta>%s</%s:ExcAC1A.ta>' % \
            (indent, ns_prefix, self.ta, ns_prefix)
        s += '%s<%s:ExcAC1A.vrmin>%s</%s:ExcAC1A.vrmin>' % \
            (indent, ns_prefix, self.vrmin, ns_prefix)
        s += '%s<%s:ExcAC1A.ke>%s</%s:ExcAC1A.ke>' % \
            (indent, ns_prefix, self.ke, ns_prefix)
        s += '%s<%s:ExcAC1A.te>%s</%s:ExcAC1A.te>' % \
            (indent, ns_prefix, self.te, ns_prefix)
        s += '%s<%s:ExcAC1A.tf>%s</%s:ExcAC1A.tf>' % \
            (indent, ns_prefix, self.tf, ns_prefix)
        s += '%s<%s:ExcAC1A.ka>%s</%s:ExcAC1A.ka>' % \
            (indent, ns_prefix, self.ka, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcAC1A")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_ac1_a.serialize


class ExcDC4B(ExcitationSystem):
    """ IEEE (2005) DC4B Model  These excitation systems utilize a field-controlled dc commutator exciter with a continuously acting voltage regulator having supplies obtained from the generator or auxiliary bus. The replacement of the controls only as an upgrade (retaining the dc commutator exciter) has resulted in a new model. This excitation system typically includes a proportional, integral, and differential (PID) generator voltage regulator (AVR). An alternative rate feedback loop (<i>kf</i>, <i>tf</i>) for stabilization is also shown in the model if the AVR does not include a derivative term. If a PSS control is supplied, the appropriate model is the Type PSS2B model.IEEE (2005) DC4B Model  These excitation systems utilize a field-controlled dc commutator exciter with a continuously acting voltage regulator having supplies obtained from the generator or auxiliary bus. The replacement of the controls only as an upgrade (retaining the dc commutator exciter) has resulted in a new model. This excitation system typically includes a proportional, integral, and differential (PID) generator voltage regulator (AVR). An alternative rate feedback loop (<i>kf</i>, <i>tf</i>) for stabilization is also shown in the model if the AVR does not include a derivative term. If a PSS control is supplied, the appropriate model is the Type PSS2B model.
    """
    # <<< exc_dc4_b
    # @generated
    def __init__(self, vrmin=0.0, uelin=0.0, ki=0.0, kp=0.0, e2=0.0, oelin=0.0, vrmax=0.0, kf=0.0, te=0.0, ke=0.0, vemin=0.0, tf=0.0, kd=0.0, se2=0.0, ta=0.0, tr=0.0, ka=0.0, se1=0.0, td=0.0, e1=0.0, **kw_args):
        """ Initialises a new 'ExcDC4B' instance.
        """
        # Minimum controller output (&lt;= 0.)Minimum controller output (&lt;= 0.) 
        self.vrmin = vrmin

        # UEL input: if &lt; 2, HV gate; if = 2, add to error signalUEL input: if &lt; 2, HV gate; if = 2, add to error signal 
        self.uelin = uelin

        # Integral gain (&gt;= 0.)Integral gain (&gt;= 0.) 
        self.ki = ki

        # Proportional gain (&gt;= 0.)Proportional gain (&gt;= 0.) 
        self.kp = kp

        # Field voltage value 2.   (&gt; 0.)Field voltage value 2.   (&gt; 0.) 
        self.e2 = e2

        # OEL input: if &lt; 2, LV gate; if = 2, subtract from error signalOEL input: if &lt; 2, LV gate; if = 2, subtract from error signal 
        self.oelin = oelin

        # Maximum controller outputMaximum controller output 
        self.vrmax = vrmax

        # Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.) 
        self.kf = kf

        # Exciter time constant (&gt; 0.)Exciter time constant (&gt; 0.) 
        self.te = te

        # Exciter field resistance line slopeExciter field resistance line slope 
        self.ke = ke

        # Exciter minimum output  (&lt;= 0.)Exciter minimum output  (&lt;= 0.) 
        self.vemin = vemin

        # Rate feedback time constant (&gt;= 0.)Rate feedback time constant (&gt;= 0.) 
        self.tf = tf

        # Derivative gain (&gt;= 0.)Derivative gain (&gt;= 0.) 
        self.kd = kd

        # Saturation factor at e2 (&gt;= 0.)Saturation factor at e2 (&gt;= 0.) 
        self.se2 = se2

        # Time constant (&gt; 0.)Time constant (&gt; 0.) 
        self.ta = ta

        # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Gain (&gt; 0.)Gain (&gt; 0.) 
        self.ka = ka

        # Saturation factor at e1   (&gt;= 0.)Saturation factor at e1   (&gt;= 0.) 
        self.se1 = se1

        # Derivative time constant (&gt; 0. If kd &gt; 0.)Derivative time constant (&gt; 0. If kd &gt; 0.) 
        self.td = td

        # Field voltage value 1     (&gt; 0.)Field voltage value 1     (&gt; 0.) 
        self.e1 = e1



        super(ExcDC4B, self).__init__(**kw_args)
    # >>> exc_dc4_b


    def __str__(self):
        """ Returns a string representation of the ExcDC4B.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_dc4_b.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcDC4B.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcDC4B", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ExcDC4B.vrmin>%s</%s:ExcDC4B.vrmin>' % \
            (indent, ns_prefix, self.vrmin, ns_prefix)
        s += '%s<%s:ExcDC4B.uelin>%s</%s:ExcDC4B.uelin>' % \
            (indent, ns_prefix, self.uelin, ns_prefix)
        s += '%s<%s:ExcDC4B.ki>%s</%s:ExcDC4B.ki>' % \
            (indent, ns_prefix, self.ki, ns_prefix)
        s += '%s<%s:ExcDC4B.kp>%s</%s:ExcDC4B.kp>' % \
            (indent, ns_prefix, self.kp, ns_prefix)
        s += '%s<%s:ExcDC4B.e2>%s</%s:ExcDC4B.e2>' % \
            (indent, ns_prefix, self.e2, ns_prefix)
        s += '%s<%s:ExcDC4B.oelin>%s</%s:ExcDC4B.oelin>' % \
            (indent, ns_prefix, self.oelin, ns_prefix)
        s += '%s<%s:ExcDC4B.vrmax>%s</%s:ExcDC4B.vrmax>' % \
            (indent, ns_prefix, self.vrmax, ns_prefix)
        s += '%s<%s:ExcDC4B.kf>%s</%s:ExcDC4B.kf>' % \
            (indent, ns_prefix, self.kf, ns_prefix)
        s += '%s<%s:ExcDC4B.te>%s</%s:ExcDC4B.te>' % \
            (indent, ns_prefix, self.te, ns_prefix)
        s += '%s<%s:ExcDC4B.ke>%s</%s:ExcDC4B.ke>' % \
            (indent, ns_prefix, self.ke, ns_prefix)
        s += '%s<%s:ExcDC4B.vemin>%s</%s:ExcDC4B.vemin>' % \
            (indent, ns_prefix, self.vemin, ns_prefix)
        s += '%s<%s:ExcDC4B.tf>%s</%s:ExcDC4B.tf>' % \
            (indent, ns_prefix, self.tf, ns_prefix)
        s += '%s<%s:ExcDC4B.kd>%s</%s:ExcDC4B.kd>' % \
            (indent, ns_prefix, self.kd, ns_prefix)
        s += '%s<%s:ExcDC4B.se2>%s</%s:ExcDC4B.se2>' % \
            (indent, ns_prefix, self.se2, ns_prefix)
        s += '%s<%s:ExcDC4B.ta>%s</%s:ExcDC4B.ta>' % \
            (indent, ns_prefix, self.ta, ns_prefix)
        s += '%s<%s:ExcDC4B.tr>%s</%s:ExcDC4B.tr>' % \
            (indent, ns_prefix, self.tr, ns_prefix)
        s += '%s<%s:ExcDC4B.ka>%s</%s:ExcDC4B.ka>' % \
            (indent, ns_prefix, self.ka, ns_prefix)
        s += '%s<%s:ExcDC4B.se1>%s</%s:ExcDC4B.se1>' % \
            (indent, ns_prefix, self.se1, ns_prefix)
        s += '%s<%s:ExcDC4B.td>%s</%s:ExcDC4B.td>' % \
            (indent, ns_prefix, self.td, ns_prefix)
        s += '%s<%s:ExcDC4B.e1>%s</%s:ExcDC4B.e1>' % \
            (indent, ns_prefix, self.e1, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcDC4B")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_dc4_b.serialize


class ExcDC1A(ExcitationSystem):
    """ IEEE (1992/2005) DC1A Model  This model is used to represent field-controlled dc commutator exciters with continuously acting voltage regulators (especially the direct-acting rheostatic, rotating amplifier, and magnetic amplifier types). Because this model has been widely implemented by the industry, it is sometimes used to represent other types of systems when detailed data for them are not available or when a simplified model is required.IEEE (1992/2005) DC1A Model  This model is used to represent field-controlled dc commutator exciters with continuously acting voltage regulators (especially the direct-acting rheostatic, rotating amplifier, and magnetic amplifier types). Because this model has been widely implemented by the industry, it is sometimes used to represent other types of systems when detailed data for them are not available or when a simplified model is required.
    """
    # <<< exc_dc1_a
    # @generated
    def __init__(self, exclim=0.0, vrmin=0.0, tc=0.0, ta=0.0, tb=0.0, ka=0.0, ke=0.0, se2=0.0, te=0.0, se1=0.0, tf=0.0, kf=0.0, uelin=0.0, tr=0.0, e1=0.0, vrmax=0.0, e2=0.0, **kw_args):
        """ Initialises a new 'ExcDC1A' instance.
        """
        # If not 0, apply lower limit of 0. to exciter outputIf not 0, apply lower limit of 0. to exciter output 
        self.exclim = exclim

        # Minimum controller output (&lt; 0.)Minimum controller output (&lt; 0.) 
        self.vrmin = vrmin

        # Lead time constantLead time constant 
        self.tc = tc

        # Time constant (&gt; 0.)Time constant (&gt; 0.) 
        self.ta = ta

        # Lag time constant (&gt;= 0.)Lag time constant (&gt;= 0.) 
        self.tb = tb

        # Gain (&gt; 0.)Gain (&gt; 0.) 
        self.ka = ka

        # Exciter field resistance line slopeExciter field resistance line slope 
        self.ke = ke

        # Saturation factor at e2  (&gt;= 0.)Saturation factor at e2  (&gt;= 0.) 
        self.se2 = se2

        # Exciter time constant (&gt; 0.)Exciter time constant (&gt; 0.) 
        self.te = te

        # Saturation factor at e1  (&gt;= 0.)Saturation factor at e1  (&gt;= 0.) 
        self.se1 = se1

        # Rate feedback time constant, sec. (&gt; 0.)Rate feedback time constant, sec. (&gt; 0.) 
        self.tf = tf

        # Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.) 
        self.kf = kf

        # UEL input: if &lt; 2, HV gate; if = 2, add to error signalUEL input: if &lt; 2, HV gate; if = 2, add to error signal 
        self.uelin = uelin

        # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Field voltage value 1    (&gt; 0.)Field voltage value 1    (&gt; 0.) 
        self.e1 = e1

        # Maximum controller outputMaximum controller output 
        self.vrmax = vrmax

        # Field voltage value 2.   (&gt; 0.)Field voltage value 2.   (&gt; 0.) 
        self.e2 = e2



        super(ExcDC1A, self).__init__(**kw_args)
    # >>> exc_dc1_a


    def __str__(self):
        """ Returns a string representation of the ExcDC1A.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_dc1_a.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcDC1A.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcDC1A", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ExcDC1A.exclim>%s</%s:ExcDC1A.exclim>' % \
            (indent, ns_prefix, self.exclim, ns_prefix)
        s += '%s<%s:ExcDC1A.vrmin>%s</%s:ExcDC1A.vrmin>' % \
            (indent, ns_prefix, self.vrmin, ns_prefix)
        s += '%s<%s:ExcDC1A.tc>%s</%s:ExcDC1A.tc>' % \
            (indent, ns_prefix, self.tc, ns_prefix)
        s += '%s<%s:ExcDC1A.ta>%s</%s:ExcDC1A.ta>' % \
            (indent, ns_prefix, self.ta, ns_prefix)
        s += '%s<%s:ExcDC1A.tb>%s</%s:ExcDC1A.tb>' % \
            (indent, ns_prefix, self.tb, ns_prefix)
        s += '%s<%s:ExcDC1A.ka>%s</%s:ExcDC1A.ka>' % \
            (indent, ns_prefix, self.ka, ns_prefix)
        s += '%s<%s:ExcDC1A.ke>%s</%s:ExcDC1A.ke>' % \
            (indent, ns_prefix, self.ke, ns_prefix)
        s += '%s<%s:ExcDC1A.se2>%s</%s:ExcDC1A.se2>' % \
            (indent, ns_prefix, self.se2, ns_prefix)
        s += '%s<%s:ExcDC1A.te>%s</%s:ExcDC1A.te>' % \
            (indent, ns_prefix, self.te, ns_prefix)
        s += '%s<%s:ExcDC1A.se1>%s</%s:ExcDC1A.se1>' % \
            (indent, ns_prefix, self.se1, ns_prefix)
        s += '%s<%s:ExcDC1A.tf>%s</%s:ExcDC1A.tf>' % \
            (indent, ns_prefix, self.tf, ns_prefix)
        s += '%s<%s:ExcDC1A.kf>%s</%s:ExcDC1A.kf>' % \
            (indent, ns_prefix, self.kf, ns_prefix)
        s += '%s<%s:ExcDC1A.uelin>%s</%s:ExcDC1A.uelin>' % \
            (indent, ns_prefix, self.uelin, ns_prefix)
        s += '%s<%s:ExcDC1A.tr>%s</%s:ExcDC1A.tr>' % \
            (indent, ns_prefix, self.tr, ns_prefix)
        s += '%s<%s:ExcDC1A.e1>%s</%s:ExcDC1A.e1>' % \
            (indent, ns_prefix, self.e1, ns_prefix)
        s += '%s<%s:ExcDC1A.vrmax>%s</%s:ExcDC1A.vrmax>' % \
            (indent, ns_prefix, self.vrmax, ns_prefix)
        s += '%s<%s:ExcDC1A.e2>%s</%s:ExcDC1A.e2>' % \
            (indent, ns_prefix, self.e2, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcDC1A")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_dc1_a.serialize


class ExcAC3A(ExcitationSystem):
    """ IEEE (1992/2005) AC3A Model  The model represents the field-controlled alternator-rectifier excitation systems designated Type AC3A. These excitation systems include an alternator main exciter with non-controlled rectifiers. The exciter employs self-excitation, and the voltage regulator power is derived from the exciter output voltage. Therefore, this system has an additional nonlinearity, simulated by the use of a multiplier whose inputs are the voltage regulator command signal, <i>VA</i>, and the exciter output voltage, <i>EFD</i>, times <i>KR</i>. This model is applicable to excitation systems employing static voltage regulators.IEEE (1992/2005) AC3A Model  The model represents the field-controlled alternator-rectifier excitation systems designated Type AC3A. These excitation systems include an alternator main exciter with non-controlled rectifiers. The exciter employs self-excitation, and the voltage regulator power is derived from the exciter output voltage. Therefore, this system has an additional nonlinearity, simulated by the use of a multiplier whose inputs are the voltage regulator command signal, <i>VA</i>, and the exciter output voltage, <i>EFD</i>, times <i>KR</i>. This model is applicable to excitation systems employing static voltage regulators.
    """
    # <<< exc_ac3_a
    # @generated
    def __init__(self, ta=0.0, ka=0.0, kd=0.0, se1=0.0, kc=0.0, se2=0.0, te=0.0, tf=0.0, tb=0.0, tc=0.0, vamax=0.0, kf=0.0, vemin=0.0, ke=0.0, vfemax=0.0, tr=0.0, e2=0.0, e1=0.0, kn=0.0, vamin=0.0, kr=0.0, efdn=0.0, **kw_args):
        """ Initialises a new 'ExcAC3A' instance.
        """
        # AVR time constant (&gt; 0.)AVR time constant (&gt; 0.) 
        self.ta = ta

        # AVR gain (&gt; 0.)AVR gain (&gt; 0.) 
        self.ka = ka

        # Exciter internal reactance (&gt;= 0.)Exciter internal reactance (&gt;= 0.) 
        self.kd = kd

        # Saturation factor at e1   (&gt;= 0.)Saturation factor at e1   (&gt;= 0.) 
        self.se1 = se1

        # Rectifier regulation factor (&gt;= 0.)Rectifier regulation factor (&gt;= 0.) 
        self.kc = kc

        # Saturation factor at e2   (&gt;= 0.)Saturation factor at e2   (&gt;= 0.) 
        self.se2 = se2

        # Exciter time constant (&gt; 0.)Exciter time constant (&gt; 0.) 
        self.te = te

        # Rate feedback time constant (&gt; 0.)Rate feedback time constant (&gt; 0.) 
        self.tf = tf

        # TGR lag time constant (&gt;= 0.)TGR lag time constant (&gt;= 0.) 
        self.tb = tb

        # TGR lead time constantTGR lead time constant 
        self.tc = tc

        # Maximum AVR output (&gt; 0.)Maximum AVR output (&gt; 0.) 
        self.vamax = vamax

        # Low level rate feedback gain (&gt;= 0.)Low level rate feedback gain (&gt;= 0.) 
        self.kf = kf

        # Minimum field voltage limit (&lt;= 0.)Minimum field voltage limit (&lt;= 0.) 
        self.vemin = vemin

        # Exciter field resistance constantExciter field resistance constant 
        self.ke = ke

        # Exciter field current limit parameter (&gt;= 0.)Exciter field current limit parameter (&gt;= 0.) 
        self.vfemax = vfemax

        # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Field voltage value 2.     (&gt; 0.)Field voltage value 2.     (&gt; 0.) 
        self.e2 = e2

        # Field voltage value 1     (&gt; 0.)Field voltage value 1     (&gt; 0.) 
        self.e1 = e1

        # High level rate feedback gain (&gt;= 0.)High level rate feedback gain (&gt;= 0.) 
        self.kn = kn

        # Minimum AVR output (&lt; 0.)Minimum AVR output (&lt; 0.) 
        self.vamin = vamin

        # Field self-excitation feedback gain (&gt; 0.)Field self-excitation feedback gain (&gt; 0.) 
        self.kr = kr

        # Rate feedback gain break level (&gt; 0.)Rate feedback gain break level (&gt; 0.) 
        self.efdn = efdn



        super(ExcAC3A, self).__init__(**kw_args)
    # >>> exc_ac3_a


    def __str__(self):
        """ Returns a string representation of the ExcAC3A.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_ac3_a.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcAC3A.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcAC3A", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ExcAC3A.ta>%s</%s:ExcAC3A.ta>' % \
            (indent, ns_prefix, self.ta, ns_prefix)
        s += '%s<%s:ExcAC3A.ka>%s</%s:ExcAC3A.ka>' % \
            (indent, ns_prefix, self.ka, ns_prefix)
        s += '%s<%s:ExcAC3A.kd>%s</%s:ExcAC3A.kd>' % \
            (indent, ns_prefix, self.kd, ns_prefix)
        s += '%s<%s:ExcAC3A.se1>%s</%s:ExcAC3A.se1>' % \
            (indent, ns_prefix, self.se1, ns_prefix)
        s += '%s<%s:ExcAC3A.kc>%s</%s:ExcAC3A.kc>' % \
            (indent, ns_prefix, self.kc, ns_prefix)
        s += '%s<%s:ExcAC3A.se2>%s</%s:ExcAC3A.se2>' % \
            (indent, ns_prefix, self.se2, ns_prefix)
        s += '%s<%s:ExcAC3A.te>%s</%s:ExcAC3A.te>' % \
            (indent, ns_prefix, self.te, ns_prefix)
        s += '%s<%s:ExcAC3A.tf>%s</%s:ExcAC3A.tf>' % \
            (indent, ns_prefix, self.tf, ns_prefix)
        s += '%s<%s:ExcAC3A.tb>%s</%s:ExcAC3A.tb>' % \
            (indent, ns_prefix, self.tb, ns_prefix)
        s += '%s<%s:ExcAC3A.tc>%s</%s:ExcAC3A.tc>' % \
            (indent, ns_prefix, self.tc, ns_prefix)
        s += '%s<%s:ExcAC3A.vamax>%s</%s:ExcAC3A.vamax>' % \
            (indent, ns_prefix, self.vamax, ns_prefix)
        s += '%s<%s:ExcAC3A.kf>%s</%s:ExcAC3A.kf>' % \
            (indent, ns_prefix, self.kf, ns_prefix)
        s += '%s<%s:ExcAC3A.vemin>%s</%s:ExcAC3A.vemin>' % \
            (indent, ns_prefix, self.vemin, ns_prefix)
        s += '%s<%s:ExcAC3A.ke>%s</%s:ExcAC3A.ke>' % \
            (indent, ns_prefix, self.ke, ns_prefix)
        s += '%s<%s:ExcAC3A.vfemax>%s</%s:ExcAC3A.vfemax>' % \
            (indent, ns_prefix, self.vfemax, ns_prefix)
        s += '%s<%s:ExcAC3A.tr>%s</%s:ExcAC3A.tr>' % \
            (indent, ns_prefix, self.tr, ns_prefix)
        s += '%s<%s:ExcAC3A.e2>%s</%s:ExcAC3A.e2>' % \
            (indent, ns_prefix, self.e2, ns_prefix)
        s += '%s<%s:ExcAC3A.e1>%s</%s:ExcAC3A.e1>' % \
            (indent, ns_prefix, self.e1, ns_prefix)
        s += '%s<%s:ExcAC3A.kn>%s</%s:ExcAC3A.kn>' % \
            (indent, ns_prefix, self.kn, ns_prefix)
        s += '%s<%s:ExcAC3A.vamin>%s</%s:ExcAC3A.vamin>' % \
            (indent, ns_prefix, self.vamin, ns_prefix)
        s += '%s<%s:ExcAC3A.kr>%s</%s:ExcAC3A.kr>' % \
            (indent, ns_prefix, self.kr, ns_prefix)
        s += '%s<%s:ExcAC3A.efdn>%s</%s:ExcAC3A.efdn>' % \
            (indent, ns_prefix, self.efdn, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcAC3A")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_ac3_a.serialize


class ExcAC6A(ExcitationSystem):
    """ IEEE (1992/2005) AC6A Model  The model is used to represent field-controlled alternator-rectifier excitation systems with system-supplied electronic voltage regulators. The maximum output of the regulator, <i>V</i><i><sub>R</sub></i>, is a function of terminal voltage, <i>V</i><i><sub>T</sub></i>. The field current limiter included in the original model AC6A remains in the 2005 update.IEEE (1992/2005) AC6A Model  The model is used to represent field-controlled alternator-rectifier excitation systems with system-supplied electronic voltage regulators. The maximum output of the regulator, <i>V</i><i><sub>R</sub></i>, is a function of terminal voltage, <i>V</i><i><sub>T</sub></i>. The field current limiter included in the original model AC6A remains in the 2005 update.
    """
    # <<< exc_ac6_a
    # @generated
    def __init__(self, vamax=0.0, vfelim=0.0, tr=0.0, e2=0.0, e1=0.0, vamin=0.0, vhmax=0.0, vrmax=0.0, se1=0.0, se2=0.0, vrmin=0.0, te=0.0, kh=0.0, tb=0.0, tc=0.0, ta=0.0, ka=0.0, kc=0.0, tj=0.0, tk=0.0, ke=0.0, th=0.0, kd=0.0, **kw_args):
        """ Initialises a new 'ExcAC6A' instance.
        """
        # Maximum controller element output (&gt; 0.)Maximum controller element output (&gt; 0.) 
        self.vamax = vamax

        # Exciter field current limit reference (&gt; 0.)Exciter field current limit reference (&gt; 0.) 
        self.vfelim = vfelim

        # Filter time constantFilter time constant 
        self.tr = tr

        # Field voltage value 2.    (&gt; 0.)Field voltage value 2.    (&gt; 0.) 
        self.e2 = e2

        # Field voltage value 1     (&gt; 0.)Field voltage value 1     (&gt; 0.) 
        self.e1 = e1

        # Minimum controller element output (&lt; 0.)Minimum controller element output (&lt; 0.) 
        self.vamin = vamin

        # Maximum field current limiter signal (&gt; 0.)Maximum field current limiter signal (&gt; 0.) 
        self.vhmax = vhmax

        # Maximum exciter control signal (&gt; 0.)Maximum exciter control signal (&gt; 0.) 
        self.vrmax = vrmax

        # Saturation factor at e1 (&gt;= 0.)Saturation factor at e1 (&gt;= 0.) 
        self.se1 = se1

        # Saturation factor at e2  (&gt;= 0.)Saturation factor at e2  (&gt;= 0.) 
        self.se2 = se2

        # Minimum exciter control signal (&lt; 0.)Minimum exciter control signal (&lt; 0.) 
        self.vrmin = vrmin

        # Exciter time constant (&gt; 0.)Exciter time constant (&gt; 0.) 
        self.te = te

        # Exciter field current limiter gain (&gt;= 0.)Exciter field current limiter gain (&gt;= 0.) 
        self.kh = kh

        # Time constant (&gt;= 0.)Time constant (&gt;= 0.) 
        self.tb = tb

        # Lead time constantLead time constant 
        self.tc = tc

        # Time constant (&gt;= 0.)Time constant (&gt;= 0.) 
        self.ta = ta

        # Gain (&gt; 0.)Gain (&gt; 0.) 
        self.ka = ka

        # Rectifier regulation factor (&gt;= 0.)Rectifier regulation factor (&gt;= 0.) 
        self.kc = kc

        # Field current limiter time constant (&gt;= 0.)Field current limiter time constant (&gt;= 0.) 
        self.tj = tj

        # Lag time constant (&gt;= 0.)Lag time constant (&gt;= 0.) 
        self.tk = tk

        # Exciter field resistance constantExciter field resistance constant 
        self.ke = ke

        # Field current limiter time constant (&gt; 0.)Field current limiter time constant (&gt; 0.) 
        self.th = th

        # Exciter internal reactance (&gt;= 0.)Exciter internal reactance (&gt;= 0.) 
        self.kd = kd



        super(ExcAC6A, self).__init__(**kw_args)
    # >>> exc_ac6_a


    def __str__(self):
        """ Returns a string representation of the ExcAC6A.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_ac6_a.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcAC6A.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcAC6A", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ExcAC6A.vamax>%s</%s:ExcAC6A.vamax>' % \
            (indent, ns_prefix, self.vamax, ns_prefix)
        s += '%s<%s:ExcAC6A.vfelim>%s</%s:ExcAC6A.vfelim>' % \
            (indent, ns_prefix, self.vfelim, ns_prefix)
        s += '%s<%s:ExcAC6A.tr>%s</%s:ExcAC6A.tr>' % \
            (indent, ns_prefix, self.tr, ns_prefix)
        s += '%s<%s:ExcAC6A.e2>%s</%s:ExcAC6A.e2>' % \
            (indent, ns_prefix, self.e2, ns_prefix)
        s += '%s<%s:ExcAC6A.e1>%s</%s:ExcAC6A.e1>' % \
            (indent, ns_prefix, self.e1, ns_prefix)
        s += '%s<%s:ExcAC6A.vamin>%s</%s:ExcAC6A.vamin>' % \
            (indent, ns_prefix, self.vamin, ns_prefix)
        s += '%s<%s:ExcAC6A.vhmax>%s</%s:ExcAC6A.vhmax>' % \
            (indent, ns_prefix, self.vhmax, ns_prefix)
        s += '%s<%s:ExcAC6A.vrmax>%s</%s:ExcAC6A.vrmax>' % \
            (indent, ns_prefix, self.vrmax, ns_prefix)
        s += '%s<%s:ExcAC6A.se1>%s</%s:ExcAC6A.se1>' % \
            (indent, ns_prefix, self.se1, ns_prefix)
        s += '%s<%s:ExcAC6A.se2>%s</%s:ExcAC6A.se2>' % \
            (indent, ns_prefix, self.se2, ns_prefix)
        s += '%s<%s:ExcAC6A.vrmin>%s</%s:ExcAC6A.vrmin>' % \
            (indent, ns_prefix, self.vrmin, ns_prefix)
        s += '%s<%s:ExcAC6A.te>%s</%s:ExcAC6A.te>' % \
            (indent, ns_prefix, self.te, ns_prefix)
        s += '%s<%s:ExcAC6A.kh>%s</%s:ExcAC6A.kh>' % \
            (indent, ns_prefix, self.kh, ns_prefix)
        s += '%s<%s:ExcAC6A.tb>%s</%s:ExcAC6A.tb>' % \
            (indent, ns_prefix, self.tb, ns_prefix)
        s += '%s<%s:ExcAC6A.tc>%s</%s:ExcAC6A.tc>' % \
            (indent, ns_prefix, self.tc, ns_prefix)
        s += '%s<%s:ExcAC6A.ta>%s</%s:ExcAC6A.ta>' % \
            (indent, ns_prefix, self.ta, ns_prefix)
        s += '%s<%s:ExcAC6A.ka>%s</%s:ExcAC6A.ka>' % \
            (indent, ns_prefix, self.ka, ns_prefix)
        s += '%s<%s:ExcAC6A.kc>%s</%s:ExcAC6A.kc>' % \
            (indent, ns_prefix, self.kc, ns_prefix)
        s += '%s<%s:ExcAC6A.tj>%s</%s:ExcAC6A.tj>' % \
            (indent, ns_prefix, self.tj, ns_prefix)
        s += '%s<%s:ExcAC6A.tk>%s</%s:ExcAC6A.tk>' % \
            (indent, ns_prefix, self.tk, ns_prefix)
        s += '%s<%s:ExcAC6A.ke>%s</%s:ExcAC6A.ke>' % \
            (indent, ns_prefix, self.ke, ns_prefix)
        s += '%s<%s:ExcAC6A.th>%s</%s:ExcAC6A.th>' % \
            (indent, ns_prefix, self.th, ns_prefix)
        s += '%s<%s:ExcAC6A.kd>%s</%s:ExcAC6A.kd>' % \
            (indent, ns_prefix, self.kd, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcAC6A")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_ac6_a.serialize


class ExcAC5A(ExcitationSystem):
    """ IEEE (1992/2005) AC5A Model  The model designated as Type AC5A, is a simplified model for brushless excitation systems. The regulator is supplied from a source, such as a permanent magnet generator, which is not affected by system disturbances. Unlike other ac models, this model uses loaded rather than open circuit exciter saturation data in the same way as it is used for the dc models. Because the model has been widely implemented by the industry, it is sometimes used to represent other types of systems when either detailed data for them are not available or simplified models are required.IEEE (1992/2005) AC5A Model  The model designated as Type AC5A, is a simplified model for brushless excitation systems. The regulator is supplied from a source, such as a permanent magnet generator, which is not affected by system disturbances. Unlike other ac models, this model uses loaded rather than open circuit exciter saturation data in the same way as it is used for the dc models. Because the model has been widely implemented by the industry, it is sometimes used to represent other types of systems when either detailed data for them are not available or simplified models are required.
    """
    # <<< exc_ac5_a
    # @generated
    def __init__(self, ta=0.0, vrmax=0.0, ka=0.0, vrmin=0.0, tr=0.0, tf1=0.0, ke=0.0, tf2=0.0, te=0.0, kf=0.0, e1=0.0, tf3=0.0, e2=0.0, se1=0.0, se2=0.0, **kw_args):
        """ Initialises a new 'ExcAC5A' instance.
        """
        # Time constant (&gt; 0.)Time constant (&gt; 0.) 
        self.ta = ta

        # Maximum controller output (&gt; 0.)Maximum controller output (&gt; 0.) 
        self.vrmax = vrmax

        # Gain  (&gt; 0.)Gain  (&gt; 0.) 
        self.ka = ka

        # Minimum controller output (&lt;  0.)Minimum controller output (&lt;  0.) 
        self.vrmin = vrmin

        # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Rate feedback lag time constant (&gt; 0.)Rate feedback lag time constant (&gt; 0.) 
        self.tf1 = tf1

        # Exciter field resistance line slopeExciter field resistance line slope 
        self.ke = ke

        # Rate feedback lag time constant (&gt;= 0.)Rate feedback lag time constant (&gt;= 0.) 
        self.tf2 = tf2

        # Exciter time constant, sec. (&gt; 0.)Exciter time constant, sec. (&gt; 0.) 
        self.te = te

        # Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.) 
        self.kf = kf

        # Field voltage value 1      (&gt; 0.)Field voltage value 1      (&gt; 0.) 
        self.e1 = e1

        # Rate feedback lead time constantRate feedback lead time constant 
        self.tf3 = tf3

        # Field voltage value 2.  (&gt; 0.)Field voltage value 2.  (&gt; 0.) 
        self.e2 = e2

        # Saturation factor at e1  (&gt;= 0.)Saturation factor at e1  (&gt;= 0.) 
        self.se1 = se1

        # Saturation factor at e2 (&gt;= 0.)Saturation factor at e2 (&gt;= 0.) 
        self.se2 = se2



        super(ExcAC5A, self).__init__(**kw_args)
    # >>> exc_ac5_a


    def __str__(self):
        """ Returns a string representation of the ExcAC5A.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_ac5_a.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcAC5A.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcAC5A", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ExcAC5A.ta>%s</%s:ExcAC5A.ta>' % \
            (indent, ns_prefix, self.ta, ns_prefix)
        s += '%s<%s:ExcAC5A.vrmax>%s</%s:ExcAC5A.vrmax>' % \
            (indent, ns_prefix, self.vrmax, ns_prefix)
        s += '%s<%s:ExcAC5A.ka>%s</%s:ExcAC5A.ka>' % \
            (indent, ns_prefix, self.ka, ns_prefix)
        s += '%s<%s:ExcAC5A.vrmin>%s</%s:ExcAC5A.vrmin>' % \
            (indent, ns_prefix, self.vrmin, ns_prefix)
        s += '%s<%s:ExcAC5A.tr>%s</%s:ExcAC5A.tr>' % \
            (indent, ns_prefix, self.tr, ns_prefix)
        s += '%s<%s:ExcAC5A.tf1>%s</%s:ExcAC5A.tf1>' % \
            (indent, ns_prefix, self.tf1, ns_prefix)
        s += '%s<%s:ExcAC5A.ke>%s</%s:ExcAC5A.ke>' % \
            (indent, ns_prefix, self.ke, ns_prefix)
        s += '%s<%s:ExcAC5A.tf2>%s</%s:ExcAC5A.tf2>' % \
            (indent, ns_prefix, self.tf2, ns_prefix)
        s += '%s<%s:ExcAC5A.te>%s</%s:ExcAC5A.te>' % \
            (indent, ns_prefix, self.te, ns_prefix)
        s += '%s<%s:ExcAC5A.kf>%s</%s:ExcAC5A.kf>' % \
            (indent, ns_prefix, self.kf, ns_prefix)
        s += '%s<%s:ExcAC5A.e1>%s</%s:ExcAC5A.e1>' % \
            (indent, ns_prefix, self.e1, ns_prefix)
        s += '%s<%s:ExcAC5A.tf3>%s</%s:ExcAC5A.tf3>' % \
            (indent, ns_prefix, self.tf3, ns_prefix)
        s += '%s<%s:ExcAC5A.e2>%s</%s:ExcAC5A.e2>' % \
            (indent, ns_prefix, self.e2, ns_prefix)
        s += '%s<%s:ExcAC5A.se1>%s</%s:ExcAC5A.se1>' % \
            (indent, ns_prefix, self.se1, ns_prefix)
        s += '%s<%s:ExcAC5A.se2>%s</%s:ExcAC5A.se2>' % \
            (indent, ns_prefix, self.se2, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcAC5A")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_ac5_a.serialize


class ExcST5B(ExcitationSystem):
    """ IEEE (2005) ST5B Model  The Type ST5B excitation system is a variation of the Type ST1A model, with alternative overexcitation and underexcitation inputs and additional limits. The corresponding stabilizer models that can be used with these models are the Type PSS2B, PSS3B, or PSS4B.IEEE (2005) ST5B Model  The Type ST5B excitation system is a variation of the Type ST1A model, with alternative overexcitation and underexcitation inputs and additional limits. The corresponding stabilizer models that can be used with these models are the Type PSS2B, PSS3B, or PSS4B.
    """
    # <<< exc_st5_b
    # @generated
    def __init__(self, toc2=0.0, toc1=0.0, tc1=0.0, vrmin=0.0, tc2=0.0, kc=0.0, tb2=0.0, tob1=0.0, vrmax=0.0, tob2=0.0, tb1=0.0, tub1=0.0, tub2=0.0, tuc1=0.0, tuc2=0.0, kr=0.0, tr=0.0, t1=0.0, **kw_args):
        """ Initialises a new 'ExcST5B' instance.
        """
        # OEL lead time constantOEL lead time constant 
        self.toc2 = toc2

        # OEL lead time constantOEL lead time constant 
        self.toc1 = toc1

        # Regulator lead time constantRegulator lead time constant 
        self.tc1 = tc1

        # Minimum regulator output (&lt; 0.)Minimum regulator output (&lt; 0.) 
        self.vrmin = vrmin

        # Regulator lead time constant.Regulator lead time constant. 
        self.tc2 = tc2

        # Rectifier regulation factor (&gt;= 0.)Rectifier regulation factor (&gt;= 0.) 
        self.kc = kc

        # Regulator lag time constant (&gt;= 0.)Regulator lag time constant (&gt;= 0.) 
        self.tb2 = tb2

        # OEL lag time constant (&gt;= 0.)OEL lag time constant (&gt;= 0.) 
        self.tob1 = tob1

        # Maximum regulator output (&gt; 0.)Maximum regulator output (&gt; 0.) 
        self.vrmax = vrmax

        # OEL lag time constant (&gt;= 0.)OEL lag time constant (&gt;= 0.) 
        self.tob2 = tob2

        # Regulator lag time constant (&gt;= 0.)Regulator lag time constant (&gt;= 0.) 
        self.tb1 = tb1

        # UEL lag time constant (&gt;= 0.)UEL lag time constant (&gt;= 0.) 
        self.tub1 = tub1

        # UEL lag time constant (&gt;= 0.)UEL lag time constant (&gt;= 0.) 
        self.tub2 = tub2

        # UEL lead time constant.UEL lead time constant. 
        self.tuc1 = tuc1

        # UEL lead time constantUEL lead time constant 
        self.tuc2 = tuc2

        # Regulator gain (&gt; 0.)Regulator gain (&gt; 0.) 
        self.kr = kr

        # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Firing circuit time constant (&gt;= 0.)Firing circuit time constant (&gt;= 0.) 
        self.t1 = t1



        super(ExcST5B, self).__init__(**kw_args)
    # >>> exc_st5_b


    def __str__(self):
        """ Returns a string representation of the ExcST5B.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_st5_b.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcST5B.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcST5B", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ExcST5B.toc2>%s</%s:ExcST5B.toc2>' % \
            (indent, ns_prefix, self.toc2, ns_prefix)
        s += '%s<%s:ExcST5B.toc1>%s</%s:ExcST5B.toc1>' % \
            (indent, ns_prefix, self.toc1, ns_prefix)
        s += '%s<%s:ExcST5B.tc1>%s</%s:ExcST5B.tc1>' % \
            (indent, ns_prefix, self.tc1, ns_prefix)
        s += '%s<%s:ExcST5B.vrmin>%s</%s:ExcST5B.vrmin>' % \
            (indent, ns_prefix, self.vrmin, ns_prefix)
        s += '%s<%s:ExcST5B.tc2>%s</%s:ExcST5B.tc2>' % \
            (indent, ns_prefix, self.tc2, ns_prefix)
        s += '%s<%s:ExcST5B.kc>%s</%s:ExcST5B.kc>' % \
            (indent, ns_prefix, self.kc, ns_prefix)
        s += '%s<%s:ExcST5B.tb2>%s</%s:ExcST5B.tb2>' % \
            (indent, ns_prefix, self.tb2, ns_prefix)
        s += '%s<%s:ExcST5B.tob1>%s</%s:ExcST5B.tob1>' % \
            (indent, ns_prefix, self.tob1, ns_prefix)
        s += '%s<%s:ExcST5B.vrmax>%s</%s:ExcST5B.vrmax>' % \
            (indent, ns_prefix, self.vrmax, ns_prefix)
        s += '%s<%s:ExcST5B.tob2>%s</%s:ExcST5B.tob2>' % \
            (indent, ns_prefix, self.tob2, ns_prefix)
        s += '%s<%s:ExcST5B.tb1>%s</%s:ExcST5B.tb1>' % \
            (indent, ns_prefix, self.tb1, ns_prefix)
        s += '%s<%s:ExcST5B.tub1>%s</%s:ExcST5B.tub1>' % \
            (indent, ns_prefix, self.tub1, ns_prefix)
        s += '%s<%s:ExcST5B.tub2>%s</%s:ExcST5B.tub2>' % \
            (indent, ns_prefix, self.tub2, ns_prefix)
        s += '%s<%s:ExcST5B.tuc1>%s</%s:ExcST5B.tuc1>' % \
            (indent, ns_prefix, self.tuc1, ns_prefix)
        s += '%s<%s:ExcST5B.tuc2>%s</%s:ExcST5B.tuc2>' % \
            (indent, ns_prefix, self.tuc2, ns_prefix)
        s += '%s<%s:ExcST5B.kr>%s</%s:ExcST5B.kr>' % \
            (indent, ns_prefix, self.kr, ns_prefix)
        s += '%s<%s:ExcST5B.tr>%s</%s:ExcST5B.tr>' % \
            (indent, ns_prefix, self.tr, ns_prefix)
        s += '%s<%s:ExcST5B.t1>%s</%s:ExcST5B.t1>' % \
            (indent, ns_prefix, self.t1, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcST5B")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_st5_b.serialize


class ExcSCRX(ExcitationSystem):
    """ Simple excitation system model representing generic characteristics of many excitation systems; intended for use where negative field current may be a problemSimple excitation system model representing generic characteristics of many excitation systems; intended for use where negative field current may be a problem
    """
    # <<< exc_scrx
    # @generated
    def __init__(self, te=0.0, tb=0.0, emax=0.0, cswitch=False, rcrfd=0.0, tatb=0.0, k=0.0, emin=0.0, **kw_args):
        """ Initialises a new 'ExcSCRX' instance.
        """
        # Time constant of gain block (&gt; 0.)Time constant of gain block (&gt; 0.) 
        self.te = te

        # Denominator time constant of lag-lead blockDenominator time constant of lag-lead block 
        self.tb = tb

        # Maximum field voltage outputMaximum field voltage output 
        self.emax = emax

        # Power source switch:     1 ? fixed voltage     0 ? generator terminal voltagePower source switch:     1 ? fixed voltage     0 ? generator terminal voltage 
        self.cswitch = cswitch

        # Rc/Rfd - ratio of field discharge resistance to field winding resistanceRc/Rfd - ratio of field discharge resistance to field winding resistance 
        self.rcrfd = rcrfd

        # Ta/Tb - gain reduction ratio of lag-lead elementTa/Tb - gain reduction ratio of lag-lead element 
        self.tatb = tatb

        # Gain (&gt; 0.)Gain (&gt; 0.) 
        self.k = k

        # Minimum field voltage outputMinimum field voltage output 
        self.emin = emin



        super(ExcSCRX, self).__init__(**kw_args)
    # >>> exc_scrx


    def __str__(self):
        """ Returns a string representation of the ExcSCRX.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_scrx.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcSCRX.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcSCRX", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ExcSCRX.te>%s</%s:ExcSCRX.te>' % \
            (indent, ns_prefix, self.te, ns_prefix)
        s += '%s<%s:ExcSCRX.tb>%s</%s:ExcSCRX.tb>' % \
            (indent, ns_prefix, self.tb, ns_prefix)
        s += '%s<%s:ExcSCRX.emax>%s</%s:ExcSCRX.emax>' % \
            (indent, ns_prefix, self.emax, ns_prefix)
        s += '%s<%s:ExcSCRX.cswitch>%s</%s:ExcSCRX.cswitch>' % \
            (indent, ns_prefix, self.cswitch, ns_prefix)
        s += '%s<%s:ExcSCRX.rcrfd>%s</%s:ExcSCRX.rcrfd>' % \
            (indent, ns_prefix, self.rcrfd, ns_prefix)
        s += '%s<%s:ExcSCRX.tatb>%s</%s:ExcSCRX.tatb>' % \
            (indent, ns_prefix, self.tatb, ns_prefix)
        s += '%s<%s:ExcSCRX.k>%s</%s:ExcSCRX.k>' % \
            (indent, ns_prefix, self.k, ns_prefix)
        s += '%s<%s:ExcSCRX.emin>%s</%s:ExcSCRX.emin>' % \
            (indent, ns_prefix, self.emin, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcSCRX")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_scrx.serialize


class ExcAC8B(ExcitationSystem):
    """ IEEE (2005) AC8B Model  The AVR in this model consists of PID control, with separate constants for the proportional (<i>KPR</i>), integral (<i>KIR</i>), and derivative (<i>KDR</i>) gains. The representation of the brushless exciter (<i>TE</i>, <i>KE</i>, <i>SE</i>, <i>KC</i>, <i>KD</i>) is similar to the model Type AC2A. The Type AC8B model can be used to represent static voltage regulators applied to brushless excitation systems. Digitally based voltage regulators feeding dc rotating main exciters can be represented with the AC Type AC8B model with the parameters <i>KC </i>and <i>KD </i>set to 0. For thyristor power stages fed from the generator terminals, the limits <i>VRMAX </i>and <i>VRMIN </i>should be a function of terminal voltage: <i>VT </i>x <i>VRMAX </i>and <i>VT </i>x <i>VRMIN</i>.IEEE (2005) AC8B Model  The AVR in this model consists of PID control, with separate constants for the proportional (<i>KPR</i>), integral (<i>KIR</i>), and derivative (<i>KDR</i>) gains. The representation of the brushless exciter (<i>TE</i>, <i>KE</i>, <i>SE</i>, <i>KC</i>, <i>KD</i>) is similar to the model Type AC2A. The Type AC8B model can be used to represent static voltage regulators applied to brushless excitation systems. Digitally based voltage regulators feeding dc rotating main exciters can be represented with the AC Type AC8B model with the parameters <i>KC </i>and <i>KD </i>set to 0. For thyristor power stages fed from the generator terminals, the limits <i>VRMAX </i>and <i>VRMIN </i>should be a function of terminal voltage: <i>VT </i>x <i>VRMAX </i>and <i>VT </i>x <i>VRMIN</i>.
    """
    # <<< exc_ac8_b
    # @generated
    def __init__(self, kdr=0.0, tr=0.0, e1=0.0, e2=0.0, kir=0.0, kc=0.0, vrmax=0.0, ka=0.0, se2=0.0, tdr=0.0, kpr=0.0, vemin=0.0, kd=0.0, te=0.0, se1=0.0, ke=0.0, vfemax=0.0, ta=0.0, vrmin=0.0, vtmult=0.0, **kw_args):
        """ Initialises a new 'ExcAC8B' instance.
        """
        # Voltage Regulator Derivative Gain (&gt;= 0.)Voltage Regulator Derivative Gain (&gt;= 0.) 
        self.kdr = kdr

        # Voltage transducer time constant (&gt;= 0.)Voltage transducer time constant (&gt;= 0.) 
        self.tr = tr

        # Field voltage value 1     (&gt; 0.)Field voltage value 1     (&gt; 0.) 
        self.e1 = e1

        # Field voltage value 2.    (&gt; 0.)Field voltage value 2.    (&gt; 0.) 
        self.e2 = e2

        # Voltage Regulator Integral Gain (&gt;= 0.)Voltage Regulator Integral Gain (&gt;= 0.) 
        self.kir = kir

        # Rectifier regulation factor (&gt;= 0.)Rectifier regulation factor (&gt;= 0.) 
        self.kc = kc

        # Maximum controller output (&gt; 0.)Maximum controller output (&gt; 0.) 
        self.vrmax = vrmax

        # Amplifier gain (&gt; 0.)Amplifier gain (&gt; 0.) 
        self.ka = ka

        # Saturation factor at e2  (&gt;= 0.)Saturation factor at e2  (&gt;= 0.) 
        self.se2 = se2

        # Voltage Regulator Derivative Time Constant (&gt; 0. if kdr &gt; 0.)Voltage Regulator Derivative Time Constant (&gt; 0. if kdr &gt; 0.) 
        self.tdr = tdr

        # Voltage Regulator Proportional Gain (&gt; 0. if kir = 0.)Voltage Regulator Proportional Gain (&gt; 0. if kir = 0.) 
        self.kpr = kpr

        # Minimum exciter ouput voltage (&lt;= 0.)Minimum exciter ouput voltage (&lt;= 0.) 
        self.vemin = vemin

        # Exciter regulation factor (&gt;= 0.)Exciter regulation factor (&gt;= 0.) 
        self.kd = kd

        # Exciter field time constant (&gt; 0.)Exciter field time constant (&gt; 0.) 
        self.te = te

        # Saturation factor at e1 (&gt;= 0.)Saturation factor at e1 (&gt;= 0.) 
        self.se1 = se1

        # Exciter field proportional constantExciter field proportional constant 
        self.ke = ke

        # Exciter field current limit parameterExciter field current limit parameter 
        self.vfemax = vfemax

        # Amplifier time constant  (&gt;= 0.)Amplifier time constant  (&gt;= 0.) 
        self.ta = ta

        # Minimum controller output (&lt;= 0.)Minimum controller output (&lt;= 0.) 
        self.vrmin = vrmin

        # if not 0, multiply vrmax and vrmin by terminal voltageif not 0, multiply vrmax and vrmin by terminal voltage 
        self.vtmult = vtmult



        super(ExcAC8B, self).__init__(**kw_args)
    # >>> exc_ac8_b


    def __str__(self):
        """ Returns a string representation of the ExcAC8B.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_ac8_b.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcAC8B.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcAC8B", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ExcAC8B.kdr>%s</%s:ExcAC8B.kdr>' % \
            (indent, ns_prefix, self.kdr, ns_prefix)
        s += '%s<%s:ExcAC8B.tr>%s</%s:ExcAC8B.tr>' % \
            (indent, ns_prefix, self.tr, ns_prefix)
        s += '%s<%s:ExcAC8B.e1>%s</%s:ExcAC8B.e1>' % \
            (indent, ns_prefix, self.e1, ns_prefix)
        s += '%s<%s:ExcAC8B.e2>%s</%s:ExcAC8B.e2>' % \
            (indent, ns_prefix, self.e2, ns_prefix)
        s += '%s<%s:ExcAC8B.kir>%s</%s:ExcAC8B.kir>' % \
            (indent, ns_prefix, self.kir, ns_prefix)
        s += '%s<%s:ExcAC8B.kc>%s</%s:ExcAC8B.kc>' % \
            (indent, ns_prefix, self.kc, ns_prefix)
        s += '%s<%s:ExcAC8B.vrmax>%s</%s:ExcAC8B.vrmax>' % \
            (indent, ns_prefix, self.vrmax, ns_prefix)
        s += '%s<%s:ExcAC8B.ka>%s</%s:ExcAC8B.ka>' % \
            (indent, ns_prefix, self.ka, ns_prefix)
        s += '%s<%s:ExcAC8B.se2>%s</%s:ExcAC8B.se2>' % \
            (indent, ns_prefix, self.se2, ns_prefix)
        s += '%s<%s:ExcAC8B.tdr>%s</%s:ExcAC8B.tdr>' % \
            (indent, ns_prefix, self.tdr, ns_prefix)
        s += '%s<%s:ExcAC8B.kpr>%s</%s:ExcAC8B.kpr>' % \
            (indent, ns_prefix, self.kpr, ns_prefix)
        s += '%s<%s:ExcAC8B.vemin>%s</%s:ExcAC8B.vemin>' % \
            (indent, ns_prefix, self.vemin, ns_prefix)
        s += '%s<%s:ExcAC8B.kd>%s</%s:ExcAC8B.kd>' % \
            (indent, ns_prefix, self.kd, ns_prefix)
        s += '%s<%s:ExcAC8B.te>%s</%s:ExcAC8B.te>' % \
            (indent, ns_prefix, self.te, ns_prefix)
        s += '%s<%s:ExcAC8B.se1>%s</%s:ExcAC8B.se1>' % \
            (indent, ns_prefix, self.se1, ns_prefix)
        s += '%s<%s:ExcAC8B.ke>%s</%s:ExcAC8B.ke>' % \
            (indent, ns_prefix, self.ke, ns_prefix)
        s += '%s<%s:ExcAC8B.vfemax>%s</%s:ExcAC8B.vfemax>' % \
            (indent, ns_prefix, self.vfemax, ns_prefix)
        s += '%s<%s:ExcAC8B.ta>%s</%s:ExcAC8B.ta>' % \
            (indent, ns_prefix, self.ta, ns_prefix)
        s += '%s<%s:ExcAC8B.vrmin>%s</%s:ExcAC8B.vrmin>' % \
            (indent, ns_prefix, self.vrmin, ns_prefix)
        s += '%s<%s:ExcAC8B.vtmult>%s</%s:ExcAC8B.vtmult>' % \
            (indent, ns_prefix, self.vtmult, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcAC8B")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_ac8_b.serialize


class ExcWT2E(ExcitationSystem):
    """ Type 2 standard wind turbine field resistance control modelType 2 standard wind turbine field resistance control model
    """
    pass
    # <<< exc_wt2_e
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ExcWT2E' instance.
        """


        super(ExcWT2E, self).__init__(**kw_args)
    # >>> exc_wt2_e


    def __str__(self):
        """ Returns a string representation of the ExcWT2E.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_wt2_e.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcWT2E.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcWT2E", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcWT2E")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_wt2_e.serialize


class ExcAC7B(ExcitationSystem):
    """ IEEE (2005) AC7B Model  These excitation systems consist of an ac alternator with either stationary or rotating rectifiers to produce the dc field requirements. Upgrades to earlier ac excitation systems, which replace only the controls but retain the ac alternator and diode rectifier bridge, have resulted in this new model. Some of the features of this excitation system include a high bandwidth inner loop regulating generator field voltage or exciter current (<i>KF</i>2, <i>KF</i>1), a fast exciter current limit, <i>VFEMAX</i>, to protect the field of the ac alternator, and the PID generator voltage regulator (AVR). An alternative rate feedback loop (<i>KF</i>, <i>TF</i>) is provided for stabilization if the AVR does not include a derivative term. If a PSS control is supplied, the Type PSS2B or PSS3B models are appropriate.IEEE (2005) AC7B Model  These excitation systems consist of an ac alternator with either stationary or rotating rectifiers to produce the dc field requirements. Upgrades to earlier ac excitation systems, which replace only the controls but retain the ac alternator and diode rectifier bridge, have resulted in this new model. Some of the features of this excitation system include a high bandwidth inner loop regulating generator field voltage or exciter current (<i>KF</i>2, <i>KF</i>1), a fast exciter current limit, <i>VFEMAX</i>, to protect the field of the ac alternator, and the PID generator voltage regulator (AVR). An alternative rate feedback loop (<i>KF</i>, <i>TF</i>) is provided for stabilization if the AVR does not include a derivative term. If a PSS control is supplied, the Type PSS2B or PSS3B models are appropriate.
    """
    # <<< exc_ac7_b
    # @generated
    def __init__(self, kd=0.0, kc=0.0, vrmin=0.0, kdr=0.0, vrmax=0.0, kpr=0.0, vemin=0.0, kl=0.0, kf1=0.0, kia=0.0, kf3=0.0, se1=0.0, vfemax=0.0, kf2=0.0, te=0.0, tf=0.0, ke=0.0, kpa=0.0, e2=0.0, se2=0.0, kp=0.0, e1=0.0, kir=0.0, tr=0.0, tdr=0.0, vamin=0.0, vamax=0.0, **kw_args):
        """ Initialises a new 'ExcAC7B' instance.
        """
        # Exciter internal reactance (&gt;= 0.)Exciter internal reactance (&gt;= 0.) 
        self.kd = kd

        # Rectifier regulation factor (&gt;= 0.)Rectifier regulation factor (&gt;= 0.) 
        self.kc = kc

        # Minimum regulator output (&lt; 0.)Minimum regulator output (&lt; 0.) 
        self.vrmin = vrmin

        # Regulator derivative gain (&gt;= 0.)Regulator derivative gain (&gt;= 0.) 
        self.kdr = kdr

        # Maximum regulator output (&gt; 0.)Maximum regulator output (&gt; 0.) 
        self.vrmax = vrmax

        # Regulator proportional gain (&gt; 0. if kir = 0.)Regulator proportional gain (&gt; 0. if kir = 0.) 
        self.kpr = kpr

        # Minimum exciter ouput voltage (&lt;= 0.)Minimum exciter ouput voltage (&lt;= 0.) 
        self.vemin = vemin

        # Exciter field voltage lower limit parameterExciter field voltage lower limit parameter 
        self.kl = kl

        # Field voltage feedback gain (&gt;= 0.)Field voltage feedback gain (&gt;= 0.) 
        self.kf1 = kf1

        # Amplifier integral gain (&gt;= 0.)Amplifier integral gain (&gt;= 0.) 
        self.kia = kia

        # Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.) 
        self.kf3 = kf3

        # Saturation factor at e1  (&gt;= 0.)Saturation factor at e1  (&gt;= 0.) 
        self.se1 = se1

        # Exciter field current limit parameterExciter field current limit parameter 
        self.vfemax = vfemax

        # Exciter field current feedback gain (&gt;= 0.)Exciter field current feedback gain (&gt;= 0.) 
        self.kf2 = kf2

        # Exciter time constant, sec. (&gt; 0.)Exciter time constant, sec. (&gt; 0.) 
        self.te = te

        # Rate feedback time constant (&gt; 0.)Rate feedback time constant (&gt; 0.) 
        self.tf = tf

        # Exciter field resistance constantExciter field resistance constant 
        self.ke = ke

        # Amplifier proportional gain (&gt; 0. if kia = 0.)Amplifier proportional gain (&gt; 0. if kia = 0.) 
        self.kpa = kpa

        # Field voltage value 2.    (&gt; 0.)Field voltage value 2.    (&gt; 0.) 
        self.e2 = e2

        # Saturation factor at e2   (&gt;= 0.)Saturation factor at e2   (&gt;= 0.) 
        self.se2 = se2

        # Exciter field voltage source gain (&gt; 0.)Exciter field voltage source gain (&gt; 0.) 
        self.kp = kp

        # Field voltage value 1   (&gt; 0.)Field voltage value 1   (&gt; 0.) 
        self.e1 = e1

        # Regulator integral gain (&gt;= 0.)Regulator integral gain (&gt;= 0.) 
        self.kir = kir

        # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Derivative gain washout time constant (&gt;= 0.)Derivative gain washout time constant (&gt;= 0.) 
        self.tdr = tdr

        # Minimum amplifier output (&lt; 0.)Minimum amplifier output (&lt; 0.) 
        self.vamin = vamin

        # Maximum amplifier output (&gt; 0.)Maximum amplifier output (&gt; 0.) 
        self.vamax = vamax



        super(ExcAC7B, self).__init__(**kw_args)
    # >>> exc_ac7_b


    def __str__(self):
        """ Returns a string representation of the ExcAC7B.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_ac7_b.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcAC7B.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcAC7B", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ExcAC7B.kd>%s</%s:ExcAC7B.kd>' % \
            (indent, ns_prefix, self.kd, ns_prefix)
        s += '%s<%s:ExcAC7B.kc>%s</%s:ExcAC7B.kc>' % \
            (indent, ns_prefix, self.kc, ns_prefix)
        s += '%s<%s:ExcAC7B.vrmin>%s</%s:ExcAC7B.vrmin>' % \
            (indent, ns_prefix, self.vrmin, ns_prefix)
        s += '%s<%s:ExcAC7B.kdr>%s</%s:ExcAC7B.kdr>' % \
            (indent, ns_prefix, self.kdr, ns_prefix)
        s += '%s<%s:ExcAC7B.vrmax>%s</%s:ExcAC7B.vrmax>' % \
            (indent, ns_prefix, self.vrmax, ns_prefix)
        s += '%s<%s:ExcAC7B.kpr>%s</%s:ExcAC7B.kpr>' % \
            (indent, ns_prefix, self.kpr, ns_prefix)
        s += '%s<%s:ExcAC7B.vemin>%s</%s:ExcAC7B.vemin>' % \
            (indent, ns_prefix, self.vemin, ns_prefix)
        s += '%s<%s:ExcAC7B.kl>%s</%s:ExcAC7B.kl>' % \
            (indent, ns_prefix, self.kl, ns_prefix)
        s += '%s<%s:ExcAC7B.kf1>%s</%s:ExcAC7B.kf1>' % \
            (indent, ns_prefix, self.kf1, ns_prefix)
        s += '%s<%s:ExcAC7B.kia>%s</%s:ExcAC7B.kia>' % \
            (indent, ns_prefix, self.kia, ns_prefix)
        s += '%s<%s:ExcAC7B.kf3>%s</%s:ExcAC7B.kf3>' % \
            (indent, ns_prefix, self.kf3, ns_prefix)
        s += '%s<%s:ExcAC7B.se1>%s</%s:ExcAC7B.se1>' % \
            (indent, ns_prefix, self.se1, ns_prefix)
        s += '%s<%s:ExcAC7B.vfemax>%s</%s:ExcAC7B.vfemax>' % \
            (indent, ns_prefix, self.vfemax, ns_prefix)
        s += '%s<%s:ExcAC7B.kf2>%s</%s:ExcAC7B.kf2>' % \
            (indent, ns_prefix, self.kf2, ns_prefix)
        s += '%s<%s:ExcAC7B.te>%s</%s:ExcAC7B.te>' % \
            (indent, ns_prefix, self.te, ns_prefix)
        s += '%s<%s:ExcAC7B.tf>%s</%s:ExcAC7B.tf>' % \
            (indent, ns_prefix, self.tf, ns_prefix)
        s += '%s<%s:ExcAC7B.ke>%s</%s:ExcAC7B.ke>' % \
            (indent, ns_prefix, self.ke, ns_prefix)
        s += '%s<%s:ExcAC7B.kpa>%s</%s:ExcAC7B.kpa>' % \
            (indent, ns_prefix, self.kpa, ns_prefix)
        s += '%s<%s:ExcAC7B.e2>%s</%s:ExcAC7B.e2>' % \
            (indent, ns_prefix, self.e2, ns_prefix)
        s += '%s<%s:ExcAC7B.se2>%s</%s:ExcAC7B.se2>' % \
            (indent, ns_prefix, self.se2, ns_prefix)
        s += '%s<%s:ExcAC7B.kp>%s</%s:ExcAC7B.kp>' % \
            (indent, ns_prefix, self.kp, ns_prefix)
        s += '%s<%s:ExcAC7B.e1>%s</%s:ExcAC7B.e1>' % \
            (indent, ns_prefix, self.e1, ns_prefix)
        s += '%s<%s:ExcAC7B.kir>%s</%s:ExcAC7B.kir>' % \
            (indent, ns_prefix, self.kir, ns_prefix)
        s += '%s<%s:ExcAC7B.tr>%s</%s:ExcAC7B.tr>' % \
            (indent, ns_prefix, self.tr, ns_prefix)
        s += '%s<%s:ExcAC7B.tdr>%s</%s:ExcAC7B.tdr>' % \
            (indent, ns_prefix, self.tdr, ns_prefix)
        s += '%s<%s:ExcAC7B.vamin>%s</%s:ExcAC7B.vamin>' % \
            (indent, ns_prefix, self.vamin, ns_prefix)
        s += '%s<%s:ExcAC7B.vamax>%s</%s:ExcAC7B.vamax>' % \
            (indent, ns_prefix, self.vamax, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcAC7B")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_ac7_b.serialize


class ExcWT4E(ExcitationSystem):
    """ Type 4 standard wind turbine convertor control modelType 4 standard wind turbine convertor control model
    """
    pass
    # <<< exc_wt4_e
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ExcWT4E' instance.
        """


        super(ExcWT4E, self).__init__(**kw_args)
    # >>> exc_wt4_e


    def __str__(self):
        """ Returns a string representation of the ExcWT4E.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_wt4_e.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcWT4E.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcWT4E", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcWT4E")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_wt4_e.serialize


class ExcST1A(ExcitationSystem):
    """ IEEE (1992/2005) ST1A Model  The computer model of the Type ST1A potential-source controlled-rectifier excitation system represents systems in which excitation power is supplied through a transformer from the generator terminals (or the unit's auxiliary bus) and is regulated by a controlled rectifier. The maximum exciter voltage available from such systems is directly related to the generator terminal voltage.IEEE (1992/2005) ST1A Model  The computer model of the Type ST1A potential-source controlled-rectifier excitation system represents systems in which excitation power is supplied through a transformer from the generator terminals (or the unit's auxiliary bus) and is regulated by a controlled rectifier. The maximum exciter voltage available from such systems is directly related to the generator terminal voltage.
    """
    # <<< exc_st1_a
    # @generated
    def __init__(self, vrmin=0.0, kc=0.0, vimin=0.0, uelin=0.0, tf=0.0, kf=0.0, tc1=0.0, pssin=0.0, tc=0.0, tb=0.0, ka=0.0, ta=0.0, tr=0.0, ilr=0.0, vamin=0.0, klr=0.0, tb1=0.0, vamax=0.0, vrmax=0.0, vimax=0.0, **kw_args):
        """ Initialises a new 'ExcST1A' instance.
        """
        # Excitation voltage lower limit (&lt; 0.)Excitation voltage lower limit (&lt; 0.) 
        self.vrmin = vrmin

        # Excitation system regulation factor (&gt;= 0.)Excitation system regulation factor (&gt;= 0.) 
        self.kc = kc

        # Minimum error (&lt; 0.)Minimum error (&lt; 0.) 
        self.vimin = vimin

        # = 2 ? UEL input added to error signal = 1 ? UEL input HV gate with error signal = -1 ? UEL input HV gate with volt. reg. output = 0 ? ignore UEL signal= 2 ? UEL input added to error signal = 1 ? UEL input HV gate with error signal = -1 ? UEL input HV gate with volt. reg. output = 0 ? ignore UEL signal 
        self.uelin = uelin

        # Rate feedback time constant (&gt;= 0.)Rate feedback time constant (&gt;= 0.) 
        self.tf = tf

        # Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.) 
        self.kf = kf

        # Lead time constantLead time constant 
        self.tc1 = tc1

        # = 0 ? PSS input (Vs) added to error signal not 0 ? PSS input (Vs) added to voltage regulator output= 0 ? PSS input (Vs) added to error signal not 0 ? PSS input (Vs) added to voltage regulator output 
        self.pssin = pssin

        # Lead time constantLead time constant 
        self.tc = tc

        # Lag time constant (&gt;= 0.)Lag time constant (&gt;= 0.) 
        self.tb = tb

        # Gain (&gt; 0.)Gain (&gt; 0.) 
        self.ka = ka

        # Time constant (&gt;= 0.)Time constant (&gt;= 0.) 
        self.ta = ta

        # Voltage transducer time constant (&gt;= 0.)Voltage transducer time constant (&gt;= 0.) 
        self.tr = tr

        # Maximum field currentMaximum field current 
        self.ilr = ilr

        # Minimum control element output (&lt; 0.)Minimum control element output (&lt; 0.) 
        self.vamin = vamin

        # Gain on field current limitGain on field current limit 
        self.klr = klr

        # Lag time constant (&gt;= 0.)Lag time constant (&gt;= 0.) 
        self.tb1 = tb1

        # Maximum control element output (&gt; 0.)Maximum control element output (&gt; 0.) 
        self.vamax = vamax

        # Excitation voltage upper limit (&gt; 0.)Excitation voltage upper limit (&gt; 0.) 
        self.vrmax = vrmax

        # Maximum error (&gt; 0.)Maximum error (&gt; 0.) 
        self.vimax = vimax



        super(ExcST1A, self).__init__(**kw_args)
    # >>> exc_st1_a


    def __str__(self):
        """ Returns a string representation of the ExcST1A.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_st1_a.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcST1A.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcST1A", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ExcST1A.vrmin>%s</%s:ExcST1A.vrmin>' % \
            (indent, ns_prefix, self.vrmin, ns_prefix)
        s += '%s<%s:ExcST1A.kc>%s</%s:ExcST1A.kc>' % \
            (indent, ns_prefix, self.kc, ns_prefix)
        s += '%s<%s:ExcST1A.vimin>%s</%s:ExcST1A.vimin>' % \
            (indent, ns_prefix, self.vimin, ns_prefix)
        s += '%s<%s:ExcST1A.uelin>%s</%s:ExcST1A.uelin>' % \
            (indent, ns_prefix, self.uelin, ns_prefix)
        s += '%s<%s:ExcST1A.tf>%s</%s:ExcST1A.tf>' % \
            (indent, ns_prefix, self.tf, ns_prefix)
        s += '%s<%s:ExcST1A.kf>%s</%s:ExcST1A.kf>' % \
            (indent, ns_prefix, self.kf, ns_prefix)
        s += '%s<%s:ExcST1A.tc1>%s</%s:ExcST1A.tc1>' % \
            (indent, ns_prefix, self.tc1, ns_prefix)
        s += '%s<%s:ExcST1A.pssin>%s</%s:ExcST1A.pssin>' % \
            (indent, ns_prefix, self.pssin, ns_prefix)
        s += '%s<%s:ExcST1A.tc>%s</%s:ExcST1A.tc>' % \
            (indent, ns_prefix, self.tc, ns_prefix)
        s += '%s<%s:ExcST1A.tb>%s</%s:ExcST1A.tb>' % \
            (indent, ns_prefix, self.tb, ns_prefix)
        s += '%s<%s:ExcST1A.ka>%s</%s:ExcST1A.ka>' % \
            (indent, ns_prefix, self.ka, ns_prefix)
        s += '%s<%s:ExcST1A.ta>%s</%s:ExcST1A.ta>' % \
            (indent, ns_prefix, self.ta, ns_prefix)
        s += '%s<%s:ExcST1A.tr>%s</%s:ExcST1A.tr>' % \
            (indent, ns_prefix, self.tr, ns_prefix)
        s += '%s<%s:ExcST1A.ilr>%s</%s:ExcST1A.ilr>' % \
            (indent, ns_prefix, self.ilr, ns_prefix)
        s += '%s<%s:ExcST1A.vamin>%s</%s:ExcST1A.vamin>' % \
            (indent, ns_prefix, self.vamin, ns_prefix)
        s += '%s<%s:ExcST1A.klr>%s</%s:ExcST1A.klr>' % \
            (indent, ns_prefix, self.klr, ns_prefix)
        s += '%s<%s:ExcST1A.tb1>%s</%s:ExcST1A.tb1>' % \
            (indent, ns_prefix, self.tb1, ns_prefix)
        s += '%s<%s:ExcST1A.vamax>%s</%s:ExcST1A.vamax>' % \
            (indent, ns_prefix, self.vamax, ns_prefix)
        s += '%s<%s:ExcST1A.vrmax>%s</%s:ExcST1A.vrmax>' % \
            (indent, ns_prefix, self.vrmax, ns_prefix)
        s += '%s<%s:ExcST1A.vimax>%s</%s:ExcST1A.vimax>' % \
            (indent, ns_prefix, self.vimax, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcST1A")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_st1_a.serialize


class ExcBBC(ExcitationSystem):
    """ Static Excitation System Model with ABB regulatorStatic Excitation System Model with ABB regulator
    """
    pass
    # <<< exc_bbc
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ExcBBC' instance.
        """


        super(ExcBBC, self).__init__(**kw_args)
    # >>> exc_bbc


    def __str__(self):
        """ Returns a string representation of the ExcBBC.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_bbc.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcBBC.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcBBC", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcBBC")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_bbc.serialize


class ExcDC3A(ExcitationSystem):
    """ IEEE (1992/2005) DC3A Model  The Type DC3A model is used to represent older systems, in particular those dc commutator exciters with non-continuously acting regulators that were commonly used before the development of the continuously acting varieties. These systems respond at basically two different rates, depending upon the magnitude of voltage error. For small errors, adjustment is made periodically with a signal to a motor-operated rheostat. Larger errors cause resistors to be quickly shorted or inserted and a strong forcing signal applied to the exciter. Continuous motion of the motor-operated rheostat occurs for these larger error signals, even though it is bypassed by contactor action.IEEE (1992/2005) DC3A Model  The Type DC3A model is used to represent older systems, in particular those dc commutator exciters with non-continuously acting regulators that were commonly used before the development of the continuously acting varieties. These systems respond at basically two different rates, depending upon the magnitude of voltage error. For small errors, adjustment is made periodically with a signal to a motor-operated rheostat. Larger errors cause resistors to be quickly shorted or inserted and a strong forcing signal applied to the exciter. Continuous motion of the motor-operated rheostat occurs for these larger error signals, even though it is bypassed by contactor action.
    """
    # <<< exc_dc3_a
    # @generated
    def __init__(self, vrmax=0.0, ke=0.0, te=0.0, exclim=0.0, se1=0.0, se2=0.0, trh=0.0, kv=0.0, e1=0.0, e2=0.0, vrmin=0.0, tr=0.0, **kw_args):
        """ Initialises a new 'ExcDC3A' instance.
        """
        # Maximum control element output (&gt; 0.)Maximum control element output (&gt; 0.) 
        self.vrmax = vrmax

        # Exciter field resistance line slopeExciter field resistance line slope 
        self.ke = ke

        # Exciter field time constant (&gt; 0.)Exciter field time constant (&gt; 0.) 
        self.te = te

        # If not 0, apply lower limit of 0. to exciter outputIf not 0, apply lower limit of 0. to exciter output 
        self.exclim = exclim

        # Saturation factor at e1 (&gt;= 0.)Saturation factor at e1 (&gt;= 0.) 
        self.se1 = se1

        # Saturation factor at e2  (&gt;= 0.)Saturation factor at e2  (&gt;= 0.) 
        self.se2 = se2

        # Rheostat full range travel time (&gt; 0.)Rheostat full range travel time (&gt; 0.) 
        self.trh = trh

        # Voltage error threshold min/max control action (&gt; 0.)Voltage error threshold min/max control action (&gt; 0.) 
        self.kv = kv

        # Field voltage value 1    (&gt; 0.)Field voltage value 1    (&gt; 0.) 
        self.e1 = e1

        # Field voltage value 2.     (&gt; 0.)Field voltage value 2.     (&gt; 0.) 
        self.e2 = e2

        # Minimum control element output (&lt;= 0.)Minimum control element output (&lt;= 0.) 
        self.vrmin = vrmin

        # Filter  time constant (&gt;= 0.)Filter  time constant (&gt;= 0.) 
        self.tr = tr



        super(ExcDC3A, self).__init__(**kw_args)
    # >>> exc_dc3_a


    def __str__(self):
        """ Returns a string representation of the ExcDC3A.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_dc3_a.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcDC3A.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcDC3A", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ExcDC3A.vrmax>%s</%s:ExcDC3A.vrmax>' % \
            (indent, ns_prefix, self.vrmax, ns_prefix)
        s += '%s<%s:ExcDC3A.ke>%s</%s:ExcDC3A.ke>' % \
            (indent, ns_prefix, self.ke, ns_prefix)
        s += '%s<%s:ExcDC3A.te>%s</%s:ExcDC3A.te>' % \
            (indent, ns_prefix, self.te, ns_prefix)
        s += '%s<%s:ExcDC3A.exclim>%s</%s:ExcDC3A.exclim>' % \
            (indent, ns_prefix, self.exclim, ns_prefix)
        s += '%s<%s:ExcDC3A.se1>%s</%s:ExcDC3A.se1>' % \
            (indent, ns_prefix, self.se1, ns_prefix)
        s += '%s<%s:ExcDC3A.se2>%s</%s:ExcDC3A.se2>' % \
            (indent, ns_prefix, self.se2, ns_prefix)
        s += '%s<%s:ExcDC3A.trh>%s</%s:ExcDC3A.trh>' % \
            (indent, ns_prefix, self.trh, ns_prefix)
        s += '%s<%s:ExcDC3A.kv>%s</%s:ExcDC3A.kv>' % \
            (indent, ns_prefix, self.kv, ns_prefix)
        s += '%s<%s:ExcDC3A.e1>%s</%s:ExcDC3A.e1>' % \
            (indent, ns_prefix, self.e1, ns_prefix)
        s += '%s<%s:ExcDC3A.e2>%s</%s:ExcDC3A.e2>' % \
            (indent, ns_prefix, self.e2, ns_prefix)
        s += '%s<%s:ExcDC3A.vrmin>%s</%s:ExcDC3A.vrmin>' % \
            (indent, ns_prefix, self.vrmin, ns_prefix)
        s += '%s<%s:ExcDC3A.tr>%s</%s:ExcDC3A.tr>' % \
            (indent, ns_prefix, self.tr, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcDC3A")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_dc3_a.serialize


class ExcST3A(ExcitationSystem):
    """ IEEE (1992/2005) ST3A Model  Some static systems utilize a field voltage control loop to linearize the exciter control characteristic. This also makes the output independent of supply source variations until supply limitations are reached. These systems utilize a variety of controlled-rectifier designs: full thyristor complements or hybrid bridges in either series or shunt configurations. The power source may consist of only a potential source, either fed from the machine terminals or from internal windings. Some designs may have compound power sources utilizing both machine potential and current. These power sources are represented as phasor combinations of machine terminal current and voltage and are accommodated by suitable parameters in the model Type ST3A.IEEE (1992/2005) ST3A Model  Some static systems utilize a field voltage control loop to linearize the exciter control characteristic. This also makes the output independent of supply source variations until supply limitations are reached. These systems utilize a variety of controlled-rectifier designs: full thyristor complements or hybrid bridges in either series or shunt configurations. The power source may consist of only a potential source, either fed from the machine terminals or from internal windings. Some designs may have compound power sources utilizing both machine potential and current. These power sources are represented as phasor combinations of machine terminal current and voltage and are accommodated by suitable parameters in the model Type ST3A.
    """
    # <<< exc_st3_a
    # @generated
    def __init__(self, vrmin=0.0, kc=0.0, ka=0.0, vbmax=0.0, vimin=0.0, xl=0.0, vgmax=0.0, angp=0.0, vmmin=0.0, vrmax=0.0, kp=0.0, km=0.0, vimax=0.0, tr=0.0, vmmax=0.0, ki=0.0, tm=0.0, ta=0.0, tb=0.0, kg=0.0, tc=0.0, **kw_args):
        """ Initialises a new 'ExcST3A' instance.
        """
        # Minimum AVR output (&lt; 0.)Minimum AVR output (&lt; 0.) 
        self.vrmin = vrmin

        # Exciter regulation factor (&gt;= 0.)Exciter regulation factor (&gt;= 0.) 
        self.kc = kc

        # AVR gain (&gt; 0.)AVR gain (&gt; 0.) 
        self.ka = ka

        # Maximum excitation voltage (&gt; 0.)Maximum excitation voltage (&gt; 0.) 
        self.vbmax = vbmax

        # Minimum error (&lt; 0.)Minimum error (&lt; 0.) 
        self.vimin = vimin

        # P-bar reactance (&gt;= 0.)P-bar reactance (&gt;= 0.) 
        self.xl = xl

        # Maximum inner loop feedback voltage (&gt;= 0.)Maximum inner loop feedback voltage (&gt;= 0.) 
        self.vgmax = vgmax

        # Phase angle of potential sourcePhase angle of potential source 
        self.angp = angp

        # Minimum inner loop output (&lt;= 0.)Minimum inner loop output (&lt;= 0.) 
        self.vmmin = vmmin

        # Maximum AVR output (&gt; 0.)Maximum AVR output (&gt; 0.) 
        self.vrmax = vrmax

        # Potential source gain (&gt; 0.)Potential source gain (&gt; 0.) 
        self.kp = kp

        # Inner loop forward gain (&gt; 0.)Inner loop forward gain (&gt; 0.) 
        self.km = km

        # Maximum error (&gt; 0.)Maximum error (&gt; 0.) 
        self.vimax = vimax

        # Voltage transducer time constant (&gt;= 0.)Voltage transducer time constant (&gt;= 0.) 
        self.tr = tr

        # Maximum inner loop output (&gt; 0.)Maximum inner loop output (&gt; 0.) 
        self.vmmax = vmmax

        # Current source gain (&gt;= 0.)Current source gain (&gt;= 0.) 
        self.ki = ki

        # Inner loop time constant (&gt; 0.)Inner loop time constant (&gt; 0.) 
        self.tm = tm

        # AVR time constant (&gt;= 0.)AVR time constant (&gt;= 0.) 
        self.ta = ta

        # AVR lag time constant (&gt;= 0.)AVR lag time constant (&gt;= 0.) 
        self.tb = tb

        # Inner loop feedback gain (&gt;= 0.)Inner loop feedback gain (&gt;= 0.) 
        self.kg = kg

        # AVR lead time constantAVR lead time constant 
        self.tc = tc



        super(ExcST3A, self).__init__(**kw_args)
    # >>> exc_st3_a


    def __str__(self):
        """ Returns a string representation of the ExcST3A.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_st3_a.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcST3A.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcST3A", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ExcST3A.vrmin>%s</%s:ExcST3A.vrmin>' % \
            (indent, ns_prefix, self.vrmin, ns_prefix)
        s += '%s<%s:ExcST3A.kc>%s</%s:ExcST3A.kc>' % \
            (indent, ns_prefix, self.kc, ns_prefix)
        s += '%s<%s:ExcST3A.ka>%s</%s:ExcST3A.ka>' % \
            (indent, ns_prefix, self.ka, ns_prefix)
        s += '%s<%s:ExcST3A.vbmax>%s</%s:ExcST3A.vbmax>' % \
            (indent, ns_prefix, self.vbmax, ns_prefix)
        s += '%s<%s:ExcST3A.vimin>%s</%s:ExcST3A.vimin>' % \
            (indent, ns_prefix, self.vimin, ns_prefix)
        s += '%s<%s:ExcST3A.xl>%s</%s:ExcST3A.xl>' % \
            (indent, ns_prefix, self.xl, ns_prefix)
        s += '%s<%s:ExcST3A.vgmax>%s</%s:ExcST3A.vgmax>' % \
            (indent, ns_prefix, self.vgmax, ns_prefix)
        s += '%s<%s:ExcST3A.angp>%s</%s:ExcST3A.angp>' % \
            (indent, ns_prefix, self.angp, ns_prefix)
        s += '%s<%s:ExcST3A.vmmin>%s</%s:ExcST3A.vmmin>' % \
            (indent, ns_prefix, self.vmmin, ns_prefix)
        s += '%s<%s:ExcST3A.vrmax>%s</%s:ExcST3A.vrmax>' % \
            (indent, ns_prefix, self.vrmax, ns_prefix)
        s += '%s<%s:ExcST3A.kp>%s</%s:ExcST3A.kp>' % \
            (indent, ns_prefix, self.kp, ns_prefix)
        s += '%s<%s:ExcST3A.km>%s</%s:ExcST3A.km>' % \
            (indent, ns_prefix, self.km, ns_prefix)
        s += '%s<%s:ExcST3A.vimax>%s</%s:ExcST3A.vimax>' % \
            (indent, ns_prefix, self.vimax, ns_prefix)
        s += '%s<%s:ExcST3A.tr>%s</%s:ExcST3A.tr>' % \
            (indent, ns_prefix, self.tr, ns_prefix)
        s += '%s<%s:ExcST3A.vmmax>%s</%s:ExcST3A.vmmax>' % \
            (indent, ns_prefix, self.vmmax, ns_prefix)
        s += '%s<%s:ExcST3A.ki>%s</%s:ExcST3A.ki>' % \
            (indent, ns_prefix, self.ki, ns_prefix)
        s += '%s<%s:ExcST3A.tm>%s</%s:ExcST3A.tm>' % \
            (indent, ns_prefix, self.tm, ns_prefix)
        s += '%s<%s:ExcST3A.ta>%s</%s:ExcST3A.ta>' % \
            (indent, ns_prefix, self.ta, ns_prefix)
        s += '%s<%s:ExcST3A.tb>%s</%s:ExcST3A.tb>' % \
            (indent, ns_prefix, self.tb, ns_prefix)
        s += '%s<%s:ExcST3A.kg>%s</%s:ExcST3A.kg>' % \
            (indent, ns_prefix, self.kg, ns_prefix)
        s += '%s<%s:ExcST3A.tc>%s</%s:ExcST3A.tc>' % \
            (indent, ns_prefix, self.tc, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcST3A")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_st3_a.serialize


class ExcCZ(ExcitationSystem):
    """ Czech proportional/integral excitation system model.Czech proportional/integral excitation system model.
    """
    pass
    # <<< exc_cz
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ExcCZ' instance.
        """


        super(ExcCZ, self).__init__(**kw_args)
    # >>> exc_cz


    def __str__(self):
        """ Returns a string representation of the ExcCZ.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< exc_cz.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcCZ.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcCZ", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcCZ")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> exc_cz.serialize


# <<< excitation_systems
# @generated
# >>> excitation_systems
