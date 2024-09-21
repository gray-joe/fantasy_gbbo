# Fantasy Bake Off

`docker run --name postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres`

`poetry run uvicorn app.app:app --reload`

`curl -X 'POST'   'http://127.0.0.1:8000/leagues/'   -H 'Content-Type: application/json'   -d '{"name": "Lord of the party rings", "code": "L123"}'`
