<?php

function isAnagram($first, $second): bool {
    if (strlen($first) !== strlen($second)) {
        return false;
    }

    $first = $first |> strtolower(...) |> str_split(...);
    $second = $second |> strtolower(...) |> str_split(...);

    $hashmap = [];

    foreach ($first as $letter) {
        if (isset($hashmap[$letter])) {
            ++$hashmap[$letter];
        } else {
            $hashmap[$letter] = 1;
        }
    }

    foreach ($second as $letter) {
        if (isset($hashmap[$letter])) {
            --$hashmap[$letter];
        } else {
            $hashmap[$letter] = -1;
        }
    }

    return array_all($hashmap, fn ($count) => $count === 0);
}

echo isAnagram('rat', 'cat');
