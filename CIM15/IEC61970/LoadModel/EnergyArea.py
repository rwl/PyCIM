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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class EnergyArea(IdentifiedObject):
    """The class describes an area having energy production or consumption. The class is the basis for further specialization.The class describes an area having energy production or consumption. The class is the basis for further specialization.
    """

    def __init__(self, ControlArea=None, *args, **kw_args):
        """Initialises a new 'EnergyArea' instance.

        @param ControlArea: The control area specification that is used for the load forecast.
        """
        self._ControlArea = None
        self.ControlArea = ControlArea

        super(EnergyArea, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ControlArea"]
    _many_refs = []

    def getControlArea(self):
        """The control area specification that is used for the load forecast.
        """
        return self._ControlArea

    def setControlArea(self, value):
        if self._ControlArea is not None:
            self._ControlArea._EnergyArea = None

        self._ControlArea = value
        if self._ControlArea is not None:
            self._ControlArea.EnergyArea = None
            self._ControlArea._EnergyArea = self

    ControlArea = property(getControlArea, setControlArea)

