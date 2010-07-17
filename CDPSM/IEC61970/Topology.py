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

from CDPSM.IEC61970.Core import IdentifiedObject



from enthought.traits.api import Instance, List, Property
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "ConnectivityNode" class:
#------------------------------------------------------------------------------

class ConnectivityNode(IdentifiedObject):
    """ Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance.Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
    Terminals = List(Instance("CDPSM.IEC61970.Core.Terminal"),
        desc="Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.")

    # Container of this connectivity node.Container of this connectivity node.
    ConnectivityNodeContainer = Instance("CDPSM.IEC61970.Core.ConnectivityNodeContainer",
        desc="Container of this connectivity node.Container of this connectivity node.",
        transient=True,
        opposite="ConnectivityNodes",
        editor=InstanceEditor(name="_connectivitynodecontainers"))

    def _get_connectivitynodecontainers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61970.Core.ConnectivityNodeContainer" ]
        else:
            return []

    _connectivitynodecontainers = Property(fget=_get_connectivitynodecontainers)

    #--------------------------------------------------------------------------
    #  Begin "ConnectivityNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "mRID", "description", "name", "localName", "aliasName",
                label="Attributes"),
            VGroup("Model", "Terminals", "ConnectivityNodeContainer",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Topology.ConnectivityNode",
        title="ConnectivityNode",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConnectivityNode" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
