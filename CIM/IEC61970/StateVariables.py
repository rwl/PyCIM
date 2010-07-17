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

""" State variables for analysis solutions such as powerflow.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM import Element
from CIM.IEC61970.Domain import ActivePower
from CIM.IEC61970.Domain import ReactivePower
from CIM.IEC61970.Domain import Voltage
from CIM.IEC61970.Domain import AngleRadians
from CIM.IEC61970.Domain import ApparentPower



from enthought.traits.api import Instance, List, Property, Bool, Int, Float
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
    """ An abstract class for state variables.
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
            VGroup("UUID",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.StateVariables.StateVariable",
        title="StateVariable",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StateVariable" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SvInjection" class:
#------------------------------------------------------------------------------

class SvInjection(StateVariable):
    """ Injectixon state variable.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The topological node associated with the state injection.
    TopologicalNode = Instance("CIM.IEC61970.Topology.TopologicalNode",
        desc="The topological node associated with the state injection.",
        transient=True,
        opposite="SvInjection",
        editor=InstanceEditor(name="_topologicalnodes"))

    def _get_topologicalnodes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Topology.TopologicalNode" ]
        else:
            return []

    _topologicalnodes = Property(fget=_get_topologicalnodes)

    # The activive power injected into the bus at this location.
    pNetInjection = ActivePower(desc="The activive power injected into the bus at this location.")

    # The activive power injected into the bus at this location.
    qNetInjection = ReactivePower(desc="The activive power injected into the bus at this location.")

    #--------------------------------------------------------------------------
    #  Begin "SvInjection" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pNetInjection", "qNetInjection",
                label="Attributes"),
            VGroup("Parent", "TopologicalNode",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.StateVariables.SvInjection",
        title="SvInjection",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SvInjection" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SvPowerFlow" class:
#------------------------------------------------------------------------------

class SvPowerFlow(StateVariable):
    """ State variable for power flow.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The terminal associated with the power flow state.
    Terminal = Instance("CIM.IEC61970.Core.Terminal",
        desc="The terminal associated with the power flow state.",
        transient=True,
        opposite="SvPowerFlow",
        editor=InstanceEditor(name="_terminals"))

    def _get_terminals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.Terminal" ]
        else:
            return []

    _terminals = Property(fget=_get_terminals)

    # The active power flow into the terminal.
    p = ActivePower(desc="The active power flow into the terminal.")

    # The reactive power flow into the terminal.
    q = ReactivePower(desc="The reactive power flow into the terminal.")

    #--------------------------------------------------------------------------
    #  Begin "SvPowerFlow" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "p", "q",
                label="Attributes"),
            VGroup("Parent", "Terminal",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.StateVariables.SvPowerFlow",
        title="SvPowerFlow",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SvPowerFlow" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SvStatus" class:
#------------------------------------------------------------------------------

class SvStatus(StateVariable):
    """ State variable for status.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The conducting equipment associated with the status state.
    ConductingEquipment = Instance("CIM.IEC61970.Core.ConductingEquipment",
        desc="The conducting equipment associated with the status state.",
        transient=True,
        opposite="SvStatus",
        editor=InstanceEditor(name="_conductingequipments"))

    def _get_conductingequipments(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.ConductingEquipment" ]
        else:
            return []

    _conductingequipments = Property(fget=_get_conductingequipments)

    # The in service status as a result of topology processing.
    inService = Bool(desc="The in service status as a result of topology processing.")

    #--------------------------------------------------------------------------
    #  Begin "SvStatus" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "inService",
                label="Attributes"),
            VGroup("Parent", "ConductingEquipment",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.StateVariables.SvStatus",
        title="SvStatus",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SvStatus" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SvVoltage" class:
#------------------------------------------------------------------------------

class SvVoltage(StateVariable):
    """ State variable for voltage.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The topological node associated with the voltage state.
    TopologicalNode = Instance("CIM.IEC61970.Topology.TopologicalNode",
        desc="The topological node associated with the voltage state.",
        transient=True,
        opposite="SvVoltage",
        editor=InstanceEditor(name="_topologicalnodes"))

    def _get_topologicalnodes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Topology.TopologicalNode" ]
        else:
            return []

    _topologicalnodes = Property(fget=_get_topologicalnodes)

    # The voltage magnitude of the topological node.
    v = Voltage(desc="The voltage magnitude of the topological node.")

    # The voltage angle in radians of the topological node.
    angle = AngleRadians(desc="The voltage angle in radians of the topological node.")

    #--------------------------------------------------------------------------
    #  Begin "SvVoltage" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "v", "angle",
                label="Attributes"),
            VGroup("Parent", "TopologicalNode",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.StateVariables.SvVoltage",
        title="SvVoltage",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SvVoltage" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SvTapStep" class:
#------------------------------------------------------------------------------

class SvTapStep(StateVariable):
    """ State variable for transformer tap step.     This class is to be used for taps of LTC (load tap changing) transformers, not fixed tap transformers.  Normally a profile specifies only one of the attributes 'position'or 'tapRatio'.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The tap changer associated with the tap step state.
    TapChanger = Instance("CIM.IEC61970.Wires.TapChanger",
        desc="The tap changer associated with the tap step state.",
        transient=True,
        opposite="SvTapStep",
        editor=InstanceEditor(name="_tapchangers"))

    def _get_tapchangers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Wires.TapChanger" ]
        else:
            return []

    _tapchangers = Property(fget=_get_tapchangers)

    # The integer tap position.
    position = Int(desc="The integer tap position.")

    # The floating point tap position.
    continuousPosition = Float(desc="The floating point tap position.")

    #--------------------------------------------------------------------------
    #  Begin "SvTapStep" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "position", "continuousPosition",
                label="Attributes"),
            VGroup("Parent", "TapChanger",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.StateVariables.SvTapStep",
        title="SvTapStep",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SvTapStep" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SvShortCircuit" class:
#------------------------------------------------------------------------------

class SvShortCircuit(StateVariable):
    """ State variable for short circuit.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The topological node associated with the short circuit state.
    TopologicalNode = Instance("CIM.IEC61970.Topology.TopologicalNode",
        desc="The topological node associated with the short circuit state.",
        transient=True,
        opposite="SvShortCircuit",
        editor=InstanceEditor(name="_topologicalnodes"))

    def _get_topologicalnodes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Topology.TopologicalNode" ]
        else:
            return []

    _topologicalnodes = Property(fget=_get_topologicalnodes)

    # Ratio of positive sequence reactance per postive sequence resistance.
    xPerR = Float(desc="Ratio of positive sequence reactance per postive sequence resistance.")

    # The ratio of zero sequence resistance to positive sequence resistance.
    r0PerR = Float(desc="The ratio of zero sequence resistance to positive sequence resistance.")

    # The short circuit apparent power drawn at this node when faulted.
    sShortCircuit = ApparentPower(desc="The short circuit apparent power drawn at this node when faulted.")

    # The ratio of zero sequence reactance per positive sequence reactance.
    x0PerX = Float(desc="The ratio of zero sequence reactance per positive sequence reactance.")

    #--------------------------------------------------------------------------
    #  Begin "SvShortCircuit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "xPerR", "r0PerR", "sShortCircuit", "x0PerX",
                label="Attributes"),
            VGroup("Parent", "TopologicalNode",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.StateVariables.SvShortCircuit",
        title="SvShortCircuit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SvShortCircuit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SvShuntCompensatorSections" class:
#------------------------------------------------------------------------------

class SvShuntCompensatorSections(StateVariable):
    """ State variable for the number of sections in service for a shunt compensator.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The shunt compensator for which the state applies.
    ShuntCompensator = Instance("CIM.IEC61970.Wires.ShuntCompensator",
        desc="The shunt compensator for which the state applies.",
        transient=True,
        opposite="SvShuntCompensatorSections",
        editor=InstanceEditor(name="_shuntcompensators"))

    def _get_shuntcompensators(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Wires.ShuntCompensator" ]
        else:
            return []

    _shuntcompensators = Property(fget=_get_shuntcompensators)

    # The number of sections in service.
    sections = Int(desc="The number of sections in service.")

    # The number of sections in service as a continous variable.
    continuousSections = Float(desc="The number of sections in service as a continous variable.")

    #--------------------------------------------------------------------------
    #  Begin "SvShuntCompensatorSections" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "sections", "continuousSections",
                label="Attributes"),
            VGroup("Parent", "ShuntCompensator",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.StateVariables.SvShuntCompensatorSections",
        title="SvShuntCompensatorSections",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SvShuntCompensatorSections" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
