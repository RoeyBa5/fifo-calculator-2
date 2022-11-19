FROM python:3.9.12-slim

RUN pip install fastapi uvicorn poetry wheel virtualenv

EXPOSE 8000

WORKDIR /usr/src/fifo_calculator

ENV PORT 8000
ENV HOST "0.0.0.0"
COPY ./ /fifo_calculator

WORKDIR /fifo_calculator
RUN poetry config virtualenvs.create false \
  && pip3 install -r requirements.txt

CMD ["uvicorn", "main:app"]