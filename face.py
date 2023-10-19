import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y , w ,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey ,ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 5)

    # Display the output
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

'''


class new:
    def __init__(self, data):
        self.data = data 
        self.left = self.right = None

def longestConsecutiveUtil(root, curLength, 
                           expected, res):
    if (root == None):
        return

    
    if (root.data == expected): 
        curLength += 1
    else:
        curLength = 1

    res[0] = max(res[0], curLength)

    
    longestConsecutiveUtil(root.left, curLength, 
                           root.data + 1, res) 
    longestConsecutiveUtil(root.right, curLength,
                           root.data + 1, res)


def longestConsecutive(root):
    if (root == None): 
        return 0

    res = [0]

    longestConsecutiveUtil(root, 0, root.data, res) 

    return res[0]


if __name__ == '__main__':

    root = new(6) 
    root.right = new(9) 
    root.right.left = new(7) 
    root.right.right = new(10) 
    root.right.right.right = new(11) 

    print(longestConsecutive(root))'''
