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

from CIM15.Element import Element

class PendingCalculation(Element):
    """When present, a scalar conversion that needs to be applied to every IntervalReading.value contained in IntervalBlock. This conversion results in a new associated ReadingType, reflecting the true dimensions of IntervalReading values after the conversion.When present, a scalar conversion that needs to be applied to every IntervalReading.value contained in IntervalBlock. This conversion results in a new associated ReadingType, reflecting the true dimensions of IntervalReading values after the conversion.
    """

    def __init__(self, scalarNumerator=0, multiplyBeforeAdd=False, scalarDenominator=0, scalarFloat=0.0, offset=0, IntervalBlocks=None, ReadingType=None, *args, **kw_args):
        """Initialises a new 'PendingCalculation' instance.

        @param scalarNumerator: (if scalar is integer or rational number)  When the scalar is a simple integer, and this attribute is presented alone and multiplied with 'IntervalReading.value', it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'. It is never used in conjunction with 'scalarFloat', only with 'scalarDenominator'. 
        @param multiplyBeforeAdd: Whether scalars should be applied before adding the 'offset'. 
        @param scalarDenominator: (if scalar is rational number) When 'IntervalReading.value' is multiplied by this attribute and divided by 'scalarDenominator, it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'. 
        @param scalarFloat: (if scalar is floating number) When multiplied with 'IntervalReading.value', it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'. 
        @param offset: (if applicable) Offset to be added as well as multiplication using scalars. 
        @param IntervalBlocks: All blocks of interval reading values to which this pending conversion applies.
        @param ReadingType: Reading type resulting from this pending conversion.
        """
        #: (if scalar is integer or rational number)  When the scalar is a simple integer, and this attribute is presented alone and multiplied with 'IntervalReading.value', it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'. It is never used in conjunction with 'scalarFloat', only with 'scalarDenominator'.
        self.scalarNumerator = scalarNumerator

        #: Whether scalars should be applied before adding the 'offset'.
        self.multiplyBeforeAdd = multiplyBeforeAdd

        #: (if scalar is rational number) When 'IntervalReading.value' is multiplied by this attribute and divided by 'scalarDenominator, it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'.
        self.scalarDenominator = scalarDenominator

        #: (if scalar is floating number) When multiplied with 'IntervalReading.value', it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'.
        self.scalarFloat = scalarFloat

        #: (if applicable) Offset to be added as well as multiplication using scalars.
        self.offset = offset

        self._IntervalBlocks = []
        self.IntervalBlocks = [] if IntervalBlocks is None else IntervalBlocks

        self._ReadingType = None
        self.ReadingType = ReadingType

        super(PendingCalculation, self).__init__(*args, **kw_args)

    _attrs = ["scalarNumerator", "multiplyBeforeAdd", "scalarDenominator", "scalarFloat", "offset"]
    _attr_types = {"scalarNumerator": int, "multiplyBeforeAdd": bool, "scalarDenominator": int, "scalarFloat": float, "offset": int}
    _defaults = {"scalarNumerator": 0, "multiplyBeforeAdd": False, "scalarDenominator": 0, "scalarFloat": 0.0, "offset": 0}
    _enums = {}
    _refs = ["IntervalBlocks", "ReadingType"]
    _many_refs = ["IntervalBlocks"]

    def getIntervalBlocks(self):
        """All blocks of interval reading values to which this pending conversion applies.
        """
        return self._IntervalBlocks

    def setIntervalBlocks(self, value):
        for x in self._IntervalBlocks:
            x.PendingCalculation = None
        for y in value:
            y._PendingCalculation = self
        self._IntervalBlocks = value

    IntervalBlocks = property(getIntervalBlocks, setIntervalBlocks)

    def addIntervalBlocks(self, *IntervalBlocks):
        for obj in IntervalBlocks:
            obj.PendingCalculation = self

    def removeIntervalBlocks(self, *IntervalBlocks):
        for obj in IntervalBlocks:
            obj.PendingCalculation = None

    def getReadingType(self):
        """Reading type resulting from this pending conversion.
        """
        return self._ReadingType

    def setReadingType(self, value):
        if self._ReadingType is not None:
            self._ReadingType._PendingCalculation = None

        self._ReadingType = value
        if self._ReadingType is not None:
            self._ReadingType.PendingCalculation = None
            self._ReadingType._PendingCalculation = self

    ReadingType = property(getReadingType, setReadingType)

