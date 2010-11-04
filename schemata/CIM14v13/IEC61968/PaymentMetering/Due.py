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

class Due(Element):
    """Details on amounts due for an account.
    """

    def __init__(self, principle=0.0, current=0.0, charges=0.0, arrears=0.0, interest=0.0, *args, **kw_args):
        """Initializes a new 'Due' instance.

        @param principle: Part of 'current' that constitutes the portion of the principle amount currently due. 
        @param current: Current total amount now due: current = principle + arrears + interest + charges. Typically the rule for settlement priority is: interest dues, then arrears dues, then current dues, then charge dues. 
        @param charges: Part of 'current' that constitutes the charge portion: 'charges' = 'Charge.fixedPortion' + 'Charge.variablePortion'. 
        @param arrears: Part of 'current' that constitutes the arrears portion. 
        @param interest: Part of 'current' that constitutes the interest portion. 
        """
        #: Part of 'current' that constitutes the portion of the principle amount currently due.
        self.principle = principle

        #: Current total amount now due: current = principle + arrears + interest + charges. Typically the rule for settlement priority is: interest dues, then arrears dues, then current dues, then charge dues.
        self.current = current

        #: Part of 'current' that constitutes the charge portion: 'charges' = 'Charge.fixedPortion' + 'Charge.variablePortion'.
        self.charges = charges

        #: Part of 'current' that constitutes the arrears portion.
        self.arrears = arrears

        #: Part of 'current' that constitutes the interest portion.
        self.interest = interest

        super(Due, self).__init__(*args, **kw_args)

