import serial
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from collections import deque

ser = serial.Serial('COM3', 9600, timeout=1)  # Replace COM3 with your port

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xdata, ydata, zdata = deque(maxlen=100), deque(maxlen=100), deque(maxlen=100)

ax.set_xlabel("Pitch")
ax.set_ylabel("Roll")
ax.set_zlabel("Dummy Z")
ax.set_title("Pitch & Roll 3D Visualization")

while True:
    try:
        line = ser.readline().decode().strip()
        if line:
            pitch, roll = map(float, line.split(",")[:2])
            xdata.append(pitch)
            ydata.append(roll)
            zdata.append(0)  # yaw ignored

            ax.clear()
            ax.set_xlabel("Pitch")
            ax.set_ylabel("Roll")
            ax.set_zlabel("Dummy Z")
            ax.plot3D(list(xdata), list(ydata), list(zdata))
            plt.pause(0.01)
    except Exception as e:
        print("Error:", e)
