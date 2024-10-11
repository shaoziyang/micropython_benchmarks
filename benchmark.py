'''
    Simple benchmark for micropython and circuitpython.

    Compare the performance of different MCUs by performing operations such as addition, multiplication, exponentiation, complex numbers, and pi.

'''
import sys
import gc

try:
    from time import ticks_ms, ticks_diff
    import machine
    TEST_ENV = 'micropython'
    
    def freq():
        try:
            f = machine.freq()//1000000
        except:
            f = machine.freq()[0]//1000000
        return f
except:
    from time import monotonic_ns
    
    def ticks_ms():
        return monotonic_ns()//1000000

    def ticks_diff(T2, T1):
        return T2 - T1
    
    try:
        import board
        TEST_ENV = 'circuitpython'
        
        import microcontroller
        
        def freq():
            return microcontroller.cpu.frequency//1000000

    except:
        TEST_ENV = 'OTHER'
        
        try:
            import psutil

            def freq():
                return psutil.cpu_freq().max
        except:
            def freq():
                return 'unknow'

def memory():
    try:
        r= gc.mem_free()+gc.mem_alloc()
    except:
        try:
            r = psutil.virtual_memory().total
        except:
            r = 'unkonw'
    return r

PLATFORM = sys.platform
VERSION = sys.version
FREQ = freq()
MEMORY = memory()

def run_test(func, *param):
    gc.collect()
    try:
        t1 = ticks_ms()
        if param == None:
            func()
        else:
            func(*param)
        t2 = ticks_ms()
        dt = ticks_diff(t2, t1)
        print('Calculation time:', dt, 'ms\n')
        return dt
    except:
        print('Error occurred during operation!')

def mandelbrot_test(p):
    iter = p[0]
    def in_set(c):
        z = 0
        for i in range(iter):
            z = z * z + c
            if abs(z) > 4:
                return False
        return True

    r = ''
    for v in range(31):
        for u in range(81):
            if in_set((u / 30 - 2) + (v / 15 - 1) * 1j):
                r += ' '
            else:
                r += '#'
        r += '\n'
    if len(p)>1 and p[1]:
        print(r)

def pi_test(p):
    iter = p[0]
    extra = 8
    one = 10 ** (iter+extra)
    t, c, n, na, d, da = 3*one, 3*one, 1, 0, 0, 24

    while t > 1: 
        n, na, d, da = n+na, na+8, d+da, da+32
        t = t * n // d
        c += t
    return c // (10 ** extra)


def add_test(p):
    for i in range(p[0]):
        C = p[1] + p[2]

def mul_test(p):
    for i in range(p[0]):
        C = p[1] * p[2]

def div_test(p):
    for i in range(p[0]):
        C = p[1] / p[2]

def pow_test(p):
    for i in range(p[0]):
        C = p[1] ** p[2]    

INT_ADD_TEST_LIST = ('Integer addition {} times', add_test, [12345678, 56781234], 10000, 100000, 1000000)
INT_MUL_TEST_LIST = ('Integer multiplication {} times', mul_test, [12345678, 56781234], 10000, 100000, 1000000)
INT_DIV_TEST_LIST = ('Integer division {} times', div_test, [99999991, 45481], 10000, 100000, 1000000)
FLOAT_ADD_TEST_LIST = ('Float addition {} times', add_test, [12345678.1234, 56781234.5678], 10000, 100000, 1000000)
FLOAT_MUL_TEST_LIST = ('Float multiplication {} times', mul_test, [12345678.1234, 56781234.5678], 10000, 100000, 1000000)
FLOAT_DIV_TEST_LIST = ('Float division {} times', div_test, [99999991.2345, 45481.1357], 10000, 100000, 1000000)
POWER_TEST_LIST = ('Power calculation {} times', pow_test, [1234.5678,2.3456], 10000, 100000, 1000000)
MAND_TEST_LIST = ('Mandelbrot iterating {} times', mandelbrot_test, [], 100, 500, 5000)
PI_TEST_LIST = ('Pi Calculation {} bits', pi_test, [], 1000, 5000, 10000, 100000, 200000)

TEST_LIST = (
    INT_ADD_TEST_LIST, INT_MUL_TEST_LIST, INT_DIV_TEST_LIST,
    FLOAT_ADD_TEST_LIST, FLOAT_MUL_TEST_LIST, FLOAT_DIV_TEST_LIST,
    POWER_TEST_LIST,
    MAND_TEST_LIST,
    PI_TEST_LIST
)

tr = []

def run():
    global tr

    for TEST in TEST_LIST:
        for item in TEST:
            if type(item) == int:
                print(TEST[0].format(item))
                p = TEST[2].copy()
                p.insert(0, item)
                r = run_test(TEST[1], p)
                tr.append([TEST[0].format(item), str(r)])

def print_result():
    print('|{:36}|{:12}|'.format('item','result'))
    print('|{:36}|{:12}|'.format('-','  :-:'))
    print('|{:36}|{:12}|'.format('Platform', PLATFORM))
    print('|{:36}|{:12}|'.format('Version', VERSION))
    print('|{:36}|{:12}|'.format('Frequency', FREQ))
    print('|{:36}|{:12}|'.format('Memory', MEMORY))

    for i in range(len(tr)):
        print('|{:36}|{:12}|'.format(tr[i][0], tr[i][1]))

###############################################################################

print('\n\n')
print('##############')
print('# Begin test #')
print('##############')

print('\nEnvironment:', TEST_ENV)
print('Platform:', PLATFORM)
print('Version:', VERSION)
print('Frequency:', FREQ)
print('Memory:', MEMORY)
print()

run()

print('\nTest finished.')
print('==============')

print_result()
