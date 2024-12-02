FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

RUN pip install -r requirements/requirements.txt

CMD ["python", "manage.py", "run_tg_bot"]