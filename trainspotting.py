import cv2

def read_video(file_name, display=False):
    video_file = cv2.VideoCapture(file_name)

    # Read iterates through the frames in the video object and returns:
    # 1. Logical - True if a frame has been read
    # 2. Image - an array with the current frame
    read_file, frame = video_file.read()
    original = []
    while read_file:
        # Going to grab the frame and create a list for future use 
        original.append(frame)
        
        if display:
            
            # Use imshow to play video
            cv2.imshow('Original video',frame)
            
            # Pause and allow for "q" button to stop video
            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break
       
        # Get next frame 
        read_file, frame = video_file.read()

        
    if display:
        cv2.destroyWindow('Original video')
    
    video_file.release()
    return original