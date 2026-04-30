<?php

require 'binarySearch.php';

function test(string $description, int $result, int $expected): void
{
    $status = $result === $expected ? '✅' : '❌';
    echo "{$status} [{$description}] → got {$result}, expected {$expected}\n";
}

function runTests(): void
{
    $passed = 0;
    $failed = 0;

    $cases = [
        // [array, target, expected, description]

        // cas normaux
        [[1, 3, 5, 7, 9, 11], 7, 3, "target in middle"],
        [[1, 3, 5, 7, 9, 11], 1, 0, "target at start"],
        [[1, 3, 5, 7, 9, 11], 11, 5, "target at end"],
        [[1, 3, 5, 7, 9, 11], 5, 2, "target left of middle"],
        [[1, 3, 5, 7, 9, 11], 9, 4, "target right of middle"],

        // cible absente
        [[1, 3, 5, 7, 9, 11], 4, -1, "target not found (between values)"],
        [[1, 3, 5, 7, 9, 11], 0, -1, "target not found (below min)"],
        [[1, 3, 5, 7, 9, 11], 12, -1, "target not found (above max)"],

        // cas extrêmes
        [[42], 42, 0, "single element found"],
        [[42], 99, -1, "single element not found"],
        [[1, 2], 1, 0, "two elements target first"],
        [[1, 2], 2, 1, "two elements target second"],
        [[1, 2], 3, -1, "two elements not found"],

        // grands tableaux
        [range(1, 1000), 500, 499, "large array target found"],
        [range(1, 1000), 999, 998, "large array target near end"],
        [range(1, 1000), 1, 0, "large array target at start"],
        [range(1, 1000), 1001, -1, "large array target not found"],

        // négatifs
        [[-10, -5, 0, 5, 10], -10, 0, "negative target at start"],
        [[-10, -5, 0, 5, 10], 0, 2, "zero in array"],
        [[-10, -5, 0, 5, 10], -3, -1, "negative target not found"],
    ];

    foreach ($cases as [$array, $target, $expected, $description]) {
        $result = binarySearch($array, $target);
        $status = $result === $expected ? '✅' : '❌';

        if ($result === $expected) {
            $passed++;
        } else {
            $failed++;
        }

        echo "{$status} [{$description}] → got {$result}, expected {$expected}\n";
    }

    echo "\n{$passed}/".($passed + $failed)." tests passed\n";
}

runTests();
