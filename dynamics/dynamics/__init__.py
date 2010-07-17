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

""" This package models generalized dynamic models. Standard models and user defined dynamics models are included.  In some ways this duplicates the partial modeling that was done in the GenerationDynamics package, but it far exceeds that package in terms of flexibility and extensibility.   This package does not attempt to fully specficfy all possible dynamics models in specific UML, but rather builds a framework in which to exchange standard or custom dyanmics models based on 'well known' block functions.This package models generalized dynamic models. Standard models and user defined dynamics models are included.  In some ways this duplicates the partial modeling that was done in the GenerationDynamics package, but it far exceeds that package in terms of flexibility and extensibility.   This package does not attempt to fully specficfy all possible dynamics models in specific UML, but rather builds a framework in which to exchange standard or custom dyanmics models based on 'well known' block functions.
"""

from dynamics import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Dynamics"

class RotatingMachine(Element):
    """ A rotating machine which may be used as a generator or motor.A rotating machine which may be used as a generator or motor.
    """
    # <<< rotating_machine
    # @generated
    def __init__(self, rated_s=0.0, s1=0.0, s12=0.0, h=0.0, d=0.0, rs=0.0, xls=0.0, **kw_args):
        """ Initialises a new 'RotatingMachine' instance.
        """
        # Nameplate apparent power rating for the unitNameplate apparent power rating for the unit 
        self.rated_s = rated_s

        # Saturation factor at rated term. voltage (&gt;= 0.)Saturation factor at rated term. voltage (&gt;= 0.) 
        self.s1 = s1

        # Saturation factor at 120% of rated term.voltage (&gt;=S1)Saturation factor at 120% of rated term.voltage (&gt;=S1) 
        self.s12 = s12

        # Inertia constant of generator or motor and mechanical load (&gt;0). <b>H</b> is the stored energy in the rotating mass. For a generator, this includes the <b>generator plus all other elements (turbine, exciter) on the same shaft</b> and has units of MW-sec. For a motor, it includes the motor plus its mechanical load. Conventional units are per unit on the generator MVA base, usually expressed as MW-sec./MVA or just sec.Inertia constant of generator or motor and mechanical load (&gt;0). <b>H</b> is the stored energy in the rotating mass. For a generator, this includes the <b>generator plus all other elements (turbine, exciter) on the same shaft</b> and has units of MW-sec. For a motor, it includes the motor plus its mechanical load. Conventional units are per unit on the generator MVA base, usually expressed as MW-sec./MVA or just sec. 
        self.h = h

        # Damping torque coefficient. <b>D</b> represents a linearized approximation of damping torque effects. This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modeled in detailDamping torque coefficient. <b>D</b> represents a linearized approximation of damping torque effects. This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modeled in detail 
        self.d = d

        # Stator (armature) resistance (&gt;= 0.) - Equivalent resistance when used for GenEquiv modelStator (armature) resistance (&gt;= 0.) - Equivalent resistance when used for GenEquiv model 
        self.rs = rs

        # Stator leakage reactance (&gt; 0.)Stator leakage reactance (&gt; 0.) 
        self.xls = xls



        super(RotatingMachine, self).__init__(**kw_args)
    # >>> rotating_machine


    def __str__(self):
        """ Returns a string representation of the RotatingMachine.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< rotating_machine.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RotatingMachine.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RotatingMachine", self.uri)
        if format:
            indent += ' ' * depth

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
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "RotatingMachine")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> rotating_machine.serialize


class MetaBlockConOutput(Element):
    """ If model uses MeasurementType association, it means the output is pushed back to the steady state model (if reasonable).If model uses MeasurementType association, it means the output is pushed back to the steady state model (if reasonable).
    """
    pass
    # <<< meta_block_con_output
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'MetaBlockConOutput' instance.
        """


        super(MetaBlockConOutput, self).__init__(**kw_args)
    # >>> meta_block_con_output


    def __str__(self):
        """ Returns a string representation of the MetaBlockConOutput.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< meta_block_con_output.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MetaBlockConOutput.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MetaBlockConOutput", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MetaBlockConOutput")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> meta_block_con_output.serialize


class MetaBlock(Element):
    """ A block is a meta-data representation of a control block.   It has an external interface and an optinal internal interface. Blocks internals can be ommitted if the block is well understood by both exchange parties.    When well understood by both partice the block can be treated as a primitive block.   All dynamic models must be defined to the level of primtive blocks in order for the model to be consumed and used for dynamic simulation. Examples of primitive blocks include a well known IEEE exciter model, a summation block, or an integrator block.A block is a meta-data representation of a control block.   It has an external interface and an optinal internal interface. Blocks internals can be ommitted if the block is well understood by both exchange parties.    When well understood by both partice the block can be treated as a primitive block.   All dynamic models must be defined to the level of primtive blocks in order for the model to be consumed and used for dynamic simulation. Examples of primitive blocks include a well known IEEE exciter model, a summation block, or an integrator block.
    """
    # <<< meta_block
    # @generated
    def __init__(self, proprietary=False, **kw_args):
        """ Initialises a new 'MetaBlock' instance.
        """
        # This block is a proprietary block. Only inputs, outputs and parameters are exchanged.This block is a proprietary block. Only inputs, outputs and parameters are exchanged. 
        self.proprietary = proprietary



        super(MetaBlock, self).__init__(**kw_args)
    # >>> meta_block


    def __str__(self):
        """ Returns a string representation of the MetaBlock.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< meta_block.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MetaBlock.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MetaBlock", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:MetaBlock.proprietary>%s</%s:MetaBlock.proprietary>' % \
            (indent, ns_prefix, self.proprietary, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MetaBlock")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> meta_block.serialize


class BlockParameter(Element):
    """ Specification of a paramter for use in a dynamic block. This is a paramters like a time constant that could be unique for each instance of, for example, an exciter in the model.Specification of a paramter for use in a dynamic block. This is a paramters like a time constant that could be unique for each instance of, for example, an exciter in the model.
    """
    # <<< block_parameter
    # @generated
    def __init__(self, value=0.0, **kw_args):
        """ Initialises a new 'BlockParameter' instance.
        """
        # The paramter value for this instance of a dynamic block usage.The paramter value for this instance of a dynamic block usage. 
        self.value = value



        super(BlockParameter, self).__init__(**kw_args)
    # >>> block_parameter


    def __str__(self):
        """ Returns a string representation of the BlockParameter.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< block_parameter.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BlockParameter.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BlockParameter", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:BlockParameter.value>%s</%s:BlockParameter.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "BlockParameter")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> block_parameter.serialize


class MetaBlockReference(Element):
    """ References a control block at the internal meta dynamics model level.    These references are contained in other blocks and reference the single instance of the meta model that defines a particular block definition. One would not expect to see bock references contained within a primitive block.References a control block at the internal meta dynamics model level.    These references are contained in other blocks and reference the single instance of the meta model that defines a particular block definition. One would not expect to see bock references contained within a primitive block.
    """
    # <<< meta_block_reference
    # @generated
    def __init__(self, equation_type=0, **kw_args):
        """ Initialises a new 'MetaBlockReference' instance.
        """
        # should be enum, initial conditions vs. simulation equationsshould be enum, initial conditions vs. simulation equations 
        self.equation_type = equation_type



        super(MetaBlockReference, self).__init__(**kw_args)
    # >>> meta_block_reference


    def __str__(self):
        """ Returns a string representation of the MetaBlockReference.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< meta_block_reference.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MetaBlockReference.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MetaBlockReference", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:MetaBlockReference.equation_type>%s</%s:MetaBlockReference.equation_type>' % \
            (indent, ns_prefix, self.equation_type, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MetaBlockReference")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> meta_block_reference.serialize


class ExcitationSystemLimiter(Element):
    pass
    # <<< excitation_system_limiter
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ExcitationSystemLimiter' instance.
        """


        super(ExcitationSystemLimiter, self).__init__(**kw_args)
    # >>> excitation_system_limiter


    def __str__(self):
        """ Returns a string representation of the ExcitationSystemLimiter.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< excitation_system_limiter.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExcitationSystemLimiter.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExcitationSystemLimiter", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExcitationSystemLimiter")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> excitation_system_limiter.serialize


class MetaBlockConnectivity(Element):
    pass
    # <<< meta_block_connectivity
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'MetaBlockConnectivity' instance.
        """


        super(MetaBlockConnectivity, self).__init__(**kw_args)
    # >>> meta_block_connectivity


    def __str__(self):
        """ Returns a string representation of the MetaBlockConnectivity.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< meta_block_connectivity.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MetaBlockConnectivity.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MetaBlockConnectivity", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MetaBlockConnectivity")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> meta_block_connectivity.serialize


class ProtectiveDevice(Element):
    pass
    # <<< protective_device
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ProtectiveDevice' instance.
        """


        super(ProtectiveDevice, self).__init__(**kw_args)
    # >>> protective_device


    def __str__(self):
        """ Returns a string representation of the ProtectiveDevice.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< protective_device.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ProtectiveDevice.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ProtectiveDevice", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ProtectiveDevice")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> protective_device.serialize


class SourceModels(Element):
    pass
    # <<< source_models
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'SourceModels' instance.
        """


        super(SourceModels, self).__init__(**kw_args)
    # >>> source_models


    def __str__(self):
        """ Returns a string representation of the SourceModels.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< source_models.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SourceModels.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SourceModels", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SourceModels")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> source_models.serialize


class MetaBlockOutputReference(Element):
    pass
    # <<< meta_block_output_reference
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'MetaBlockOutputReference' instance.
        """


        super(MetaBlockOutputReference, self).__init__(**kw_args)
    # >>> meta_block_output_reference


    def __str__(self):
        """ Returns a string representation of the MetaBlockOutputReference.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< meta_block_output_reference.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MetaBlockOutputReference.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MetaBlockOutputReference", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MetaBlockOutputReference")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> meta_block_output_reference.serialize


class BlockConnection(Element):
    """ A meta-dyanamics model connectivity specification.A meta-dyanamics model connectivity specification.
    """
    pass
    # <<< block_connection
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'BlockConnection' instance.
        """


        super(BlockConnection, self).__init__(**kw_args)
    # >>> block_connection


    def __str__(self):
        """ Returns a string representation of the BlockConnection.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< block_connection.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BlockConnection.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BlockConnection", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "BlockConnection")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> block_connection.serialize


class MetaBlockConInput(Element):
    """ If model the association to MeasurementType, the it means take the input from the associated PSR or Terminal in the static model.If model the association to MeasurementType, the it means take the input from the associated PSR or Terminal in the static model.
    """
    pass
    # <<< meta_block_con_input
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'MetaBlockConInput' instance.
        """


        super(MetaBlockConInput, self).__init__(**kw_args)
    # >>> meta_block_con_input


    def __str__(self):
        """ Returns a string representation of the MetaBlockConInput.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< meta_block_con_input.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MetaBlockConInput.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MetaBlockConInput", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MetaBlockConInput")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> meta_block_con_input.serialize


class StaticVarDevice(Element):
    pass
    # <<< static_var_device
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'StaticVarDevice' instance.
        """


        super(StaticVarDevice, self).__init__(**kw_args)
    # >>> static_var_device


    def __str__(self):
        """ Returns a string representation of the StaticVarDevice.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< static_var_device.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the StaticVarDevice.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "StaticVarDevice", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "StaticVarDevice")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> static_var_device.serialize


class MetaBlockConnection(Element):
    # <<< meta_block_connection
    # @generated
    def __init__(self, slotname='', **kw_args):
        """ Initialises a new 'MetaBlockConnection' instance.
        """
        # Used for standard connection situations where multiple blocks of same class or same MetaBlock::blockkind have to be connected. The slotnames used are defined in the Reference Manual for Exchanging Standard Power System Dynamic Models. Application: Cross-compound or Combined Cycle connections.Used for standard connection situations where multiple blocks of same class or same MetaBlock::blockkind have to be connected. The slotnames used are defined in the Reference Manual for Exchanging Standard Power System Dynamic Models. Application: Cross-compound or Combined Cycle connections. 
        self.slotname = slotname



        super(MetaBlockConnection, self).__init__(**kw_args)
    # >>> meta_block_connection


    def __str__(self):
        """ Returns a string representation of the MetaBlockConnection.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< meta_block_connection.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MetaBlockConnection.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MetaBlockConnection", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:MetaBlockConnection.slotname>%s</%s:MetaBlockConnection.slotname>' % \
            (indent, ns_prefix, self.slotname, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MetaBlockConnection")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> meta_block_connection.serialize


class BlockConnectivity(Element):
    """ A instance definition of connectivity of BlockUsage objects as defined in a a BlockConnection within the dyanmics-meta-model.A instance definition of connectivity of BlockUsage objects as defined in a a BlockConnection within the dyanmics-meta-model.
    """
    pass
    # <<< block_connectivity
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'BlockConnectivity' instance.
        """


        super(BlockConnectivity, self).__init__(**kw_args)
    # >>> block_connectivity


    def __str__(self):
        """ Returns a string representation of the BlockConnectivity.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< block_connectivity.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BlockConnectivity.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BlockConnectivity", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "BlockConnectivity")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> block_connectivity.serialize


class MetaBlockConSignal(Element):
    pass
    # <<< meta_block_con_signal
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'MetaBlockConSignal' instance.
        """


        super(MetaBlockConSignal, self).__init__(**kw_args)
    # >>> meta_block_con_signal


    def __str__(self):
        """ Returns a string representation of the MetaBlockConSignal.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< meta_block_con_signal.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MetaBlockConSignal.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MetaBlockConSignal", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MetaBlockConSignal")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> meta_block_con_signal.serialize


class Block(Element):
    """ A specific usage of a dynamics block, supplied with parameters and any linkages to the power system static model that are required.     Sometimes a block is used to simply specify a location of input or output from dyanmics equations to the static model.A specific usage of a dynamics block, supplied with parameters and any linkages to the power system static model that are required.     Sometimes a block is used to simply specify a location of input or output from dyanmics equations to the static model.
    """
    # <<< block
    # @generated
    def __init__(self, in_service=False, **kw_args):
        """ Initialises a new 'Block' instance.
        """
 
        self.in_service = in_service



        super(Block, self).__init__(**kw_args)
    # >>> block


    def __str__(self):
        """ Returns a string representation of the Block.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< block.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Block.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Block", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:Block.in_service>%s</%s:Block.in_service>' % \
            (indent, ns_prefix, self.in_service, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Block")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> block.serialize


class MetaBlockStateReference(Element):
    pass
    # <<< meta_block_state_reference
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'MetaBlockStateReference' instance.
        """


        super(MetaBlockStateReference, self).__init__(**kw_args)
    # >>> meta_block_state_reference


    def __str__(self):
        """ Returns a string representation of the MetaBlockStateReference.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< meta_block_state_reference.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MetaBlockStateReference.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MetaBlockStateReference", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MetaBlockStateReference")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> meta_block_state_reference.serialize


class TieToMeasurement(Element):
    """ Ties a block input to a specific state variable measurment.  Thus giving a unit type, a location in the network (typically a terminal).   A specific value is not given, just enough information to obtain the value from the model during a solution. This has nothing to do with SCADA.Ties a block input to a specific state variable measurment.  Thus giving a unit type, a location in the network (typically a terminal).   A specific value is not given, just enough information to obtain the value from the model during a solution. This has nothing to do with SCADA.
    """
    pass
    # <<< tie_to_measurement
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'TieToMeasurement' instance.
        """


        super(TieToMeasurement, self).__init__(**kw_args)
    # >>> tie_to_measurement


    def __str__(self):
        """ Returns a string representation of the TieToMeasurement.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< tie_to_measurement.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TieToMeasurement.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TieToMeasurement", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "TieToMeasurement")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> tie_to_measurement.serialize


class MetaBlockSignal(Element):
    pass
    # <<< meta_block_signal
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'MetaBlockSignal' instance.
        """


        super(MetaBlockSignal, self).__init__(**kw_args)
    # >>> meta_block_signal


    def __str__(self):
        """ Returns a string representation of the MetaBlockSignal.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< meta_block_signal.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MetaBlockSignal.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MetaBlockSignal", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MetaBlockSignal")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> meta_block_signal.serialize


class MetaBlockInputReference(Element):
    pass
    # <<< meta_block_input_reference
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'MetaBlockInputReference' instance.
        """


        super(MetaBlockInputReference, self).__init__(**kw_args)
    # >>> meta_block_input_reference


    def __str__(self):
        """ Returns a string representation of the MetaBlockInputReference.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< meta_block_input_reference.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MetaBlockInputReference.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MetaBlockInputReference", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MetaBlockInputReference")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> meta_block_input_reference.serialize


class MetaBlockParameterReference(Element):
    """ References a parameter of a block used in the internal representation of a block.References a parameter of a block used in the internal representation of a block.
    """
    pass
    # <<< meta_block_parameter_reference
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'MetaBlockParameterReference' instance.
        """


        super(MetaBlockParameterReference, self).__init__(**kw_args)
    # >>> meta_block_parameter_reference


    def __str__(self):
        """ Returns a string representation of the MetaBlockParameterReference.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< meta_block_parameter_reference.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MetaBlockParameterReference.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MetaBlockParameterReference", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MetaBlockParameterReference")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> meta_block_parameter_reference.serialize


class MetaBlockConnectable(Element):
    """ This is a source connection for a block input at the dynamics meta-data level.   The subtypes represent different ways to obtain the numbers.  Note that a block output is NOT derived from this class since block outputs can only be computed from references to other blocks via the BlockOutputReference class.This is a source connection for a block input at the dynamics meta-data level.   The subtypes represent different ways to obtain the numbers.  Note that a block output is NOT derived from this class since block outputs can only be computed from references to other blocks via the BlockOutputReference class.
    """
    pass
    # <<< meta_block_connectable
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'MetaBlockConnectable' instance.
        """


        super(MetaBlockConnectable, self).__init__(**kw_args)
    # >>> meta_block_connectable


    def __str__(self):
        """ Returns a string representation of the MetaBlockConnectable.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< meta_block_connectable.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MetaBlockConnectable.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MetaBlockConnectable", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MetaBlockConnectable")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> meta_block_connectable.serialize


class AttributeBlockParameter(MetaBlockParameter):
    """ An attribute from the associated PowerSystemResource is used.   This is like reflection into the UML model as one must name the paramter the same as the CIM name of the desired attribute. Such parameters are not important for completely standard models as the relation to the CIM attributes is fixed.  This object is required for user defined models that use attributes already existing on the PowerSystemResource or its derived classes.   Using this class avoids creating new paramter instances (with values) when we already have the values as class attributes of the associated PowerSystemResource.   Standard block models might optinally use objects of this class to convey information about the internals of the standard block.An attribute from the associated PowerSystemResource is used.   This is like reflection into the UML model as one must name the paramter the same as the CIM name of the desired attribute. Such parameters are not important for completely standard models as the relation to the CIM attributes is fixed.  This object is required for user defined models that use attributes already existing on the PowerSystemResource or its derived classes.   Using this class avoids creating new paramter instances (with values) when we already have the values as class attributes of the associated PowerSystemResource.   Standard block models might optinally use objects of this class to convey information about the internals of the standard block.
    """
    # <<< attribute_block_parameter
    # @generated
    def __init__(self, attribute_name='', **kw_args):
        """ Initialises a new 'AttributeBlockParameter' instance.
        """
        # The name of the attribute in the information model. This could be any attribute of the derived class of the power system resource for which the block is intended to be used.  For example, if the one were using the xxx attribute from Generator class, one would specifiy this attribute as 'xxx'.  This would also limit the block to only those classes which have an 'xxx' attribute.  This attribute could be replaced by using the inherited IdentifiedObject.name value for the purpose described above.The name of the attribute in the information model. This could be any attribute of the derived class of the power system resource for which the block is intended to be used.  For example, if the one were using the xxx attribute from Generator class, one would specifiy this attribute as 'xxx'.  This would also limit the block to only those classes which have an 'xxx' attribute.  This attribute could be replaced by using the inherited IdentifiedObject.name value for the purpose described above. 
        self.attribute_name = attribute_name



        super(AttributeBlockParameter, self).__init__(**kw_args)
    # >>> attribute_block_parameter


    def __str__(self):
        """ Returns a string representation of the AttributeBlockParameter.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< attribute_block_parameter.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AttributeBlockParameter.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AttributeBlockParameter", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:AttributeBlockParameter.attribute_name>%s</%s:AttributeBlockParameter.attribute_name>' % \
            (indent, ns_prefix, self.attribute_name, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "AttributeBlockParameter")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> attribute_block_parameter.serialize


class MetaBlockInput(MetaBlockConnectable):
    """ Linkage at the dynanics meta model level.    The output of a block could link to this. This is a public interface external to the block.Linkage at the dynanics meta model level.    The output of a block could link to this. This is a public interface external to the block.
    """
    pass
    # <<< meta_block_input
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'MetaBlockInput' instance.
        """


        super(MetaBlockInput, self).__init__(**kw_args)
    # >>> meta_block_input


    def __str__(self):
        """ Returns a string representation of the MetaBlockInput.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< meta_block_input.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MetaBlockInput.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MetaBlockInput", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MetaBlockInput")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> meta_block_input.serialize


class MetaBlockOutput(MetaBlockConnectable):
    """ Output state of a block.   This is a public interface external to the block.    One or more block outputs should be specified in order to link blocks together.    Certain block kinds might require a specific output.   For example, an exciter block might require an output called 'Ea'.Output state of a block.   This is a public interface external to the block.    One or more block outputs should be specified in order to link blocks together.    Certain block kinds might require a specific output.   For example, an exciter block might require an output called 'Ea'.
    """
    pass
    # <<< meta_block_output
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'MetaBlockOutput' instance.
        """


        super(MetaBlockOutput, self).__init__(**kw_args)
    # >>> meta_block_output


    def __str__(self):
        """ Returns a string representation of the MetaBlockOutput.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< meta_block_output.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MetaBlockOutput.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MetaBlockOutput", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MetaBlockOutput")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> meta_block_output.serialize


class MetaBlockParameter(MetaBlockConnectable):
    """ An identified parameter of a block.   This is meta dynamics model and does not contain specific parameter values. When using a block one would need to supply specific parameter values. These are typically time constants, but are not restricted to this.  Sometimes, for standard blocks, the block paramter may come directly from the attributes of an associated PowerSystemResource object, but such parameters may be specified to enable user defined models to alter the behavior of a standard block.An identified parameter of a block.   This is meta dynamics model and does not contain specific parameter values. When using a block one would need to supply specific parameter values. These are typically time constants, but are not restricted to this.  Sometimes, for standard blocks, the block paramter may come directly from the attributes of an associated PowerSystemResource object, but such parameters may be specified to enable user defined models to alter the behavior of a standard block.
    """
    pass
    # <<< meta_block_parameter
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'MetaBlockParameter' instance.
        """


        super(MetaBlockParameter, self).__init__(**kw_args)
    # >>> meta_block_parameter


    def __str__(self):
        """ Returns a string representation of the MetaBlockParameter.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< meta_block_parameter.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MetaBlockParameter.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MetaBlockParameter", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MetaBlockParameter")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> meta_block_parameter.serialize


class AsynchronousMachine(RotatingMachine):
    """ An asynchronous (induction) machine with no external connection to the rotor windings, e.g squirel-cage induction machine.An asynchronous (induction) machine with no external connection to the rotor windings, e.g squirel-cage induction machine.
    """
    # <<< asynchronous_machine
    # @generated
    def __init__(self, rr1=0.0, xp=0.0, tpo=0.0, xm=0.0, xs=0.0, rr2=0.0, xlr1=0.0, xlr2=0.0, tppo=0.0, xpp=0.0, **kw_args):
        """ Initialises a new 'AsynchronousMachine' instance.
        """
        # Damper 1 winding resistanceDamper 1 winding resistance 
        self.rr1 = rr1

        # Transient reactance (unsaturated) (&gt; =Xpp)Transient reactance (unsaturated) (&gt; =Xpp) 
        self.xp = xp

        # Transient rotor time constant (&gt; Tppo)Transient rotor time constant (&gt; Tppo) 
        self.tpo = tpo

        # Magnetizing reactanceMagnetizing reactance 
        self.xm = xm

        # Synchronous reactance (&gt;= Xp)Synchronous reactance (&gt;= Xp) 
        self.xs = xs

        # Damper 2 winding resistanceDamper 2 winding resistance 
        self.rr2 = rr2

        # Damper 1 winding leakage reactanceDamper 1 winding leakage reactance 
        self.xlr1 = xlr1

        # Damper 2 winding leakage reactanceDamper 2 winding leakage reactance 
        self.xlr2 = xlr2

        # Sub-transient rotor time constant (&gt; 0.)Sub-transient rotor time constant (&gt; 0.) 
        self.tppo = tppo

        # Sub-transient reactance (unsaturated) (&gt; Xl)Sub-transient reactance (unsaturated) (&gt; Xl) 
        self.xpp = xpp



        super(AsynchronousMachine, self).__init__(**kw_args)
    # >>> asynchronous_machine


    def __str__(self):
        """ Returns a string representation of the AsynchronousMachine.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< asynchronous_machine.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AsynchronousMachine.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AsynchronousMachine", self.uri)
        if format:
            indent += ' ' * depth

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
        s += '%s</%s:%s>' % (indent, ns_prefix, "AsynchronousMachine")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> asynchronous_machine.serialize


class MetaBlockState(MetaBlockConnectable):
    pass
    # <<< meta_block_state
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'MetaBlockState' instance.
        """


        super(MetaBlockState, self).__init__(**kw_args)
    # >>> meta_block_state


    def __str__(self):
        """ Returns a string representation of the MetaBlockState.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< meta_block_state.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MetaBlockState.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MetaBlockState", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MetaBlockState")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> meta_block_state.serialize


# <<< dynamics
# @generated
# >>> dynamics
