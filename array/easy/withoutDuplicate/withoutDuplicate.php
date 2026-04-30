<?php

function withoutDuplicate(array $nombres): array {
    $result = [];

    foreach ($nombres as $nombre) {
        if (!isset($result[$nombre])) {
            $result[$nombre] = true;
        }
    }

    return array_keys($result);
}

print_r(withoutDuplicate([1, 2, 2, 3, 1, 4])); // → [1, 2, 3, 4]
