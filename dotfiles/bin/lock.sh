#!/bin/bash
IMAGE=/tmp/i3lock.png
SCREENSHOT="scrot $IMAGE" # 0.46s
$SCREENSHOT
convert $IMAGE -resize 10% $IMAGE
convert $IMAGE -resize 1000% $IMAGE
i3lock -i $IMAGE
rm $IMAGE
