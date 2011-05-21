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

class Contingency(IdentifiedObject):
    """An event threatening system reliability, consisting of one or more contingency elements.
    """

    def __init__(self, mustStudy=False, ContingencyElement=None, *args, **kw_args):
        """Initialises a new 'Contingency' instance.

        @param mustStudy: Set true if must study this contingency. 
        @param ContingencyElement: A contingency can have any number of contingency elements.
        """
        #: Set true if must study this contingency.
        self.mustStudy = mustStudy

        self._ContingencyElement = []
        self.ContingencyElement = [] if ContingencyElement is None else ContingencyElement

        super(Contingency, self).__init__(*args, **kw_args)

    _attrs = ["mustStudy"]
    _attr_types = {"mustStudy": bool}
    _defaults = {"mustStudy": False}
    _enums = {}
    _refs = ["ContingencyElement"]
    _many_refs = ["ContingencyElement"]

    def getContingencyElement(self):
        """A contingency can have any number of contingency elements.
        """
        return self._ContingencyElement

    def setContingencyElement(self, value):
        for x in self._ContingencyElement:
            x.Contingency = None
        for y in value:
            y._Contingency = self
        self._ContingencyElement = value

    ContingencyElement = property(getContingencyElement, setContingencyElement)

    def addContingencyElement(self, *ContingencyElement):
        for obj in ContingencyElement:
            obj.Contingency = self

    def removeContingencyElement(self, *ContingencyElement):
        for obj in ContingencyElement:
            obj.Contingency = None

