#!/bin/bash

FILES="data/carla-jack-multi data/carla-rack data/carla-jack-single data/carla-single data/carla-single data/carla-patchbay data/carla-control data/carla-settings data/carla-database data/carla source/frontend/carla_skin.py source/frontend/carla_widgets.py source/frontend/carla_shared.py source/tests/CarlaUtils3.cpp source/tests/CarlaUtils2.cpp"

for Files in $FILES
do
    echo "Change path from lib to lib64"
    sed -i -e "s/\/lib\//\/lib64\//g" $Files
done
