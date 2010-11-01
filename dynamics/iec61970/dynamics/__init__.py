# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

""" This package models generalized dynamic models. Standard models and user defined dynamics models are included.  In some ways this duplicates the partial modeling that was done in the GenerationDynamics package, but it far exceeds that package in terms of flexibility and extensibility.   This package does not attempt to fully specficfy all possible dynamics models in specific UML, but rather builds a framework in which to exchange standard or custom dyanmics models based on 'well known' block functions.
"""

from dynamics import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Dynamics"

class RotatingMachine(Element):
    """ A rotating machine which may be used as a generator or motor.
    """
    # <<< rotating_machine
    # @generated
    def __init__(self, rated_s=0.0, s1=0.0, s12=0.0, h=0.0, d=0.0, rs=0.0, xls=0.0, *args, **kw_args):
        """ Initialises a new 'RotatingMachine' instance.

        @param rated_s: Nameplate apparent power rating for the unit
        @param s1: Saturation factor at rated term. voltage (&gt;= 0.)
        @param s12: Saturation factor at 120% of rated term.voltage (&gt;=S1)
        @param h: Inertia constant of generator or motor and mechanical load (&gt;0). <b>H</b> is the stored energy in the rotating mass. For a generator, this includes the <b>generator plus all other elements (turbine, exciter) on the same shaft</b> and has units of MW-sec. For a motor, it includes the motor plus its mechanical load. Conventional units are per unit on the generator MVA base, usually expressed as MW-sec./MVA or just sec.
        @param d: Damping torque coefficient. <b>D</b> represents a linearized approximation of damping torque effects. This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modeled in detail
        @param rs: Stator (armature) resistance (&gt;= 0.) - Equivalent resistance when used for GenEquiv model
        @param xls: Stator leakage reactance (&gt; 0.)
        """
        # Nameplate apparent power rating for the unit
        self.rated_s = rated_s

        # Saturation factor at rated term. voltage (&gt;= 0.)
        self.s1 = s1

        # Saturation factor at 120% of rated term.voltage (&gt;=S1)
        self.s12 = s12

        # Inertia constant of generator or motor and mechanical load (&gt;0). <b>H</b> is the stored energy in the rotating mass. For a generator, this includes the <b>generator plus all other elements (turbine, exciter) on the same shaft</b> and has units of MW-sec. For a motor, it includes the motor plus its mechanical load. Conventional units are per unit on the generator MVA base, usually expressed as MW-sec./MVA or just sec.
        self.h = h

        # Damping torque coefficient. <b>D</b> represents a linearized approximation of damping torque effects. This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modeled in detail
        self.d = d

        # Stator (armature) resistance (&gt;= 0.) - Equivalent resistance when used for GenEquiv model
        self.rs = rs

        # Stator leakage reactance (&gt; 0.)
        self.xls = xls



        super(RotatingMachine, self).__init__(*args, **kw_args)
    # >>> rotating_machine



class MetaBlockConOutput(Element):
    """ If model uses MeasurementType association, it means the output is pushed back to the steady state model (if reasonable).
    """
    pass
    # <<< meta_block_con_output
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'MetaBlockConOutput' instance.

        """


        super(MetaBlockConOutput, self).__init__(*args, **kw_args)
    # >>> meta_block_con_output



class MetaBlock(Element):
    """ A block is a meta-data representation of a control block.   It has an external interface and an optinal internal interface. Blocks internals can be ommitted if the block is well understood by both exchange parties.    When well understood by both partice the block can be treated as a primitive block.   All dynamic models must be defined to the level of primtive blocks in order for the model to be consumed and used for dynamic simulation. Examples of primitive blocks include a well known IEEE exciter model, a summation block, or an integrator block.
    """
    # <<< meta_block
    # @generated
    def __init__(self, proprietary=False, *args, **kw_args):
        """ Initialises a new 'MetaBlock' instance.

        @param proprietary: This block is a proprietary block. Only inputs, outputs and parameters are exchanged.
        """
        # This block is a proprietary block. Only inputs, outputs and parameters are exchanged.
        self.proprietary = proprietary



        super(MetaBlock, self).__init__(*args, **kw_args)
    # >>> meta_block



class BlockParameter(Element):
    """ Specification of a paramter for use in a dynamic block. This is a paramters like a time constant that could be unique for each instance of, for example, an exciter in the model.
    """
    # <<< block_parameter
    # @generated
    def __init__(self, value=0.0, *args, **kw_args):
        """ Initialises a new 'BlockParameter' instance.

        @param value: The paramter value for this instance of a dynamic block usage.
        """
        # The paramter value for this instance of a dynamic block usage.
        self.value = value



        super(BlockParameter, self).__init__(*args, **kw_args)
    # >>> block_parameter



class MetaBlockReference(Element):
    """ References a control block at the internal meta dynamics model level.    These references are contained in other blocks and reference the single instance of the meta model that defines a particular block definition. One would not expect to see bock references contained within a primitive block.
    """
    # <<< meta_block_reference
    # @generated
    def __init__(self, equation_type=0, *args, **kw_args):
        """ Initialises a new 'MetaBlockReference' instance.

        @param equation_type: should be enum, initial conditions vs. simulation equations
        """
        # should be enum, initial conditions vs. simulation equations
        self.equation_type = equation_type



        super(MetaBlockReference, self).__init__(*args, **kw_args)
    # >>> meta_block_reference



class ExcitationSystemLimiter(Element):
    pass
    # <<< excitation_system_limiter
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'ExcitationSystemLimiter' instance.

        """


        super(ExcitationSystemLimiter, self).__init__(*args, **kw_args)
    # >>> excitation_system_limiter



class MetaBlockConnectivity(Element):
    pass
    # <<< meta_block_connectivity
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'MetaBlockConnectivity' instance.

        """


        super(MetaBlockConnectivity, self).__init__(*args, **kw_args)
    # >>> meta_block_connectivity



class ProtectiveDevice(Element):
    pass
    # <<< protective_device
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'ProtectiveDevice' instance.

        """


        super(ProtectiveDevice, self).__init__(*args, **kw_args)
    # >>> protective_device



class SourceModels(Element):
    pass
    # <<< source_models
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'SourceModels' instance.

        """


        super(SourceModels, self).__init__(*args, **kw_args)
    # >>> source_models



class MetaBlockOutputReference(Element):
    pass
    # <<< meta_block_output_reference
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'MetaBlockOutputReference' instance.

        """


        super(MetaBlockOutputReference, self).__init__(*args, **kw_args)
    # >>> meta_block_output_reference



class BlockConnection(Element):
    """ A meta-dyanamics model connectivity specification.
    """
    pass
    # <<< block_connection
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'BlockConnection' instance.

        """


        super(BlockConnection, self).__init__(*args, **kw_args)
    # >>> block_connection



class MetaBlockConInput(Element):
    """ If model the association to MeasurementType, the it means take the input from the associated PSR or Terminal in the static model.
    """
    pass
    # <<< meta_block_con_input
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'MetaBlockConInput' instance.

        """


        super(MetaBlockConInput, self).__init__(*args, **kw_args)
    # >>> meta_block_con_input



class StaticVarDevice(Element):
    pass
    # <<< static_var_device
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'StaticVarDevice' instance.

        """


        super(StaticVarDevice, self).__init__(*args, **kw_args)
    # >>> static_var_device



class MetaBlockConnection(Element):
    # <<< meta_block_connection
    # @generated
    def __init__(self, slotname='', *args, **kw_args):
        """ Initialises a new 'MetaBlockConnection' instance.

        @param slotname: Used for standard connection situations where multiple blocks of same class or same MetaBlock::blockkind have to be connected. The slotnames used are defined in the Reference Manual for Exchanging Standard Power System Dynamic Models. Application: Cross-compound or Combined Cycle connections.
        """
        # Used for standard connection situations where multiple blocks of same class or same MetaBlock::blockkind have to be connected. The slotnames used are defined in the Reference Manual for Exchanging Standard Power System Dynamic Models. Application: Cross-compound or Combined Cycle connections.
        self.slotname = slotname



        super(MetaBlockConnection, self).__init__(*args, **kw_args)
    # >>> meta_block_connection



class BlockConnectivity(Element):
    """ A instance definition of connectivity of BlockUsage objects as defined in a a BlockConnection within the dyanmics-meta-model.
    """
    pass
    # <<< block_connectivity
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'BlockConnectivity' instance.

        """


        super(BlockConnectivity, self).__init__(*args, **kw_args)
    # >>> block_connectivity



class MetaBlockConSignal(Element):
    pass
    # <<< meta_block_con_signal
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'MetaBlockConSignal' instance.

        """


        super(MetaBlockConSignal, self).__init__(*args, **kw_args)
    # >>> meta_block_con_signal



class Block(Element):
    """ A specific usage of a dynamics block, supplied with parameters and any linkages to the power system static model that are required.     Sometimes a block is used to simply specify a location of input or output from dyanmics equations to the static model.
    """
    # <<< block
    # @generated
    def __init__(self, in_service=False, *args, **kw_args):
        """ Initialises a new 'Block' instance.

        @param in_service:
        """

        self.in_service = in_service



        super(Block, self).__init__(*args, **kw_args)
    # >>> block



class MetaBlockStateReference(Element):
    pass
    # <<< meta_block_state_reference
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'MetaBlockStateReference' instance.

        """


        super(MetaBlockStateReference, self).__init__(*args, **kw_args)
    # >>> meta_block_state_reference



class TieToMeasurement(Element):
    """ Ties a block input to a specific state variable measurment.  Thus giving a unit type, a location in the network (typically a terminal).   A specific value is not given, just enough information to obtain the value from the model during a solution. This has nothing to do with SCADA.
    """
    pass
    # <<< tie_to_measurement
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'TieToMeasurement' instance.

        """


        super(TieToMeasurement, self).__init__(*args, **kw_args)
    # >>> tie_to_measurement



class MetaBlockSignal(Element):
    pass
    # <<< meta_block_signal
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'MetaBlockSignal' instance.

        """


        super(MetaBlockSignal, self).__init__(*args, **kw_args)
    # >>> meta_block_signal



class MetaBlockInputReference(Element):
    pass
    # <<< meta_block_input_reference
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'MetaBlockInputReference' instance.

        """


        super(MetaBlockInputReference, self).__init__(*args, **kw_args)
    # >>> meta_block_input_reference



class MetaBlockParameterReference(Element):
    """ References a parameter of a block used in the internal representation of a block.
    """
    pass
    # <<< meta_block_parameter_reference
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'MetaBlockParameterReference' instance.

        """


        super(MetaBlockParameterReference, self).__init__(*args, **kw_args)
    # >>> meta_block_parameter_reference



class MetaBlockConnectable(Element):
    """ This is a source connection for a block input at the dynamics meta-data level.   The subtypes represent different ways to obtain the numbers.  Note that a block output is NOT derived from this class since block outputs can only be computed from references to other blocks via the BlockOutputReference class.
    """
    pass
    # <<< meta_block_connectable
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'MetaBlockConnectable' instance.

        """


        super(MetaBlockConnectable, self).__init__(*args, **kw_args)
    # >>> meta_block_connectable



class MetaBlockInput(MetaBlockConnectable):
    """ Linkage at the dynanics meta model level.    The output of a block could link to this. This is a public interface external to the block.
    """
    pass
    # <<< meta_block_input
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'MetaBlockInput' instance.

        """


        super(MetaBlockInput, self).__init__(*args, **kw_args)
    # >>> meta_block_input



class MetaBlockOutput(MetaBlockConnectable):
    """ Output state of a block.   This is a public interface external to the block.    One or more block outputs should be specified in order to link blocks together.    Certain block kinds might require a specific output.   For example, an exciter block might require an output called 'Ea'.
    """
    pass
    # <<< meta_block_output
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'MetaBlockOutput' instance.

        """


        super(MetaBlockOutput, self).__init__(*args, **kw_args)
    # >>> meta_block_output



class MetaBlockParameter(MetaBlockConnectable):
    """ An identified parameter of a block.   This is meta dynamics model and does not contain specific parameter values. When using a block one would need to supply specific parameter values. These are typically time constants, but are not restricted to this.  Sometimes, for standard blocks, the block paramter may come directly from the attributes of an associated PowerSystemResource object, but such parameters may be specified to enable user defined models to alter the behavior of a standard block.
    """
    pass
    # <<< meta_block_parameter
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'MetaBlockParameter' instance.

        """


        super(MetaBlockParameter, self).__init__(*args, **kw_args)
    # >>> meta_block_parameter



class AttributeBlockParameter(MetaBlockParameter):
    """ An attribute from the associated PowerSystemResource is used.   This is like reflection into the UML model as one must name the paramter the same as the CIM name of the desired attribute. Such parameters are not important for completely standard models as the relation to the CIM attributes is fixed.  This object is required for user defined models that use attributes already existing on the PowerSystemResource or its derived classes.   Using this class avoids creating new paramter instances (with values) when we already have the values as class attributes of the associated PowerSystemResource.   Standard block models might optinally use objects of this class to convey information about the internals of the standard block.
    """
    # <<< attribute_block_parameter
    # @generated
    def __init__(self, attribute_name='', *args, **kw_args):
        """ Initialises a new 'AttributeBlockParameter' instance.

        @param attribute_name: The name of the attribute in the information model. This could be any attribute of the derived class of the power system resource for which the block is intended to be used.  For example, if the one were using the xxx attribute from Generator class, one would specifiy this attribute as 'xxx'.  This would also limit the block to only those classes which have an 'xxx' attribute.  This attribute could be replaced by using the inherited IdentifiedObject.name value for the purpose described above.
        """
        # The name of the attribute in the information model. This could be any attribute of the derived class of the power system resource for which the block is intended to be used.  For example, if the one were using the xxx attribute from Generator class, one would specifiy this attribute as 'xxx'.  This would also limit the block to only those classes which have an 'xxx' attribute.  This attribute could be replaced by using the inherited IdentifiedObject.name value for the purpose described above.
        self.attribute_name = attribute_name



        super(AttributeBlockParameter, self).__init__(*args, **kw_args)
    # >>> attribute_block_parameter



class AsynchronousMachine(RotatingMachine):
    """ An asynchronous (induction) machine with no external connection to the rotor windings, e.g squirel-cage induction machine.
    """
    # <<< asynchronous_machine
    # @generated
    def __init__(self, rr1=0.0, xp=0.0, tpo=0.0, xm=0.0, xs=0.0, rr2=0.0, xlr1=0.0, xlr2=0.0, tppo=0.0, xpp=0.0, *args, **kw_args):
        """ Initialises a new 'AsynchronousMachine' instance.

        @param rr1: Damper 1 winding resistance
        @param xp: Transient reactance (unsaturated) (&gt; =Xpp)
        @param tpo: Transient rotor time constant (&gt; Tppo)
        @param xm: Magnetizing reactance
        @param xs: Synchronous reactance (&gt;= Xp)
        @param rr2: Damper 2 winding resistance
        @param xlr1: Damper 1 winding leakage reactance
        @param xlr2: Damper 2 winding leakage reactance
        @param tppo: Sub-transient rotor time constant (&gt; 0.)
        @param xpp: Sub-transient reactance (unsaturated) (&gt; Xl)
        """
        # Damper 1 winding resistance
        self.rr1 = rr1

        # Transient reactance (unsaturated) (&gt; =Xpp)
        self.xp = xp

        # Transient rotor time constant (&gt; Tppo)
        self.tpo = tpo

        # Magnetizing reactance
        self.xm = xm

        # Synchronous reactance (&gt;= Xp)
        self.xs = xs

        # Damper 2 winding resistance
        self.rr2 = rr2

        # Damper 1 winding leakage reactance
        self.xlr1 = xlr1

        # Damper 2 winding leakage reactance
        self.xlr2 = xlr2

        # Sub-transient rotor time constant (&gt; 0.)
        self.tppo = tppo

        # Sub-transient reactance (unsaturated) (&gt; Xl)
        self.xpp = xpp



        super(AsynchronousMachine, self).__init__(*args, **kw_args)
    # >>> asynchronous_machine



class MetaBlockState(MetaBlockConnectable):
    pass
    # <<< meta_block_state
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'MetaBlockState' instance.

        """


        super(MetaBlockState, self).__init__(*args, **kw_args)
    # >>> meta_block_state



# <<< dynamics
# @generated
# >>> dynamics
