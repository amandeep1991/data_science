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
    
    


**Image Manipulation**:
1. Transformations:
    - Geometric distortions enacted upon an image
    - Used to correct distortions or perspective issues from arising from the point of view an image was captured.
    - Types (different categories of classification but we will talk about main):
        - Affine: Scaling, Rotation, Translation
        - Non-Affine: (Projective Transformation or Homography)
            - It doesn't preserve parallelism, length and angle. It does however preserve collinearity and incidence (two adjacent point will remain adjacent.)
            - Mainly because of different camera perspectives.
2. Edge Detections:
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
        
        

 
    
