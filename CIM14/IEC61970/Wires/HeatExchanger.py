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

from CIM14.IEC61970.Core.Equipment import Equipment

class HeatExchanger(Equipment):
    """Equipment for the cooling of electrical equipment and the extraction of heat
    """

    def __init__(self, PowerTransformer=None, *args, **kw_args):
        """Initialises a new 'HeatExchanger' instance.

        @param PowerTransformer: A transformer may have a heat exchanger
        """
        self._PowerTransformer = None
        self.PowerTransformer = PowerTransformer

        super(HeatExchanger, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["PowerTransformer"]
    _many_refs = []

    def getPowerTransformer(self):
        """A transformer may have a heat exchanger
        """
        return self._PowerTransformer

    def setPowerTransformer(self, value):
        if self._PowerTransformer is not None:
            self._PowerTransformer._HeatExchanger = None

        self._PowerTransformer = value
        if self._PowerTransformer is not None:
            self._PowerTransformer._HeatExchanger = self

    PowerTransformer = property(getPowerTransformer, setPowerTransformer)

