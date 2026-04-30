<?php

require_once 'isAnagram.php';

function test_isAnagram(): void
{
    $cases = [
        // [$s, $t, $expected, $description]
        ["anagram", "nagaram", true, "classic anagram"],
        ["rat", "car", false, "3-letter anagram"],
        ["listen", "silent", true, "6-letter anagram"],
        ["hello", "world", false, "no common letters"],
        ["cat", "rat", false, "one letter differs"],
        ["ab", "a", false, "different lengths"],
        ["a", "a", true, "single identical letter"],
        ["a", "b", false, "single different letter"],
        ["", "", true, "both empty"],
        ["aabbcc", "abcabc", true, "repeated letters"],
        ["aab", "bba", false, "same letters different counts"],
        ["Astronomer", "Moon starer", false, "case sensitive with space"],
    ];

    $passed = 0;
    $failed = 0;

    foreach ($cases as [$s, $t, $expected, $description]) {
        $result = isAnagram($s, $t);
        $status = $result === $expected ? "✅" : "❌";

        if ($result === $expected) {
            $passed++;
        } else {
            $failed++;
        }

        $resultStr = $result ? 'true' : 'false';
        $expectedStr = $expected ? 'true' : 'false';

        echo "$status [$description] isAnagram('$s', '$t') → got $resultStr, expected $expectedStr\n";
    }

    echo "\n$passed/".($passed + $failed)." tests passed\n";
}

test_isAnagram();
