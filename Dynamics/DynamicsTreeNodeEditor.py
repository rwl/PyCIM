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

""" Defines TreeNodes interface for the model.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api \
    import HasTraits, Str, Property, Instance

from enthought.traits.ui.api \
    import View, Item, Group, TreeEditor, TreeNode

from enthought.traits.ui.menu \
    import Action, Menu

from Dynamics import *
from Dynamics.IEC61970 import *
from Dynamics.IEC61970.Dynamics import *
from Dynamics.IEC61970.Domain import *
from Dynamics.IEC61970.Dynamics.Loads import *
from Dynamics.IEC61970.Dynamics.ExcitationSystems import *
from Dynamics.IEC61970.Dynamics.TurbineGovernors import *
from Dynamics.IEC61970.Dynamics.PowerSystemStabilizers import *
from Dynamics.IEC61970.Dynamics.Generators import *
from Dynamics.IEC61970.Dynamics.VoltageCompensator import *
from Dynamics.IEC61970.Dynamics.Motors import *

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------
# <<< constants
# @generated
IMAGE_PATH = ""
# >>> constants

#------------------------------------------------------------------------------
#  Tree nodes:
#------------------------------------------------------------------------------

Element_TreeNode = TreeNode(
    node_for=[Element],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Model_TreeNode = TreeNode(
    node_for=[Model],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Model_Elements_TreeNode = TreeNode(
    node_for=[Model],
    children="Elements",
    label="=Elements",
    tooltip="",
    add=[Element],
    move=[Element],
    icon_path=IMAGE_PATH)

RotatingMachine_TreeNode = TreeNode(
    node_for=[RotatingMachine],
        tooltip="A rotating machine which may be used as a generator or motor.A rotating machine which may be used as a generator or motor.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MetaBlockConOutput_TreeNode = TreeNode(
    node_for=[MetaBlockConOutput],
        tooltip="If model uses MeasurementType association, it means the output is pushed back to the steady state model (if reasonable).If model uses MeasurementType association, it means the output is pushed back to the steady state model (if reasonable).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


AttributeBlockParameter_TreeNode = TreeNode(
    node_for=[AttributeBlockParameter],
        tooltip="An attribute from the associated PowerSystemResource is used.   This is like reflection into the UML model as one must name the paramter the same as the CIM name of the desired attribute. Such parameters are not important for completely standard models as the relation to the CIM attributes is fixed.  This object is required for user defined models that use attributes already existing on the PowerSystemResource or its derived classes.   Using this class avoids creating new paramter instances (with values) when we already have the values as class attributes of the associated PowerSystemResource.   Standard block models might optinally use objects of this class to convey information about the internals of the standard block.An attribute from the associated PowerSystemResource is used.   This is like reflection into the UML model as one must name the paramter the same as the CIM name of the desired attribute. Such parameters are not important for completely standard models as the relation to the CIM attributes is fixed.  This object is required for user defined models that use attributes already existing on the PowerSystemResource or its derived classes.   Using this class avoids creating new paramter instances (with values) when we already have the values as class attributes of the associated PowerSystemResource.   Standard block models might optinally use objects of this class to convey information about the internals of the standard block.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MetaBlock_TreeNode = TreeNode(
    node_for=[MetaBlock],
        tooltip="A block is a meta-data representation of a control block.   It has an external interface and an optinal internal interface. Blocks internals can be ommitted if the block is well understood by both exchange parties.    When well understood by both partice the block can be treated as a primitive block.   All dynamic models must be defined to the level of primtive blocks in order for the model to be consumed and used for dynamic simulation. Examples of primitive blocks include a well known IEEE exciter model, a summation block, or an integrator block.A block is a meta-data representation of a control block.   It has an external interface and an optinal internal interface. Blocks internals can be ommitted if the block is well understood by both exchange parties.    When well understood by both partice the block can be treated as a primitive block.   All dynamic models must be defined to the level of primtive blocks in order for the model to be consumed and used for dynamic simulation. Examples of primitive blocks include a well known IEEE exciter model, a summation block, or an integrator block.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


BlockParameter_TreeNode = TreeNode(
    node_for=[BlockParameter],
        tooltip="Specification of a paramter for use in a dynamic block. This is a paramters like a time constant that could be unique for each instance of, for example, an exciter in the model.Specification of a paramter for use in a dynamic block. This is a paramters like a time constant that could be unique for each instance of, for example, an exciter in the model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MetaBlockReference_TreeNode = TreeNode(
    node_for=[MetaBlockReference],
        tooltip="References a control block at the internal meta Dynamics model level.    These references are contained in other blocks and reference the single instance of the meta model that defines a particular block definition. One would not expect to see bock references contained within a primitive block.References a control block at the internal meta Dynamics model level.    These references are contained in other blocks and reference the single instance of the meta model that defines a particular block definition. One would not expect to see bock references contained within a primitive block.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcitationSystemLimiter_TreeNode = TreeNode(
    node_for=[ExcitationSystemLimiter],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MetaBlockConnectivity_TreeNode = TreeNode(
    node_for=[MetaBlockConnectivity],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ProtectiveDevice_TreeNode = TreeNode(
    node_for=[ProtectiveDevice],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MetaBlockInput_TreeNode = TreeNode(
    node_for=[MetaBlockInput],
        tooltip="Linkage at the dynanics meta model level.    The output of a block could link to this. This is a public interface external to the block.Linkage at the dynanics meta model level.    The output of a block could link to this. This is a public interface external to the block.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SourceModels_TreeNode = TreeNode(
    node_for=[SourceModels],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MetaBlockOutputReference_TreeNode = TreeNode(
    node_for=[MetaBlockOutputReference],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MetaBlockOutput_TreeNode = TreeNode(
    node_for=[MetaBlockOutput],
        tooltip="Output state of a block.   This is a public interface external to the block.    One or more block outputs should be specified in order to link blocks together.    Certain block kinds might require a specific output.   For example, an exciter block might require an output called 'Ea'.Output state of a block.   This is a public interface external to the block.    One or more block outputs should be specified in order to link blocks together.    Certain block kinds might require a specific output.   For example, an exciter block might require an output called 'Ea'.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MetaBlockParameter_TreeNode = TreeNode(
    node_for=[MetaBlockParameter],
        tooltip="An identified parameter of a block.   This is meta Dynamics model and does not contain specific parameter values. When using a block one would need to supply specific parameter values. These are typically time constants, but are not restricted to this.  Sometimes, for standard blocks, the block paramter may come directly from the attributes of an associated PowerSystemResource object, but such parameters may be specified to enable user defined models to alter the behavior of a standard block.An identified parameter of a block.   This is meta Dynamics model and does not contain specific parameter values. When using a block one would need to supply specific parameter values. These are typically time constants, but are not restricted to this.  Sometimes, for standard blocks, the block paramter may come directly from the attributes of an associated PowerSystemResource object, but such parameters may be specified to enable user defined models to alter the behavior of a standard block.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


BlockConnection_TreeNode = TreeNode(
    node_for=[BlockConnection],
        tooltip="A meta-dyanamics model connectivity specification.A meta-dyanamics model connectivity specification.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MetaBlockConInput_TreeNode = TreeNode(
    node_for=[MetaBlockConInput],
        tooltip="If model the association to MeasurementType, the it means take the input from the associated PSR or Terminal in the static model.If model the association to MeasurementType, the it means take the input from the associated PSR or Terminal in the static model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


StaticVarDevice_TreeNode = TreeNode(
    node_for=[StaticVarDevice],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MetaBlockConnection_TreeNode = TreeNode(
    node_for=[MetaBlockConnection],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


BlockConnectivity_TreeNode = TreeNode(
    node_for=[BlockConnectivity],
        tooltip="A instance definition of connectivity of BlockUsage objects as defined in a a BlockConnection within the dyanmics-meta-model.A instance definition of connectivity of BlockUsage objects as defined in a a BlockConnection within the dyanmics-meta-model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MetaBlockConSignal_TreeNode = TreeNode(
    node_for=[MetaBlockConSignal],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Block_TreeNode = TreeNode(
    node_for=[Block],
        tooltip="A specific usage of a Dynamics block, supplied with parameters and any linkages to the power system static model that are required.     Sometimes a block is used to simply specify a location of input or output from dyanmics equations to the static model.A specific usage of a Dynamics block, supplied with parameters and any linkages to the power system static model that are required.     Sometimes a block is used to simply specify a location of input or output from dyanmics equations to the static model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MetaBlockStateReference_TreeNode = TreeNode(
    node_for=[MetaBlockStateReference],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


AsynchronousMachine_TreeNode = TreeNode(
    node_for=[AsynchronousMachine],
        tooltip="An asynchronous (induction) machine with no external connection to the rotor windings, e.g squirel-cage induction machine.An asynchronous (induction) machine with no external connection to the rotor windings, e.g squirel-cage induction machine.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TieToMeasurement_TreeNode = TreeNode(
    node_for=[TieToMeasurement],
        tooltip="Ties a block input to a specific state variable measurment.  Thus giving a unit type, a location in the network (typically a terminal).   A specific value is not given, just enough information to obtain the value from the model during a solution. This has nothing to do with SCADA.Ties a block input to a specific state variable measurment.  Thus giving a unit type, a location in the network (typically a terminal).   A specific value is not given, just enough information to obtain the value from the model during a solution. This has nothing to do with SCADA.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MetaBlockSignal_TreeNode = TreeNode(
    node_for=[MetaBlockSignal],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MetaBlockInputReference_TreeNode = TreeNode(
    node_for=[MetaBlockInputReference],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MetaBlockParameterReference_TreeNode = TreeNode(
    node_for=[MetaBlockParameterReference],
        tooltip="References a parameter of a block used in the internal representation of a block.References a parameter of a block used in the internal representation of a block.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MetaBlockConnectable_TreeNode = TreeNode(
    node_for=[MetaBlockConnectable],
        tooltip="This is a source connection for a block input at the Dynamics meta-data level.   The subtypes represent different ways to obtain the numbers.  Note that a block output is NOT derived from this class since block outputs can only be computed from references to other blocks via the BlockOutputReference class.This is a source connection for a block input at the Dynamics meta-data level.   The subtypes represent different ways to obtain the numbers.  Note that a block output is NOT derived from this class since block outputs can only be computed from references to other blocks via the BlockOutputReference class.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MetaBlockState_TreeNode = TreeNode(
    node_for=[MetaBlockState],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LoadStaticSystem_TreeNode = TreeNode(
    node_for=[LoadStaticSystem],
        tooltip="Static load associated with a specific system.Static load associated with a specific system.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LoadStaticOwner_TreeNode = TreeNode(
    node_for=[LoadStaticOwner],
        tooltip="Static load associated with a single owner.Static load associated with a single owner.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LoadStatic_TreeNode = TreeNode(
    node_for=[LoadStatic],
        tooltip="General Static Load Model. A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage.General Static Load Model. A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


AggregateLoad_TreeNode = TreeNode(
    node_for=[AggregateLoad],
        tooltip="Aggregate loads are used to represent all or part of the real and reactive load from a load in the static (power flow) data. This load is usually the aggregation of many individual load devices. The load models are approximate representation of the aggregate response of the load devices to system disturbances.   Models of loads for dynamic analysis may themselves be either static or dynamic. A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage. A dynamic load model can used to represent the aggregate response of the motor components of the load.   Large industrial motors or groups of similar motors may be represented by individual motor models (synchronous or asynchronous) which are usually represented as generators with negative Pgen in the static (power flow) data.Aggregate loads are used to represent all or part of the real and reactive load from a load in the static (power flow) data. This load is usually the aggregation of many individual load devices. The load models are approximate representation of the aggregate response of the load devices to system disturbances.   Models of loads for dynamic analysis may themselves be either static or dynamic. A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage. A dynamic load model can used to represent the aggregate response of the motor components of the load.   Large industrial motors or groups of similar motors may be represented by individual motor models (synchronous or asynchronous) which are usually represented as generators with negative Pgen in the static (power flow) data.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LoadMotor_TreeNode = TreeNode(
    node_for=[LoadMotor],
        tooltip="Aggregate induction motor load. This model  is used to represent a fraction of an ordinary load as 'induction motor load'.  It allows load that is treated as ordinary constant power in power flow analysis to be represented by an induction motor in dynamic simulation.  Either a 'one-cage' or 'two-cage' model of the induction machine can be modeled.  Magnetic saturation is not modeled.  This model is intended for representation of aggregations of many motors dispersed through a load represented at a high voltage bus but where there is no information on the characteristics of individual motors.Aggregate induction motor load. This model  is used to represent a fraction of an ordinary load as 'induction motor load'.  It allows load that is treated as ordinary constant power in power flow analysis to be represented by an induction motor in dynamic simulation.  Either a 'one-cage' or 'two-cage' model of the induction machine can be modeled.  Magnetic saturation is not modeled.  This model is intended for representation of aggregations of many motors dispersed through a load represented at a high voltage bus but where there is no information on the characteristics of individual motors.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LoadStaticBus_TreeNode = TreeNode(
    node_for=[LoadStaticBus],
        tooltip="Static load model associated with a single bus.Static load model associated with a single bus.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LoadStaticZone_TreeNode = TreeNode(
    node_for=[LoadStaticZone],
        tooltip="Static load associated with a zone.Static load associated with a zone.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LoadStaticArea_TreeNode = TreeNode(
    node_for=[LoadStaticArea],
        tooltip="Static load associated with an Area.Static load associated with an Area.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcBAS_TreeNode = TreeNode(
    node_for=[ExcBAS],
        tooltip="Basler static voltage regulator feeding dc or ac rotating exciter modelBasler static voltage regulator feeding dc or ac rotating exciter model",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcDC2A_TreeNode = TreeNode(
    node_for=[ExcDC2A],
        tooltip="IEEE (1992/2005) DC2A Model  The model is used to represent field-controlled dc commutator exciters with continuously acting voltage regulators having supplies obtained from the generator or auxiliary bus. It differs from the Type DC1A model only in the voltage regulator output limits, which are now proportional to terminal voltage <i>V</i><i><sub>T</sub></i>. It is representative of solid-state replacements for various forms of older mechanical and rotating amplifier regulating equipment connected to dc commutator exciters.IEEE (1992/2005) DC2A Model  The model is used to represent field-controlled dc commutator exciters with continuously acting voltage regulators having supplies obtained from the generator or auxiliary bus. It differs from the Type DC1A model only in the voltage regulator output limits, which are now proportional to terminal voltage <i>V</i><i><sub>T</sub></i>. It is representative of solid-state replacements for various forms of older mechanical and rotating amplifier regulating equipment connected to dc commutator exciters.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcSEXS_TreeNode = TreeNode(
    node_for=[ExcSEXS],
        tooltip="Simplified Excitation System ModelSimplified Excitation System Model",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcELIN2_TreeNode = TreeNode(
    node_for=[ExcELIN2],
        tooltip="Detailed Excitation System Model - ELIN (VATECH)Detailed Excitation System Model - ELIN (VATECH)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcAC4A_TreeNode = TreeNode(
    node_for=[ExcAC4A],
        tooltip="IEEE (1992/2005) AC4A Model  The Type AC4A alternator-supplied controlled-rectifier excitation system is quite different from the other type ac systems. This high initial response excitation system utilizes a full thyristor bridge in the exciter output circuit. The voltage regulator controls the firing of the thyristor bridges. The exciter alternator uses an independent voltage regulator to control its output voltage to a constant value. These effects are not modeled; however, transient loading effects on the exciter alternator are included.IEEE (1992/2005) AC4A Model  The Type AC4A alternator-supplied controlled-rectifier excitation system is quite different from the other type ac systems. This high initial response excitation system utilizes a full thyristor bridge in the exciter output circuit. The voltage regulator controls the firing of the thyristor bridges. The exciter alternator uses an independent voltage regulator to control its output voltage to a constant value. These effects are not modeled; however, transient loading effects on the exciter alternator are included.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcSK_TreeNode = TreeNode(
    node_for=[ExcSK],
        tooltip="Slovakian Excitation System Model (UEL, secondary voltage control)Slovakian Excitation System Model (UEL, secondary voltage control)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcAC2A_TreeNode = TreeNode(
    node_for=[ExcAC2A],
        tooltip="IEEE (1992/2005) AC2A Model The model designated as Type AC2A, represents a high initial response fieldcontrolled alternator-rectifier excitation system. The alternator main exciter is used with non-controlled rectifiers. The Type AC2A model is similar to that of Type AC1A except for the inclusion of exciter time constant compensation and exciter field current limiting elements.IEEE (1992/2005) AC2A Model The model designated as Type AC2A, represents a high initial response fieldcontrolled alternator-rectifier excitation system. The alternator main exciter is used with non-controlled rectifiers. The Type AC2A model is similar to that of Type AC1A except for the inclusion of exciter time constant compensation and exciter field current limiting elements.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcELIN1_TreeNode = TreeNode(
    node_for=[ExcELIN1],
        tooltip="Simplified Excitation System Model - ELIN (VATECH)Simplified Excitation System Model - ELIN (VATECH)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcST6B_TreeNode = TreeNode(
    node_for=[ExcST6B],
        tooltip="IEEE (2005) ST6B Model  The AVR consists of a PI voltage regulator with an inner loop field voltage regulator and pre-control. The field voltage regulator implements a proportional control. The pre-control and the delay in the feedback circuit increase the dynamic response.IEEE (2005) ST6B Model  The AVR consists of a PI voltage regulator with an inner loop field voltage regulator and pre-control. The field voltage regulator implements a proportional control. The pre-control and the delay in the feedback circuit increase the dynamic response.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcST4B_TreeNode = TreeNode(
    node_for=[ExcST4B],
        tooltip="IEEE (2005) ST4B Model  This model is a variation of the Type ST3A model, with a proportional plus integral (PI) regulator block replacing the lag-lead regulator characteristic that was in the ST3A model. Both potential- and compoundsource rectifier excitation systems are modeled. The PI regulator blocks have nonwindup limits that are represented. The voltage regulator of this model is typically implemented digitally.IEEE (2005) ST4B Model  This model is a variation of the Type ST3A model, with a proportional plus integral (PI) regulator block replacing the lag-lead regulator characteristic that was in the ST3A model. Both potential- and compoundsource rectifier excitation systems are modeled. The PI regulator blocks have nonwindup limits that are represented. The voltage regulator of this model is typically implemented digitally.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcWT3E_TreeNode = TreeNode(
    node_for=[ExcWT3E],
        tooltip="Type 3 standard wind turbine converter control modelType 3 standard wind turbine converter control model",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcPIC_TreeNode = TreeNode(
    node_for=[ExcPIC],
        tooltip="Excitation System Model with PI voltage regulatorExcitation System Model with PI voltage regulator",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcSK2_TreeNode = TreeNode(
    node_for=[ExcSK2],
        tooltip="Slovakian alternator-rectifier Excitation System Model (UEL, secondary voltage control)Slovakian alternator-rectifier Excitation System Model (UEL, secondary voltage control)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcST2A_TreeNode = TreeNode(
    node_for=[ExcST2A],
        tooltip="IEEE (1992/2005) ST2A Model  Some static systems utilize both current and voltage sources (generator terminal quantities) to comprise the power source. These compound-source rectifier excitation systems are designated Type ST2A. The regulator controls the exciter output through controlled saturation of the power transformer components.IEEE (1992/2005) ST2A Model  Some static systems utilize both current and voltage sources (generator terminal quantities) to comprise the power source. These compound-source rectifier excitation systems are designated Type ST2A. The regulator controls the exciter output through controlled saturation of the power transformer components.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcHU_TreeNode = TreeNode(
    node_for=[ExcHU],
        tooltip="Hungarian Excitation System ModelHungarian Excitation System Model",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcREXS_TreeNode = TreeNode(
    node_for=[ExcREXS],
        tooltip="General Purpose Rotating Excitation System ModelGeneral Purpose Rotating Excitation System Model",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcST7B_TreeNode = TreeNode(
    node_for=[ExcST7B],
        tooltip="IEEE (2005) ST7B Model  The model ST7B is representative of static potential-source excitation systems. In this system, the AVR consists of a PI voltage regulator. A phase lead-lag filter in series allows introduction of a derivative function, typically used with brushless excitation systems. In that case, the regulator is of the PID type. In addition, the terminal voltage channel includes a phase lead-lag filter. The AVR includes the appropriate inputs on its reference for overexcitation limiter (OEL1), underexcitation limiter (UEL), stator current limiter (SCL), and current compensator (DROOP). All these limitations, when they work at voltage reference level, keep the PSS (VS signal from Type PSS1A, PSS2A, or PSS2B) in operation. However, the UEL limitation can also be transferred to the high value (HV) gate acting on the output signal. In addition, the output signal passes through a low value (LV) gate for a ceiling overexcitation limiter (OEL2).IEEE (2005) ST7B Model  The model ST7B is representative of static potential-source excitation systems. In this system, the AVR consists of a PI voltage regulator. A phase lead-lag filter in series allows introduction of a derivative function, typically used with brushless excitation systems. In that case, the regulator is of the PID type. In addition, the terminal voltage channel includes a phase lead-lag filter. The AVR includes the appropriate inputs on its reference for overexcitation limiter (OEL1), underexcitation limiter (UEL), stator current limiter (SCL), and current compensator (DROOP). All these limitations, when they work at voltage reference level, keep the PSS (VS signal from Type PSS1A, PSS2A, or PSS2B) in operation. However, the UEL limitation can also be transferred to the high value (HV) gate acting on the output signal. In addition, the output signal passes through a low value (LV) gate for a ceiling overexcitation limiter (OEL2).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcAC1A_TreeNode = TreeNode(
    node_for=[ExcAC1A],
        tooltip="IEEE (1992/2005) AC1A Model The model represents the field-controlled alternator-rectifier excitation systems designated Type AC1A. These excitation systems consist of an alternator main exciter with non-controlled rectifiers.IEEE (1992/2005) AC1A Model The model represents the field-controlled alternator-rectifier excitation systems designated Type AC1A. These excitation systems consist of an alternator main exciter with non-controlled rectifiers.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcDC4B_TreeNode = TreeNode(
    node_for=[ExcDC4B],
        tooltip="IEEE (2005) DC4B Model  These excitation systems utilize a field-controlled dc commutator exciter with a continuously acting voltage regulator having supplies obtained from the generator or auxiliary bus. The replacement of the controls only as an upgrade (retaining the dc commutator exciter) has resulted in a new model. This excitation system typically includes a proportional, integral, and differential (PID) generator voltage regulator (AVR). An alternative rate feedback loop (<i>kf</i>, <i>tf</i>) for stabilization is also shown in the model if the AVR does not include a derivative term. If a PSS control is supplied, the appropriate model is the Type PSS2B model.IEEE (2005) DC4B Model  These excitation systems utilize a field-controlled dc commutator exciter with a continuously acting voltage regulator having supplies obtained from the generator or auxiliary bus. The replacement of the controls only as an upgrade (retaining the dc commutator exciter) has resulted in a new model. This excitation system typically includes a proportional, integral, and differential (PID) generator voltage regulator (AVR). An alternative rate feedback loop (<i>kf</i>, <i>tf</i>) for stabilization is also shown in the model if the AVR does not include a derivative term. If a PSS control is supplied, the appropriate model is the Type PSS2B model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcDC1A_TreeNode = TreeNode(
    node_for=[ExcDC1A],
        tooltip="IEEE (1992/2005) DC1A Model  This model is used to represent field-controlled dc commutator exciters with continuously acting voltage regulators (especially the direct-acting rheostatic, rotating amplifier, and magnetic amplifier types). Because this model has been widely implemented by the industry, it is sometimes used to represent other types of systems when detailed data for them are not available or when a simplified model is required.IEEE (1992/2005) DC1A Model  This model is used to represent field-controlled dc commutator exciters with continuously acting voltage regulators (especially the direct-acting rheostatic, rotating amplifier, and magnetic amplifier types). Because this model has been widely implemented by the industry, it is sometimes used to represent other types of systems when detailed data for them are not available or when a simplified model is required.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcAC3A_TreeNode = TreeNode(
    node_for=[ExcAC3A],
        tooltip="IEEE (1992/2005) AC3A Model  The model represents the field-controlled alternator-rectifier excitation systems designated Type AC3A. These excitation systems include an alternator main exciter with non-controlled rectifiers. The exciter employs self-excitation, and the voltage regulator power is derived from the exciter output voltage. Therefore, this system has an additional nonlinearity, simulated by the use of a multiplier whose inputs are the voltage regulator command signal, <i>VA</i>, and the exciter output voltage, <i>EFD</i>, times <i>KR</i>. This model is applicable to excitation systems employing static voltage regulators.IEEE (1992/2005) AC3A Model  The model represents the field-controlled alternator-rectifier excitation systems designated Type AC3A. These excitation systems include an alternator main exciter with non-controlled rectifiers. The exciter employs self-excitation, and the voltage regulator power is derived from the exciter output voltage. Therefore, this system has an additional nonlinearity, simulated by the use of a multiplier whose inputs are the voltage regulator command signal, <i>VA</i>, and the exciter output voltage, <i>EFD</i>, times <i>KR</i>. This model is applicable to excitation systems employing static voltage regulators.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcAC6A_TreeNode = TreeNode(
    node_for=[ExcAC6A],
        tooltip="IEEE (1992/2005) AC6A Model  The model is used to represent field-controlled alternator-rectifier excitation systems with system-supplied electronic voltage regulators. The maximum output of the regulator, <i>V</i><i><sub>R</sub></i>, is a function of terminal voltage, <i>V</i><i><sub>T</sub></i>. The field current limiter included in the original model AC6A remains in the 2005 update.IEEE (1992/2005) AC6A Model  The model is used to represent field-controlled alternator-rectifier excitation systems with system-supplied electronic voltage regulators. The maximum output of the regulator, <i>V</i><i><sub>R</sub></i>, is a function of terminal voltage, <i>V</i><i><sub>T</sub></i>. The field current limiter included in the original model AC6A remains in the 2005 update.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcAC5A_TreeNode = TreeNode(
    node_for=[ExcAC5A],
        tooltip="IEEE (1992/2005) AC5A Model  The model designated as Type AC5A, is a simplified model for brushless excitation systems. The regulator is supplied from a source, such as a permanent magnet generator, which is not affected by system disturbances. Unlike other ac models, this model uses loaded rather than open circuit exciter saturation data in the same way as it is used for the dc models. Because the model has been widely implemented by the industry, it is sometimes used to represent other types of systems when either detailed data for them are not available or simplified models are required.IEEE (1992/2005) AC5A Model  The model designated as Type AC5A, is a simplified model for brushless excitation systems. The regulator is supplied from a source, such as a permanent magnet generator, which is not affected by system disturbances. Unlike other ac models, this model uses loaded rather than open circuit exciter saturation data in the same way as it is used for the dc models. Because the model has been widely implemented by the industry, it is sometimes used to represent other types of systems when either detailed data for them are not available or simplified models are required.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcST5B_TreeNode = TreeNode(
    node_for=[ExcST5B],
        tooltip="IEEE (2005) ST5B Model  The Type ST5B excitation system is a variation of the Type ST1A model, with alternative overexcitation and underexcitation inputs and additional limits. The corresponding stabilizer models that can be used with these models are the Type PSS2B, PSS3B, or PSS4B.IEEE (2005) ST5B Model  The Type ST5B excitation system is a variation of the Type ST1A model, with alternative overexcitation and underexcitation inputs and additional limits. The corresponding stabilizer models that can be used with these models are the Type PSS2B, PSS3B, or PSS4B.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcSCRX_TreeNode = TreeNode(
    node_for=[ExcSCRX],
        tooltip="Simple excitation system model representing generic characteristics of many excitation systems; intended for use where negative field current may be a problemSimple excitation system model representing generic characteristics of many excitation systems; intended for use where negative field current may be a problem",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcAC8B_TreeNode = TreeNode(
    node_for=[ExcAC8B],
        tooltip="IEEE (2005) AC8B Model  The AVR in this model consists of PID control, with separate constants for the proportional (<i>KPR</i>), integral (<i>KIR</i>), and derivative (<i>KDR</i>) gains. The representation of the brushless exciter (<i>TE</i>, <i>KE</i>, <i>SE</i>, <i>KC</i>, <i>KD</i>) is similar to the model Type AC2A. The Type AC8B model can be used to represent static voltage regulators applied to brushless excitation systems. Digitally based voltage regulators feeding dc rotating main exciters can be represented with the AC Type AC8B model with the parameters <i>KC </i>and <i>KD </i>set to 0. For thyristor power stages fed from the generator terminals, the limits <i>VRMAX </i>and <i>VRMIN </i>should be a function of terminal voltage: <i>VT </i>x <i>VRMAX </i>and <i>VT </i>x <i>VRMIN</i>.IEEE (2005) AC8B Model  The AVR in this model consists of PID control, with separate constants for the proportional (<i>KPR</i>), integral (<i>KIR</i>), and derivative (<i>KDR</i>) gains. The representation of the brushless exciter (<i>TE</i>, <i>KE</i>, <i>SE</i>, <i>KC</i>, <i>KD</i>) is similar to the model Type AC2A. The Type AC8B model can be used to represent static voltage regulators applied to brushless excitation systems. Digitally based voltage regulators feeding dc rotating main exciters can be represented with the AC Type AC8B model with the parameters <i>KC </i>and <i>KD </i>set to 0. For thyristor power stages fed from the generator terminals, the limits <i>VRMAX </i>and <i>VRMIN </i>should be a function of terminal voltage: <i>VT </i>x <i>VRMAX </i>and <i>VT </i>x <i>VRMIN</i>.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcWT2E_TreeNode = TreeNode(
    node_for=[ExcWT2E],
        tooltip="Type 2 standard wind turbine field resistance control modelType 2 standard wind turbine field resistance control model",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcAC7B_TreeNode = TreeNode(
    node_for=[ExcAC7B],
        tooltip="IEEE (2005) AC7B Model  These excitation systems consist of an ac alternator with either stationary or rotating rectifiers to produce the dc field requirements. Upgrades to earlier ac excitation systems, which replace only the controls but retain the ac alternator and diode rectifier bridge, have resulted in this new model. Some of the features of this excitation system include a high bandwidth inner loop regulating generator field voltage or exciter current (<i>KF</i>2, <i>KF</i>1), a fast exciter current limit, <i>VFEMAX</i>, to protect the field of the ac alternator, and the PID generator voltage regulator (AVR). An alternative rate feedback loop (<i>KF</i>, <i>TF</i>) is provided for stabilization if the AVR does not include a derivative term. If a PSS control is supplied, the Type PSS2B or PSS3B models are appropriate.IEEE (2005) AC7B Model  These excitation systems consist of an ac alternator with either stationary or rotating rectifiers to produce the dc field requirements. Upgrades to earlier ac excitation systems, which replace only the controls but retain the ac alternator and diode rectifier bridge, have resulted in this new model. Some of the features of this excitation system include a high bandwidth inner loop regulating generator field voltage or exciter current (<i>KF</i>2, <i>KF</i>1), a fast exciter current limit, <i>VFEMAX</i>, to protect the field of the ac alternator, and the PID generator voltage regulator (AVR). An alternative rate feedback loop (<i>KF</i>, <i>TF</i>) is provided for stabilization if the AVR does not include a derivative term. If a PSS control is supplied, the Type PSS2B or PSS3B models are appropriate.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcWT4E_TreeNode = TreeNode(
    node_for=[ExcWT4E],
        tooltip="Type 4 standard wind turbine convertor control modelType 4 standard wind turbine convertor control model",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcST1A_TreeNode = TreeNode(
    node_for=[ExcST1A],
        tooltip="IEEE (1992/2005) ST1A Model  The computer model of the Type ST1A potential-source controlled-rectifier excitation system represents systems in which excitation power is supplied through a transformer from the generator terminals (or the unit's auxiliary bus) and is regulated by a controlled rectifier. The maximum exciter voltage available from such systems is directly related to the generator terminal voltage.IEEE (1992/2005) ST1A Model  The computer model of the Type ST1A potential-source controlled-rectifier excitation system represents systems in which excitation power is supplied through a transformer from the generator terminals (or the unit's auxiliary bus) and is regulated by a controlled rectifier. The maximum exciter voltage available from such systems is directly related to the generator terminal voltage.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcBBC_TreeNode = TreeNode(
    node_for=[ExcBBC],
        tooltip="Static Excitation System Model with ABB regulatorStatic Excitation System Model with ABB regulator",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcitationSystem_TreeNode = TreeNode(
    node_for=[ExcitationSystem],
        tooltip="An excitation system provides the field voltage (Efd) for a synchronous machine model. It is linked to a specific generator by the Bus number and Unit ID.An excitation system provides the field voltage (Efd) for a synchronous machine model. It is linked to a specific generator by the Bus number and Unit ID.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcDC3A_TreeNode = TreeNode(
    node_for=[ExcDC3A],
        tooltip="IEEE (1992/2005) DC3A Model  The Type DC3A model is used to represent older systems, in particular those dc commutator exciters with non-continuously acting regulators that were commonly used before the development of the continuously acting varieties. These systems respond at basically two different rates, depending upon the magnitude of voltage error. For small errors, adjustment is made periodically with a signal to a motor-operated rheostat. Larger errors cause resistors to be quickly shorted or inserted and a strong forcing signal applied to the exciter. Continuous motion of the motor-operated rheostat occurs for these larger error signals, even though it is bypassed by contactor action.IEEE (1992/2005) DC3A Model  The Type DC3A model is used to represent older systems, in particular those dc commutator exciters with non-continuously acting regulators that were commonly used before the development of the continuously acting varieties. These systems respond at basically two different rates, depending upon the magnitude of voltage error. For small errors, adjustment is made periodically with a signal to a motor-operated rheostat. Larger errors cause resistors to be quickly shorted or inserted and a strong forcing signal applied to the exciter. Continuous motion of the motor-operated rheostat occurs for these larger error signals, even though it is bypassed by contactor action.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcST3A_TreeNode = TreeNode(
    node_for=[ExcST3A],
        tooltip="IEEE (1992/2005) ST3A Model  Some static systems utilize a field voltage control loop to linearize the exciter control characteristic. This also makes the output independent of supply source variations until supply limitations are reached. These systems utilize a variety of controlled-rectifier designs: full thyristor complements or hybrid bridges in either series or shunt configurations. The power source may consist of only a potential source, either fed from the machine terminals or from internal windings. Some designs may have compound power sources utilizing both machine potential and current. These power sources are represented as phasor combinations of machine terminal current and voltage and are accommodated by suitable parameters in the model Type ST3A.IEEE (1992/2005) ST3A Model  Some static systems utilize a field voltage control loop to linearize the exciter control characteristic. This also makes the output independent of supply source variations until supply limitations are reached. These systems utilize a variety of controlled-rectifier designs: full thyristor complements or hybrid bridges in either series or shunt configurations. The power source may consist of only a potential source, either fed from the machine terminals or from internal windings. Some designs may have compound power sources utilizing both machine potential and current. These power sources are represented as phasor combinations of machine terminal current and voltage and are accommodated by suitable parameters in the model Type ST3A.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ExcCZ_TreeNode = TreeNode(
    node_for=[ExcCZ],
        tooltip="Czech proportional/integral excitation system model.Czech proportional/integral excitation system model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovHydro3_TreeNode = TreeNode(
    node_for=[GovHydro3],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovHydro2_TreeNode = TreeNode(
    node_for=[GovHydro2],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovGAST_TreeNode = TreeNode(
    node_for=[GovGAST],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovWT1T_TreeNode = TreeNode(
    node_for=[GovWT1T],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TurbineGovernor_TreeNode = TreeNode(
    node_for=[TurbineGovernor],
        tooltip="The turbine-governor determines the mechanical power (Pm) supplied to the generator modelThe turbine-governor determines the mechanical power (Pm) supplied to the generator model",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovWT2P_TreeNode = TreeNode(
    node_for=[GovWT2P],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovHydroDD_TreeNode = TreeNode(
    node_for=[GovHydroDD],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovHydroWEH_TreeNode = TreeNode(
    node_for=[GovHydroWEH],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovWT3T_TreeNode = TreeNode(
    node_for=[GovWT3T],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovHydroPID_TreeNode = TreeNode(
    node_for=[GovHydroPID],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovHydro4_TreeNode = TreeNode(
    node_for=[GovHydro4],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovDUM_TreeNode = TreeNode(
    node_for=[GovDUM],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovHydroWPID_TreeNode = TreeNode(
    node_for=[GovHydroWPID],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovWT4P_TreeNode = TreeNode(
    node_for=[GovWT4P],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TLCFB1_TreeNode = TreeNode(
    node_for=[TLCFB1],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovGASM_TreeNode = TreeNode(
    node_for=[GovGASM],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovHydroR_TreeNode = TreeNode(
    node_for=[GovHydroR],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovSteamFV2_TreeNode = TreeNode(
    node_for=[GovSteamFV2],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovRAV_TreeNode = TreeNode(
    node_for=[GovRAV],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovCT2_TreeNode = TreeNode(
    node_for=[GovCT2],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovSteam1_TreeNode = TreeNode(
    node_for=[GovSteam1],
        tooltip="IEEE steam turbine/governor model  (with optional deadband and nonlinear valve gain added)IEEE steam turbine/governor model  (with optional deadband and nonlinear valve gain added)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovSteamCC_TreeNode = TreeNode(
    node_for=[GovSteamCC],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovSteamSGO_TreeNode = TreeNode(
    node_for=[GovSteamSGO],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovSteamFV3_TreeNode = TreeNode(
    node_for=[GovSteamFV3],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovWT3P_TreeNode = TreeNode(
    node_for=[GovWT3P],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovWT1P_TreeNode = TreeNode(
    node_for=[GovWT1P],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovSteam0_TreeNode = TreeNode(
    node_for=[GovSteam0],
        tooltip="A simplified steam turbine-governor model.A simplified steam turbine-governor model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovCT1_TreeNode = TreeNode(
    node_for=[GovCT1],
        tooltip="General model for any prime mover with a PID governor, used primarily for combustion turbine and combined cycle units.General model for any prime mover with a PID governor, used primarily for combustion turbine and combined cycle units.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovWT2T_TreeNode = TreeNode(
    node_for=[GovWT2T],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovHydro1_TreeNode = TreeNode(
    node_for=[GovHydro1],
        tooltip="Hydro turbine-governor model.Hydro turbine-governor model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovHydroPID2_TreeNode = TreeNode(
    node_for=[GovHydroPID2],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovWT4T_TreeNode = TreeNode(
    node_for=[GovWT4T],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovSteamEU_TreeNode = TreeNode(
    node_for=[GovSteamEU],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovHydro0_TreeNode = TreeNode(
    node_for=[GovHydro0],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovGASTWD_TreeNode = TreeNode(
    node_for=[GovGASTWD],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GovGAST2_TreeNode = TreeNode(
    node_for=[GovGAST2],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PowerSystemStabilizer_TreeNode = TreeNode(
    node_for=[PowerSystemStabilizer],
        tooltip="A PSS provides an input (Vs) to the excitation system model to improve damping of system oscillations.  A variety of input signals may be used depending on the particular design.A PSS provides an input (Vs) to the excitation system model to improve damping of system oscillations.  A variety of input signals may be used depending on the particular design.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PssIEEE4B_TreeNode = TreeNode(
    node_for=[PssIEEE4B],
        tooltip="PSS type IEEE PSS4BPSS type IEEE PSS4B",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PssIEEE2B_TreeNode = TreeNode(
    node_for=[PssIEEE2B],
        tooltip="IEEE (2005) PSS2B Model  This stabilizer model is designed to represent a variety of dual-input stabilizers, which normally use combinations of power and speed or frequency to derive the stabilizing signal.IEEE (2005) PSS2B Model  This stabilizer model is designed to represent a variety of dual-input stabilizers, which normally use combinations of power and speed or frequency to derive the stabilizing signal.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PssSB4_TreeNode = TreeNode(
    node_for=[PssSB4],
        tooltip="Power sensitive stabilizer modelPower sensitive stabilizer model",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PssSB_TreeNode = TreeNode(
    node_for=[PssSB],
        tooltip="Dual input PSS, pss2a and transient stabilizerDual input PSS, pss2a and transient stabilizer",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PssSK_TreeNode = TreeNode(
    node_for=[PssSK],
        tooltip="PSS Slovakian type &ndash; three inputsPSS Slovakian type &ndash; three inputs",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PssPTIST3_TreeNode = TreeNode(
    node_for=[PssPTIST3],
        tooltip="PTI microprocessor-based stabilizer model type 3PTI microprocessor-based stabilizer model type 3",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PssIEEE1A_TreeNode = TreeNode(
    node_for=[PssIEEE1A],
        tooltip="PSS type IEEE PSS1APSS type IEEE PSS1A",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PssIEEE3B_TreeNode = TreeNode(
    node_for=[PssIEEE3B],
        tooltip="PSS type IEEE PSS3BPSS type IEEE PSS3B",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PssWSCC_TreeNode = TreeNode(
    node_for=[PssWSCC],
        tooltip="Dual input PSSDual input PSS",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PssPTIST1_TreeNode = TreeNode(
    node_for=[PssPTIST1],
        tooltip="PTI microprocessor-based stabilizer model type 1PTI microprocessor-based stabilizer model type 1",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PssSH_TreeNode = TreeNode(
    node_for=[PssSH],
        tooltip="Siemens H infinity PSSSiemens H infinity PSS",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GenSync_TreeNode = TreeNode(
    node_for=[GenSync],
        tooltip="Synchronous generator model. A single standard synchronous model is defined for the CIM, with several variations indicated by the 'model type' attribute.  This model can be used for all types of synchronous machines (salient pole, solid iron rotor, etc.).Synchronous generator model. A single standard synchronous model is defined for the CIM, with several variations indicated by the 'model type' attribute.  This model can be used for all types of synchronous machines (salient pole, solid iron rotor, etc.).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GenLoad_TreeNode = TreeNode(
    node_for=[GenLoad],
        tooltip="Representation of a small generator as a negative load rather than a dynamic generator model. This practice is also referred to as 'netting' the generation with the load, i.e. taking the net value of load minus generation as the new load value.  For dynamic modeling purposes, each generator that does not have a dynamic load model must have a genLoad record.Representation of a small generator as a negative load rather than a dynamic generator model. This practice is also referred to as 'netting' the generation with the load, i.e. taking the net value of load minus generation as the new load value.  For dynamic modeling purposes, each generator that does not have a dynamic load model must have a genLoad record.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GenAsync_TreeNode = TreeNode(
    node_for=[GenAsync],
        tooltip="An asynchronous (induction) generator with no external connection to the rotor windings, e.g., squirrel-cage induction machine.An asynchronous (induction) generator with no external connection to the rotor windings, e.g., squirrel-cage induction machine.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GenEquiv_TreeNode = TreeNode(
    node_for=[GenEquiv],
        tooltip="An equivalent representation of a synchronous generator as a constant internal voltage behind an impedance Ra plus Xp.An equivalent representation of a synchronous generator as a constant internal voltage behind an impedance Ra plus Xp.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


VcompIEEE_TreeNode = TreeNode(
    node_for=[VcompIEEE],
        tooltip="IEEE Voltage Compensation ModelIEEE Voltage Compensation Model",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


VoltageCompensator_TreeNode = TreeNode(
    node_for=[VoltageCompensator],
        tooltip="A voltage compensator adjusts the terminal voltage feedback to the excitation system by adding a quantity that is proportional to the terminal current of the generator. It is linked to a specific generator by the Bus number and Unit IDA voltage compensator adjusts the terminal voltage feedback to the excitation system by adding a quantity that is proportional to the terminal current of the generator. It is linked to a specific generator by the Bus number and Unit ID",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


VcompCross_TreeNode = TreeNode(
    node_for=[VcompCross],
        tooltip="Voltage Compensation Model for Cross-Compound Generating UnitVoltage Compensation Model for Cross-Compound Generating Unit",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MotorAsync_TreeNode = TreeNode(
    node_for=[MotorAsync],
        tooltip="An asynchronous (induction) motor with no external connection to the rotor windings, e.g., a squirrel-cage induction motor.An asynchronous (induction) motor with no external connection to the rotor windings, e.g., a squirrel-cage induction motor.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MechanicalLoad_TreeNode = TreeNode(
    node_for=[MechanicalLoad],
        tooltip="A mechanical load represents the variation in a motor's shaft torque or power as a function of shaft speed.A mechanical load represents the variation in a motor's shaft torque or power as a function of shaft speed.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MechLoad1_TreeNode = TreeNode(
    node_for=[MechLoad1],
        tooltip="Mechanical load model 1Mechanical load model 1",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SynchronousMotorType_TreeNode = TreeNode(
    node_for=[SynchronousMotorType],
        tooltip="Type of synchronous motorType of synchronous motor",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MotorSync_TreeNode = TreeNode(
    node_for=[MotorSync],
        tooltip="A large industrial motor or group of similar motors.  They are represented as <b>generators with negative Pgen</b> in the static (power flow) data.A large industrial motor or group of similar motors.  They are represented as <b>generators with negative Pgen</b> in the static (power flow) data.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)



#------------------------------------------------------------------------------
#  Tree node list:
#------------------------------------------------------------------------------


tree_nodes = [
    Element_TreeNode,
    Model_TreeNode,
    Model_Elements_TreeNode,
    RotatingMachine_TreeNode,
    MetaBlockConOutput_TreeNode,
    MetaBlock_TreeNode,
    BlockParameter_TreeNode,
    MetaBlockReference_TreeNode,
    ExcitationSystemLimiter_TreeNode,
    MetaBlockConnectivity_TreeNode,
    ProtectiveDevice_TreeNode,
    SourceModels_TreeNode,
    MetaBlockOutputReference_TreeNode,
    BlockConnection_TreeNode,
    MetaBlockConInput_TreeNode,
    StaticVarDevice_TreeNode,
    MetaBlockConnection_TreeNode,
    BlockConnectivity_TreeNode,
    MetaBlockConSignal_TreeNode,
    Block_TreeNode,
    MetaBlockStateReference_TreeNode,
    AsynchronousMachine_TreeNode,
    TieToMeasurement_TreeNode,
    MetaBlockSignal_TreeNode,
    MetaBlockInputReference_TreeNode,
    MetaBlockParameterReference_TreeNode,
    MetaBlockConnectable_TreeNode,
    MetaBlockState_TreeNode,
    AggregateLoad_TreeNode,
    LoadMotor_TreeNode,
    ExcBAS_TreeNode,
    ExcDC2A_TreeNode,
    ExcSEXS_TreeNode,
    ExcELIN2_TreeNode,
    ExcAC4A_TreeNode,
    ExcSK_TreeNode,
    ExcAC2A_TreeNode,
    ExcELIN1_TreeNode,
    ExcST6B_TreeNode,
    ExcST4B_TreeNode,
    ExcWT3E_TreeNode,
    ExcPIC_TreeNode,
    ExcSK2_TreeNode,
    ExcST2A_TreeNode,
    ExcHU_TreeNode,
    ExcREXS_TreeNode,
    ExcST7B_TreeNode,
    ExcAC1A_TreeNode,
    ExcDC4B_TreeNode,
    ExcDC1A_TreeNode,
    ExcAC3A_TreeNode,
    ExcAC6A_TreeNode,
    ExcAC5A_TreeNode,
    ExcST5B_TreeNode,
    ExcSCRX_TreeNode,
    ExcAC8B_TreeNode,
    ExcWT2E_TreeNode,
    ExcAC7B_TreeNode,
    ExcWT4E_TreeNode,
    ExcST1A_TreeNode,
    ExcBBC_TreeNode,
    ExcitationSystem_TreeNode,
    ExcDC3A_TreeNode,
    ExcST3A_TreeNode,
    ExcCZ_TreeNode,
    TurbineGovernor_TreeNode,
    GovWT2P_TreeNode,
    GovHydroDD_TreeNode,
    GovHydroWEH_TreeNode,
    GovWT3T_TreeNode,
    GovHydroPID_TreeNode,
    GovHydro4_TreeNode,
    GovDUM_TreeNode,
    GovHydroWPID_TreeNode,
    GovWT4P_TreeNode,
    TLCFB1_TreeNode,
    GovGASM_TreeNode,
    GovHydroR_TreeNode,
    GovSteamFV2_TreeNode,
    GovRAV_TreeNode,
    GovCT2_TreeNode,
    GovSteam1_TreeNode,
    GovSteamCC_TreeNode,
    GovSteamSGO_TreeNode,
    GovSteamFV3_TreeNode,
    GovWT3P_TreeNode,
    GovWT1P_TreeNode,
    GovSteam0_TreeNode,
    GovCT1_TreeNode,
    GovWT2T_TreeNode,
    GovHydro1_TreeNode,
    GovHydroPID2_TreeNode,
    GovWT4T_TreeNode,
    GovSteamEU_TreeNode,
    GovHydro0_TreeNode,
    GovGASTWD_TreeNode,
    GovGAST2_TreeNode,
    PowerSystemStabilizer_TreeNode,
    PssIEEE4B_TreeNode,
    PssIEEE2B_TreeNode,
    PssSB4_TreeNode,
    PssSB_TreeNode,
    PssSK_TreeNode,
    PssPTIST3_TreeNode,
    PssIEEE1A_TreeNode,
    PssIEEE3B_TreeNode,
    PssWSCC_TreeNode,
    PssPTIST1_TreeNode,
    PssSH_TreeNode,
    GenSync_TreeNode,
    GenLoad_TreeNode,
    GenAsync_TreeNode,
    GenEquiv_TreeNode,
    VoltageCompensator_TreeNode,
    VcompCross_TreeNode,
    MotorAsync_TreeNode,
    MechanicalLoad_TreeNode,
    MechLoad1_TreeNode,
    SynchronousMotorType_TreeNode,
    MotorSync_TreeNode,
    AttributeBlockParameter_TreeNode,
    MetaBlockInput_TreeNode,
    MetaBlockOutput_TreeNode,
    MetaBlockParameter_TreeNode,
    LoadStatic_TreeNode,
    LoadStaticBus_TreeNode,
    LoadStaticZone_TreeNode,
    LoadStaticArea_TreeNode,
    GovHydro3_TreeNode,
    GovHydro2_TreeNode,
    GovGAST_TreeNode,
    GovWT1T_TreeNode,
    VcompIEEE_TreeNode,
    LoadStaticSystem_TreeNode,
    LoadStaticOwner_TreeNode,
]
tree_nodes.reverse()

#------------------------------------------------------------------------------
#  Dynamics Tree Editor:
#------------------------------------------------------------------------------

DynamicsTreeEditor = TreeEditor(nodes=tree_nodes, editable=True)

#------------------------------------------------------------------------------
#  Begin "DynamicsTreeEditor" user region:
#------------------------------------------------------------------------------
# @generated
class TreeRoot(HasTraits):

    # Root element of the model tree.
    root = Instance(HasTraits)

    # Traits view to display.
    view = View(
        Item('root',
            editor=DynamicsTreeEditor,
            show_label=False),
        width     = 0.33,
        height    = 0.50,
        resizable = True,
        buttons   = ["OK", "Cancel"]
    )

#------------------------------------------------------------------------------
#  End "DynamicsTreeEditor" user region:
#------------------------------------------------------------------------------

if __name__ == "__main__":
    root = TreeRoot()
    root.configure_traits()

# EOF -------------------------------------------------------------------------
