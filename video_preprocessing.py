import cv2
import numpy
import skimage


def frames_count(videofile):
    cap = cv2.VideoCapture(videofile)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return length

def load_set(videofile):
    '''The input is the path to the video file - the training videos are 99 frames long and have resolution of 720x1248
       This will be used for each video, individially, to turn the video into a sequence/stack of frames as arrays
       The shape returned (img) will be 99 (frames per video), 144 (pixels per column), 256 (pixels per row))
    '''
    ### below, the video is loaded in using VideoCapture function
    vidcap = cv2.VideoCapture(videofile)
    ### capturing frames_count of a video
    num_frames = frames_count(videofile)
    ### now, read in the first frame
    success ,image = vidcap.read()
    count = 0       ### start a counter at zero
    error = ''      ### error flag
    success = True  ### start "sucess" flag at True
    all_frames = []
    img = []        ### create an array to save each image as an array as its loaded
    while success: ### while success == True
        success, img = vidcap.read()  ### if success is still true, attempt to read in next frame from vidcap video import
        count += 1  ### increase count
        frames = []  ### frames will be the individual images and frames_resh will be the "processed" ones
        for j in range(0 ,num_frames):
            try:
                success, img = vidcap.read()

                ### conversion from RGB to grayscale image to reduce data
                tmp = skimage.color.rgb2gray(numpy.array(img))
                ### ref for above: https://www.safaribooksonline.com/library/view/programming-computer-vision/9781449341916/ch06.html
                ### downsample image
                #tmp = skimage.transform.downscale_local_mean(tmp, (4,3))
                frames.append(tmp)
                count+=num_frames

            except:
                count+=1
                pass  # print 'There are ', count, ' frame; delete last'        read_frames(videofile, name)

        ### if the frames are the right shape , then save
        # print numpy.shape(frames), numpy.shape(all_frames)
        #if numpy.shape(frames )==(num_frames, 160, 120):
        all_frames.append(frames)

    vidcap.release()
    del frames; del image
    return all_frames, error

def prepare_video(video_file):

    num_frames = frames_count(video_file)
    sequence = numpy.zeros((1,num_frames,640,320))
    t,errors = load_set(video_file)
    #if numpy.shape(t)==(num_frames,160,120):
    sequence[0] = t

    return sequence

