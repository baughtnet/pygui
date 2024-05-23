import cv2
import os
from PIL import Image

def images_to_video(image_folder, output_video, frame_rate=30):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith(".jpg")]
    images.sort()

    if not images:
        print("No images found in the specified folder.")
        return

    first_image_path = os.path.join(image_folder, images[0])
    first_image = Image.open(first_image_path)
    width, height = first_image.size

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_video, fourcc, frame_rate, (width, height))

    for image in images:
        img_path = os.path.join(image_folder, image)
        img = cv2.imread(img_path)

        if img is None:
            print(f"Error reading image {img_path}. Skipping.")
            continue

        if (img.shape[1], img.shape[0]) != (width, height):
            img = cv2.resize(img, (width, height))

        video_writer.write(img)

    video_writer.release()

if __name__ == "__main__":
    image_folder = "c:\\tmp\\fix"
    output_video = "c:\\tmp\\fixed.mkv"
    frame_rate = 30

    images_to_video(image_folder, output_video, frame_rate)
    print(f"Video saved as {output_video}")
