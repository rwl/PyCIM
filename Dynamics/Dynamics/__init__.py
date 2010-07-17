#------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------

""" This package models generalized dynamic models. Standard models and user defined dynamics models are included.  In some ways this duplicates the partial modeling that was done in the GenerationDynamics package, but it far exceeds that package in terms of flexibility and extensibility.   This package does not attempt to fully specficfy all possible dynamics models in specific UML, but rather builds a framework in which to exchange standard or custom dyanmics models based on 'well known' block functions.This package models generalized dynamic models. Standard models and user defined dynamics models are included.  In some ways this duplicates the partial modeling that was done in the GenerationDynamics package, but it far exceeds that package in terms of flexibility and extensibility.   This package does not attempt to fully specficfy all possible dynamics models in specific UML, but rather builds a framework in which to exchange standard or custom dyanmics models based on 'well known' block functions.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from dynamics import Element
from dynamics.Domain import ApparentPower
from dynamics.Domain import Seconds
from dynamics.Domain import Resistance
from dynamics.Domain import Reactance



from enthought.traits.api import Enum, Float, Str, Bool, Int
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


BlockKind = Enum("dotDotDot", "govenor", "automaticVoltageControl", "turbine", "exciter", "powerSystemStabilizer", "energySource")

#------------------------------------------------------------------------------
#  "RotatingMachine" class:
#------------------------------------------------------------------------------

class RotatingMachine(Element):
    """ A rotating machine which may be used as a generator or motor.A rotating machine which may be used as a generator or motor.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Nameplate apparent power rating for the unitNameplate apparent power rating for the unit
    ratedS = ApparentPower(desc="Nameplate apparent power rating for the unitNameplate apparent power rating for the unit")

    # Saturation factor at rated term. voltage (&gt;= 0.)Saturation factor at rated term. voltage (&gt;= 0.)
    s1 = Float(desc="Saturation factor at rated term. voltage (&gt;= 0.)Saturation factor at rated term. voltage (&gt;= 0.)")

    # Saturation factor at 120% of rated term.voltage (&gt;=S1)Saturation factor at 120% of rated term.voltage (&gt;=S1)
    s12 = Float(desc="Saturation factor at 120% of rated term.voltage (&gt;=S1)Saturation factor at 120% of rated term.voltage (&gt;=S1)")

    # Inertia constant of generator or motor and mechanical load (&gt;0). <b>H</b> is the stored energy in the rotating mass. For a generator, this includes the <b>generator plus all other elements (turbine, exciter) on the same shaft</b> and has units of MW-sec. For a motor, it includes the motor plus its mechanical load. Conventional units are per unit on the generator MVA base, usually expressed as MW-sec./MVA or just sec.Inertia constant of generator or motor and mechanical load (&gt;0). <b>H</b> is the stored energy in the rotating mass. For a generator, this includes the <b>generator plus all other elements (turbine, exciter) on the same shaft</b> and has units of MW-sec. For a motor, it includes the motor plus its mechanical load. Conventional units are per unit on the generator MVA base, usually expressed as MW-sec./MVA or just sec.
    h = Seconds(desc="Inertia constant of generator or motor and mechanical load (&gt;0). <b>H</b> is the stored energy in the rotating mass. For a generator, this includes the <b>generator plus all other elements (turbine, exciter) on the same shaft</b> and has units of MW-sec. For a motor, it includes the motor plus its mechanical load. Conventional units are per unit on the generator MVA base, usually expressed as MW-sec./MVA or just sec.Inertia constant of generator or motor and mechanical load (&gt;0). <b>H</b> is the stored energy in the rotating mass. For a generator, this includes the <b>generator plus all other elements (turbine, exciter) on the same shaft</b> and has units of MW-sec. For a motor, it includes the motor plus its mechanical load. Conventional units are per unit on the generator MVA base, usually expressed as MW-sec./MVA or just sec.")

    # Damping torque coefficient. <b>D</b> represents a linearized approximation of damping torque effects. This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modeled in detailDamping torque coefficient. <b>D</b> represents a linearized approximation of damping torque effects. This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modeled in detail
    d = Float(desc="Damping torque coefficient. <b>D</b> represents a linearized approximation of damping torque effects. This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modeled in detailDamping torque coefficient. <b>D</b> represents a linearized approximation of damping torque effects. This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modeled in detail")

    # Stator (armature) resistance (&gt;= 0.) - Equivalent resistance when used for GenEquiv modelStator (armature) resistance (&gt;= 0.) - Equivalent resistance when used for GenEquiv model
    rs = Resistance(desc="Stator (armature) resistance (&gt;= 0.) - Equivalent resistance when used for GenEquiv modelStator (armature) resistance (&gt;= 0.) - Equivalent resistance when used for GenEquiv model")

    # Stator leakage reactance (&gt; 0.)Stator leakage reactance (&gt; 0.)
    xls = Reactance(desc="Stator leakage reactance (&gt; 0.)Stator leakage reactance (&gt; 0.)")

    #--------------------------------------------------------------------------
    #  Begin "RotatingMachine" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "ratedS", "s1", "s12", "h", "d", "rs", "xls",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.RotatingMachine",
        title="RotatingMachine",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RotatingMachine" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MetaBlockConOutput" class:
#------------------------------------------------------------------------------

class MetaBlockConOutput(Element):
    """ If model uses MeasurementType association, it means the output is pushed back to the steady state model (if reasonable).If model uses MeasurementType association, it means the output is pushed back to the steady state model (if reasonable).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "MetaBlockConOutput" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.MetaBlockConOutput",
        title="MetaBlockConOutput",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MetaBlockConOutput" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MetaBlock" class:
#------------------------------------------------------------------------------

class MetaBlock(Element):
    """ A block is a meta-data representation of a control block.   It has an external interface and an optinal internal interface. Blocks internals can be ommitted if the block is well understood by both exchange parties.    When well understood by both partice the block can be treated as a primitive block.   All dynamic models must be defined to the level of primtive blocks in order for the model to be consumed and used for dynamic simulation. Examples of primitive blocks include a well known IEEE exciter model, a summation block, or an integrator block.A block is a meta-data representation of a control block.   It has an external interface and an optinal internal interface. Blocks internals can be ommitted if the block is well understood by both exchange parties.    When well understood by both partice the block can be treated as a primitive block.   All dynamic models must be defined to the level of primtive blocks in order for the model to be consumed and used for dynamic simulation. Examples of primitive blocks include a well known IEEE exciter model, a summation block, or an integrator block.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # This block is a proprietary block. Only inputs, outputs and parameters are exchanged.This block is a proprietary block. Only inputs, outputs and parameters are exchanged.
    proprietary = Bool(desc="This block is a proprietary block. Only inputs, outputs and parameters are exchanged.This block is a proprietary block. Only inputs, outputs and parameters are exchanged.")

    #--------------------------------------------------------------------------
    #  Begin "MetaBlock" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "proprietary",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.MetaBlock",
        title="MetaBlock",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MetaBlock" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BlockParameter" class:
#------------------------------------------------------------------------------

class BlockParameter(Element):
    """ Specification of a paramter for use in a dynamic block. This is a paramters like a time constant that could be unique for each instance of, for example, an exciter in the model.Specification of a paramter for use in a dynamic block. This is a paramters like a time constant that could be unique for each instance of, for example, an exciter in the model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The paramter value for this instance of a dynamic block usage.The paramter value for this instance of a dynamic block usage.
    value = Float(desc="The paramter value for this instance of a dynamic block usage.The paramter value for this instance of a dynamic block usage.")

    #--------------------------------------------------------------------------
    #  Begin "BlockParameter" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "value",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.BlockParameter",
        title="BlockParameter",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BlockParameter" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MetaBlockReference" class:
#------------------------------------------------------------------------------

class MetaBlockReference(Element):
    """ References a control block at the internal meta dynamics model level.    These references are contained in other blocks and reference the single instance of the meta model that defines a particular block definition. One would not expect to see bock references contained within a primitive block.References a control block at the internal meta dynamics model level.    These references are contained in other blocks and reference the single instance of the meta model that defines a particular block definition. One would not expect to see bock references contained within a primitive block.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # should be enum, initial conditions vs. simulation equationsshould be enum, initial conditions vs. simulation equations
    equationType = Int(desc="should be enum, initial conditions vs. simulation equationsshould be enum, initial conditions vs. simulation equations")

    #--------------------------------------------------------------------------
    #  Begin "MetaBlockReference" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "equationType",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.MetaBlockReference",
        title="MetaBlockReference",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MetaBlockReference" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcitationSystemLimiter" class:
#------------------------------------------------------------------------------

class ExcitationSystemLimiter(Element):
    pass
    #--------------------------------------------------------------------------
    #  Begin "ExcitationSystemLimiter" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystemLimiter",
        title="ExcitationSystemLimiter",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcitationSystemLimiter" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MetaBlockConnectivity" class:
#------------------------------------------------------------------------------

class MetaBlockConnectivity(Element):
    pass
    #--------------------------------------------------------------------------
    #  Begin "MetaBlockConnectivity" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.MetaBlockConnectivity",
        title="MetaBlockConnectivity",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MetaBlockConnectivity" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ProtectiveDevice" class:
#------------------------------------------------------------------------------

class ProtectiveDevice(Element):
    pass
    #--------------------------------------------------------------------------
    #  Begin "ProtectiveDevice" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ProtectiveDevice",
        title="ProtectiveDevice",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ProtectiveDevice" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SourceModels" class:
#------------------------------------------------------------------------------

class SourceModels(Element):
    pass
    #--------------------------------------------------------------------------
    #  Begin "SourceModels" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.SourceModels",
        title="SourceModels",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SourceModels" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MetaBlockOutputReference" class:
#------------------------------------------------------------------------------

class MetaBlockOutputReference(Element):
    pass
    #--------------------------------------------------------------------------
    #  Begin "MetaBlockOutputReference" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.MetaBlockOutputReference",
        title="MetaBlockOutputReference",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MetaBlockOutputReference" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BlockConnection" class:
#------------------------------------------------------------------------------

class BlockConnection(Element):
    """ A meta-dyanamics model connectivity specification.A meta-dyanamics model connectivity specification.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "BlockConnection" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.BlockConnection",
        title="BlockConnection",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BlockConnection" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MetaBlockConInput" class:
#------------------------------------------------------------------------------

class MetaBlockConInput(Element):
    """ If model the association to MeasurementType, the it means take the input from the associated PSR or Terminal in the static model.If model the association to MeasurementType, the it means take the input from the associated PSR or Terminal in the static model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "MetaBlockConInput" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.MetaBlockConInput",
        title="MetaBlockConInput",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MetaBlockConInput" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StaticVarDevice" class:
#------------------------------------------------------------------------------

class StaticVarDevice(Element):
    pass
    #--------------------------------------------------------------------------
    #  Begin "StaticVarDevice" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.StaticVarDevice",
        title="StaticVarDevice",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StaticVarDevice" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MetaBlockConnection" class:
#------------------------------------------------------------------------------

class MetaBlockConnection(Element):
    # Used for standard connection situations where multiple blocks of same class or same MetaBlock::blockkind have to be connected. The slotnames used are defined in the Reference Manual for Exchanging Standard Power System Dynamic Models. Application: Cross-compound or Combined Cycle connections.Used for standard connection situations where multiple blocks of same class or same MetaBlock::blockkind have to be connected. The slotnames used are defined in the Reference Manual for Exchanging Standard Power System Dynamic Models. Application: Cross-compound or Combined Cycle connections.
    slotname = Str(desc="Used for standard connection situations where multiple blocks of same class or same MetaBlock::blockkind have to be connected. The slotnames used are defined in the Reference Manual for Exchanging Standard Power System Dynamic Models. Application: Cross-compound or Combined Cycle connections.Used for standard connection situations where multiple blocks of same class or same MetaBlock::blockkind have to be connected. The slotnames used are defined in the Reference Manual for Exchanging Standard Power System Dynamic Models. Application: Cross-compound or Combined Cycle connections.")

    #--------------------------------------------------------------------------
    #  Begin "MetaBlockConnection" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "slotname",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.MetaBlockConnection",
        title="MetaBlockConnection",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MetaBlockConnection" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BlockConnectivity" class:
#------------------------------------------------------------------------------

class BlockConnectivity(Element):
    """ A instance definition of connectivity of BlockUsage objects as defined in a a BlockConnection within the dyanmics-meta-model.A instance definition of connectivity of BlockUsage objects as defined in a a BlockConnection within the dyanmics-meta-model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "BlockConnectivity" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.BlockConnectivity",
        title="BlockConnectivity",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BlockConnectivity" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MetaBlockConSignal" class:
#------------------------------------------------------------------------------

class MetaBlockConSignal(Element):
    pass
    #--------------------------------------------------------------------------
    #  Begin "MetaBlockConSignal" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.MetaBlockConSignal",
        title="MetaBlockConSignal",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MetaBlockConSignal" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Block" class:
#------------------------------------------------------------------------------

class Block(Element):
    """ A specific usage of a dynamics block, supplied with parameters and any linkages to the power system static model that are required.     Sometimes a block is used to simply specify a location of input or output from dyanmics equations to the static model.A specific usage of a dynamics block, supplied with parameters and any linkages to the power system static model that are required.     Sometimes a block is used to simply specify a location of input or output from dyanmics equations to the static model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    inService = Bool

    #--------------------------------------------------------------------------
    #  Begin "Block" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "inService",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.Block",
        title="Block",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Block" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MetaBlockStateReference" class:
#------------------------------------------------------------------------------

class MetaBlockStateReference(Element):
    pass
    #--------------------------------------------------------------------------
    #  Begin "MetaBlockStateReference" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.MetaBlockStateReference",
        title="MetaBlockStateReference",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MetaBlockStateReference" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TieToMeasurement" class:
#------------------------------------------------------------------------------

class TieToMeasurement(Element):
    """ Ties a block input to a specific state variable measurment.  Thus giving a unit type, a location in the network (typically a terminal).   A specific value is not given, just enough information to obtain the value from the model during a solution. This has nothing to do with SCADA.Ties a block input to a specific state variable measurment.  Thus giving a unit type, a location in the network (typically a terminal).   A specific value is not given, just enough information to obtain the value from the model during a solution. This has nothing to do with SCADA.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "TieToMeasurement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TieToMeasurement",
        title="TieToMeasurement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TieToMeasurement" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MetaBlockSignal" class:
#------------------------------------------------------------------------------

class MetaBlockSignal(Element):
    pass
    #--------------------------------------------------------------------------
    #  Begin "MetaBlockSignal" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.MetaBlockSignal",
        title="MetaBlockSignal",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MetaBlockSignal" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MetaBlockInputReference" class:
#------------------------------------------------------------------------------

class MetaBlockInputReference(Element):
    pass
    #--------------------------------------------------------------------------
    #  Begin "MetaBlockInputReference" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.MetaBlockInputReference",
        title="MetaBlockInputReference",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MetaBlockInputReference" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MetaBlockParameterReference" class:
#------------------------------------------------------------------------------

class MetaBlockParameterReference(Element):
    """ References a parameter of a block used in the internal representation of a block.References a parameter of a block used in the internal representation of a block.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "MetaBlockParameterReference" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.MetaBlockParameterReference",
        title="MetaBlockParameterReference",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MetaBlockParameterReference" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MetaBlockConnectable" class:
#------------------------------------------------------------------------------

class MetaBlockConnectable(Element):
    """ This is a source connection for a block input at the dynamics meta-data level.   The subtypes represent different ways to obtain the numbers.  Note that a block output is NOT derived from this class since block outputs can only be computed from references to other blocks via the BlockOutputReference class.This is a source connection for a block input at the dynamics meta-data level.   The subtypes represent different ways to obtain the numbers.  Note that a block output is NOT derived from this class since block outputs can only be computed from references to other blocks via the BlockOutputReference class.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "MetaBlockConnectable" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.MetaBlockConnectable",
        title="MetaBlockConnectable",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MetaBlockConnectable" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AttributeBlockParameter" class:
#------------------------------------------------------------------------------

class AttributeBlockParameter(MetaBlockParameter):
    """ An attribute from the associated PowerSystemResource is used.   This is like reflection into the UML model as one must name the paramter the same as the CIM name of the desired attribute. Such parameters are not important for completely standard models as the relation to the CIM attributes is fixed.  This object is required for user defined models that use attributes already existing on the PowerSystemResource or its derived classes.   Using this class avoids creating new paramter instances (with values) when we already have the values as class attributes of the associated PowerSystemResource.   Standard block models might optinally use objects of this class to convey information about the internals of the standard block.An attribute from the associated PowerSystemResource is used.   This is like reflection into the UML model as one must name the paramter the same as the CIM name of the desired attribute. Such parameters are not important for completely standard models as the relation to the CIM attributes is fixed.  This object is required for user defined models that use attributes already existing on the PowerSystemResource or its derived classes.   Using this class avoids creating new paramter instances (with values) when we already have the values as class attributes of the associated PowerSystemResource.   Standard block models might optinally use objects of this class to convey information about the internals of the standard block.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The name of the attribute in the information model. This could be any attribute of the derived class of the power system resource for which the block is intended to be used.  For example, if the one were using the xxx attribute from Generator class, one would specifiy this attribute as 'xxx'.  This would also limit the block to only those classes which have an 'xxx' attribute.  This attribute could be replaced by using the inherited IdentifiedObject.name value for the purpose described above.The name of the attribute in the information model. This could be any attribute of the derived class of the power system resource for which the block is intended to be used.  For example, if the one were using the xxx attribute from Generator class, one would specifiy this attribute as 'xxx'.  This would also limit the block to only those classes which have an 'xxx' attribute.  This attribute could be replaced by using the inherited IdentifiedObject.name value for the purpose described above.
    attributeName = Str(desc="The name of the attribute in the information model. This could be any attribute of the derived class of the power system resource for which the block is intended to be used.  For example, if the one were using the xxx attribute from Generator class, one would specifiy this attribute as 'xxx'.  This would also limit the block to only those classes which have an 'xxx' attribute.  This attribute could be replaced by using the inherited IdentifiedObject.name value for the purpose described above.The name of the attribute in the information model. This could be any attribute of the derived class of the power system resource for which the block is intended to be used.  For example, if the one were using the xxx attribute from Generator class, one would specifiy this attribute as 'xxx'.  This would also limit the block to only those classes which have an 'xxx' attribute.  This attribute could be replaced by using the inherited IdentifiedObject.name value for the purpose described above.")

    #--------------------------------------------------------------------------
    #  Begin "AttributeBlockParameter" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "attributeName",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.AttributeBlockParameter",
        title="AttributeBlockParameter",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AttributeBlockParameter" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MetaBlockInput" class:
#------------------------------------------------------------------------------

class MetaBlockInput(MetaBlockConnectable):
    """ Linkage at the dynanics meta model level.    The output of a block could link to this. This is a public interface external to the block.Linkage at the dynanics meta model level.    The output of a block could link to this. This is a public interface external to the block.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "MetaBlockInput" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.MetaBlockInput",
        title="MetaBlockInput",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MetaBlockInput" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MetaBlockOutput" class:
#------------------------------------------------------------------------------

class MetaBlockOutput(MetaBlockConnectable):
    """ Output state of a block.   This is a public interface external to the block.    One or more block outputs should be specified in order to link blocks together.    Certain block kinds might require a specific output.   For example, an exciter block might require an output called 'Ea'.Output state of a block.   This is a public interface external to the block.    One or more block outputs should be specified in order to link blocks together.    Certain block kinds might require a specific output.   For example, an exciter block might require an output called 'Ea'.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "MetaBlockOutput" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.MetaBlockOutput",
        title="MetaBlockOutput",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MetaBlockOutput" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MetaBlockParameter" class:
#------------------------------------------------------------------------------

class MetaBlockParameter(MetaBlockConnectable):
    """ An identified parameter of a block.   This is meta dynamics model and does not contain specific parameter values. When using a block one would need to supply specific parameter values. These are typically time constants, but are not restricted to this.  Sometimes, for standard blocks, the block paramter may come directly from the attributes of an associated PowerSystemResource object, but such parameters may be specified to enable user defined models to alter the behavior of a standard block.An identified parameter of a block.   This is meta dynamics model and does not contain specific parameter values. When using a block one would need to supply specific parameter values. These are typically time constants, but are not restricted to this.  Sometimes, for standard blocks, the block paramter may come directly from the attributes of an associated PowerSystemResource object, but such parameters may be specified to enable user defined models to alter the behavior of a standard block.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "MetaBlockParameter" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.MetaBlockParameter",
        title="MetaBlockParameter",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MetaBlockParameter" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AsynchronousMachine" class:
#------------------------------------------------------------------------------

class AsynchronousMachine(RotatingMachine):
    """ An asynchronous (induction) machine with no external connection to the rotor windings, e.g squirel-cage induction machine.An asynchronous (induction) machine with no external connection to the rotor windings, e.g squirel-cage induction machine.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Damper 1 winding resistanceDamper 1 winding resistance
    rr1 = Resistance(desc="Damper 1 winding resistanceDamper 1 winding resistance")

    # Transient reactance (unsaturated) (&gt; =Xpp)Transient reactance (unsaturated) (&gt; =Xpp)
    xp = Reactance(desc="Transient reactance (unsaturated) (&gt; =Xpp)Transient reactance (unsaturated) (&gt; =Xpp)")

    # Transient rotor time constant (&gt; Tppo)Transient rotor time constant (&gt; Tppo)
    tpo = Seconds(desc="Transient rotor time constant (&gt; Tppo)Transient rotor time constant (&gt; Tppo)")

    # Magnetizing reactanceMagnetizing reactance
    xm = Reactance(desc="Magnetizing reactanceMagnetizing reactance")

    # Synchronous reactance (&gt;= Xp)Synchronous reactance (&gt;= Xp)
    xs = Reactance(desc="Synchronous reactance (&gt;= Xp)Synchronous reactance (&gt;= Xp)")

    # Damper 2 winding resistanceDamper 2 winding resistance
    rr2 = Resistance(desc="Damper 2 winding resistanceDamper 2 winding resistance")

    # Damper 1 winding leakage reactanceDamper 1 winding leakage reactance
    xlr1 = Reactance(desc="Damper 1 winding leakage reactanceDamper 1 winding leakage reactance")

    # Damper 2 winding leakage reactanceDamper 2 winding leakage reactance
    xlr2 = Reactance(desc="Damper 2 winding leakage reactanceDamper 2 winding leakage reactance")

    # Sub-transient rotor time constant (&gt; 0.)Sub-transient rotor time constant (&gt; 0.)
    tppo = Seconds(desc="Sub-transient rotor time constant (&gt; 0.)Sub-transient rotor time constant (&gt; 0.)")

    # Sub-transient reactance (unsaturated) (&gt; Xl)Sub-transient reactance (unsaturated) (&gt; Xl)
    xpp = Reactance(desc="Sub-transient reactance (unsaturated) (&gt; Xl)Sub-transient reactance (unsaturated) (&gt; Xl)")

    #--------------------------------------------------------------------------
    #  Begin "AsynchronousMachine" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "ratedS", "s1", "s12", "h", "d", "rs", "xls", "rr1", "xp", "tpo", "xm", "xs", "rr2", "xlr1", "xlr2", "tppo", "xpp",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.AsynchronousMachine",
        title="AsynchronousMachine",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AsynchronousMachine" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MetaBlockState" class:
#------------------------------------------------------------------------------

class MetaBlockState(MetaBlockConnectable):
    pass
    #--------------------------------------------------------------------------
    #  Begin "MetaBlockState" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.MetaBlockState",
        title="MetaBlockState",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MetaBlockState" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
