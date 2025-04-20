FROM python:3.10

WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y git ffmpeg libsm6 libxext6
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]