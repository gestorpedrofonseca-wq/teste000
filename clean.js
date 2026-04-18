const fs = require('fs');

fs.readdirSync('.').filter(f => f.endsWith('.html')).forEach(f => {
    let c = fs.readFileSync(f, 'utf8');
    
    // Remove source map comments
    c = c.replace(/\/\*# sourceMappingURL=.*?\*\//g, '');
    c = c.replace(/\/\/# sourceMappingURL=.*/g, '');
    
    // Fix carousel path logic
    // Target: var a=location.pathname.split("/").pop();"index.html"===a&&
    c = c.replace(/var [a-z]=location\.pathname\.split\("\/"\)\.pop\(\);\s*("index\.html"===[a-z]&&|index === "index\.html" &&)/g, (match) => {
        return 'var filename=location.pathname.split("/").pop(); if(filename === "index.html" || filename === "") ';
    });

    // Also handle transparency.48707058.js style regex if different
    c = c.replace(/var [a-z]=location\.pathname\.split\("\/"\)\.pop\(\);console\.log\("filename:",[a-z]\),"index\.html"===[a-z]&&/g, 'var filename=location.pathname.split("/").pop(); if(filename === "index.html" || filename === "") ');

    fs.writeFileSync(f, c);
    console.log('Cleaned ' + f);
});
