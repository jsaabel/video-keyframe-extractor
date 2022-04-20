import os
import videoAnalysis
import frameSelector
import frameExtractor
import makePdf
import downloader

FRAMES_SKIP= 100 # Increase value for faster processing but may lead to skipped slides
FOLDER_PATH= os.path.join(os.getcwd(), 'ExtractedSlides') # Folder where slide images and merged pdf will be stored
## EDIT THIS BEFORE RUNNING
VIDEO_PATH= "/home/jonas/Desktop/video-keyframe-extractor/Think%20for%20yourself%20Lecture%201%20part%204.mp4" # Absolute path of video for running script using only / as separator

downloader.main()

# videoAnalysis.videoAnalysis(FRAMES_SKIP, VIDEO_PATH)
# selectedFrames= frameSelector.frameSelector()
# frameExtractor.frameExtractor(FOLDER_PATH, VIDEO_PATH, selectedFrames)
# print('Review extracted slides and delete duplicates or wrong selections.')
# ch= input('Press any key to create PDF or Q to exit... ')
# if ch=='Q' or ch=='q':
#     exit()
# makePdf.makePdf(FOLDER_PATH)
