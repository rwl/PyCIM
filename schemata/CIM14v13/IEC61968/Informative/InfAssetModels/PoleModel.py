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

from CIM14v13.IEC61968.AssetModels.AssetModel import AssetModel

class PoleModel(AssetModel):
    """A type of pole supplied by a given manufacturer.
    """

    def __init__(self, speciesType='', classification='', PoleTypeAsset=None, Poles=None, *args, **kw_args):
        """Initializes a new 'PoleModel' instance.

        @param speciesType: Pole species. Aluminum, Aluminum Davit, Concrete, Fiberglass, Galvanized Davit, Galvanized, Steel Davit Primed, Steel Davit, Steel Standard Primed, Steel, Truncated, Wood-Treated, Wood-Hard, Wood-Salt Treated, Wood-Soft, Wood, Other, Unknown. 
        @param classification: Pole class: 1, 2, 3, 4, 5, 6, 7, H1, H2, Other, Unknown. 
        @param PoleTypeAsset:
        @param Poles:
        """
        #: Pole species. Aluminum, Aluminum Davit, Concrete, Fiberglass, Galvanized Davit, Galvanized, Steel Davit Primed, Steel Davit, Steel Standard Primed, Steel, Truncated, Wood-Treated, Wood-Hard, Wood-Salt Treated, Wood-Soft, Wood, Other, Unknown.
        self.speciesType = speciesType

        #: Pole class: 1, 2, 3, 4, 5, 6, 7, H1, H2, Other, Unknown.
        self.classification = classification

        self._PoleTypeAsset = None
        self.PoleTypeAsset = PoleTypeAsset

        self._Poles = []
        self.Poles = [] if Poles is None else Poles

        super(PoleModel, self).__init__(*args, **kw_args)

    def getPoleTypeAsset(self):
        
        return self._PoleTypeAsset

    def setPoleTypeAsset(self, value):
        if self._PoleTypeAsset is not None:
            filtered = [x for x in self.PoleTypeAsset.PoleModels if x != self]
            self._PoleTypeAsset._PoleModels = filtered

        self._PoleTypeAsset = value
        if self._PoleTypeAsset is not None:
            self._PoleTypeAsset._PoleModels.append(self)

    PoleTypeAsset = property(getPoleTypeAsset, setPoleTypeAsset)

    def getPoles(self):
        
        return self._Poles

    def setPoles(self, value):
        for x in self._Poles:
            x._PoleModel = None
        for y in value:
            y._PoleModel = self
        self._Poles = value

    Poles = property(getPoles, setPoles)

    def addPoles(self, *Poles):
        for obj in Poles:
            obj._PoleModel = self
            self._Poles.append(obj)

    def removePoles(self, *Poles):
        for obj in Poles:
            obj._PoleModel = None
            self._Poles.remove(obj)

