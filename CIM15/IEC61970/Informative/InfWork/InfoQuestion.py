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

from CIM15.IEC61968.Common.Document import Document

class InfoQuestion(Document):
    """Questions and answers associated with a type of document for purposes of clarification. Questions may be predefined or ad hoc.Questions and answers associated with a type of document for purposes of clarification. Questions may be predefined or ad hoc.
    """

    def __init__(self, answer='', answerRemark='', questionText='', answerDateTime='', questionCode='', questionRemark='', questionCategory='', *args, **kw_args):
        """Initialises a new 'InfoQuestion' instance.

        @param answer: Answer to question. 
        @param answerRemark: Remarks to qualify the answer. 
        @param questionText: For non-coded questions, the question is provided here. 
        @param answerDateTime: The date and time the quesiton was answered. 
        @param questionCode: The question code. If blank, refer to questionText. 
        @param questionRemark: Remarks to qualify the question in this situation. 
        @param questionCategory: The category of the question. 
        """
        #: Answer to question.
        self.answer = answer

        #: Remarks to qualify the answer.
        self.answerRemark = answerRemark

        #: For non-coded questions, the question is provided here.
        self.questionText = questionText

        #: The date and time the quesiton was answered.
        self.answerDateTime = answerDateTime

        #: The question code. If blank, refer to questionText.
        self.questionCode = questionCode

        #: Remarks to qualify the question in this situation.
        self.questionRemark = questionRemark

        #: The category of the question.
        self.questionCategory = questionCategory

        super(InfoQuestion, self).__init__(*args, **kw_args)

    _attrs = ["answer", "answerRemark", "questionText", "answerDateTime", "questionCode", "questionRemark", "questionCategory"]
    _attr_types = {"answer": str, "answerRemark": str, "questionText": str, "answerDateTime": str, "questionCode": str, "questionRemark": str, "questionCategory": str}
    _defaults = {"answer": '', "answerRemark": '', "questionText": '', "answerDateTime": '', "questionCode": '', "questionRemark": '', "questionCategory": ''}
    _enums = {}
    _refs = []
    _many_refs = []

