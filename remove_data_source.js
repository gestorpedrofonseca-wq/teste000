const fs = require('fs');

fs.readdirSync('.').filter(f => f.endsWith('.html')).forEach(f => {
    let c = fs.readFileSync(f, 'utf8');
    
    // Remove data-source attributes which might be confusing the user or build tools
    c = c.replace(/ data-source="assets\/[^"]+"/g, '');
    
    fs.writeFileSync(f, c);
    console.log('Removed data-source attribute from ' + f);
});
