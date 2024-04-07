import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Liệt kê tất cả các giọng đọc có sẵn
for voice in voices:
    print(f"ID: {voice.id} - Name: {voice.name}")

# Thử nghiệm với một giọng đọc khác
# Thay 'voice_id' bằng ID thực tế của giọng đọc bạn muốn sử dụng
engine.setProperty('voice', 'english')
engine.say("Hello Nguyen Truong")
engine.runAndWait()
