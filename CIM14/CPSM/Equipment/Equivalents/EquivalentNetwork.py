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

from CIM14.CPSM.Equipment.Core.ConnectivityNodeContainer import ConnectivityNodeContainer

class EquivalentNetwork(ConnectivityNodeContainer):
    """A class that represents an external meshed network that has been reduced to an electrically equivalent model. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent.
    """

    def __init__(self, EquivalentEquipments=None, *args, **kw_args):
        """Initialises a new 'EquivalentNetwork' instance.

        @param EquivalentEquipments: The associated reduced equivalents.
        """
        self._EquivalentEquipments = []
        self.EquivalentEquipments = [] if EquivalentEquipments is None else EquivalentEquipments

        super(EquivalentNetwork, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["EquivalentEquipments"]
    _many_refs = ["EquivalentEquipments"]

    def getEquivalentEquipments(self):
        """The associated reduced equivalents.
        """
        return self._EquivalentEquipments

    def setEquivalentEquipments(self, value):
        for x in self._EquivalentEquipments:
            x.EquivalentNetwork = None
        for y in value:
            y._EquivalentNetwork = self
        self._EquivalentEquipments = value

    EquivalentEquipments = property(getEquivalentEquipments, setEquivalentEquipments)

    def addEquivalentEquipments(self, *EquivalentEquipments):
        for obj in EquivalentEquipments:
            obj.EquivalentNetwork = self

    def removeEquivalentEquipments(self, *EquivalentEquipments):
        for obj in EquivalentEquipments:
            obj.EquivalentNetwork = None

