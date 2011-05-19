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

from CIM15.IEC61970.Informative.InfAssets.ProcedureDataSet import ProcedureDataSet

class MaintenanceDataSet(ProcedureDataSet):
    """The result of a maintenance activity, a type of Procedure, for a given attribute of an asset is documentated in an MaintenanceDataSet.The result of a maintenance activity, a type of Procedure, for a given attribute of an asset is documentated in an MaintenanceDataSet.
    """

    def __init__(self, conditionAfter='', conditionBefore='', maintCode='', *args, **kw_args):
        """Initialises a new 'MaintenanceDataSet' instance.

        @param conditionAfter: Condition of asset just following maintenance procedure. 
        @param conditionBefore: Description of the condition of the asset just prior to maintenance being performed. 
        @param maintCode: Code for the type of maintenance performed. 
        """
        #: Condition of asset just following maintenance procedure.
        self.conditionAfter = conditionAfter

        #: Description of the condition of the asset just prior to maintenance being performed.
        self.conditionBefore = conditionBefore

        #: Code for the type of maintenance performed.
        self.maintCode = maintCode

        super(MaintenanceDataSet, self).__init__(*args, **kw_args)

    _attrs = ["conditionAfter", "conditionBefore", "maintCode"]
    _attr_types = {"conditionAfter": str, "conditionBefore": str, "maintCode": str}
    _defaults = {"conditionAfter": '', "conditionBefore": '', "maintCode": ''}
    _enums = {}
    _refs = []
    _many_refs = []

