import time

def riemann_integration(f, a, b, n):
    """
    Menghitung integral fungsi f menggunakan metode Riemann.

    Args:
    f: fungsi yang ingin diintegralkan
    a: batas bawah interval
    b: batas atas interval
    n: jumlah subinterval

    Returns:
    Integral numerik dari fungsi f di antara a dan b.
    """
    h = (b - a) / n
    integral = 0
    for i in range(n):
        integral += f(a + i * h)
    integral *= h
    return integral

def trapezoidal_integration(f, a, b, n):
    """
    Menghitung integral fungsi f menggunakan metode trapesium.

    Args:
    f: fungsi yang ingin diintegralkan
    a: batas bawah interval
    b: batas atas interval
    n: jumlah trapesium

    Returns:
    Integral numerik dari fungsi f di antara a dan b.
    """
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral

def simpson_integration(f, a, b, n):
    """
    Menghitung integral fungsi f menggunakan metode Simpson 1/3.

    Args:
    f: fungsi yang ingin diintegralkan
    a: batas bawah interval
    b: batas atas interval
    n: jumlah subinterval (harus genap)

    Returns:
    Integral numerik dari fungsi f di antara a dan b.
    """
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    integral = f(a) + f(b)
    for i in range(1, n, 2):
        integral += 4 * f(x[i])
    for i in range(2, n-1, 2):
        integral += 2 * f(x[i])
    integral *= h / 3
    return integral

# Fungsi f(x)
def f(x):
    return 4 / (1 + x**2)

# Nilai referensi pi
pi_ref = 3.14159265358979323846

# Variasi nilai N
Ns = [10, 100, 1000, 10000]

# Menentukan metode berdasarkan dua digit terakhir NIM
nim_last_two_digits = 7
method_index = nim_last_two_digits % 3

# Pilih metode sesuai dengan hasil perhitungan
methods = {
    0: riemann_integration,
    1: trapezoidal_integration,
    2: simpson_integration
}
integration_method = methods[method_index]

# Pengujian
for N in Ns:
    start_time = time.time()
    result = integration_method(f, 0, 1, N)
    end_time = time.time()
    execution_time = end_time - start_time
    error = abs(result - pi_ref)
    print(f"Metode {method_index + 1}, N = {N}: Integral = {result}, Error = {error}, Execution Time = {execution_time} seconds")
