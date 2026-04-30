<?php

function isPalindrome(string $string): bool
{
    $string = strtolower($string);

    $reversedString = strrev($string);

    return $reversedString === $string;
}

//echo 'kayak: ' . isPalindrome("kayak") . "\n"; // → true
//echo 'Radar: ' . isPalindrome("Radar") . "\n"; // → true
//echo 'bonjour: ' . isPalindrome("bonjour") . "\n"; // → false
