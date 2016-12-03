raspivid -o - -t 0 -n -w 1080 -h 720 -fps 24 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/tank}' :demux=h264

