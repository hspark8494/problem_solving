fun sieve(n:Int): List<Int> {
    val sieve = Array<Boolean>(n) { it % 2 != 0 }
    val primes = mutableListOf<Int>()
    sieve[0] = false
    sieve[2] = true
    primes.add(2)
    for (i in 3 until sieve.size step 2) {
        if (sieve[i]) {
            primes.add(i)
            for (j in i until sieve.size step i) {
                sieve[j] = false
            }
        }
    }
    return primes
}