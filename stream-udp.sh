gst-launch-1.0 -e rpicamsrc vflip=true hflip=true bitrate=5000000 do-timestamp=true preview=false  ! 'video/x-h264,width=1024,height=768,framerate=30/1' ! h264parse ! rtph264pay config-interval=1 pt=96 ! udpsink host=192.168.0.7 port=9000 sync=false async=true

