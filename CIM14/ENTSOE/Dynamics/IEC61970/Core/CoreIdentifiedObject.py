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

from CIM14.ENTSOE.Dynamics.Element import Element

class CoreIdentifiedObject(Element):

    def __init__(self, mRID='', description='', name='', localName='', aliasName='', pathName='', ModelingAuthoritySet=None, *args, **kw_args):
        """Initialises a new 'CoreIdentifiedObject' instance.

        @param mRID: 
        @param description:  
        @param name:  
        @param localName: 
        @param aliasName: 
        @param pathName: 
        @param ModelingAuthoritySet:
        """

        self.mRID = mRID

        #: 
        self.description = description

        #: 
        self.name = name


        self.localName = localName


        self.aliasName = aliasName


        self.pathName = pathName

        self._ModelingAuthoritySet = None
        self.ModelingAuthoritySet = ModelingAuthoritySet

        super(CoreIdentifiedObject, self).__init__(*args, **kw_args)

    _attrs = ["mRID", "description", "name", "localName", "aliasName", "pathName"]
    _attr_types = {"mRID": str, "description": str, "name": str, "localName": str, "aliasName": str, "pathName": str}
    _defaults = {"mRID": '', "description": '', "name": '', "localName": '', "aliasName": '', "pathName": ''}
    _enums = {}
    _refs = ["ModelingAuthoritySet"]
    _many_refs = []

    def getModelingAuthoritySet(self):
        
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

