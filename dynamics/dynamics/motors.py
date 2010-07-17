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


from dynamics.dynamics import AsynchronousMachine
from dynamics import Element
from dynamics.dynamics import RotatingMachine

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Motors"

class MotorAsync(AsynchronousMachine):
    """ An asynchronous (induction) motor with no external connection to the rotor windings, e.g., a squirrel-cage induction motor.An asynchronous (induction) motor with no external connection to the rotor windings, e.g., a squirrel-cage induction motor.
    """
    pass
    # <<< motor_async
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'MotorAsync' instance.
        """


        super(MotorAsync, self).__init__(**kw_args)
    # >>> motor_async


    def __str__(self):
        """ Returns a string representation of the MotorAsync.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< motor_async.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MotorAsync.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MotorAsync", self.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "MotorAsync")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> motor_async.serialize


class MechanicalLoad(Element):
    """ A mechanical load represents the variation in a motor's shaft torque or power as a function of shaft speed.A mechanical load represents the variation in a motor's shaft torque or power as a function of shaft speed.
    """
    pass
    # <<< mechanical_load
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'MechanicalLoad' instance.
        """


        super(MechanicalLoad, self).__init__(**kw_args)
    # >>> mechanical_load


    def __str__(self):
        """ Returns a string representation of the MechanicalLoad.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< mechanical_load.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MechanicalLoad.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MechanicalLoad", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MechanicalLoad")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> mechanical_load.serialize


class SynchronousMotorType(Element):
    """ Type of synchronous motorType of synchronous motor
    """
    pass
    # <<< synchronous_motor_type
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'SynchronousMotorType' instance.
        """


        super(SynchronousMotorType, self).__init__(**kw_args)
    # >>> synchronous_motor_type


    def __str__(self):
        """ Returns a string representation of the SynchronousMotorType.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< synchronous_motor_type.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SynchronousMotorType.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SynchronousMotorType", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SynchronousMotorType")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> synchronous_motor_type.serialize


class MotorSync(RotatingMachine):
    """ A large industrial motor or group of similar motors.  They are represented as <b>generators with negative Pgen</b> in the static (power flow) data.A large industrial motor or group of similar motors.  They are represented as <b>generators with negative Pgen</b> in the static (power flow) data.
    """
    pass
    # <<< motor_sync
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'MotorSync' instance.
        """


        super(MotorSync, self).__init__(**kw_args)
    # >>> motor_sync


    def __str__(self):
        """ Returns a string representation of the MotorSync.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< motor_sync.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MotorSync.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MotorSync", self.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "MotorSync")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> motor_sync.serialize


class MechLoad1(MechanicalLoad):
    """ Mechanical load model 1Mechanical load model 1
    """
    # <<< mech_load1
    # @generated
    def __init__(self, b=0.0, a=0.0, d=0.0, e=0.0, **kw_args):
        """ Initialises a new 'MechLoad1' instance.
        """
        # Speed squared coefficientSpeed squared coefficient 
        self.b = b

        # Speed squared coefficientSpeed squared coefficient 
        self.a = a

        # Speed to the exponent coefficientSpeed to the exponent coefficient 
        self.d = d

        # ExponentExponent 
        self.e = e



        super(MechLoad1, self).__init__(**kw_args)
    # >>> mech_load1


    def __str__(self):
        """ Returns a string representation of the MechLoad1.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< mech_load1.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MechLoad1.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MechLoad1", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:MechLoad1.b>%s</%s:MechLoad1.b>' % \
            (indent, ns_prefix, self.b, ns_prefix)
        s += '%s<%s:MechLoad1.a>%s</%s:MechLoad1.a>' % \
            (indent, ns_prefix, self.a, ns_prefix)
        s += '%s<%s:MechLoad1.d>%s</%s:MechLoad1.d>' % \
            (indent, ns_prefix, self.d, ns_prefix)
        s += '%s<%s:MechLoad1.e>%s</%s:MechLoad1.e>' % \
            (indent, ns_prefix, self.e, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MechLoad1")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> mech_load1.serialize


# <<< motors
# @generated
# >>> motors
