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

from CIM15.IEC61970.Core.ConductingEquipment import ConductingEquipment

class EquivalentEquipment(ConductingEquipment):
    """The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of different types.The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of different types.
    """

    def __init__(self, EquivalentNetwork=None, *args, **kw_args):
        """Initialises a new 'EquivalentEquipment' instance.

        @param EquivalentNetwork: The equivalent where the reduced model belongs.
        """
        self._EquivalentNetwork = None
        self.EquivalentNetwork = EquivalentNetwork

        super(EquivalentEquipment, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["EquivalentNetwork"]
    _many_refs = []

    def getEquivalentNetwork(self):
        """The equivalent where the reduced model belongs.
        """
        return self._EquivalentNetwork

    def setEquivalentNetwork(self, value):
        if self._EquivalentNetwork is not None:
            filtered = [x for x in self.EquivalentNetwork.EquivalentEquipments if x != self]
            self._EquivalentNetwork._EquivalentEquipments = filtered

        self._EquivalentNetwork = value
        if self._EquivalentNetwork is not None:
            if self not in self._EquivalentNetwork._EquivalentEquipments:
                self._EquivalentNetwork._EquivalentEquipments.append(self)

    EquivalentNetwork = property(getEquivalentNetwork, setEquivalentNetwork)

