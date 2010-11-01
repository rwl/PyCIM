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

from CIM14v13.IEC61968.Assets.Asset import Asset

class TapChangerAsset(Asset):
    """Physical asset performing TapChanger function.
    """

    def __init__(self, TapChangerAssetModel=None, *args, **kw_args):
        """Initializes a new 'TapChangerAsset' instance.

        @param TapChangerAssetModel:
        """
        self._TapChangerAssetModel = None
        self.TapChangerAssetModel = TapChangerAssetModel

        super(TapChangerAsset, self).__init__(*args, **kw_args)

    def getTapChangerAssetModel(self):
        
        return self._TapChangerAssetModel

    def setTapChangerAssetModel(self, value):
        if self._TapChangerAssetModel is not None:
            filtered = [x for x in self.TapChangerAssetModel.TapChangerAssets if x != self]
            self._TapChangerAssetModel._TapChangerAssets = filtered

        self._TapChangerAssetModel = value
        if self._TapChangerAssetModel is not None:
            self._TapChangerAssetModel._TapChangerAssets.append(self)

    TapChangerAssetModel = property(getTapChangerAssetModel, setTapChangerAssetModel)

