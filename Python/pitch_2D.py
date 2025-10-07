import serial
import matplotlib.pyplot as plt
from collections import deque

# Configure serial port
ser = serial.Serial('COM3', 9600, timeout=1)  # Replace COM3 with your port

plt.ion()
fig, ax = plt.subplots()
ydata = deque(maxlen=100)
line, = ax.plot([], [])

ax.set_ylim(-180, 180)
ax.set_xlabel("Time")
ax.set_ylabel("Pitch (°)")
ax.set_title("Pitch 2D Visualization")

while True:
    try:
        data = ser.readline().decode().strip()
        if data:
            pitch = float(data.split(",")[0])
            ydata.append(pitch)
            line.set_data(range(len(ydata)), list(ydata))
            ax.set_xlim(0, len(ydata))
            plt.pause(0.01)
    except Exception as e:
        print("Error:", e)
