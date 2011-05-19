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

class IdentifiedObject(Element):
    """This is a root class to provide common identification for all classes needing identification and naming attributesThis is a root class to provide common identification for all classes needing identification and naming attributes
    """

    def __init__(self, mRID='', aliasName='', name='', Names=None, DiagramObjects=None, ModelingAuthoritySet=None, *args, **kw_args):
        """Initialises a new 'IdentifiedObject' instance.

        @param mRID: A Model Authority issues mRIDs. Given that each Model Authority has a unique id and this id is part of the mRID, then the mRID is globally unique. Global uniqeness is easily achived by using a UUID for the mRID. It is strongly recommended to do this. For CIMXML data files the mRID is mapped to rdf:ID or rdf:about attributes that identifies CIM object elements. 
        @param aliasName: The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy. The attribute aliasName is put back because of backwards compatibility between CIM relases. It is however recommended to replace aliasName with the Name class as aliasName is planned for retirement at a future time. This was decided at a joint WG13/14 meeting in Minneapolis 2010-10-06. 
        @param name: The name is any free human readable and possibly non unique text naming the object. 
        @param Names: All names of this identified object.
        @param DiagramObjects: The diagram objects that are associated with the domain object
        @param ModelingAuthoritySet: An IdentifiedObject belongs to a Modeling Authority Set for purposes of defining a group of data maintained by the same Modeling Authority.
        """
        #: A Model Authority issues mRIDs. Given that each Model Authority has a unique id and this id is part of the mRID, then the mRID is globally unique. Global uniqeness is easily achived by using a UUID for the mRID. It is strongly recommended to do this. For CIMXML data files the mRID is mapped to rdf:ID or rdf:about attributes that identifies CIM object elements.
        self.mRID = mRID

        #: The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy. The attribute aliasName is put back because of backwards compatibility between CIM relases. It is however recommended to replace aliasName with the Name class as aliasName is planned for retirement at a future time. This was decided at a joint WG13/14 meeting in Minneapolis 2010-10-06.
        self.aliasName = aliasName

        #: The name is any free human readable and possibly non unique text naming the object.
        self.name = name

        self._Names = []
        self.Names = [] if Names is None else Names

        self._DiagramObjects = []
        self.DiagramObjects = [] if DiagramObjects is None else DiagramObjects

        self._ModelingAuthoritySet = None
        self.ModelingAuthoritySet = ModelingAuthoritySet

        super(IdentifiedObject, self).__init__(*args, **kw_args)

    _attrs = ["mRID", "aliasName", "name"]
    _attr_types = {"mRID": str, "aliasName": str, "name": str}
    _defaults = {"mRID": '', "aliasName": '', "name": ''}
    _enums = {}
    _refs = ["Names", "DiagramObjects", "ModelingAuthoritySet"]
    _many_refs = ["Names", "DiagramObjects"]

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

    def getDiagramObjects(self):
        """The diagram objects that are associated with the domain object
        """
        return self._DiagramObjects

    def setDiagramObjects(self, value):
        for x in self._DiagramObjects:
            x.IdentifiedObject = None
        for y in value:
            y._IdentifiedObject = self
        self._DiagramObjects = value

    DiagramObjects = property(getDiagramObjects, setDiagramObjects)

    def addDiagramObjects(self, *DiagramObjects):
        for obj in DiagramObjects:
            obj.IdentifiedObject = self

    def removeDiagramObjects(self, *DiagramObjects):
        for obj in DiagramObjects:
            obj.IdentifiedObject = None

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

