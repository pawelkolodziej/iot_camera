#!/bin/bash

API="YOURKEY"
MSG="$1"

curl -u $API: https://api.pushbullet.com/v2/pushes -d type=note -d title="iot_camera" -d body="$MSG"