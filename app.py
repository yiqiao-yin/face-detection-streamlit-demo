from streamlit_webrtc import webrtc_streamer, RTCConfiguration
import streamlit as st
import av
import cv2

# Title
st.set_page_config(page_title="Face Detector", page_icon="🤖", layout="wide")
st.write("# Welcome to the Cascade Classifier from OpenCV - Quick Demo! 🤖")


# Model
# cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


class VideoProcessor:
    """Class to process video frames."""

    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        """Receive a video frame, detect faces, and draw rectangles around them.

        Args:
            frame (av.VideoFrame): Input video frame.

        Returns:
            av.VideoFrame: Processed video frame with rectangles drawn around faces.
        """
        frm = frame.to_ndarray(format="bgr24")
        faces = cascade.detectMultiScale(
            cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY), 1.1, 3
        )
        i = 1
        for x, y, w, h in faces:
            cv2.rectangle(frm, (x, y), (x + w, y + h), (0, 255, 0), 1)
            cv2.putText(frm, f"Person {i}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.putText(frm, f"No. of people: {i}", (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1, cv2.LINE_AA)
            i += 1

        return av.VideoFrame.from_ndarray(frm, format="bgr24")


webrtc_streamer(
    key="key",
    video_processor_factory=VideoProcessor,
    rtc_configuration=RTCConfiguration(
        {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
    ),
)
