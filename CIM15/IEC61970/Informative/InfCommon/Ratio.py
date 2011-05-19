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


class Ratio(object):
    """Fraction specified explicitly with a numerator and denominator, which can be used to calculate the quotient.Fraction specified explicitly with a numerator and denominator, which can be used to calculate the quotient.
    """

    def __init__(self, numerator=0.0, denominator=0.0):
        """Initialises a new 'Ratio' instance.

        @param numerator: The part of a fraction that is above the line and signifies the number to be divided by the denominator. 
        @param denominator: The part of a fraction that is below the line and that functions as the divisor of the numerator. 
        """
        #: The part of a fraction that is above the line and signifies the number to be divided by the denominator.
        self.numerator = numerator

        #: The part of a fraction that is below the line and that functions as the divisor of the numerator.
        self.denominator = denominator


    _attrs = ["numerator", "denominator"]
    _attr_types = {"numerator": float, "denominator": float}
    _defaults = {"numerator": 0.0, "denominator": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

