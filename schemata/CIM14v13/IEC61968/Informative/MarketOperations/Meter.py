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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Meter(IdentifiedObject):
    """This is generic logical meter object.
    """

    def __init__(self, RegisteredResource=None, **kw_args):
        """Initializes a new 'Meter' instance.

        @param RegisteredResource:
        """
        self._RegisteredResource = None
        self.RegisteredResource = RegisteredResource

        super(Meter, self).__init__(**kw_args)

    def getRegisteredResource(self):
        
        return self._RegisteredResource

    def setRegisteredResource(self, value):
        if self._RegisteredResource is not None:
            filtered = [x for x in self.RegisteredResource.Meters if x != self]
            self._RegisteredResource._Meters = filtered

        self._RegisteredResource = value
        if self._RegisteredResource is not None:
            self._RegisteredResource._Meters.append(self)

    RegisteredResource = property(getRegisteredResource, setRegisteredResource)

