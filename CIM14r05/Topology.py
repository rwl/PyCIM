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

from CIM14r05.Core import IdentifiedObject



from enthought.traits.api import Instance, List, Property, Bool, Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "BusNameMarker" class:
#------------------------------------------------------------------------------

class BusNameMarker(IdentifiedObject):
    """ Used to apply user standard names to topology buses. Typically used for 'bus/branch' case generation. Associated with one or more ConnectivityNodes that are normally a part of the bus name.    The associated ConnectivityNodes are to be connected by non-retained switches. For a ring bus station configuration, all busbar connectivity nodes in the ring are typically associated.   For a breaker and a half scheme, both busbars would be associated.  For a ring bus, all busbars would be associated.  For a 'straight' busbar configuration, only the main connectivity node at the busbar would be associated.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ConnectivityNode = List(Instance("CIM14r05.Topology.ConnectivityNode"))

    ReportingGroup = Instance("CIM14r05.Core.ReportingGroup",
        transient=True,
        opposite="BusNameMarker",
        editor=InstanceEditor(name="_reportinggroups"))

    def _get_reportinggroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.Core.ReportingGroup" ]
        else:
            return []

    _reportinggroups = Property(fget=_get_reportinggroups)

    ControlArea = Instance("CIM14r05.ControlArea.ControlArea",
        transient=True,
        opposite="BusNameMarker",
        editor=InstanceEditor(name="_controlareas"))

    def _get_controlareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.ControlArea.ControlArea" ]
        else:
            return []

    _controlareas = Property(fget=_get_controlareas)

    #--------------------------------------------------------------------------
    #  Begin "BusNameMarker" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("description", "mRID", "pathName", "localName", "aliasName", "name",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ConnectivityNode", "ReportingGroup", "ControlArea",
                label="References"),
            dock="tab"),
        id="CIM14r05.Topology.BusNameMarker",
        title="BusNameMarker",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BusNameMarker" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConnectivityNode" class:
#------------------------------------------------------------------------------

class ConnectivityNode(IdentifiedObject):
    """ Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
    TopologicalNode = Instance("CIM14r05.Topology.TopologicalNode",
        desc="Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.",
        transient=True,
        opposite="ConnectivityNodes",
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

    BusNameMarker = Instance("CIM14r05.Topology.BusNameMarker",
        transient=True,
        opposite="ConnectivityNode",
        editor=InstanceEditor(name="_busnamemarkers"))

    def _get_busnamemarkers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.Topology.BusNameMarker" ]
        else:
            return []

    _busnamemarkers = Property(fget=_get_busnamemarkers)

    # Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
    Terminals = List(Instance("CIM14r05.Core.Terminal"),
        desc="Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.")

    MemberOf_EquipmentContainer = Instance("CIM14r05.Core.ConnectivityNodeContainer",
        transient=True,
        opposite="ConnectivityNodes",
        editor=InstanceEditor(name="_connectivitynodecontainers"))

    def _get_connectivitynodecontainers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.Core.ConnectivityNodeContainer" ]
        else:
            return []

    _connectivitynodecontainers = Property(fget=_get_connectivitynodecontainers)

    #--------------------------------------------------------------------------
    #  Begin "ConnectivityNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("description", "mRID", "pathName", "localName", "aliasName", "name",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "TopologicalNode", "BusNameMarker", "Terminals", "MemberOf_EquipmentContainer",
                label="References"),
            dock="tab"),
        id="CIM14r05.Topology.ConnectivityNode",
        title="ConnectivityNode",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConnectivityNode" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TopologicalNode" class:
#------------------------------------------------------------------------------

class TopologicalNode(IdentifiedObject):
    """ A set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes can change as the current network state changes (i.e., switches, breakers, etc. change state).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    BaseVoltage = Instance("CIM14r05.Core.BaseVoltage",
        transient=True,
        opposite="TopologicalNode",
        editor=InstanceEditor(name="_basevoltages"))

    def _get_basevoltages(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.Core.BaseVoltage" ]
        else:
            return []

    _basevoltages = Property(fget=_get_basevoltages)

    SvVoltage = Instance("CIM14r05.StateVariables.SvVoltage",
        transient=True,
        opposite="TopologicalNode",
        editor=InstanceEditor(name="_svvoltages"))

    def _get_svvoltages(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.StateVariables.SvVoltage" ]
        else:
            return []

    _svvoltages = Property(fget=_get_svvoltages)

    ControlArea = Instance("CIM14r05.ControlArea.ControlArea",
        transient=True,
        opposite="TopologicalNode",
        editor=InstanceEditor(name="_controlareas"))

    def _get_controlareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.ControlArea.ControlArea" ]
        else:
            return []

    _controlareas = Property(fget=_get_controlareas)

    # Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
    ConnectivityNodes = List(Instance("CIM14r05.Topology.ConnectivityNode"),
        desc="Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.")

    Terminal = List(Instance("CIM14r05.Core.Terminal"))

    ReportingGroup = Instance("CIM14r05.Core.ReportingGroup",
        transient=True,
        opposite="TopologicalNode",
        editor=InstanceEditor(name="_reportinggroups"))

    def _get_reportinggroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.Core.ReportingGroup" ]
        else:
            return []

    _reportinggroups = Property(fget=_get_reportinggroups)

    AngleRef_TopologicalIsland = Instance("CIM14r05.Topology.TopologicalIsland",
        transient=True,
        opposite="AngleRef_TopologicalNode",
        editor=InstanceEditor(name="_topologicalislands"))

    def _get_topologicalislands(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.Topology.TopologicalIsland" ]
        else:
            return []

    _topologicalislands = Property(fget=_get_topologicalislands)

    SvInjection = Instance("CIM14r05.StateVariables.SvInjection",
        transient=True,
        opposite="TopologicalNode",
        editor=InstanceEditor(name="_svinjections"))

    def _get_svinjections(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.StateVariables.SvInjection" ]
        else:
            return []

    _svinjections = Property(fget=_get_svinjections)

    # A topological node belongs to a topological island
    TopologicalIsland = Instance("CIM14r05.Topology.TopologicalIsland",
        desc="A topological node belongs to a topological island",
        transient=True,
        opposite="TopologicalNodes",
        editor=InstanceEditor(name="_topologicalislands"))

    def _get_topologicalislands(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.Topology.TopologicalIsland" ]
        else:
            return []

    _topologicalislands = Property(fget=_get_topologicalislands)

    ConnectivityNodeContainer = Instance("CIM14r05.Core.ConnectivityNodeContainer",
        transient=True,
        opposite="TopologicalNode",
        editor=InstanceEditor(name="_connectivitynodecontainers"))

    def _get_connectivitynodecontainers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.Core.ConnectivityNodeContainer" ]
        else:
            return []

    _connectivitynodecontainers = Property(fget=_get_connectivitynodecontainers)

    # True if node is load carrying
    loadCarrying = Bool(desc="True if node is load carrying")

    # Ratio of positive sequence reactance per postive sequence resistance.
    xPerR = Float(desc="Ratio of positive sequence reactance per postive sequence resistance.")

    # Net injection active power
    netInjectionP = Float(desc="Net injection active power")

    # Voltage of node
    voltage = Float(desc="Voltage of node")

    # The ratio of zero sequence reactance per positive sequence reactance.
    x0PerX = Float(desc="The ratio of zero sequence reactance per positive sequence reactance.")

    # True if node energized
    energized = Bool(desc="True if node energized")

    # The observability status of the node.
    observabilityFlag = Bool(desc="The observability status of the node.")

    # Net injection reactive power
    netInjectionQ = Float(desc="Net injection reactive power")

    # The ratio of zero sequence resistance to positive sequence resistance.
    r0PerR = Float(desc="The ratio of zero sequence resistance to positive sequence resistance.")

    # The short circuit apparent power drawn at this node when faulted.
    sShortCircuit = Float(desc="The short circuit apparent power drawn at this node when faulted.")

    # Phase angle of node
    phaseAngle = Float(desc="Phase angle of node")

    # The topological node is equivalent and not real equipment.
    equivalent = Bool(desc="The topological node is equivalent and not real equipment.")

    #--------------------------------------------------------------------------
    #  Begin "TopologicalNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("description", "mRID", "pathName", "localName", "aliasName", "name", "loadCarrying", "xPerR", "netInjectionP", "voltage", "x0PerX", "energized", "observabilityFlag", "netInjectionQ", "r0PerR", "sShortCircuit", "phaseAngle", "equivalent",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "BaseVoltage", "SvVoltage", "ControlArea", "ConnectivityNodes", "Terminal", "ReportingGroup", "AngleRef_TopologicalIsland", "SvInjection", "TopologicalIsland", "ConnectivityNodeContainer",
                label="References", columns=1),
            dock="tab"),
        id="CIM14r05.Topology.TopologicalNode",
        title="TopologicalNode",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TopologicalNode" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TopologicalIsland" class:
#------------------------------------------------------------------------------

class TopologicalIsland(IdentifiedObject):
    """ An electrically connected subset of the network. Topological islands can change as the current network state changes (i.e., disconnect switches, breakers, etc. change state).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A topological node belongs to a topological island
    TopologicalNodes = List(Instance("CIM14r05.Topology.TopologicalNode"),
        desc="A topological node belongs to a topological island")

    AngleRef_TopologicalNode = Instance("CIM14r05.Topology.TopologicalNode",
        transient=True,
        opposite="AngleRef_TopologicalIsland",
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

    #--------------------------------------------------------------------------
    #  Begin "TopologicalIsland" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("description", "mRID", "pathName", "localName", "aliasName", "name",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "TopologicalNodes", "AngleRef_TopologicalNode",
                label="References"),
            dock="tab"),
        id="CIM14r05.Topology.TopologicalIsland",
        title="TopologicalIsland",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TopologicalIsland" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
