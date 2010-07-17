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


from dynamics.dynamics import RotatingMachine
from dynamics import Element
from dynamics.dynamics import AsynchronousMachine

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Generators"

class GenSync(RotatingMachine):
    """ Synchronous generator model. A single standard synchronous model is defined for the CIM, with several variations indicated by the 'model type' attribute.  This model can be used for all types of synchronous machines (salient pole, solid iron rotor, etc.).Synchronous generator model. A single standard synchronous model is defined for the CIM, with several variations indicated by the 'model type' attribute.  This model can be used for all types of synchronous machines (salient pole, solid iron rotor, etc.).
    """
    pass
    # <<< gen_sync
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GenSync' instance.
        """


        super(GenSync, self).__init__(**kw_args)
    # >>> gen_sync


    def __str__(self):
        """ Returns a string representation of the GenSync.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gen_sync.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GenSync.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GenSync", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:RotatingMachine.rated_s>%s</%s:RotatingMachine.rated_s>' % \
            (indent, ns_prefix, self.rated_s, ns_prefix)
        s += '%s<%s:RotatingMachine.s1>%s</%s:RotatingMachine.s1>' % \
            (indent, ns_prefix, self.s1, ns_prefix)
        s += '%s<%s:RotatingMachine.s12>%s</%s:RotatingMachine.s12>' % \
            (indent, ns_prefix, self.s12, ns_prefix)
        s += '%s<%s:RotatingMachine.h>%s</%s:RotatingMachine.h>' % \
            (indent, ns_prefix, self.h, ns_prefix)
        s += '%s<%s:RotatingMachine.d>%s</%s:RotatingMachine.d>' % \
            (indent, ns_prefix, self.d, ns_prefix)
        s += '%s<%s:RotatingMachine.rs>%s</%s:RotatingMachine.rs>' % \
            (indent, ns_prefix, self.rs, ns_prefix)
        s += '%s<%s:RotatingMachine.xls>%s</%s:RotatingMachine.xls>' % \
            (indent, ns_prefix, self.xls, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GenSync")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gen_sync.serialize


class GenLoad(Element):
    """ Representation of a small generator as a negative load rather than a dynamic generator model. This practice is also referred to as 'netting' the generation with the load, i.e. taking the net value of load minus generation as the new load value.  For dynamic modeling purposes, each generator that does not have a dynamic load model must have a genLoad record.Representation of a small generator as a negative load rather than a dynamic generator model. This practice is also referred to as 'netting' the generation with the load, i.e. taking the net value of load minus generation as the new load value.  For dynamic modeling purposes, each generator that does not have a dynamic load model must have a genLoad record.
    """
    pass
    # <<< gen_load
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GenLoad' instance.
        """


        super(GenLoad, self).__init__(**kw_args)
    # >>> gen_load


    def __str__(self):
        """ Returns a string representation of the GenLoad.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gen_load.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GenLoad.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GenLoad", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GenLoad")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gen_load.serialize


class GenAsync(AsynchronousMachine):
    """ An asynchronous (induction) generator with no external connection to the rotor windings, e.g., squirrel-cage induction machine.An asynchronous (induction) generator with no external connection to the rotor windings, e.g., squirrel-cage induction machine.
    """
    pass
    # <<< gen_async
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GenAsync' instance.
        """


        super(GenAsync, self).__init__(**kw_args)
    # >>> gen_async


    def __str__(self):
        """ Returns a string representation of the GenAsync.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gen_async.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GenAsync.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GenAsync", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:RotatingMachine.rated_s>%s</%s:RotatingMachine.rated_s>' % \
            (indent, ns_prefix, self.rated_s, ns_prefix)
        s += '%s<%s:RotatingMachine.s1>%s</%s:RotatingMachine.s1>' % \
            (indent, ns_prefix, self.s1, ns_prefix)
        s += '%s<%s:RotatingMachine.s12>%s</%s:RotatingMachine.s12>' % \
            (indent, ns_prefix, self.s12, ns_prefix)
        s += '%s<%s:RotatingMachine.h>%s</%s:RotatingMachine.h>' % \
            (indent, ns_prefix, self.h, ns_prefix)
        s += '%s<%s:RotatingMachine.d>%s</%s:RotatingMachine.d>' % \
            (indent, ns_prefix, self.d, ns_prefix)
        s += '%s<%s:RotatingMachine.rs>%s</%s:RotatingMachine.rs>' % \
            (indent, ns_prefix, self.rs, ns_prefix)
        s += '%s<%s:RotatingMachine.xls>%s</%s:RotatingMachine.xls>' % \
            (indent, ns_prefix, self.xls, ns_prefix)
        s += '%s<%s:AsynchronousMachine.rr1>%s</%s:AsynchronousMachine.rr1>' % \
            (indent, ns_prefix, self.rr1, ns_prefix)
        s += '%s<%s:AsynchronousMachine.xp>%s</%s:AsynchronousMachine.xp>' % \
            (indent, ns_prefix, self.xp, ns_prefix)
        s += '%s<%s:AsynchronousMachine.tpo>%s</%s:AsynchronousMachine.tpo>' % \
            (indent, ns_prefix, self.tpo, ns_prefix)
        s += '%s<%s:AsynchronousMachine.xm>%s</%s:AsynchronousMachine.xm>' % \
            (indent, ns_prefix, self.xm, ns_prefix)
        s += '%s<%s:AsynchronousMachine.xs>%s</%s:AsynchronousMachine.xs>' % \
            (indent, ns_prefix, self.xs, ns_prefix)
        s += '%s<%s:AsynchronousMachine.rr2>%s</%s:AsynchronousMachine.rr2>' % \
            (indent, ns_prefix, self.rr2, ns_prefix)
        s += '%s<%s:AsynchronousMachine.xlr1>%s</%s:AsynchronousMachine.xlr1>' % \
            (indent, ns_prefix, self.xlr1, ns_prefix)
        s += '%s<%s:AsynchronousMachine.xlr2>%s</%s:AsynchronousMachine.xlr2>' % \
            (indent, ns_prefix, self.xlr2, ns_prefix)
        s += '%s<%s:AsynchronousMachine.tppo>%s</%s:AsynchronousMachine.tppo>' % \
            (indent, ns_prefix, self.tppo, ns_prefix)
        s += '%s<%s:AsynchronousMachine.xpp>%s</%s:AsynchronousMachine.xpp>' % \
            (indent, ns_prefix, self.xpp, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GenAsync")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gen_async.serialize


class GenEquiv(RotatingMachine):
    """ An equivalent representation of a synchronous generator as a constant internal voltage behind an impedance Ra plus Xp.An equivalent representation of a synchronous generator as a constant internal voltage behind an impedance Ra plus Xp.
    """
    # <<< gen_equiv
    # @generated
    def __init__(self, xp=0.0, **kw_args):
        """ Initialises a new 'GenEquiv' instance.
        """
        # Equivalent reactance, also known as Xp.Equivalent reactance, also known as Xp. 
        self.xp = xp



        super(GenEquiv, self).__init__(**kw_args)
    # >>> gen_equiv


    def __str__(self):
        """ Returns a string representation of the GenEquiv.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gen_equiv.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GenEquiv.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GenEquiv", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:GenEquiv.xp>%s</%s:GenEquiv.xp>' % \
            (indent, ns_prefix, self.xp, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:RotatingMachine.rated_s>%s</%s:RotatingMachine.rated_s>' % \
            (indent, ns_prefix, self.rated_s, ns_prefix)
        s += '%s<%s:RotatingMachine.s1>%s</%s:RotatingMachine.s1>' % \
            (indent, ns_prefix, self.s1, ns_prefix)
        s += '%s<%s:RotatingMachine.s12>%s</%s:RotatingMachine.s12>' % \
            (indent, ns_prefix, self.s12, ns_prefix)
        s += '%s<%s:RotatingMachine.h>%s</%s:RotatingMachine.h>' % \
            (indent, ns_prefix, self.h, ns_prefix)
        s += '%s<%s:RotatingMachine.d>%s</%s:RotatingMachine.d>' % \
            (indent, ns_prefix, self.d, ns_prefix)
        s += '%s<%s:RotatingMachine.rs>%s</%s:RotatingMachine.rs>' % \
            (indent, ns_prefix, self.rs, ns_prefix)
        s += '%s<%s:RotatingMachine.xls>%s</%s:RotatingMachine.xls>' % \
            (indent, ns_prefix, self.xls, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GenEquiv")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gen_equiv.serialize


# <<< generators
# @generated
# >>> generators
