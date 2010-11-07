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

from CIM14.IEC61970.StateVariables.StateVariable import StateVariable

class SvInjection(StateVariable):
    """Injection state variable.
    """

    def __init__(self, pNetInjection=0.0, qNetInjection=0.0, TopologicalNode=None, **kw_args):
        """Initializes a new 'SvInjection' instance.

        @param pNetInjection: The active power injected into the bus at this location.  Positive sign means injection into the bus. 
        @param qNetInjection: The reactive power injected into the bus at this location. Positive sign means injection into the bus. 
        @param TopologicalNode: The topological node associated with the state injection.
        """
        #: The active power injected into the bus at this location.  Positive sign means injection into the bus.
        self.pNetInjection = pNetInjection

        #: The reactive power injected into the bus at this location. Positive sign means injection into the bus.
        self.qNetInjection = qNetInjection

        self._TopologicalNode = None
        self.TopologicalNode = TopologicalNode

        super(SvInjection, self).__init__(**kw_args)

    def getTopologicalNode(self):
        """The topological node associated with the state injection.
        """
        return self._TopologicalNode

    def setTopologicalNode(self, value):
        if self._TopologicalNode is not None:
            self._TopologicalNode._SvInjection = None

        self._TopologicalNode = value
        if self._TopologicalNode is not None:
            self._TopologicalNode._SvInjection = self

    TopologicalNode = property(getTopologicalNode, setTopologicalNode)

