import numpy as np
import matplotlib.pyplot as plt

Am = 5
Fm = 5
t= np.arange(0,2,0.001)
message = Am*np.sin(2*np.pi*Fm*t)
plt.subplot(3,1,1)
plt.plot(t,message)
plt.xlabel("Time")
plt.ylabel("amplitude")
plt.title("Message Signal")

Ac = 10
Fc=50
carrier = Ac*np.sin(2*np.pi*Fc*t)
plt.subplot(3,1,2)
plt.plot(t,carrier)
plt.xlabel("Time")
plt.ylabel("amplitude")
plt.title("Carrier Signal")

m = Am/Ac
modulated = Ac*(1+m*np.sin(2*np.pi*Fm*t))*np.sin(2*np.pi*Fc*t)
plt.subplot(3,1,3)
plt.plot(t,modulated)
plt.xlabel("Time")
plt.ylabel("amplitude")
plt.title("Modulated Signal")
plt.show()



#noisy signal
fs= 5000
t = np.arange(0,0.04,1/fs)
fm = 100

message = np.sin(2*np.pi*fm*t)

noise_power = 0.4
noise = np.random.normal(0,noise_power,len(t))

channel_output = message + noise

window_size=5
Rx_recovered = np.convolve(
    channel_output,
    np.ones(window_size)/window_size,
    mode="same"
)

plt.figure(figsize=(10,8))

plt.subplot(3,1,1)
plt.plot(t,message,color="green")
plt.xlabel("Time")
plt.ylabel("amplitude")
plt.title("Transmitter output")
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(t,channel_output,color="red")
plt.xlabel("Time")
plt.ylabel("amplitude")
plt.title("Channel output (Noisy signal)")
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(t,Rx_recovered,color="blue")
plt.xlabel("Time")
plt.ylabel("amplitude")
plt.title("Receiver output")
plt.grid(True)
plt.legend()

plt.show()

