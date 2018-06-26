import numpy

from video_preprocessing import prepare_video, frames_count
from keras.models import load_model


model = load_model('model.hdf5')

video_path = 'video2.mp4'

rand = (int) (frames_count(video_path) - 99)

data = prepare_video(video_path,min(rand,5))
print(str(numpy.shape(data)))
# print(str(data))
prediction = model.predict(data)
print(prediction)
