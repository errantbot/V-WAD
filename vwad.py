import datetime
from idlelib.ToolTip import ToolTip
from wad.detection import Detector
import webbrowser as web
from threading import Thread
import tldextract
import tkinter as tk
from tkinter.ttk import Treeview

__version__ = '1.0.0'

CREDITS = (
    "This program is free software: you can redistribute it and/or modify "
    "it under the terms of the GNU General Public License as published by "
    "the Free Software Foundation, either version 3 of the License, or "
    "(at your option) any later version.\n\n"

    "This program is distributed in the hope that it will be useful, "
    "but WITHOUT ANY WARRANTY; without even the implied warranty of "
    "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the "
    "GNU General Public License for more details.\n\n"

    "You should have received a copy of the GNU General Public License "
    "along with this program. If not, see http://www.gnu.org/licenses/.")


class CreditsTool(tk.Toplevel):
    """Opens a new window providing information regarding author, program
    version, license and links to used Icons."""

    def __init__(self, master=None, *args, **kwargs):
        """Initializes Toplevel object and builds credit interface."""
        super().__init__(master, *args, **kwargs)
        self.build()

    def build(self):
        """Initializes and builds application widgets."""
        text_credits = 'V-WAD\ncopyright © {year}\nerrantbot\nversion ' \
                       '{ver}'.format(year=datetime.datetime.now().year,
                                      ver=__version__)
        self.img_1 = tk.PhotoImage(file='wad/data/python-powered-h-50x65.png')

        # create main credits label
        self.lbl_info = tk.Label(self, text=text_credits,
                                 font=('courier', 10, 'normal'))

        self.lbl_info.grid(row=0, column=0, sticky='w', padx=1, pady=1)

        # create python logo credit
        self.lbl_logo = tk.Label(self, image=self.img_1, cursor='hand2')
        self.lbl_logo.grid(row=0, column=1, sticky='e', padx=1, pady=1)
        self.logo_tip = ToolTip(self.lbl_logo,
                                ["Check", "out", "www.python.org"])

        # create credits text labelframe
        self.credits_labelframe = tk.LabelFrame(self,
                                                text='License information',
                                                foreground='brown')
        self.credits_labelframe.grid(row=1, column=0, padx=1, pady=1,
                                     sticky='we', columnspan=3)

        # create credits text display
        self.credits_display = tk.Text(self.credits_labelframe)
        self.scrollbar = tk.Scrollbar(self.credits_labelframe)
        self.credits_display.grid(row=0, column=0, padx=1, pady=1, columnspan=1)
        self.credits_display.insert(0.0, CREDITS)
        self.credits_display.config(state=tk.DISABLED, wrap=tk.WORD,
                                    height=5, width=33, font=('courier', 8, 'normal'))
        self.scrollbar.grid(row=0, column=1, padx=1, pady=1, sticky='ens')
        self.credits_display.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.credits_display.yview)

        # create hyperlink labelframe
        self.credits_labelframe_2 = tk.LabelFrame(self, text='Icon credits',
                                                  foreground='brown')
        self.credits_labelframe_2.grid(row=2, column=0, padx=1, pady=1,
                                       sticky='we', columnspan=3)

        # create hyperlink labels and grid them
        self.lbl_link_2 = tk.Label(self.credits_labelframe_2,
                                   text='http://www.famfamfam.com/',
                                   cursor='hand2')
        self.lbl_link_2.grid(row=1, column=0, padx=0, pady=0, sticky='e')

        # bind link labels to hyperlink functions
        self.lbl_link_2.bind('<Button-1>', self.hyperlink_2)
        self.lbl_logo.bind('<Button-1>', self.hyperlink_4)

    @staticmethod
    def hyperlink_2(event=None):
        """Opens link to specified URL for credit purposes."""
        web.open_new(r"http://www.famfamfam.com/")

    @staticmethod
    def hyperlink_4(event=None):
        """Opens link to specified URL for credit purposes."""
        web.open_new(r"https://www.python.org/")


class Gui(tk.Frame):
    """Main program graphical user interface"""
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.build_menu(), self.build()

    def build_menu(self):
        """Initializes and builds program menu bar"""
        self.top = tk.Menu(self)

        # create file menu
        self.file = tk.Menu(self.top, tearoff=False)
        self.file.add_command(label='Search', accelerator='Ctrl+S',
                              command=self.search, compound=tk.LEFT, underline=0)
        self.file.add_separator()
        self.file.add_command(label='Exit', command=self.quit_program,
                              underline=0)
        self.top.add_cascade(label='File', menu=self.file, underline=0)

        # commands: view help, about
        self.info = tk.Menu(self.top, tearoff=False)
        self.info.add_command(label='About ...', command=self.view_credits,
                              compound=tk.LEFT, underline=0)
        self.top.add_cascade(label='?', menu=self.info, underline=0)

    def build(self):
        """Builds main program interface"""

        # search frame
        f1 = tk.Frame()
        f1.grid(row=0, column=0)
        group = tk.LabelFrame(f1, text="Search", padx=5, pady=5, fg='brown')
        group.pack(side="top", expand='yes', fill='x', padx=2, pady=2, anchor='n')
        self.entry_main = tk.Entry(group, width=73)
        self.entry_main.grid(sticky='ne')

        # results frame
        f2 = tk.Frame()
        f2.grid(row=1, column=0)
        group_2 = tk.LabelFrame(f2, text="Results", padx=5, pady=5, fg='brown')
        group_2.pack(side="top", expand='yes', fill='both', padx=2, pady=2)
        self.status = tk.Label(f2, text='ready', font=('verdana', 6, 'normal'))
        self.status.pack(anchor='se')
        self.treeview = Treeview(group_2, column=('A', 'B'),
                                 selectmode='extended', height=5)
        self.treeview.grid(row=0, column=0, sticky='w')
        self.treeview.column("#0", stretch=tk.NO, width=200)
        self.treeview.heading("#0", text='target')
        self.treeview.column("A", width=150, anchor='center')
        self.treeview.heading("A", text='technology')
        self.treeview.column("B", width=70)
        self.treeview.heading("B", text="version")
        self.sbar = tk.Scrollbar(group_2)
        self.treeview.config(yscrollcommand=self.sbar.set)
        self.sbar.config(command=self.treeview.yview)
        self.sbar.grid(column=1, row=0, rowspan=1, pady=0, sticky='ens')

        # key shortcut bindings
        self.entry_main.bind('<Return>', self.search)
        self.entry_main.bind('<Double-1>', self.search)
        self.bind_all('<Control-S>', self.search)
        self.bind_all('<Control-s>', self.search)

    def search(self, event=None):
        """Triggers a threaded technology detection scan"""
        url = self.entry_main.get()
        self.status['text'] = 'scanning...'
        Thread(target=self.scan_target, args=(url,)).start()

    def scan_target(self, url):
        """Function to detect technologies running on target and list them in
        gui treeview"""
        _id = None
        try:
            d = Detector().detect(url=url, timeout=5)
            for result in d:
                if d[result]:
                    ext = tldextract.extract(url)
                    _id = self.treeview.insert('', 'end', text='.'.join(ext[:3]))
                    tech_type, software = d[result][0].get('type'), \
                                          d[result][0].get('app')
                    version = d[result][0].get('ver')

                    # assign to gui treeview
                    if not version:
                        version = 'None'
                    self.treeview.insert(_id, 'end', text=tech_type,
                                         values=(software, version))
                    self.status['text'] = 'done'
                else:
                    self.status['text'] = 'No results found'

        except ValueError:
            self.status['text'] = "Invalid! Please input a full url"
        finally:
            del _id

    def view_credits(self):
        """ Opens a new window providing credits information."""

        # launch window and configure window settings
        self.win_credits = CreditsTool(self)
        self.win_credits.title('')
        self.win_credits.iconbitmap('wad/data/magnifier.ico')
        self.win_credits.geometry('+%d+%d' % (root.winfo_x() +
                                              20, root.winfo_y() + 20))
        self.win_credits.resizable(width=False, height=False)

        # set focus on window
        self.win_credits.grab_set()
        self.win_credits.focus()

        # start mainloop
        self.win_credits.mainloop()

    @staticmethod
    def quit_program():
        """Quits main program window"""
        root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("V-WAD {}".format(__version__))
    v_wad = Gui(root)
    root.config(menu=v_wad.top)
    v_wad.grid()
    root.resizable(width=False, height=False)
    root.iconbitmap('wad/data/magnifier.ico')
    root.protocol('WM_DELETE_WINDOW', v_wad.quit_program)
    root.mainloop()
