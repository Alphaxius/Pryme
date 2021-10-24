


class Pryme:
    """ class prime provides functions related to primes while
        caching the primes that are found while processing
        good for small primes
        includes functions for factoring
    """
        
    def __init__ ( self, n : int = None):
        # https://oeis.org/A000040/list 20 Oct 2021
        self._prime_factors_cache = {}
        self._prime_cache = [2,3]
        if n == None:
            self._prime_cache = \
            [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59, \
            61,67,71,73,79,83,89,97,101,103,107,109,113,127, \
            131,137,139,149,151,157,163,167,173,179,181,191, \
            193,197,199,211,223,227,229,233,239,241,251,257, \
            263,269,271]
        elif n > 2: 
            self.n_primes ( n )

    def __str__ ( self ):
        return str ( self._prime_cache )

    def __repr__ ( self ):
        return str ( f"Pryme({len(self._prime_cache)})" )

    def is_prime ( self, p : int ) -> bool:
        """ is_prime returns bool
            Test if number is prime.
            parameter p : int is the test value
        """
        #NOTE: Modifies _prime_cache directly

        if p in self._prime_cache:
            return True
        elif p < self._prime_cache[-1]:
            return False
        else:
            candidate = self._prime_cache[-1] + 2
            while self._prime_cache[-1] <= p:
                pc_index = 0
                while pc_index < len ( self._prime_cache ) // 2:
                    if candidate % self._prime_cache[pc_index] == 0:
                        pc_index = 0
                        candidate = candidate + 2
                    else:
                        pc_index = pc_index + 1
                self._prime_cache.append ( candidate )
                candidate = candidate + 2
                    

    def n_primes ( self, n : int ) -> list[int]:
        """ n_primes returns list[int] of primes
            returned list starts at the first prime (2)
            parameter n : int is the number of primes in the list
        """
        if n < 0:
            return []
        elif len ( self._prime_cache ) == n:
            return list ( self._prime_cache )
        elif len ( self._prime_cache ) > n:
            return list ( self._prime_cache[:n] )
        else:
            candidate = self._prime_cache[-1] + 2
            while len ( self._prime_cache ) < n:
                self.is_prime ( candidate )
                if self._prime_cache[-1] > candidate + 2:
                    candidate = self._prime_cache[-1] + 2
                else:
                    candidate = candidate + 2
            return list ( self._prime_cache )
                
    def primes_less_than ( self, n : int ) -> list[int]:
        """ primes_less_than returns list[int] of primes less than or equal to some maximum value
            returned list starts at the first prime (2)
            parameter n : int is the maximum value
        """
        if n < 2:
            return []
        elif n == self._prime_cache[-1]:
            return list ( self._prime_cache )
        elif n < self._prime_cache[-1]:
            pc_index_left = 0 # increments
            pc_index_right = len ( self._prime_cache ) - 1 # decrements
            while pc_index_right-pc_index_left > 1:
                midpoint = ( pc_index_left + pc_index_right ) // 2
                if n >= self._prime_cache[midpoint]:
                    pc_index_left = midpoint
                else:
                    pc_index_right = midpoint
            return list ( self._prime_cache[:pc_index_right] )
        else:
            self.is_prime ( n )
            return self.primes_less_than ( n )

    def ith_prime ( self, i : int ) -> int:
        """ ith_prime returns int which is the prime at an index, 0 -> 2
            parameter i : int is the index
        """
        if i < 0:
            return -1
        elif i < len ( self._prime_cache ):
            return self._prime_cache[i]
        else:
            return n_primes ( i )[i]

    def prime_less_than ( self, n : int ) -> int:
        """ prime_less_than returns int, the greatest prime less than or equal to n
            parameter n : int is the value to check against
        """
        if n < 2:
            return -1
        elif n == self._prime_cache[-1]:
            return self._prime_cache[-1]
        elif n < self._prime_cache[-1]:
            pc_index_left = 0 # increments
            pc_index_right = len ( self._prime_cache ) - 1 # decrements
            while pc_index_right-pc_index_left > 1:
                midpoint = ( pc_index_left + pc_index_right ) // 2
                if n >= self._prime_cache[midpoint]:
                    pc_index_left = midpoint
                else:
                    pc_index_right = midpoint
            return self._prime_cache[pc_index_left]
        else:
            self.is_prime ( n )
            return self.prime_less_than ( n )

    def prime_greater_than ( self, n : int ) -> int:
        """ prime_greater_than returns int, the least prime greater than or equal to n
            parameter n : int is the value to check against
        """
        if n < 2:
            return 2
        elif n == self._prime_cache[-1]:
            return self._prime_cache[-1]
        elif n < self._prime_cache[-1]:
            pc_index_left = 0 # increments
            pc_index_right = len ( self._prime_cache ) - 1 # decrements
            while pc_index_right-pc_index_left > 1:
                midpoint = ( pc_index_left + pc_index_right ) // 2
                if n > self._prime_cache[midpoint]:
                    pc_index_left = midpoint
                else:
                    pc_index_right = midpoint
            return self._prime_cache[pc_index_right]
        else:
            self.is_prime ( n )
            return self.prime_greater_than ( n )

    def index_of ( self, p : int ) -> int:
        """ index_of returns int which is the index of a given prime
            inputs which are not primes returns -1
            parameter p : int is the prime to check
        """
        if p in self._prime_cache: # might be slow
            return self._prime_cache.index ( p )
        elif p < self._prime_cache[-1]:
            return -1
        else:
            if self.is_prime ( p ):
                return len ( self._prime_cache ) - 1
            else:
                return -1

    def primes_between ( self, a : int, b : int ) -> list[int]:
        """ primes_between returns list[int] of primes between (inclusive) the inputs
            parameter a : int is one side of the range
            parameter b : int is the other side of the range
        """
        if a > b:
            temp = a
            a = b
            b = temp
        if a == b:
            if is_prime ( a ):
                return [a]
            else:
                return []
        if b > self._prime_cache[-1]:
            self.is_prime ( b )

        # one greater than a ( or equal to )
        pc_index_left_a = 0 # increments
        pc_index_right_a = len ( self._prime_cache ) - 1 # decrements
        if a == 2:
            pc_index_right_a = 0
        else:
            while pc_index_right_a-pc_index_left_a > 1:
                midpoint = ( pc_index_left_a + pc_index_right_a ) // 2
                if a > self._prime_cache[midpoint]:
                    pc_index_left_a = midpoint
                else:
                    pc_index_right_a = midpoint

        # one less than b ( or equal to )                
        pc_index_left_b = pc_index_right_a # increments
        pc_index_right_b = len ( self._prime_cache ) - 1 # decrements
        while pc_index_right_b-pc_index_left_b > 1:
            midpoint = ( pc_index_left_b + pc_index_right_b ) // 2
            if b >= self._prime_cache[midpoint]:
                pc_index_left_b = midpoint
            else:
                pc_index_right_b = midpoint

        return self._prime_cache[pc_index_right_a:pc_index_right_b]

    def prime_factors ( self, x : int ) -> list[int]:
        """ prime_factors returns list[int] which is the list of prime factors
            including multiplicity
            parameter x : int is the number to try
        """
        #NOTE: modifies _prime_factors_cache directly
        if x < 2:
            return [x]
        elif x in self._prime_factors_cache:
            return list(self._prime_factors_cache[x])
        elif x // 2 > self._prime_cache[-1]:
            self.is_prime ( x // 2 )
        factors = self._prime_factors_internal ( x, 0 )
        self._prime_factors_cache[x] = factors
        return factors

    def _prime_factors_internal ( self, x : int, i : int ) -> list[int]:
        """ _prime_factors_internal returns list[int] which is the list of prime
            factors of x including multiplicity
            parameter x : int is the number to try
            parameter i : int is the first prime to try
        """
        if x in self._prime_factors_cache:
            return list(self._prime_factors_cache[x])
        elif self._prime_cache[i] > x // 2:
            return [x]
        elif x % self._prime_cache[i] == 0:
            # can't compress this line, not sure why - 24 Oct 2021
            factors = self._prime_factors_internal ( x // self._prime_cache[i], i )
            factors.append( self._prime_cache[i] )
            return factors
        else:
            return self._prime_factors_internal ( x, i + 1 )
            
    def min_prime_factor ( self, x : int ) -> int:
        """ min_prime_factor returns int which is the least prime factor of the parameter
            parameter x : int is the number to try
        """
        if x in self._prime_factors_cache:
            return self._prime_factors_cache[x][-1]
        else:
            return self.prime_factors ( x )[-1]

    def max_prime_factor ( self, x : int ) -> int:
        """ max_prime_factor returns int which is the greatest prime factor of the parameter
            parameter x : int is the number to try
        """
        if x in self._prime_factors_cache:
            return self._prime_factors_cache[x][0]
        else:
            return self.prime_factors ( x )[0]

    def radical ( self, x : int ) -> int:
        """ radical returns int which is the product of prime factors with multiplicity removed
            parameter x : int is the number to try
        """
        factors = []
        min_factors = []
        product = 1
        if x in self._prime_factors_cache:
            factors = list(self._prime_factors_cache[x])
        else:
            factors = self.prime_factors ( x )
        for pf in factors:
            if pf not in min_factors:
                min_factors.append(pf)
        for mf in min_factors:
            product *= mf
        return product

    def coprime ( self, x : int, y : int ) -> bool:
        """ coprime returns bool, True if x and y do not share factors
            parameter x : int is the first number to try
            parameter y : int is the second number to try
        """
        if x == y:
            return False
        else:
            x_factors = self.prime_factors ( x )
            y_factors = self.prime_factors ( y )
            for xf in x_factors:
                if xf in y_factors:
                    return False
            return True

    def clear_cache ( self ) -> None:
        """ clear cache resets the cache of prime numbers to the minimal list [2, 3] """
        self._prime_cache = [2,3]

    def clear_factor_cache ( self ) -> None:
        """ clear_factor_cache deletes the entire cache of prime factors """
        self._prime_factors_cache = {}


_default_pryme_instance = Pryme()
is_prime = _default_pryme_instance.is_prime
n_primes = _default_pryme_instance.n_primes
primes_less_than = _default_pryme_instance.primes_less_than
ith_prime = _default_pryme_instance.ith_prime
prime_less_than = _default_pryme_instance.prime_less_than
prime_greater_than = _default_pryme_instance.prime_greater_than
index_of = _default_pryme_instance.index_of
primes_between = _default_pryme_instance.primes_between
prime_factors = _default_pryme_instance.prime_factors
min_prime_factor = _default_pryme_instance.min_prime_factor
max_prime_factor = _default_pryme_instance.max_prime_factor
radical = _default_pryme_instance.radical
coprime = _default_pryme_instance.coprime
clear_prime_cache = _default_pryme_instance.clear_cache
clear_factor_cache= _default_pryme_instance.clear_factor_cache











