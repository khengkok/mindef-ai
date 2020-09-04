from PIL import Image
import glob
import matplotlib.pyplot as plt
import math
import os
import zipfile
import wget
import tensorflow as tf

dataset_root_dir = 'UCSD_Anomaly_Dataset.v1p2'

def create_gif(image_folder, output_file, img_type='png',):
    # Create the frames
    frames = []

    # files need to be sorted from 1...n so that the video is played in correct sequence
    imgs = sorted(glob.glob(f'{image_folder}/*.{img_type}'))
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)
    
    # Save into a GIF file that loops forever
    frames[0].save(output_file, format='gif',
                append_images=frames[1:],
                save_all=True,
                duration=120, loop=0)

def plot_image(image):
    '''if image is a file, then open the file first'''
    if type(image) == str:
        image = Image.open(image)
    elif type(image) == tf.python.framework.ops.EagerTensor:
        if len(image.shape) == 4:  # the tensor with batch axis
            image =  image[0][:,:,0]
        else:
            image = image[:,:,0]

    plt.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
    plt.axis("off")
    
    
def display_images(image_folder, image_range=(1,10), max_per_row=5):
    start, end = image_range
    num_images = end - start
    images = []
    for i in range(start, end):
        images.append(os.path.join(image_folder, '{:03d}.tif'.format(i)))

    nrows = math.ceil(num_images/max_per_row)
    fig = plt.figure(figsize=(max_per_row * 3, nrows * 2))
    for index, image in enumerate(images):
        plt.subplot(nrows, max_per_row, 1 + index)
        plot_image(image)
    #fig.save('fig.png')
    plt.show()

def download_data(url, extract=True, force=False):
    # if not force download and directory already exists
    if not force and os.path.exists(dataset_root_dir):
        print('dataset directory already exists, skip download')
        return

    filename = wget.download(url)
    print(filename)
    if extract: 
        with zipfile.ZipFile(filename, 'r') as zip:
            zip.extractall('.')

if __name__ == '__main__':
    
    image_folder = r'C:\Users\kheng\.keras\datasets\UCSD_Anomaly_Dataset.v1p2\UCSDped1\Test\Test024'
    #create_gif(image_folder, 'mygif.gif', img_type='tif')

    # images = []
    # for i in range(10):
    #     images.append(os.path.join(image_folder, '{:03d}.tif'.format(i+1)))
    
    # print(images)
    image_folder = os.path.join(dataset_root_dir, 'UCSDped1', 'Train', 'Train001')
    display_images(image_folder,image_range=(1,6), max_per_row=5)

    # url = 'https://sdaaidata.s3-ap-southeast-1.amazonaws.com/UCSD_Anomaly_Dataset.v1p2.zip'

    # download(url, extract=True)