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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class GmlTopologyStyle(IdentifiedObject):
    """The style for one topology property. Similarly to the Geometry style, a feature can have multiple topology properties, thus multiple topology style descriptors can be specified within one feature style.
    """

    def __init__(self, GmlLableStyle=None, GmlFeatureStyle=None, **kw_args):
        """Initializes a new 'GmlTopologyStyle' instance.

        @param GmlLableStyle:
        @param GmlFeatureStyle:
        """
        self._GmlLableStyle = None
        self.GmlLableStyle = GmlLableStyle

        self._GmlFeatureStyle = None
        self.GmlFeatureStyle = GmlFeatureStyle

        super(GmlTopologyStyle, self).__init__(**kw_args)

    def getGmlLableStyle(self):
        
        return self._GmlLableStyle

    def setGmlLableStyle(self, value):
        if self._GmlLableStyle is not None:
            filtered = [x for x in self.GmlLableStyle.GmlTopologyStyles if x != self]
            self._GmlLableStyle._GmlTopologyStyles = filtered

        self._GmlLableStyle = value
        if self._GmlLableStyle is not None:
            self._GmlLableStyle._GmlTopologyStyles.append(self)

    GmlLableStyle = property(getGmlLableStyle, setGmlLableStyle)

    def getGmlFeatureStyle(self):
        
        return self._GmlFeatureStyle

    def setGmlFeatureStyle(self, value):
        if self._GmlFeatureStyle is not None:
            filtered = [x for x in self.GmlFeatureStyle.GmlTobologyStyles if x != self]
            self._GmlFeatureStyle._GmlTobologyStyles = filtered

        self._GmlFeatureStyle = value
        if self._GmlFeatureStyle is not None:
            self._GmlFeatureStyle._GmlTobologyStyles.append(self)

    GmlFeatureStyle = property(getGmlFeatureStyle, setGmlFeatureStyle)

