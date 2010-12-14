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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ControlType(IdentifiedObject):
    """Specifies the type of Control, e.g. BreakerOn/Off, GeneratorVoltageSetPoint, TieLineFlow etc. The ControlType.name shall be unique among all specified types and describe the type. The ControlType.aliasName is meant to be used for localization.
    """

    def __init__(self, Controls=None, *args, **kw_args):
        """Initialises a new 'ControlType' instance.

        @param Controls: The Controls having the ControlType
        """
        self._Controls = []
        self.Controls = [] if Controls is None else Controls

        super(ControlType, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Controls"]
    _many_refs = ["Controls"]

    def getControls(self):
        """The Controls having the ControlType
        """
        return self._Controls

    def setControls(self, value):
        for x in self._Controls:
            x.ControlType = None
        for y in value:
            y._ControlType = self
        self._Controls = value

    Controls = property(getControls, setControls)

    def addControls(self, *Controls):
        for obj in Controls:
            obj.ControlType = self

    def removeControls(self, *Controls):
        for obj in Controls:
            obj.ControlType = None

