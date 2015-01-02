#!/bin/bash


sudo docker build --rm=true  -t "davegoopot/ee-balance-checker" .
sudo docker run -ti -v `pwd`:/code "davegoopot/ee-balance-checker"  /bin/bash
