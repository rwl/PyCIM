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

class Craft(IdentifiedObject):
    """Craft of a person or a crew. Examples include overhead electric, underground electric, high pressure gas, etc. This ensures necessary knowledge and skills before being allowed to perform certain types of work.
    """

    def __init__(self, category='', Skills=None, ErpPersons=None, status=None, Capabilities=None, *args, **kw_args):
        """Initializes a new 'Craft' instance.

        @param category: Category by utility's work mangement standards and practices. 
        @param Skills:
        @param ErpPersons:
        @param status:
        @param Capabilities:
        """
        #: Category by utility's work mangement standards and practices. 
        self.category = category

        self._Skills = []
        self.Skills = [] if Skills is None else Skills

        self._ErpPersons = []
        self.ErpPersons = [] if ErpPersons is None else ErpPersons

        self.status = status

        self._Capabilities = []
        self.Capabilities = [] if Capabilities is None else Capabilities

        super(Craft, self).__init__(*args, **kw_args)

    def getSkills(self):
        
        return self._Skills

    def setSkills(self, value):
        for p in self._Skills:
            filtered = [q for q in p.Crafts if q != self]
            self._Skills._Crafts = filtered
        for r in value:
            if self not in r._Crafts:
                r._Crafts.append(self)
        self._Skills = value

    Skills = property(getSkills, setSkills)

    def addSkills(self, *Skills):
        for obj in Skills:
            if self not in obj._Crafts:
                obj._Crafts.append(self)
            self._Skills.append(obj)

    def removeSkills(self, *Skills):
        for obj in Skills:
            if self in obj._Crafts:
                obj._Crafts.remove(self)
            self._Skills.remove(obj)

    def getErpPersons(self):
        
        return self._ErpPersons

    def setErpPersons(self, value):
        for p in self._ErpPersons:
            filtered = [q for q in p.Crafts if q != self]
            self._ErpPersons._Crafts = filtered
        for r in value:
            if self not in r._Crafts:
                r._Crafts.append(self)
        self._ErpPersons = value

    ErpPersons = property(getErpPersons, setErpPersons)

    def addErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            if self not in obj._Crafts:
                obj._Crafts.append(self)
            self._ErpPersons.append(obj)

    def removeErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            if self in obj._Crafts:
                obj._Crafts.remove(self)
            self._ErpPersons.remove(obj)

    status = None

    def getCapabilities(self):
        
        return self._Capabilities

    def setCapabilities(self, value):
        for p in self._Capabilities:
            filtered = [q for q in p.Crafts if q != self]
            self._Capabilities._Crafts = filtered
        for r in value:
            if self not in r._Crafts:
                r._Crafts.append(self)
        self._Capabilities = value

    Capabilities = property(getCapabilities, setCapabilities)

    def addCapabilities(self, *Capabilities):
        for obj in Capabilities:
            if self not in obj._Crafts:
                obj._Crafts.append(self)
            self._Capabilities.append(obj)

    def removeCapabilities(self, *Capabilities):
        for obj in Capabilities:
            if self in obj._Crafts:
                obj._Crafts.remove(self)
            self._Capabilities.remove(obj)

