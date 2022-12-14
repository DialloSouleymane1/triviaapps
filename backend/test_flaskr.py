import os
from unicodedata import category
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from flaskr.models import setup_db
from settings import TEST_DB_NAME,TEST_DB_PASSWORD,TEST_DB_USER, TEST_DOMAINE_NAME


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        # self.database_name = "trivia_test"
        # self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            TEST_DB_USER, TEST_DB_PASSWORD, TEST_DOMAINE_NAME, TEST_DB_NAME
        )
        setup_db(self.app, self.database_path)

        self.new_question = {"question": "What is Flask ?", "answer": "A micro Framework of Python", "category": 1, "difficulty":1}
        
        self.myparams = {
            "quiz_category": {
                "type": "Art",
                "id": "2"},
            "previous_questions": []
        }
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_paginated_questions(self):
        res = self.client().get("/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["questions"]))
        self.assertTrue(len(data["categories"]))
        # self.assertTrue(len(data["current_category"]))

    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client().get("/questions?page=1500", json={"page": 1})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")
    

    def test_delete_question(self):
        res = self.client().delete("/questions/10")
        data = json.loads(res.data)
        # question = Question.query.filter(Question.id == 10).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["deleted"], 10)
        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["questions"]))

    def test_get_question_search_with_results(self):
        res = self.client().post("/questions/search", json={"searchTerm": "title"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])
        self.assertTrue((data["total_questions"]))

    def test_get_question_search_without_results(self):
        res = self.client().post("/questions/search", json={"searchTerm": "Doumbouya"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["questions"], [])

    def test_422_if_question_does_not_exist(self):
        res = self.client().delete("/questions/1300")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def test_get_categories(self):
        res = self.client().get("/categories")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["categories"])
    
    def test_422_quizzes_if_quiz_category_does_not_exist(self):
        res = self.client().post("/quizzes", json={"quiz_category":{'type': 'Art', 'id': '100'}, "previous_questions":[]})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")
    

    def test_get_questions_by_category_id(self):
        res = self.client().get("/categories/2/questions")
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])
        self.assertTrue(data["current_category"])
        self.assertTrue(len(data["questions"]))


    def test_get_quizzes(self):
        res = self.client().post("/quizzes", json=self.myparams)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["question"])


    def test_create_new_question(self):
        res = self.client().post("/questions", json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["created"])
        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["questions"]))


    # def test_405_if_question_creation_not_allowed(self):
    #     res = self.client().post("/questions/4", json=self.new_question)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 405)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "method not allowed")

    

    
    
        
    
        
    
    
    

    

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()