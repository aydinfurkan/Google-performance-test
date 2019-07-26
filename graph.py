import matplotlib.pyplot as plt
import statistics
from operator import truediv 

file_names = ["Results\\1 Kelime.txt", "Results\\2 Kelime.txt", "Results\\5 Kelime.txt"] # words without quotes
file_names_T = ["Results\\1 Kelime T.txt", "Results\\2 Kelime T.txt", "Results\\5 Kelime T.txt"] # words with quotes


def R_file(file_name): # Read file
    # Read strings line by line
    read_File = open(file_name,"r")
    wordList = []
    wordList = read_File.read().splitlines()
    read_File.close()

    word = []
    # Split lines 
    for i in wordList:
        a = i.split()
        word.append(a)

    number = []
    min_time = []
    max_time = []
    ave_time = []
    # Split values different arrays ( i[0] = result_number, i[1] = "->", i[2] = min. time, i[3] = max. time, i[4] = ave. time )
    for i in word:
        number.append(int(i[0]))
        min_time.append(int(i[2]))
        max_time.append(int(i[3]))
        ave_time.append(float(i[4]))
    
    return [number, min_time, max_time, ave_time]

def graph1():

    i = 1 # Subplot index
    for f in file_names + file_names_T:
        a = R_file(f)

        plt.subplot(2, 3, i)
        plt.title(f) # Subplot graph name

        plt.plot(a[0], a[2], "r", label = "Maximum")
        plt.plot(a[0], a[3], "b", label = "Average")
        plt.plot(a[0], a[1], "g", label = "Minimum")
        
        if i == 1 or i == 4 : plt.ylabel("Zaman(ms)") # Left sublots 
        if i == 4 or i == 5 or i == 6 : plt.xlabel("Sonuç sayısı") # Down subplots 
        
        i+=1

    plt.legend()
    plt.show()

def graph11():

    i = 1 # Subplot index
    for f in file_names + file_names_T:
        a = R_file(f)

        plt.subplot(2, 3, i)
        plt.title(f) # Subplot graph name
        
        plt.plot(a[0], list(map(truediv, a[0], a[2])), "r", label = "Maximum")
        plt.plot(a[0], list(map(truediv, a[0], a[3])), "b", label = "Average")
        plt.plot(a[0], list(map(truediv, a[0], a[1])), "g", label = "Minimum")

        if i == 4 or i == 5 or i == 6 : plt.xlabel("Sonuç sayısı") # Left sublots 
        if i == 1 or i == 4 : plt.ylabel("Sonuç sayısı / Zaman(ms)") # Down subplots
        
        i+=1

    plt.legend()
    plt.show()

def graph2():

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1) # Seperate three subplots

    for f in file_names + file_names_T:
        a = R_file(f)

        ax1.set(ylabel = "Maximum Time (ms)")
        ax1.plot(a[0], a[2], label = f)
        ax1.axis([0, 22000000, 0, 1000])
        ax1.legend()

        ax2.set(ylabel = "Average Time (ms)")
        ax2.plot(a[0], a[3], label = f)
        ax2.axis([0, 22000000, 0, 800])
        ax2.legend()

        ax3.set(ylabel = "Minimum Time (ms)")
        ax3.plot(a[0], a[1], label = f)
        ax3.axis([0, 22000000, 0, 600])
        ax3.legend()

    plt.xlabel("Sonuç sayısı")
    plt.show()

def graph21():

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1) # Seperate three subplots

    for f in file_names + file_names_T:
        a = R_file(f)

        ax1.set(ylabel = "Sonuç sayısı /\n Maximum Time (ms)")
        ax1.plot(a[0], list(map(truediv, a[0], a[2])), label = f)
        ax1.axis([0, 22000000, 0, 40000])
        ax1.legend()

        ax2.set(ylabel = "Sonuç sayısı /\n Average Time (ms)")
        ax2.plot(a[0], list(map(truediv, a[0], a[3])), label = f)
        ax2.axis([0, 22000000, 0, 60000])
        ax2.legend()

        ax3.set(ylabel = "Sonuç sayısı /\n Minimum Time (ms)")
        ax3.plot(a[0], list(map(truediv, a[0], a[1])), label = f)
        ax3.axis([0, 22000000, 0, 70000])
        ax3.legend()

    plt.xlabel("Sonuç sayısı")
    plt.show()

def graph3(n = "Tırnaksız"):

    min_times = []
    max_times = []
    ave_times = []

    file_n = file_names if n == "Tırnaksız" else file_names_T
    
    for f in file_n:
        a = R_file(f)
        min_times.append(statistics.mean(a[0]) / statistics.mean(a[1]))
        max_times.append(statistics.mean(a[0]) / statistics.mean(a[2]))
        ave_times.append(statistics.mean(a[0]) / statistics.mean(a[3]))

    x = [1, 2, 3]

    plt.plot(x, min_times, label = "Min." + n)
    plt.plot(x, ave_times, label = "Ave." + n)
    plt.plot(x, max_times, label = "Max." + n)

    if(n == "Tırnaksız"):
        graph3("Tırnaklı")
        return

    tick = ['1 Kelime', '2 Kelime', '5 Kelime']

    plt.title("Grup ortalamaları")
    plt.xlabel("Kelime")
    plt.ylabel("Sonuç sayısı / Zaman(ms)")
    plt.xticks(x, tick)
    plt.legend()
    plt.show()


graph1()
graph11()

graph2()
graph21()

graph3()
