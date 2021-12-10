import ffmpeg
folder='/content/gdrive/MyDrive/Capstone'
openpose_video='/content/gdrive/MyDrive/Capstone/Red_0.avi'
probe = ffmpeg.probe(openpose_video)
time = float(probe['streams'][0]['duration'])
width = probe['streams'][0]['width']
parts = 16
intervals = time /parts
interval_list = [(j * intervals, (j + 1) * intervals) for j in range(parts)]

j=0
for item in interval_list:
  (
    ffmpeg
    .input(openpose_video, ss=item[1])
    .filter('scale', width, -1)
    .output(folder+'/'+'Frames'+'/'+'Red'+'_'+str(j)+'.jpg', vframes=1)
    .run()
  )
  j+= 1
