import pyttsx3

# id speech VN: [b'\x05vi']
#id speech US: [b'\x02en-us']

engine = pyttsx3.init()
value = 150
engine.setProperty('rate', value)
engine.say("Xin chào, bạn đang làm gì?")
engine.runAndWait()