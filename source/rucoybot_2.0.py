import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image
from multiprocessing import Process, Queue, freeze_support
from urllib.request import urlopen
import json

class RucoyGui(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		toolbarfont = Font(size=20)
		
		self.welcomebtn = tk.Button(cursor='hand2', text="Welcome", bg='#3f3f3f', fg='#57cade', command=self.welcome, relief='flat', font=toolbarfont, overrelief='sunken')
		self.welcomebtn.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), ipadx=30, sticky='nesw')
		
		self.getstartbtn = tk.Button(cursor='hand2', text="Get Started", bg='#1f1f1f', fg='#57cade', command=self.getstarted, relief='flat', font=toolbarfont, overrelief='sunken')
		self.getstartbtn.grid(row=1, column=0, padx=(0, 0), pady=(0, 0), ipadx=30, sticky='nesw')
		
		self.runmybotbtn = tk.Button(cursor='hand2', text="Run My Bot", bg='#1f1f1f', fg='#57cade', command=self.runmybot, relief='flat', font=toolbarfont, overrelief='sunken')
		self.runmybotbtn.grid(row=2, column=0, padx=(0, 0), pady=(0, 0), ipadx=30, sticky='nesw')
		
		self.helpbtn = tk.Button(cursor='hand2', text="Help", bg='#1f1f1f', fg='#57cade', command=self.help, relief='flat', font=toolbarfont, overrelief='sunken')
		self.helpbtn.grid(row=3, column=0, padx=(0, 0), pady=(0, 0), ipadx=30, sticky='nesw')
		
		self.settingsbtn = tk.Button(cursor='hand2', text="Settings", bg='#1f1f1f', fg='#57cade', command=self.settings, relief='flat', font=toolbarfont, overrelief='sunken')
		self.settingsbtn.grid(row=4, column=0, padx=(0, 0), pady=(0, 0), ipadx=30, sticky='nesw')
		
		self.devicesbtn = tk.Button(cursor='hand2', text="Devices", bg='#1f1f1f', fg='#57cade', command=self.devices, relief='flat', font=toolbarfont, overrelief='sunken')
		self.devicesbtn.grid(row=5, column=0, padx=(0, 0), pady=(0, 0), ipadx=30, sticky='nesw')
		
		self.filterbtn = tk.Button(cursor='hand2', text="Filters", bg='#1f1f1f', fg='#57cade', command=self.filters, relief='flat', font=toolbarfont, overrelief='sunken')
		self.filterbtn.grid(row=6, column=0, padx=(0, 0), pady=(0, 0), ipadx=30, sticky='nesw')
		
		
		self.aboutbtn = tk.Button(cursor='hand2', text="About", bg='#1f1f1f', fg='#57cade', command=self.about, relief='flat', font=toolbarfont, overrelief='sunken')
		self.aboutbtn.grid(row=7, column=0, padx=(0, 0), pady=(0, 0), ipadx=30, sticky='nesw')
		
		
		'''
		Welcome
		Get Started 
		Run My Bot
		Help
		Settings
		Devices
		Filters
		About
		'''
		
		
		ghostlbl = tk.Label(text="  ", bg='#1f1f1f')
		ghostlbl.grid(row=8, rowspan=2, column=0, padx=(0, 0), pady=(0, 0), sticky='nesw')
		
		self.activeframe = "welcome"
		
		
		# This below is the frame for the Welcome Tab.
		self.welcomeframe = tk.Frame(bg='black')
		
		self.w_img = ImageTk.PhotoImage(Image.open("robot.png").resize((200, 200)))
		self.w_imglbl = tk.Label(self.welcomeframe, image=self.w_img, bg='black')
		self.w_imglbl.image = self.w_img
		self.w_imglbl.grid(row=0, column=1, sticky='w', padx=(20, 0), pady=(50, 40))
		
		w_headfont = Font(size=30)
		self.w_headlbl = tk.Label(self.welcomeframe, text="Welcome to\nRucoy Bot", bg='black', fg='#57cade', font=w_headfont)
		self.w_headlbl.grid(row=0, column=0, sticky='e', padx=(0, 20), pady=(50, 40))
		
		self.w_introtext = """Hi, thank you for trying out Rucoy Bot!\n\nTo start running a bot for gold, xp, and drops, check out the Get Started Tab.\n\nIf you'd like to learn about advanced settings or troubleshooting, check out the Help Tab. \n\nOtherwise, if you have any questions/feedback/issues, please contact me at your.rucoybot@gmail.com """
		
		w_msgfont = Font(size=15)
		self.w_intromsg = tk.Message(self.welcomeframe, text=self.w_introtext, justify='left', bg='black', fg='#57cade', relief='flat', width=500, font=w_msgfont)
		self.w_intromsg.grid(row=1, column=0, columnspan=2, padx=(0, 0), pady=(0, 0), sticky='nesw')
		
		self.welcomeframe.grid(row=0, rowspan=500, column=1, sticky='nesw')
		
		
		#This below is the frame for the Get Started Tab
		self.getstartframe = tk.Frame(bg='black')
		
		g_headfont = Font(size=30, underline=True)
		self.g_headlbl = tk.Label(self.getstartframe, text="How To Get Started", bg='black', fg='#57cade', font=g_headfont)
		self.g_headlbl.grid(row=0, column=0, sticky='es', padx=(0, 20), pady=(50, 40))
		
		self.g_img = ImageTk.PhotoImage(Image.open("robot.png").resize((50, 50)))
		self.g_imglbl = tk.Label(self.getstartframe, image=self.g_img, bg='black')
		self.g_imglbl.image = self.g_img
		self.g_imglbl.grid(row=0, column=1, sticky='w', padx=(20, 0), pady=(50, 40))
		
		self.g_instructtext = """There are currently four botting modes. To bot, you only need to know Hunting Mode, Farming Mode, and Training Mode.\n\n*   Hunting mode will just attack monsters and ignore any drops.\n*   Farming Mode will hunt monsters and pick up all gold/drops.\n*   Training mode will autoswitch to your training weapon and will focus on stats.\n\nTo Start, it's just 5 steps.\n\n1) Select Hunting, Farming, or Training Mode.\n2) Choose the server you want to bot on. (That number is players online.)\n3) Choose a weapon to bot with. (Melee/Dist/Mage)\n4) Click which potions to use while botting.\n5) Hit 'Start Bot!' """
		
		g_msgfont = Font(size=15)
		self.g_instructmsg = tk.Message(self.getstartframe, text=self.g_instructtext, justify='left', bg='black', fg='#57cade', relief='flat', width=700, font=g_msgfont)
		self.g_instructmsg.grid(row=1, column=0, columnspan=2, padx=(0, 0), pady=(0, 0), sticky='nesw')
		
		# runmybot needed initialization values
		self.botpower = False
		self.botmode = 0
		self.weapon = 0
		self.hppot = 0
		self.mppot = 0
		self.pottier = 3
		self.tier = 6
		
		#This below is the frame for the Run My Bot Tab
		self.runmybotframe = tk.Frame(bg='black')
		
		r_headfont = Font(size=30, underline=True)
		self.r_headlbl = tk.Label(self.runmybotframe, text="Let's Bot!", bg='black', fg='#57cade', font=r_headfont)
		self.r_headlbl.grid(row=0, column=1, sticky='es', padx=(0, 0), pady=(40, 20))
		
		self.r_img = ImageTk.PhotoImage(Image.open("robot.png").resize((50, 50)))
		self.r_imglbl = tk.Label(self.runmybotframe, image=self.r_img, bg='black')
		self.r_imglbl.image = self.r_img
		self.r_imglbl.grid(row=0, column=2, sticky='w', padx=(70, 0), pady=(40, 20))
		
		r_subheadfont = Font(size=20)
		self.r_choosemodemsg = tk.Message(self.runmybotframe, text="Choose Your Botting Mode", justify='right', bg='black', fg='#57cade', relief='flat', width=700, font=r_subheadfont)
		self.r_choosemodemsg.grid(row=1, column=1, columnspan=2, pady=(0, 20), sticky='nesw')
		
		self.r_monimg_active = ImageTk.PhotoImage(Image.open("mon_active.png").resize((30, 30)))
		self.r_monimg_disabled = ImageTk.PhotoImage(Image.open("mon_disabled.png").resize((30, 30)))
		self.r_monimgbtn = tk.Button(self.runmybotframe, cursor='hand2', text='Monitor Mode', image=self.r_monimg_active, bg="#49e0e3", command=self.monitorplz, compound='top')
		self.r_monimgbtn.image = self.r_monimg_active
		self.r_monimgbtn.grid(row=2, column=1, padx=(0, 60), pady=(0, 30), sticky='e')
		
		self.r_huntimg_active = ImageTk.PhotoImage(Image.open("hunt_active.png").resize((30, 30)))
		self.r_huntimg_disabled = ImageTk.PhotoImage(Image.open("hunt_disabled.png").resize((30, 30)))
		self.r_huntimgbtn = tk.Button(self.runmybotframe, cursor='hand2', text='Hunting Mode', image=self.r_huntimg_disabled, bg='#1f1f1f', command=self.hunterplz, compound='top')
		self.r_huntimgbtn.image = self.r_huntimg_disabled
		self.r_huntimgbtn.grid(row=2, column=2, padx=(20, 0), pady=(0, 30), sticky='w')
		
		self.r_farmimg_active = ImageTk.PhotoImage(Image.open("farm_active.png").resize((30, 30)))
		self.r_farmimg_disabled = ImageTk.PhotoImage(Image.open("farm_disabled.png").resize((30, 30)))
		self.r_farmimgbtn = tk.Button(self.runmybotframe, cursor='hand2', text='Farming Mode', image=self.r_farmimg_disabled, bg='#1f1f1f', command=self.farmerplz, compound='top')
		self.r_farmimgbtn.image = self.r_farmimg_disabled
		self.r_farmimgbtn.grid(row=3, column=1, padx=(0, 60), pady=(0, 30), sticky='e')
		
		self.r_skillimg_active = ImageTk.PhotoImage(Image.open("skill_active.png").resize((30, 30)))
		self.r_skillimg_disabled = ImageTk.PhotoImage(Image.open("skill_disabled.png").resize((30, 30)))
		self.r_skillimgbtn = tk.Button(self.runmybotframe, cursor='hand2', text='Training Mode', image=self.r_skillimg_disabled, bg='#1f1f1f', command=self.skillerplz, compound='top')
		self.r_skillimgbtn.image = self.r_skillimg_disabled
		self.r_skillimgbtn.grid(row=3, column=2, padx=(20, 0), pady=(0, 30), sticky='w')
		
		self.r_chooseweaponmsg = tk.Message(self.runmybotframe, text="Choose Your Weapon", justify='right', bg='black', fg='#57cade', relief='flat', width=700, font=r_subheadfont)
		self.r_chooseweaponmsg.grid(row=4, column=1, columnspan=2, pady=(0, 20), sticky='nesw')
		
		
		
		#Set Var to keep track of which level range weapon to show/ no sword/ training dagger.
		self.swordimg_n = ImageTk.PhotoImage(Image.open("nosword.png").resize((35, 35)))
		self.swordimg_t = ImageTk.PhotoImage(Image.open("tsword.png").resize((35, 35)))
		self.swordimg_1 = ImageTk.PhotoImage(Image.open("1sword.png").resize((35, 35)))
		self.swordimg_2 = ImageTk.PhotoImage(Image.open("2sword.png").resize((35, 35)))
		self.swordimg_3 = ImageTk.PhotoImage(Image.open("3sword.png").resize((35, 35)))
		self.swordimg_4 = ImageTk.PhotoImage(Image.open("4sword.png").resize((35, 35)))
		self.swordimg_5 = ImageTk.PhotoImage(Image.open("5sword.png").resize((35, 35)))
		self.swordimg_6 = ImageTk.PhotoImage(Image.open("6sword.png").resize((35, 35)))
		self.swordimg_7 = ImageTk.PhotoImage(Image.open("7sword.png").resize((35, 35)))
		#Create sword image Label and grid into place.
		self.swordimgbtn = tk.Button(self.runmybotframe, cursor='hand2', image=self.swordimg_n, bg='#1f1f1f', command=self.swordplz, text='  Melee  ', compound='top')
		self.swordimgbtn.image = self.swordimg_n
		self.swordimgbtn.grid(row=5, column=1, padx=(0, 90), sticky='e')
		
		#Set Var to keep track of which level range weapon to show/ no bow/ training bow.
		self.bowimg_n = ImageTk.PhotoImage(Image.open("nobow.png").resize((35, 35)))
		self.bowimg_t = ImageTk.PhotoImage(Image.open("tbow.png").resize((35, 35)))
		self.bowimg_1 = ImageTk.PhotoImage(Image.open("1bow.png").resize((35, 35)))
		self.bowimg_2 = ImageTk.PhotoImage(Image.open("2bow.png").resize((35, 35)))
		self.bowimg_3 = ImageTk.PhotoImage(Image.open("3bow.png").resize((35, 35)))
		self.bowimg_4 = ImageTk.PhotoImage(Image.open("4bow.png").resize((35, 35)))
		self.bowimg_5 = ImageTk.PhotoImage(Image.open("5bow.png").resize((35, 35)))
		self.bowimg_6 = ImageTk.PhotoImage(Image.open("6bow.png").resize((35, 35)))
		self.bowimg_7 = ImageTk.PhotoImage(Image.open("7bow.png").resize((35, 35)))
		#Create bow image Label and grid into place.
		self.bowimgbtn = tk.Button(self.runmybotframe, cursor='hand2', image=self.bowimg_n, bg='#1f1f1f', command=self.bowplz, text='Distance', compound='top')
		self.bowimgbtn.image = self.bowimg_n
		self.bowimgbtn.grid(row=5, column=1, columnspan=2)
		
		#Set Var to keep track of which level range weapon to show/ no wand/ training wand.
		self.wandimg_n = ImageTk.PhotoImage(Image.open("nowand.png").resize((35, 35)))
		self.wandimg_t = ImageTk.PhotoImage(Image.open("twand.png").resize((35, 35)))
		self.wandimg_1 = ImageTk.PhotoImage(Image.open("1wand.png").resize((35, 35)))
		self.wandimg_2 = ImageTk.PhotoImage(Image.open("2wand.png").resize((35, 35)))
		self.wandimg_3 = ImageTk.PhotoImage(Image.open("3wand.png").resize((35, 35)))
		self.wandimg_4 = ImageTk.PhotoImage(Image.open("4wand.png").resize((35, 35)))
		self.wandimg_5 = ImageTk.PhotoImage(Image.open("5wand.png").resize((35, 35)))
		self.wandimg_6 = ImageTk.PhotoImage(Image.open("6wand.png").resize((35, 35)))
		self.wandimg_7 = ImageTk.PhotoImage(Image.open("7wand.png").resize((35, 35)))
		#Create wand image Label and grid into place.
		self.wandimgbtn = tk.Button(self.runmybotframe, cursor='hand2', image=self.wandimg_n, bg='#1f1f1f', command=self.wandplz, text='  Mage  ', compound='top')
		self.wandimgbtn.image = self.wandimg_n
		self.wandimgbtn.grid(row=5, column=2, padx=(45, 0), sticky='w')
		
		self.r_nextimg = ImageTk.PhotoImage(Image.open("forward_arrow.png").resize((35, 35)))
		self.r_nextpage = tk.Button(self.runmybotframe, cursor='hand2', bg='#c7ffb5', command=self.r_nextpage, text='Next   ', font=r_subheadfont, image=self.r_nextimg, compound='right')
		self.r_nextpage.grid(row=6, column=1, columnspan=2, ipadx=180, pady=(40, 0))
		
		
		self.runmybotframe2 = tk.Frame(bg='black')
		
		self.r_headlbl2 = tk.Label(self.runmybotframe2, text="Let's Bot!", bg='black', fg='#57cade', font=r_headfont)
		self.r_headlbl2.grid(row=0, column=1, sticky='es', padx=(0, 0), pady=(40, 20))
		
		self.r_img2 = ImageTk.PhotoImage(Image.open("robot.png").resize((50, 50)))
		self.r_imglbl2 = tk.Label(self.runmybotframe2, image=self.r_img2, bg='black')
		self.r_imglbl2.image = self.r_img2
		self.r_imglbl2.grid(row=0, column=2, sticky='w', padx=(70, 0), pady=(40, 20))
		
		self.r_chooseservmsg = tk.Message(self.runmybotframe2, text="Choose Your Server", justify='right', bg='black', fg='#57cade', relief='flat', width=700, font=r_subheadfont)
		self.r_chooseservmsg.grid(row=1, column=1, columnspan=2, pady=(0, 20), sticky='nesw')
		
		#Grab the server data from the rucoyonline.com json file
		self.server_options = tk.StringVar()
		self.all_servers = ['Any Server']
		
		self.update_servlist()
		
		self.server_options.set(self.all_servers[0])
		self.servoptdd = tk.OptionMenu(self.runmybotframe2, self.server_options, *self.all_servers)
		servoptddfont = Font(size=15)
		self.servoptdd.config(bg='#1f1f1f', fg='#57cade', font=servoptddfont, width=20)
		self.servoptdd['menu'].config(bg='#1f1f1f', fg='#57cade')
		self.servoptdd['highlightthickness'] = 0
		self.servoptdd.grid(row=2, column=1, columnspan=2, pady=(0, 10))
		#Refresh Server List Button
		self.reload_serv_img = ImageTk.PhotoImage(Image.open("reload.png").resize((18, 18)))
		reloadfont = Font(size=12)
		self.reload_serv_btn = tk.Button(self.runmybotframe2, cursor='hand2', image=self.reload_serv_img, bg='#1f1f1f', fg='#57cade', command=self.update_servlist, text='Refresh  ', compound='right', font=reloadfont)
		self.reload_serv_btn.image = self.reload_serv_img
		self.reload_serv_btn.grid(row=3, column=1, columnspan=2)
		
		self.r_choosepotsmsg = tk.Message(self.runmybotframe2, text="Choose Your Potions", justify='right', bg='black', fg='#57cade', relief='flat', width=700, font=r_subheadfont)
		self.r_choosepotsmsg.grid(row=4, column=1, columnspan=2, pady=(30, 20), sticky='nesw')
		
		
		#Create HP potion image resources.
		self.hppotimg_1 = ImageTk.PhotoImage(Image.open("h1pot.png").resize((35, 35)))
		self.hppotimg_2 = ImageTk.PhotoImage(Image.open("h2pot.png").resize((35, 35)))
		self.hppotimg_3 = ImageTk.PhotoImage(Image.open("h3pot.png").resize((35, 35)))
		self.hppotimg_n = ImageTk.PhotoImage(Image.open("nopot.png").resize((35, 35)))
		#Create HP Potion image label and grid into place.
		self.hppotimgbtn = tk.Button(self.runmybotframe2, cursor='hand2', image=self.hppotimg_n, bg='#1f1f1f', command=self.hppotplz)
		self.hppotimgbtn.image = self.hppotimg_n
		self.hppotimgbtn.grid(row=5, column=1, padx=(0, 60), sticky='e')
		#Create MP Potion image resources.
		self.mppotimg_1 = ImageTk.PhotoImage(Image.open("m1pot.png").resize((35, 35)))
		self.mppotimg_2 = ImageTk.PhotoImage(Image.open("m2pot.png").resize((35, 35)))
		self.mppotimg_3 = ImageTk.PhotoImage(Image.open("m3pot.png").resize((35, 35)))
		self.mppotimg_n = ImageTk.PhotoImage(Image.open("nopot.png").resize((35, 35)))
		#Create MP Potion image label and grid into place.
		self.mppotimgbtn = tk.Button(self.runmybotframe2, cursor='hand2', image=self.mppotimg_n, bg='#1f1f1f', command=self.mppotplz)
		self.mppotimgbtn.image = self.mppotimg_n
		self.mppotimgbtn.grid(row=5, column=2, padx=(10, 0), sticky='w')
		
		self.r_nextimg2 = ImageTk.PhotoImage(Image.open("forward_arrow.png").resize((35, 35)))
		self.r_nextpage2 = tk.Button(self.runmybotframe2, cursor='hand2', bg='#c7ffb5', command=self.r_nextpage2, text='Start!   ', font=r_subheadfont, image=self.r_nextimg2, compound='right')
		self.r_nextpage2.grid(row=8, column=1, columnspan=2, ipadx=180, pady=(70, 0))
		
		self.runmybotframe3 = tk.Frame(bg='black')
		
		self.r_headlbl3 = tk.Label(self.runmybotframe3, text="Let's Bot!", bg='black', fg='#57cade', font=r_headfont)
		self.r_headlbl3.grid(row=0, column=1, sticky='es', padx=(0, 0), pady=(40, 20))
		
		self.r_img3 = ImageTk.PhotoImage(Image.open("robot.png").resize((50, 50)))
		self.r_imglbl3 = tk.Label(self.runmybotframe3, image=self.r_img3, bg='black')
		self.r_imglbl3.image = self.r_img3
		self.r_imglbl3.grid(row=0, column=2, sticky='w', padx=(70, 0), pady=(40, 20))
		
		
		
		
		
		#This below is the frame for the Help Tab
		self.helpframe = tk.Frame(bg='black')
		
		h_pagefont = Font(size=10)
		self.h_nextimg = ImageTk.PhotoImage(Image.open("forward_arrow.png").resize((15, 15)))
		self.h_nextpagebtn = tk.Button(self.helpframe, cursor='hand2', text="Next Page  ", image=self.h_nextimg, bg='#1f1f1f', fg='#57cade', compound='right', command=self.h_nextpage, relief='flat', font=h_pagefont, overrelief='sunken')
		self.h_nextpagebtn.grid(row=0, column=1, columnspan=2, padx=(40, 0), pady=(10, 10), ipadx=10, sticky='w')
		
		self.h_page = 0
		
		h_headfont = Font(size=30, underline=True)
		self.h_headlbl = tk.Label(self.helpframe, text="Help & General Resources", bg='black', fg='#57cade', font=h_headfont)
		self.h_headlbl.grid(row=1, column=0, sticky='es', padx=(0, 20), pady=(30, 30))
		
		self.h_img = ImageTk.PhotoImage(Image.open("robot.png").resize((50, 50)))
		self.h_imglbl = tk.Label(self.helpframe, image=self.h_img, bg='black')
		self.h_imglbl.image = self.h_img
		self.h_imglbl.grid(row=1, column=1, sticky='w', padx=(20, 0), pady=(30, 30))
		
		h_subheadfont = Font(size=20)
		self.h_troubleshootmsg = tk.Message(self.helpframe, text="Troubleshooting", justify='left', bg='black', fg='#57cade', relief='flat', width=700, font=h_subheadfont)
		self.h_troubleshootmsg.grid(row=2, column=0, columnspan=2, pady=(0, 20), sticky='nesw')
		
		self.h_instructtext = """Fatal Error: I don't know my coordinates-    If this doesn't resolve itself, double check you're on the right server in the Rucoy app. \n\nMy bot isn't doing anything/It's really slow-   If your internet is slow, that's the problem. If not, manually move your character near a monster. If the bot still fails to attack, double check you're not on monitor mode.\n\nThe bot is moving but isn't attacking anything-   What screen resolution is your device or emulator? If it's not 1280x720 or 720p, hit the Devices Tab, and enable 1080p mode.\n\nI still can't get this to work right! -   I'm sorry! Please email me at your.rucoybot@gmail.com """
		
		h_msgfont = Font(size=15)
		self.h_instructmsg = tk.Message(self.helpframe, text=self.h_instructtext, justify='left', bg='black', fg='#57cade', relief='flat', width=700, font=h_msgfont)
		self.h_instructmsg.grid(row=3, column=0, columnspan=2, padx=(0, 0), pady=(0, 0), sticky='nesw')
		
		
		self.helpframe2 = tk.Frame(bg='black')
		
		h_pagefont2 = Font(size=10)
		
		self.h_backimg2 = ImageTk.PhotoImage(Image.open("back_arrow.png").resize((15, 15)))
		self.h_backpagebtn2 = tk.Button(self.helpframe2, cursor='hand2', text="  Previous Page", image=self.h_backimg2, bg='#1f1f1f', fg='#57cade', compound='left', command=self.h_backpage2, relief='flat', font=h_pagefont2, overrelief='sunken')
		self.h_backpagebtn2.grid(row=0, column=0, padx=(0, 420), pady=(10, 10), ipadx=10, sticky='e')
		
		self.h_nextimg2 = ImageTk.PhotoImage(Image.open("forward_arrow.png").resize((15, 15)))
		self.h_nextpagebtn2 = tk.Button(self.helpframe2, cursor='hand2', text="Next Page  ", image=self.h_nextimg2, bg='#1f1f1f', fg='#57cade', compound='right', command=self.h_nextpage2, relief='flat', font=h_pagefont2, overrelief='sunken')
		self.h_nextpagebtn2.grid(row=0, column=1, columnspan=2, padx=(40, 0), pady=(10, 10), ipadx=10, sticky='w')
		
		h_headfont2 = Font(size=30, underline=True)
		self.h_headlbl2 = tk.Label(self.helpframe2, text="Help & General Resources", bg='black', fg='#57cade', font=h_headfont2)
		self.h_headlbl2.grid(row=1, column=0, sticky='es', padx=(0, 20), pady=(30, 30))
		
		self.h_img2 = ImageTk.PhotoImage(Image.open("robot.png").resize((50, 50)))
		self.h_imglbl2 = tk.Label(self.helpframe2, image=self.h_img2, bg='black')
		self.h_imglbl2.image = self.h_img2
		self.h_imglbl2.grid(row=1, column=1, sticky='w', padx=(20, 0), pady=(30, 30))
		
		h_subheadfont2 = Font(size=20)
		self.h_protipsmsg2 = tk.Message(self.helpframe2, text="Pro Tips", justify='left', bg='black', fg='#57cade', relief='flat', width=700, font=h_subheadfont2)
		self.h_protipsmsg2.grid(row=2, column=0, columnspan=2, pady=(0, 20), sticky='nesw')
		
		self.h_protipstext2 = """Pro Tip #1 (Advanced)-\n*   You can actually use this program to bot on your phone! First, just plug your phone into your computer. Next, google how to enable ADB and do so. Then, google, install, and run 'gnirehtet' from github.com \n\nPro Tip #2-\n*   Enable email notifications in the Settings Menu and use your 'email to text' address to get text notifications. For example, Verizon in the U.S. is 5553331111@vtext.com\n\nPro Tip #3-\n*   Use the 'Only Attack' option in the Settings menu to keep your bot focused on the monsters you want. For example, typing in 'Skeleton' prevents your bot from wandering into Drow Territory."""
		
		h_msgfont2 = Font(size=15)
		self.h_instructmsg2 = tk.Message(self.helpframe2, text=self.h_protipstext2, justify='left', bg='black', fg='#57cade', relief='flat', width=700, font=h_msgfont2)
		self.h_instructmsg2.grid(row=3, column=0, columnspan=2, padx=(0, 0), pady=(0, 0), sticky='nesw')
		
		
		self.helpframe3 = tk.Frame(bg='black')
		
		h_pagefont3 = Font(size=10)
		
		self.h_backimg3 = ImageTk.PhotoImage(Image.open("back_arrow.png").resize((15, 15)))
		self.h_backpagebtn3 = tk.Button(self.helpframe3, cursor='hand2', text="  Previous Page", image=self.h_backimg3, bg='#1f1f1f', fg='#57cade', compound='left', command=self.h_backpage3, relief='flat', font=h_pagefont3, overrelief='sunken')
		self.h_backpagebtn3.grid(row=0, column=0, padx=(0, 420), pady=(10, 10), ipadx=10, sticky='e')
		
		#self.h_nextimg3 = ImageTk.PhotoImage(Image.open("forward_arrow.png").resize((15, 15)))
		self.h_nextpagebtn3 = tk.Button(self.helpframe3, text="Next Page     ", bg='black', fg='black', command=self.donothing, relief='flat', font=h_pagefont3, activebackground='black')
		self.h_nextpagebtn3.grid(row=0, column=1, columnspan=2, padx=(40, 0), pady=(10, 10), ipadx=5, sticky='w')
		
		h_headfont3 = Font(size=30, underline=True)
		self.h_headlbl3 = tk.Label(self.helpframe3, text="Help & General Resources", bg='black', fg='#57cade', font=h_headfont3)
		self.h_headlbl3.grid(row=1, column=0, sticky='es', padx=(0, 20), pady=(30, 30))
		
		self.h_img3 = ImageTk.PhotoImage(Image.open("robot.png").resize((50, 50)))
		self.h_imglbl3 = tk.Label(self.helpframe3, image=self.h_img3, bg='black')
		self.h_imglbl3.image = self.h_img3
		self.h_imglbl3.grid(row=1, column=1, sticky='w', padx=(20, 0), pady=(30, 30))
		
		h_subheadfont3 = Font(size=20)
		self.h_finetunemsg3 = tk.Message(self.helpframe3, text="Fine Tuning", justify='left', bg='black', fg='#57cade', relief='flat', width=700, font=h_subheadfont3)
		self.h_finetunemsg3.grid(row=2, column=0, columnspan=2, pady=(0, 20), sticky='nesw')
		
		self.h_finetunetext3 = """Monitor Mode & Changes-\n*   Monitor mode will not bot for you. Monitor just listens in on Rucoy's conversation with the server and translates it to English.\n*   While it can be interesting, this can be used to 'Disable server switch time limit' or 'Set up store for 12+ hours'.\n*   Note: For disabling server switch limits, Rucoy Online must be restarted after the 'you must wait' message for it to work.\n\nSettings and Filter Menu-\n*   To the left, you can see the Settings Tab and the Filter Tab.\n*   Settings will let you affect how the bot runs and the Filter Menu will let you change what messages you see in the Console while the bot is running. Please open them for more information. """
		
		h_msgfont3 = Font(size=15)
		self.h_instructmsg3 = tk.Message(self.helpframe3, text=self.h_finetunetext3, justify='left', bg='black', fg='#57cade', relief='flat', width=700, font=h_msgfont3)
		self.h_instructmsg3.grid(row=3, column=0, columnspan=2, padx=(0, 0), pady=(0, 0), sticky='nesw')
		
		
		
		
		
		
		
		
		
		
		
		
		
		#This below is the frame for the Settings Tab
		self.settingsframe = tk.Frame(bg='black')
		
		#This below is the frame for the Devices Tab
		self.devicesframe = tk.Frame(bg='black')
		
		#This below is the frame for the Filters Tab
		self.filtersframe = tk.Frame(bg='black')
		
		#This below is the frame for the Settings Tab
		self.aboutframe = tk.Frame(bg='black')
		
		
		
		tk.Grid.columnconfigure(self, 1, weight=1)
		tk.Grid.rowconfigure(self, 8, weight=2)
		
		tk.Grid.columnconfigure(self.welcomeframe, 0, weight=1)
		tk.Grid.columnconfigure(self.welcomeframe, 1, weight=1)
		#tk.Grid.rowconfigure(self.welcomeframe, 8, weight=1)
		
		tk.Grid.columnconfigure(self.getstartframe, 0, weight=1)
		tk.Grid.columnconfigure(self.getstartframe, 1, weight=1)
		#tk.Grid.rowconfigure(self.getstartframe, 8, weight=1)
		
		#tk.Grid.columnconfigure(self.runmybotframe, 0, weight=1)
		tk.Grid.columnconfigure(self.runmybotframe, 1, weight=1)
		tk.Grid.columnconfigure(self.runmybotframe, 2, weight=1)
		#tk.Grid.columnconfigure(self.runmybotframe, 3, weight=1)
		#tk.Grid.rowconfigure(self.runmybotframe, 8, weight=1)
		
		#tk.Grid.columnconfigure(self.runmybotframe2, 0, weight=1)
		tk.Grid.columnconfigure(self.runmybotframe2, 1, weight=1)
		tk.Grid.columnconfigure(self.runmybotframe2, 2, weight=1)
		#tk.Grid.columnconfigure(self.runmybotframe2, 3, weight=1)
		#tk.Grid.rowconfigure(self.runmybotframe2, 8, weight=1)
		
		tk.Grid.columnconfigure(self.helpframe, 0, weight=1)
		tk.Grid.columnconfigure(self.helpframe, 1, weight=1)
		#tk.Grid.rowconfigure(self.helpframe, 8, weight=1)
		
		tk.Grid.columnconfigure(self.helpframe2, 0, weight=1)
		tk.Grid.columnconfigure(self.helpframe2, 1, weight=1)
		#tk.Grid.rowconfigure(self.helpframe2, 8, weight=1)
		
		tk.Grid.columnconfigure(self.helpframe3, 0, weight=1)
		tk.Grid.columnconfigure(self.helpframe3, 1, weight=1)
		#tk.Grid.rowconfigure(self.helpframe3, 8, weight=1)
		
		
		
	def welcome(self):
		self.welcomebtn.config(bg='#3f3f3f', fg='#57cade')
		self.getstartbtn.config(bg='#1f1f1f', fg='#57cade')
		self.runmybotbtn.config(bg='#1f1f1f', fg='#57cade')
		self.helpbtn.config(bg='#1f1f1f', fg='#57cade')
		self.settingsbtn.config(bg='#1f1f1f', fg='#57cade')
		self.devicesbtn.config(bg='#1f1f1f', fg='#57cade')
		self.filterbtn.config(bg='#1f1f1f', fg='#57cade')
		self.aboutbtn.config(bg='#1f1f1f', fg='#57cade')
		if self.activeframe == 'welcome':
			self.welcomeframe.grid_remove()
		if self.activeframe == 'getstart':
			self.getstartframe.grid_remove()
		if self.activeframe == 'runmybot':
			self.runmybotframe.grid_remove()
		if self.activeframe == 'runmybot2':
			self.runmybotframe2.grid_remove()
		if self.activeframe == 'help':
			self.helpframe.grid_remove()
		if self.activeframe == 'help2':
			self.helpframe2.grid_remove()
		if self.activeframe == 'help3':
			self.helpframe3.grid_remove()
		if self.activeframe == 'settings':
			self.settingsframe.grid_remove()
		if self.activeframe == 'devices':
			self.devicesframe.grid_remove()
		if self.activeframe == 'filters':
			self.filtersframe.grid_remove()
		if self.activeframe == 'about':
			self.aboutframe.grid_remove()
		self.activeframe = 'welcome'
		self.welcomeframe.grid(row=0, rowspan=50, column=1, sticky='nesw')
		
	
	def getstarted(self):
		self.welcomebtn.config(bg='#1f1f1f', fg='#57cade')
		self.getstartbtn.config(bg='#3f3f3f', fg='#57cade')
		self.runmybotbtn.config(bg='#1f1f1f', fg='#57cade')
		self.helpbtn.config(bg='#1f1f1f', fg='#57cade')
		self.settingsbtn.config(bg='#1f1f1f', fg='#57cade')
		self.devicesbtn.config(bg='#1f1f1f', fg='#57cade')
		self.filterbtn.config(bg='#1f1f1f', fg='#57cade')
		self.aboutbtn.config(bg='#1f1f1f', fg='#57cade')
		if self.activeframe == 'welcome':
			self.welcomeframe.grid_remove()
		if self.activeframe == 'getstart':
			self.getstartframe.grid_remove()
		if self.activeframe == 'runmybot':
			self.runmybotframe.grid_remove()
		if self.activeframe == 'runmybot2':
			self.runmybotframe2.grid_remove()
		if self.activeframe == 'help':
			self.helpframe.grid_remove()
		if self.activeframe == 'help2':
			self.helpframe2.grid_remove()
		if self.activeframe == 'help3':
			self.helpframe3.grid_remove()
		if self.activeframe == 'settings':
			self.settingsframe.grid_remove()
		if self.activeframe == 'devices':
			self.devicesframe.grid_remove()
		if self.activeframe == 'filters':
			self.filtersframe.grid_remove()
		if self.activeframe == 'about':
			self.aboutframe.grid_remove()
		self.activeframe = 'getstart'
		self.getstartframe.grid(row=0, rowspan=50, column=1, sticky='nesw')
		
	
	def runmybot(self):
		self.welcomebtn.config(bg='#1f1f1f', fg='#57cade')
		self.getstartbtn.config(bg='#1f1f1f', fg='#57cade')
		self.runmybotbtn.config(bg='#3f3f3f', fg='#57cade')
		self.helpbtn.config(bg='#1f1f1f', fg='#57cade')
		self.settingsbtn.config(bg='#1f1f1f', fg='#57cade')
		self.devicesbtn.config(bg='#1f1f1f', fg='#57cade')
		self.filterbtn.config(bg='#1f1f1f', fg='#57cade')
		self.aboutbtn.config(bg='#1f1f1f', fg='#57cade')
		if self.activeframe == 'welcome':
			self.welcomeframe.grid_remove()
		if self.activeframe == 'getstart':
			self.getstartframe.grid_remove()
		if self.activeframe == 'runmybot':
			self.runmybotframe.grid_remove()
		if self.activeframe == 'runmybot2':
			self.runmybotframe2.grid_remove()
		if self.activeframe == 'help':
			self.helpframe.grid_remove()
		if self.activeframe == 'help2':
			self.helpframe2.grid_remove()
		if self.activeframe == 'help3':
			self.helpframe3.grid_remove()
		if self.activeframe == 'settings':
			self.settingsframe.grid_remove()
		if self.activeframe == 'devices':
			self.devicesframe.grid_remove()
		if self.activeframe == 'filters':
			self.filtersframe.grid_remove()
		if self.activeframe == 'about':
			self.aboutframe.grid_remove()
		self.activeframe = 'runmybot'
		self.runmybotframe.grid(row=0, rowspan=50, column=1, sticky='nesw')
	
	def monitorplz(self):
		if self.botpower:
			sys.stderr.write('These settings cannot be changed until the bot is stopped.\n')
			return
		if self.botmode != 0:
			self.r_monimgbtn.config(bg="#49e0e3", image=self.r_monimg_active)
			self.r_monimgbtn.image = self.r_monimg_active
			self.botmode = 0
			self.r_huntimgbtn.config(bg='#1f1f1f', image=self.r_huntimg_disabled)
			self.r_huntimgbtn.image = self.r_huntimg_disabled
			self.r_farmimgbtn.config(bg='#1f1f1f', image=self.r_farmimg_disabled)
			self.r_farmimgbtn.image = self.r_farmimg_disabled
			self.r_skillimgbtn.config(bg='#1f1f1f', image=self.r_skillimg_disabled)
			self.r_skillimgbtn.image = self.r_skillimg_disabled
			
			self.weapon = 0
			self.hppot = 0
			self.mppot = 0
			
			self.swordimgbtn.config(bg='#1f1f1f', image=self.swordimg_n)
			self.swordimgbtn.image = self.swordimg_n
			self.bowimgbtn.config(bg='#1f1f1f', image=self.bowimg_n)
			self.bowimgbtn.image = self.bowimg_n
			self.wandimgbtn.config(bg='#1f1f1f', image=self.wandimg_n)
			self.wandimgbtn.image = self.wandimg_n
			
			self.mppotimgbtn.config(bg="#1f1f1f", image=self.mppotimg_n)
			self.mppotimgbtn.image = self.mppotimg_n
			self.hppotimgbtn.config(bg="#1f1f1f", image=self.hppotimg_n)
			self.hppotimgbtn.image = self.hppotimg_n
			
			
			
		
	def hunterplz(self):
		if self.botpower:
			sys.stderr.write('These settings cannot be changed until the bot is stopped.\n')
			return
		if self.botmode != 1:
			self.r_huntimgbtn.config(bg="#49e0e3", image=self.r_huntimg_active)
			self.r_huntimgbtn.image = self.r_huntimg_active
			self.botmode = 1
			self.r_monimgbtn.config(bg='#1f1f1f', image=self.r_monimg_disabled)
			self.r_monimgbtn.image = self.r_monimg_disabled
			self.r_farmimgbtn.config(bg='#1f1f1f', image=self.r_farmimg_disabled)
			self.r_farmimgbtn.image = self.r_farmimg_disabled
			self.r_skillimgbtn.config(bg='#1f1f1f', image=self.r_skillimg_disabled)
			self.r_skillimgbtn.image = self.r_skillimg_disabled
			
			self.weapon = 1
			self.hppot = 0
			self.mppot = 0
			self.swordplz()
			self.hppotplz()
			self.mppotplz()
		
	def farmerplz(self):
		if self.botpower:
			sys.stderr.write('These settings cannot be changed until the bot is stopped.\n')
			return
		if self.botmode != 2:
			self.r_farmimgbtn.config(bg="#49e0e3", image=self.r_farmimg_active)
			self.r_farmimgbtn.image = self.r_farmimg_active
			self.botmode = 2
			self.r_monimgbtn.config(bg='#1f1f1f', image=self.r_monimg_disabled)
			self.r_monimgbtn.image = self.r_monimg_disabled
			self.r_huntimgbtn.config(bg='#1f1f1f', image=self.r_huntimg_disabled)
			self.r_huntimgbtn.image = self.r_huntimg_disabled
			self.r_skillimgbtn.config(bg='#1f1f1f', image=self.r_skillimg_disabled)
			self.r_skillimgbtn.image = self.r_skillimg_disabled
			
			self.weapon = 1
			self.hppot = 0
			self.mppot = 0
			self.swordplz()
			self.hppotplz()
			self.mppotplz()
		
	def skillerplz(self):
		if self.botpower:
			sys.stderr.write('These settings cannot be changed until the bot is stopped.\n')
			return
		if self.botmode != 3:
			self.r_skillimgbtn.config(bg="#49e0e3", image=self.r_skillimg_active)
			self.r_skillimgbtn.image = self.r_skillimg_active
			self.botmode = 3
			self.r_monimgbtn.config(bg='#1f1f1f', image=self.r_monimg_disabled)
			self.r_monimgbtn.image = self.r_monimg_disabled
			self.r_huntimgbtn.config(bg='#1f1f1f', image=self.r_huntimg_disabled)
			self.r_huntimgbtn.image = self.r_huntimg_disabled
			self.r_farmimgbtn.config(bg='#1f1f1f', image=self.r_farmimg_disabled)
			self.r_farmimgbtn.image = self.r_farmimg_disabled
			
			self.weapon = 1
			self.hppot = 0
			self.mppot = 0
			self.swordplz()
			self.hppotplz()
			self.mppotplz()
	
	def swordplz(self, bypass=False):
		#Make sure bot mode is any mode other than monitor and sword is not already selected.
		if self.botpower and bypass == False:
			sys.stderr.write('These settings cannot be changed until the bot is stopped.\n')
			return
		if self.botmode != 0 and self.weapon != 0:
			self.weapon = 0
			self.bowimgbtn.config(bg='#1f1f1f', image=self.bowimg_n)
			self.bowimgbtn.image = self.bowimg_n
			self.wandimgbtn.config(bg='#1f1f1f', image=self.wandimg_n)
			self.wandimgbtn.image = self.wandimg_n
			if self.botmode != 3:
				#Code for showing color swords if bot mode is other than training mode.
				if self.tier == 1:
					self.swordimgbtn.config(bg="#49e0e3", image=self.swordimg_1)
					self.swordimgbtn.image = self.swordimg_1
				elif self.tier == 2:
					self.swordimgbtn.config(bg="#49e0e3", image=self.swordimg_2)
					self.swordimgbtn.image = self.swordimg_2
				elif self.tier == 3:
					self.swordimgbtn.config(bg="#49e0e3", image=self.swordimg_3)
					self.swordimgbtn.image = self.swordimg_3
				elif self.tier == 4:
					self.swordimgbtn.config(bg="#49e0e3", image=self.swordimg_4)
					self.swordimgbtn.image = self.swordimg_4
				elif self.tier == 5:
					self.swordimgbtn.config(bg="#49e0e3", image=self.swordimg_5)
					self.swordimgbtn.image = self.swordimg_5
				elif self.tier == 6:
					self.swordimgbtn.config(bg="#49e0e3", image=self.swordimg_6)
					self.swordimgbtn.image = self.swordimg_6
				elif self.tier == 7:
					self.swordimgbtn.config(bg="#49e0e3", image=self.swordimg_7)
					self.swordimgbtn.image = self.swordimg_7
			else:
				self.swordimgbtn.config(bg="#49e0e3", image=self.swordimg_t)
				self.swordimgbtn.image = self.swordimg_t
				
		
	def bowplz(self, bypass=False):
		#Make sure bot mode is any mode other than monitor and sword is not already selected.
		if self.botpower and bypass == False:
			sys.stderr.write('These settings cannot be changed until the bot is stopped.\n')
			return
		if self.botmode != 0 and self.weapon != 1:
			self.weapon = 1
			self.swordimgbtn.config(bg='#1f1f1f', image=self.swordimg_n)
			self.swordimgbtn.image = self.swordimg_n
			self.wandimgbtn.config(bg='#1f1f1f', image=self.wandimg_n)
			self.wandimgbtn.image = self.wandimg_n
			if self.botmode != 3:
				#Code for showing color bows if bot mode is other than training mode.
				if self.tier == 1:
					self.bowimgbtn.config(bg="#49e0e3", image=self.bowimg_1)
					self.bowimgbtn.image = self.bowimg_1
				elif self.tier == 2:
					self.bowimgbtn.config(bg="#49e0e3", image=self.bowimg_2)
					self.bowimgbtn.image = self.bowimg_2
				elif self.tier == 3:
					self.bowimgbtn.config(bg="#49e0e3", image=self.bowimg_3)
					self.bowimgbtn.image = self.bowimg_3
				elif self.tier == 4:
					self.bowimgbtn.config(bg="#49e0e3", image=self.bowimg_4)
					self.bowimgbtn.image = self.bowimg_4
				elif self.tier == 5:
					self.bowimgbtn.config(bg="#49e0e3", image=self.bowimg_5)
					self.bowimgbtn.image = self.bowimg_5
				elif self.tier == 6:
					self.bowimgbtn.config(bg="#49e0e3", image=self.bowimg_6)
					self.bowimgbtn.image = self.bowimg_6
				elif self.tier == 7:
					self.bowimgbtn.config(bg="#49e0e3", image=self.bowimg_7)
					self.bowimgbtn.image = self.bowimg_7
			else:
				self.bowimgbtn.config(bg="#49e0e3", image=self.bowimg_t)
				self.bowimgbtn.image = self.bowimg_t
			
	def wandplz(self, bypass=False):
		#Make sure bot mode is any mode other than monitor and sword is not already selected.
		if self.botpower and bypass == False:
			sys.stderr.write('These settings cannot be changed until the bot is stopped.\n')
			return
		if self.botmode != 0 and self.weapon != 2:
			self.weapon = 2
			self.swordimgbtn.config(bg='#1f1f1f', image=self.swordimg_n)
			self.swordimgbtn.image = self.swordimg_n
			self.bowimgbtn.config(bg='#1f1f1f', image=self.bowimg_n)
			self.bowimgbtn.image = self.bowimg_n
			if self.botmode != 3:
				#Code for showing color wands if bot mode is other than training mode.
				if self.tier == 1:
					self.wandimgbtn.config(bg="#49e0e3", image=self.wandimg_1)
					self.wandimgbtn.image = self.wandimg_1
				elif self.tier == 2:
					self.wandimgbtn.config(bg="#49e0e3", image=self.wandimg_2)
					self.wandimgbtn.image = self.wandimg_2
				elif self.tier == 3:
					self.wandimgbtn.config(bg="#49e0e3", image=self.wandimg_3)
					self.wandimgbtn.image = self.wandimg_3
				elif self.tier == 4:
					self.wandimgbtn.config(bg="#49e0e3", image=self.wandimg_4)
					self.wandimgbtn.image = self.wandimg_4
				elif self.tier == 5:
					self.wandimgbtn.config(bg="#49e0e3", image=self.wandimg_5)
					self.wandimgbtn.image = self.wandimg_5
				elif self.tier == 6:
					self.wandimgbtn.config(bg="#49e0e3", image=self.wandimg_6)
					self.wandimgbtn.image = self.wandimg_6
				elif self.tier == 7:
					self.wandimgbtn.config(bg="#49e0e3", image=self.wandimg_7)
					self.wandimgbtn.image = self.wandimg_7
			else:
				self.wandimgbtn.config(bg="#49e0e3", image=self.wandimg_t)
				self.wandimgbtn.image = self.wandimg_t
	
	def update_servlist(self):
		try:
			self.all_servers = ['Any Server']
			self.servjson = self.get_jsonparsed_data("https://www.rucoyonline.com/server_list.json")
			for a in self.servjson.get('servers'):
				if a.get('visible'):
					info = '{} - {}'.format(a.get('name'), a.get('characters_online'))
					self.all_servers.append(info)
			self.all_servers = sorted(self.all_servers)
			if self.server_options.get() != '':
				for item in self.all_servers:
					if item.startswith(self.server_options.get()):
						self.server_options.set(item)
			else:
				self.server_options.set(self.all_servers[0])
			#Finish setting up widgets with data now obtained from the internet.
			#self.servoptdd.grid_remove()
			#self.servoptdd.grid(row=4, column=2, pady=(5, 0), sticky='w')
		except:
			self.servjson = 'failed'
			self.all_servers = ['Network Failure']
			self.server_options.set(self.all_servers[0])
	
	def get_jsonparsed_data(self, url):
		response = urlopen(url, timeout=5)
		data = response.read().decode("utf-8")
		return json.loads(data)
	
	def r_nextpage(self):
		self.activeframe = 'runmybot2'
		self.runmybotframe.grid_remove()
		self.runmybotframe2.grid(row=0, rowspan=50, column=1, sticky='nesw')
	
	def r_nextpage2(self):
		pass
	
	def hppotplz(self, bypass=False):
		#Make sure bot mode is any mode other than monitor and hppot is not already selected.
		if self.botpower and bypass == False:
			sys.stderr.write('These settings cannot be changed until the bot is stopped.\n')
			return
		if self.botmode != 0:
			if self.hppot == 0:
				self.hppot = 1
				if self.pottier == 1:
					self.hppotimgbtn.config(bg="#49e0e3", image=self.hppotimg_1)
					self.hppotimgbtn.image = self.hppotimg_1
				elif self.pottier == 2:
					self.hppotimgbtn.config(bg="#49e0e3", image=self.hppotimg_2)
					self.hppotimgbtn.image = self.hppotimg_2
				elif self.pottier == 3:
					self.hppotimgbtn.config(bg="#49e0e3", image=self.hppotimg_3)
					self.hppotimgbtn.image = self.hppotimg_3
			else:
				self.hppot = 0
				self.hppotimgbtn.config(bg="#1f1f1f", image=self.hppotimg_n)
				self.hppotimgbtn.image = self.hppotimg_n
				
	def mppotplz(self, bypass=False):
		#Make sure bot mode is any mode other than monitor and mppot is not already selected.
		if self.botpower and bypass == False:
			sys.stderr.write('These settings cannot be changed until the bot is stopped.\n')
			return
		if self.botmode != 0:
			if self.mppot == 0:
				self.mppot = 1
				if self.pottier == 1:
					self.mppotimgbtn.config(bg="#49e0e3", image=self.mppotimg_1)
					self.mppotimgbtn.image = self.mppotimg_1
				elif self.pottier == 2:
					self.mppotimgbtn.config(bg="#49e0e3", image=self.mppotimg_2)
					self.mppotimgbtn.image = self.mppotimg_2
				elif self.pottier == 3:
					self.mppotimgbtn.config(bg="#49e0e3", image=self.mppotimg_3)
					self.mppotimgbtn.image = self.mppotimg_3
			else:
				self.mppot = 0
				self.mppotimgbtn.config(bg="#1f1f1f", image=self.mppotimg_n)
				self.mppotimgbtn.image = self.mppotimg_n
	
	def help(self):
		self.welcomebtn.config(bg='#1f1f1f', fg='#57cade')
		self.getstartbtn.config(bg='#1f1f1f', fg='#57cade')
		self.runmybotbtn.config(bg='#1f1f1f', fg='#57cade')
		self.helpbtn.config(bg='#3f3f3f', fg='#57cade')
		self.settingsbtn.config(bg='#1f1f1f', fg='#57cade')
		self.devicesbtn.config(bg='#1f1f1f', fg='#57cade')
		self.filterbtn.config(bg='#1f1f1f', fg='#57cade')
		self.aboutbtn.config(bg='#1f1f1f', fg='#57cade')
		if self.activeframe == 'welcome':
			self.welcomeframe.grid_remove()
		if self.activeframe == 'getstart':
			self.getstartframe.grid_remove()
		if self.activeframe == 'runmybot':
			self.runmybotframe.grid_remove()
		if self.activeframe == 'runmybot2':
			self.runmybotframe2.grid_remove()
		if self.activeframe == 'help':
			self.helpframe.grid_remove()
		if self.activeframe == 'help2':
			self.helpframe2.grid_remove()
		if self.activeframe == 'help3':
			self.helpframe3.grid_remove()
		if self.activeframe == 'settings':
			self.settingsframe.grid_remove()
		if self.activeframe == 'devices':
			self.devicesframe.grid_remove()
		if self.activeframe == 'filters':
			self.filtersframe.grid_remove()
		if self.activeframe == 'about':
			self.aboutframe.grid_remove()
		self.activeframe = 'help'
		self.helpframe.grid(row=0, rowspan=50, column=1, sticky='nesw')
	
	def h_nextpage(self):
		self.activeframe = 'help2'
		self.helpframe.grid_remove()
		self.helpframe2.grid(row=0, rowspan=50, column=1, sticky='nesw')
	
	def h_nextpage2(self):
		self.activeframe = 'help3'
		self.helpframe2.grid_remove()
		self.helpframe3.grid(row=0, rowspan=50, column=1, sticky='nesw')
	
	def h_backpage2(self):
		self.activeframe = 'help'
		self.helpframe2.grid_remove()
		self.helpframe.grid(row=0, rowspan=50, column=1, sticky='nesw')
	
	def h_backpage3(self):
		self.activeframe = 'help2'
		self.helpframe3.grid_remove()
		self.helpframe2.grid(row=0, rowspan=50, column=1, sticky='nesw')
	
	def settings(self):
		self.welcomebtn.config(bg='#1f1f1f', fg='#57cade')
		self.getstartbtn.config(bg='#1f1f1f', fg='#57cade')
		self.runmybotbtn.config(bg='#1f1f1f', fg='#57cade')
		self.helpbtn.config(bg='#1f1f1f', fg='#57cade')
		self.settingsbtn.config(bg='#3f3f3f', fg='#57cade')
		self.devicesbtn.config(bg='#1f1f1f', fg='#57cade')
		self.filterbtn.config(bg='#1f1f1f', fg='#57cade')
		self.aboutbtn.config(bg='#1f1f1f', fg='#57cade')
		if self.activeframe == 'welcome':
			self.welcomeframe.grid_remove()
		if self.activeframe == 'getstart':
			self.getstartframe.grid_remove()
		if self.activeframe == 'runmybot':
			self.runmybotframe.grid_remove()
		if self.activeframe == 'runmybot2':
			self.runmybotframe2.grid_remove()
		if self.activeframe == 'help':
			self.helpframe.grid_remove()
		if self.activeframe == 'help2':
			self.helpframe2.grid_remove()
		if self.activeframe == 'help3':
			self.helpframe3.grid_remove()
		if self.activeframe == 'settings':
			self.settingsframe.grid_remove()
		if self.activeframe == 'devices':
			self.devicesframe.grid_remove()
		if self.activeframe == 'filters':
			self.filtersframe.grid_remove()
		if self.activeframe == 'about':
			self.aboutframe.grid_remove()
		self.activeframe = 'settings'
		self.settingsframe.grid(row=0, rowspan=50, column=1, sticky='nesw')
	
	def devices(self):
		self.welcomebtn.config(bg='#1f1f1f', fg='#57cade')
		self.getstartbtn.config(bg='#1f1f1f', fg='#57cade')
		self.runmybotbtn.config(bg='#1f1f1f', fg='#57cade')
		self.helpbtn.config(bg='#1f1f1f', fg='#57cade')
		self.settingsbtn.config(bg='#1f1f1f', fg='#57cade')
		self.devicesbtn.config(bg='#3f3f3f', fg='#57cade')
		self.filterbtn.config(bg='#1f1f1f', fg='#57cade')
		self.aboutbtn.config(bg='#1f1f1f', fg='#57cade')
		if self.activeframe == 'welcome':
			self.welcomeframe.grid_remove()
		if self.activeframe == 'getstart':
			self.getstartframe.grid_remove()
		if self.activeframe == 'runmybot':
			self.runmybotframe.grid_remove()
		if self.activeframe == 'runmybot2':
			self.runmybotframe2.grid_remove()
		if self.activeframe == 'help':
			self.helpframe.grid_remove()
		if self.activeframe == 'help2':
			self.helpframe2.grid_remove()
		if self.activeframe == 'help3':
			self.helpframe3.grid_remove()
		if self.activeframe == 'settings':
			self.settingsframe.grid_remove()
		if self.activeframe == 'devices':
			self.devicesframe.grid_remove()
		if self.activeframe == 'filters':
			self.filtersframe.grid_remove()
		if self.activeframe == 'about':
			self.aboutframe.grid_remove()
		self.activeframe = 'devices'
		self.devicesframe.grid(row=0, rowspan=50, column=1, sticky='nesw')
	
	def filters(self):
		self.welcomebtn.config(bg='#1f1f1f', fg='#57cade')
		self.getstartbtn.config(bg='#1f1f1f', fg='#57cade')
		self.runmybotbtn.config(bg='#1f1f1f', fg='#57cade')
		self.helpbtn.config(bg='#1f1f1f', fg='#57cade')
		self.settingsbtn.config(bg='#1f1f1f', fg='#57cade')
		self.devicesbtn.config(bg='#1f1f1f', fg='#57cade')
		self.filterbtn.config(bg='#3f3f3f', fg='#57cade')
		self.aboutbtn.config(bg='#1f1f1f', fg='#57cade')
		if self.activeframe == 'welcome':
			self.welcomeframe.grid_remove()
		if self.activeframe == 'getstart':
			self.getstartframe.grid_remove()
		if self.activeframe == 'runmybot':
			self.runmybotframe.grid_remove()
		if self.activeframe == 'runmybot2':
			self.runmybotframe2.grid_remove()
		if self.activeframe == 'help':
			self.helpframe.grid_remove()
		if self.activeframe == 'help2':
			self.helpframe2.grid_remove()
		if self.activeframe == 'help3':
			self.helpframe3.grid_remove()
		if self.activeframe == 'settings':
			self.settingsframe.grid_remove()
		if self.activeframe == 'devices':
			self.devicesframe.grid_remove()
		if self.activeframe == 'filters':
			self.filtersframe.grid_remove()
		if self.activeframe == 'about':
			self.aboutframe.grid_remove()
		self.activeframe = 'filters'
		self.filtersframe.grid(row=0, rowspan=50, column=1, sticky='nesw')
	
	def about(self):
		self.welcomebtn.config(bg='#1f1f1f', fg='#57cade')
		self.getstartbtn.config(bg='#1f1f1f', fg='#57cade')
		self.runmybotbtn.config(bg='#1f1f1f', fg='#57cade')
		self.helpbtn.config(bg='#1f1f1f', fg='#57cade')
		self.settingsbtn.config(bg='#1f1f1f', fg='#57cade')
		self.devicesbtn.config(bg='#1f1f1f', fg='#57cade')
		self.filterbtn.config(bg='#1f1f1f', fg='#57cade')
		self.aboutbtn.config(bg='#3f3f3f', fg='#57cade')
		if self.activeframe == 'welcome':
			self.welcomeframe.grid_remove()
		if self.activeframe == 'getstart':
			self.getstartframe.grid_remove()
		if self.activeframe == 'runmybot':
			self.runmybotframe.grid_remove()
		if self.activeframe == 'runmybot2':
			self.runmybotframe2.grid_remove()
		if self.activeframe == 'help':
			self.helpframe.grid_remove()
		if self.activeframe == 'help2':
			self.helpframe2.grid_remove()
		if self.activeframe == 'help3':
			self.helpframe3.grid_remove()
		if self.activeframe == 'settings':
			self.settingsframe.grid_remove()
		if self.activeframe == 'devices':
			self.devicesframe.grid_remove()
		if self.activeframe == 'filters':
			self.filtersframe.grid_remove()
		if self.activeframe == 'about':
			self.aboutframe.grid_remove()
		self.activeframe = 'about'
		self.aboutframe.grid(row=0, rowspan=50, column=1, sticky='nesw')
	
	def on_closing(self):
		self.destroy()
	
	def donothing(self):
		pass


if __name__ == "__main__":
	freeze_support()
	
	app = RucoyGui()
	app.configure(background="black")
	app.protocol("WM_DELETE_WINDOW", app.on_closing)
	app.iconbitmap('robot.ico')
	#app.resizable(False, False)
	app.title(" Rucoy Bot")
	app.minsize(1000, 600)
	app.mainloop()