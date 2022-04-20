import os
import videoAnalysis
import frameSelector
import frameExtractor
import makePdf
import downloader

# downloader.main() # edit downloader.py to fit your use case and comment this in if needed

video_folders = os.listdir("videos")
for folder in video_folders:
    video_files = os.listdir(f"videos/{folder}")
    for video in video_files:
        print(f"Current file: {video}")
        path_to_file = f"videos/{folder}/{video}"

        
        FRAMES_SKIP=30  # Increase value for faster processing but may lead to skipped slides
        FOLDER_PATH= f"ExtractedSlides/{folder}/{video[:-4]}" 
        try:
            os.makedirs(FOLDER_PATH)
        except FileExistsError:
            pass
        VIDEO_PATH= path_to_file

        videoAnalysis.videoAnalysis(FRAMES_SKIP, VIDEO_PATH)
        selectedFrames= frameSelector.frameSelector()
        frameExtractor.frameExtractor(FOLDER_PATH, VIDEO_PATH, selectedFrames)
        makePdf.makePdf(FOLDER_PATH)
