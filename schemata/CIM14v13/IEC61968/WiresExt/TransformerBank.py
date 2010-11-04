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

from CIM14v13.IEC61970.Core.Equipment import Equipment

class TransformerBank(Equipment):
    """An assembly of transformers that are connected together. For three-phase transformers, there would be one transformer per bank. For banks of single-phase transformers, there will be more than one transformer per bank, and they need not be identical.
    """

    def __init__(self, vectorGroup='', Transformers=None, *args, **kw_args):
        """Initializes a new 'TransformerBank' instance.

        @param vectorGroup: Vector group of the bank for protective relaying, e.g., Dyn1. For unbalanced transformers, this may not be simply determined from the constituent winding connections. 
        @param Transformers: All transformers that belong to this bank.
        """
        #: Vector group of the bank for protective relaying, e.g., Dyn1. For unbalanced transformers, this may not be simply determined from the constituent winding connections.
        self.vectorGroup = vectorGroup

        self._Transformers = []
        self.Transformers = [] if Transformers is None else Transformers

        super(TransformerBank, self).__init__(*args, **kw_args)

    def getTransformers(self):
        """All transformers that belong to this bank.
        """
        return self._Transformers

    def setTransformers(self, value):
        for x in self._Transformers:
            x._TransformerBank = None
        for y in value:
            y._TransformerBank = self
        self._Transformers = value

    Transformers = property(getTransformers, setTransformers)

    def addTransformers(self, *Transformers):
        for obj in Transformers:
            obj._TransformerBank = self
            self._Transformers.append(obj)

    def removeTransformers(self, *Transformers):
        for obj in Transformers:
            obj._TransformerBank = None
            self._Transformers.remove(obj)

