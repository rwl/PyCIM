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

from CIM15.IEC61970.StateVariables.StateVariable import StateVariable

class SvStatus(StateVariable):
    """State variable for status.State variable for status.
    """

    def __init__(self, inService=False, ConductingEquipment=None, *args, **kw_args):
        """Initialises a new 'SvStatus' instance.

        @param inService: The in service status as a result of topology processing. 
        @param ConductingEquipment: The conducting equipment associated with the status state.
        """
        #: The in service status as a result of topology processing.
        self.inService = inService

        self._ConductingEquipment = None
        self.ConductingEquipment = ConductingEquipment

        super(SvStatus, self).__init__(*args, **kw_args)

    _attrs = ["inService"]
    _attr_types = {"inService": bool}
    _defaults = {"inService": False}
    _enums = {}
    _refs = ["ConductingEquipment"]
    _many_refs = []

    def getConductingEquipment(self):
        """The conducting equipment associated with the status state.
        """
        return self._ConductingEquipment

    def setConductingEquipment(self, value):
        if self._ConductingEquipment is not None:
            self._ConductingEquipment._SvStatus = None

        self._ConductingEquipment = value
        if self._ConductingEquipment is not None:
            self._ConductingEquipment.SvStatus = None
            self._ConductingEquipment._SvStatus = self

    ConductingEquipment = property(getConductingEquipment, setConductingEquipment)

