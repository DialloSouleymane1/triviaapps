# Backend - Trivia API

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createbd trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## To Do Tasks

These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

One note before you delve into your tasks: for each endpoint, you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

1. Use Flask-CORS to enable cross-domain requests and set response headers.
2. Create an endpoint to handle `GET` requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
3. Create an endpoint to handle `GET` requests for all available categories.
4. Create an endpoint to `DELETE` a question using a question `ID`.
5. Create an endpoint to `POST` a new question, which will require the question and answer text, category, and difficulty score.
6. Create a `POST` endpoint to get questions based on category.
7. Create a `POST` endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
8. Create a `POST` endpoint to get questions to play the quiz. This endpoint should take a category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
9. Create error handlers for all expected errors including 400, 404, 422, and 500.

## Documenting your Endpoints

You will need to provide detailed documentation of your API endpoints including the URL, request parameters, and the response body. Use the example below as a reference.

### Documentation Example

`GET '/api/v1.0/categories'`

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, `categories`, that contains an object of `id: category_string` key: value pairs.

```json
{
  "1": "Science",
  "2": "Art",
  "3": "Geography",
  "4": "History",
  "5": "Entertainment",
  "6": "Sports"
}
```

- Returns all the categories
- URI:- http://127.0.0.1:5000/categories
- GET '/categories'
- Response
```json
  {
      "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
      },
      "success": true
  }
```

- Returns all the categories and questions with paginated per 10
- URI:- http://127.0.0.1:5000/questions
- GET '/questions'
- Response
```json
  {
	"categories": [
		{
			"id": 1,
			"type": "Science"
		},
		{
			"id": 2,
			"type": "Art"
		},
		{
			"id": 3,
			"type": "Geography"
		},
		{
			"id": 4,
			"type": "History"
		},
		{
			"id": 5,
			"type": "Entertainment"
		},
		{
			"id": 6,
			"type": "Sports"
		}
	],
	"questions": [
		{
			"answer": "Edward Scissorhands",
			"category": 5,
			"difficulty": 3,
			"id": 6,
			"question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
		},
		{
			"answer": "Muhammad Ali",
			"category": 4,
			"difficulty": 1,
			"id": 9,
			"question": "What boxers original name is Cassius Clay?"
		},
		{
			"answer": "Uruguay",
			"category": 6,
			"difficulty": 4,
			"id": 11,
			"question": "Which country won the first ever soccer World Cup in 1930?"
		},
		{
			"answer": "George Washington Carver",
			"category": 4,
			"difficulty": 2,
			"id": 12,
			"question": "Who invented Peanut Butter?"
		},
		{
			"answer": "Lake Victoria",
			"category": 3,
			"difficulty": 2,
			"id": 13,
			"question": "What is the largest lake in Africa?"
		},
		{
			"answer": "The Palace of Versailles",
			"category": 3,
			"difficulty": 3,
			"id": 14,
			"question": "In which royal palace would you find the Hall of Mirrors?"
		},
		{
			"answer": "Agra",
			"category": 3,
			"difficulty": 2,
			"id": 15,
			"question": "The Taj Mahal is located in which Indian city?"
		},
		{
			"answer": "Escher",
			"category": 2,
			"difficulty": 1,
			"id": 16,
			"question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
		},
		{
			"answer": "Mona Lisa",
			"category": 2,
			"difficulty": 3,
			"id": 17,
			"question": "La Giaconda is better known as what?"
		},
		{
			"answer": "One",
			"category": 2,
			"difficulty": 4,
			"id": 18,
			"question": "How many paintings did Van Gogh sell in his lifetime?"
		}
	],
	"success": true,
	"total_questions": 15
}
```

- Inserting a new question.
- URI:- http://127.0.0.1:5000/questions
- POST '/questions'
- JSON file format (the body)
```json
  {
      "answer": "West Africa",
      "category": "3",
      "difficulty": 1,   
      "question": "Where is Guinea ?"
  }
```
- Response
```json
  {
	"created": 4,
	"questions": [
		{
			"answer": "West Africa",
			"category": 3,
			"difficulty": 1,
			"id": 4,
			"question": "Where is Guinea ?"
		},
		{
			"answer": "Edward Scissorhands",
			"category": 5,
			"difficulty": 3,
			"id": 6,
			"question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
		},
		{
			"answer": "Muhammad Ali",
			"category": 4,
			"difficulty": 1,
			"id": 9,
			"question": "What boxers original name is Cassius Clay?"
		},
		{
			"answer": "Uruguay",
			"category": 6,
			"difficulty": 4,
			"id": 11,
			"question": "Which country won the first ever soccer World Cup in 1930?"
		},
		{
			"answer": "George Washington Carver",
			"category": 4,
			"difficulty": 2,
			"id": 12,
			"question": "Who invented Peanut Butter?"
		},
		{
			"answer": "Lake Victoria",
			"category": 3,
			"difficulty": 2,
			"id": 13,
			"question": "What is the largest lake in Africa?"
		},
		{
			"answer": "The Palace of Versailles",
			"category": 3,
			"difficulty": 3,
			"id": 14,
			"question": "In which royal palace would you find the Hall of Mirrors?"
		},
		{
			"answer": "Agra",
			"category": 3,
			"difficulty": 2,
			"id": 15,
			"question": "The Taj Mahal is located in which Indian city?"
		},
		{
			"answer": "Escher",
			"category": 2,
			"difficulty": 1,
			"id": 16,
			"question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
		},
		{
			"answer": "Mona Lisa",
			"category": 2,
			"difficulty": 3,
			"id": 17,
			"question": "La Giaconda is better known as what?"
		}
	],
	"success": true,
	"total_questions": 16
}
```


- Get questions based on a search term.
- URI:- http://127.0.0.1:5000/questions/search
- POST '/questions/search'
- JSON file format (the body)
```json
  {
      "searchTerm": "title",
  }
```
- Response
```json

{
	"questions": [
		{
			"answer": "Edward Scissorhands",
			"category": 5,
			"difficulty": 3,
			"id": 6,
			"question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
		}
	],
	"success": true,
	"total_questions": 1
}

```

- Deletes question with given ID.
- URI:- http://127.0.0.1:5000/questions/4
- DELETE '/questions/<int: question_id>'
- Response
```json
  {
	"deleted": 4,
	"questions": [
		{
			"answer": "Edward Scissorhands",
			"category": 5,
			"difficulty": 3,
			"id": 6,
			"question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
		},
		{
			"answer": "Muhammad Ali",
			"category": 4,
			"difficulty": 1,
			"id": 9,
			"question": "What boxers original name is Cassius Clay?"
		},
		{
			"answer": "Uruguay",
			"category": 6,
			"difficulty": 4,
			"id": 11,
			"question": "Which country won the first ever soccer World Cup in 1930?"
		},
		{
			"answer": "George Washington Carver",
			"category": 4,
			"difficulty": 2,
			"id": 12,
			"question": "Who invented Peanut Butter?"
		},
		{
			"answer": "Lake Victoria",
			"category": 3,
			"difficulty": 2,
			"id": 13,
			"question": "What is the largest lake in Africa?"
		},
		{
			"answer": "The Palace of Versailles",
			"category": 3,
			"difficulty": 3,
			"id": 14,
			"question": "In which royal palace would you find the Hall of Mirrors?"
		},
		{
			"answer": "Agra",
			"category": 3,
			"difficulty": 2,
			"id": 15,
			"question": "The Taj Mahal is located in which Indian city?"
		},
		{
			"answer": "Escher",
			"category": 2,
			"difficulty": 1,
			"id": 16,
			"question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
		},
		{
			"answer": "Mona Lisa",
			"category": 2,
			"difficulty": 3,
			"id": 17,
			"question": "La Giaconda is better known as what?"
		},
		{
			"answer": "One",
			"category": 2,
			"difficulty": 4,
			"id": 18,
			"question": "How many paintings did Van Gogh sell in his lifetime?"
		}
	],
	"success": true,
	"total_questions": 15
}
```


- Get questions based on category.
- URI:- http://127.0.0.1:5000/categories/2/questions
- GET '/categories/<int:category_id>/questions'

- Response
```json

{
	"current_category": [
		{
			"id": 2,
			"type": "Art"
		}
	],
	"questions": [
		{
			"answer": "Escher",
			"category": 2,
			"difficulty": 1,
			"id": 16,
			"question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
		},
		{
			"answer": "Mona Lisa",
			"category": 2,
			"difficulty": 3,
			"id": 17,
			"question": "La Giaconda is better known as what?"
		},
		{
			"answer": "One",
			"category": 2,
			"difficulty": 4,
			"id": 18,
			"question": "How many paintings did Van Gogh sell in his lifetime?"
		},
		{
			"answer": "Jackson Pollock",
			"category": 2,
			"difficulty": 2,
			"id": 19,
			"question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
		}
	],
	"success": true,
	"total_questions": 15
}

```



- Get questions to play the quiz.
- URI:- http://127.0.0.1:5000/quizzes
- POST '/quizzes'
- JSON file format (the body)
```json
  {
	"quiz_category": {
		"type": "Geography",
	  "id": "3"},
	"previous_questions": []
}
```
- Response
```json

{
	"question": [
		{
			"answer": "The Palace of Versailles",
			"category": 3,
			"difficulty": 3,
			"id": 14,
			"question": "In which royal palace would you find the Hall of Mirrors?"
		}
	],
	"success": true
}

```



## Testing

Write at least one test for the success and at least one error behavior of each endpoint using the unittest library.

To deploy the tests, run

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
