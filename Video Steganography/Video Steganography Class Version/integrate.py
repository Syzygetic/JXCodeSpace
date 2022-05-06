from videoSteganography import VideoCoder

#Video Encoder
video = VideoCoder()
source_file = "./cover_assets/coverWaterfall.mp4"
embedded_file = "./encoded_assets/stegoVideo.avi"
decoded_text = "./encoded_assets/decoded_video.txt"
bitRange = 3
payload = "Enter your payload here"
video.encode_video(source_file, payload, bitRange)
video.decode_video(embedded_file, decoded_text, bitRange)