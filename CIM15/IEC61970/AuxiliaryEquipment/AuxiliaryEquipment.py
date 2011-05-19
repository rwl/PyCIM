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

from CIM15.IEC61970.Core.Equipment import Equipment

class AuxiliaryEquipment(Equipment):
    """AuxiliaryEquipment describe equipment that is not performing any primary functions but support for the equipment performing the primary function. AuxiliaryEquipment is attached to primary eqipment via an association with Terminal.AuxiliaryEquipment describe equipment that is not performing any primary functions but support for the equipment performing the primary function. AuxiliaryEquipment is attached to primary eqipment via an association with Terminal.
    """

    def __init__(self, Terminal=None, *args, **kw_args):
        """Initialises a new 'AuxiliaryEquipment' instance.

        @param Terminal: The Terminal at the equipment where the AuxiliaryEquipment is attached.
        """
        self._Terminal = None
        self.Terminal = Terminal

        super(AuxiliaryEquipment, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Terminal"]
    _many_refs = []

    def getTerminal(self):
        """The Terminal at the equipment where the AuxiliaryEquipment is attached.
        """
        return self._Terminal

    def setTerminal(self, value):
        if self._Terminal is not None:
            filtered = [x for x in self.Terminal.AuxiliaryEquipment if x != self]
            self._Terminal._AuxiliaryEquipment = filtered

        self._Terminal = value
        if self._Terminal is not None:
            if self not in self._Terminal._AuxiliaryEquipment:
                self._Terminal._AuxiliaryEquipment.append(self)

    Terminal = property(getTerminal, setTerminal)

