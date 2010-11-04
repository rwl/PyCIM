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

class SvVoltage(StateVariable):
    """State variable for voltage.
    """

    def __init__(self, v=0.0, angle=0.0, TopologicalNode=None, **kw_args):
        """Initializes a new 'SvVoltage' instance.

        @param v: The voltage magnitude of the topological node. 
        @param angle: The voltage angle in radians of the topological node. 
        @param TopologicalNode: The topological node associated with the voltage state.
        """
        #: The voltage magnitude of the topological node.
        self.v = v

        #: The voltage angle in radians of the topological node.
        self.angle = angle

        self._TopologicalNode = None
        self.TopologicalNode = TopologicalNode

        super(SvVoltage, self).__init__(**kw_args)

    def getTopologicalNode(self):
        """The topological node associated with the voltage state.
        """
        return self._TopologicalNode

    def setTopologicalNode(self, value):
        if self._TopologicalNode is not None:
            self._TopologicalNode._SvVoltage = None

        self._TopologicalNode = value
        if self._TopologicalNode is not None:
            self._TopologicalNode._SvVoltage = self

    TopologicalNode = property(getTopologicalNode, setTopologicalNode)

