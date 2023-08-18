import speech_recognition as sr
from moviepy.editor import *
import os, shutil

def clip_audio(audio_file, clipped_audio_file, start_time, end_time):
    clip = AudioFileClip(audio_file)
    
    if end_time is None:
        end_time = clip.duration
    
    clip = clip.subclip(start_time, end_time)
    clip.write_audiofile(clipped_audio_file)
    clip.close()

def clip_video(video_file, clipped_video_file, start_time, end_time):
    clip = VideoFileClip(video_file)

    if end_time is None:
        end_time = clip.duration

    clip = clip.subclip(start_time, end_time)
    clip.write_videofile(clipped_video_file)
    clip.close()
    
def covert_video_to_audio(video_file, audio_file):
    try:
        videoclip = VideoFileClip(video_file)

        audioclip = videoclip.audio
        audioclip.write_audiofile(audio_file, codec='pcm_s16le')
    except Exception as e:
        print("exception in converting video to audio")
    finally:
        audioclip.close()
        videoclip.close()

def transcript_audio_to_txt(audio_file, text_file):
    clip = AudioFileClip(audio_file)
    end_time = clip.duration
    
    gap = 50
    
    s_r = sr.Recognizer()
    sr_audio = sr.AudioFile(audio_file)
    
    start = 0
    end = gap
    while end < end_time:
        f = open(text_file, "a")
        with sr_audio as source:
            try:
                audio = s_r.record(source, duration=end, offset=start)
                f.write(s_r.recognize_google(audio, language="en-UK"))
                f.write("\n")
            except Exception as e:
                f.write("\nThis " + str(gap) + " sec content got some error.\n")
                print(e)
            
        start = end
        end = end + gap
        f.close()

def main():
    video_file = input("Enter the path of video you want to transcribe : ") or r"D:\\Study\\Kubernetes Tutorial for Beginners [FULL COURSE in 4 Hours].mp4"
    clipped_video_file = 'clipped_video.mp4'

    audio_file  = 'audio.wav'
    clipped_audio_file = 'clipped_audio.wav'

    text_file   = 'final_text.txt'
    transcript_dir = "D:\\Transcript"

    if os.path.exists(transcript_dir):
        shutil.rmtree(transcript_dir, ignore_errors=True)
    os.mkdir(transcript_dir)
    os.chdir(transcript_dir)

    start_time = 0
    trim = False
    while True:
        response = input("Do you want to trim video (Yes/No) : ")
        if "Yes" in response:
            start_time = input("Enter start time in seconds (default is 0): ") or 0
            end_time = input("Enter end time in seconds (default is end time of video) : ") or None
            
            if (start_time != 0 or end_time is not None):
                trim = True
            break
        elif "No" in response:
            break
        else:
            print("Invalid response. Try again")
    
    covert_video_to_audio(video_file, audio_file)
    
    if trim:
        clip_audio(audio_file, clipped_audio_file, start_time, end_time)

    if os.path.exists(clipped_audio_file):
        transcript_audio_to_txt(clipped_audio_file, text_file)
    else:
        transcript_audio_to_txt(audio_file, text_file)


if __name__ == '__main__':
    main()