FROM python:3.12

WORKDIR web

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

COPY web ./web

CMD ["gunicorn", "-b", "0.0.0.0:5000", "web:app"]
