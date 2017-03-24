import os, sys
from PIL import Image

def resize_images(imageFolder):

    for root, dirs, files in os.walk(imageFolder):
        for file_name in files:
            pathname = os.path.join(root, file_name)
            try:
                img = Image.open(pathname)
                width, height = img.size
                sized_image = img.resize((int(width / 2), int(height / 2)))
                output_files = os.path.join(root, 'resized_' + file_name)
                sized_image.save(output_files)
            except IOError: #oops, not an image
                print u'File {} can not be processed!'.format(file_name)

if __name__ == "__main__":
    imageFolder = sys.argv[1] # first arg is path to image folder
    resize_images(imageFolder)



# def delete_resize_images(imageFolder):
#     for root, dirs, files in os.walk(imageFolder):
#         for file_name in files:
#             try:
#                 print u'The file {} was deleted'.format(root ,'resized_' + file_name)
#                 os.remove('resized_' + file_name)
#             except OSError:
#                 pass


    # imageFolder = sys.argv[1] # second arg is path to delete resized images
    # delete_resize_images(imageFolder)


    #allowedExtensions = ("jpg")
    #if file_name.endswith(allowedExtensions):

    # resizeFactor=float(sys.argv[2])/100.0# 2nd is resize in %
    # bulkResize(imageFolder, resizeFactor)


    # jpegfiles = [os.path.join(x)
    #         for d, dirs, files in os.walk(spath)'resized_'
    #         for x in files if x.endswith(".jpg")]
    #
    # print jpegfiles


    # #Only the roots
    # roots = next(os.walk(spath))[0]
    # print u'Roots = {}'.format(roots)
    #
    # #Only the dirs
    # dirs = next(os.walk(spath))[1]
    # print u'Dirs = {}'.format(dirs)
    #
    # #Only the files
    # files = next(os.walk(spath))[2]
    # print u'Fles = {}'.format(files)


    # for items in fnmatch.filter(files, "*.jpg"):
    #             print "..." + items

