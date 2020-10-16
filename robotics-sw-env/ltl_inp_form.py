import os
import sys
import datetime
import json

class JSONLTLSpecWriter():
    def __init__(self):
        self.ltl_spec = {}

    def save_data(self):
        with open('ltl_spec.json', 'w') as f:
            json.dump(self.ltl_spec, f)
            f.close()

    def write_ltl_spec(self, exec_name, formula):
        """
        Writing user input in JSON format
        :return:
        """
        if os.path.isfile("ltl_spec.json") and os.access("ltl_spec.json", os.R_OK):
            # Check if file exists and readable
            print("JSON file already exist .... ")
            f = open("ltl_spec.json", "r")
            self.ltl_spec = json.load(f)

        if "total_req" in self.ltl_spec:
            self.ltl_spec["total_req"] = self.ltl_spec["total_req"] + 1
        else:
            self.ltl_spec["total_req"] = 1

        current_id = self.ltl_spec["total_req"]
        self.ltl_spec[current_id] = {}
        self.ltl_spec[current_id] ["timestamp"] = str(datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S'))
        self.ltl_spec[current_id] ["executor"] = exec_name
        self.ltl_spec[current_id] ["ltl_formula"] = formula

'''
class LTLFormWindow():
    def __init__(self):
        #self.executor_name = None
        #self.formula = None
        self.json_obj = JSONLTLSpecWriter()
        self.layout_creation_tk()

    def layout_creation_tk(self):
        """
        Layout for the User Input (LTL Formula) Form
        :return:
        """
        def write_user_inp():
            executor_name = exec_name.get()
            formula = inp_formula.get("1.0", END)
            print("exec name : ", executor_name)
            print("Formula : ", formula)
            self.json_obj.write_ltl_spec(executor_name, formula)
            self.json_obj.save_data()
            win.destroy()

        win = Tk()
        win.title("LTL Input Formulation!")
        #win.geometry('475x350')
        #win.minsize(width=480, height=300)
        #win.maxsize(width=480, height=300)
        win.resizable(width=False, height=False)
        win.configure(background="black")



        exec_label = Label(win, text="Program Executor: ", justify=CENTER, relief='solid', bd=1,  bg="#ff5500",
                           font=(None, 18), borderwidth="2").grid(row=0, column=0, sticky=W+E)
        exec_name = Entry(win, font=(None, 18), relief='solid', bd=1, borderwidth="2")
        exec_name.grid(row=0, column=1, sticky=W+E)
        #sp = StringVar()
        #sp_label = Label(text='\n').grid(row=1, column=0)
        ltl_inp_label = Label(win, text="LTL Input: ", justify=CENTER, relief='solid', bg="#ff5500", font=(None, 18),
                  borderwidth="2").grid(row=2, column=0, sticky=W+E)

        #e2= Entry(win, justify=LEFT, font=(None, 18), borderwidth="2").grid(row=3, column=0, columnspan=3)
        inp_formula = Text(win, font=(None, 18), width = 38, height=10, borderwidth="2")
        inp_formula.grid(row=3, column=0, columnspan=3, sticky=W+E)

        run_btn = Button(win, text="Run", command=write_user_inp, bg='green', font=(None, 18),
                         borderwidth="2").grid(row=4, column=0, sticky=W+E)
        quit_btn = Button(win, text="Quit", command=quit, bg='red', font=(None, 18), borderwidth="2").grid(row=4, column=1, sticky=W+E)

        win.mainloop()
'''

if __name__ == "__main__":
    #obj = LTLFormWindow()
    json_obj = JSONLTLSpecWriter()
    executor = sys.argv[1]
    formula = sys.argv[2]
    print("exec name : ", executor)
    print("Formula : ", formula)
    json_obj.write_ltl_spec(executor, formula)
    json_obj.save_data()




