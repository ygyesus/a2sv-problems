# Problem: Closest Prime Numbers in Range - https://leetcode.com/problems/closest-prime-numbers-in-range/

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        isPrime = [True] * (right+1)

        if 0<len(isPrime): isPrime[0] = False
        if 1<len(isPrime): isPrime[1] = False

        for prime in range(right+1):
            if not isPrime[prime]: continue
            for multiple in range(prime*prime, right+1, prime): isPrime[multiple] = False


        primes = [prime for prime in range(left, right+1) if isPrime[prime]]

        leftAns = rightAns = -1
        for i in range(1, len(primes)):
            if leftAns == rightAns == -1:
                leftAns, rightAns = primes[i-1], primes[i]
            elif primes[i]-primes[i-1] < rightAns - leftAns:
                leftAns, rightAns = primes[i-1], primes[i]

        return [leftAns, rightAns]