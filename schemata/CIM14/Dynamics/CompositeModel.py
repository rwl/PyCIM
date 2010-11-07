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

from CIM14.Element import Element

class CompositeModel(Element):

    def __init__(self, slotReference0=None, **kw_args):
        """Initializes a new 'CompositeModel' instance.

        @param slotReference0:
        """
        self._slotReference0 = []
        self.slotReference0 = [] if slotReference0 is None else slotReference0

        super(CompositeModel, self).__init__(**kw_args)

    def getslotReference0(self):
        
        return self._slotReference0

    def setslotReference0(self, value):
        for p in self._slotReference0:
            filtered = [q for q in p.compositeModel0 if q != self]
            self._slotReference0._compositeModel0 = filtered
        for r in value:
            if self not in r._compositeModel0:
                r._compositeModel0.append(self)
        self._slotReference0 = value

    slotReference0 = property(getslotReference0, setslotReference0)

    def addslotReference0(self, *slotReference0):
        for obj in slotReference0:
            if self not in obj._compositeModel0:
                obj._compositeModel0.append(self)
            self._slotReference0.append(obj)

    def removeslotReference0(self, *slotReference0):
        for obj in slotReference0:
            if self in obj._compositeModel0:
                obj._compositeModel0.remove(self)
            self._slotReference0.remove(obj)

