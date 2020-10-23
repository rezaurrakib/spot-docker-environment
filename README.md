# Docker Environment for Human Motion Synthesis Platform 

This is a server-client environment, where the Robot Simulation setup intereact with [SPOT](https://spot.lrde.epita.fr/) based setup for LTL formulation. 

### How to deploy
**robotic-sw-env** foleder comprises the contents of the Robot Simulation environment.
  - Dockerfile (containes all the necessary commands to assemble an image for automated build)
  - requirements.txt (list of libraries needed for simulation)

**spot-env** holds the files for SPOT based environment.

For building and starting up both the environments, run **docker-compose.yml** from the project directory with the following command
```bash
$ docker-compose up

Starting docker_compose_test_robotics-sw-env_1 ... done
Recreating docker_compose_test_spot-env_1      ... done
Attaching to docker_compose_test_robotics-sw-env_1, docker_compose_test_spot-env_1
spot-env_1         | [I 07:12:01.077 NotebookApp] Writing notebook server cookie secret to /home/robotics/.local/share/jupyter/runtime/notebook_cookie_secret
robotics-sw-env_1  | [I 07:12:01.361 NotebookApp] Serving notebooks from local directory: /home/spot_server
robotics-sw-env_1  | [I 07:12:01.362 NotebookApp] Jupyter Notebook 6.1.4 is running at:
robotics-sw-env_1  | [I 07:12:01.362 NotebookApp] http://fc880df2d479:8888/?token=440110631be086af556c44cad3fb9d7a512713a5f6245173
robotics-sw-env_1  | [I 07:12:01.362 NotebookApp]  or http://127.0.0.1:8888/?token=440110631be086af556c44cad3fb9d7a512713a5f6245173
robotics-sw-env_1  | [I 07:12:01.362 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
robotics-sw-env_1  | [C 07:12:01.404 NotebookApp] 
robotics-sw-env_1  |     
robotics-sw-env_1  |     To access the notebook, open this file in a browser:
robotics-sw-env_1  |         file:///root/.local/share/jupyter/runtime/nbserver-1-open.html
robotics-sw-env_1  |     Or copy and paste one of these URLs:
robotics-sw-env_1  |         http://fc880df2d479:8888/?token=440110631be086af556c44cad3fb9d7a512713a5f6245173
robotics-sw-env_1  |      or http://127.0.0.1:8888/?token=440110631be086af556c44cad3fb9d7a512713a5f6245173
spot-env_1         | [I 07:12:03.624 NotebookApp] JupyterLab extension loaded from /home/robotics/anaconda3/lib/python3.8/site-packages/jupyterlab
spot-env_1         | [I 07:12:03.624 NotebookApp] JupyterLab application directory is /home/robotics/anaconda3/share/jupyter/lab
spot-env_1         | [I 07:12:03.634 NotebookApp] Serving notebooks from local directory: /home/robotics/spot_server
spot-env_1         | [I 07:12:03.634 NotebookApp] The Jupyter Notebook is running at:
spot-env_1         | [I 07:12:03.634 NotebookApp] http://61d6b9c336e1:8888/?token=a77ed0f1b55e87c9fcd0161655c4392b01d17a70884f8999
spot-env_1         | [I 07:12:03.634 NotebookApp]  or http://127.0.0.1:8888/?token=a77ed0f1b55e87c9fcd0161655c4392b01d17a70884f8999
spot-env_1         | [I 07:12:03.635 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
spot-env_1         | [C 07:12:03.658 NotebookApp] 
spot-env_1         |     
spot-env_1         |     To access the notebook, open this file in a browser:
spot-env_1         |         file:///home/robotics/.local/share/jupyter/runtime/nbserver-1-open.html
spot-env_1         |     Or copy and paste one of these URLs:
spot-env_1         |         http://61d6b9c336e1:8888/?token=a77ed0f1b55e87c9fcd0161655c4392b01d17a70884f8999
spot-env_1         |      or http://127.0.0.1:8888/?token=a77ed0f1b55e87c9fcd0161655c4392b01d17a70884f8999

```
Compose pulls the desired images, builds the images for the code, and starts the services defined in both Dockerfiles. Both of the services run two jupyter notebooks in two separate ports **8000 and 8001**. You need token to run both of these notebooks. Open a browser and go to **https://localhost/port_number**, a jupyter login page will pop up that requires token for authentication. From the notebook url presented above (after running the compose up command) for each of the environments, copy the token part and paste it in the coprresponding jupyter login page to enter the jupyter notebook environment. 

### Mounted volume in local directory
Both of the services is mounted on a local directory called **spot-env-shared-volume**. First you should create this folder at your `home` directory in Linux. Otherwise the folder created after **compose up** command will make it a private forlder, which will not let you create files in docker environment.

### LTL Graph parser
The jupyter notebook build from the **spot-env** Dockerfile comes with a SPOT installed enviroment. It creates notebook ready for development with SPOT Library for LTL, ω-automata manipulation and model checking in Python 3. The commands for the source code build for SPOT can be found on the corresponding Dockerfile. The dockerfile will also install a small python module called [ltl-grraph-parser](https://pypi.org/project/ltl-parser-pkg/). Currently the version 0.1.2 will come with the default installation. If you want to change it or extend it, you can modify it into the **ltl_graph_parser.py** file in the [ltl_parser](https://github.com/rezaurrakib/ltl_parser) repository.   


