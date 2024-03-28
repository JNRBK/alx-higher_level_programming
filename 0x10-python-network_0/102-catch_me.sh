#!/bin/bash
#script that makes request to 0.0.0.0:5000/catch_me and causes server to respond with a message of You Got Me !
curl -sLX PUT -H "origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
