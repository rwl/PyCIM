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

class TestDataSet(ProcedureDataSet):
    """Test results, usually obtained by a lab or other independent organisation.Test results, usually obtained by a lab or other independent organisation.
    """

    def __init__(self, specimenToLabDateTime='', conclusion='', specimenID='', *args, **kw_args):
        """Initialises a new 'TestDataSet' instance.

        @param specimenToLabDateTime: Date and time the specimen was received by the lab. 
        @param conclusion: Conclusion drawn from test results. 
        @param specimenID: Identifier of specimen used in inspection or test. 
        """
        #: Date and time the specimen was received by the lab.
        self.specimenToLabDateTime = specimenToLabDateTime

        #: Conclusion drawn from test results.
        self.conclusion = conclusion

        #: Identifier of specimen used in inspection or test.
        self.specimenID = specimenID

        super(TestDataSet, self).__init__(*args, **kw_args)

    _attrs = ["specimenToLabDateTime", "conclusion", "specimenID"]
    _attr_types = {"specimenToLabDateTime": str, "conclusion": str, "specimenID": str}
    _defaults = {"specimenToLabDateTime": '', "conclusion": '', "specimenID": ''}
    _enums = {}
    _refs = []
    _many_refs = []

