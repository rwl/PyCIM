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

from CIM15.IEC61968.Assets.Asset import Asset

class ComEquipment(Asset):
    """Communicaiton equipment assets other than media (such as gateways, routers, controllers, etc.).Communicaiton equipment assets other than media (such as gateways, routers, controllers, etc.).
    """

    def __init__(self, EndDeviceFunctions=None, *args, **kw_args):
        """Initialises a new 'ComEquipment' instance.

        @param EndDeviceFunctions: All device functions of this communication equipment.
        """
        self._EndDeviceFunctions = []
        self.EndDeviceFunctions = [] if EndDeviceFunctions is None else EndDeviceFunctions

        super(ComEquipment, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["EndDeviceFunctions"]
    _many_refs = ["EndDeviceFunctions"]

    def getEndDeviceFunctions(self):
        """All device functions of this communication equipment.
        """
        return self._EndDeviceFunctions

    def setEndDeviceFunctions(self, value):
        for x in self._EndDeviceFunctions:
            x.ComEquipment = None
        for y in value:
            y._ComEquipment = self
        self._EndDeviceFunctions = value

    EndDeviceFunctions = property(getEndDeviceFunctions, setEndDeviceFunctions)

    def addEndDeviceFunctions(self, *EndDeviceFunctions):
        for obj in EndDeviceFunctions:
            obj.ComEquipment = self

    def removeEndDeviceFunctions(self, *EndDeviceFunctions):
        for obj in EndDeviceFunctions:
            obj.ComEquipment = None

