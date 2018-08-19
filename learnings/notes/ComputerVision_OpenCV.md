**Issues with Computer Vision**
1. Camera sensor and lens limitations
2. Viewpoint variations (side view or top view)
3. Changing Lightening conditions (outer or inside)
4. Scaling Issues (close or far)
5. Non-rigid deformations (running horses)
6. Occlusion (partly blocked images)
7. Clutter (Chameleon doubt or photo with a market backgroud)
8. Object class variations (there are so many different types of cars, glasses, beds etc.)
9. Ambiguous Images/Optical Illusions (Negative Space, Mirrage, science-model)

**Images**: 2-dimensional represenation of visible light spectrum (different wavelenghts - different colors ). <BR> 
Image gets formed when light reflects off an object onto a film, sensor or retina.<br>
Using a small opening in the barrier (called aperture), we block off most of the rays of light reducing blurring on the film or sensor. This is the **pinhole camera model**.<br>
Both eyes & camera use an adaptive lens to control:
1. Aperture Size : Controls amount of light, depth of field (bokeh)
2. Lens width: Adjusts focus distance (near or far)

**How images are stored in computers**
* OpenCV by default stores images in RGB color space (Order is BGR). Mixing different intensities of Red, Green & Blue, we can create a full color spectrum. Yellow = Red+Green
* Types of Images: 
    - Black and White Images: Stored in 2-dimensional arrays
        - Grayscale - Ranges of shades of grey
        - Binary - Pixels are either black or white 

**Color Spaces**: RGB (BGR), HSV (Hue, Saturation, Value/Brightness), CMYK
1. HSV:
    - Attempts to represent colors the way humans perceive it.
    - Stores color in cylindrical representation of RGB color points.
        - Hue - Color Value (0-179)
            - For Open-CV, otherwise we do have 359 value as well
            ![02_HueColorSpace.jpg](images/02_HueColorSpace.jpg)
            - Red (165-15)
            - Green (45-75)
            - Blue (90-120)
            
        - Saturation - Vibrancy of Color (0-255)
        
        - Value - Brightness or intensity (0-255)
    - It's useful in computer vision for color segmentation. In RGB, filtering specific colors isn't easy, however, HSV makes it much easier to set color ranges to filter specific colors we perceive them.
![01_HSV_concept.jpg](images/01_HSV_concept.jpg)




**Playing with OpenCV**
1. cv2.imread(<file>)
2. cv2.imshow(<LabelOfWindow>, <NumpyArrayForImage>)
3. cv2.imwrite(<NameOfFile>, <NumpyArrayForImage>)
4. cv2.cvtColor(<NumpyArrayForImage>, cv2.BGR2GRAY) #Grayscaling
5. cv2.imread(<file>, 0) #Grayscaling
<BR>**NOTE** A lot of algorithms/APIs in open-cv require you to first convert the image into gray scaled image (reason being they are easy to process as they have less information but important ones - that's why black & white TV worked fine colors were just a bonus to it but are not necessary)
6. B, G, R = image[10, 50] # BGR Values for the first 0,0 pixel
7. HSV : for color filtering
    - hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    - cv2.imshow('Hue channel', hsv_image[:, :, 0])
    - cv2.imshow('Saturation channel', hsv_image[:, :, 1])
    - cv2.imshow('Value channel', hsv_image[:, :, 2])# Value Channel
    
    - # Let's re-make the original image, 
    - merged = cv2.merge([B, G,R]) 
    - cv2.imshow("Merged", merged)
    
    - # Let's amplify the blue color
    - merged = cv2.merge([B+100, G, R])
    
8. Create Histograms:
    - image = cv2.imread('images/input.jpg') 
    - plt.hist(image.ravel(), 256, [0, 256]); plt.show() # for filled histograms
    - For hollow histogram shapes, find below:
        - histogram2 = cv2.calcHist([image], [0], None, [256], [0, 256]) # Second parameter [0] for blue color extraction and [1] for green and [2] for red etc.  
        - plt.plot(histogram2, color = 'b') # 'r' for red, 'g' for green
        
9. Draw Shapes:
    - cv2.line(image, (startposition), (endposition), (colors), width)
        - cv2.line(image, (0,0), (511,511), (255,127,0), 5)
    - cv2.rectangle(image, (100,100), (300,250), (127,50,127), -1) # -1 means filled
    - cv2.circle(image, (centre), Radius, (15,75,50), -1)
        - cv2.circle(image, (350, 350), 100, (15,75,50), 10)
    - Polynomial:
        - pts = np.array( [[10,50], [400,50], [90,200], [50,500]], np.int32)
        - pts = pts.reshape((-1,1,2))
        - cv2.polylines(image, [pts], True, (0,0,255), 3)
    - Extract Text:
        - cv2.putText(image, 'Hello World!', (75,290), cv2.FONT_HERSHEY_COMPLEX, 2, (100,170,0), 3)
        - Different Fonts supported are:
            - FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN
            - FONT_HERSHEY_DUPLEX,FONT_HERSHEY_COMPLEX 
            - FONT_HERSHEY_TRIPLEX, FONT_HERSHEY_COMPLEX_SMALL
            - FONT_HERSHEY_SCRIPT_SIMPLEX
            - FONT_HERSHEY_SCRIPT_COMPLEX
10. Translation:
    - T = np.float32([[1, 0, -50], [0, 1,-50]])
    - img_translation = cv2.warpAffine(image, T, (width//2, height//2))
11. Rotation: to scale & rotate at the same time
    - rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, .5) #.5 is the scaling factor, 90 is anti-clockwise rotation angle (now since canvas remain the same change of shape might cause other area to be cropped or black boundary)
    - rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    - To avoid that cropping or black areas issues, can use below for 90 degree thing:
        - cv2.transpose(img)
        - flipped = cv2.flip(image, 0) # for 180 degree rotation
12. Interpolation:
    - Interpolation is the method of constructing new data points within the range of discrete set of known data points
    - Different Algorithms:
        - INTER_NEAREST (**Fastest**) - a nearest-neighbor interpolation 
        - INTER_LINEAR (**Good for zooming and upscaling**) - a bilinear interpolation (used by default) 
        - INTER_AREA (**Good for shrinking and downsampling**) - resampling using pixel area relation. It may be a preferred method for image decimation, as it gives moire’-free results. But when the image is zoomed, it is similar to the INTER_NEAREST method. 
        - INTER_CUBIC (**BETTER**) - a bicubic interpolation over 4x4 pixel neighborhood 
        - INTER_LANCZOS4 (**BEST**) - a Lanczos interpolation over 8x8 pixel neighborhood
    - image_scaled = cv2.resize(image, None, fx=0.75, fy=0.75)
    - img_scaled = cv2.resize(image, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
    - img_scaled = cv2.resize(image, (900, 400), interpolation = cv2.INTER_AREA) 
    
         ![03_Interpolation.jpg](images/03_Interpolation.jpg)    
    
13. Image Pyramids:
    - smaller = cv2.pyrDown(image)
    - larger = cv2.pyrUp(smaller)
14. Edges Detection:
    -  Sobel
        - sobel_x = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
        - sobel_y = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
        - cv2.imshow('Sobel X', sobel_x)
        - cv2.imshow('Sobel Y', sobel_y)
        - sobel_OR = cv2.bitwise_or(sobel_x, sobel_y)
        - cv2.imshow('sobel_OR', sobel_OR)
    - Laplacian:
        - laplacian = cv2.Laplacian(image, cv2.CV_64F)
        - cv2.imshow('Laplacian', laplacian)
    - Canny:
        - canny = cv2.Canny(image, 50, 120)
        - cv2.imshow('Canny', canny)
15. Getting Perspective:
    - Non-Affine:
        - -# Cordinates of the 4 corners of the original image
        - points_A = np.float32([[320,15], [700,215], [85,610], [530,780]])
        - -# Cordinates of the 4 corners of the desired output
        - -# We use a ratio of an A4 Paper 1 : 1.41
        - points_B = np.float32([[0,0], [420,0], [0,594], [420,594]])
        - M = cv2.getPerspectiveTransform(points_A, points_B)
        - warped = cv2.warpPerspective(image, M, (420,594))
        - cv2.imshow('warpPerspective', warped)
    - Affine:
        - points_A = np.float32([[320,15], [700,215], [85,610]])
        - points_B = np.float32([[0,0], [420,0], [0,594]])
        - M = cv2.getAffineTransform(points_A, points_B)
        - warped = cv2.warpAffine(image, M, (cols, rows))
        - cv2.imshow('warpAffine', warped)
16. Sketch from Web-cam, live:
    `# Our sketch generating function`<BR><BR>
    `def sketch(image):`<BR>
    `    # Convert image to grayscale`<BR>
    `    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)`<BR>
    `    # Clean up image using Guassian Blur`<BR>
    `    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)`<BR>
    `    # Extract edges`<BR>
    `    canny_edges = cv2.Canny(img_gray_blur, 10, 70)`<BR>
    `    # Do an invert binarize the image`<BR> 
    `    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)`<BR>
    `    return mask`<BR>
<BR>    
    `cap = cv2.VideoCapture(0)`<BR>
<BR>
    `while True:`<BR>
    `    ret, frame = cap.read()`<BR>
    `    cv2.imshow('Our Live Sketcher', sketch(frame))`<BR>
    `    if cv2.waitKey(1) == 13: #13 is the Enter Key`<BR>
    `        break`<BR>
<BR>            
    `-# Release camera and close windows`<BR>
    `cap.release()`<BR>
    `cv2.destroyAllWindows()`<BR>
    
17. Contours: [More about contours - area, centroid, fitting circle or line etc](https://docs.opencv.org/3.4.2/dd/d49/tutorial_py_contour_features.html)
    -  Find & draw contours:
        - `gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)`    
        - `edged = cv2.Canny(gray, 30, 200)`    
        - `# Use a copy of your image e.g. edged.copy(), since findContours alters the image`    
        - `image, contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)`
            - 'hierarchy' describes the child-parent relationships between contours (i.e. contours within contours)
            - Approximation Methods (3rd Parameter):
                - cv2.CHAIN_APPROX_NONE: 
                    - stores all the boundary points. 
                    - But we don't necessarily need all bounding points. 
                    - If the points form a straight line, we only need the start and ending points of that line.
                - cv2.CHAIN_APPROX_SIMPLE: 
                    - instead only provides these start and end points of bounding contours.
                    - Thus resulting in much more efficent storage of contour information.
            - Retrieval Modes (Hierarchy Types): https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contours_hierarchy/py_contours_hierarchy.html#contours-hierarchy
                - cv2.RETR_LIST: Retrieves all contours
                - cv2.RETR_EXTERNAL: Retrieves external or outer contours only
                - cv2.RETR_CCOMP: Retrieves all in a 2-level hierarchy
                - cv2.RETR_TREE: Retrieves all in full hierarchy
                - cv2.RETR_FLOODFILL: 
        - `# Use '-1' as the 3rd parameter to draw all`    
        - `cv2.drawContours(image, contours, -1, (0,255,0), 3)` 
    
    - Sorting Contours:
        - By Area:
          ```python
              area = cv2.contourArea(contour_from_contour_list_we_get_from_findContours_method)
              
              #Sort contours large to small, above line is just to get area, but not required for below sorting
              sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
          ```
  
        - By spatial position (LEFT-to-RIGHT): **OPEN-CV left topmost point is 0,0**
          ```python
            def x_cord_contour(contours):
                #Returns the X cordinate for the contour centroid
                if cv2.contourArea(contours) > 10:
                    M = cv2.moments(contours)
                    return (int(M['m10']/M['m00']))
            
            
            def label_contour_center(image, c):
                # Places a red circle on the centers of contours
                M = cv2.moments(c)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                # Draw the countour number on the image
                cv2.circle(image,(cx,cy), 10, (0,0,255), -1)
                return image
            
            # Labeling Contours left to right
            for (i,c)  in enumerate(contours_left_to_right):
                cv2.drawContours(orginal_image, [c], -1, (0,0,255), 3)  
                M = cv2.moments(c)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                cv2.putText(orginal_image, str(i+1), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow('6 - Left to Right Contour', orginal_image)
                cv2.waitKey(0)
                (x, y, w, h) = cv2.boundingRect(c)
                # Let's now crop each contour and save these images
                cropped_contour = orginal_image[y:y + h, x:x + w]
                image_name = "output_shape_number_" + str(i+1) + ".jpg"
                print(image_name)
                # cv2.imwrite(image_name, cropped_contour)
                cv2.imshow(image_name, cropped_contour)
          ```
    - Approximate Contours + Convex Hull:-
        - **cv2.approxPolyDP(contour, Approximation Accuracy, Closed)**
            - **contour** – is the individual contour we wish to approximate
            - **Approximation Accuracy** – Important parameter is determining the accuracy of the approximation. Small values give precise-  approximations, large values give more generic approximation. A good rule of thumb is less than 5% of the contour perimeter
            - **Closed** – a Boolean value that states whether the approximate contour should be open or closed
        ```python
              _, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
              # Iterate through each contour and compute the approx contour
              for c in contours:
                  # Calculate accuracy as a percent of the contour perimeter
                  accuracy = 0.03 * cv2.arcLength(c, True)
                  approx = cv2.approxPolyDP(c, accuracy, True)
                  cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
                  cv2.imshow('Approx Poly DP', image)
        ```
        - **Convex Hull**:
        ```python
              _, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
              # Sort Contours by area and then remove the largest frame contour
              n = len(contours) - 1
              contours = sorted(contours, key=cv2.contourArea, reverse=False)[:n]
              # Iterate through contours and draw the convex hull
              for c in contours:
                  hull = cv2.convexHull(c)
                  cv2.drawContours(image, [hull], 0, (0, 255, 0), 2)
                  cv2.imshow('Convex Hull', image)
        ``` 
18. Shape Matching: (Shape can be identified by number of minimum points to remember contour or approxPolyDP)
    - **cv2.matchShapes(contour template, contour, method, method parameter)**
    - **Output** – match value (lower values means a closer match)
        - **Contour Template** – This is our reference contour that we’re trying to find in the new image
        - **Contour** – The individual contour we are checking against
        - **Method** – Type of contour matching (1, 2, 3) [More Details here](http://docs.opencv.org/2.4/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html)
        - **Method** Parameter – leave alone as 0.0 (not fully utilized in python OpenCV)
    ```python
            # Find contours in template
            _, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
            
            # We need to sort the contours by area so that we can remove the largest
            # contour which is the image outline
            sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
            
            # We extract the second largest contour which will be our template contour
            template_contour = contours[1]
            
            # Extract contours from second target image
            _, contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
            
            for c in contours:
                # Iterate through each contour in the target image and 
                # use cv2.matchShapes to compare contour shapes
                match = cv2.matchShapes(template_contour, c, 1, 0.0)
                print(match)
                # If the match value is less than 0.15 we
                if match < 0.15:
                    closest_contour = c
                else:
                    closest_contour = [] 
                            
            cv2.drawContours(target, [closest_contour], -1, (0,255,0), 3)
            cv2.imshow('Output', target)
    ```
19. Line Detection:
    - **cv2.HoughLines**(binarized/thresholded image, 𝜌 accuracy, 𝜃 accuracy, threshold)
        - Threshold here is the minimum vote for it to be considered a line
        ```python
                # Grayscale and Canny Edges extracted
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                edges = cv2.Canny(gray, 100, 170, apertureSize = 3)
                #cv2.imshow("Canny",edges)
                
                # Run HoughLines using a rho accuracy of 1 pixel
                # theta accuracy of np.pi / 180 which is 1 degree
                # Our line threshold is set to 240 (number of points on line)
                lines = cv2.HoughLines(edges, 1, np.pi / 180, 240)
                
                # We iterate through each line and convert it to the format
                # required by cv.lines (i.e. requiring end points)
                for rho, theta in lines[0]:
                    a = np.cos(theta)
                    b = np.sin(theta)
                    x0 = a * rho
                    y0 = b * rho
                    x1 = int(x0 + 1000 * (-b))
                    y1 = int(y0 + 1000 * (a))
                    x2 = int(x0 - 1000 * (-b))
                    y2 = int(y0 - 1000 * (a))
                    cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
                
                cv2.imshow('Hough Lines', image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
        ```
    - **cv2.HoughLinesP**(binarized image, 𝜌 accuracy, 𝜃 accuracy, threshold, minimum line length, max line gap)
        ```python
                # Grayscale and Canny Edges extracted
                image = cv2.imread('images/soduku.jpg')
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                edges = cv2.Canny(gray, 100, 170, apertureSize = 3)
                
                # Again we use the same rho and theta accuracies
                # However, we specific a minimum vote (pts along line) of 100
                # and Min line length of 5 pixels and max gap between lines of 10 pixels
                lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 200, 5, 10)
                print(lines.shape)
                
                for x1, y1, x2, y2 in lines[0]:
                    cv2.line(image, (x1, y1), (x2, y2),(0, 255, 0), 3)
                
                cv2.imshow('Probabilistic Hough Lines', image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
        ```
        
**Image Manipulation**:
1. **Transformations**:
    - Geometric distortions enacted upon an image
    - Used to correct distortions or perspective issues from arising from the point of view an image was captured.
    - Types (different categories of classification but we will talk about main):
        - Affine: Scaling, Rotation, Translation
        - Non-Affine: (Projective Transformation or Homography)
            - It doesn't preserve parallelism, length and angle. It does however preserve collinearity and incidence (two adjacent point will remain adjacent.)
            - Mainly because of different camera perspectives.
2. **Edge Detections**:
    - Very important especially when dealing with contours.
    - Edges can be defined as sudden changes (discontinuities) in an image and they can encode just as much information as pixels. These capture important information generally sufficient to identify an object but scenarios could be complex.
![04_EdgeDetection.jpg](images/04_EdgeDetection.jpg)    
    - Types of algorithms:
        - Sobel: to emphasize vertical or horizontal edges
        - Laplacian: Gets all orientations
        - Canny: Optimal due to low error rate, well defined edges and accurate detection.
    - Canny Algorithm:
        - Applies Gaussian blurring
        -  Finds intensity gradient of the image
        - Applied non-maximum suppression (i.e removes pixels that are not edges)
        - Hysteresis - Applies thresholds (i.e if pixel is within the upper and lower thresholds, it is considered an edge)
3. **Image Segmentation**
    - Partitioning images into different regions.
    - Different Techniques:
        - Contours: Are continuous lines or curves that bound or cover the full boundary of an object in an image.
            - Very important in : Object Detection, Shape Analysis
            - Open-CV's findContours require gray-scale image otherwise it will throw an error.
                - findContours doesn't require image to be passed to Canny Algorithm but if passed it will remove a lot of noise and hence let to easy processing (can help to reduce the number of unnecessary contours).
                - open-cv stores contours as a list of list. List contour1 stores all the points of one contour as a list for example.
            - **Sorting Contours**:
                - **Sorting by Area** can assist in Object Recognition (using contours area).
                    - Eliminate small contours that may be noise.
                    - Extract the largest contour
                - **Sorting by spatial position**: using the contours centroid
                    - Sort characters left to right.
                    - Process images in specific order.
                - It is usually a good technique to find contours and draw it on a blank white or black backgroud.
        - Line Detection
            
                ![05_LineDetection.jpg](05_LineDetection.jpg)
            - open-cv stores line as per above equation where 
                - p is the perpendicular distance from origin
                - theta is the angle formed by the normal of this line to the origin
            - Two types of algorithms:
                - Hough Lines: Threshold is the minimum vote to be considered a line
                - Probabilitic Hough Lines:
                    - Idea is that it takes only a random subset of points sufficient enough for line detection.
                    - Also returns the start and end points of the line unlike the previous function.
            
        - Circle Detection
        - Blob Detection:
            - Blobs can be described as groups of connected pixels that all share a common property.
            - Steps for open-cv:
                - Create Detector
                - Input image into Detector
                - Obtain key points
                - Draw key points
            ```python
                    # Read image
                    image = cv2.imread("images/Sunflowers.jpg")
                     
                    # Set up the detector with default parameters.
                    detector = cv2.SimpleBlobDetector_create()
                     
                    # Detect blobs.
                    keypoints = detector.detect(image)
                     
                    # Draw detected blobs as red circles.
                    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of
                    # the circle corresponds to the size of blob
                    blank = np.zeros((1,1)) 
                    blobs = cv2.drawKeypoints(image, keypoints, blank, (0,255,255),
                                                          cv2.DRAW_MATCHES_FLAGS_DEFAULT)
                     
                    # Show keypoints
                    cv2.imshow("Blobs", blobs)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
            ```
            
            - The function **cv2.drawKeypoints** takes the following arguments:
                - **cv2.drawKeypoints**(input image, keypoints, blank_output_array, color, flags)
                - flags:
                    - **cv2.DRAW_MATCHES_FLAGS_DEFAULT**
                    - **cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS**
                    - **cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG**
                    - **cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS**
                    
            - Detect ellipses:
            ```python
                      # Intialize the detector using the default parameters
                      detector = cv2.SimpleBlobDetector_create()
                         
                      # Detect blobs
                      keypoints = detector.detect(image)
                         
                      # Draw blobs on our image as red circles
                      blank = np.zeros((1,1)) 
                      blobs = cv2.drawKeypoints(image, keypoints, blank, (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            
                      number_of_blobs = len(keypoints)
                      text = "Total Number of Blobs: " + str(len(keypoints))
                      cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 0, 255), 2)
            
                      # Display image with blob keypoints
                      cv2.imshow("Blobs using default parameters", blobs)
                      cv2.waitKey(0)
            ```
            - Detect ellipses and circles separately:
            ```python
                        # Set our filtering parameters
                        # Initialize parameter settiing using cv2.SimpleBlobDetector
                        params = cv2.SimpleBlobDetector_Params()
                        
                        # Set Area filtering parameters
                        params.filterByArea = True
                        params.minArea = 100
                        
                        # Set Circularity filtering parameters
                        params.filterByCircularity = True 
                        params.minCircularity = 0.9
                        
                        # Set Convexity filtering parameters
                        params.filterByConvexity = False
                        params.minConvexity = 0.2
                            
                        # Set inertia filtering parameters
                        params.filterByInertia = True
                        params.minInertiaRatio = 0.01
                        
                        # Create a detector with the parameters
                        detector = cv2.SimpleBlobDetector_create(params)
                            
                        # Detect blobs
                        keypoints = detector.detect(image)
                        
                        # Draw blobs on our image as red circles
                        blank = np.zeros((1,1)) 
                        blobs = cv2.drawKeypoints(image, keypoints, blank, (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                        
                        number_of_blobs = len(keypoints)
                        text = "Number of Circular Blobs: " + str(len(keypoints))
                        cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)
            ```
            - Blob filtering shape & size: **cv2.SimpleBlobDetector_Params()**
                - Area: (to see all blobs having area in given range)
                    - params.filterByArea=True/False
                    - params.minArea = pixels
                    - params.maxArea = pixels
                - Circularity: ()
                    - params.filterByCircularity = True/False
                    - params.minCircularity = 1 being perfect circle, 0 the opposite
                - Convexity: (Area of blob **divide** Area of Convex Hull)
                    - params.filterByConvexity = True/False
                    - params.minConvexity= 0 to 1
                - Inertia: Measure of ellipticalness (low being more elliptical, high being more circular)
                    - params.filterByInertia = True/False
                    - params.minInertiaRatio = 0.01 (high means more circular)                

**Random**
1. Moments: [More About image-moments](http://www.aishack.in/tutorials/image-moments/)
    - If the **points** represent **mass**, 
        - then the zeroth moment is the total mass, 
        - the first moment divided by the total mass is the center of mass
        - the second moment is the rotational inertia. 
    - If the **points** represent **probability density**, 
        - then the zeroth moment is the total probability (i.e. one), 
        - the first moment is the mean, 
        - the second moment is the variance, 
        - the third moment is the skewness, and 
        - the fourth moment (with normalization and shift) is the kurtosis
    - Tells: Area, centroid, Orientation
    
2. Hu Moments: Invariant to translation, scale and rotation (orientation as well).        

 
    
