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

from CIM14v13.Element import Element

class Ratio(Element):
    """Fraction specified explicitly with a numerator and denominator, which can be used to calculate the quotient.
    """

    def __init__(self, denominator=0.0, numerator=0.0, *args, **kw_args):
        """Initializes a new 'Ratio' instance.

        @param denominator: The part of a fraction that is below the line and that functions as the divisor of the numerator. 
        @param numerator: The part of a fraction that is above the line and signifies the number to be divided by the denominator. 
        """
        #: The part of a fraction that is below the line and that functions as the divisor of the numerator. 
        self.denominator = denominator

        #: The part of a fraction that is above the line and signifies the number to be divided by the denominator. 
        self.numerator = numerator

        super(Ratio, self).__init__(*args, **kw_args)

