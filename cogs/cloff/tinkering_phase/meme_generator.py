import cv2 as cv
path = "templates\\lisa.jpg"

cv.namedWindow("Processed", cv.WINDOW_AUTOSIZE)
image = cv.imread(path) 
font = cv.FONT_HERSHEY_SIMPLEX 

a,b = 150,200

org = (a,b) 
argument = 'fuck off'
fontScale = 1
color = (255, 0, 0) 
thickness = 2
img2 = cv.putText(image, argument, org, font, fontScale, color, thickness, cv.LINE_AA) 
cv.imshow("Processed", img2)

k = cv.waitKey(2000)
if k == ord('q'):
    cv.destroyAllWindows()

print(image.shape)