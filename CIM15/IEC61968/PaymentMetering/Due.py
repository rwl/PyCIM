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


class Due(object):
    """Details on amounts due for an account.Details on amounts due for an account.
    """

    def __init__(self, interest=0.0, charges=0.0, principle=0.0, current=0.0, arrears=0.0):
        """Initialises a new 'Due' instance.

        @param interest: Part of 'current' that constitutes the interest portion. 
        @param charges: Part of 'current' that constitutes the charge portion: 'charges' = 'Charge.fixedPortion' + 'Charge.variablePortion'. 
        @param principle: Part of 'current' that constitutes the portion of the principle amount currently due. 
        @param current: Current total amount now due: current = principle + arrears + interest + charges. Typically the rule for settlement priority is: interest dues, then arrears dues, then current dues, then charge dues. 
        @param arrears: Part of 'current' that constitutes the arrears portion. 
        """
        #: Part of 'current' that constitutes the interest portion.
        self.interest = interest

        #: Part of 'current' that constitutes the charge portion: 'charges' = 'Charge.fixedPortion' + 'Charge.variablePortion'.
        self.charges = charges

        #: Part of 'current' that constitutes the portion of the principle amount currently due.
        self.principle = principle

        #: Current total amount now due: current = principle + arrears + interest + charges. Typically the rule for settlement priority is: interest dues, then arrears dues, then current dues, then charge dues.
        self.current = current

        #: Part of 'current' that constitutes the arrears portion.
        self.arrears = arrears


    _attrs = ["interest", "charges", "principle", "current", "arrears"]
    _attr_types = {"interest": float, "charges": float, "principle": float, "current": float, "arrears": float}
    _defaults = {"interest": 0.0, "charges": 0.0, "principle": 0.0, "current": 0.0, "arrears": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

