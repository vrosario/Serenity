#!/bin/bash

#number of pods
 oc create clusterresourcequota student-resource-quota --project-label-selector=level=ist-student --hard=pods=3 #--hard=secrets=20

 oc create clusterresourcequota student-adv-resource-quota --project-label-selector=level=ist-student-adv --hard=pods=6 #--hard=secrets=20


#create limit range
oc create -f <limit_range_file> -n <project>
oc create -f pod-limit-range.yaml -n prusso-test-1
