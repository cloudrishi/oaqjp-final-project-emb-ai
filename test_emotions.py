from emotion_detection import emotion_detector
result = emotion_detector("I love this new technology")
print(json.dumps(result, indent=4))