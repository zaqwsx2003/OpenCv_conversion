import cv, cv2

fn = 'on.jpg'

im_gray = cv2.imread(fn, cv.CV_LOAD_IMAGE_GRAYSCALE)
im_gray_mat = cv.fromarray(im_gray)
im_bw = cv.CreateImage(cv.GetSize(im_gray_mat), cv.IPL_DEPTH_8U, 1);
im_bw_mat = cv.GetMat(im_bw)

threshold = 0 

cv.Threshold(im_gray_mat, im_bw_mat, threshold, 255, cv.CV_THRESH_BINARY | cv.CV_THRESH_OTSU);
cv2.imshow('', np.asarray(im_bw_mat))
cv2.waitKey()