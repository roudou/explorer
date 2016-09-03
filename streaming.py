#!/usr/bin/python -O
# -*- coding: utf-8 -*-
#

import cv2, subprocess, sys

process = subprocess.Popen( ["cvlc", "v4l2:///dev/video0", "--sout", "#transcode{vcodec=MJPG,vb=640,width=640,height=480}:duplicate{dst=std{access=http{mime=multipart/x-mixed-replace;boundary=--7b3cc56e5f51db803f790dad720ed50a},mux=mpjpeg,dst=:9090/webcam.mjpg}}"]
                          )

print("Video capture started")
