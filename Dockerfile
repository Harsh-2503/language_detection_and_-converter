# 
FROM python:3.9.6

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./src /code/src

#
COPY ./config /code/config

#
COPY ./.env /code/.env

#
COPY ./alembic.ini /code/alembic

# 
CMD ["uvicorn", "src.server:app", "--host", "0.0.0.0", "--port", "80"]