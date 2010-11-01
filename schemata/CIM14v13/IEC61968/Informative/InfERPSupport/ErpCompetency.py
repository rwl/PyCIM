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

class ErpCompetency(IdentifiedObject):
    """Information that describes aptitudes of a utility employee. Unlike Skills that an ErpPerson must be certified to perform before undertaking certain type of assignments (to be able to perfrom a Craft), ErpCompetency has more to do with typical Human Resource (HR) matters such as schooling, training, etc.
    """

    def __init__(self, ErpPersons=None, *args, **kw_args):
        """Initializes a new 'ErpCompetency' instance.

        @param ErpPersons:
        """
        self._ErpPersons = []
        self.ErpPersons = [] if ErpPersons is None else ErpPersons

        super(ErpCompetency, self).__init__(*args, **kw_args)

    def getErpPersons(self):
        
        return self._ErpPersons

    def setErpPersons(self, value):
        for x in self._ErpPersons:
            x._ErpCompetency = None
        for y in value:
            y._ErpCompetency = self
        self._ErpPersons = value

    ErpPersons = property(getErpPersons, setErpPersons)

    def addErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            obj._ErpCompetency = self
            self._ErpPersons.append(obj)

    def removeErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            obj._ErpCompetency = None
            self._ErpPersons.remove(obj)

