class fibonacciSequence():
    # Calculate valid fibonacci sequence number
    def F(self):
        a, b = 0,1
        while True:
            yield a
            a, b = b, a + b

    # return fibonacci sequence given a range
    def SubFib(self, x, y):
        for c in self.F():
            if c > y: return
            if c >= x:
                yield c

    # run the main loop inside class. Contains primary run
    def run(self):
        for i in self.SubFib(1, 10000000000):
            print (i)

# call run method on fibonacciSequence Object
def main():
    sequence = fibonacciSequence()
    sequence.run()

# Run only if not imported
if __name__ == '__main__':
    main()
