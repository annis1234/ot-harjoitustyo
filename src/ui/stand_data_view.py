import tkinter as Tk
from tkinter import ttk, constants
from services.plot_service import PLOT_SERVICE

class StandDataView():

    def __init__ (self, root, handle_show_plot_view):
        self._root = root
        self._frame = None
        self._plot_service = PLOT_SERVICE
        self._handle_show_plot_view = handle_show_plot_view

        self._font = "Comic Sans MS", 15
        self._fg = "green"

        self._initialize_stand_data()

    def pack(self):
        self._frame.place(relx=0.5, rely=0.5 ,anchor="center")

    def destroy(self):
        self._frame.destroy()

    def _initialize_stand_data(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_go_back_button()

        if self._plot_service.return_trees():
            main_tree_sp = ttk.Label(master=self._frame, text= f"Pääpuulaji: {self._plot_service.main_tree_sp()}", font=self._font, foreground=self._fg)
            mean_d = ttk.Label(master=self._frame, text=f"Keskiläpimitta (cm): {self._plot_service.mean_diameter():0.2f}", font=self._font, foreground=self._fg)
            mean_h = ttk.Label(master=self._frame, text=f"Keskipituus (m): {self._plot_service.mean_height():0.2f}", font=self._font, foreground=self._fg)
            sum_v = ttk.Label(master=self._frame, text=f"Tilavuus (m3/ha): {self._plot_service.sum_vol():0.3f}", font=self._font, foreground=self._fg)

            main_tree_sp.grid(row=12, column=0, sticky=constants.W, padx=5, pady=5)
            mean_d.grid(row=13, column=0, sticky=constants.W, padx=5, pady=5)
            mean_h.grid(row=14, column=0, sticky=constants.W, padx=5, pady=5)
            sum_v.grid(row=15, column=0, sticky=constants.W, padx=5, pady=5)

        else:
            label= ttk.Label(master=self._frame, text="Koeala on tyhjä.", font=self._font, foreground=self._fg)
            label.grid(row=11, column=0, sticky=constants.W, padx=5, pady=5)

    def _initialize_go_back_button(self):
        label = Tk.Button(master=self._frame, text="Takaisin", command=self._handle_show_plot_view, font=self._font, foreground=self._fg)
        label.grid(row=0, column=1, sticky=constants.E)