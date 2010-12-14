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

class Pending(Element):
    """When present, a scalar conversion that is associated with IntervalBlock and which needs to be applied to every contained IntervalReading value. This conversion results in a new associated ReadingType, reflecting the true dimensions of interval reading values after the conversion.
    """

    def __init__(self, scalarDenominator=0, scalarFloat=0.0, scalarNumerator=0, multiplyBeforeAdd=False, offset=0, IntervalBlocks=None, ReadingType=None, *args, **kw_args):
        """Initialises a new 'Pending' instance.

        @param scalarDenominator: (if scalar is rational number) When 'IntervalReading.value' is multiplied by this attribute and divided by 'scalarDenominator, it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'. 
        @param scalarFloat: (if scalar is floating number) When multiplied with 'IntervalReading.value', it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'. 
        @param scalarNumerator: (if scalar is integer or rational number)  When the scalar is a simple integer, and this attribute is presented alone and multiplied with 'IntervalReading.value', it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'. It is never used in conjunction with 'scalarFloat', only with 'scalarDenominator'. 
        @param multiplyBeforeAdd: Whether scalars should be applied before adding the 'offset'. 
        @param offset: (if applicable) Offset to be added as well as multiplication using scalars. 
        @param IntervalBlocks: All blocks of interval reading values to which this pending conversion applies.
        @param ReadingType: Reading type resulting from this pending conversion.
        """
        #: (if scalar is rational number) When 'IntervalReading.value' is multiplied by this attribute and divided by 'scalarDenominator, it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'.
        self.scalarDenominator = scalarDenominator

        #: (if scalar is floating number) When multiplied with 'IntervalReading.value', it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'.
        self.scalarFloat = scalarFloat

        #: (if scalar is integer or rational number)  When the scalar is a simple integer, and this attribute is presented alone and multiplied with 'IntervalReading.value', it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'. It is never used in conjunction with 'scalarFloat', only with 'scalarDenominator'.
        self.scalarNumerator = scalarNumerator

        #: Whether scalars should be applied before adding the 'offset'.
        self.multiplyBeforeAdd = multiplyBeforeAdd

        #: (if applicable) Offset to be added as well as multiplication using scalars.
        self.offset = offset

        self._IntervalBlocks = []
        self.IntervalBlocks = [] if IntervalBlocks is None else IntervalBlocks

        self._ReadingType = None
        self.ReadingType = ReadingType

        super(Pending, self).__init__(*args, **kw_args)

    _attrs = ["scalarDenominator", "scalarFloat", "scalarNumerator", "multiplyBeforeAdd", "offset"]
    _attr_types = {"scalarDenominator": int, "scalarFloat": float, "scalarNumerator": int, "multiplyBeforeAdd": bool, "offset": int}
    _defaults = {"scalarDenominator": 0, "scalarFloat": 0.0, "scalarNumerator": 0, "multiplyBeforeAdd": False, "offset": 0}
    _enums = {}
    _refs = ["IntervalBlocks", "ReadingType"]
    _many_refs = ["IntervalBlocks"]

    def getIntervalBlocks(self):
        """All blocks of interval reading values to which this pending conversion applies.
        """
        return self._IntervalBlocks

    def setIntervalBlocks(self, value):
        for x in self._IntervalBlocks:
            x.Pending = None
        for y in value:
            y._Pending = self
        self._IntervalBlocks = value

    IntervalBlocks = property(getIntervalBlocks, setIntervalBlocks)

    def addIntervalBlocks(self, *IntervalBlocks):
        for obj in IntervalBlocks:
            obj.Pending = self

    def removeIntervalBlocks(self, *IntervalBlocks):
        for obj in IntervalBlocks:
            obj.Pending = None

    def getReadingType(self):
        """Reading type resulting from this pending conversion.
        """
        return self._ReadingType

    def setReadingType(self, value):
        if self._ReadingType is not None:
            self._ReadingType._Pending = None

        self._ReadingType = value
        if self._ReadingType is not None:
            self._ReadingType.Pending = None
            self._ReadingType._Pending = self

    ReadingType = property(getReadingType, setReadingType)

