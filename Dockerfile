FROM python:3.9

RUN apt update && apt install tzdata -y
ENV TZ="Europe/Warsaw"

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-u", "app.py"]