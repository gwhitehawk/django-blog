PIC_NUMBER = 10
PIC_PATH = "img"
USER_NAME = "gwhitehawk"

python FlickrBanner $PIC_NUMBER $PIC_PATH $USER_NAME
for ((i=0; i<$PIC_NUMBER; i++))
    do
        convert -geometry 200x200 $PIC_PATH/pic$i.jpg -background white -flatten -transparent white -thumbnail x200 -resize '200x<' -resize 50% -gravity center -crop 100x100+0+0 +repage $PIC_PATH/pic$i.jpg
    done

montage $PIC_PATH/pic[0-$PIC_NUMBER-1].jpg -tile x1 -geometry +5+5 $PIC_PATH/photoblog_banner.jpg
