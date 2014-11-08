def karatsuba(num1, num2):
    if num1 < 10 or num2 < 10:
        return num1 * num2

    num1 = str(num1)
    num2 = str(num2)

    if len(num1) < len(num2):
        num1 = num1.zfill(len(num2))
    elif len(num1) > len(num2):
        num2 = num2.zfill(len(num1))

    m1 = (len(num1) + 1) / 2
    m2 = len(num1) / 2

    x0, x1 = int(str(num1)[:m1]), int(str(num1)[m1:])
    y0, y1 = int(str(num2)[:m1]), int(str(num2)[m1:])

    z0 = karatsuba(x1, y1)
    z1 = karatsuba((x1 + x0), (y1 + y0))
    z2 = karatsuba(x0, y0)

    return (z2 * 10 ** (2 * m2)) + ((z1 - z2 - z0) * 10 ** (m2)) + z0


def test_karatsuba():
    assert karatsuba(2, 3) == 6
    assert karatsuba(11, 4) == 44
    assert karatsuba(1234, 567) == 699678
    assert karatsuba(1234, 5678) == 7006652
    assert karatsuba(123, 56789) == 6985047

if __name__ == "__main__":

    test_karatsuba()
