import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        self.assertEqual(
            emotion_detector("I am glad this happened")["dominant_emotion"],
            "joy"
        )

    def test_anger(self):
        self.assertEqual(
            emotion_detector("I am really mad about this")["dominant_emotion"],
            "anger"
        )

    def test_disgust(self):
        self.assertEqual(
            emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"],
            "disgust"
        )

    def test_fear(self):
        self.assertEqual(
            emotion_detector("I am so afraid of this")["dominant_emotion"],
            "fear"
        )

    def test_sadness(self):
        self.assertEqual(
            emotion_detector("I am really sad about this")["dominant_emotion"],
            "sadness"
        )

if __name__ == "__main__":
    unittest.main()
