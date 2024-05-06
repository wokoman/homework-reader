FROM cgr.dev/chainguard/python:latest-dev as builder
WORKDIR /homework_reader
COPY requirements.txt .
RUN pip install -r requirements.txt --user --no-cache-dir
FROM cgr.dev/chainguard/python:latest
WORKDIR /homework_reader
COPY --from=builder /home/nonroot/.local/lib/python3.12/site-packages /home/nonroot/.local/lib/python3.12/site-packages
COPY main.py .
EXPOSE 5000
ENTRYPOINT [ "python", "/homework_reader/main.py" ]