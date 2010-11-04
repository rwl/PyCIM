# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61968.Informative.MarketOperations.ConstraintTerm import ConstraintTerm

class NodeConstraintTerm(ConstraintTerm):
    """To be used only to constrain a quantity that cannot be associated with a terminal. For example, a registered generating unit that is not electrically connected to the network.
    """

    def __init__(self, ConnectivityNode=None, **kw_args):
        """Initializes a new 'NodeConstraintTerm' instance.

        @param ConnectivityNode:
        """
        self._ConnectivityNode = None
        self.ConnectivityNode = ConnectivityNode

        super(NodeConstraintTerm, self).__init__(**kw_args)

    def getConnectivityNode(self):
        
        return self._ConnectivityNode

    def setConnectivityNode(self, value):
        if self._ConnectivityNode is not None:
            filtered = [x for x in self.ConnectivityNode.NodeConstraintTerms if x != self]
            self._ConnectivityNode._NodeConstraintTerms = filtered

        self._ConnectivityNode = value
        if self._ConnectivityNode is not None:
            self._ConnectivityNode._NodeConstraintTerms.append(self)

    ConnectivityNode = property(getConnectivityNode, setConnectivityNode)

