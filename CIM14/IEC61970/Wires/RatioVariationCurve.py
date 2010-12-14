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

from CIM14.IEC61970.Core.Curve import Curve

class RatioVariationCurve(Curve):
    """A Ratio Variation Curve describes the change in tap ratio in relationship to tap step changes.  The tap step is represented using the xValue and the ratio using y1value.
    """

    def __init__(self, RatioTapChanger=None, *args, **kw_args):
        """Initialises a new 'RatioVariationCurve' instance.

        @param RatioTapChanger: A RatioVariationCurve defines tap ratio changes for a RatioTapChanger.
        """
        self._RatioTapChanger = None
        self.RatioTapChanger = RatioTapChanger

        super(RatioVariationCurve, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["RatioTapChanger"]
    _many_refs = []

    def getRatioTapChanger(self):
        """A RatioVariationCurve defines tap ratio changes for a RatioTapChanger.
        """
        return self._RatioTapChanger

    def setRatioTapChanger(self, value):
        if self._RatioTapChanger is not None:
            self._RatioTapChanger._RatioVariationCurve = None

        self._RatioTapChanger = value
        if self._RatioTapChanger is not None:
            self._RatioTapChanger.RatioVariationCurve = None
            self._RatioTapChanger._RatioVariationCurve = self

    RatioTapChanger = property(getRatioTapChanger, setRatioTapChanger)

