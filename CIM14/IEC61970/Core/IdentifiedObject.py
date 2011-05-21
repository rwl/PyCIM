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

from CIM14.Element import Element

class IdentifiedObject(Element):
    """This is a root class to provide common naming attributes for all classes needing naming attributes
    """

    def __init__(self, pathName='', aliasName='', mRID='', name='', description='', localName='', ModelingAuthoritySet=None, *args, **kw_args):
        """Initialises a new 'IdentifiedObject' instance.

        @param pathName: The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root. 
        @param aliasName: The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy. 
        @param mRID: A Model Authority issues mRIDs. Given that each Model Authority has a unique id and this id is part of the mRID, then the mRID is globally unique. 
        @param name: The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy. 
        @param description: The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. 
        @param localName: The localName is a human readable name of the object. It is only used with objects organized in a naming hierarchy. The simplest naming hierarchy has just one parent (the root) giving a flat naming hierarchy. However, the naming hierarchy usually has several levels, e.g. Substation, VoltageLevel, Equipment etc. Children of the same parent have names that are unique among them. If the uniqueness requirement cannot be met IdentifiedObject.localName shall not be used, use IdentifiedObject.name  instead. 
        @param ModelingAuthoritySet: An IdentifiedObject belongs to a Modeling Authority Set for purposes of defining a group of data maintained by the same Modeling Authority.
        """
        #: The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root.
        self.pathName = pathName

        #: The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.
        self.aliasName = aliasName

        #: A Model Authority issues mRIDs. Given that each Model Authority has a unique id and this id is part of the mRID, then the mRID is globally unique.
        self.mRID = mRID

        #: The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.
        self.name = name

        #: The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.
        self.description = description

        #: The localName is a human readable name of the object. It is only used with objects organized in a naming hierarchy. The simplest naming hierarchy has just one parent (the root) giving a flat naming hierarchy. However, the naming hierarchy usually has several levels, e.g. Substation, VoltageLevel, Equipment etc. Children of the same parent have names that are unique among them. If the uniqueness requirement cannot be met IdentifiedObject.localName shall not be used, use IdentifiedObject.name  instead.
        self.localName = localName

        self._ModelingAuthoritySet = None
        self.ModelingAuthoritySet = ModelingAuthoritySet

        super(IdentifiedObject, self).__init__(*args, **kw_args)

    _attrs = ["pathName", "aliasName", "mRID", "name", "description", "localName"]
    _attr_types = {"pathName": str, "aliasName": str, "mRID": str, "name": str, "description": str, "localName": str}
    _defaults = {"pathName": '', "aliasName": '', "mRID": '', "name": '', "description": '', "localName": ''}
    _enums = {}
    _refs = ["ModelingAuthoritySet"]
    _many_refs = []

    def getModelingAuthoritySet(self):
        """An IdentifiedObject belongs to a Modeling Authority Set for purposes of defining a group of data maintained by the same Modeling Authority.
        """
        return self._ModelingAuthoritySet

    def setModelingAuthoritySet(self, value):
        if self._ModelingAuthoritySet is not None:
            filtered = [x for x in self.ModelingAuthoritySet.IdentifiedObjects if x != self]
            self._ModelingAuthoritySet._IdentifiedObjects = filtered

        self._ModelingAuthoritySet = value
        if self._ModelingAuthoritySet is not None:
            if self not in self._ModelingAuthoritySet._IdentifiedObjects:
                self._ModelingAuthoritySet._IdentifiedObjects.append(self)

    ModelingAuthoritySet = property(getModelingAuthoritySet, setModelingAuthoritySet)

