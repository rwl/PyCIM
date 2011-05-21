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

class ModelingAuthority(IdentifiedObject):
    """A Modeling Authority is an entity responsible for supplying and maintaining the data defining a specific set of objects in a network model.
    """

    def __init__(self, ModelingAuthoritySets=None, *args, **kw_args):
        """Initialises a new 'ModelingAuthority' instance.

        @param ModelingAuthoritySets: A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.
        """
        self._ModelingAuthoritySets = []
        self.ModelingAuthoritySets = [] if ModelingAuthoritySets is None else ModelingAuthoritySets

        super(ModelingAuthority, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ModelingAuthoritySets"]
    _many_refs = ["ModelingAuthoritySets"]

    def getModelingAuthoritySets(self):
        """A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.
        """
        return self._ModelingAuthoritySets

    def setModelingAuthoritySets(self, value):
        for x in self._ModelingAuthoritySets:
            x.ModelingAuthority = None
        for y in value:
            y._ModelingAuthority = self
        self._ModelingAuthoritySets = value

    ModelingAuthoritySets = property(getModelingAuthoritySets, setModelingAuthoritySets)

    def addModelingAuthoritySets(self, *ModelingAuthoritySets):
        for obj in ModelingAuthoritySets:
            obj.ModelingAuthority = self

    def removeModelingAuthoritySets(self, *ModelingAuthoritySets):
        for obj in ModelingAuthoritySets:
            obj.ModelingAuthority = None

