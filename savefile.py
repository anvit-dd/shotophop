import tkinter
import tkinter.filedialog
import tkinter.messagebox


def save_image() -> str:
    top = tkinter.Tk()
    top.withdraw()
    file_name = tkinter.filedialog.asksaveasfilename(
        defaultextension="*.shp",
        filetypes=[("SHP File", "*.shp"),
                   ("Jpg File", "*.jpg"),
                   ("Png File", "*.png"),
                   ("Icon File", "*.ico")
                   ])
    top.destroy()

    return file_name


def open_image() -> str:
    top = tkinter.Tk()
    top.withdraw()
    file_name = tkinter.filedialog.askopenfilename(defaultextension="*.shp",
                                                   filetypes=[('SHP File', '*.shp'), ('PNG File', '*.png'),
                                                              ('JPG File', '*.jpg')])
    top.destroy()
    return file_name


def ask_save(title, text) -> str:
    top = tkinter.Tk()
    top.withdraw()
    ans = tkinter.messagebox.askquestion(title, text)
    top.destroy()
    return ans


def save_error() -> str:
    top = tkinter.Tk()
    top.withdraw()
    ans = tkinter.messagebox.showerror("Error occured!", "Invalid File name")
    top.destroy()
    return ans


def blackwhite_warn() -> bool:
    top = tkinter.Tk()
    top.withdraw()
    ans = tkinter.messagebox.askyesnocancel("Warning!",
                                            "\nThe operation you are about to execute is permanent and irreversible.It is strongly recommended that you save your current work before proceeding.\n\nWould you like to save your work before proceeding with this operation?")
    top.destroy()
    return ans

def remove_bg() -> str:
    top = tkinter.Tk()
    top.withdraw()
    ans = tkinter.messagebox.askyesnocancel("Remove background", "Save as *.png detected!\nWould you like the image to be transparent?")
    top.destroy()
    return ans
