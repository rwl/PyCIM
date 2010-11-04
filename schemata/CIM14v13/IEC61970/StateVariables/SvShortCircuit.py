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

from CIM14v13.IEC61970.StateVariables.StateVariable import StateVariable

class SvShortCircuit(StateVariable):
    """State variable for short circuit.
    """

    def __init__(self, xPerR=0.0, r0PerR=0.0, sShortCircuit=0.0, x0PerX=0.0, TopologicalNode=None, *args, **kw_args):
        """Initializes a new 'SvShortCircuit' instance.

        @param xPerR: Ratio of positive sequence reactance per postive sequence resistance. 
        @param r0PerR: The ratio of zero sequence resistance to positive sequence resistance. 
        @param sShortCircuit: The short circuit apparent power drawn at this node when faulted. 
        @param x0PerX: The ratio of zero sequence reactance per positive sequence reactance. 
        @param TopologicalNode: The topological node associated with the short circuit state.
        """
        #: Ratio of positive sequence reactance per postive sequence resistance.
        self.xPerR = xPerR

        #: The ratio of zero sequence resistance to positive sequence resistance.
        self.r0PerR = r0PerR

        #: The short circuit apparent power drawn at this node when faulted.
        self.sShortCircuit = sShortCircuit

        #: The ratio of zero sequence reactance per positive sequence reactance.
        self.x0PerX = x0PerX

        self._TopologicalNode = None
        self.TopologicalNode = TopologicalNode

        super(SvShortCircuit, self).__init__(*args, **kw_args)

    def getTopologicalNode(self):
        """The topological node associated with the short circuit state.
        """
        return self._TopologicalNode

    def setTopologicalNode(self, value):
        if self._TopologicalNode is not None:
            self._TopologicalNode._SvShortCircuit = None

        self._TopologicalNode = value
        if self._TopologicalNode is not None:
            self._TopologicalNode._SvShortCircuit = self

    TopologicalNode = property(getTopologicalNode, setTopologicalNode)

