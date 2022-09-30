import tkinter
from tkinter import StringVar, ttk
import abc
import serial
import glob
import sys
#import serialCode

speed = 0
battery_voltage = 0
curr_sense_right = 0
accel_x = 0
accel_y = 0
accel_z = 0
class Window(ttk.Frame):
    '''
        Creates abstract class for all pop-up windows

    '''
    __metaclass__ = abc.ABCMeta

     # Constructor 

    def __init__(self, parent):
       
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.resizable(width=False, height=False) # Disallows window resizing
        self.validate_notempty = (self.register(self.notEmpty), '%P') 
        self.init_gui()

    # Validates Entry fields to ensure they aren't empty

    def notEmpty(self, P):
        
        if P.strip():
            valid = True
        else:
            print("Error: Field must not be empty.")
            valid = False
        return valid

    # Closes Window

    def close_win(self):
        
        self.parent.destroy()

class TelemetryWindow(Window):
    ''' 
        
        Creates a Telemetry Window displaying speed, accelerometer, left wheel current sense, right wheel current sense, battery voltage

    '''
    
    def init_gui(self):
        global speed
        self.parent.title("Telemetry")
        self.parent.geometry("300x150")
        
        self.grid_columnconfigure(0, weight=1) 
        self.grid_rowconfigure(5, weight=1) 
        
        self.parent.resizable(False, False)

        
        
        # Create Widgets
        self.chosen_comm = ttk.Label(self, text=comm_port)
        self.chosen_comm.grid(row=0, column=1, sticky='nswe')

        self.speed = ttk.Label(self, text="Speed: ")
        self.speed.grid(row=1, column=0, sticky='w')

        
        self.speed_val = ttk.Label(self, text='0')
        self.speed_val.grid(row=1, column=2, sticky='e')
        

        self.curr_sense_r= ttk.Label(self, text="Current Sense Right: ")
        self.curr_sense_r.grid(row=2, column=0, sticky='w')

        
        self.curr_sense_val = ttk.Label(self, text='0')
        self.curr_sense_val.grid(row=2, column=2, sticky='e')
        

        self.batt = ttk.Label(self, text="Battery Voltage: ")
        self.batt.grid(row=4, column=0, sticky='w')

        
        self.batt_val = ttk.Label(self, text='0')
        self.batt_val.grid(row=4, column=2, sticky='e')
        

        self.acc = ttk.Label(self, text="Accelerometer: ")
        self.acc.grid(row=5, column=0, sticky='w')
        
            
        self.accel_val = ttk.Label(self, text='0')
        self.accel_val.grid(row=5, column=2, sticky='e')
        



        # Padding
        for child in self.parent.winfo_children():
            child.grid_configure(padx=10, pady=1)

        self.parent.after(1000, self.updateVariables)
        
    def updateVariables(self):
        global speed
        global battery_voltage
        global accel_x
        global accel_y
        global accel_z
        global curr_sense_right

        speed += 1
        battery_voltage += 0.2
        accel_x += 1
        accel_y += 1
        accel_z += 1
        curr_sense_right += 0.2
        
        accel_text = "{}, {}, {}.".format(accel_x, accel_y, accel_z)
    
        self.speed_val['text'] = speed
        self.accel_val['text'] = accel_text
        self.batt_val['text'] = battery_voltage
        self.curr_sense_val['text'] = curr_sense_right

        self.parent.after(1000, self.updateVariables) 
  

class RCWindow(Window):
    '''
   
        Remote Control Window:
            
        Add the following to the code:
            * Functionality between serialCode.py and the individual functions for each button

    '''

    def init_gui(self):
        self.parent.title("Remote Control Window")
        self.parent.geometry("350x170")
        self.parent.columnconfigure(10, weight=2)
        self.parent.rowconfigure(10, weight=2)
        self.parent.resizable(False, False)
        # Create Widgets

        
        self.btfp = ttk.Button(self.parent, text="FWD+", command=self.fwd_plus)
        self.btfp.grid(row=0, column=7, stick='n')
        self.btfm = ttk.Button(self.parent, text="FWD-", command=self.fwd_minus)
        self.btfm.grid(row=1, column=7, stick='s')

        self.btbp = ttk.Button(self.parent, text="BACK+", command=self.back_plus)
        self.btbp.grid(row=9, column=7, stick='n')
        self.btbm = ttk.Button(self.parent, text="BACK-", command=self.back_minus)
        self.btbm.grid(row=10, column=7, stick='s')

        self.btlp = ttk.Button(self.parent, text="LEFT+", command=self.left_plus)
        self.btlp.grid(row=5, column=0, stick='wn')
        self.btlm = ttk.Button(self.parent, text="LEFT-", command=self.left_minus)
        self.btlm.grid(row=6, column=0, stick='ws')

        self.btrp = ttk.Button(self.parent, text="RIGHT+", command=self.right_plus)
        self.btrp.grid(row=5, column=9, stick='en')
        self.btrm = ttk.Button(self.parent, text="RIGHT-", command=self.right_minus)
        self.btrm.grid(row=6, column=9, stick='es')

        
        # Padding
        for child in self.parent.winfo_children():
            child.grid_configure(padx=20, pady=1)

        
     
    def fwd_plus(self):
        # Fill in your own code here
        pass

    def fwd_minus(self):
        # Fill in your own code here
        pass

    def left_plus(self):
        # Fill in your own code here
        pass

    def left_minus(self):
        # Fill in your own code here
        pass

    def right_plus(self):
        # Fill in your own code here
        pass

    def right_minus(self):
        # Fill in your own code here
        pass

    def back_plus(self):
        # Fill in your own code here
        pass

    def back_minus(self):
        # Fill in your own code here
        pass

class GUI(ttk.Frame):
    '''
  
        Main GUI class

        DO NOT CHANGE OR REMOVE THIS CODE

    '''
    
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    def opentelemetry(self):
        self.new_win = tkinter.Toplevel(self.root) # Set parent
        TelemetryWindow(self.new_win)

    def openremotecontrol(self):
        self.new_win = tkinter.Toplevel(self.root) # Set parent
        RCWindow(self.new_win)

    def init_gui(self):
        global com_ports
        com_ports = serial_ports()
        
        
        self.root.title('Design(E) - Serial Comms GUI')
        self.root.geometry("400x200")
        self.root.resizable(False, False)
        self.root.eval('tk::PlaceWindow . center')
        self.grid(column=0, row=0, sticky='nsew')
        self.grid_columnconfigure(0, weight=1) 
        self.grid_rowconfigure(0, weight=1) 
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        
        # Create Widgets
        self.label1 = ttk.Label(self, text="Select the COM port associated with your Bluetooth Dongle")
        self.label1.grid(row=0, column=0, sticky='we')

        var1 = StringVar(self)
        
        #self.combo1 = ttk.Combobox(self, textvariable=var1, values=com_ports)
        self.combo1 = ttk.Combobox(self, textvariable=var1, values=["COM12"])
        self.combo1.grid(row=1, column=0, sticky='ws')

        self.btnref = ttk.Button(self, text="Refresh COM Ports", command=self.refresh)
        self.btnref.grid(row=1, column=0, sticky='es')
        
        self.combut = ttk.Button(self, text='Choose COM', command=self.disable_buttons, width=150 ) 
        self.combut.grid(row=2, column=0, sticky='n')
        

        self.btn1 = ttk.Button(self, text='Telemetry', command=self.opentelemetry, width=300, state="disabled" ) 
        self.btn1.grid(row=3, column=0, sticky='n')

        self.btn2 = ttk.Button(self, text='Remote Control', command=self.openremotecontrol, width=300, state="disabled")
        self.btn2.grid(row=4, column=0, sticky='n')
        
        
        # Padding
        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=5)
        
        
        
        
    def disable_buttons(self):
        global comm_port

        comm_port = self.combo1.get()
        
        if comm_port != "" and comm_port != "~NONE~":
            self.btn1["state"] = "normal"
            self.btn2["state"] = "normal"
        else:
            self.btn1["state"] = "disabled"
            self.btn2["state"] = "disabled"
               
    def refresh(self):
        com_ports = serial_ports()
        self.combo1['values'] = com_ports


    

     
    
    

def serial_ports():
    
    '''

        Lists serial port names

        DO NOT CHANGE OR REMOVE THIS CODE

    '''

    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    com_ports = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            com_ports.append(port)
            
        except Exception as e:
            pass

    if not com_ports:
        com_ports = "~NONE~"
  
    return com_ports



if __name__ == '__main__':
    root = tkinter.Tk()
    GUI(root)
    
    #root.after(1000, updateVariables)
    root.mainloop()
    
