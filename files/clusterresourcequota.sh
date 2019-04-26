#!/bin/bash

 oc create clusterresourcequota student-resource-quota --project-label-selector=level=ist-student --hard=pods=3 #--hard=secrets=20

 oc create clusterresourcequota student-adv-resource-quota --project-label-selector=level=ist-student-adv --hard=pods=6 #--hard=secrets=20