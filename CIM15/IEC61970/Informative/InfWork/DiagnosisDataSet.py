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

class DiagnosisDataSet(ProcedureDataSet):
    """The result of a problem (typically an asset failure) diagnosis.The result of a problem (typically an asset failure) diagnosis.
    """

    def __init__(self, finalCause='', finalRemark='', phaseCode="s12N", preliminaryDateTime='', preliminaryCode='', rootRemark='', rootCause='', preliminaryRemark='', effect='', finalOrigin='', finalCode='', rootOrigin='', failureMode='', *args, **kw_args):
        """Initialises a new 'DiagnosisDataSet' instance.

        @param finalCause: Cause of problem determined during diagnosis. 
        @param finalRemark: Remarks pertaining to findings during problem diagnosis. 
        @param phaseCode: Phase(s) diagnosed. Values are: "s12N", "BN", "BC", "ABN", "s2N", "N", "ACN", "BCN", "ABCN", "AC", "s1N", "AN", "B", "AB", "C", "A", "CN", "ABC"
        @param preliminaryDateTime: Date and time preliminary assessment of problem was performed. 
        @param preliminaryCode: Code for problem category determined during preliminary assessment. 
        @param rootRemark: Remarks pertaining to root cause findings during problem diagnosis. 
        @param rootCause: Root cause of problem determined during diagnosis. 
        @param preliminaryRemark: Remarks pertaining to preliminary assessment of problem. 
        @param effect: Effect of problem. 
        @param finalOrigin: Origin of problem determined during diagnosis. 
        @param finalCode: Code for diagnosed probem category. 
        @param rootOrigin: Root origin of problem determined during diagnosis. 
        @param failureMode: Failuer mode, for example: Failure to Insulate; Failure to conduct; Failure to contain oil; Failure to provide ground plane; Other. 
        """
        #: Cause of problem determined during diagnosis.
        self.finalCause = finalCause

        #: Remarks pertaining to findings during problem diagnosis.
        self.finalRemark = finalRemark

        #: Phase(s) diagnosed. Values are: "s12N", "BN", "BC", "ABN", "s2N", "N", "ACN", "BCN", "ABCN", "AC", "s1N", "AN", "B", "AB", "C", "A", "CN", "ABC"
        self.phaseCode = phaseCode

        #: Date and time preliminary assessment of problem was performed.
        self.preliminaryDateTime = preliminaryDateTime

        #: Code for problem category determined during preliminary assessment.
        self.preliminaryCode = preliminaryCode

        #: Remarks pertaining to root cause findings during problem diagnosis.
        self.rootRemark = rootRemark

        #: Root cause of problem determined during diagnosis.
        self.rootCause = rootCause

        #: Remarks pertaining to preliminary assessment of problem.
        self.preliminaryRemark = preliminaryRemark

        #: Effect of problem.
        self.effect = effect

        #: Origin of problem determined during diagnosis.
        self.finalOrigin = finalOrigin

        #: Code for diagnosed probem category.
        self.finalCode = finalCode

        #: Root origin of problem determined during diagnosis.
        self.rootOrigin = rootOrigin

        #: Failuer mode, for example: Failure to Insulate; Failure to conduct; Failure to contain oil; Failure to provide ground plane; Other.
        self.failureMode = failureMode

        super(DiagnosisDataSet, self).__init__(*args, **kw_args)

    _attrs = ["finalCause", "finalRemark", "phaseCode", "preliminaryDateTime", "preliminaryCode", "rootRemark", "rootCause", "preliminaryRemark", "effect", "finalOrigin", "finalCode", "rootOrigin", "failureMode"]
    _attr_types = {"finalCause": str, "finalRemark": str, "phaseCode": str, "preliminaryDateTime": str, "preliminaryCode": str, "rootRemark": str, "rootCause": str, "preliminaryRemark": str, "effect": str, "finalOrigin": str, "finalCode": str, "rootOrigin": str, "failureMode": str}
    _defaults = {"finalCause": '', "finalRemark": '', "phaseCode": "s12N", "preliminaryDateTime": '', "preliminaryCode": '', "rootRemark": '', "rootCause": '', "preliminaryRemark": '', "effect": '', "finalOrigin": '', "finalCode": '', "rootOrigin": '', "failureMode": ''}
    _enums = {"phaseCode": "PhaseCode"}
    _refs = []
    _many_refs = []

