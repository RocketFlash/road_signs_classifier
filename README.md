# Road Signs Classifier

ROS node for road signs classification based on Siamese architecture


# Usage

## Using Docker container

### Requirements
- Docker CE
- nvidia-docker2

Clone this repo to your catkin workspace

Run docker container

```bash
$ docker run -v /home/rauf/catkin_ws/src/:/home/road_signs_classifier/catkin_ws/src -it --rm --runtime nvidia --name road_signs_classif --net host --add-host road_signs_docker:127.0.0.1 --add-host unihost-dg03:127.0.0.1 --add-host detect_docker:127.0.0.1 --hostname road_signs_docker rocketflash/road_signs_classifier:latest
```

Inside docker build package using catkin_make
```bash
$ cd ~/catkin_ws/ && catkin_make
$ source devel/setup.bash
```

Run classifier node

```bash
$ rosrun road_signs_classifier classifier_node.py
```