#!/bin/bash

 oc create clusterresourcequota student-resource-quota \ 
    --project-label-selector=level=student \ 
    --hard=pods=6 #--hard=secrets=20