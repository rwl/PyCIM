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

from CIM15.CDPSM.Connectivity.Element import Element

class NameTypeAuthority(Element):
    """Authority responsible for creation and management of names of a given type; typically an organization or an enterprise system.
    """

    def __init__(self, name='', description='', NameTypes=None, *args, **kw_args):
        """Initialises a new 'NameTypeAuthority' instance.

        @param name: Name of the name type authority. 
        @param description: Description of the name type authority. 
        @param NameTypes: All name types managed by this authority.
        """
        #: Name of the name type authority.
        self.name = name

        #: Description of the name type authority.
        self.description = description

        self._NameTypes = []
        self.NameTypes = [] if NameTypes is None else NameTypes

        super(NameTypeAuthority, self).__init__(*args, **kw_args)

    _attrs = ["name", "description"]
    _attr_types = {"name": str, "description": str}
    _defaults = {"name": '', "description": ''}
    _enums = {}
    _refs = ["NameTypes"]
    _many_refs = ["NameTypes"]

    def getNameTypes(self):
        """All name types managed by this authority.
        """
        return self._NameTypes

    def setNameTypes(self, value):
        for x in self._NameTypes:
            x.NameTypeAuthority = None
        for y in value:
            y._NameTypeAuthority = self
        self._NameTypes = value

    NameTypes = property(getNameTypes, setNameTypes)

    def addNameTypes(self, *NameTypes):
        for obj in NameTypes:
            obj.NameTypeAuthority = self

    def removeNameTypes(self, *NameTypes):
        for obj in NameTypes:
            obj.NameTypeAuthority = None

