from video_preprocessing import prepare_video
from keras.models import load_model

model = load_model('model.hdf5')

video_path = 'video.mp4'

data = prepare_video(video_path)

prediction = model.predict(data)

print(prediction)
