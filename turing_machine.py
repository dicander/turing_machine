import random


class row(object):
    """A row in a Turing machine program"""
    def __init__(self, state="start", symbol = ">", write = ">" , direction="R", new_state = "start"):
        self.state=state
        self.symbol=symbol
        self.write = write
        self.direction = direction
        self.new_state = new_state

    def __str__(self):
        return(" {:10}{:7}{:7}{:7}{:10}".format(self.state, self.symbol, self.write, self.direction, self.new_state))


class machine(object):
    """A virtual Turing machine."""
    def __init__(self, program=[], memory=['>'], state="start", pointer=0, mem_max=1000, steps_max=10000):
        self.program = program
        self.state = state
        self.memory = memory
        self.pointer = 0
        self.steps = 0
        self.error = ""
        self.mem_max=mem_max
        self.steps_max=steps_max

    def report(self):
        """Prints memory, errors and steps."""
        print ("".join(self.memory), self.error, self.steps)

    def step(self):
        """Take a single step."""
        for row in self.program:
            if row.state == self.state and row.symbol == self.memory[self.pointer]:
                self.steps += 1
                self.memory[self.pointer] = row.write
                self.state=row.new_state
                if row.direction == ">":
                    self.pointer +=1
                    if self.pointer >= self.mem_max:
                        self.error = "Memory limit exceeded."
                        return 0
                    elif self.pointer >=len(self.memory):
                        self.memory += ["#" for x in range(len(self.memory))]
                    return 1
                elif row.direction == "<":
                    self.pointer -=1
                    if self.pointer <0:
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
        print("  {:10}{:7}{:7}{:7}{:10}".format("State", "symbol", "write", "move", "new_state"))
        for row in self.program:
            if row.state == self.state and row.symbol == self.memory[self.pointer]:
                print(">", end="")
            else:
                print(" ", end="")
            print(row)

    def k_steps(self, k):
        """Takes k steps."""
        for i in range(k):
            if 0 == self.step() or state=="halt":
                report()
                return

def successor():
    """Example machine that adds one to binary numbers."""
    code=[]
    code.append(row("start", ">", ">", ">", "start"))
    code.append(row("start", "0", "0", ">", "right"))
    code.append(row("start", "1", "1", ">", "all_one"))
    code.append(row("start", "#", "1", "<", "halt"))
    code.append(row("all_one", "0", "0", ">", "right"))
    code.append(row("all_one", "1", "1", ">", "all_one"))
    code.append(row("all_one", "#", "0", "<", "clear"))
    code.append(row("right", "0", "0", ">", "right"))
    code.append(row("right", "1", "1", ">", "right"))
    code.append(row("right", "#", "#", "<", "carry"))
    code.append(row("clear", ">", ">", ">", "put_one"))
    code.append(row("clear", "1", "0", "<", "clear"))
    code.append(row("put_one", "0", "1", "<", "halt"))
    code.append(row("carry", "0", "1", "<", "halt"))
    code.append(row("carry", "1", "0", "<", "carry"))
    datatapes=[['>', '1', '1', '1', '1','#','#'], ['>','#','#','#'], ['>','1','0','1','0','1','0','#']]
    datatapes+=[(['>']+[random.choice(['0','1']) for symbols in range(random.randint(1,10))]+['#','#','#']) for x in range(10)]
    for mem in datatapes:
        m = machine(code, mem)
        while m.state != "halt":
            m.debug()
            m.step()
            input()
        m.debug()
        input()
        print("**********************************")

def little_endian_add():
    """Code that adds one to a little endian binary number."""
    code=[]
    code.append(row("start", ">", ">", ">", "carry"))
    #state symbol write direction new_state
    code.append(row("carry", "0", "1", "<", "halt"))
    code.append(row("carry", "1", "0", ">", "carry"))
    code.append(row("carry", "#", "1", "<", "halt"))
    m=machine(code, ['>', '1', '1', '1', '1','#','#'])


def main():
    """Main performs the operations of a trivial machine."""
    code=[]
    code.append(row("start", ">", ">", ">", "carry"))
    #state symbol write direction new_state
    code.append(row("carry", "0", "1", "<", "halt"))
    code.append(row("carry", "1", "0", ">", "carry"))
    code.append(row("carry", "#", "1", "<", "halt"))
    m=machine(code, ['>', '1', '1', '1', '1','#','#'])
    while m.state != "halt":
        m.debug()
        m.step()
        input()
    m.debug()

successor()
