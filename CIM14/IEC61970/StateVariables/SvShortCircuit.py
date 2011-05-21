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

class SvShortCircuit(StateVariable):
    """State variable for short circuit.
    """

    def __init__(self, x0PerX=0.0, sShortCircuit=0.0, r0PerR=0.0, xPerR=0.0, TopologicalNode=None, *args, **kw_args):
        """Initialises a new 'SvShortCircuit' instance.

        @param x0PerX: The ratio of zero sequence reactance per positive sequence reactance. 
        @param sShortCircuit: The short circuit apparent power drawn at this node when faulted. 
        @param r0PerR: The ratio of zero sequence resistance to positive sequence resistance. 
        @param xPerR: Ratio of positive sequence reactance per postive sequence resistance. 
        @param TopologicalNode: The topological node associated with the short circuit state.
        """
        #: The ratio of zero sequence reactance per positive sequence reactance.
        self.x0PerX = x0PerX

        #: The short circuit apparent power drawn at this node when faulted.
        self.sShortCircuit = sShortCircuit

        #: The ratio of zero sequence resistance to positive sequence resistance.
        self.r0PerR = r0PerR

        #: Ratio of positive sequence reactance per postive sequence resistance.
        self.xPerR = xPerR

        self._TopologicalNode = None
        self.TopologicalNode = TopologicalNode

        super(SvShortCircuit, self).__init__(*args, **kw_args)

    _attrs = ["x0PerX", "sShortCircuit", "r0PerR", "xPerR"]
    _attr_types = {"x0PerX": float, "sShortCircuit": float, "r0PerR": float, "xPerR": float}
    _defaults = {"x0PerX": 0.0, "sShortCircuit": 0.0, "r0PerR": 0.0, "xPerR": 0.0}
    _enums = {}
    _refs = ["TopologicalNode"]
    _many_refs = []

    def getTopologicalNode(self):
        """The topological node associated with the short circuit state.
        """
        return self._TopologicalNode

    def setTopologicalNode(self, value):
        if self._TopologicalNode is not None:
            self._TopologicalNode._SvShortCircuit = None

        self._TopologicalNode = value
        if self._TopologicalNode is not None:
            self._TopologicalNode.SvShortCircuit = None
            self._TopologicalNode._SvShortCircuit = self

    TopologicalNode = property(getTopologicalNode, setTopologicalNode)

