import cv2

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	if ret == False: break
	print('frame.shape=', frame.shape)
	anchoMitad = frame.shape[1] // 2
	frame[:,:anchoMitad] = cv2.flip(frame[:,anchoMitad:],1)
	cv2.imshow('Frame',frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()