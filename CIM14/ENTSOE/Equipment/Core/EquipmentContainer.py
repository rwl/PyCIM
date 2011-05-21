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

from CIM14.ENTSOE.Equipment.Core.ConnectivityNodeContainer import ConnectivityNodeContainer

class EquipmentContainer(ConnectivityNodeContainer):
    """A modeling construct to provide a root class for containing equipment.
    """

    def __init__(self, Equipments=None, *args, **kw_args):
        """Initialises a new 'EquipmentContainer' instance.

        @param Equipments: The association is used in the naming hierarchy.
        """
        self._Equipments = []
        self.Equipments = [] if Equipments is None else Equipments

        super(EquipmentContainer, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Equipments"]
    _many_refs = ["Equipments"]

    def getEquipments(self):
        """The association is used in the naming hierarchy.
        """
        return self._Equipments

    def setEquipments(self, value):
        for x in self._Equipments:
            x.EquipmentContainer = None
        for y in value:
            y._EquipmentContainer = self
        self._Equipments = value

    Equipments = property(getEquipments, setEquipments)

    def addEquipments(self, *Equipments):
        for obj in Equipments:
            obj.EquipmentContainer = self

    def removeEquipments(self, *Equipments):
        for obj in Equipments:
            obj.EquipmentContainer = None

