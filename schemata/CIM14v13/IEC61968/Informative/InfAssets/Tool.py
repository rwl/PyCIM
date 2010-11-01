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

class Tool(Asset):
    """Utility asset typically used by utility resources like crews and persons. As is the case for other assets, tools must be maintained.
    """

    def __init__(self, lastCalibrationDate='', ToolAssetModel=None, Crew=None, *args, **kw_args):
        """Initializes a new 'Tool' instance.

        @param lastCalibrationDate: Date the tool was last caibrated, if applicable. 
        @param ToolAssetModel:
        @param Crew:
        """
        #: Date the tool was last caibrated, if applicable. 
        self.lastCalibrationDate = lastCalibrationDate

        self._ToolAssetModel = None
        self.ToolAssetModel = ToolAssetModel

        self._Crew = None
        self.Crew = Crew

        super(Tool, self).__init__(*args, **kw_args)

    def getToolAssetModel(self):
        
        return self._ToolAssetModel

    def setToolAssetModel(self, value):
        if self._ToolAssetModel is not None:
            filtered = [x for x in self.ToolAssetModel.Tools if x != self]
            self._ToolAssetModel._Tools = filtered

        self._ToolAssetModel = value
        if self._ToolAssetModel is not None:
            self._ToolAssetModel._Tools.append(self)

    ToolAssetModel = property(getToolAssetModel, setToolAssetModel)

    def getCrew(self):
        
        return self._Crew

    def setCrew(self, value):
        if self._Crew is not None:
            filtered = [x for x in self.Crew.Tools if x != self]
            self._Crew._Tools = filtered

        self._Crew = value
        if self._Crew is not None:
            self._Crew._Tools.append(self)

    Crew = property(getCrew, setCrew)

