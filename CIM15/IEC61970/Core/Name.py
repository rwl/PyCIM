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

from CIM15.Element import Element

class Name(Element):
    """The Name class provides the means to define any number of human readable  names for an object. A name is <b>not</b> to be used for defining inter-object relationships. For inter-object relationships instead use the object identification 'mRID'.The Name class provides the means to define any number of human readable  names for an object. A name is <b>not</b> to be used for defining inter-object relationships. For inter-object relationships instead use the object identification 'mRID'.
    """

    def __init__(self, name='', NameType=None, IdentifiedObject=None, *args, **kw_args):
        """Initialises a new 'Name' instance.

        @param name: Any free text that name the object. 
        @param NameType: Type of this name.
        @param IdentifiedObject: Identified object that this name designates.
        """
        #: Any free text that name the object.
        self.name = name

        self._NameType = None
        self.NameType = NameType

        self._IdentifiedObject = None
        self.IdentifiedObject = IdentifiedObject

        super(Name, self).__init__(*args, **kw_args)

    _attrs = ["name"]
    _attr_types = {"name": str}
    _defaults = {"name": ''}
    _enums = {}
    _refs = ["NameType", "IdentifiedObject"]
    _many_refs = []

    def getNameType(self):
        """Type of this name.
        """
        return self._NameType

    def setNameType(self, value):
        if self._NameType is not None:
            filtered = [x for x in self.NameType.Names if x != self]
            self._NameType._Names = filtered

        self._NameType = value
        if self._NameType is not None:
            if self not in self._NameType._Names:
                self._NameType._Names.append(self)

    NameType = property(getNameType, setNameType)

    def getIdentifiedObject(self):
        """Identified object that this name designates.
        """
        return self._IdentifiedObject

    def setIdentifiedObject(self, value):
        if self._IdentifiedObject is not None:
            filtered = [x for x in self.IdentifiedObject.Names if x != self]
            self._IdentifiedObject._Names = filtered

        self._IdentifiedObject = value
        if self._IdentifiedObject is not None:
            if self not in self._IdentifiedObject._Names:
                self._IdentifiedObject._Names.append(self)

    IdentifiedObject = property(getIdentifiedObject, setIdentifiedObject)

