FROM nvidia/opengl:1.0-glvnd-runtime-ubuntu18.04
MAINTAINER Matthias Mayer <matthias.mayer@tum.de>

RUN cd /home/ && apt-get update && apt-get install -y python3.6 python3-pip
COPY requirements.txt /home/
#mayavi dependencies:
RUN apt-get install -y libsm6 libxext6 libxrender-dev libglvnd-dev
RUN cd /home/ && pip3 install -r requirements.txt
RUN rm /home/requirements.txt
RUN mkdir spot_server
COPY ltl_inp_form.py /home/spot_server/

# install graph-tool
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y keyboard-configuration
RUN echo "deb [ arch=amd64 ] https://downloads.skewed.de/apt bionic main" >> /etc/apt/sources.list && \
    apt-key adv --keyserver keys.openpgp.org --recv-key 612DEFB798507F25 && \
    apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y python3-graph-tool

RUN apt-get install -y libcairo2-dev && pip3 install jupyter pycairo

# Mayavi additional stuff
RUN apt-get install -y xvfb libxkbcommon-x11-0 && pip3 install ipyevents && \
    jupyter nbextension install --py mayavi --user

# Run Jupyter notebook as Docker main process
CMD ["jupyter", "notebook", "--allow-root", "--notebook-dir=/home/spot_server", "--ip='0.0.0.0'", "--port=8888", "--no-browser"]
