import cv2
import numpy as np
import sys

class Node(object):
	def __init__(self, top=None, bottom=None, nxt=None, parent=None, value=None, label='X'):
		self.top = top
		self.bottom = bottom
		self.nxt = nxt
		self.label = label
		self.parent = parent
		self.value = value

def printTree(start):
	if start is None:
		return
	print start.value
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

# Find the contours
_,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=lambda cont: cv2.boundingRect(cont)[0])

X_cord = []
Y_cord = []
W_cord = []
H_cord = []
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

# process subscripts, superscripts
start = Node(value=0)
prev_node = start
for i in xrange(1, len(X_cord)):
	l_avg = (Y_cord[i-1] + (H_cord[i-1]/2))
	print l_avg, 'lavg'
	r_bot = Y_cord[i]
	print r_bot, 'r_bot'
	r_top = r_bot + H_cord[i]
	print r_top, 'rtop'
	new_node = Node(value=i)
	if l_avg < r_bot:
		print 'holo 1'
		prnt = prev_node.parent
		if prnt is not None:
			parent_avg = (Y_cord[prnt.value] + H_cord[prnt.value]/2)
		else:
			parent_avg = r_top + 1	# just shit to make it to go to superscript

		# back to parent
		if parent_avg < r_top:
			prnt.nxt = new_node
			new_node.parent = prnt.parent
			prev_node = new_node
		else:
			# superscript in subscript!!!
			prev_node.top = new_node
			new_node.parent = prev_node
			prev_node = new_node
	elif l_avg > r_top:
		print 'holo 2'
		prnt = prev_node.parent
		if prnt is not None:
			parent_avg = (Y_cord[prnt.value] + H_cord[prnt.value]/2)
		else:
			parent_avg = r_bot - 1	# just shit to make it to go to subscript

		# back to parent
		if parent_avg > r_bot:
			prnt.nxt = new_node
			new_node.parent = prnt.parent
			prev_node = new_node
		else:
			# subscript in superscript!!!
			prev_node.bottom = new_node
			new_node.parent = prev_node
			prev_node = new_node
	else:
		print 'holo 3'
		prev_node.nxt = new_node
		new_node.parent = prev_node.parent
		prev_node = new_node

printTree(start)

# Finally show the image
cv2.imshow('img',img)
# cv2.imshow('res',thresh_color)
cv2.waitKey()
# sys.exit(1)
                                           
# cv2.destroyAllWindows()