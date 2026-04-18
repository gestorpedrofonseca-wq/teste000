const fs = require('fs');

const cp1252_to_byte = {
  "\u20AC": 0x80, // €
  "\u201A": 0x82, // ‚
  "\u0192": 0x83, // ƒ
  "\u201E": 0x84, // „
  "\u2026": 0x85, // …
  "\u2020": 0x86, // †
  "\u2021": 0x87, // ‡
  "\u02C6": 0x88, // ˆ
  "\u2030": 0x89, // ‰
  "\u0160": 0x8A, // Š
  "\u2039": 0x8B, // ‹
  "\u0152": 0x8C, // Œ
  "\u017D": 0x8E, // Ž
  "\u2018": 0x91, // ‘
  "\u2019": 0x92, // ’
  "\u201C": 0x93, // “
  "\u201D": 0x94, // ”
  "\u2022": 0x95, // •
  "\u2013": 0x96, // –
  "\u2014": 0x97, // —
  "\u02DC": 0x98, // ˜
  "\u2122": 0x99, // ™
  "\u0161": 0x9A, // š
  "\u203A": 0x9B, // ›
  "\u0153": 0x9C, // œ
  "\u017E": 0x9E, // ž
  "\u0178": 0x9F  // Ÿ
};

function fixMojibake(filename) {
    try {
        let text = fs.readFileSync(filename, 'utf-8');
        
        // Simple heuristic to check if the file is mojibake currently
        if (text.includes('Ã§') || text.includes('Ã£') || text.includes('Ã¡') || text.includes('Ãª') || text.includes('Ã­')) {
            console.log("Fixing Mojibake in " + filename);
            
            let bytes = new Uint8Array(text.length);
            for (let i = 0; i < text.length; i++) {
                let char = text.charAt(i);
                if (cp1252_to_byte[char]) {
                    bytes[i] = cp1252_to_byte[char];
                } else {
                    bytes[i] = text.charCodeAt(i) & 0xFF;
                }
            }
            
            let correctText = Buffer.from(bytes).toString('utf8');
            fs.writeFileSync(filename, correctText, 'utf-8');
            console.log("Successfully fixed " + filename);
        }
    } catch(e) {
        console.error("Error in " + filename + ":", e);
    }
}

fs.readdirSync('.').forEach(f => {
    if (f.endsWith('.html')) {
        fixMojibake(f);
    }
});
