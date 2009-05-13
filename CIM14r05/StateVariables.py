#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM14r05 import Element



from enthought.traits.api import Instance, List, Property, Float, Int, Bool
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
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM14r05.StateVariables.StateVariable",
        title="StateVariable",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StateVariable" user definitions:
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

    Terminal = Instance("CIM14r05.Core.Terminal",
        transient=True,
        opposite="SvPowerFlow",
        editor=InstanceEditor(name="_terminals"))

    def _get_terminals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.Core.Terminal" ]
        else:
            return []

    _terminals = Property(fget=_get_terminals)

    # The active power flow into the terminal.
    p = Float(desc="The active power flow into the terminal.")

    # The reactive power flow into the terminal.
    q = Float(desc="The reactive power flow into the terminal.")

    #--------------------------------------------------------------------------
    #  Begin "SvPowerFlow" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("p", "q",
                label="Attributes"),
            VGroup("Parent", "Terminal",
                label="References"),
            dock="tab"),
        id="CIM14r05.StateVariables.SvPowerFlow",
        title="SvPowerFlow",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SvPowerFlow" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SvTapStep" class:
#------------------------------------------------------------------------------

class SvTapStep(StateVariable):
    """ State variable for transformer tap step.     Normally a profile specifies only one of the attributes 'position'or 'continuousPosition'.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    TapChanger = Instance("CIM14r05.Wires.TapChanger",
        transient=True,
        opposite="SvTapStep",
        editor=InstanceEditor(name="_tapchangers"))

    def _get_tapchangers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.Wires.TapChanger" ]
        else:
            return []

    _tapchangers = Property(fget=_get_tapchangers)

    # The floating point tap position.
    continuousPosition = Float(desc="The floating point tap position.")

    # The integer tap position.
    position = Int(desc="The integer tap position.")

    #--------------------------------------------------------------------------
    #  Begin "SvTapStep" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("continuousPosition", "position",
                label="Attributes"),
            VGroup("Parent", "TapChanger",
                label="References"),
            dock="tab"),
        id="CIM14r05.StateVariables.SvTapStep",
        title="SvTapStep",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SvTapStep" user definitions:
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

    ShuntCompensator = Instance("CIM14r05.Wires.ShuntCompensator",
        transient=True,
        opposite="SvShuntCompensatorSections",
        editor=InstanceEditor(name="_shuntcompensators"))

    def _get_shuntcompensators(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.Wires.ShuntCompensator" ]
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
            VGroup("sections", "continuousSections",
                label="Attributes"),
            VGroup("Parent", "ShuntCompensator",
                label="References"),
            dock="tab"),
        id="CIM14r05.StateVariables.SvShuntCompensatorSections",
        title="SvShuntCompensatorSections",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SvShuntCompensatorSections" user definitions:
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

    ConductingEquipment = Instance("CIM14r05.Core.ConductingEquipment",
        transient=True,
        opposite="SvStatus",
        editor=InstanceEditor(name="_conductingequipments"))

    def _get_conductingequipments(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.Core.ConductingEquipment" ]
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
            VGroup("inService",
                label="Attributes"),
            VGroup("Parent", "ConductingEquipment",
                label="References"),
            dock="tab"),
        id="CIM14r05.StateVariables.SvStatus",
        title="SvStatus",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SvStatus" user definitions:
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

    TopologicalNode = Instance("CIM14r05.Topology.TopologicalNode",
        transient=True,
        opposite="SvInjection",
        editor=InstanceEditor(name="_topologicalnodes"))

    def _get_topologicalnodes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.Topology.TopologicalNode" ]
        else:
            return []

    _topologicalnodes = Property(fget=_get_topologicalnodes)

    # The activive power injected into the bus at this location.
    qNetInjection = Float(desc="The activive power injected into the bus at this location.")

    # The activive power injected into the bus at this location.
    pNetInjection = Float(desc="The activive power injected into the bus at this location.")

    #--------------------------------------------------------------------------
    #  Begin "SvInjection" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("qNetInjection", "pNetInjection",
                label="Attributes"),
            VGroup("Parent", "TopologicalNode",
                label="References"),
            dock="tab"),
        id="CIM14r05.StateVariables.SvInjection",
        title="SvInjection",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SvInjection" user definitions:
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

    TopologicalNode = Instance("CIM14r05.Topology.TopologicalNode",
        transient=True,
        opposite="SvVoltage",
        editor=InstanceEditor(name="_topologicalnodes"))

    def _get_topologicalnodes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.Topology.TopologicalNode" ]
        else:
            return []

    _topologicalnodes = Property(fget=_get_topologicalnodes)

    # The voltage angle in radians of the topological node.
    angle = Float(desc="The voltage angle in radians of the topological node.")

    # The voltage magnitude of the topological node.
    v = Float(desc="The voltage magnitude of the topological node.")

    #--------------------------------------------------------------------------
    #  Begin "SvVoltage" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("angle", "v",
                label="Attributes"),
            VGroup("Parent", "TopologicalNode",
                label="References"),
            dock="tab"),
        id="CIM14r05.StateVariables.SvVoltage",
        title="SvVoltage",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SvVoltage" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
