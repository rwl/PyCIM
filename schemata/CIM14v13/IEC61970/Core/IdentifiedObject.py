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

from CIM14v13.Element import Element

class IdentifiedObject(Element):
    """This is a root class to provide common naming attributes for all classes needing naming attributes
    """

    def __init__(self, description='', mRID='', name='', pathName='', localName='', aliasName='', ModelingAuthoritySet=None, *args, **kw_args):
        """Initializes a new 'IdentifiedObject' instance.

        @param description: The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. 
        @param mRID: A Model Authority issues mRIDs. Given that each Model Authority has a unique id and this id is part of the mRID, then the mRID is globally unique. 
        @param name: The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy. 
        @param pathName: The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root. 
        @param localName: The localName is a human readable name of the object. It is only used with objects organized in a naming hierarchy. The simplest naming hierarchy has just one parent (the root) giving a flat naming hierarchy. However, the naming hierarchy usually has several levels, e.g. Substation, VoltageLevel, Equipment etc. Children of the same parent have names that are unique among them. If the uniqueness requirement cannot be met IdentifiedObject.localName shall not be used, use IdentifiedObject.name  instead. 
        @param aliasName: The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy. 
        @param ModelingAuthoritySet: An IdentifiedObject belongs to a Modeling Authority Set for purposes of defining a group of data maintained by the same Modeling Authority.
        """
        #: The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. 
        self.description = description

        #: A Model Authority issues mRIDs. Given that each Model Authority has a unique id and this id is part of the mRID, then the mRID is globally unique. 
        self.mRID = mRID

        #: The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy. 
        self.name = name

        #: The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root. 
        self.pathName = pathName

        #: The localName is a human readable name of the object. It is only used with objects organized in a naming hierarchy. The simplest naming hierarchy has just one parent (the root) giving a flat naming hierarchy. However, the naming hierarchy usually has several levels, e.g. Substation, VoltageLevel, Equipment etc. Children of the same parent have names that are unique among them. If the uniqueness requirement cannot be met IdentifiedObject.localName shall not be used, use IdentifiedObject.name  instead. 
        self.localName = localName

        #: The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy. 
        self.aliasName = aliasName

        self._ModelingAuthoritySet = None
        self.ModelingAuthoritySet = ModelingAuthoritySet

        super(IdentifiedObject, self).__init__(*args, **kw_args)

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
            self._ModelingAuthoritySet._IdentifiedObjects.append(self)

    ModelingAuthoritySet = property(getModelingAuthoritySet, setModelingAuthoritySet)

