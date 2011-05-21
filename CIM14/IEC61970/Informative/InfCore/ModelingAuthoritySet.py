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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ModelingAuthoritySet(IdentifiedObject):
    """A Modeling Authority Set is a group of objects in a network model where the data is supplied and maintained by the same Modeling Authority.
    """

    def __init__(self, ModelingAuthority=None, IdentifiedObjects=None, *args, **kw_args):
        """Initialises a new 'ModelingAuthoritySet' instance.

        @param ModelingAuthority: A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.
        @param IdentifiedObjects: An IdentifiedObject belongs to a Modeling Authority Set for purposes of defining a group of data maintained by the same Modeling Authority.
        """
        self._ModelingAuthority = None
        self.ModelingAuthority = ModelingAuthority

        self._IdentifiedObjects = []
        self.IdentifiedObjects = [] if IdentifiedObjects is None else IdentifiedObjects

        super(ModelingAuthoritySet, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ModelingAuthority", "IdentifiedObjects"]
    _many_refs = ["IdentifiedObjects"]

    def getModelingAuthority(self):
        """A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.
        """
        return self._ModelingAuthority

    def setModelingAuthority(self, value):
        if self._ModelingAuthority is not None:
            filtered = [x for x in self.ModelingAuthority.ModelingAuthoritySets if x != self]
            self._ModelingAuthority._ModelingAuthoritySets = filtered

        self._ModelingAuthority = value
        if self._ModelingAuthority is not None:
            if self not in self._ModelingAuthority._ModelingAuthoritySets:
                self._ModelingAuthority._ModelingAuthoritySets.append(self)

    ModelingAuthority = property(getModelingAuthority, setModelingAuthority)

    def getIdentifiedObjects(self):
        """An IdentifiedObject belongs to a Modeling Authority Set for purposes of defining a group of data maintained by the same Modeling Authority.
        """
        return self._IdentifiedObjects

    def setIdentifiedObjects(self, value):
        for x in self._IdentifiedObjects:
            x.ModelingAuthoritySet = None
        for y in value:
            y._ModelingAuthoritySet = self
        self._IdentifiedObjects = value

    IdentifiedObjects = property(getIdentifiedObjects, setIdentifiedObjects)

    def addIdentifiedObjects(self, *IdentifiedObjects):
        for obj in IdentifiedObjects:
            obj.ModelingAuthoritySet = self

    def removeIdentifiedObjects(self, *IdentifiedObjects):
        for obj in IdentifiedObjects:
            obj.ModelingAuthoritySet = None

