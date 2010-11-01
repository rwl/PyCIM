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

class GmlFeatureType(IdentifiedObject):
    """Type classification of feature.
    """

    def __init__(self, GmlFeatureStyles=None, *args, **kw_args):
        """Initializes a new 'GmlFeatureType' instance.

        @param GmlFeatureStyles:
        """
        self._GmlFeatureStyles = []
        self.GmlFeatureStyles = [] if GmlFeatureStyles is None else GmlFeatureStyles

        super(GmlFeatureType, self).__init__(*args, **kw_args)

    def getGmlFeatureStyles(self):
        
        return self._GmlFeatureStyles

    def setGmlFeatureStyles(self, value):
        for p in self._GmlFeatureStyles:
            filtered = [q for q in p.GmlFeatureTypes if q != self]
            self._GmlFeatureStyles._GmlFeatureTypes = filtered
        for r in value:
            if self not in r._GmlFeatureTypes:
                r._GmlFeatureTypes.append(self)
        self._GmlFeatureStyles = value

    GmlFeatureStyles = property(getGmlFeatureStyles, setGmlFeatureStyles)

    def addGmlFeatureStyles(self, *GmlFeatureStyles):
        for obj in GmlFeatureStyles:
            if self not in obj._GmlFeatureTypes:
                obj._GmlFeatureTypes.append(self)
            self._GmlFeatureStyles.append(obj)

    def removeGmlFeatureStyles(self, *GmlFeatureStyles):
        for obj in GmlFeatureStyles:
            if self in obj._GmlFeatureTypes:
                obj._GmlFeatureTypes.remove(self)
            self._GmlFeatureStyles.remove(obj)

