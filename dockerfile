FROM python:3.11-alpine

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "run_tg_bot"]