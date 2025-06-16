FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir flask  # Flask 설치 필요
RUN pip install --no-cache-dir pymysql
RUN pip install --no-cache-dir cryptography
CMD ["python", "app.py"]
