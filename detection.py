#!/usr/bin/env python3
"""
Assignment 3: Object Detection
"""

import jetson.inference
import jetson.utils

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)

print("Processing Image 1...")
img1 = jetson.utils.loadImage("image1.jpg")
detections1 = net.Detect(img1)

print(f"\nImage 1 Detection Results:")
print(f"Number of detections: {len(detections1)}")
for i, detection in enumerate(detections1):
    print(f"\nDetection {i+1}:")
    print(f"-- ClassID: {detection.ClassID}")
    print(f"-- Confidence: {detection.Confidence}")
    print(f"-- Left: {detection.Left}")
    print(f"-- Top: {detection.Top}")
    print(f"-- Right: {detection.Right}")
    print(f"-- Bottom: {detection.Bottom}")
    print(f"-- Width: {detection.Width}")
    print(f"-- Height: {detection.Height}")
    print(f"-- Area: {detection.Area}")
    print(f"-- Center: {detection.Center}")

jetson.utils.saveImage("detected_image1.jpg", img1)

print("\n\nProcessing Image 2...")
img2 = jetson.utils.loadImage("image2.jpg")
detections2 = net.Detect(img2)

print(f"\nImage 2 Detection Results:")
print(f"Number of detections: {len(detections2)}")
for i, detection in enumerate(detections2):
    print(f"\nDetection {i+1}:")
    print(f"-- ClassID: {detection.ClassID}")
    print(f"-- Confidence: {detection.Confidence}")
    print(f"-- Left: {detection.Left}")
    print(f"-- Top: {detection.Top}")
    print(f"-- Right: {detection.Right}")
    print(f"-- Bottom: {detection.Bottom}")
    print(f"-- Width: {detection.Width}")
    print(f"-- Height: {detection.Height}")
    print(f"-- Area: {detection.Area}")
    print(f"-- Center: {detection.Center}")

# Save output with detections
jetson.utils.saveImage("detected_image2.jpg", img2)

print("\nDetection complete! Check detected_image1.jpg and detected_image2.jpg for results.")