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

from CIM15.IEC61968.Common.Document import Document

class ErpBOM(Document):
    """Information that generally describes the Bill of Material Structure and its contents for a utility.  This is used by ERP systems to transfer Bill of Material information between two business applications.Information that generally describes the Bill of Material Structure and its contents for a utility.  This is used by ERP systems to transfer Bill of Material information between two business applications.
    """

    def __init__(self, Design=None, ErpBomItemDatas=None, *args, **kw_args):
        """Initialises a new 'ErpBOM' instance.

        @param Design:
        @param ErpBomItemDatas:
        """
        self._Design = None
        self.Design = Design

        self._ErpBomItemDatas = []
        self.ErpBomItemDatas = [] if ErpBomItemDatas is None else ErpBomItemDatas

        super(ErpBOM, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Design", "ErpBomItemDatas"]
    _many_refs = ["ErpBomItemDatas"]

    def getDesign(self):
        
        return self._Design

    def setDesign(self, value):
        if self._Design is not None:
            filtered = [x for x in self.Design.ErpBOMs if x != self]
            self._Design._ErpBOMs = filtered

        self._Design = value
        if self._Design is not None:
            if self not in self._Design._ErpBOMs:
                self._Design._ErpBOMs.append(self)

    Design = property(getDesign, setDesign)

    def getErpBomItemDatas(self):
        
        return self._ErpBomItemDatas

    def setErpBomItemDatas(self, value):
        for x in self._ErpBomItemDatas:
            x.ErpBOM = None
        for y in value:
            y._ErpBOM = self
        self._ErpBomItemDatas = value

    ErpBomItemDatas = property(getErpBomItemDatas, setErpBomItemDatas)

    def addErpBomItemDatas(self, *ErpBomItemDatas):
        for obj in ErpBomItemDatas:
            obj.ErpBOM = self

    def removeErpBomItemDatas(self, *ErpBomItemDatas):
        for obj in ErpBomItemDatas:
            obj.ErpBOM = None

