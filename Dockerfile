FROM jupyter/base-notebook

CMD ["start-notebook.sh", "--NotebookApp.token=''", "--notebook-dir=/home/jovyan/source"]
