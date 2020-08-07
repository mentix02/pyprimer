import unittest

from pyprimer import *


class PrimeNumberGenerationTest(unittest.TestCase):

    """  """

    def setUp(self):
        self.primes = [2, 3, 5, 7, 11]

    def test_is_prime(self):
        for prime in self.primes:
            self.assertTrue(is_prime(prime))
        for prime in self.primes:
            self.assertFalse(is_prime(prime * 2))

    def test_primes_till(self):
        self.assertEqual(primes_till(11), self.primes)

    def test_n_primes(self):
        self.assertEqual(n_primes(len(self.primes)), self.primes)

    def test_n_prime(self):
        for idx, prime in enumerate(self.primes):
            self.assertEqual(n_prime(idx + 1), prime)

    def test_prime_generator(self):
        count = 0
        generator = prime_generator()
        n: int = next(generator)
        while n < 12:
            self.assertEqual(n, self.primes[count])
            n = next(generator)
            count += 1


if __name__ == '__main__':
    unittest.main()
