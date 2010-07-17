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

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_TurbineGovernors"

class TurbineGovernor(Element):
    """ The turbine-governor determines the mechanical power (Pm) supplied to the generator modelThe turbine-governor determines the mechanical power (Pm) supplied to the generator model
    """
    pass
    # <<< turbine_governor
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'TurbineGovernor' instance.
        """


        super(TurbineGovernor, self).__init__(**kw_args)
    # >>> turbine_governor


    def __str__(self):
        """ Returns a string representation of the TurbineGovernor.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< turbine_governor.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TurbineGovernor.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TurbineGovernor", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "TurbineGovernor")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> turbine_governor.serialize


class GovHydro3(TurbineGovernor):
    pass
    # <<< gov_hydro3
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovHydro3' instance.
        """


        super(GovHydro3, self).__init__(**kw_args)
    # >>> gov_hydro3


    def __str__(self):
        """ Returns a string representation of the GovHydro3.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_hydro3.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovHydro3.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovHydro3", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovHydro3")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_hydro3.serialize


class GovHydro2(TurbineGovernor):
    # <<< gov_hydro2
    # @generated
    def __init__(self, bturb=0.0, rtemp=0.0, tw=0.0, rperm=0.0, gv1=0.0, gv2=0.0, tr=0.0, aturb=0.0, tp=0.0, uo=0.0, gv6=0.0, gv5=0.0, pgv5=0.0, gv4=0.0, pgv6=0.0, gv3=0.0, pgv2=0.0, pgv1=0.0, db1=0.0, pgv4=0.0, kturb=0.0, db2=0.0, tg=0.0, pmax=0.0, pgv3=0.0, mwbase=0.0, uc=0.0, pmin=0.0, eps=0.0, **kw_args):
        """ Initialises a new 'GovHydro2' instance.
        """
        # Turbine denominator multiplierTurbine denominator multiplier 
        self.bturb = bturb

        # Temporary droopTemporary droop 
        self.rtemp = rtemp

        # Water inertia time constantWater inertia time constant 
        self.tw = tw

        # Permanent droopPermanent droop 
        self.rperm = rperm

        # Nonlinear gain point 1, p.u. gvNonlinear gain point 1, p.u. gv 
        self.gv1 = gv1

        # Nonlinear gain point 2, p.u. gvNonlinear gain point 2, p.u. gv 
        self.gv2 = gv2

        # Dashpot time constantDashpot time constant 
        self.tr = tr

        # Turbine numerator multiplierTurbine numerator multiplier 
        self.aturb = aturb

        # Pilot servo valve time constantPilot servo valve time constant 
        self.tp = tp

        # Maximum gate opening velocityMaximum gate opening velocity 
        self.uo = uo

        # Nonlinear gain point 6, p.u. gvNonlinear gain point 6, p.u. gv 
        self.gv6 = gv6

        # Nonlinear gain point 5, p.u. gvNonlinear gain point 5, p.u. gv 
        self.gv5 = gv5

        # Nonlinear gain point 5, p.u. powerNonlinear gain point 5, p.u. power 
        self.pgv5 = pgv5

        # Nonlinear gain point 4, p.u. gvNonlinear gain point 4, p.u. gv 
        self.gv4 = gv4

        # Nonlinear gain point 6, p.u. powerNonlinear gain point 6, p.u. power 
        self.pgv6 = pgv6

        # Nonlinear gain point 3, p.u. gvNonlinear gain point 3, p.u. gv 
        self.gv3 = gv3

        # Nonlinear gain point 2, p.u. powerNonlinear gain point 2, p.u. power 
        self.pgv2 = pgv2

        # Nonlinear gain point 1, p.u. powerNonlinear gain point 1, p.u. power 
        self.pgv1 = pgv1

        # Intentional deadband widthIntentional deadband width 
        self.db1 = db1

        # Nonlinear gain point 4, p.u. powerNonlinear gain point 4, p.u. power 
        self.pgv4 = pgv4

        # Turbine gainTurbine gain 
        self.kturb = kturb

        # Unintentional deadbandUnintentional deadband 
        self.db2 = db2

        # Gate servo time constantGate servo time constant 
        self.tg = tg

        # Maximum gate openingMaximum gate opening 
        self.pmax = pmax

        # Nonlinear gain point 3, p.u. powerNonlinear gain point 3, p.u. power 
        self.pgv3 = pgv3

        # Base for power values (&gt; 0.)Base for power values (&gt; 0.) 
        self.mwbase = mwbase

        # Maximum gate closing velocity (&lt;0.)Maximum gate closing velocity (&lt;0.) 
        self.uc = uc

        # Minimum gate openingMinimum gate opening 
        self.pmin = pmin

        # Intentional db hysteresisIntentional db hysteresis 
        self.eps = eps



        super(GovHydro2, self).__init__(**kw_args)
    # >>> gov_hydro2


    def __str__(self):
        """ Returns a string representation of the GovHydro2.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_hydro2.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovHydro2.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovHydro2", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:GovHydro2.bturb>%s</%s:GovHydro2.bturb>' % \
            (indent, ns_prefix, self.bturb, ns_prefix)
        s += '%s<%s:GovHydro2.rtemp>%s</%s:GovHydro2.rtemp>' % \
            (indent, ns_prefix, self.rtemp, ns_prefix)
        s += '%s<%s:GovHydro2.tw>%s</%s:GovHydro2.tw>' % \
            (indent, ns_prefix, self.tw, ns_prefix)
        s += '%s<%s:GovHydro2.rperm>%s</%s:GovHydro2.rperm>' % \
            (indent, ns_prefix, self.rperm, ns_prefix)
        s += '%s<%s:GovHydro2.gv1>%s</%s:GovHydro2.gv1>' % \
            (indent, ns_prefix, self.gv1, ns_prefix)
        s += '%s<%s:GovHydro2.gv2>%s</%s:GovHydro2.gv2>' % \
            (indent, ns_prefix, self.gv2, ns_prefix)
        s += '%s<%s:GovHydro2.tr>%s</%s:GovHydro2.tr>' % \
            (indent, ns_prefix, self.tr, ns_prefix)
        s += '%s<%s:GovHydro2.aturb>%s</%s:GovHydro2.aturb>' % \
            (indent, ns_prefix, self.aturb, ns_prefix)
        s += '%s<%s:GovHydro2.tp>%s</%s:GovHydro2.tp>' % \
            (indent, ns_prefix, self.tp, ns_prefix)
        s += '%s<%s:GovHydro2.uo>%s</%s:GovHydro2.uo>' % \
            (indent, ns_prefix, self.uo, ns_prefix)
        s += '%s<%s:GovHydro2.gv6>%s</%s:GovHydro2.gv6>' % \
            (indent, ns_prefix, self.gv6, ns_prefix)
        s += '%s<%s:GovHydro2.gv5>%s</%s:GovHydro2.gv5>' % \
            (indent, ns_prefix, self.gv5, ns_prefix)
        s += '%s<%s:GovHydro2.pgv5>%s</%s:GovHydro2.pgv5>' % \
            (indent, ns_prefix, self.pgv5, ns_prefix)
        s += '%s<%s:GovHydro2.gv4>%s</%s:GovHydro2.gv4>' % \
            (indent, ns_prefix, self.gv4, ns_prefix)
        s += '%s<%s:GovHydro2.pgv6>%s</%s:GovHydro2.pgv6>' % \
            (indent, ns_prefix, self.pgv6, ns_prefix)
        s += '%s<%s:GovHydro2.gv3>%s</%s:GovHydro2.gv3>' % \
            (indent, ns_prefix, self.gv3, ns_prefix)
        s += '%s<%s:GovHydro2.pgv2>%s</%s:GovHydro2.pgv2>' % \
            (indent, ns_prefix, self.pgv2, ns_prefix)
        s += '%s<%s:GovHydro2.pgv1>%s</%s:GovHydro2.pgv1>' % \
            (indent, ns_prefix, self.pgv1, ns_prefix)
        s += '%s<%s:GovHydro2.db1>%s</%s:GovHydro2.db1>' % \
            (indent, ns_prefix, self.db1, ns_prefix)
        s += '%s<%s:GovHydro2.pgv4>%s</%s:GovHydro2.pgv4>' % \
            (indent, ns_prefix, self.pgv4, ns_prefix)
        s += '%s<%s:GovHydro2.kturb>%s</%s:GovHydro2.kturb>' % \
            (indent, ns_prefix, self.kturb, ns_prefix)
        s += '%s<%s:GovHydro2.db2>%s</%s:GovHydro2.db2>' % \
            (indent, ns_prefix, self.db2, ns_prefix)
        s += '%s<%s:GovHydro2.tg>%s</%s:GovHydro2.tg>' % \
            (indent, ns_prefix, self.tg, ns_prefix)
        s += '%s<%s:GovHydro2.pmax>%s</%s:GovHydro2.pmax>' % \
            (indent, ns_prefix, self.pmax, ns_prefix)
        s += '%s<%s:GovHydro2.pgv3>%s</%s:GovHydro2.pgv3>' % \
            (indent, ns_prefix, self.pgv3, ns_prefix)
        s += '%s<%s:GovHydro2.mwbase>%s</%s:GovHydro2.mwbase>' % \
            (indent, ns_prefix, self.mwbase, ns_prefix)
        s += '%s<%s:GovHydro2.uc>%s</%s:GovHydro2.uc>' % \
            (indent, ns_prefix, self.uc, ns_prefix)
        s += '%s<%s:GovHydro2.pmin>%s</%s:GovHydro2.pmin>' % \
            (indent, ns_prefix, self.pmin, ns_prefix)
        s += '%s<%s:GovHydro2.eps>%s</%s:GovHydro2.eps>' % \
            (indent, ns_prefix, self.eps, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovHydro2")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_hydro2.serialize


class GovGAST(TurbineGovernor):
    pass
    # <<< gov_gast
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovGAST' instance.
        """


        super(GovGAST, self).__init__(**kw_args)
    # >>> gov_gast


    def __str__(self):
        """ Returns a string representation of the GovGAST.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_gast.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovGAST.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovGAST", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovGAST")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_gast.serialize


class GovWT1T(TurbineGovernor):
    pass
    # <<< gov_wt1_t
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovWT1T' instance.
        """


        super(GovWT1T, self).__init__(**kw_args)
    # >>> gov_wt1_t


    def __str__(self):
        """ Returns a string representation of the GovWT1T.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_wt1_t.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovWT1T.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovWT1T", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovWT1T")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_wt1_t.serialize


class GovWT2P(TurbineGovernor):
    pass
    # <<< gov_wt2_p
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovWT2P' instance.
        """


        super(GovWT2P, self).__init__(**kw_args)
    # >>> gov_wt2_p


    def __str__(self):
        """ Returns a string representation of the GovWT2P.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_wt2_p.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovWT2P.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovWT2P", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovWT2P")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_wt2_p.serialize


class GovHydroDD(TurbineGovernor):
    pass
    # <<< gov_hydro_dd
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovHydroDD' instance.
        """


        super(GovHydroDD, self).__init__(**kw_args)
    # >>> gov_hydro_dd


    def __str__(self):
        """ Returns a string representation of the GovHydroDD.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_hydro_dd.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovHydroDD.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovHydroDD", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovHydroDD")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_hydro_dd.serialize


class GovHydroWEH(TurbineGovernor):
    pass
    # <<< gov_hydro_weh
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovHydroWEH' instance.
        """


        super(GovHydroWEH, self).__init__(**kw_args)
    # >>> gov_hydro_weh


    def __str__(self):
        """ Returns a string representation of the GovHydroWEH.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_hydro_weh.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovHydroWEH.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovHydroWEH", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovHydroWEH")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_hydro_weh.serialize


class GovWT3T(TurbineGovernor):
    pass
    # <<< gov_wt3_t
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovWT3T' instance.
        """


        super(GovWT3T, self).__init__(**kw_args)
    # >>> gov_wt3_t


    def __str__(self):
        """ Returns a string representation of the GovWT3T.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_wt3_t.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovWT3T.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovWT3T", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovWT3T")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_wt3_t.serialize


class GovHydroPID(TurbineGovernor):
    pass
    # <<< gov_hydro_pid
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovHydroPID' instance.
        """


        super(GovHydroPID, self).__init__(**kw_args)
    # >>> gov_hydro_pid


    def __str__(self):
        """ Returns a string representation of the GovHydroPID.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_hydro_pid.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovHydroPID.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovHydroPID", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovHydroPID")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_hydro_pid.serialize


class GovHydro4(TurbineGovernor):
    pass
    # <<< gov_hydro4
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovHydro4' instance.
        """


        super(GovHydro4, self).__init__(**kw_args)
    # >>> gov_hydro4


    def __str__(self):
        """ Returns a string representation of the GovHydro4.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_hydro4.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovHydro4.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovHydro4", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovHydro4")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_hydro4.serialize


class GovDUM(TurbineGovernor):
    pass
    # <<< gov_dum
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovDUM' instance.
        """


        super(GovDUM, self).__init__(**kw_args)
    # >>> gov_dum


    def __str__(self):
        """ Returns a string representation of the GovDUM.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_dum.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovDUM.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovDUM", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovDUM")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_dum.serialize


class GovHydroWPID(TurbineGovernor):
    pass
    # <<< gov_hydro_wpid
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovHydroWPID' instance.
        """


        super(GovHydroWPID, self).__init__(**kw_args)
    # >>> gov_hydro_wpid


    def __str__(self):
        """ Returns a string representation of the GovHydroWPID.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_hydro_wpid.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovHydroWPID.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovHydroWPID", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovHydroWPID")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_hydro_wpid.serialize


class GovWT4P(TurbineGovernor):
    pass
    # <<< gov_wt4_p
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovWT4P' instance.
        """


        super(GovWT4P, self).__init__(**kw_args)
    # >>> gov_wt4_p


    def __str__(self):
        """ Returns a string representation of the GovWT4P.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_wt4_p.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovWT4P.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovWT4P", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovWT4P")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_wt4_p.serialize


class TLCFB1(TurbineGovernor):
    pass
    # <<< tlcfb1
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'TLCFB1' instance.
        """


        super(TLCFB1, self).__init__(**kw_args)
    # >>> tlcfb1


    def __str__(self):
        """ Returns a string representation of the TLCFB1.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< tlcfb1.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TLCFB1.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TLCFB1", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "TLCFB1")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> tlcfb1.serialize


class GovGASM(TurbineGovernor):
    pass
    # <<< gov_gasm
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovGASM' instance.
        """


        super(GovGASM, self).__init__(**kw_args)
    # >>> gov_gasm


    def __str__(self):
        """ Returns a string representation of the GovGASM.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_gasm.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovGASM.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovGASM", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovGASM")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_gasm.serialize


class GovHydroR(TurbineGovernor):
    pass
    # <<< gov_hydro_r
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovHydroR' instance.
        """


        super(GovHydroR, self).__init__(**kw_args)
    # >>> gov_hydro_r


    def __str__(self):
        """ Returns a string representation of the GovHydroR.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_hydro_r.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovHydroR.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovHydroR", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovHydroR")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_hydro_r.serialize


class GovSteamFV2(TurbineGovernor):
    pass
    # <<< gov_steam_fv2
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovSteamFV2' instance.
        """


        super(GovSteamFV2, self).__init__(**kw_args)
    # >>> gov_steam_fv2


    def __str__(self):
        """ Returns a string representation of the GovSteamFV2.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_steam_fv2.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovSteamFV2.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovSteamFV2", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovSteamFV2")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_steam_fv2.serialize


class GovRAV(TurbineGovernor):
    pass
    # <<< gov_rav
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovRAV' instance.
        """


        super(GovRAV, self).__init__(**kw_args)
    # >>> gov_rav


    def __str__(self):
        """ Returns a string representation of the GovRAV.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_rav.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovRAV.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovRAV", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovRAV")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_rav.serialize


class GovCT2(TurbineGovernor):
    pass
    # <<< gov_ct2
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovCT2' instance.
        """


        super(GovCT2, self).__init__(**kw_args)
    # >>> gov_ct2


    def __str__(self):
        """ Returns a string representation of the GovCT2.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_ct2.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovCT2.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovCT2", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovCT2")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_ct2.serialize


class GovSteam1(TurbineGovernor):
    """ IEEE steam turbine/governor model  (with optional deadband and nonlinear valve gain added)IEEE steam turbine/governor model  (with optional deadband and nonlinear valve gain added)
    """
    # <<< gov_steam1
    # @generated
    def __init__(self, eps=0.0, uc=0.0, mwbase=0.0, pmin=0.0, k3=0.0, k=0.0, k2=0.0, k1=0.0, pgv1=0.0, k7=0.0, k6=0.0, pmax=0.0, k5=0.0, k4=0.0, gv6=0.0, t6=0.0, pgv6=0.0, t7=0.0, gv5=0.0, k8=0.0, gv1=0.0, t1=0.0, t2=0.0, pgv3=0.0, db1=0.0, t3=0.0, uo=0.0, pgv2=0.0, gv4=0.0, pgv5=0.0, t4=0.0, gv2=0.0, gv3=0.0, t5=0.0, pgv4=0.0, db2=0.0, **kw_args):
        """ Initialises a new 'GovSteam1' instance.
        """
        # Intentional db hysteresisIntentional db hysteresis 
        self.eps = eps

        # Maximum valve closing velocity, p.u./sec (&lt; 0.)Maximum valve closing velocity, p.u./sec (&lt; 0.) 
        self.uc = uc

        # Base for power values (&gt; 0.)Base for power values (&gt; 0.) 
        self.mwbase = mwbase

        # Minimum valve opening (&gt;= 0.)Minimum valve opening (&gt;= 0.) 
        self.pmin = pmin

        # Fraction of HP shaft power after second boiler passFraction of HP shaft power after second boiler pass 
        self.k3 = k3

        # Governor gain (reciprocal of droop) (&gt; 0.)Governor gain (reciprocal of droop) (&gt; 0.) 
        self.k = k

        # Fraction of LP shaft power after first boiler passFraction of LP shaft power after first boiler pass 
        self.k2 = k2

        # Fraction of HP shaft power after first boiler passFraction of HP shaft power after first boiler pass 
        self.k1 = k1

        # Nonlinear gain power value point 1Nonlinear gain power value point 1 
        self.pgv1 = pgv1

        # Fraction of HP shaft power after fourth boiler passFraction of HP shaft power after fourth boiler pass 
        self.k7 = k7

        # Fraction of LP shaft power after third boiler passFraction of LP shaft power after third boiler pass 
        self.k6 = k6

        # Maximum valve opening (&gt; Pmin)Maximum valve opening (&gt; Pmin) 
        self.pmax = pmax

        # Fraction of HP shaft power after third boiler passFraction of HP shaft power after third boiler pass 
        self.k5 = k5

        # Fraction of LP shaft power after second boiler passFraction of LP shaft power after second boiler pass 
        self.k4 = k4

        # Nonlinear gain valve position point 6Nonlinear gain valve position point 6 
        self.gv6 = gv6

        # Time constant of third boiler passTime constant of third boiler pass 
        self.t6 = t6

        # Nonlinear gain power value point 6Nonlinear gain power value point 6 
        self.pgv6 = pgv6

        # Time constant of fourth boiler pasTime constant of fourth boiler pas 
        self.t7 = t7

        # Nonlinear gain valve position point 5Nonlinear gain valve position point 5 
        self.gv5 = gv5

        # Fraction of LP shaft power after fourth boiler passFraction of LP shaft power after fourth boiler pass 
        self.k8 = k8

        # Nonlinear gain valve position point 1Nonlinear gain valve position point 1 
        self.gv1 = gv1

        # Governor lag time constantGovernor lag time constant 
        self.t1 = t1

        # Governor lead time constantGovernor lead time constant 
        self.t2 = t2

        # Nonlinear gain power value point 3Nonlinear gain power value point 3 
        self.pgv3 = pgv3

        # Intentional deadband widthIntentional deadband width 
        self.db1 = db1

        # Valve positioner time constant (&gt; 0.)Valve positioner time constant (&gt; 0.) 
        self.t3 = t3

        # Maximum valve opening velocity (&gt; 0.)Maximum valve opening velocity (&gt; 0.) 
        self.uo = uo

        # Nonlinear gain power value point 2Nonlinear gain power value point 2 
        self.pgv2 = pgv2

        # Nonlinear gain valve position point 4Nonlinear gain valve position point 4 
        self.gv4 = gv4

        # Nonlinear gain power value point 5Nonlinear gain power value point 5 
        self.pgv5 = pgv5

        # Inlet piping/steam bowl time constantInlet piping/steam bowl time constant 
        self.t4 = t4

        # Nonlinear gain valve position point 2Nonlinear gain valve position point 2 
        self.gv2 = gv2

        # Nonlinear gain valve position point 3Nonlinear gain valve position point 3 
        self.gv3 = gv3

        # Time constant of second boiler passTime constant of second boiler pass 
        self.t5 = t5

        # Nonlinear gain power value point 4Nonlinear gain power value point 4 
        self.pgv4 = pgv4

        # Unintentional deadbandUnintentional deadband 
        self.db2 = db2



        super(GovSteam1, self).__init__(**kw_args)
    # >>> gov_steam1


    def __str__(self):
        """ Returns a string representation of the GovSteam1.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_steam1.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovSteam1.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovSteam1", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:GovSteam1.eps>%s</%s:GovSteam1.eps>' % \
            (indent, ns_prefix, self.eps, ns_prefix)
        s += '%s<%s:GovSteam1.uc>%s</%s:GovSteam1.uc>' % \
            (indent, ns_prefix, self.uc, ns_prefix)
        s += '%s<%s:GovSteam1.mwbase>%s</%s:GovSteam1.mwbase>' % \
            (indent, ns_prefix, self.mwbase, ns_prefix)
        s += '%s<%s:GovSteam1.pmin>%s</%s:GovSteam1.pmin>' % \
            (indent, ns_prefix, self.pmin, ns_prefix)
        s += '%s<%s:GovSteam1.k3>%s</%s:GovSteam1.k3>' % \
            (indent, ns_prefix, self.k3, ns_prefix)
        s += '%s<%s:GovSteam1.k>%s</%s:GovSteam1.k>' % \
            (indent, ns_prefix, self.k, ns_prefix)
        s += '%s<%s:GovSteam1.k2>%s</%s:GovSteam1.k2>' % \
            (indent, ns_prefix, self.k2, ns_prefix)
        s += '%s<%s:GovSteam1.k1>%s</%s:GovSteam1.k1>' % \
            (indent, ns_prefix, self.k1, ns_prefix)
        s += '%s<%s:GovSteam1.pgv1>%s</%s:GovSteam1.pgv1>' % \
            (indent, ns_prefix, self.pgv1, ns_prefix)
        s += '%s<%s:GovSteam1.k7>%s</%s:GovSteam1.k7>' % \
            (indent, ns_prefix, self.k7, ns_prefix)
        s += '%s<%s:GovSteam1.k6>%s</%s:GovSteam1.k6>' % \
            (indent, ns_prefix, self.k6, ns_prefix)
        s += '%s<%s:GovSteam1.pmax>%s</%s:GovSteam1.pmax>' % \
            (indent, ns_prefix, self.pmax, ns_prefix)
        s += '%s<%s:GovSteam1.k5>%s</%s:GovSteam1.k5>' % \
            (indent, ns_prefix, self.k5, ns_prefix)
        s += '%s<%s:GovSteam1.k4>%s</%s:GovSteam1.k4>' % \
            (indent, ns_prefix, self.k4, ns_prefix)
        s += '%s<%s:GovSteam1.gv6>%s</%s:GovSteam1.gv6>' % \
            (indent, ns_prefix, self.gv6, ns_prefix)
        s += '%s<%s:GovSteam1.t6>%s</%s:GovSteam1.t6>' % \
            (indent, ns_prefix, self.t6, ns_prefix)
        s += '%s<%s:GovSteam1.pgv6>%s</%s:GovSteam1.pgv6>' % \
            (indent, ns_prefix, self.pgv6, ns_prefix)
        s += '%s<%s:GovSteam1.t7>%s</%s:GovSteam1.t7>' % \
            (indent, ns_prefix, self.t7, ns_prefix)
        s += '%s<%s:GovSteam1.gv5>%s</%s:GovSteam1.gv5>' % \
            (indent, ns_prefix, self.gv5, ns_prefix)
        s += '%s<%s:GovSteam1.k8>%s</%s:GovSteam1.k8>' % \
            (indent, ns_prefix, self.k8, ns_prefix)
        s += '%s<%s:GovSteam1.gv1>%s</%s:GovSteam1.gv1>' % \
            (indent, ns_prefix, self.gv1, ns_prefix)
        s += '%s<%s:GovSteam1.t1>%s</%s:GovSteam1.t1>' % \
            (indent, ns_prefix, self.t1, ns_prefix)
        s += '%s<%s:GovSteam1.t2>%s</%s:GovSteam1.t2>' % \
            (indent, ns_prefix, self.t2, ns_prefix)
        s += '%s<%s:GovSteam1.pgv3>%s</%s:GovSteam1.pgv3>' % \
            (indent, ns_prefix, self.pgv3, ns_prefix)
        s += '%s<%s:GovSteam1.db1>%s</%s:GovSteam1.db1>' % \
            (indent, ns_prefix, self.db1, ns_prefix)
        s += '%s<%s:GovSteam1.t3>%s</%s:GovSteam1.t3>' % \
            (indent, ns_prefix, self.t3, ns_prefix)
        s += '%s<%s:GovSteam1.uo>%s</%s:GovSteam1.uo>' % \
            (indent, ns_prefix, self.uo, ns_prefix)
        s += '%s<%s:GovSteam1.pgv2>%s</%s:GovSteam1.pgv2>' % \
            (indent, ns_prefix, self.pgv2, ns_prefix)
        s += '%s<%s:GovSteam1.gv4>%s</%s:GovSteam1.gv4>' % \
            (indent, ns_prefix, self.gv4, ns_prefix)
        s += '%s<%s:GovSteam1.pgv5>%s</%s:GovSteam1.pgv5>' % \
            (indent, ns_prefix, self.pgv5, ns_prefix)
        s += '%s<%s:GovSteam1.t4>%s</%s:GovSteam1.t4>' % \
            (indent, ns_prefix, self.t4, ns_prefix)
        s += '%s<%s:GovSteam1.gv2>%s</%s:GovSteam1.gv2>' % \
            (indent, ns_prefix, self.gv2, ns_prefix)
        s += '%s<%s:GovSteam1.gv3>%s</%s:GovSteam1.gv3>' % \
            (indent, ns_prefix, self.gv3, ns_prefix)
        s += '%s<%s:GovSteam1.t5>%s</%s:GovSteam1.t5>' % \
            (indent, ns_prefix, self.t5, ns_prefix)
        s += '%s<%s:GovSteam1.pgv4>%s</%s:GovSteam1.pgv4>' % \
            (indent, ns_prefix, self.pgv4, ns_prefix)
        s += '%s<%s:GovSteam1.db2>%s</%s:GovSteam1.db2>' % \
            (indent, ns_prefix, self.db2, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovSteam1")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_steam1.serialize


class GovSteamCC(TurbineGovernor):
    pass
    # <<< gov_steam_cc
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovSteamCC' instance.
        """


        super(GovSteamCC, self).__init__(**kw_args)
    # >>> gov_steam_cc


    def __str__(self):
        """ Returns a string representation of the GovSteamCC.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_steam_cc.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovSteamCC.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovSteamCC", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovSteamCC")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_steam_cc.serialize


class GovSteamSGO(TurbineGovernor):
    pass
    # <<< gov_steam_sgo
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovSteamSGO' instance.
        """


        super(GovSteamSGO, self).__init__(**kw_args)
    # >>> gov_steam_sgo


    def __str__(self):
        """ Returns a string representation of the GovSteamSGO.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_steam_sgo.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovSteamSGO.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovSteamSGO", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovSteamSGO")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_steam_sgo.serialize


class GovSteamFV3(TurbineGovernor):
    pass
    # <<< gov_steam_fv3
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovSteamFV3' instance.
        """


        super(GovSteamFV3, self).__init__(**kw_args)
    # >>> gov_steam_fv3


    def __str__(self):
        """ Returns a string representation of the GovSteamFV3.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_steam_fv3.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovSteamFV3.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovSteamFV3", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovSteamFV3")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_steam_fv3.serialize


class GovWT3P(TurbineGovernor):
    pass
    # <<< gov_wt3_p
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovWT3P' instance.
        """


        super(GovWT3P, self).__init__(**kw_args)
    # >>> gov_wt3_p


    def __str__(self):
        """ Returns a string representation of the GovWT3P.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_wt3_p.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovWT3P.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovWT3P", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovWT3P")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_wt3_p.serialize


class GovWT1P(TurbineGovernor):
    pass
    # <<< gov_wt1_p
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovWT1P' instance.
        """


        super(GovWT1P, self).__init__(**kw_args)
    # >>> gov_wt1_p


    def __str__(self):
        """ Returns a string representation of the GovWT1P.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_wt1_p.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovWT1P.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovWT1P", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovWT1P")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_wt1_p.serialize


class GovSteam0(TurbineGovernor):
    """ A simplified steam turbine-governor model.A simplified steam turbine-governor model.
    """
    # <<< gov_steam0
    # @generated
    def __init__(self, t2=0.0, t3=0.0, t1=0.0, vmax=0.0, dt=0.0, r=0.0, vmin=0.0, mwbase=0.0, **kw_args):
        """ Initialises a new 'GovSteam0' instance.
        """
        # Numerator time constant of T2/T3 blockNumerator time constant of T2/T3 block 
        self.t2 = t2

        # Reheater time constantReheater time constant 
        self.t3 = t3

        # Steam bowl time constantSteam bowl time constant 
        self.t1 = t1

        # Maximum valve position, p.u. of mwcapMaximum valve position, p.u. of mwcap 
        self.vmax = vmax

        # Turbine damping coefficientTurbine damping coefficient 
        self.dt = dt

        # Permanent droopPermanent droop 
        self.r = r

        # Minimum valve position, p.u. of mwcapMinimum valve position, p.u. of mwcap 
        self.vmin = vmin

        # Base for power values  (&gt; 0.)Base for power values  (&gt; 0.) 
        self.mwbase = mwbase



        super(GovSteam0, self).__init__(**kw_args)
    # >>> gov_steam0


    def __str__(self):
        """ Returns a string representation of the GovSteam0.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_steam0.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovSteam0.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovSteam0", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:GovSteam0.t2>%s</%s:GovSteam0.t2>' % \
            (indent, ns_prefix, self.t2, ns_prefix)
        s += '%s<%s:GovSteam0.t3>%s</%s:GovSteam0.t3>' % \
            (indent, ns_prefix, self.t3, ns_prefix)
        s += '%s<%s:GovSteam0.t1>%s</%s:GovSteam0.t1>' % \
            (indent, ns_prefix, self.t1, ns_prefix)
        s += '%s<%s:GovSteam0.vmax>%s</%s:GovSteam0.vmax>' % \
            (indent, ns_prefix, self.vmax, ns_prefix)
        s += '%s<%s:GovSteam0.dt>%s</%s:GovSteam0.dt>' % \
            (indent, ns_prefix, self.dt, ns_prefix)
        s += '%s<%s:GovSteam0.r>%s</%s:GovSteam0.r>' % \
            (indent, ns_prefix, self.r, ns_prefix)
        s += '%s<%s:GovSteam0.vmin>%s</%s:GovSteam0.vmin>' % \
            (indent, ns_prefix, self.vmin, ns_prefix)
        s += '%s<%s:GovSteam0.mwbase>%s</%s:GovSteam0.mwbase>' % \
            (indent, ns_prefix, self.mwbase, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovSteam0")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_steam0.serialize


class GovCT1(TurbineGovernor):
    """ General model for any prime mover with a PID governor, used primarily for combustion turbine and combined cycle units.General model for any prime mover with a PID governor, used primarily for combustion turbine and combined cycle units.
    """
    # <<< gov_ct1
    # @generated
    def __init__(self, rdown=0.0, vmax=0.0, wfnl=0.0, tdgov=0.0, aset=0.0, r=0.0, wfspd=False, kpgov=0.0, minerr=0.0, tsa=0.0, tact=0.0, tsb=0.0, ldref=0.0, kimw=0.0, maxerr=0.0, vmin=0.0, mwbase=0.0, rclose=0.0, tpelec=0.0, rup=0.0, tb=0.0, ka=0.0, ta=0.0, kdgov=0.0, kturb=0.0, db=0.0, teng=0.0, tc=0.0, ropen=0.0, dm=0.0, kiload=0.0, pmwset=0.0, rselect=False, kigov=0.0, kpload=0.0, tfload=0.0, **kw_args):
        """ Initialises a new 'GovCT1' instance.
        """
        # Maximum rate of load limit decreaseMaximum rate of load limit decrease 
        self.rdown = rdown

        # Maximum valve position limitMaximum valve position limit 
        self.vmax = vmax

        # No load fuel flowNo load fuel flow 
        self.wfnl = wfnl

        # Governor derivative controller time constantGovernor derivative controller time constant 
        self.tdgov = tdgov

        # Acceleration limiter setpointAcceleration limiter setpoint 
        self.aset = aset

        # Permanent droopPermanent droop 
        self.r = r

        # Switch for fuel source characteristic = 0 for fuel flow independent of speed = 1 fuel flow proportional to speedSwitch for fuel source characteristic = 0 for fuel flow independent of speed = 1 fuel flow proportional to speed 
        self.wfspd = wfspd

        # Governor proportional gainGovernor proportional gain 
        self.kpgov = kpgov

        # Minimum value for speed error signalMinimum value for speed error signal 
        self.minerr = minerr

        # Temperature detection lead time constantTemperature detection lead time constant 
        self.tsa = tsa

        # Actuator time constantActuator time constant 
        self.tact = tact

        # Temperature detection lag time constantTemperature detection lag time constant 
        self.tsb = tsb

        # Load limiter reference valueLoad limiter reference value 
        self.ldref = ldref

        # Power controller (reset) gainPower controller (reset) gain 
        self.kimw = kimw

        # Maximum value for speed error signalMaximum value for speed error signal 
        self.maxerr = maxerr

        # Minimum valve position limitMinimum valve position limit 
        self.vmin = vmin

        # Base for power values (&gt; 0.)Base for power values (&gt; 0.) 
        self.mwbase = mwbase

        # Minimum valve closing rateMinimum valve closing rate 
        self.rclose = rclose

        # Electrical power transducer time constant, sec. (&gt;0.)Electrical power transducer time constant, sec. (&gt;0.) 
        self.tpelec = tpelec

        # Maximum rate of load limit increaseMaximum rate of load limit increase 
        self.rup = rup

        # Turbine lag time constant, sec.  (&gt;0.)Turbine lag time constant, sec.  (&gt;0.) 
        self.tb = tb

        # Acceleration limiter gainAcceleration limiter gain 
        self.ka = ka

        # Acceleration limiter time constant (&gt;0.)Acceleration limiter time constant (&gt;0.) 
        self.ta = ta

        # Governor derivative gainGovernor derivative gain 
        self.kdgov = kdgov

        # Turbine gain  (&gt;0.)Turbine gain  (&gt;0.) 
        self.kturb = kturb

        # Speed governor dead bandSpeed governor dead band 
        self.db = db

        # Transport time delay for diesel engineTransport time delay for diesel engine 
        self.teng = teng

        # Turbine lead time constant, sec.Turbine lead time constant, sec. 
        self.tc = tc

        # Maximum valve opening rateMaximum valve opening rate 
        self.ropen = ropen

        # Speed sensitivity coefficientSpeed sensitivity coefficient 
        self.dm = dm

        # Load limiter integral gain for PI controllerLoad limiter integral gain for PI controller 
        self.kiload = kiload

        # Power controller setpointPower controller setpoint 
        self.pmwset = pmwset

        # Feedback signal for droop  = 1 electrical power = 0 none (isochronous governor) = -1 fuel valve stroke ( true stroke) = -2 governor output ( requested stroke)Feedback signal for droop  = 1 electrical power = 0 none (isochronous governor) = -1 fuel valve stroke ( true stroke) = -2 governor output ( requested stroke) 
        self.rselect = rselect

        # Governor integral gainGovernor integral gain 
        self.kigov = kigov

        # Load limiter proportional gain for PI controllerLoad limiter proportional gain for PI controller 
        self.kpload = kpload

        # Load Limiter time constant (&gt;0.)Load Limiter time constant (&gt;0.) 
        self.tfload = tfload



        super(GovCT1, self).__init__(**kw_args)
    # >>> gov_ct1


    def __str__(self):
        """ Returns a string representation of the GovCT1.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_ct1.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovCT1.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovCT1", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:GovCT1.rdown>%s</%s:GovCT1.rdown>' % \
            (indent, ns_prefix, self.rdown, ns_prefix)
        s += '%s<%s:GovCT1.vmax>%s</%s:GovCT1.vmax>' % \
            (indent, ns_prefix, self.vmax, ns_prefix)
        s += '%s<%s:GovCT1.wfnl>%s</%s:GovCT1.wfnl>' % \
            (indent, ns_prefix, self.wfnl, ns_prefix)
        s += '%s<%s:GovCT1.tdgov>%s</%s:GovCT1.tdgov>' % \
            (indent, ns_prefix, self.tdgov, ns_prefix)
        s += '%s<%s:GovCT1.aset>%s</%s:GovCT1.aset>' % \
            (indent, ns_prefix, self.aset, ns_prefix)
        s += '%s<%s:GovCT1.r>%s</%s:GovCT1.r>' % \
            (indent, ns_prefix, self.r, ns_prefix)
        s += '%s<%s:GovCT1.wfspd>%s</%s:GovCT1.wfspd>' % \
            (indent, ns_prefix, self.wfspd, ns_prefix)
        s += '%s<%s:GovCT1.kpgov>%s</%s:GovCT1.kpgov>' % \
            (indent, ns_prefix, self.kpgov, ns_prefix)
        s += '%s<%s:GovCT1.minerr>%s</%s:GovCT1.minerr>' % \
            (indent, ns_prefix, self.minerr, ns_prefix)
        s += '%s<%s:GovCT1.tsa>%s</%s:GovCT1.tsa>' % \
            (indent, ns_prefix, self.tsa, ns_prefix)
        s += '%s<%s:GovCT1.tact>%s</%s:GovCT1.tact>' % \
            (indent, ns_prefix, self.tact, ns_prefix)
        s += '%s<%s:GovCT1.tsb>%s</%s:GovCT1.tsb>' % \
            (indent, ns_prefix, self.tsb, ns_prefix)
        s += '%s<%s:GovCT1.ldref>%s</%s:GovCT1.ldref>' % \
            (indent, ns_prefix, self.ldref, ns_prefix)
        s += '%s<%s:GovCT1.kimw>%s</%s:GovCT1.kimw>' % \
            (indent, ns_prefix, self.kimw, ns_prefix)
        s += '%s<%s:GovCT1.maxerr>%s</%s:GovCT1.maxerr>' % \
            (indent, ns_prefix, self.maxerr, ns_prefix)
        s += '%s<%s:GovCT1.vmin>%s</%s:GovCT1.vmin>' % \
            (indent, ns_prefix, self.vmin, ns_prefix)
        s += '%s<%s:GovCT1.mwbase>%s</%s:GovCT1.mwbase>' % \
            (indent, ns_prefix, self.mwbase, ns_prefix)
        s += '%s<%s:GovCT1.rclose>%s</%s:GovCT1.rclose>' % \
            (indent, ns_prefix, self.rclose, ns_prefix)
        s += '%s<%s:GovCT1.tpelec>%s</%s:GovCT1.tpelec>' % \
            (indent, ns_prefix, self.tpelec, ns_prefix)
        s += '%s<%s:GovCT1.rup>%s</%s:GovCT1.rup>' % \
            (indent, ns_prefix, self.rup, ns_prefix)
        s += '%s<%s:GovCT1.tb>%s</%s:GovCT1.tb>' % \
            (indent, ns_prefix, self.tb, ns_prefix)
        s += '%s<%s:GovCT1.ka>%s</%s:GovCT1.ka>' % \
            (indent, ns_prefix, self.ka, ns_prefix)
        s += '%s<%s:GovCT1.ta>%s</%s:GovCT1.ta>' % \
            (indent, ns_prefix, self.ta, ns_prefix)
        s += '%s<%s:GovCT1.kdgov>%s</%s:GovCT1.kdgov>' % \
            (indent, ns_prefix, self.kdgov, ns_prefix)
        s += '%s<%s:GovCT1.kturb>%s</%s:GovCT1.kturb>' % \
            (indent, ns_prefix, self.kturb, ns_prefix)
        s += '%s<%s:GovCT1.db>%s</%s:GovCT1.db>' % \
            (indent, ns_prefix, self.db, ns_prefix)
        s += '%s<%s:GovCT1.teng>%s</%s:GovCT1.teng>' % \
            (indent, ns_prefix, self.teng, ns_prefix)
        s += '%s<%s:GovCT1.tc>%s</%s:GovCT1.tc>' % \
            (indent, ns_prefix, self.tc, ns_prefix)
        s += '%s<%s:GovCT1.ropen>%s</%s:GovCT1.ropen>' % \
            (indent, ns_prefix, self.ropen, ns_prefix)
        s += '%s<%s:GovCT1.dm>%s</%s:GovCT1.dm>' % \
            (indent, ns_prefix, self.dm, ns_prefix)
        s += '%s<%s:GovCT1.kiload>%s</%s:GovCT1.kiload>' % \
            (indent, ns_prefix, self.kiload, ns_prefix)
        s += '%s<%s:GovCT1.pmwset>%s</%s:GovCT1.pmwset>' % \
            (indent, ns_prefix, self.pmwset, ns_prefix)
        s += '%s<%s:GovCT1.rselect>%s</%s:GovCT1.rselect>' % \
            (indent, ns_prefix, self.rselect, ns_prefix)
        s += '%s<%s:GovCT1.kigov>%s</%s:GovCT1.kigov>' % \
            (indent, ns_prefix, self.kigov, ns_prefix)
        s += '%s<%s:GovCT1.kpload>%s</%s:GovCT1.kpload>' % \
            (indent, ns_prefix, self.kpload, ns_prefix)
        s += '%s<%s:GovCT1.tfload>%s</%s:GovCT1.tfload>' % \
            (indent, ns_prefix, self.tfload, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovCT1")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_ct1.serialize


class GovWT2T(TurbineGovernor):
    pass
    # <<< gov_wt2_t
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovWT2T' instance.
        """


        super(GovWT2T, self).__init__(**kw_args)
    # >>> gov_wt2_t


    def __str__(self):
        """ Returns a string representation of the GovWT2T.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_wt2_t.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovWT2T.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovWT2T", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovWT2T")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_wt2_t.serialize


class GovHydro1(TurbineGovernor):
    """ Hydro turbine-governor model.Hydro turbine-governor model.
    """
    # <<< gov_hydro1
    # @generated
    def __init__(self, rperm=0.0, tg=0.0, tf=0.0, mwbase=0.0, at=0.0, qnl=0.0, tw=0.0, dturb=0.0, rtemp=0.0, tr=0.0, **kw_args):
        """ Initialises a new 'GovHydro1' instance.
        """
        # Permanent droop (R) (&gt;0)Permanent droop (R) (&gt;0) 
        self.rperm = rperm

        # Gate servo time constant (&gt;0)Gate servo time constant (&gt;0) 
        self.tg = tg

        # Filter time constant (&gt;0)Filter time constant (&gt;0) 
        self.tf = tf

        # Base for power values  (&gt; 0.)Base for power values  (&gt; 0.) 
        self.mwbase = mwbase

        # Turbine gain (&gt;0)Turbine gain (&gt;0) 
        self.at = at

        # No-load flow at nominal head (&gt;=0)No-load flow at nominal head (&gt;=0) 
        self.qnl = qnl

        # Water inertia time constant (&gt;0)Water inertia time constant (&gt;0) 
        self.tw = tw

        # Turbine damping factor (&gt;=0)Turbine damping factor (&gt;=0) 
        self.dturb = dturb

        # Temporary droop (r) (&gt;R)Temporary droop (r) (&gt;R) 
        self.rtemp = rtemp

        # Washout time constant (&gt;0)Washout time constant (&gt;0) 
        self.tr = tr



        super(GovHydro1, self).__init__(**kw_args)
    # >>> gov_hydro1


    def __str__(self):
        """ Returns a string representation of the GovHydro1.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_hydro1.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovHydro1.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovHydro1", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:GovHydro1.rperm>%s</%s:GovHydro1.rperm>' % \
            (indent, ns_prefix, self.rperm, ns_prefix)
        s += '%s<%s:GovHydro1.tg>%s</%s:GovHydro1.tg>' % \
            (indent, ns_prefix, self.tg, ns_prefix)
        s += '%s<%s:GovHydro1.tf>%s</%s:GovHydro1.tf>' % \
            (indent, ns_prefix, self.tf, ns_prefix)
        s += '%s<%s:GovHydro1.mwbase>%s</%s:GovHydro1.mwbase>' % \
            (indent, ns_prefix, self.mwbase, ns_prefix)
        s += '%s<%s:GovHydro1.at>%s</%s:GovHydro1.at>' % \
            (indent, ns_prefix, self.at, ns_prefix)
        s += '%s<%s:GovHydro1.qnl>%s</%s:GovHydro1.qnl>' % \
            (indent, ns_prefix, self.qnl, ns_prefix)
        s += '%s<%s:GovHydro1.tw>%s</%s:GovHydro1.tw>' % \
            (indent, ns_prefix, self.tw, ns_prefix)
        s += '%s<%s:GovHydro1.dturb>%s</%s:GovHydro1.dturb>' % \
            (indent, ns_prefix, self.dturb, ns_prefix)
        s += '%s<%s:GovHydro1.rtemp>%s</%s:GovHydro1.rtemp>' % \
            (indent, ns_prefix, self.rtemp, ns_prefix)
        s += '%s<%s:GovHydro1.tr>%s</%s:GovHydro1.tr>' % \
            (indent, ns_prefix, self.tr, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovHydro1")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_hydro1.serialize


class GovHydroPID2(TurbineGovernor):
    pass
    # <<< gov_hydro_pid2
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovHydroPID2' instance.
        """


        super(GovHydroPID2, self).__init__(**kw_args)
    # >>> gov_hydro_pid2


    def __str__(self):
        """ Returns a string representation of the GovHydroPID2.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_hydro_pid2.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovHydroPID2.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovHydroPID2", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovHydroPID2")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_hydro_pid2.serialize


class GovWT4T(TurbineGovernor):
    pass
    # <<< gov_wt4_t
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovWT4T' instance.
        """


        super(GovWT4T, self).__init__(**kw_args)
    # >>> gov_wt4_t


    def __str__(self):
        """ Returns a string representation of the GovWT4T.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_wt4_t.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovWT4T.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovWT4T", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovWT4T")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_wt4_t.serialize


class GovSteamEU(TurbineGovernor):
    pass
    # <<< gov_steam_eu
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovSteamEU' instance.
        """


        super(GovSteamEU, self).__init__(**kw_args)
    # >>> gov_steam_eu


    def __str__(self):
        """ Returns a string representation of the GovSteamEU.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_steam_eu.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovSteamEU.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovSteamEU", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovSteamEU")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_steam_eu.serialize


class GovHydro0(TurbineGovernor):
    pass
    # <<< gov_hydro0
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovHydro0' instance.
        """


        super(GovHydro0, self).__init__(**kw_args)
    # >>> gov_hydro0


    def __str__(self):
        """ Returns a string representation of the GovHydro0.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_hydro0.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovHydro0.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovHydro0", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovHydro0")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_hydro0.serialize


class GovGASTWD(TurbineGovernor):
    pass
    # <<< gov_gastwd
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovGASTWD' instance.
        """


        super(GovGASTWD, self).__init__(**kw_args)
    # >>> gov_gastwd


    def __str__(self):
        """ Returns a string representation of the GovGASTWD.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_gastwd.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovGASTWD.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovGASTWD", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovGASTWD")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_gastwd.serialize


class GovGAST2(TurbineGovernor):
    pass
    # <<< gov_gast2
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GovGAST2' instance.
        """


        super(GovGAST2, self).__init__(**kw_args)
    # >>> gov_gast2


    def __str__(self):
        """ Returns a string representation of the GovGAST2.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gov_gast2.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GovGAST2.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GovGAST2", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GovGAST2")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gov_gast2.serialize


# <<< turbine_governors
# @generated
# >>> turbine_governors
