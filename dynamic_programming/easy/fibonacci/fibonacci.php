<?php

// Time: O(2^n) - Space: O(n)
function naiveFibonacci(int $n): int {
    if ($n < 2) {
        return $n;
    }

    return fibonacci($n - 1) + fibonacci($n - 2);
}

// Time: O(n) - Space: O(n)
function fibonacci(int $n, &$memo = []): int {
    if ($n < 2) {
        return $n;
    }

    if (isset($memo[$n])) {
        return $memo[$n];
    }

    $memo[$n] = fibonacci($n - 1, $memo) + fibonacci($n - 2, $memo);

    return $memo[$n];
}

// Time: O(n) - Space: O(1)
function fibonacciWithoutRecursion(int $n): int {
    if ($n < 2) {
        return $n;
    }

    $a = 0;
    $b = 1;

    for ($i = 2; $i <= $n; $i++) {
        [$a, $b] = [$b, $a + $b];
    }

    return $b;
}

echo fibonacciWithoutRecursion(50) . "\n";
