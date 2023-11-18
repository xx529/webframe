FROM python:3.10.12-slim-bullseye
LABEL AUTHORS="Hang"

COPY ./app /project/app
COPY ./requirements.txt /project/requirements.txt

RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir  -i https://pypi.tuna.tsinghua.edu.cn/simple -r /project/requirements.txt && \
    pip cache purge

WORKDIR /project/app

CMD ["python", "main.py"]
