import Image, ImageEnhance

def main():  #{

    filename ='BMP.jpg'
    image = Image.open( filename );
    size = width, height = image.size;

    #RGBA
    color_to_find = ( 0, 0, 0, 0 );
    color_to_replace = ( 255, 255 ,255 ,255 );

    rotated_image = image.rotate( 45, expand=True, resample=Image.BILINEAR )

    new_image_data = [];
    for color in list( rotated_image.getdata() ): #{
        if ( color == color_to_find ): #{
            new_image_data += [color_to_replace];
        #}
        else: #{
            new_image_data += [ color ];
        #}
    #}

    rotated_image.putdata(new_image_data)
    rotated_image.save( 'modified_rotate_' + filename)


    del  image, rotated_image;
#}
if ( __name__ == '__main__'):
    main()