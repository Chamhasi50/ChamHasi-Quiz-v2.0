import customtkinter as ck
from tkinter import *
from tkinter import messagebox as msg
import json
from datetime import datetime
import emoji

with open('Questions.json') as Questions_file:
  data = json.load(Questions_file)

acronym_ques = (data['Acronym_questions'])
acronym_ans = (data['Acronym_answer'])
acronym_opt = (data['Acronym_option'])

animation_ques = (data['Animation_questions'])
animation_ans = (data['Animation_answer'])
animation_opt = (data['Animation_option'])

computer_ques = (data['Computer_questions'])
computer_ans = (data['Computer_answer'])
computer_opt = (data['Computer_option'])

program_ques = (data['Programming_questions'])
program_ans = (data['Programming_answer'])
program_opt = (data['Programming_option'])

it_ques = (data['It_questions'])
it_ans = (data['It_answer'])
it_opt = (data['It_option'])

reli_ques = (data['Religion_questions'])
reli_ans = (data['Religion_answer'])
reli_opt = (data['Religion_option'])


class Quiz_Game(ck.CTk):
  def __init__(self):
    super().__init__()
    self.title("Cham Quize Game")
    self.geometry("1000x500+350+250")
    self.iconbitmap('Cham.ico')
    self.config(background='#313440')
    self.resizable(False, False)

    self.new_user = []

    # ------------------------------ The main frames.
    self.start_frame = ck.CTkFrame(self, width=990, height=490, bg_color='#313440', fg_color='#313440', border_width=1, border_color='royalblue')
    self.register_frame = ck.CTkFrame(self, width=340, height=150, bg_color='#313440', fg_color='#313440', border_width=1, border_color='royalblue')
    self.game_frame = ck.CTkFrame(self, width=990, height=490, bg_color='#313440', fg_color='#313440', border_width=1, border_color='royalblue')

    # ------------------------------ The begning window.
    label1 = ck.CTkLabel(self.start_frame, text='WELCOME TO CHAM QUIZ GAME', font=('Helvetica', 50, 'bold','underline'), fg_color='#313440', bg_color='#313440').place(x=100, y=50)

    label2 = ck.CTkLabel(self.start_frame, text='Before starting, you have to know that this game is completely free and OPEN-SOURCE.\nTherefore, selling it or using it to earn money is not allowed, so be aware.\nFor more information or free games you can visit us on our website :\nwww.chamsoudine.com OR chamsoudine50@gmail.com\n\n\nThank you for visiting us in advance !', font=('Helvetica', 20, 'bold'), fg_color='#313440', bg_color='#313440').place(x=80, y=160)

    start_button = ck.CTkButton(self.start_frame, text='Start The Game', width=600, height=50, font=('Helvetica', 20, 'bold'), fg_color='royalblue', bg_color='#313440', hover_color='#313440', border_width=1, border_color='#fff', command=self.register_window).place(x=200, y=400)

    self.start_frame.place(x=5, y=5)

    # ------------------------------ The registration window.
    regis_label = ck.CTkLabel(self.register_frame, text="Registration", font=("Helvetica", 25, 'bold'), fg_color="#313440", bg_color="#313440").place(x=95, y=10)

    self.user_name = ck.CTkEntry(self.register_frame, width=320, height=40, font=("Helvetica", 15, "bold"), placeholder_text="Enter Your Fullname", fg_color="#313440", bg_color="#313440", border_width=1, border_color="royalblue")
    self.user_name.place(x=10, y=50)

    regis_button = ck.CTkButton(self.register_frame, width=320, height=40, text="Register", font=("Helvetica", 15, "bold"), fg_color="royalblue", bg_color="#313440", hover_color="#313440", border_width=1, border_color="#fff", command=self.game_window).place(x=10, y=100)

    # ------------------------------ The Game manu.
    title = ck.CTkLabel(self.game_frame, text=(f'Welcome to CHAM Quiz. \nMake your choice to start the game.'), font=('Helvetica', 45, 'bold', 'underline'), fg_color="#313440", bg_color="#313440").place(x=120, y=20)

    acronym_btn = ck.CTkButton(self.game_frame, width=310, height=70, text="Acronym", font=("Helvetica", 20, "bold"), fg_color="#5662f6", bg_color="#313440", hover_color="#313440", border_width=1, border_color="#fff", command=self.Acronym_window).place(x=10, y=180)

    manga_btn = ck.CTkButton(self.game_frame, width=310, height=70, text="Manga", font=("Helvetica", 20, "bold"), fg_color="#5662f6", bg_color="#313440", hover_color="#313440", border_width=1, border_color="#fff", command=self.Manga_window).place(x=338, y=180)

    it_btn = ck.CTkButton(self.game_frame, width=310, height=70, text="Information Technology", font=("Helvetica", 20, "bold"), fg_color="#5662f6", bg_color="#313440", hover_color="#313440", border_width=1, border_color="#fff", command=self.Information_technology_window).place(x=668, y=180)

    program_btn = ck.CTkButton(self.game_frame, width=310, height=70, text="Programing", font=("Helvetica", 20, "bold"), fg_color="#5662f6", bg_color="#313440", hover_color="#313440", border_width=1, border_color="#fff", command=self.Programming_window).place(x=10, y=280)

    computer_btn = ck.CTkButton(self.game_frame, width=310, height=70, text="Computer", font=("Helvetica", 20, "bold"), fg_color="#5662f6", bg_color="#313440", hover_color="#313440", border_width=1, border_color="#fff", command=self.Computer_window).place(x=338, y=280)

    religion_btn = ck.CTkButton(self.game_frame, width=310, height=70, text="Religion", font=("Helvetica", 20, "bold"), fg_color="#5662f6", bg_color="#313440", hover_color="#313440", border_width=1, border_color="#fff", command=self.Religion_window).place(x=668, y=280)

    about_btn = ck.CTkButton(self.game_frame, width=310, height=70, text="About", font=("Helvetica", 20, "bold"), fg_color="#ffa500", bg_color="#313440", hover_color="#313440", border_width=1, border_color="#fff", command=self.about).place(x=338, y=380)

    exit_btn = ck.CTkButton(self.game_frame, width=310, height=70, text="Exit Game", font=("Helvetica", 20, "bold"), fg_color="#fc3c44", bg_color="#313440", hover_color="#313440", border_width=1, border_color="#fff", command=self.close_game).place(x=668, y=380)


  def close_game(self):
    self.destroy()


  def window(self):
    self.iconbitmap('Cham.ico')
    self.geometry("1000x500+350+250")
    self.config(background='#313440')
    self.resizable(False, False)

  
  def about(self):
    msg.showinfo("About","CHAM QUIZ is an OPEN-SOURCE Game developed by Chamsoudine Boubacar known as Cham50. The version of this application is v2.0, and it was released to the public on monday 2021/09/06.\n\nFor more information please consider visiting our website www.chamsoudine.com. Thanks!")


  def game_window(self):
    self.start_frame.place_forget()
    self.register_frame.place_forget()
    self.user = self.user_name.get()

    if self.user == '':
      msg.showwarning("Warning","Please Enter your fullname to start the game. Thanks")
      self.register_frame.place(x=5, y=5)
    else:
      self.new_user.append(self.user)
      msg.showinfo("Success",f"{self.user} is registed successfully, you can now start the game.")
      self.window()
      self.user_name.delete(0, END)
      self.game_frame.place(x=5, y=5)


  def register_window(self):
    self.start_frame.place_forget()
    self.iconbitmap('Cham.ico')
    self.geometry("350x160+700+400")
    self.config(background='#313440')
    self.resizable(False, False)
    self.register_frame.place(x=5, y=5)


  def Acronym_window(self):
    self.win = Toplevel()
    self.win.title('Acronym')
    self.win.iconbitmap('Cham.ico')
    self.win.geometry('1000x500+350+250')
    self.win.config(background="#313440")
    self.win.resizable(False, False)

    # ------------------------------ The main window frame.
    self.warning_frame = ck.CTkFrame(self.win, width=990, height=490, bg_color='#313440', fg_color='#313440', border_width=1, border_color='royalblue')
    
    # ------------------------------ The questions frame.
    self.quiz_frame = ck.CTkFrame(self.win, width=990, height=490, bg_color='#313440', fg_color='#313440', border_width=1, border_color='royalblue')
    self.up_frame = ck.CTkFrame(self.quiz_frame, width=980, height=40, bg_color='#313440', fg_color='royalblue', border_width=1, border_color='royalblue')
    
    # ------------------------------ The start quiz elements.
    warning_title_label = ck.CTkLabel(self.warning_frame, text=emoji.emojize(':warning: ACORNYM QUIZ WARNING :warning:'), font=('Helvetica', 50, 'bold'), fg_color='#313440', bg_color='#313440').place(x=105, y=50)
    warning_info_label = ck.CTkLabel(self.warning_frame, text="Dear User. This is a friendly reminder that an important task is currently in progress within this \napplication window. Closing the window prematurely may result in the loss of unsaved \ndata or incomplete actions.\n\nTo ensure a seamless experience and to avoid any potential data loss, please refrain from closing \nthe app window until the task is successfully completed. If you encounter any issues \nor have questions, feel free to reach out to our support team for assistance.\n\nThank you for your understanding and collaboration.", font=('Helvetica', 20, 'bold'), fg_color='#313440', bg_color='#313440').place(x=30, y=160)
    
    start_button = ck.CTkButton(self.warning_frame, text='Start The Quiz', width=600, height=50, font=('Helvetica', 20, 'bold'), fg_color='royalblue', bg_color='#313440', hover_color='#313440', border_width=1, border_color='#fff', command=lambda:Acronym_quiz_window()).place(x=200, y=400)
    
    self.warning_frame.place(x=5, y=5)

    # ------------------------------ The up frame items.
    time = datetime.now()
    now = time.date()
    player_name = ck.CTkLabel(self.up_frame, text=f"Player: {self.user}", font=("Helvetica",17,"bold")).place(x=10, y=5)
    bar_lab = ck.CTkLabel(self.up_frame, text=f" | ", font=("Helvetica",17,"bold")).place(x=380, y=5)
    player_section = ck.CTkLabel(self.up_frame, text="Section: Acronym", font=("Helvetica",17,"bold")).place(x=420, y=5)
    bar_lab = ck.CTkLabel(self.up_frame, text=f" | ", font=("Helvetica",17,"bold")).place(x=600, y=5)
    player_level = ck.CTkLabel(self.up_frame, text="Questions N°: 1", font=("Helvetica",17,"bold")).place(x=640, y=5)
    bar_lab = ck.CTkLabel(self.up_frame, text=f" | ", font=("Helvetica",17,"bold")).place(x=805, y=5)
    current_time = ck.CTkLabel(self.up_frame, text=f"Date: {now}", font=("Helvetica",15,"bold")).place(x=850, y=5)
    

    def Acronym_quiz_window():
      self.up_frame.place(x=5, y=15)
      self.quiz_frame.place(x=5, y=5)


    def acro_display_result():
      wrong_count = self.data_size - self.correct
      correct = f"Correct Answers: {self.correct}"
      wrong = f"Wrong Answers: {wrong_count}"

      score = int(self.correct / self.data_size * 100)
      result = f"Total Score: {score}%"

      msg.showinfo("Result", f"{result}\n{correct}\n{wrong}")


    def acro_check_ans(acro_ques_no):
      if self.opt_selected.get() == acronym_ans[acro_ques_no]:
        return True


    def acro_next_btn():
      if acro_check_ans(self.acro_ques_no):
        self.correct += 1

      self.acro_ques_no += 1
      if self.acro_ques_no == self.data_size:
        acro_display_result()
        self.win.destroy()
      else:
        acro_display_question()
        acro_display_options()


    def acro_display_options():
      val = 0
      self.opt_selected.set(0)
      for option in acronym_opt[self.acro_ques_no]:
        self.opts[val]['text'] = option
        val += 1


    def acro_display_question():
      question_label = ck.CTkLabel(self.quiz_frame, width=820, text = acronym_ques[self.acro_ques_no], font=("Helvetica", 30, "bold"), text_color="#fff")
      question_label.place(x=50, y=100)


    def acro_radio_buttons():
      acro_ques_list = []
      y_pos = 190
      while len(acro_ques_list) < 4:
        radio_btn = Radiobutton(self.quiz_frame, text=" ", variable=self.opt_selected, value = len(acro_ques_list)+1, font=("Helvetica",20, 'bold'), bg="#313440", fg="white", activebackground="#3399ff", activeforeground="white", selectcolor="#313440", padx=10)
        acro_ques_list.append(radio_btn)
        radio_btn.place(x=140, y=y_pos)
        y_pos += 60
      return acro_ques_list


    self.acro_ques_no = 0
    acro_display_question()
    self.opt_selected = IntVar()
    self.opts = acro_radio_buttons()
    acro_display_options()
    self.data_size = len(acronym_ques)
    self.correct = 0

    next_btn = ck.CTkButton(self.quiz_frame, text='Next', width=150, height=40, font=('Helvetica', 20, 'bold'), fg_color='royalblue', bg_color='#313440', hover_color='#313440', border_width=1, border_color='#fff', command=acro_next_btn)
    next_btn.place(x=830, y=440)


  def Manga_window(self):
    self.win = Toplevel()
    self.win.title('Manga')
    self.win.iconbitmap('Cham.ico')
    self.win.geometry('1000x500+350+250')
    self.win.config(background="#313440")
    self.win.resizable(False, False)

    # ------------------------------ The main window frame..
    self.warning_frame = ck.CTkFrame(self.win, width=990, height=490, bg_color='#313440', fg_color='#313440', border_width=1, border_color='royalblue')
    
    # ------------------------------ The questions frame.
    self.quiz_frame = ck.CTkFrame(self.win, width=990, height=490, bg_color='#313440', fg_color='#313440', border_width=1, border_color='royalblue')
    self.up_frame = ck.CTkFrame(self.quiz_frame, width=980, height=40, bg_color='#313440', fg_color='royalblue', border_width=1, border_color='royalblue')
    
    # ------------------------------ The start quiz elements.
    warning_title_label = ck.CTkLabel(self.warning_frame, text=emoji.emojize(':warning: MANGA QUIZ WARNING :warning:'), font=('Helvetica', 50, 'bold'), fg_color='#313440', bg_color='#313440').place(x=145, y=50)
    warning_info_label = ck.CTkLabel(self.warning_frame, text="Dear User. This is a friendly reminder that an important task is currently in progress within this \napplication window. Closing the window prematurely may result in the loss of unsaved \ndata or incomplete actions.\n\nTo ensure a seamless experience and to avoid any potential data loss, please refrain from closing \nthe app window until the task is successfully completed. If you encounter any issues \nor have questions, feel free to reach out to our support team for assistance.\n\nThank you for your understanding and collaboration.", font=('Helvetica', 20, 'bold'), fg_color='#313440', bg_color='#313440').place(x=30, y=160)
    
    start_button = ck.CTkButton(self.warning_frame, text='Start The Quiz', width=600, height=50, font=('Helvetica', 20, 'bold'), fg_color='royalblue', bg_color='#313440', hover_color='#313440', border_width=1, border_color='#fff', command=lambda:Manga_quiz_window()).place(x=200, y=400)
    
    self.warning_frame.place(x=5, y=5)

    # ------------------------------ The up frame items.
    time = datetime.now()
    now = time.date()
    player_name = ck.CTkLabel(self.up_frame, text=f"Player: {self.user}", font=("Helvetica",17,"bold")).place(x=10, y=5)
    bar_lab = ck.CTkLabel(self.up_frame, text=f" | ", font=("Helvetica",17,"bold")).place(x=380, y=5)
    player_section = ck.CTkLabel(self.up_frame, text="Section: Manga", font=("Helvetica",17,"bold")).place(x=420, y=5)
    bar_lab = ck.CTkLabel(self.up_frame, text=f" | ", font=("Helvetica",17,"bold")).place(x=600, y=5)
    player_level = ck.CTkLabel(self.up_frame, text="Questions N°: 15", font=("Helvetica",17,"bold")).place(x=640, y=5)
    bar_lab = ck.CTkLabel(self.up_frame, text=f" | ", font=("Helvetica",17,"bold")).place(x=805, y=5)
    current_time = ck.CTkLabel(self.up_frame, text=f"Date: {now}", font=("Helvetica",15,"bold")).place(x=850, y=5)


    def Manga_quiz_window():
      self.up_frame.place(x=5, y=15)
      self.quiz_frame.place(x=5, y=5)


    def manga_display_result():
      wrong_count = self.data_size - self.correct
      correct = f"Correct Answers: {self.correct}"
      wrong = f"Wrong Answers: {wrong_count}"

      score = int(self.correct / self.data_size * 100)
      result = f"Total Score: {score}%"

      msg.showinfo("Result", f"{result}\n{correct}\n{wrong}")


    def manga_check_ans(manga_ques_no):
      if self.opt_selected.get() == animation_ans[manga_ques_no]:
        return True


    def manga_next_btn():
      if manga_check_ans(self.manga_ques_no):
        self.correct += 1

      self.manga_ques_no += 1
      if self.manga_ques_no == self.data_size:
        manga_display_result()
        self.win.destroy()
      else:
        manga_display_question()
        manga_display_options()


    def manga_display_options():
      val = 0
      self.opt_selected.set(0)
      for option in animation_opt[self.manga_ques_no]:
        self.opts[val]['text'] = option
        val += 1


    def manga_display_question():
      question_label = ck.CTkLabel(self.quiz_frame, width=900, height=100, text = animation_ques[self.manga_ques_no], font=("Helvetica", 30, "bold"), text_color="#fff")
      question_label.place(x=50, y=90)


    def manga_radio_buttons():
      manga_ques_list = []
      y_pos = 190
      while len(manga_ques_list) < 4:
        radio_btn = Radiobutton(self.quiz_frame, text=" ", variable=self.opt_selected, value = len(manga_ques_list)+1, font=("Helvetica",20, 'bold'), bg="#313440", fg="white", activebackground="#3399ff", activeforeground="white", selectcolor="#313440", padx=10)
        manga_ques_list.append(radio_btn)
        radio_btn.place(x=140, y=y_pos)
        y_pos += 60
      return manga_ques_list


    self.manga_ques_no = 0
    manga_display_question()
    self.opt_selected = IntVar()
    self.opts = manga_radio_buttons()
    manga_display_options()
    self.data_size = len(acronym_ques)
    self.correct = 0

    next_btn = ck.CTkButton(self.quiz_frame, text='Next', width=150, height=40, font=('Helvetica', 20, 'bold'), fg_color='royalblue', bg_color='#313440', hover_color='#313440', border_width=1, border_color='#fff', command=manga_next_btn)
    next_btn.place(x=830, y=440)


  def Computer_window(self):
    self.win = Toplevel()
    self.win.title('Computer')
    self.win.iconbitmap('Cham.ico')
    self.win.geometry('1000x500+350+250')
    self.win.config(background="#313440")
    self.win.resizable(False, False)

    # ------------------------------ The main window frame.
    self.warning_frame = ck.CTkFrame(self.win, width=990, height=490, bg_color='#313440', fg_color='#313440', border_width=1, border_color='royalblue')
    # ------------------------------ The questions frame.
    self.quiz_frame = ck.CTkFrame(self.win, width=990, height=490, bg_color='#313440', fg_color='#313440', border_width=1, border_color='royalblue')
    self.up_frame = ck.CTkFrame(self.quiz_frame, width=980, height=40, bg_color='#313440', fg_color='royalblue', border_width=1, border_color='royalblue')
    
    # ------------------------------ The start quiz elements.
    warning_title_label = ck.CTkLabel(self.warning_frame, text=emoji.emojize(':warning: COMPUTER QUIZ WARNING :warning:'), font=('Helvetica', 50, 'bold'), fg_color='#313440', bg_color='#313440').place(x=100, y=50)
    warning_info_label = ck.CTkLabel(self.warning_frame, text="Dear User. This is a friendly reminder that an important task is currently in progress within this \napplication window. Closing the window prematurely may result in the loss of unsaved \ndata or incomplete actions.\n\nTo ensure a seamless experience and to avoid any potential data loss, please refrain from closing \nthe app window until the task is successfully completed. If you encounter any issues \nor have questions, feel free to reach out to our support team for assistance.\n\nThank you for your understanding and collaboration.", font=('Helvetica', 20, 'bold'), fg_color='#313440', bg_color='#313440').place(x=30, y=160)
    
    start_button = ck.CTkButton(self.warning_frame, text='Start The Quiz', width=600, height=50, font=('Helvetica', 20, 'bold'), fg_color='royalblue', bg_color='#313440', hover_color='#313440', border_width=1, border_color='#fff', command=lambda:Computer_quiz_window()).place(x=200, y=400)
    
    self.warning_frame.place(x=5, y=5)

    # ------------------------------ The up frame items.
    time = datetime.now()
    now = time.date()
    player_name = ck.CTkLabel(self.up_frame, text=f"Player: {self.user}", font=("Helvetica",17,"bold")).place(x=10, y=5)
    bar_lab = ck.CTkLabel(self.up_frame, text=f" | ", font=("Helvetica",17,"bold")).place(x=380, y=5)
    player_section = ck.CTkLabel(self.up_frame, text="Section: Computer", font=("Helvetica",17,"bold")).place(x=420, y=5)
    bar_lab = ck.CTkLabel(self.up_frame, text=f" | ", font=("Helvetica",17,"bold")).place(x=600, y=5)
    player_level = ck.CTkLabel(self.up_frame, text="Questions N°: 15", font=("Helvetica",17,"bold")).place(x=640, y=5)
    bar_lab = ck.CTkLabel(self.up_frame, text=f" | ", font=("Helvetica",17,"bold")).place(x=805, y=5)
    current_time = ck.CTkLabel(self.up_frame, text=f"Date: {now}", font=("Helvetica",15,"bold")).place(x=850, y=5)


    def Computer_quiz_window():
      self.up_frame.place(x=5, y=15)
      self.quiz_frame.place(x=5, y=5)


    def computer_display_result():
      wrong_count = self.data_size - self.correct
      correct = f"Correct Answers: {self.correct}"
      wrong = f"Wrong Answers: {wrong_count}"

      score = int(self.correct / self.data_size * 100)
      result = f"Total Score: {score}%"

      msg.showinfo("Result", f"{result}\n{correct}\n{wrong}")


    def computer_check_ans(computer_ques_no):
      if self.opt_selected.get() == computer_ans[computer_ques_no]:
        return True


    def computer_next_btn():
      if computer_check_ans(self.computer_ques_no):
        self.correct += 1

      self.computer_ques_no += 1
      if self.computer_ques_no == self.data_size:
        computer_display_result()
        self.win.destroy()
      else:
        computer_display_question()
        computer_display_options()


    def computer_display_options():
      val = 0
      self.opt_selected.set(0)
      for option in computer_opt[self.computer_ques_no]:
        self.opts[val]['text'] = option
        val += 1


    def computer_display_question():
      question_label = ck.CTkLabel(self.quiz_frame, width=900, height=100, text = computer_ques[self.computer_ques_no], font=("Helvetica", 30, "bold"), text_color="#fff")
      question_label.place(x=50, y=80)


    def computer_radio_buttons():
      computer_ques_list = []
      y_pos = 190
      while len(computer_ques_list) < 4:
        radio_btn = Radiobutton(self.quiz_frame, text=" ", variable=self.opt_selected, value = len(computer_ques_list)+1, font=("Helvetica",20, 'bold'), bg="#313440", fg="white", activebackground="#3399ff", activeforeground="white", selectcolor="#313440", padx=10)
        computer_ques_list.append(radio_btn)
        radio_btn.place(x=140, y=y_pos)
        y_pos += 60
      return computer_ques_list


    self.computer_ques_no = 0
    computer_display_question()
    self.opt_selected = IntVar()
    self.opts = computer_radio_buttons()
    computer_display_options()
    self.data_size = len(acronym_ques)
    self.correct = 0

    next_btn = ck.CTkButton(self.quiz_frame, text='Next', width=150, height=40, font=('Helvetica', 20, 'bold'), fg_color='royalblue', bg_color='#313440', hover_color='#313440', border_width=1, border_color='#fff', command=computer_next_btn)
    next_btn.place(x=830, y=440)


  def Programming_window(self):
    self.win = Toplevel()
    self.win.title('Programming')
    self.win.iconbitmap('Cham.ico')
    self.win.geometry('1000x500+350+250')
    self.win.config(background="#313440")
    self.win.resizable(False, False)

    # ------------------------------ The main window frame.
    self.warning_frame = ck.CTkFrame(self.win, width=990, height=490, bg_color='#313440', fg_color='#313440', border_width=1, border_color='royalblue')
    # ------------------------------ The questions frame.
    self.quiz_frame = ck.CTkFrame(self.win, width=990, height=490, bg_color='#313440', fg_color='#313440', border_width=1, border_color='royalblue')
    self.up_frame = ck.CTkFrame(self.quiz_frame, width=980, height=40, bg_color='#313440', fg_color='royalblue', border_width=1, border_color='royalblue')
    
    # ------------------------------ The start quiz elements.
    warning_title_label = ck.CTkLabel(self.warning_frame, text=emoji.emojize(':warning: PROGRAMMING QUIZ WARNING :warning:'), font=('Helvetica', 50, 'bold'), fg_color='#313440', bg_color='#313440').place(x=40, y=50)
    warning_info_label = ck.CTkLabel(self.warning_frame, text="Dear User. This is a friendly reminder that an important task is currently in progress within this \napplication window. Closing the window prematurely may result in the loss of unsaved \ndata or incomplete actions.\n\nTo ensure a seamless experience and to avoid any potential data loss, please refrain from closing \nthe app window until the task is successfully completed. If you encounter any issues \nor have questions, feel free to reach out to our support team for assistance.\n\nThank you for your understanding and collaboration.", font=('Helvetica', 20, 'bold'), fg_color='#313440', bg_color='#313440').place(x=30, y=160)
    
    start_button = ck.CTkButton(self.warning_frame, text='Start The Quiz', width=600, height=50, font=('Helvetica', 20, 'bold'), fg_color='royalblue', bg_color='#313440', hover_color='#313440', border_width=1, border_color='#fff', command=lambda:Programming_quiz_window()).place(x=200, y=400)
    
    self.warning_frame.place(x=5, y=5)

    # ------------------------------ The up frame items.
    time = datetime.now()
    now = time.date()
    player_name = ck.CTkLabel(self.up_frame, text=f"Player: {self.user}", font=("Helvetica",17,"bold")).place(x=10, y=5)
    bar_lab = ck.CTkLabel(self.up_frame, text=f" | ", font=("Helvetica",17,"bold")).place(x=380, y=5)
    player_section = ck.CTkLabel(self.up_frame, text="Section: Programming", font=("Helvetica",17,"bold")).place(x=420, y=5)
    bar_lab = ck.CTkLabel(self.up_frame, text=f" | ", font=("Helvetica",17,"bold")).place(x=600, y=5)
    player_level = ck.CTkLabel(self.up_frame, text="Questions N°: 15", font=("Helvetica",17,"bold")).place(x=640, y=5)
    bar_lab = ck.CTkLabel(self.up_frame, text=f" | ", font=("Helvetica",17,"bold")).place(x=805, y=5)
    current_time = ck.CTkLabel(self.up_frame, text=f"Date: {now}", font=("Helvetica",15,"bold")).place(x=850, y=5)


    def Programming_quiz_window():
      self.up_frame.place(x=5, y=15)
      self.quiz_frame.place(x=5, y=5)


    def programming_display_result():
      wrong_count = self.data_size - self.correct
      correct = f"Correct Answers: {self.correct}"
      wrong = f"Wrong Answers: {wrong_count}"

      score = int(self.correct / self.data_size * 100)
      result = f"Total Score: {score}%"

      msg.showinfo("Result", f"{result}\n{correct}\n{wrong}")


    def programming_check_ans(programming_ques_no):
      if self.opt_selected.get() == program_ans[programming_ques_no]:
        return True


    def programming_next_btn():
      if programming_check_ans(self.programming_ques_no):
        self.correct += 1

      self.programming_ques_no += 1
      if self.programming_ques_no == self.data_size:
        programming_display_result()
        self.win.destroy()
      else:
        programming_display_question()
        programming_display_options()


    def programming_display_options():
      val = 0
      self.opt_selected.set(0)
      for option in program_opt[self.programming_ques_no]:
        self.opts[val]['text'] = option
        val += 1


    def programming_display_question():
      question_label = ck.CTkLabel(self.quiz_frame, width=900, height=100, text = program_ques[self.programming_ques_no], font=("Helvetica", 27, "bold"), text_color="#fff")
      question_label.place(x=50, y=80)


    def programming_radio_buttons():
      programming_ques_list = []
      y_pos = 190
      while len(programming_ques_list) < 4:
        radio_btn = Radiobutton(self.quiz_frame, text=" ", variable=self.opt_selected, value = len(programming_ques_list)+1, font=("Helvetica",20, 'bold'), bg="#313440", fg="white", activebackground="#3399ff", activeforeground="white", selectcolor="#313440", padx=10)
        programming_ques_list.append(radio_btn)
        radio_btn.place(x=140, y=y_pos)
        y_pos += 60
      return programming_ques_list


    self.programming_ques_no = 0
    programming_display_question()
    self.opt_selected = IntVar()
    self.opts = programming_radio_buttons()
    programming_display_options()
    self.data_size = len(acronym_ques)
    self.correct = 0

    next_btn = ck.CTkButton(self.quiz_frame, text='Next', width=150, height=40, font=('Helvetica', 20, 'bold'), fg_color='royalblue', bg_color='#313440', hover_color='#313440', border_width=1, border_color='#fff', command=programming_next_btn)
    next_btn.place(x=830, y=440)


  def Religion_window(self):
    self.win = Toplevel()
    self.win.title('Religion')
    self.win.iconbitmap('Cham.ico')
    self.win.geometry('1000x500+350+250')
    self.win.config(background="#313440")
    self.win.resizable(False, False)

    # ------------------------------ The main window frame.
    self.warning_frame = ck.CTkFrame(self.win, width=990, height=490, bg_color='#313440', fg_color='#313440', border_width=1, border_color='royalblue')
    # ------------------------------ The questions frame.
    self.quiz_frame = ck.CTkFrame(self.win, width=990, height=490, bg_color='#313440', fg_color='#313440', border_width=1, border_color='royalblue')
    self.up_frame = ck.CTkFrame(self.quiz_frame, width=980, height=40, bg_color='#313440', fg_color='royalblue', border_width=1, border_color='royalblue')
    
    # ------------------------------ The start quiz elements.
    warning_title_label = ck.CTkLabel(self.warning_frame, text=emoji.emojize(':warning: RELIGION QUIZ WARNING :warning:'), font=('Helvetica', 50, 'bold'), fg_color='#313440', bg_color='#313440').place(x=110, y=50)
    warning_info_label = ck.CTkLabel(self.warning_frame, text="Dear User. This is a friendly reminder that an important task is currently in progress within this \napplication window. Closing the window prematurely may result in the loss of unsaved \ndata or incomplete actions.\n\nTo ensure a seamless experience and to avoid any potential data loss, please refrain from closing \nthe app window until the task is successfully completed. If you encounter any issues \nor have questions, feel free to reach out to our support team for assistance.\n\nThank you for your understanding and collaboration.", font=('Helvetica', 20, 'bold'), fg_color='#313440', bg_color='#313440').place(x=30, y=160)
    
    start_button = ck.CTkButton(self.warning_frame, text='Start The Quiz', width=600, height=50, font=('Helvetica', 20, 'bold'), fg_color='royalblue', bg_color='#313440', hover_color='#313440', border_width=1, border_color='#fff', command=lambda:Religion_quiz_window()).place(x=200, y=400)
    
    self.warning_frame.place(x=5, y=5)

    # ------------------------------ The up frame items.
    time = datetime.now()
    now = time.date()
    player_name = ck.CTkLabel(self.up_frame, text=f"Player: {self.user}", font=("Helvetica",17,"bold")).place(x=10, y=5)
    bar_lab = ck.CTkLabel(self.up_frame, text=f" | ", font=("Helvetica",17,"bold")).place(x=380, y=5)
    player_section = ck.CTkLabel(self.up_frame, text="Section: Religion", font=("Helvetica",17,"bold")).place(x=420, y=5)
    bar_lab = ck.CTkLabel(self.up_frame, text=f" | ", font=("Helvetica",17,"bold")).place(x=600, y=5)
    player_level = ck.CTkLabel(self.up_frame, text="Questions N°: 15", font=("Helvetica",17,"bold")).place(x=640, y=5)
    bar_lab = ck.CTkLabel(self.up_frame, text=f" | ", font=("Helvetica",17,"bold")).place(x=805, y=5)
    current_time = ck.CTkLabel(self.up_frame, text=f"Date: {now}", font=("Helvetica",15,"bold")).place(x=850, y=5)


    def Religion_quiz_window():
      self.up_frame.place(x=5, y=15)
      self.quiz_frame.place(x=5, y=5)


    def religion_display_result():
      wrong_count = self.data_size - self.correct
      correct = f"Correct Answers: {self.correct}"
      wrong = f"Wrong Answers: {wrong_count}"

      score = int(self.correct / self.data_size * 100)
      result = f"Total Score: {score}%"

      msg.showinfo("Result", f"{result}\n{correct}\n{wrong}")


    def religion_check_ans(religion_ques_no):
      if self.opt_selected.get() == reli_ans[religion_ques_no]:
        return True


    def religion_next_btn():
      if religion_check_ans(self.religion_ques_no):
        self.correct += 1

      self.religion_ques_no += 1
      if self.religion_ques_no == self.data_size:
        religion_display_result()
        self.win.destroy()
      else:
        religion_display_question()
        religion_display_options()


    def religion_display_options():
      val = 0
      self.opt_selected.set(0)
      for option in reli_opt[self.religion_ques_no]:
        self.opts[val]['text'] = option
        val += 1


    def religion_display_question():
      question_label = ck.CTkLabel(self.quiz_frame, width=900, height=100, text = reli_ques[self.religion_ques_no], font=("Helvetica", 30, "bold"), text_color="#fff")
      question_label.place(x=50, y=80)


    def religion_radio_buttons():
      religion_ques_list = []
      y_pos = 190
      while len(religion_ques_list) < 4:
        radio_btn = Radiobutton(self.quiz_frame, text=" ", variable=self.opt_selected, value = len(religion_ques_list)+1, font=("Helvetica",20, 'bold'), bg="#313440", fg="white", activebackground="#3399ff", activeforeground="white", selectcolor="#313440", padx=10)
        religion_ques_list.append(radio_btn)
        radio_btn.place(x=140, y=y_pos)
        y_pos += 60
      return religion_ques_list


    self.religion_ques_no = 0
    religion_display_question()
    self.opt_selected = IntVar()
    self.opts = religion_radio_buttons()
    religion_display_options()
    self.data_size = len(acronym_ques)
    self.correct = 0

    next_btn = ck.CTkButton(self.quiz_frame, text='Next', width=150, height=40, font=('Helvetica', 20, 'bold'), fg_color='royalblue', bg_color='#313440', hover_color='#313440', border_width=1, border_color='#fff', command=religion_next_btn)
    next_btn.place(x=830, y=440)


  def Information_technology_window(self):
    self.win = Toplevel()
    self.win.title('Information Technology')
    self.win.iconbitmap('Cham.ico')
    self.win.geometry('1000x500+350+250')
    self.win.config(background="#313440")
    self.win.resizable(False, False)

    # ------------------------------ The main window frame.
    self.warning_frame = ck.CTkFrame(self.win, width=990, height=490, bg_color='#313440', fg_color='#313440', border_width=1, border_color='royalblue')
    # ------------------------------ The questions frame.
    self.quiz_frame = ck.CTkFrame(self.win, width=990, height=490, bg_color='#313440', fg_color='#313440', border_width=1, border_color='royalblue')
    self.up_frame = ck.CTkFrame(self.quiz_frame, width=980, height=40, bg_color='#313440', fg_color='royalblue', border_width=1, border_color='royalblue')
    
    # ------------------------------ The start quiz elements.
    warning_title_label = ck.CTkLabel(self.warning_frame, text=emoji.emojize(':warning: I.T QUIZ WARNING :warning:'), font=('Helvetica', 50, 'bold'), fg_color='#313440', bg_color='#313440').place(x=210, y=50)
    warning_info_label = ck.CTkLabel(self.warning_frame, text="Dear User. This is a friendly reminder that an important task is currently in progress within this \napplication window. Closing the window prematurely may result in the loss of unsaved \ndata or incomplete actions.\n\nTo ensure a seamless experience and to avoid any potential data loss, please refrain from closing \nthe app window until the task is successfully completed. If you encounter any issues \nor have questions, feel free to reach out to our support team for assistance.\n\nThank you for your understanding and collaboration.", font=('Helvetica', 20, 'bold'), fg_color='#313440', bg_color='#313440').place(x=30, y=160)
    
    start_button = ck.CTkButton(self.warning_frame, text='Start The Quiz', width=600, height=50, font=('Helvetica', 20, 'bold'), fg_color='royalblue', bg_color='#313440', hover_color='#313440', border_width=1, border_color='#fff', command=lambda:Information_technology_quiz_window()).place(x=200, y=400)
    
    self.warning_frame.place(x=5, y=5)

    # ------------------------------ The up frame items.
    time = datetime.now()
    now = time.date()
    player_name = ck.CTkLabel(self.up_frame, text=f"Player: {self.user}", font=("Helvetica",17,"bold")).place(x=10, y=5)
    bar_lab = ck.CTkLabel(self.up_frame, text=f" | ", font=("Helvetica",17,"bold")).place(x=380, y=5)
    player_section = ck.CTkLabel(self.up_frame, text="Section: I.T", font=("Helvetica",17,"bold")).place(x=420, y=5)
    bar_lab = ck.CTkLabel(self.up_frame, text=f" | ", font=("Helvetica",17,"bold")).place(x=600, y=5)
    player_level = ck.CTkLabel(self.up_frame, text="Questions N°: 15", font=("Helvetica",17,"bold")).place(x=640, y=5)
    bar_lab = ck.CTkLabel(self.up_frame, text=f" | ", font=("Helvetica",17,"bold")).place(x=805, y=5)
    current_time = ck.CTkLabel(self.up_frame, text=f"Date: {now}", font=("Helvetica",15,"bold")).place(x=850, y=5)


    def Information_technology_quiz_window():
      self.up_frame.place(x=5, y=15)
      self.quiz_frame.place(x=5, y=5)


    def information_technology_display_result():
      wrong_count = self.data_size - self.correct
      correct = f"Correct Answers: {self.correct}"
      wrong = f"Wrong Answers: {wrong_count}"

      score = int(self.correct / self.data_size * 100)
      result = f"Total Score: {score}%"

      msg.showinfo("Result", f"{result}\n{correct}\n{wrong}")


    def information_technology_check_ans(information_technology_ques_no):
      if self.opt_selected.get() == it_ans[information_technology_ques_no]:
        return True


    def information_technology_next_btn():
      if information_technology_check_ans(self.information_technology_ques_no):
        self.correct += 1

      self.information_technology_ques_no += 1
      if self.information_technology_ques_no == self.data_size:
        information_technology_display_result()
        self.win.destroy()
      else:
        information_technology_display_question()
        information_technology_display_options()


    def information_technology_display_options():
      val = 0
      self.opt_selected.set(0)
      for option in it_opt[self.information_technology_ques_no]:
        self.opts[val]['text'] = option
        val += 1


    def information_technology_display_question():
      question_label = ck.CTkLabel(self.quiz_frame, width=900, height=100, text = it_ques[self.information_technology_ques_no], font=("Helvetica", 30, "bold"), text_color="#fff")
      question_label.place(x=50, y=80)


    def information_technology_radio_buttons():
      information_technology_ques_list = []
      y_pos = 190
      while len(information_technology_ques_list) < 4:
        radio_btn = Radiobutton(self.quiz_frame, text=" ", variable=self.opt_selected, value = len(information_technology_ques_list)+1, font=("Helvetica",20, 'bold'), bg="#313440", fg="white", activebackground="#3399ff", activeforeground="white", selectcolor="#313440", padx=10)
        information_technology_ques_list.append(radio_btn)
        radio_btn.place(x=140, y=y_pos)
        y_pos += 60
      return information_technology_ques_list


    self.information_technology_ques_no = 0
    information_technology_display_question()
    self.opt_selected = IntVar()
    self.opts = information_technology_radio_buttons()
    information_technology_display_options()
    self.data_size = len(acronym_ques)
    self.correct = 0

    next_btn = ck.CTkButton(self.quiz_frame, text='Next', width=150, height=40, font=('Helvetica', 20, 'bold'), fg_color='royalblue', bg_color='#313440', hover_color='#313440', border_width=1, border_color='#fff', command=information_technology_next_btn)
    next_btn.place(x=830, y=440)


"""   """


app = Quiz_Game()
app.mainloop()