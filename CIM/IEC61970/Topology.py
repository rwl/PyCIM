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

""" An extension to the Core Package that in association with the Terminal class models Connectivity, that is the physical definition of how equipment is connected together. In addition it models Topology, that is the logical definition of how equipment is connected via closed switches. The Topology definition is independent of the other electrical characteristics.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61970.Core import IdentifiedObject



from enthought.traits.api import Instance, List, Property
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

    # The list of nodes which have the same bus name in the normal  topology.  Note that this list of ConnectivityNodes should be connected by objects derived from Switch that are normally closed.
    ConnectivityNode = List(Instance("CIM.IEC61970.Topology.ConnectivityNode"),
        desc="The list of nodes which have the same bus name in the normal  topology.  Note that this list of ConnectivityNodes should be connected by objects derived from Switch that are normally closed.")

    # The reporting group to which this BusNameMarker belongs.
    ReportingGroup = Instance("CIM.IEC61970.Core.ReportingGroup",
        desc="The reporting group to which this BusNameMarker belongs.",
        transient=True,
        opposite="BusNameMarker",
        editor=InstanceEditor(name="_reportinggroups"))

    def _get_reportinggroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.ReportingGroup" ]
        else:
            return []

    _reportinggroups = Property(fget=_get_reportinggroups)

    #--------------------------------------------------------------------------
    #  Begin "BusNameMarker" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ConnectivityNode", "ReportingGroup",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Topology.BusNameMarker",
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

    Pnode = Instance("CIM.IEC61968.Informative.MarketOperations.Pnode",
        transient=True,
        opposite="ConnectivityNode",
        editor=InstanceEditor(name="_pnodes"))

    def _get_pnodes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.Pnode" ]
        else:
            return []

    _pnodes = Property(fget=_get_pnodes)

    # The associated name of the bus (TopologicalNode) containing the ConnectivityNode is derived by an algorithm that uses the bus name marker.
    BusNameMarker = Instance("CIM.IEC61970.Topology.BusNameMarker",
        desc="The associated name of the bus (TopologicalNode) containing the ConnectivityNode is derived by an algorithm that uses the bus name marker.",
        transient=True,
        opposite="ConnectivityNode",
        editor=InstanceEditor(name="_busnamemarkers"))

    def _get_busnamemarkers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Topology.BusNameMarker" ]
        else:
            return []

    _busnamemarkers = Property(fget=_get_busnamemarkers)

    LossPenaltyFactors = List(Instance("CIM.IEC61968.Informative.MarketOperations.LossPenaltyFactor"))

    # Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
    TopologicalNode = Instance("CIM.IEC61970.Topology.TopologicalNode",
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
                    "CIM.IEC61970.Topology.TopologicalNode" ]
        else:
            return []

    _topologicalnodes = Property(fget=_get_topologicalnodes)

    NodeConstraintTerms = List(Instance("CIM.IEC61968.Informative.MarketOperations.NodeConstraintTerm"))

    # Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
    Terminals = List(Instance("CIM.IEC61970.Core.Terminal"),
        desc="Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.")

    # Container of this connectivity node.
    ConnectivityNodeContainer = Instance("CIM.IEC61970.Core.ConnectivityNodeContainer",
        desc="Container of this connectivity node.",
        transient=True,
        opposite="ConnectivityNodes",
        editor=InstanceEditor(name="_connectivitynodecontainers"))

    def _get_connectivitynodecontainers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.ConnectivityNodeContainer" ]
        else:
            return []

    _connectivitynodecontainers = Property(fget=_get_connectivitynodecontainers)

    #--------------------------------------------------------------------------
    #  Begin "ConnectivityNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Pnode", "BusNameMarker", "LossPenaltyFactors", "TopologicalNode", "NodeConstraintTerms", "Terminals", "ConnectivityNodeContainer",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Topology.ConnectivityNode",
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

    # The state voltage associated with the topological node.
    SvVoltage = Instance("CIM.IEC61970.StateVariables.SvVoltage",
        desc="The state voltage associated with the topological node.",
        transient=True,
        opposite="TopologicalNode",
        editor=InstanceEditor(name="_svvoltages"))

    def _get_svvoltages(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.StateVariables.SvVoltage" ]
        else:
            return []

    _svvoltages = Property(fget=_get_svvoltages)

    # The reporting group to which the topological node belongs.
    ReportingGroup = Instance("CIM.IEC61970.Core.ReportingGroup",
        desc="The reporting group to which the topological node belongs.",
        transient=True,
        opposite="TopologicalNode",
        editor=InstanceEditor(name="_reportinggroups"))

    def _get_reportinggroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.ReportingGroup" ]
        else:
            return []

    _reportinggroups = Property(fget=_get_reportinggroups)

    # The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.
    Terminal = List(Instance("CIM.IEC61970.Core.Terminal"),
        desc="The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.")

    # The short circuit state associated with the topological node.
    SvShortCircuit = Instance("CIM.IEC61970.StateVariables.SvShortCircuit",
        desc="The short circuit state associated with the topological node.",
        transient=True,
        opposite="TopologicalNode",
        editor=InstanceEditor(name="_svshortcircuits"))

    def _get_svshortcircuits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.StateVariables.SvShortCircuit" ]
        else:
            return []

    _svshortcircuits = Property(fget=_get_svshortcircuits)

    # The injection state associated with the topological node.
    SvInjection = Instance("CIM.IEC61970.StateVariables.SvInjection",
        desc="The injection state associated with the topological node.",
        transient=True,
        opposite="TopologicalNode",
        editor=InstanceEditor(name="_svinjections"))

    def _get_svinjections(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.StateVariables.SvInjection" ]
        else:
            return []

    _svinjections = Property(fget=_get_svinjections)

    # The island for which the node is an angle reference.   Normally there is one angle reference node for each island.
    AngleRef_TopologicalIsland = Instance("CIM.IEC61970.Topology.TopologicalIsland",
        desc="The island for which the node is an angle reference.   Normally there is one angle reference node for each island.",
        transient=True,
        opposite="AngleRef_TopologicalNode",
        editor=InstanceEditor(name="_topologicalislands"))

    def _get_topologicalislands(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Topology.TopologicalIsland" ]
        else:
            return []

    _topologicalislands = Property(fget=_get_topologicalislands)

    # Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
    ConnectivityNodes = List(Instance("CIM.IEC61970.Topology.ConnectivityNode"),
        desc="Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.")

    # The connectivity node container to which the toplogical node belongs.
    ConnectivityNodeContainer = Instance("CIM.IEC61970.Core.ConnectivityNodeContainer",
        desc="The connectivity node container to which the toplogical node belongs.",
        transient=True,
        opposite="TopologicalNode",
        editor=InstanceEditor(name="_connectivitynodecontainers"))

    def _get_connectivitynodecontainers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.ConnectivityNodeContainer" ]
        else:
            return []

    _connectivitynodecontainers = Property(fget=_get_connectivitynodecontainers)

    # The base voltage of the topologocial node.
    BaseVoltage = Instance("CIM.IEC61970.Core.BaseVoltage",
        desc="The base voltage of the topologocial node.",
        transient=True,
        opposite="TopologicalNode",
        editor=InstanceEditor(name="_basevoltages"))

    def _get_basevoltages(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.BaseVoltage" ]
        else:
            return []

    _basevoltages = Property(fget=_get_basevoltages)

    # A topological node belongs to a topological island
    TopologicalIsland = Instance("CIM.IEC61970.Topology.TopologicalIsland",
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
                    "CIM.IEC61970.Topology.TopologicalIsland" ]
        else:
            return []

    _topologicalislands = Property(fget=_get_topologicalislands)

    #--------------------------------------------------------------------------
    #  Begin "TopologicalNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "SvVoltage", "ReportingGroup", "Terminal", "SvShortCircuit", "SvInjection", "AngleRef_TopologicalIsland", "ConnectivityNodes", "ConnectivityNodeContainer", "BaseVoltage", "TopologicalIsland",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61970.Topology.TopologicalNode",
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

    # The angle reference for the island.   Normally there is one TopologicalNode that is selected as the angle reference for each island.   Other reference schemes exist, so the association is optional.
    AngleRef_TopologicalNode = Instance("CIM.IEC61970.Topology.TopologicalNode",
        desc="The angle reference for the island.   Normally there is one TopologicalNode that is selected as the angle reference for each island.   Other reference schemes exist, so the association is optional.",
        transient=True,
        opposite="AngleRef_TopologicalIsland",
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

    # A topological node belongs to a topological island
    TopologicalNodes = List(Instance("CIM.IEC61970.Topology.TopologicalNode"),
        desc="A topological node belongs to a topological island")

    #--------------------------------------------------------------------------
    #  Begin "TopologicalIsland" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "AngleRef_TopologicalNode", "TopologicalNodes",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Topology.TopologicalIsland",
        title="TopologicalIsland",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TopologicalIsland" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
