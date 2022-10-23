FROM jupyter/base-notebook

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./packages packages
ENV PYTHONPATH=$PYTHONPATH:/home/jovyan/packages

CMD ["start-notebook.sh", "--NotebookApp.token=''", "--notebook-dir=/home/jovyan/source"]
