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

from CIM.Core import IdentifiedObject
from CIM.Domain import ActivePower
from CIM.Domain import Voltage
from CIM.Domain import ReactivePower
from CIM.Domain import ApparentPower
from CIM.Domain import AngleRadians



from enthought.traits.api import Instance, List, Property, Bool, Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


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
    TopologicalNodes = List(Instance("CIM.Topology.TopologicalNode"),
        desc="A topological node belongs to a topological island")

    # The angle reference for the island.   Normally there is one TopologicalNode that is selected as the angle reference for each island.   Other reference schemes exist, so the association is optional.
    AngleRef_TopologicalNode = Instance("CIM.Topology.TopologicalNode",
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
                    "CIM.Topology.TopologicalNode" ]
        else:
            return []

    _topologicalnodes = Property(fget=_get_topologicalnodes)

    #--------------------------------------------------------------------------
    #  Begin "TopologicalIsland" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "TopologicalNodes", "AngleRef_TopologicalNode",
                label="References"),
            dock="tab"),
        id="CIM.Topology.TopologicalIsland",
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

    # Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
    TopologicalNode = Instance("CIM.Topology.TopologicalNode",
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
                    "CIM.Topology.TopologicalNode" ]
        else:
            return []

    _topologicalnodes = Property(fget=_get_topologicalnodes)

    # Container of this connectivity node.
    MemberOf_EquipmentContainer = Instance("CIM.Core.ConnectivityNodeContainer",
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
                    "CIM.Core.ConnectivityNodeContainer" ]
        else:
            return []

    _connectivitynodecontainers = Property(fget=_get_connectivitynodecontainers)

    # The associated name of the bus (TopologicalNode) containing the ConnectivityNode is derived by an algorithm that uses the bus name marker.
    BusNameMarker = Instance("CIM.Topology.BusNameMarker",
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
                    "CIM.Topology.BusNameMarker" ]
        else:
            return []

    _busnamemarkers = Property(fget=_get_busnamemarkers)

    # Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
    Terminals = List(Instance("CIM.Core.Terminal"),
        desc="Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.")

    #--------------------------------------------------------------------------
    #  Begin "ConnectivityNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "TopologicalNode", "MemberOf_EquipmentContainer", "BusNameMarker", "Terminals",
                label="References"),
            dock="tab"),
        id="CIM.Topology.ConnectivityNode",
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

    # Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
    ConnectivityNodes = List(Instance("CIM.Topology.ConnectivityNode"),
        desc="Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.")

    # The connectivity node container to which the toplogical node belongs.
    ConnectivityNodeContainer = Instance("CIM.Core.ConnectivityNodeContainer",
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
                    "CIM.Core.ConnectivityNodeContainer" ]
        else:
            return []

    _connectivitynodecontainers = Property(fget=_get_connectivitynodecontainers)

    # The base voltage of the topologocial node.
    BaseVoltage = Instance("CIM.Core.BaseVoltage",
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
                    "CIM.Core.BaseVoltage" ]
        else:
            return []

    _basevoltages = Property(fget=_get_basevoltages)

    # The injection state associated with the topological node.
    SvInjection = Instance("CIM.StateVariables.SvInjection",
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
                    "CIM.StateVariables.SvInjection" ]
        else:
            return []

    _svinjections = Property(fget=_get_svinjections)

    # The reporting group to which the topological node belongs.
    ReportingGroup = Instance("CIM.Core.ReportingGroup",
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
                    "CIM.Core.ReportingGroup" ]
        else:
            return []

    _reportinggroups = Property(fget=_get_reportinggroups)

    # A topological node belongs to a topological island
    TopologicalIsland = Instance("CIM.Topology.TopologicalIsland",
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
                    "CIM.Topology.TopologicalIsland" ]
        else:
            return []

    _topologicalislands = Property(fget=_get_topologicalislands)

    # The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.
    Terminal = List(Instance("CIM.Core.Terminal"),
        desc="The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.")

    # The island for which the node is an angle reference.   Normally there is one angle reference node for each island.
    AngleRef_TopologicalIsland = Instance("CIM.Topology.TopologicalIsland",
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
                    "CIM.Topology.TopologicalIsland" ]
        else:
            return []

    _topologicalislands = Property(fget=_get_topologicalislands)

    # The state voltage associated with the topological node.
    SvVoltage = Instance("CIM.StateVariables.SvVoltage",
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
                    "CIM.StateVariables.SvVoltage" ]
        else:
            return []

    _svvoltages = Property(fget=_get_svvoltages)

    # The control area into which the node is included.
    ControlArea = Instance("CIM.ControlArea.ControlArea",
        desc="The control area into which the node is included.",
        transient=True,
        opposite="TopologicalNode",
        editor=InstanceEditor(name="_controlareas"))

    def _get_controlareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.ControlArea.ControlArea" ]
        else:
            return []

    _controlareas = Property(fget=_get_controlareas)

    # The topological node is equivalent and not real equipment.
    equivalent = Bool(desc="The topological node is equivalent and not real equipment.")

    # True if node is load carrying
    loadCarrying = Bool(desc="True if node is load carrying")

    # Net injection active power
    netInjectionP = ActivePower(desc="Net injection active power")

    # Voltage of node
    voltage = Voltage(desc="Voltage of node")

    # The ratio of zero sequence reactance per positive sequence reactance.
    x0PerX = Float(desc="The ratio of zero sequence reactance per positive sequence reactance.")

    # Net injection reactive power
    netInjectionQ = ReactivePower(desc="Net injection reactive power")

    # The short circuit apparent power drawn at this node when faulted.
    sShortCircuit = ApparentPower(desc="The short circuit apparent power drawn at this node when faulted.")

    # The ratio of zero sequence resistance to positive sequence resistance.
    r0PerR = Float(desc="The ratio of zero sequence resistance to positive sequence resistance.")

    # Ratio of positive sequence reactance per postive sequence resistance.
    xPerR = Float(desc="Ratio of positive sequence reactance per postive sequence resistance.")

    # Phase angle of node
    phaseAngle = AngleRadians(desc="Phase angle of node")

    # True if node energized
    energized = Bool(desc="True if node energized")

    # The observability status of the node.
    observabilityFlag = Bool(desc="The observability status of the node.")

    #--------------------------------------------------------------------------
    #  Begin "TopologicalNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "loadCarrying", "netInjectionP", "voltage", "x0PerX", "netInjectionQ", "sShortCircuit", "r0PerR", "xPerR", "phaseAngle", "energized", "observabilityFlag",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "ConnectivityNodes", "ConnectivityNodeContainer", "BaseVoltage", "SvInjection", "ReportingGroup", "TopologicalIsland", "Terminal", "AngleRef_TopologicalIsland", "SvVoltage", "ControlArea",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Topology.TopologicalNode",
        title="TopologicalNode",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TopologicalNode" user definitions:
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

    # The list of nodes which have the same bus name in the normal  topology.  Note that this list of ConnectivityNodes should be connected by objects derived from Switch that are normally closed.
    ConnectivityNode = List(Instance("CIM.Topology.ConnectivityNode"),
        desc="The list of nodes which have the same bus name in the normal  topology.  Note that this list of ConnectivityNodes should be connected by objects derived from Switch that are normally closed.")

    # The reporting group to which this BusNameMarker belongs.
    ReportingGroup = Instance("CIM.Core.ReportingGroup",
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
                    "CIM.Core.ReportingGroup" ]
        else:
            return []

    _reportinggroups = Property(fget=_get_reportinggroups)

    # The control area into which the BusNameMarker is included.
    ControlArea = Instance("CIM.ControlArea.ControlArea",
        desc="The control area into which the BusNameMarker is included.",
        transient=True,
        opposite="BusNameMarker",
        editor=InstanceEditor(name="_controlareas"))

    def _get_controlareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.ControlArea.ControlArea" ]
        else:
            return []

    _controlareas = Property(fget=_get_controlareas)

    #--------------------------------------------------------------------------
    #  Begin "BusNameMarker" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "ConnectivityNode", "ReportingGroup", "ControlArea",
                label="References"),
            dock="tab"),
        id="CIM.Topology.BusNameMarker",
        title="BusNameMarker",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BusNameMarker" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
