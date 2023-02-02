var summaryRanges = function(nums) {
    const range = [];
    
    for(let n of nums) {
        if(!range.length || n-1 > range[range.length-1][1]) {
            range.push([n, n]);
        } else  range[range.length-1][1]++;
    }
    return range.map(([x, y]) => x == y ? x + '' : x + '->' + y);
};