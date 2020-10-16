import os
import time
import json
import spot
import datetime
import ltl_graph_parser as LGP


class SPOTClient():
    def __init__(self):
        self.res_ltl_spec = {}
        self.prev_id = -1
        self.current_id = 0
        self.mounted_path = "/home/robotics/spot_server/"
        self.req_json_path = os.path.join(self.mounted_path, "ltl_spec.json")
        self.res_json_path = os.path.join(self.mounted_path, "ltl_spec_response.json")
        self.read_request_json()
        
    def save_parsing_result(self, tstmp, exctr, trv_seq, act_seq, graph):
        # Check if response json file exists and readable
        if os.path.isfile("res_ltl_spec.json") and os.access("res_ltl_spec.json", os.R_OK):
            print("Response json file already exist .... ")
            f = open("res_ltl_spec.json", "r")
            self.res_ltl_spec = json.load(f)
            
        if "total_response" in self.res_ltl_spec:
            self.res_ltl_spec["total_response"] = self.res_ltl_spec["total_response"] + 1
        else:
            self.res_ltl_spec["total_response"] = 1
        
        cur_res_id = self.res_ltl_spec["total_response"]
        self.res_ltl_spec[cur_res_id] = {}
        self.res_ltl_spec[cur_res_id]["timestamp"] = str(datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S'))
        self.res_ltl_spec[cur_res_id]["executor"] = exctr
        self.res_ltl_spec[cur_res_id]["graph_info"] = graph
        self.res_ltl_spec[cur_res_id]["traversal_sequence"] = trv_seq
        self.res_ltl_spec[cur_res_id]["action_sequence"] = act_seq
        
        with open('res_ltl_spec.json', 'w') as f:
            json.dump(self.res_ltl_spec, f)
            f.close()
        
    def generate_spot_result(self, formula, tstmp, exctr):
        # Get result from SPOT in *.dot format
        spot_lang = spot.translate(formula, 'BA', 'complete')
        dot_file = spot_lang.to_str('dot')
        print("Dot file: ", dot_file)
        # Parsing dot file and save traversal and action sequence
        G = LGP.LTLGraphCreation(dot_file)
        G.recurse_traversal(0, [0], [])
        print("Recursion finished ....")
        trv_seq =  G.traversal_seq # contains traversal sequence
        act_seq = G.action_seq # contains action sequence
        graph = G.graph
        self.save_parsing_result(tstmp, exctr, trv_seq, act_seq, graph)

    def process_request(self, req_json_obj, curnt_id):
        curnt_id = str(curnt_id)
        print("Currently processing request: ", curnt_id)
        formula = req_json_obj[curnt_id]["ltl_formula"]
        executor = req_json_obj[curnt_id]["executor"]
        time_stamp = req_json_obj[curnt_id]["timestamp"]
        print("Formula: ", formula , "  Executor: ", executor, "  Timestamp: ", time_stamp)
        self.generate_spot_result(formula, time_stamp, executor)
    
    def read_request_json(self):
        while True:
            print("req_json_path: ", self.req_json_path)
            if os.path.isfile(self.req_json_path) and os.access(self.req_json_path, os.R_OK):
                # Request file exists
                f = open(self.req_json_path, "r")
                self.req_obj = json.load(f)
                if self.current_id < self.req_obj["total_req"]:
                    # Pending new request..
                    # elif(self.current_id > self.prev_id):
                    self.process_request(self.req_obj, self.current_id+1)
                    self.prev_id = self.current_id
                    self.current_id += 1
                
                else:
                    print("Log: No new request")

            time.sleep(2) # pauses for 2 sec

if __name__ == "__main__":
    SPOTClient()
