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

from CIM13r19.Core import IdentifiedObject



from enthought.traits.api import Instance, List, Property, Bool, Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "TopologicalNode" class:
#------------------------------------------------------------------------------

class TopologicalNode(IdentifiedObject):
    """ A set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes can change as the current network state changes (i.e., switches, breakers, etc. change state).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ReportingGroup = Instance("CIM13r19.Core.ReportingGroup",
        transient=True,
        opposite="TopologicalNode",
        editor=InstanceEditor(name="_reportinggroups"))

    def _get_reportinggroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.ReportingGroup" ]
        else:
            return []

    _reportinggroups = Property(fget=_get_reportinggroups)

    AngleRef_TopologicalIsland = Instance("CIM13r19.Topology.TopologicalIsland",
        transient=True,
        opposite="AngleRef_TopologicalNode",
        editor=InstanceEditor(name="_topologicalislands"))

    def _get_topologicalislands(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Topology.TopologicalIsland" ]
        else:
            return []

    _topologicalislands = Property(fget=_get_topologicalislands)

    ConnectivityNodeContainer = Instance("CIM13r19.Core.ConnectivityNodeContainer",
        transient=True,
        opposite="TopologicalNode",
        editor=InstanceEditor(name="_connectivitynodecontainers"))

    def _get_connectivitynodecontainers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.ConnectivityNodeContainer" ]
        else:
            return []

    _connectivitynodecontainers = Property(fget=_get_connectivitynodecontainers)

    # A topological node belongs to a topological island
    TopologicalIsland = Instance("CIM13r19.Topology.TopologicalIsland",
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
                    "CIM13r19.Topology.TopologicalIsland" ]
        else:
            return []

    _topologicalislands = Property(fget=_get_topologicalislands)

    # Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
    ConnectivityNodes = List(Instance("CIM13r19.Topology.ConnectivityNode"),
        desc="Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.")

    Terminal = List(Instance("CIM13r19.Core.Terminal"))

    ControlArea = Instance("CIM13r19.ControlArea.ControlArea",
        transient=True,
        opposite="TopologicalNode",
        editor=InstanceEditor(name="_controlareas"))

    def _get_controlareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.ControlArea.ControlArea" ]
        else:
            return []

    _controlareas = Property(fget=_get_controlareas)

    # True if node energized
    energized = Bool(desc="True if node energized")

    # Net injection active power
    netInjectionP = Float(desc="Net injection active power")

    # Net injection reactive power
    netInjectionQ = Float(desc="Net injection reactive power")

    # Phase angle of node
    phaseAngle = Float(desc="Phase angle of node")

    # The observability status of the node.
    observabilityFlag = Bool(desc="The observability status of the node.")

    # Voltage of node
    voltage = Float(desc="Voltage of node")

    # True if node is load carrying
    loadCarrying = Bool(desc="True if node is load carrying")

    #--------------------------------------------------------------------------
    #  Begin "TopologicalNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "energized", "netInjectionP", "netInjectionQ", "phaseAngle", "observabilityFlag", "voltage", "loadCarrying",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ReportingGroup", "AngleRef_TopologicalIsland", "ConnectivityNodeContainer", "TopologicalIsland", "ConnectivityNodes", "Terminal", "ControlArea",
                label="References"),
            dock="tab"),
        id="CIM13r19.Topology.TopologicalNode",
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

    AngleRef_TopologicalNode = Instance("CIM13r19.Topology.TopologicalNode",
        transient=True,
        opposite="AngleRef_TopologicalIsland",
        editor=InstanceEditor(name="_topologicalnodes"))

    def _get_topologicalnodes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Topology.TopologicalNode" ]
        else:
            return []

    _topologicalnodes = Property(fget=_get_topologicalnodes)

    # A topological node belongs to a topological island
    TopologicalNodes = List(Instance("CIM13r19.Topology.TopologicalNode"),
        desc="A topological node belongs to a topological island")

    #--------------------------------------------------------------------------
    #  Begin "TopologicalIsland" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "AngleRef_TopologicalNode", "TopologicalNodes",
                label="References"),
            dock="tab"),
        id="CIM13r19.Topology.TopologicalIsland",
        title="TopologicalIsland",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TopologicalIsland" user definitions:
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

    MemberOf_EquipmentContainer = Instance("CIM13r19.Core.ConnectivityNodeContainer",
        transient=True,
        opposite="ConnectivityNodes",
        editor=InstanceEditor(name="_connectivitynodecontainers"))

    def _get_connectivitynodecontainers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.ConnectivityNodeContainer" ]
        else:
            return []

    _connectivitynodecontainers = Property(fget=_get_connectivitynodecontainers)

    BusNameMarker = Instance("CIM13r19.Topology.BusNameMarker",
        transient=True,
        opposite="ConnectivityNode",
        editor=InstanceEditor(name="_busnamemarkers"))

    def _get_busnamemarkers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Topology.BusNameMarker" ]
        else:
            return []

    _busnamemarkers = Property(fget=_get_busnamemarkers)

    # Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
    Terminals = List(Instance("CIM13r19.Core.Terminal"),
        desc="Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.")

    # Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
    TopologicalNode = Instance("CIM13r19.Topology.TopologicalNode",
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
                    "CIM13r19.Topology.TopologicalNode" ]
        else:
            return []

    _topologicalnodes = Property(fget=_get_topologicalnodes)

    #--------------------------------------------------------------------------
    #  Begin "ConnectivityNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "MemberOf_EquipmentContainer", "BusNameMarker", "Terminals", "TopologicalNode",
                label="References"),
            dock="tab"),
        id="CIM13r19.Topology.ConnectivityNode",
        title="ConnectivityNode",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConnectivityNode" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BusNameMarker" class:
#------------------------------------------------------------------------------

class BusNameMarker(IdentifiedObject):
    """ Used to apply user standard names to topology buses. Typically used for 'bus/branch' case generation. Associated with one or more ConnectivityNodes that are normally a part of the bus name.    The associated ConnectivityNodes are to be connected by non-retained switches. For a ring bus station configuration, all busbar connectivity nodes in the ring are typically associated.   For a breaker and a half scheme, both busbars would be associated.  For a ring bus, all busbars would be associated.  For a 'straight' busbar configuration, only the main connectivity node at the busbar would be associated.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ControlArea = Instance("CIM13r19.ControlArea.ControlArea",
        transient=True,
        opposite="BusNameMarker",
        editor=InstanceEditor(name="_controlareas"))

    def _get_controlareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.ControlArea.ControlArea" ]
        else:
            return []

    _controlareas = Property(fget=_get_controlareas)

    ConnectivityNode = List(Instance("CIM13r19.Topology.ConnectivityNode"))

    ReportingGroup = Instance("CIM13r19.Core.ReportingGroup",
        transient=True,
        opposite="BusNameMarker",
        editor=InstanceEditor(name="_reportinggroups"))

    def _get_reportinggroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.ReportingGroup" ]
        else:
            return []

    _reportinggroups = Property(fget=_get_reportinggroups)

    #--------------------------------------------------------------------------
    #  Begin "BusNameMarker" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ControlArea", "ConnectivityNode", "ReportingGroup",
                label="References"),
            dock="tab"),
        id="CIM13r19.Topology.BusNameMarker",
        title="BusNameMarker",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BusNameMarker" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
