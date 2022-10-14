FROM jupyter/base-notebook

USER root

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY ./tello_sim tello_sim
RUN cd tello_sim && pip install .

CMD ["start-notebook.sh", "--NotebookApp.token=''", "--notebook-dir=/home/jovyan/source"]
