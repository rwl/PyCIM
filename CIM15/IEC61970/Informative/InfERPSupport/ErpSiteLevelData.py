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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ErpSiteLevelData(IdentifiedObject):
    """For a utility, general information that describes physical locations of organizations or the location codes and their meanings. This enables ERP applications to ensure that the physical location identifiers are synchronized between the business applications.For a utility, general information that describes physical locations of organizations or the location codes and their meanings. This enables ERP applications to ensure that the physical location identifiers are synchronized between the business applications.
    """

    def __init__(self, status=None, LandProperty=None, *args, **kw_args):
        """Initialises a new 'ErpSiteLevelData' instance.

        @param status:
        @param LandProperty:
        """
        self.status = status

        self._LandProperty = None
        self.LandProperty = LandProperty

        super(ErpSiteLevelData, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["status", "LandProperty"]
    _many_refs = []

    status = None

    def getLandProperty(self):
        
        return self._LandProperty

    def setLandProperty(self, value):
        if self._LandProperty is not None:
            filtered = [x for x in self.LandProperty.ErpSiteLevelDatas if x != self]
            self._LandProperty._ErpSiteLevelDatas = filtered

        self._LandProperty = value
        if self._LandProperty is not None:
            if self not in self._LandProperty._ErpSiteLevelDatas:
                self._LandProperty._ErpSiteLevelDatas.append(self)

    LandProperty = property(getLandProperty, setLandProperty)

