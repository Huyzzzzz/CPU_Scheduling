from queue import Queue

class FCFS():
    # Processes is a dict with the following format:
    # key=process_name : values={arrival_time:, burst_time:}
    def __init__(self, processes, antt_chart):
        self.processes_queue = Queue(maxsize=6)
        self.number_processes = len(processes)
        self.processes = processes
        self.gantt_chart = gantt_chart
        self.run_time = 0
        self.simulation_process = []


    # Running the algorithm
    def run(self):
        # Put process into queue       
        sorted_arrival_time = sorted(self.processes.values(), key=lambda d: d["arrival_time"]) 
        for i in range(self.number_processes):
            self.processes_queue.put(sorted_arrival_time[i])
        
        # Calculate waiting time and turn around time
        process_running = None
        for i in range(self.number_processes): 
            process_running = self.processes_queue.get()
            if self.gantt_chart.qsize() == 0:
                process_running["waiting_time"] = 0
                process_running["turn_around_time"] = process_running["burst_time"]
            else:
                process_running["waiting_time"] = self.run_time 
                process_running["turn_around_time"] = process_running["waiting_time"] + process_running["burst_time"]
            self.gantt_chart.put(process_running)
            self.run_time += process_running["burst_time"]

processes = {
    "p1": {"process_name": "p1", "arrival_time": 4,"burst_time":3},
    "p2": {"process_name": "p2", "arrival_time": 2,"burst_time":7},
    "p3": {"process_name": "p3", "arrival_time": 1,"burst_time":5},
    "p4": {"process_name": "p4", "arrival_time": 3,"burst_time":9}
}
gantt_chart = Queue(maxsize=6)
fcfs = FCFS(processes, gantt_chart).run()
n = gantt_chart.qsize()
for i in range(n):
    a = gantt_chart.get()
    print(a)
    