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

from CIM14.CDPSM.Unbalanced.IEC61970.Core.Equipment import Equipment

class TransformerBank(Equipment):
    """An assembly of transformers that are connected together. For three-phase transformers, there would be one transformer per bank. For banks of single-phase transformers, there will be more than one transformer per bank, and they need not be identical.
    """

    def __init__(self, vectorGroup='', Transformers=None, *args, **kw_args):
        """Initialises a new 'TransformerBank' instance.

        @param vectorGroup: Vector group of the bank for protective relaying, e.g., Dyn1. For unbalanced transformers, this may not be simply determined from the constituent winding connections. 
        @param Transformers: All transformers that belong to this bank.
        """
        #: Vector group of the bank for protective relaying, e.g., Dyn1. For unbalanced transformers, this may not be simply determined from the constituent winding connections.
        self.vectorGroup = vectorGroup

        self._Transformers = []
        self.Transformers = [] if Transformers is None else Transformers

        super(TransformerBank, self).__init__(*args, **kw_args)

    _attrs = ["vectorGroup"]
    _attr_types = {"vectorGroup": str}
    _defaults = {"vectorGroup": ''}
    _enums = {}
    _refs = ["Transformers"]
    _many_refs = ["Transformers"]

    def getTransformers(self):
        """All transformers that belong to this bank.
        """
        return self._Transformers

    def setTransformers(self, value):
        for x in self._Transformers:
            x.TransformerBank = None
        for y in value:
            y._TransformerBank = self
        self._Transformers = value

    Transformers = property(getTransformers, setTransformers)

    def addTransformers(self, *Transformers):
        for obj in Transformers:
            obj.TransformerBank = self

    def removeTransformers(self, *Transformers):
        for obj in Transformers:
            obj.TransformerBank = None

