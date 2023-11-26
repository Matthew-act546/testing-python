import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Test for the anonymous survey"""

    def setUp(self):
        question = "What is your programming langguage/s"
        self.my_survey= AnonymousSurvey(question)
        self.my_survey.store_responses("English")
        self.responses = ["Java", "Python", "C"]
         
    def test_store_single_response(self):
        self.my_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_responses(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == "__main__":
    unittest.main()