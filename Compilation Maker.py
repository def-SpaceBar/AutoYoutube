import os
import random
import shutil
from moviepy.editor import VideoFileClip, concatenate_videoclips
from PIL import Image

# MAIN PATHS #
bank_path = 'Z:\\AutoCASH\\bank\\'
burned_path = 'Z:\\AutoCASH\\burned\\'
ready_path = 'Z:\\AutoCASH\\ready\\'
thumbnails_bank = 'Z:\\TikTube Project\\asmr\\Qoob Clips\\'
# LISTING, COUNTING AND SELECTING 14 RANDOM CLIPS CLIPS #
bank_list = os.listdir(bank_path)
print(bank_list)
bank_list_count = len(bank_list)
print(bank_list_count)
cuts = random.sample(bank_list, 15)
print(cuts)
# MAKING FOLDERS ACCORDING TO THE VIDEO NUMBER #
ready_video_count = input('Video number? (check b4 answering in burned or ready folders): ')
    # Making full paths and making the folders #
ready_video_folder_path = os.path.join(ready_path, ready_video_count)
burned_parts_folder_path = os.path.join(burned_path, ready_video_count)
print(burned_parts_folder_path)
        # Creating the folders #
os.makedirs(ready_video_folder_path)
os.makedirs(burned_parts_folder_path)
# Moving the files b4 creation. #
def burn_files(x,y):
    for i in x:
        src = bank_path+i
        shutil.move(src, y)
burn_files(cuts, burned_parts_folder_path)
# Combining the clips
def combine_clips(x, y,z):
    clips = []
    for filename in os.listdir(x):
        if filename.endswith(".mp4"):
            clips.append(filename)
    print(clips)
    os.chdir(x)
    clip01 = VideoFileClip(clips[0])
    clip02 = VideoFileClip(clips[1])
    clip03 = VideoFileClip(clips[2])
    clip04 = VideoFileClip(clips[3])
    clip05 = VideoFileClip(clips[4])
    clip06 = VideoFileClip(clips[5])
    clip07 = VideoFileClip(clips[6])
    clip08 = VideoFileClip(clips[7])
    clip09 = VideoFileClip(clips[8])
    clip10 = VideoFileClip(clips[9])
    clip11 = VideoFileClip(clips[10])
    clip12 = VideoFileClip(clips[11])
    clip13 = VideoFileClip(clips[12])
    clip14 = VideoFileClip(clips[13])
    clip15 = VideoFileClip(clips[14])
    combined = concatenate_videoclips([clip01, clip02, clip03,clip04, clip05, clip06, clip07, clip08, clip09, clip10, clip11, clip12,clip13,clip14,clip15], method='compose')
    combined.write_videofile(f'ASMR Tiktok Compilation {y}.mp4')
    with open(f'{z}creators.txt','w+') as creators:
        for i in clips:
            users = i.split('_1')
            creators.write(f'@{users[0]} -- https://www.tiktok.com/@{users[0]}\n')
    creators.close()

combine_clips(burned_parts_folder_path, ready_video_count, ready_video_folder_path)

# Moving the edited video to his sub-folder in 'ready' according to the compilation number #
#file_to_move = f'Satisfying ASMR Tiktoks Compilation {ready_video_count}.mp4'
def move_to_ready(x, x1, y):
    file_to_move = f'\\ASMR Tiktok Compilation {x1}.mp4'
    src = x+file_to_move
    shutil.move(src, y)
move_to_ready(burned_parts_folder_path, ready_video_count, ready_video_folder_path)

# Getting the thumbnails #
def thumbnail_grabber(z,x,t_b):
    thumbnails = []
    os.makedirs(f'{z}\\thumbnails')
    for filename in os.listdir(x):
        if filename.endswith(".mp4"):
            j = filename.split('.mp4')
            z1 = f'{j[0]}_cover.jpeg'
            thumbnails.append(z1)
    for i in thumbnails:
        split = i.split('_1')
        src = f'{t_b}{split[0]}\\cover\\{i}'
        shutil.move(src, f'{z}\\thumbnails')
thumbnail_grabber(ready_video_folder_path, burned_parts_folder_path, thumbnails_bank)

# Z:\AutoCASH\ready\1\thumbnails
# Takes 3 random thumbnails and combine them + add watermark. #
def thumbnail_editor(path):
    os.chdir(path)
    thumbnails = os.listdir(path)
    thumbnails_sample = random.sample(thumbnails, 3)
    images = [Image.open(x) for x in thumbnails_sample]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    new_im.save(f'{path}\\done.jpeg')
thumbnail_editor(f'{ready_video_folder_path}\\thumbnails')
