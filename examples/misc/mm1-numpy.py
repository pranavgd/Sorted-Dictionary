import numpy # assuming numpy has been installed
import simulus

numpy.random.seed(123)

def job(idx):
    r.acquire()
    print("%g: job(%d) gains access" % (sim.now,idx))
    sim.sleep(numpy.random.gamma(2, 2))
    print("%g: job(%d) releases" % (sim.now,idx))
    r.release()

def arrival():
    i = 0
    while True:
        i += 1
        sim.sleep(numpy.random.pareto(0.95))
        print("%g: job(%d) arrives" % (sim.now,i))
        sim.process(job, i)

sim = simulus.simulator()
r = sim.resource()
sim.process(arrival)
sim.run(10)
