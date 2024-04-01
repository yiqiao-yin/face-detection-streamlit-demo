# 🎥 Face Detection Web App 🎬

Welcome to the Face Detection Web App! 👋

This interactive application allows you to detect faces in live video streams. 😊

## How it Works

1. **Open the App**: Click [here](https://face-detection-demo.streamlit.app/) to launch the web app.
   
2. **Enable Your Camera**: Grant permission to access your camera.

3. **See the Magic Happen**: Watch as the app detects faces in real-time and draws rectangles around them.

## Code Overview

The magic behind this app is powered by Python and the following libraries:

- `streamlit_webrtc`: A Streamlit component for WebRTC-based live video streams.
- `av`: A library for working with audio and video frames.
- `OpenCV`: A computer vision library for face detection.

Here's a quick overview of what's happening in the code:

- We define a `VideoProcessor` class to process incoming video frames.
- Each frame is analyzed to detect faces using OpenCV's Haar cascade classifier.
- Detected faces are highlighted with green rectangles.
- Finally, the processed frames are streamed back to the user in real-time.

## Try it Yourself! 🚀

Experience the excitement of face detection firsthand! Launch the [Face Detection Web App](https://face-detection-demo.streamlit.app/) now!

Feel free to explore, have fun, and share with your friends! 🎉

If you have any feedback or suggestions, we'd love to hear from you. Happy face detecting! 😄
