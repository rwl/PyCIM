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

from CIM14.ENTSOE.StateVariables.Element import Element

class TopologicalNode(Element):
    """For a detailed substation model a TopologicalNode is a set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes changes as the current network state changes (i.e., switches, breakers, etc. change state). For a planning model switch statuses are not used to form TopologicalNodes. Instead they are manually created or deleted in a model builder tool. TopologialNodes maintained this way are also called 'busses'.
    """

    def __init__(self, SvShortCircuit=None, SvVoltage=None, SvInjection=None, *args, **kw_args):
        """Initialises a new 'TopologicalNode' instance.

        @param SvShortCircuit: The short circuit state associated with the topological node.
        @param SvVoltage: The state voltage associated with the topological node.
        @param SvInjection: The injection state associated with the topological node.
        """
        self._SvShortCircuit = None
        self.SvShortCircuit = SvShortCircuit

        self._SvVoltage = None
        self.SvVoltage = SvVoltage

        self._SvInjection = None
        self.SvInjection = SvInjection

        super(TopologicalNode, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["SvShortCircuit", "SvVoltage", "SvInjection"]
    _many_refs = []

    def getSvShortCircuit(self):
        """The short circuit state associated with the topological node.
        """
        return self._SvShortCircuit

    def setSvShortCircuit(self, value):
        if self._SvShortCircuit is not None:
            self._SvShortCircuit._TopologicalNode = None

        self._SvShortCircuit = value
        if self._SvShortCircuit is not None:
            self._SvShortCircuit.TopologicalNode = None
            self._SvShortCircuit._TopologicalNode = self

    SvShortCircuit = property(getSvShortCircuit, setSvShortCircuit)

    def getSvVoltage(self):
        """The state voltage associated with the topological node.
        """
        return self._SvVoltage

    def setSvVoltage(self, value):
        if self._SvVoltage is not None:
            self._SvVoltage._TopologicalNode = None

        self._SvVoltage = value
        if self._SvVoltage is not None:
            self._SvVoltage.TopologicalNode = None
            self._SvVoltage._TopologicalNode = self

    SvVoltage = property(getSvVoltage, setSvVoltage)

    def getSvInjection(self):
        """The injection state associated with the topological node.
        """
        return self._SvInjection

    def setSvInjection(self, value):
        if self._SvInjection is not None:
            self._SvInjection._TopologicalNode = None

        self._SvInjection = value
        if self._SvInjection is not None:
            self._SvInjection.TopologicalNode = None
            self._SvInjection._TopologicalNode = self

    SvInjection = property(getSvInjection, setSvInjection)

