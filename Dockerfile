FROM jupyter/base-notebook

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["start-notebook.sh", "--NotebookApp.token=''", "--notebook-dir=/home/jovyan/source"]
