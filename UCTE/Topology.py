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

""" An extension to the Core Package that in association with the Terminal class models Connectivity, that is the physical definition of how equipment is connected together. In addition it models Topology, that is the logical definition of how equipment is connected via closed switches. The Topology definition is independent of the other electrical characteristics.An extension to the Core Package that in association with the Terminal class models Connectivity, that is the physical definition of how equipment is connected together. In addition it models Topology, that is the logical definition of how equipment is connected via closed switches. The Topology definition is independent of the other electrical characteristics.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from UCTE.Core import IdentifiedObject
from UCTE.Domain import ApparentPower



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
    """ A set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes can change as the current network state changes (i.e., switches, breakers, etc. change state).A set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes can change as the current network state changes (i.e., switches, breakers, etc. change state).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The control area into which the node is included.The control area into which the node is included.
    ControlArea = Instance("UCTE.ControlArea.ControlArea", allow_none=False,
        desc="The control area into which the node is included.The control area into which the node is included.",
        transient=True,
        opposite="TopologicalNode",
        editor=InstanceEditor(name="_controlareas"))

    def _get_controlareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.ControlArea.ControlArea" ]
        else:
            return []

    _controlareas = Property(fget=_get_controlareas)

    # The base voltage of the topologocial node.The base voltage of the TopologicalNode should match the BaseVoltage of the containing VoltageLevel if such a containing VoltageLevel is specified.The base voltage of the topologocial node.The base voltage of the TopologicalNode should match the BaseVoltage of the containing VoltageLevel if such a containing VoltageLevel is specified.
    BaseVoltage = Instance("UCTE.Core.BaseVoltage", allow_none=False,
        desc="The base voltage of the topologocial node.The base voltage of the TopologicalNode should match the BaseVoltage of the containing VoltageLevel if such a containing VoltageLevel is specified.The base voltage of the topologocial node.The base voltage of the TopologicalNode should match the BaseVoltage of the containing VoltageLevel if such a containing VoltageLevel is specified.",
        transient=True,
        opposite="TopologicalNode",
        editor=InstanceEditor(name="_basevoltages"))

    def _get_basevoltages(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Core.BaseVoltage" ]
        else:
            return []

    _basevoltages = Property(fget=_get_basevoltages)

    # The state voltage associated with the topological node.The state voltage associated with the topological node.
    SvVoltage = Instance("UCTE.StateVariables.SvVoltage",
        desc="The state voltage associated with the topological node.The state voltage associated with the topological node.",
        transient=True,
        opposite="TopologicalNode",
        editor=InstanceEditor(name="_svvoltages"))

    def _get_svvoltages(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.StateVariables.SvVoltage" ]
        else:
            return []

    _svvoltages = Property(fget=_get_svvoltages)

    # A topological node belongs to a topological islandA topological node belongs to a topological island
    TopologicalIsland = Instance("UCTE.Topology.TopologicalIsland", allow_none=False,
        desc="A topological node belongs to a topological islandA topological node belongs to a topological island",
        transient=True,
        opposite="TopologicalNodes",
        editor=InstanceEditor(name="_topologicalislands"))

    def _get_topologicalislands(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Topology.TopologicalIsland" ]
        else:
            return []

    _topologicalislands = Property(fget=_get_topologicalislands)

    # The island for which the node is an angle reference.   Normally there is one angle reference node for each island.The island for which the node is an angle reference.   Normally there is one angle reference node for each island.
    AngleRef_TopologicalIsland = Instance("UCTE.Topology.TopologicalIsland",
        desc="The island for which the node is an angle reference.   Normally there is one angle reference node for each island.The island for which the node is an angle reference.   Normally there is one angle reference node for each island.",
        transient=True,
        opposite="AngleRef_TopologicalNode",
        editor=InstanceEditor(name="_topologicalislands"))

    def _get_topologicalislands(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Topology.TopologicalIsland" ]
        else:
            return []

    _topologicalislands = Property(fget=_get_topologicalislands)

    # The connectivity node container to which the toplogical node belongs.The TopologicalNode will normally belong only to a VoltageLevel instance within a Substation.   All instances of TopologicalNode that are not X-nodes will require an association to a containing VoltageLevel instance.  The BaseVoltage of the VoltageLevel should match that of the TopologicalNode itself. A TopologicalNode object used for an X-node will not be contained, thus this association is specified as optional in the profile.The connectivity node container to which the toplogical node belongs.The TopologicalNode will normally belong only to a VoltageLevel instance within a Substation.   All instances of TopologicalNode that are not X-nodes will require an association to a containing VoltageLevel instance.  The BaseVoltage of the VoltageLevel should match that of the TopologicalNode itself. A TopologicalNode object used for an X-node will not be contained, thus this association is specified as optional in the profile.
    ConnectivityNodeContainer = Instance("UCTE.Core.ConnectivityNodeContainer",
        desc="The connectivity node container to which the toplogical node belongs.The TopologicalNode will normally belong only to a VoltageLevel instance within a Substation.   All instances of TopologicalNode that are not X-nodes will require an association to a containing VoltageLevel instance.  The BaseVoltage of the VoltageLevel should match that of the TopologicalNode itself. A TopologicalNode object used for an X-node will not be contained, thus this association is specified as optional in the profile.The connectivity node container to which the toplogical node belongs.The TopologicalNode will normally belong only to a VoltageLevel instance within a Substation.   All instances of TopologicalNode that are not X-nodes will require an association to a containing VoltageLevel instance.  The BaseVoltage of the VoltageLevel should match that of the TopologicalNode itself. A TopologicalNode object used for an X-node will not be contained, thus this association is specified as optional in the profile.",
        transient=True,
        opposite="TopologicalNode",
        editor=InstanceEditor(name="_connectivitynodecontainers"))

    def _get_connectivitynodecontainers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Core.ConnectivityNodeContainer" ]
        else:
            return []

    _connectivitynodecontainers = Property(fget=_get_connectivitynodecontainers)

    # The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.
    Terminal = List(Instance("UCTE.Core.Terminal"),
        desc="The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.")

    # The short circuit apparent power drawn at this node when faulted.This is for Short Circuit only.The short circuit apparent power drawn at this node when faulted.This is for Short Circuit only.
    sShortCircuit = ApparentPower(desc="The short circuit apparent power drawn at this node when faulted.This is for Short Circuit only.The short circuit apparent power drawn at this node when faulted.This is for Short Circuit only.")

    # The topological node is equivalent and not real equipment.If this is missing, it is assumed to be False.  If it is an X-Node, this equivalent is required.The topological node is equivalent and not real equipment.If this is missing, it is assumed to be False.  If it is an X-Node, this equivalent is required.
    equivalent = Bool(desc="The topological node is equivalent and not real equipment.If this is missing, it is assumed to be False.  If it is an X-Node, this equivalent is required.The topological node is equivalent and not real equipment.If this is missing, it is assumed to be False.  If it is an X-Node, this equivalent is required.")

    # The ratio of zero sequence reactance per positive sequence reactance.This is for Short Circuit only.The ratio of zero sequence reactance per positive sequence reactance.This is for Short Circuit only.
    x0PerX = Float(desc="The ratio of zero sequence reactance per positive sequence reactance.This is for Short Circuit only.The ratio of zero sequence reactance per positive sequence reactance.This is for Short Circuit only.")

    # The ratio of zero sequence resistance to positive sequence resistance.This is for Short Circuit only.The ratio of zero sequence resistance to positive sequence resistance.This is for Short Circuit only.
    r0PerR = Float(desc="The ratio of zero sequence resistance to positive sequence resistance.This is for Short Circuit only.The ratio of zero sequence resistance to positive sequence resistance.This is for Short Circuit only.")

    # Ratio of positive sequence reactance per postive sequence resistance.This is for Short Circuit only.Ratio of positive sequence reactance per postive sequence resistance.This is for Short Circuit only.
    xPerR = Float(desc="Ratio of positive sequence reactance per postive sequence resistance.This is for Short Circuit only.Ratio of positive sequence reactance per postive sequence resistance.This is for Short Circuit only.")

    #--------------------------------------------------------------------------
    #  Begin "TopologicalNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "description", "name", "aliasName", "sShortCircuit", "equivalent", "x0PerX", "r0PerR", "xPerR",
                label="Attributes"),
            VGroup("Model", "ControlArea", "BaseVoltage", "SvVoltage", "TopologicalIsland", "AngleRef_TopologicalIsland", "ConnectivityNodeContainer", "Terminal",
                label="References"),
            dock="tab"),
        id="UCTE.Topology.TopologicalNode",
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
    """ An electrically connected subset of the network. Topological islands can change as the current network state changes (i.e., disconnect switches, breakers, etc. change state).An electrically connected subset of the network. Topological islands can change as the current network state changes (i.e., disconnect switches, breakers, etc. change state).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A topological node belongs to a topological islandA topological node belongs to a topological island
    TopologicalNodes = List(Instance("UCTE.Topology.TopologicalNode"),
        desc="A topological node belongs to a topological islandA topological node belongs to a topological island")

    # The angle reference for the island.   Normally there is one TopologicalNode that is selected as the angle reference for each island.   Other reference schemes exist, so the association is optional.The angle reference for the island.   Normally there is one TopologicalNode that is selected as the angle reference for each island.   Other reference schemes exist, so the association is optional.
    AngleRef_TopologicalNode = Instance("UCTE.Topology.TopologicalNode",
        desc="The angle reference for the island.   Normally there is one TopologicalNode that is selected as the angle reference for each island.   Other reference schemes exist, so the association is optional.The angle reference for the island.   Normally there is one TopologicalNode that is selected as the angle reference for each island.   Other reference schemes exist, so the association is optional.",
        transient=True,
        opposite="AngleRef_TopologicalIsland",
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

    #--------------------------------------------------------------------------
    #  Begin "TopologicalIsland" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "description", "name", "aliasName",
                label="Attributes"),
            VGroup("Model", "TopologicalNodes", "AngleRef_TopologicalNode",
                label="References"),
            dock="tab"),
        id="UCTE.Topology.TopologicalIsland",
        title="TopologicalIsland",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TopologicalIsland" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
