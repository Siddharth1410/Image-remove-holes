import sys
#Siddharth Vadgama
#UTA ID-1001397508
def remove_holes(image):
	im = Image.open(image)

	if 'gif' in image:
		Image.open(image).convert('RGB').save('prev.jpg')

	image = 'prev.jpg'

	input_image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

	im_out=remove_holes_helper(input_image)

	cv2.imwrite("holes.jpg", im_out)
	return im_out
	#cv2.waitKey(0)

def remove_holes_helper(input_image):
	
	
	th, image_threshold = cv2.threshold(input_image, 35, 255, cv2.THRESH_BINARY)
	
	height, width = image_threshold.shape[:2]

	mask = np.zeros((height+2, width+2), np.uint8)

	cv2.imwrite("abcd.jpg",image_threshold)

	image_fill = image_threshold.copy()
		
	

	cv2.floodFill(image_fill, mask, (0,0), 255);

	im_fill_inv = cv2.bitwise_not(image_fill)

	im_out = image_threshold | im_fill_inv

	return im_out
