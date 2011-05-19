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

from CIM15.IEC61968.Assets.AssetInfo import AssetInfo

class ShuntCompensatorInfo(AssetInfo):
    """Properties of shunt capacitor, shunt reactor or switchable bank of shunt capacitor or reactor assets.Properties of shunt capacitor, shunt reactor or switchable bank of shunt capacitor or reactor assets.
    """

    def __init__(self, maxPowerLoss=0.0, ShuntImpedanceInfo=None, *args, **kw_args):
        """Initialises a new 'ShuntCompensatorInfo' instance.

        @param maxPowerLoss: Maximum allowed Apparent Power loss 
        @param ShuntImpedanceInfo:
        """
        #: Maximum allowed Apparent Power loss
        self.maxPowerLoss = maxPowerLoss

        self._ShuntImpedanceInfo = None
        self.ShuntImpedanceInfo = ShuntImpedanceInfo

        super(ShuntCompensatorInfo, self).__init__(*args, **kw_args)

    _attrs = ["maxPowerLoss"]
    _attr_types = {"maxPowerLoss": float}
    _defaults = {"maxPowerLoss": 0.0}
    _enums = {}
    _refs = ["ShuntImpedanceInfo"]
    _many_refs = []

    def getShuntImpedanceInfo(self):
        
        return self._ShuntImpedanceInfo

    def setShuntImpedanceInfo(self, value):
        if self._ShuntImpedanceInfo is not None:
            filtered = [x for x in self.ShuntImpedanceInfo.ShuntCompensatorInfos if x != self]
            self._ShuntImpedanceInfo._ShuntCompensatorInfos = filtered

        self._ShuntImpedanceInfo = value
        if self._ShuntImpedanceInfo is not None:
            if self not in self._ShuntImpedanceInfo._ShuntCompensatorInfos:
                self._ShuntImpedanceInfo._ShuntCompensatorInfos.append(self)

    ShuntImpedanceInfo = property(getShuntImpedanceInfo, setShuntImpedanceInfo)

