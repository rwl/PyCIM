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

""" State variables for analysis solutions such as powerflow.State variables for analysis solutions such as powerflow.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from UCTE import Element
from UCTE.Domain import AngleRadians
from UCTE.Domain import Voltage
from UCTE.Domain import ActivePower
from UCTE.Domain import ReactivePower



from enthought.traits.api import Instance, List, Property, Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "StateVariable" class:
#------------------------------------------------------------------------------

class StateVariable(Element):
    """ An abstract class for state variables.An abstract class for state variables.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "StateVariable" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="UCTE.StateVariables.StateVariable",
        title="StateVariable",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StateVariable" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SvVoltage" class:
#------------------------------------------------------------------------------

class SvVoltage(StateVariable):
    """ State variable for voltage.State variable for voltage.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The topological node associated with the voltage state.The topological node associated with the voltage state.
    TopologicalNode = Instance("UCTE.Topology.TopologicalNode", allow_none=False,
        desc="The topological node associated with the voltage state.The topological node associated with the voltage state.",
        transient=True,
        opposite="SvVoltage",
        editor=InstanceEditor(name="_topologicalnodes"))

    def _get_topologicalnodes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Topology.TopologicalNode" ]
        else:
            return []

    _topologicalnodes = Property(fget=_get_topologicalnodes)

    # The voltage angle in radians of the topological node.The voltage angle in radians of the topological node.
    angle = AngleRadians(desc="The voltage angle in radians of the topological node.The voltage angle in radians of the topological node.")

    # The voltage magnitude of the topological node.The voltage magnitude of the topological node.
    v = Voltage(desc="The voltage magnitude of the topological node.The voltage magnitude of the topological node.")

    #--------------------------------------------------------------------------
    #  Begin "SvVoltage" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "angle", "v",
                label="Attributes"),
            VGroup("Model", "TopologicalNode",
                label="References"),
            dock="tab"),
        id="UCTE.StateVariables.SvVoltage",
        title="SvVoltage",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SvVoltage" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SvShuntCompensatorSections" class:
#------------------------------------------------------------------------------

class SvShuntCompensatorSections(StateVariable):
    """ State variable for the number of sections in service for a shunt compensator.A SvShuntCompensator is always associated with any instance of ShuntCompensator.   The sections or continuousSections values are specified depending upon the value of the associated RegulatingControl.discrete attribute.  If no RegulatingControl is associated, then the ShuntCompensator is treated as discrete.    In discrete mode, the 'sections' attribute must be present.   In the not 'discrete' mode (continuous mode) the 'continuousSections' attribute must be present.     In the case the Terminal.connected value is 'false' the specificed number of sections is not meaningful to the powerflow solution and powerflow implementations should interpret this as zero injection.   Note that an SvShuntCompensatorSections should be supplied even for ShuntCompensators whose Terminal.connected status is 'false' to keep total number of ShuntCompensator and SvShuntCompensatorSection objects in the model the same.State variable for the number of sections in service for a shunt compensator.A SvShuntCompensator is always associated with any instance of ShuntCompensator.   The sections or continuousSections values are specified depending upon the value of the associated RegulatingControl.discrete attribute.  If no RegulatingControl is associated, then the ShuntCompensator is treated as discrete.    In discrete mode, the 'sections' attribute must be present.   In the not 'discrete' mode (continuous mode) the 'continuousSections' attribute must be present.     In the case the Terminal.connected value is 'false' the specificed number of sections is not meaningful to the powerflow solution and powerflow implementations should interpret this as zero injection.   Note that an SvShuntCompensatorSections should be supplied even for ShuntCompensators whose Terminal.connected status is 'false' to keep total number of ShuntCompensator and SvShuntCompensatorSection objects in the model the same.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The shunt compensator for which the state applies.The shunt compensator for which the state applies.
    ShuntCompensator = Instance("UCTE.Wires.ShuntCompensator", allow_none=False,
        desc="The shunt compensator for which the state applies.The shunt compensator for which the state applies.",
        transient=True,
        opposite="SvShuntCompensatorSections",
        editor=InstanceEditor(name="_shuntcompensators"))

    def _get_shuntcompensators(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Wires.ShuntCompensator" ]
        else:
            return []

    _shuntcompensators = Property(fget=_get_shuntcompensators)

    # The number of sections in service as a continous variable.The number of sections in service as a continous variable.
    continuousSections = Float(desc="The number of sections in service as a continous variable.The number of sections in service as a continous variable.")

    #--------------------------------------------------------------------------
    #  Begin "SvShuntCompensatorSections" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "continuousSections",
                label="Attributes"),
            VGroup("Model", "ShuntCompensator",
                label="References"),
            dock="tab"),
        id="UCTE.StateVariables.SvShuntCompensatorSections",
        title="SvShuntCompensatorSections",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SvShuntCompensatorSections" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SvTapStep" class:
#------------------------------------------------------------------------------

class SvTapStep(StateVariable):
    """ State variable for transformer tap step.     Normally a profile specifies only one of the attributes 'position'or 'continuousPosition'.SvTapStep is only meant to be used for taps that change under load.State variable for transformer tap step.     Normally a profile specifies only one of the attributes 'position'or 'continuousPosition'.SvTapStep is only meant to be used for taps that change under load.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The tap changer associated with the tap step state.The tap changer associated with the tap step state.
    TapChanger = Instance("UCTE.Wires.TapChanger", allow_none=False,
        desc="The tap changer associated with the tap step state.The tap changer associated with the tap step state.",
        transient=True,
        opposite="SvTapStep",
        editor=InstanceEditor(name="_tapchangers"))

    def _get_tapchangers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Wires.TapChanger" ]
        else:
            return []

    _tapchangers = Property(fget=_get_tapchangers)

    # The floating point tap position.The floating point tap position.
    continuousPosition = Float(desc="The floating point tap position.The floating point tap position.")

    #--------------------------------------------------------------------------
    #  Begin "SvTapStep" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "continuousPosition",
                label="Attributes"),
            VGroup("Model", "TapChanger",
                label="References"),
            dock="tab"),
        id="UCTE.StateVariables.SvTapStep",
        title="SvTapStep",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SvTapStep" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SvPowerFlow" class:
#------------------------------------------------------------------------------

class SvPowerFlow(StateVariable):
    """ State variable for power flow.Only Terminal instances of EnergyConsumer and SynchronousMachine will have SvPowerFlow instances assigned.   The number of SvPowerFlow instances in the model should match the number EnergyConsumer plus SynchronousMachine objects in the model regardless of the Terminal.connected values.    Any SvPowerFlow with a Terminal.connected value of false must have zero flow explicitly specified on an SvPowerFlow instance. The other types of terminals are not included in exchanges since their values can be readily computed from local voltages and attributes without a global powerflow solution.State variable for power flow.Only Terminal instances of EnergyConsumer and SynchronousMachine will have SvPowerFlow instances assigned.   The number of SvPowerFlow instances in the model should match the number EnergyConsumer plus SynchronousMachine objects in the model regardless of the Terminal.connected values.    Any SvPowerFlow with a Terminal.connected value of false must have zero flow explicitly specified on an SvPowerFlow instance. The other types of terminals are not included in exchanges since their values can be readily computed from local voltages and attributes without a global powerflow solution.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The terminal associated with the power flow state.The SvPowerFlow is only associated with the Terminal objects of shunt injection classes EnergyConsumer and  SynchronousMachine.  Branch flows are not exchanged since they can be readily computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  Similarly, Switch flows are not included because they can typically be uniquely computed, except in the case of meshed networks of Switch objects.  Terminals of the ShuntCompensator class are not associated because the injection value can be computed from the solved voltage, number of sections, Termianl.connected state, and the impedance per section attributes on the ShuntCompensator. The terminal associated with the power flow state.The SvPowerFlow is only associated with the Terminal objects of shunt injection classes EnergyConsumer and  SynchronousMachine.  Branch flows are not exchanged since they can be readily computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  Similarly, Switch flows are not included because they can typically be uniquely computed, except in the case of meshed networks of Switch objects.  Terminals of the ShuntCompensator class are not associated because the injection value can be computed from the solved voltage, number of sections, Termianl.connected state, and the impedance per section attributes on the ShuntCompensator. 
    Terminal = Instance("UCTE.Core.Terminal", allow_none=False,
        desc="The terminal associated with the power flow state.The SvPowerFlow is only associated with the Terminal objects of shunt injection classes EnergyConsumer and  SynchronousMachine.  Branch flows are not exchanged since they can be readily computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  Similarly, Switch flows are not included because they can typically be uniquely computed, except in the case of meshed networks of Switch objects.  Terminals of the ShuntCompensator class are not associated because the injection value can be computed from the solved voltage, number of sections, Termianl.connected state, and the impedance per section attributes on the ShuntCompensator. The terminal associated with the power flow state.The SvPowerFlow is only associated with the Terminal objects of shunt injection classes EnergyConsumer and  SynchronousMachine.  Branch flows are not exchanged since they can be readily computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  Similarly, Switch flows are not included because they can typically be uniquely computed, except in the case of meshed networks of Switch objects.  Terminals of the ShuntCompensator class are not associated because the injection value can be computed from the solved voltage, number of sections, Termianl.connected state, and the impedance per section attributes on the ShuntCompensator. ",
        transient=True,
        opposite="SvPowerFlow",
        editor=InstanceEditor(name="_terminals"))

    def _get_terminals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Core.Terminal" ]
        else:
            return []

    _terminals = Property(fget=_get_terminals)

    # The active power flow into the terminal.If the associated Terminal.connected status is 'false', the flow specified in the SvPowerFlow.p should be zero.   The power flow is into the Terminal of the ConductingEquipment.The active power flow into the terminal.If the associated Terminal.connected status is 'false', the flow specified in the SvPowerFlow.p should be zero.   The power flow is into the Terminal of the ConductingEquipment.
    p = ActivePower(desc="The active power flow into the terminal.If the associated Terminal.connected status is 'false', the flow specified in the SvPowerFlow.p should be zero.   The power flow is into the Terminal of the ConductingEquipment.The active power flow into the terminal.If the associated Terminal.connected status is 'false', the flow specified in the SvPowerFlow.p should be zero.   The power flow is into the Terminal of the ConductingEquipment.")

    # The reactive power flow into the terminal.If the associated Terminal.connected status is 'false', the flow specified in the SvPowerFlow.q should be zero.   The power flow is into the Terminal of the ConductingEquipment.The reactive power flow into the terminal.If the associated Terminal.connected status is 'false', the flow specified in the SvPowerFlow.q should be zero.   The power flow is into the Terminal of the ConductingEquipment.
    q = ReactivePower(desc="The reactive power flow into the terminal.If the associated Terminal.connected status is 'false', the flow specified in the SvPowerFlow.q should be zero.   The power flow is into the Terminal of the ConductingEquipment.The reactive power flow into the terminal.If the associated Terminal.connected status is 'false', the flow specified in the SvPowerFlow.q should be zero.   The power flow is into the Terminal of the ConductingEquipment.")

    #--------------------------------------------------------------------------
    #  Begin "SvPowerFlow" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "p", "q",
                label="Attributes"),
            VGroup("Model", "Terminal",
                label="References"),
            dock="tab"),
        id="UCTE.StateVariables.SvPowerFlow",
        title="SvPowerFlow",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SvPowerFlow" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
