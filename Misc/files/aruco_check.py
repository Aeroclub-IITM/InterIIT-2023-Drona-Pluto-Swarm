import numpy as np
import cv2
import cv2.aruco as aruco

# Create a dictionary of ArUco markers
aruco_dict  = aruco.getPredefinedDictionary(aruco.DICT_4X4_250)
parameters  = aruco.DetectorParameters()

# Create a video capture object
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the video
    ret, frame = cap.read()

    # # Convert the frame to grayscale
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # # Detect ArUco markers in the frame
    # corners, ids, _ = aruco.detectMarkers(gray, aruco_dict)




    gray    = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #-- remember, OpenCV stores color images in Blue, Green, Red

    detector = aruco.ArucoDetector(aruco_dict,parameters)
    #-- Find all the aruco markers in the image
    corners, ids, rejected = detector.detectMarkers(gray)



    # If at least one ArUco marker was detected, draw a bounding box around it
    if corners:
        # Draw a bounding box around each ArUco marker
        aruco.drawDetectedMarkers(frame, corners)

        # Print the number of ArUco markers detected
        print("Number of ArUco markers detected: ", len(corners))
        print (type(ids))
        print (type(ids[0]))
        
        

        # Print the IDs and locations of the ArUco markers
        # for i in range(len(corners)):
        #     # print("ID: ", ids, " Location: ", corners[i][0])

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()