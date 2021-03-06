import datetime
from HoverSpace.models import ANSWERS_COLLECTION, QUESTIONS_COLLECTION
from HoverSpace.user import User
from HoverSpace.QuestionClass import QuestionMethods
from bson.objectid import ObjectId

class Answers():
    #  quesID, short_description, long_description, posetdBy, timestamp, ansID, upvotes, downvotes
    def __init__(self, posetdBy, quesID, ansText):
        self.posetdBy = posetdBy
        self.timestamp = datetime.datetime.utcnow()
        self.ansText = ansText
        self.quesID = quesID


    def post_answer(self):
        ansID = ANSWERS_COLLECTION.insert_one({
                    'posetdBy': self.posetdBy, 'quesID': self.quesID,
                    'ansText': self.ansText, 'timestamp': self.timestamp,
                    'quesID': self.quesID}).inserted_id

        usr = User(self.posetdBy)
        usr.update_answers(str(ansID))
        ques = QuestionMethods(self.quesID)
        ques.update_answers(str(ansID))
        return ansID

class AnswerMethods():
    def __init__(self, quesID):
        self.quesID = quesID

    def get_answers(self, quesID):
        answers = []
        try:
            ans_obj = (QUESTIONS_COLLECTION.find_one({'_id': ObjectId(quesID)}))['ansID']
            for answer in ans_obj:
                answers.append(ANSWERS_COLLECTION.find_one({'_id': ObjectId(answer)}))
        except TypeError:
            answers = []
        return answers
