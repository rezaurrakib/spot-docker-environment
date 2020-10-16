FROM ubuntu:xenial
MAINTAINER Md Rezaur Rahman <rakib08cse@gmail.com>

# updates and packages
ENV DEBIAN_FRONTEND=noninteractive 
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y sudo vim
RUN apt-get install -y build-essential

# Adding wget and bzip2
RUN apt-get install -y wget bzip2

# Add user robotics with no password, add to sudo group
RUN adduser --disabled-password --gecos '' robotics
RUN adduser robotics sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER robotics
WORKDIR /home/robotics/
RUN chmod a+rwx /home/robotics/
RUN echo `pwd`

# Anaconda installing
RUN wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh
RUN bash Anaconda3-2020.07-Linux-x86_64.sh -b
RUN rm Anaconda3-2020.07-Linux-x86_64.sh

# Set path to conda
ENV PATH /home/robotics/anaconda3/bin:$PATH

# Configuring access to Jupyter
RUN mkdir /home/robotics/notebooks
RUN jupyter notebook --generate-config --allow-root
RUN echo "c.NotebookApp.ip = '0.0.0.0'" >> /home/robotics/.jupyter/jupyter_notebook_config.py


# Installing SPOT library
RUN wget http://www.lrde.epita.fr/dload/spot/spot-2.9.3.tar.gz
RUN tar -xf spot-2.9.3.tar.gz
RUN rm spot-2.9.3.tar.gz
RUN spot-2.9.3/configure --prefix ~/anaconda3/
RUN make
RUN make install

RUN pip install ltl-parser-pkg==0.1.2

# Installing graph tools
RUN sudo apt-get install -y graphviz

# Jupyter listens port: 8888
EXPOSE 8888

RUN mkdir -p /home/robotics/spot_server
COPY ltl_inp_form.py /home/robotics/spot_server/

# Run Jupytewr notebook as Docker main process
CMD ["jupyter", "notebook", "--allow-root", "--notebook-dir=/home/robotics/spot_server", "--ip='0.0.0.0'", "--port=8888", "--no-browser"]
