About:
This project uses all the mentioned technologies to creat a app which detects languages, translates them into englis and also identifies and corrent any grammatical mistakes. This app includs authentication and autorization as well

Setup using docker:

0. Add the OPENAI_API_KEY (security key) in docker-compose.yml file

1. docker compose up -d

2. docker ps -a
   copy the container_id of postgres image

3. docker exec -it {container_id} psql -U postgres

4. CREATE DATABASE lang_process;

5. \q

6. docker compose down

7. docker compose up -d

Setup Without docker:

0. python -m venv venv (fro creating virtaul env)

1. source ./venv/bin/activate (for mac and linux) to activate virtaul enviornment

2. pip install -r requirements.txt

3. create .env file same as .env.local and add the required details.

4. uvicorn src.server:app --reload --host 0.0.0.0 --port 8080 to start the server at port 8080

Api's

Now let's open this endpoint in browser

http://localhost:8000/docs#/

1. First click on the /v1/auth/signup route and create a user

2. After creating user click on the Authorize button to login and setup cookies in the frontend

3. Use the /v1/model/convert endpoint ( this endpoint takes any language as parameter then detects the language, convert's it into English, checks for grammar mistakes and informs users.
   )
   Enter your language in the text box

4. Other endoponts include /me to know about the current user

5. /token to generate a new token
