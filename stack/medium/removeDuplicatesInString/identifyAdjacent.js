function identifyAdjacent(s, k) {
    const stack = [];

    for (const char of s) {
        if (stack.length > 0 && stack[stack.length - 1][0] === char) {
            stack[stack.length - 1][1] += 1;
        } else {   
            stack.push([char, 1]);
        }
        
        if (stack[stack.length - 1][1] === k) {
            stack.pop();
        }
    }

    return stack.map(([char, count]) => char.repeat(count)).join('');
}

console.log(identifyAdjacent("deeedbbcccbdaa", 3));
