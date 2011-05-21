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

from CIM14.CPSM.StateVariables.Element import Element

class SvInjection(Element):
    """Injection state variable.
    """

    def __init__(self, qNetInjection=0.0, pNetInjection=0.0, TopologicalNode=None, *args, **kw_args):
        """Initialises a new 'SvInjection' instance.

        @param qNetInjection: The reactive power injected into the bus at this location. Positive sign means injection into the bus. 
        @param pNetInjection: The active power injected into the bus at this location.  Positive sign means injection into the bus. 
        @param TopologicalNode: The topological node associated with the state injection.
        """
        #: The reactive power injected into the bus at this location. Positive sign means injection into the bus.
        self.qNetInjection = qNetInjection

        #: The active power injected into the bus at this location.  Positive sign means injection into the bus.
        self.pNetInjection = pNetInjection

        self._TopologicalNode = None
        self.TopologicalNode = TopologicalNode

        super(SvInjection, self).__init__(*args, **kw_args)

    _attrs = ["qNetInjection", "pNetInjection"]
    _attr_types = {"qNetInjection": float, "pNetInjection": float}
    _defaults = {"qNetInjection": 0.0, "pNetInjection": 0.0}
    _enums = {}
    _refs = ["TopologicalNode"]
    _many_refs = []

    def getTopologicalNode(self):
        """The topological node associated with the state injection.
        """
        return self._TopologicalNode

    def setTopologicalNode(self, value):
        if self._TopologicalNode is not None:
            self._TopologicalNode._SvInjection = None

        self._TopologicalNode = value
        if self._TopologicalNode is not None:
            self._TopologicalNode.SvInjection = None
            self._TopologicalNode._SvInjection = self

    TopologicalNode = property(getTopologicalNode, setTopologicalNode)

