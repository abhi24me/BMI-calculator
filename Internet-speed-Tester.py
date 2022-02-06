from tkinter import *
import speedtest


def speedcheck():
    sd = speedtest.Speedtest()
    sd.get_best_servers()
    down = str(round(sd.download() / (10 ** 6), 3)) + "Mbps"
    up = str(round(sd.upload() / (10 ** 6), 3)) + "Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)


sd = Tk()
sd.title(" Internet Speed Tester")
sd.geometry("450x450")
sd.config(bg="cyan")

lab = Label(sd, text="Internet Speed Tester", font=("Time New Roman", 26, "bold"), bg="cyan", fg="yellow")
lab.place(x=30, y=30, height=50, width=380)

lab = Label(sd, text="Downloading Speed", font=("Time New Roman", 26, "bold"))
lab.place(x=30, y=90, height=50, width=380)

lab_down = Label(sd, text="00", font=("Time New Roman", 26, "bold"))
lab_down.place(x=30, y=160, height=50, width=380)

lab = Label(sd, text="Uploading Speed", font=("Time New Roman", 26, "bold"))
lab.place(x=30, y=230, height=50, width=380)

lab_up = Label(sd, text="00", font=("Time New Roman", 26, "bold"))
lab_up.place(x=30, y=300, height=50, width=380)

button = Button(sd, text="CHECK SPEED", font=("Time New Roman", 26, "bold"), relief=RAISED, bg="blue", fg="red",
                command=speedcheck)
button.place(x=30, y=370, height=50, width=380)
sd.mainloop()
