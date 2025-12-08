import cv2

def draw_rectangle(event,x,y,flags,param):
    global pt1,pt2,pt3,pt4,pt1_clicked,pt2_clicked,pt3_clicked,pt4_clicked,pt5_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        if pt1_clicked and pt2_clicked and pt3_clicked and pt4_clicked and pt5_clicked:
            pt1_clicked = False
            pt2_clicked = False
            pt3_clicked = False
            pt4_clicked = False
            pt1 = (0,0)
            pt2 = (0,0)
            pt3 = (0,0)
            pt4 = (0,0)
        if pt1_clicked == False:
            pt1 = (x,y)
            pt1_clicked = True
        elif pt2_clicked == False:
            pt2 = (x,y)
            pt2_clicked = True
        elif pt3_clicked == False:
            pt3 = (x,y)
            pt3_clicked = True
        elif pt4_clicked == False:
            pt4 = (x,y)
            pt4_clicked = True
        elif pt5_clicked == False:
            print('pt1 =',pt1)
            print('pt2 =',pt2)
            print('pt3 =',pt3)
            print('pt4 =',pt4)
            pt5_clicked = True

pt1 = (0,0)
pt2 = (0,0)
pt3 = (0,0)
pt4 = (0,0)
pt1_clicked = False
pt2_clicked = False
pt3_clicked = False
pt4_clicked = False
pt5_clicked = False

cap = cv2.VideoCapture(0) 
cv2.namedWindow('Test')
cv2.setMouseCallback('Test', draw_rectangle) 


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        if pt1_clicked:
            cv2.circle(frame, center=pt1, radius=5, color=(0,0,255), thickness=-1)
        if pt1_clicked and pt2_clicked:
            cv2.circle(frame, center=pt1, radius=5, color=(0,0,255), thickness=-1)
            cv2.circle(frame, center=pt2, radius=5, color=(0,0,255), thickness=-1)
        if pt1_clicked and pt2_clicked and pt3_clicked:
            cv2.circle(frame, center=pt1, radius=5, color=(0,0,255), thickness=-1)
            cv2.circle(frame, center=pt2, radius=5, color=(0,0,255), thickness=-1)
            cv2.circle(frame, center=pt3, radius=5, color=(0,0,255), thickness=-1)
        if pt1_clicked and pt2_clicked and pt3_clicked and pt4_clicked:
            cv2.circle(frame, center=pt1, radius=5, color=(0,0,255), thickness=-1)
            cv2.circle(frame, center=pt2, radius=5, color=(0,0,255), thickness=-1)
            cv2.circle(frame, center=pt3, radius=5, color=(0,0,255), thickness=-1)
            cv2.circle(frame, center=pt4, radius=5, color=(0,0,255), thickness=-1)
        cv2.imshow('Test', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
