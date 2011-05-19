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

from CIM15.IEC61968.Assets.AssetContainer import AssetContainer

class Duct(AssetContainer):
    """A Duct contains underground cables and is contained within a duct bank. The xCoord and yCoord attributes define its positioning within the DuctBank.A Duct contains underground cables and is contained within a duct bank. The xCoord and yCoord attributes define its positioning within the DuctBank.
    """

    def __init__(self, xCoord=0, yCoord=0, DuctBankInfo=None, CableInfos=None, *args, **kw_args):
        """Initialises a new 'Duct' instance.

        @param xCoord: X position of the duct within the duct bank. 
        @param yCoord: Y position of the duct within the duct bank. 
        @param DuctBankInfo:
        @param CableInfos:
        """
        #: X position of the duct within the duct bank.
        self.xCoord = xCoord

        #: Y position of the duct within the duct bank.
        self.yCoord = yCoord

        self._DuctBankInfo = None
        self.DuctBankInfo = DuctBankInfo

        self._CableInfos = []
        self.CableInfos = [] if CableInfos is None else CableInfos

        super(Duct, self).__init__(*args, **kw_args)

    _attrs = ["xCoord", "yCoord"]
    _attr_types = {"xCoord": int, "yCoord": int}
    _defaults = {"xCoord": 0, "yCoord": 0}
    _enums = {}
    _refs = ["DuctBankInfo", "CableInfos"]
    _many_refs = ["CableInfos"]

    def getDuctBankInfo(self):
        
        return self._DuctBankInfo

    def setDuctBankInfo(self, value):
        if self._DuctBankInfo is not None:
            filtered = [x for x in self.DuctBankInfo.DuctInfos if x != self]
            self._DuctBankInfo._DuctInfos = filtered

        self._DuctBankInfo = value
        if self._DuctBankInfo is not None:
            if self not in self._DuctBankInfo._DuctInfos:
                self._DuctBankInfo._DuctInfos.append(self)

    DuctBankInfo = property(getDuctBankInfo, setDuctBankInfo)

    def getCableInfos(self):
        
        return self._CableInfos

    def setCableInfos(self, value):
        for x in self._CableInfos:
            x.DuctBankInfo = None
        for y in value:
            y._DuctBankInfo = self
        self._CableInfos = value

    CableInfos = property(getCableInfos, setCableInfos)

    def addCableInfos(self, *CableInfos):
        for obj in CableInfos:
            obj.DuctBankInfo = self

    def removeCableInfos(self, *CableInfos):
        for obj in CableInfos:
            obj.DuctBankInfo = None

