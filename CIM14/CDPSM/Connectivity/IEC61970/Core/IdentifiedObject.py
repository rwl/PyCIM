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

class IdentifiedObject(Element):
    """This is a root class to provide common identification for all classes needing identification and naming attributes
    """

    def __init__(self, name='', aliasName='', Names=None, *args, **kw_args):
        """Initialises a new 'IdentifiedObject' instance.

        @param name: The name is any free human readable and possibly non unique text naming the object. 
        @param aliasName: The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy. The attribute aliasName is put back because of backwards compatibility between CIM relases. It is however recommended to replace aliasName with the Name class as aliasName is planned for retirement at a future time. This was decided at a joint WG13/14 meeting in Minneapolis 2010-10-06. 
        @param Names: All names of this identified object.
        """
        #: The name is any free human readable and possibly non unique text naming the object.
        self.name = name

        #: The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy. The attribute aliasName is put back because of backwards compatibility between CIM relases. It is however recommended to replace aliasName with the Name class as aliasName is planned for retirement at a future time. This was decided at a joint WG13/14 meeting in Minneapolis 2010-10-06.
        self.aliasName = aliasName

        self._Names = []
        self.Names = [] if Names is None else Names

        super(IdentifiedObject, self).__init__(*args, **kw_args)

    _attrs = ["name", "aliasName"]
    _attr_types = {"name": str, "aliasName": str}
    _defaults = {"name": '', "aliasName": ''}
    _enums = {}
    _refs = ["Names"]
    _many_refs = ["Names"]

    def getNames(self):
        """All names of this identified object.
        """
        return self._Names

    def setNames(self, value):
        for x in self._Names:
            x.IdentifiedObject = None
        for y in value:
            y._IdentifiedObject = self
        self._Names = value

    Names = property(getNames, setNames)

    def addNames(self, *Names):
        for obj in Names:
            obj.IdentifiedObject = self

    def removeNames(self, *Names):
        for obj in Names:
            obj.IdentifiedObject = None

