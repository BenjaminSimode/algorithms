<?php

// Return the index of the target if found, else return -1
function binarySearch(array $array, int $target): int {
    $start = 0;
    $end = count($array) - 1;

    while ($start <= $end) {
        $mid = floor(($start + $end) / 2);

        if ($array[$mid] > $target) {
            $end = $mid - 1;
        } elseif ($array[$mid] < $target) {
            $start = $mid + 1;
        } else {
            return $mid;
        }
    }

    return -1;
}
