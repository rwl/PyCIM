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

from CIM14.CPSM.Equipment.Core.Equipment import Equipment

class PowerTransformer(Equipment):
    """An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).A PowerTransformer can be either two winding or three winding. -  A two winding transformer has two TransformerWindings -  A three winding transformer has three TransformerWindings 
    """

    def __init__(self, TransformerWindings=None, *args, **kw_args):
        """Initialises a new 'PowerTransformer' instance.

        @param TransformerWindings: A transformer has windings
        """
        self._TransformerWindings = []
        self.TransformerWindings = [] if TransformerWindings is None else TransformerWindings

        super(PowerTransformer, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["TransformerWindings"]
    _many_refs = ["TransformerWindings"]

    def getTransformerWindings(self):
        """A transformer has windings
        """
        return self._TransformerWindings

    def setTransformerWindings(self, value):
        for x in self._TransformerWindings:
            x.PowerTransformer = None
        for y in value:
            y._PowerTransformer = self
        self._TransformerWindings = value

    TransformerWindings = property(getTransformerWindings, setTransformerWindings)

    def addTransformerWindings(self, *TransformerWindings):
        for obj in TransformerWindings:
            obj.PowerTransformer = self

    def removeTransformerWindings(self, *TransformerWindings):
        for obj in TransformerWindings:
            obj.PowerTransformer = None

