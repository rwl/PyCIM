# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM14.IEC61970.StateVariables.StateVariable import StateVariable

class SvVoltage(StateVariable):
    """State variable for voltage.
    """

    def __init__(self, angle=0.0, v=0.0, TopologicalNode=None, *args, **kw_args):
        """Initialises a new 'SvVoltage' instance.

        @param angle: The voltage angle in radians of the topological node. 
        @param v: The voltage magnitude of the topological node. 
        @param TopologicalNode: The topological node associated with the voltage state.
        """
        #: The voltage angle in radians of the topological node.
        self.angle = angle

        #: The voltage magnitude of the topological node.
        self.v = v

        self._TopologicalNode = None
        self.TopologicalNode = TopologicalNode

        super(SvVoltage, self).__init__(*args, **kw_args)

    _attrs = ["angle", "v"]
    _attr_types = {"angle": float, "v": float}
    _defaults = {"angle": 0.0, "v": 0.0}
    _enums = {}
    _refs = ["TopologicalNode"]
    _many_refs = []

    def getTopologicalNode(self):
        """The topological node associated with the voltage state.
        """
        return self._TopologicalNode

    def setTopologicalNode(self, value):
        if self._TopologicalNode is not None:
            self._TopologicalNode._SvVoltage = None

        self._TopologicalNode = value
        if self._TopologicalNode is not None:
            self._TopologicalNode.SvVoltage = None
            self._TopologicalNode._SvVoltage = self

    TopologicalNode = property(getTopologicalNode, setTopologicalNode)

