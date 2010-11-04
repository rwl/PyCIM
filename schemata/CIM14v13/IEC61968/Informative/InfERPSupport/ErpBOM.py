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

from CIM14v13.IEC61968.Common.Document import Document

class ErpBOM(Document):
    """Information that generally describes the Bill of Material Structure and its contents for a utility.  This is used by ERP systems to transfer Bill of Material information between two business applications.
    """

    def __init__(self, Design=None, ErpBomItemDatas=None, **kw_args):
        """Initializes a new 'ErpBOM' instance.

        @param Design:
        @param ErpBomItemDatas:
        """
        self._Design = None
        self.Design = Design

        self._ErpBomItemDatas = []
        self.ErpBomItemDatas = [] if ErpBomItemDatas is None else ErpBomItemDatas

        super(ErpBOM, self).__init__(**kw_args)

    def getDesign(self):
        
        return self._Design

    def setDesign(self, value):
        if self._Design is not None:
            filtered = [x for x in self.Design.ErpBOMs if x != self]
            self._Design._ErpBOMs = filtered

        self._Design = value
        if self._Design is not None:
            self._Design._ErpBOMs.append(self)

    Design = property(getDesign, setDesign)

    def getErpBomItemDatas(self):
        
        return self._ErpBomItemDatas

    def setErpBomItemDatas(self, value):
        for x in self._ErpBomItemDatas:
            x._ErpBOM = None
        for y in value:
            y._ErpBOM = self
        self._ErpBomItemDatas = value

    ErpBomItemDatas = property(getErpBomItemDatas, setErpBomItemDatas)

    def addErpBomItemDatas(self, *ErpBomItemDatas):
        for obj in ErpBomItemDatas:
            obj._ErpBOM = self
            self._ErpBomItemDatas.append(obj)

    def removeErpBomItemDatas(self, *ErpBomItemDatas):
        for obj in ErpBomItemDatas:
            obj._ErpBOM = None
            self._ErpBomItemDatas.remove(obj)

