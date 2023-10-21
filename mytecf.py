import cv2
from mtcnn.mtcnn import MTCNN

# Inicializando o detector
detector = MTCNN()

# Abrindo o vídeo
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture(0)

while True:
    # Lendo o frame do vídeo
    ret, frame = cap.read()

    if ret:
        # Detectando rostos no frame
        faces = detector.detect_faces(frame)
        
        for face in faces:
            # Desenhando um retângulo ao redor do rosto detectado
            cv2.rectangle(frame, 
                          (face['box'][0], face['box'][1]), 
                          (face['box'][0]+face['box'][2], face['box'][1] + face['box'][3]), 
                          (255,0,0), 
                          2)

        # Exibindo o frame
        cv2.imshow('window', frame)
        
    # Saindo do loop se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberando o vídeo e fechando as janelas
cap.release()
cv2.destroyAllWindows()

# {
# 	'box': [422, 113, 76, 99], 
# 	'confidence': 0.7092751264572144, 
# 	'keypoints': {
# 		'left_eye': (443, 152), 
# 		'right_eye': (474, 151), 
# 		'nose': (453, 173), 
# 		'mouth_left': (445, 190), 
# 		'mouth_right': (472, 188)
# 	}
# }
