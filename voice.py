# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#
# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(
#     IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = cast(interface, POINTER(IAudioEndpointVolume))
#
# # Control volume
# volume.SetMasterVolumeLevel(-0.0, None) #max
# # volume.SetMasterVolumeLevel(-5.0, None) #72%
# # volume.SetMasterVolumeLevel(-10.0, None)  # 51%
#
#
#
#
#
#
#
#
#
#
#
# import pygame
#
#
# # Initialize pygame mixer
# pygame.mixer.init()
#
# # # Set the volume to 100%
# # pygame.mixer.music.set_volume(1.0)  # 1.0 is the max volume (100%)
#
# import ctypes
#
# # Define the Windows API function for setting volume
# # sndvol32 = ctypes.WinDLL('winmm.dll')
# # sndvol32.waveOutSetVolume(0, 0xFFFF)
# #
# # # Now, when you play music with Pygame, it will be at the system's max volume
# # pygame.mixer.music.set_volume(1.0)
#
#
# # AudioSegment.from_mp3("jira-voice.mp3").export("jira-voice.wav", format="wav")
# # sound = pygame.mixer.Sound('jira-voice.wav')
#
# # Load the sound file
# # sound = pygame.mixer.Sound('D:/WorkArea2/Jira-report/JiraVoice.ogg')
# #
# # # Play the sound
# # sound.play()
# #
# # # Keep the program running until the sound is finished
# # pygame.time.wait(int(sound.get_length() * 1000))
#
# #
# # import simpleaudio as sa
# #
# # filename = 'D:/WorkArea2/Jira-report/JiraVoice.ogg'
# # wave_obj = sa.WaveObject.from_wave_file(filename)
# # play_obj = wave_obj.play()
# # play_obj.wait_done()  # Wait until sound has finished playing
#
# import pygame
#
# # Initialize pygame mixer
# pygame.mixer.init()
#
# # Load the MP3 file
# pygame.mixer.music.load('Mario.mp3')
#
# # Play the music
# pygame.mixer.music.play()
#
# # Wait for the music to finish playing
# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)
#


import pyglet

player = pyglet.media.Player()
source = pyglet.media.load('Mario.mp3', streaming=False)
player.queue(source)
player.play()
player.volume = 0.2
player.volume = 0.5