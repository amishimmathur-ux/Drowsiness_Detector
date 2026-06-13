# Brief
The Drowsiness Detector is a CV based AI model which detects if the person siting behind the wheel is drowsy or not, and with respect to that, sounds an alarm to prompty wake them up.<br>
Sleep is a dynamic process which affects out body in various ways. Lack of sleep is terms as sleep deprivation and can cause severe damages to out body, and rather obviously, it is very harmful for individuals who drive.
<br>
Sleep deprivation, tiredness or fatigue when taking over the person incharge of the wheel can make them have small gusts of sleep called ‘Micro-Sleep Attacks’.
<br>
These sleep attacks last for a mere seconds but on the road can cause a huge problem in just that short instance in which it occurs.

# Problem
 How can we help general public like pedestrians, car drivers and late night truck delivery drivers find a way to be safe from micro-sleep attacks so that they can drive safely without the fear of sleeping in the middle of driving and potentially causing a fatal road accident risking their lives and others too.

# Solution 
The drowsiness detector makes use of different librearies to detect the sleepyness of a driver.<br>
-CV2 : Helps integrate AI into the camera.
-OS : Lets us load aur datasets into the code.
-Numpy - Handels the arrays and vectors formed by image dataset.
-Pygame - Triggers the alarm sound whenever the driver apears sleepy.
-Sklearn - Essential for making the actual prediction model.