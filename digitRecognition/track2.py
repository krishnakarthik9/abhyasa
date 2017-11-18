import cv2
import numpy as np
import sys

class Node(object):
	def __init__(self, top=None, bottom=None, nxt=None, parent=None, value=None, label=None):
		self.top = top
		self.bottom = bottom
		self.nxt = nxt
		self.label = label
		self.parent = parent
		self.value = value

def printTree(start):
	if start is None:
		return
	print start.label
	if start.bottom is not None:
		print '_{'
		printTree(start.bottom)
		print '}'
	if start.top is not None:
		print '^{'
		printTree(start.top)
		print '}'
	printTree(start.nxt)

# Load the image
img = cv2.imread(sys.argv[1])

# convert to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# smooth the image to avoid noises
gray = cv2.medianBlur(gray,5)


# Apply adaptive threshold
thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)
thresh_color = cv2.cvtColor(thresh,cv2.COLOR_GRAY2BGR)

# apply some dilation and erosion to join the gaps
thresh = cv2.dilate(thresh,None,iterations = 3)
thresh = cv2.erode(thresh,None,iterations = 2)

# im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# im_gray = cv2.GaussianBlur(im_gray, (5, 5), 0)

# # Threshold the image
# ret, im_th = cv2.threshold(im_gray, 90, 255, cv2.THRESH_BINARY_INV)

# Find the contours
_,contours,hierarchy = cv2.findContours(im_th,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=lambda cont: cv2.boundingRect(cont)[0])

X_cord = []
Y_cord = []
W_cord = []
H_cord = []
labels = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
# For each contour, find the bounding rectangle and draw it
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    # print x;
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    # get labels of this rectangle
    X_cord.append(x)
    Y_cord.append(-(y+h))
    W_cord.append(w)
    H_cord.append(h)

    # cv2.rectangle(thresh_color,(x,y),(x+w,y+h),(0,255,0),2)

print X_cord
print Y_cord
print W_cord
print H_cord

# count  = 0

# process subscripts, superscripts
start = Node(value=0,label=labels[0])
parent_avg = (Y_cord[0] + (H_cord[0]/2))
prev_node = start
# for i in xrange(1, len(X_cord)):

def shitfun(prev_node,curr_node,count):
	# count = count +1
	l_avg = (Y_cord[prev_node.value] + (H_cord[prev_node.value]/2))
	l_bot = Y_cord[prev_node.value]
	l_top = l_bot + H_cord[prev_node.value]
	r_bot = Y_cord[curr_node.value]
	r_top = r_bot + H_cord[curr_node.value]
	prnt = prev_node.parent
	if prnt is None:
		print "count is ",count,"Inside None"
		if l_avg < r_bot:
				# Go to TOP of L 
			print "count is ",count,"Inside None 1"
			prev_node.top = curr_node
			curr_node.parent = prev_node
			prev_node = curr_node
		elif l_avg > r_top:
			# Go to BOT Of L
			print "count is ",count,"Inside None 2" 
			prev_node.bottom = curr_node
			curr_node.parent = prev_node
			prev_node = curr_node
		else:
			# GO to Next of L 
			print "count is ",count,"Inside None 3"
			prev_node.nxt = curr_node
			curr_node.parent = prev_node.parent
			prev_node = curr_node
		return prev_node
	else:
		parent_avg = (Y_cord[prnt.value] + (H_cord[prnt.value]/2))
		if parent_avg < l_bot:
			print "count is ",count,"Inside Parent in down"
			if r_bot > parent_avg:
				if r_bot > l_avg and r_bot < l_top:
					#  Go to TOP of L
					print "TOP"
					prev_node.top = curr_node
					curr_node.parent = prev_node
					prev_node = curr_node

				elif r_top < l_avg: 
					# Go to Bottom  of L
					print "Bottom"
					prev_node.bottom = curr_node
					curr_node.parent = prev_node
					prev_node = curr_node
				elif r_top > l_avg:
					# Go to next of L
					print "Next"
					prev_node.nxt = curr_node
					curr_node.parent = prev_node.parent
					prev_node = curr_node
				else:
					return shitfun(prev_node.parent,curr_node,count)
					
			else:
				return shitfun(prev_node.parent,curr_node,count)
			return prev_node
		elif parent_avg > l_top:
			print "count is ",count,"Inside Parent is UP"
			if r_top < parent_avg:
				if r_top > l_bot and r_top < l_avg:
					# Go to BOTTOM of L
					print "Bottom" 
					prev_node.bottom = curr_node
					curr_node.parent = prev_node
					prev_node = curr_node
				elif r_bot > l_avg:
					# Go to TOP of L
					print "Top" 
					prev_node.top = curr_node
					curr_node.parent = prev_node
					prev_node = curr_node
				elif r_bot < l_avg:
					#  Go to Next of L
					print "Next"
					prev_node.nxt = curr_node
					curr_node.parent = prev_node.parent
					prev_node = curr_node 
				else:
					return shitfun(prev_node.parent,curr_node,count)
			else:
				return shitfun(prev_node.parent,curr_node,count)
			return prev_node
cv2.imshow('img',img)
# cv2.imshow('res',thresh_color)
cv2.waitKey()

for i in xrange(1,len(X_cord)):
	curr_node = Node(value=i,label=labels[i])
	prev_node = shitfun(prev_node,curr_node,i)
	print "_L-------------------",prev_node.label
printTree(start)
# Finally show the image
# sys.exit(1)
                                           
# cv2.destroyAllWindows()