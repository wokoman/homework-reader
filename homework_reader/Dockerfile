FROM python:3.12-slim
WORKDIR /homework_reader
ADD . /homework_reader
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]