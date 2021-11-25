import os
import tkinter.filedialog
import cv2 as cv

#My Module
import isDirNull

def movie_to_images(video_path = "", base_name = "", extension = 'jpg'):
	print("movie_to_images")
	file_type = [('動画ファイル', '*.mp4')]
	root = tkinter.Tk()
	while not video_path:
		print("画像化する動画を選んでください")
		video_path = tkinter.filedialog.askopenfilename(filetypes = file_type, initialdir = ".")
	root.destroy()
	raw_movie = cv.VideoCapture(video_path)
	if not raw_movie.isOpened():
		print("元動画を開くことができませんでした。")
		return
	result_folder_name = "RawImg"
	basename_without_extension = os.path.splitext(os.path.basename(video_path))[0]
	os.makedirs(f"./{result_folder_name}", exist_ok=True)
	os.makedirs(f"./{result_folder_name}/{basename_without_extension}", exist_ok=True)

	total_frames_digit = len(str(int(raw_movie.get(cv.CAP_PROP_FRAME_COUNT))))

	print("画像化する動画：", video_path)
	print("画像出力先：", f"./{result_folder_name}/{basename_without_extension}")
	
	isDirNull.result_output_folder(f"./{result_folder_name}/{basename_without_extension}/")

	n = 0
	while True:
		ret, frame = raw_movie.read()
		if ret:
			cv.imwrite(f"./{result_folder_name}/{basename_without_extension}/{str(n).zfill(total_frames_digit)}.{extension}", frame)
			n += 1
		else:
			break
	return video_path


if __name__ == '__main__':
	movie_to_images("")

