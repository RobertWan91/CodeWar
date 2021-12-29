class FSM(object):
    def __init__(self, instructions):
        # Compile instructions string
        self._instructions = instructions
        self._role_dict = None

    @property
    def role_dict(self):
        if self._role_dict is not None:
            return self._role_dict
        instruct_list = self._instructions.split('\n')
        for line in instruct_list:
            input_point, next_0_input_point, next_1_input_point, output = line[0], line[1], line[2], line[3]
            self.role_dict[input_point] = {}
            self.role_dict[input_point][0] = next_0_input_point
            self.role_dict[input_point][1] = next_1_input_point
            self.role_dict[input_point]['output'] = output

    def run_fsm(self, start, sequence):
        # return tuple: (final_state, final_state_output, path)
        path = [start]
        mid = start
        while sequence:
            state_num = sequence.pop(0)
            next_state = self.role_dict[mid][state_num]
            path.append(next_state)
            mid = next_state
        return mid, self.role_dict[mid]['output'], path
