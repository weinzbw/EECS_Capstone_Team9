"""
Program Name: onboard_microphone.py
Description: Sets up the speakers to play a sample audio. This file will be modified to work with the microphone on the PYNQ board
Programmer(s): Ben Weinzirl
Date Made: 3/02/2025
Date(s) Revised:
Preconditions: 
Postconditions: 
Errors/Exceptions:
Side Effects:
Invariants: 
Known Faults:
"""

from pynq.overlays.base import BaseOverlay
base = BaseOverlay("base.bit")
pAudio = base.audio

# Not sure if this does anything yet
pAudio.load("/home/xilinx/pynq/lib/tests/pynq_welcome.pdm")
pAudio.play()
