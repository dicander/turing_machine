import random
import sys


class Row(object):
    """A row in a Turing machine program"""
    def __init__(self, state="start", symbol=">", write=">", direction=">", new_state="start"):
        self.state = state
        self.symbol = symbol
        self.write = write
        self.direction = direction
        self.new_state = new_state

    def __str__(self):
        return(" {:16}{:7}{:7}{:7}{:16}".format(self.state, self.symbol,
                                                self.write, self.direction, self.new_state))


class Machine(object):
    """A virtual Turing machine."""
    def __init__(self, program=[], memory=['>'], state="start", pointer=0, 
                 mem_max=100000, steps_max=100000):
        self.program = program
        self.state = state
        self.memory = memory
        self.pointer = 0
        self.steps = 0
        self.error = ""
        self.mem_max = mem_max
        self.steps_max = steps_max

    def report(self):
        """Prints memory, errors and steps."""
        print("".join(self.memory), self.error, self.steps)

    def step(self):
        """Take a single step."""
        for row in self.program:
            if row.state == self.state and row.symbol == self.memory[self.pointer]:
                self.steps += 1
                self.memory[self.pointer] = row.write
                self.state=row.new_state
                if row.direction in ">rR":
                    self.pointer += 1
                    if self.pointer >= self.mem_max:
                        self.error = "Memory limit exceeded."
                        return 0
                    elif self.pointer >= len(self.memory):
                        self.memory += ["#" for x in range(len(self.memory))]
                    return 1
                elif row.direction in "<lL":
                    self.pointer -= 1
                    if self.pointer < 0:
                        self.error = "Pointer negative."
                        return 0
                    return 1
                return 1
        self.error = "No row matches state and symbol"
        return 0

    def debug(self):
        """Prints the state, memory and lines of the program. Current
        row is marked with a '>'."""
        print("_,.-^ DEBUG ^-.,_")
        print("state = %s %s"%(self.state, self.error))
        print("".join(self.memory))
        print ((self.pointer*" ")+"^")
        print("PROGRAM")
        print("  {:16}{:7}{:7}{:7}{:16}".format("State", "symbol", "write", "move", "new_state"))
        for row in self.program:
            if row.state == self.state and row.symbol == self.memory[self.pointer]:
                print(">", end="")
            else:
                print(" ", end="")
            print(row)

    def k_steps(self, k):
        """Takes k steps."""
        for i in range(k):
            if 0 == self.step() or self.state == "halt":
                self.report()
                return


def main():
    if len(sys.argv) < 2:
        print("turing_machine: No files.")
        return
    file = open(sys.argv[1])
    code = []
    tapes = []
    counter = 0
    for line in file:
        counter += 1
        tokens = line.split()
        if len(tokens)>1 and tokens[0] == "TAPE":
            tapes.append(tokens[1])
        if len(tokens)<5:
            continue
        if "#" in tokens[0]:
            continue
        if tokens[1] not in "01>#" or tokens[2] not in "01>#" or tokens[3] not in "lrLR<>":
            print("Error in line", counter)
            continue
        code.append(Row(tokens[0], tokens[1], tokens[2], tokens[3], tokens[4]))
    for tape in tapes:
        m = Machine(code, [symbol for symbol in tape])
        while m.state != "halt":
            m.debug()
            m.step()
            input()
        m.debug()
        input()


main()
