FROM python:3.12-slim

WORKDIR /app

COPY task.py .

RUN mkdir -p /app/data

ENV TASKS_FILE=/app/data/tasks.json

VOLUME ["/app/data"]

ENTRYPOINT ["python", "task.py"]
CMD []