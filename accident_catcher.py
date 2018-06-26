import numpy

from video_preprocessing import prepare_video, frames_count, load_set
from keras.models import load_model



def prepare_video(video_file,rand,model):



    sequence = numpy.zeros((1,99,144,256))

    for i in range(rand):
        t, errors = load_set(video_file, i)
        if numpy.shape(t) == (99, 144, 256):
            sequence[0] = t
            prediction = model.predict(sequence)
            print("prediction: " + str(i))
            print(prediction)

    return sequence


model = load_model('model.hdf5')
video_path = 'test.mp4'
num_frames = frames_count(video_path)
rand = int(frames_count(video_path) - 100)

data = prepare_video(video_path,min(rand,9000),model)
# print(str(numpy.shape(data)))
# # print(str(data))
# prediction = model.predict(data)
# print(prediction)