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

class Craft(IdentifiedObject):
    """Craft of a person or a crew. Examples include overhead electric, underground electric, high pressure gas, etc. This ensures necessary knowledge and skills before being allowed to perform certain types of work.Craft of a person or a crew. Examples include overhead electric, underground electric, high pressure gas, etc. This ensures necessary knowledge and skills before being allowed to perform certain types of work.
    """

    def __init__(self, category='', Skills=None, ErpPersons=None, status=None, Capabilities=None, *args, **kw_args):
        """Initialises a new 'Craft' instance.

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

    _attrs = ["category"]
    _attr_types = {"category": str}
    _defaults = {"category": ''}
    _enums = {}
    _refs = ["Skills", "ErpPersons", "status", "Capabilities"]
    _many_refs = ["Skills", "ErpPersons", "Capabilities"]

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

