import cv2
import face_recognition
import numpy as np
import os

DATA_FILE = 'face_data.npy' #varibale storing where face data is saved


def capture_face_encoding(prompt="Look at the camera and press 'SPACE' to capture your face"):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None
    
    print(prompt)
    encoding = None
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("FACE ID - Press 'SPACE' to capture, ESC to cancel", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC key to exit
            break
        if key == 32:  # SPACE key to capture
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            locations = face_recognition.face_locations(rgb_frame)
            encodings = face_recognition.face_encodings(rgb_frame, locations)
            
            if len(encodings) == 0:
                print("No face detected. Try again with better lighting.")
            elif len(encodings) > 1:
                print("Multiple faces detected. Try again with only one face in frame.")
            else:
                encoding = encodings[0]
                print("Face captured.")
                break

    cap.release()
    cv2.destroyAllWindows()
    return encoding


def enroll_user():
    user_face_encoding = capture_face_encoding("Enroll: Look at the camera and press 'SPACE' to capture your face")
    if user_face_encoding is None:
        print("Enrollment cancelled.")
        return
    
    np.save(DATA_FILE, user_face_encoding)
    print(f"Enrollment successful. Face data saved to {DATA_FILE}.")


def sign_in_with_face_id(tolerance=0.50):
    if not os.path.exists(DATA_FILE):
        print("No enrolled face data found. Please enroll first.")
        return
    
    stored_encoding = np.load(DATA_FILE)
    
    live_encoding = capture_face_encoding("Sign In: Look at the camera and press 'SPACE' to capture your face")
    if live_encoding is None:
        print("Sign-in cancelled.")
        return
    
    distance = face_recognition.face_distance([stored_encoding], live_encoding)[0]
    is_match = distance <= tolerance
    
    if is_match:
        print("Face ID verified. Sign-in successful.")
    else:
        print("Face ID verification failed. Sign-in unsuccessful.")
        
    print(f"(match score distance: {distance:.3f} (Tolerance: {tolerance})")


def main():
    while True:
        print('\n--- Face ID Sign-In APP ---')
        print('1. Enroll User')
        print('2. Sign In with Face ID')
        print('3. Exit')
        
        choice = input("Select an option (1-3): ").strip()
        if choice == '1':
            enroll_user()
        elif choice == '2':
            sign_in_with_face_id()
        elif choice == '3':
            print("Exiting Face ID APP. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
