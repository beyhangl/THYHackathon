def lets_checkin():
	import glob
	import os
	import cv2
	list_of_files = glob.glob('images/*') # * means all if need specific format then *.csv
	latest_file = max(list_of_files, key=os.path.getctime)
	import face_recognition
	for i in range(1,4):
		try:
			print('11111')
			known_image = face_recognition.load_image_file('/home/kafein/thy_hackathon/bilinen_isimler/' + str(i)+'.jpg')
			print(str(latest_file))
			unknown_image = face_recognition.load_image_file('/home/kafein/thy_hackathon/'+str(latest_file))

			biden_encoding = face_recognition.face_encodings(known_image)[0]

			unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

			results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
			if results[0] == True:
			 print(i)
			 path = '/home/kafein/thy_hackathon/check-in'
			 if i==1:
		
				 cv2.imwrite(os.path.join(path , 'Beyhan.Gul_20875332358_TK506_18C'+'.jpg'), unknown_image)
				 cv2.waitKey(0)
			 if i==3:
				 cv2.imwrite(os.path.join(path , 'Muhammed.Demirci_21548852878_TK201_11A'+'.jpg'), unknown_image)
				 cv2.waitKey(0)
			 if i ==2:
				 cv2.imwrite(os.path.join(path , 'Guldudu.Firtina_2456569852578_TK201_11A'+'.jpg'), unknown_image)
				 cv2.waitKey(0)
		except:
		  pass
