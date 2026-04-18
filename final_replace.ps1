$json = Get-Content -Raw -Path "scratch\full_image_map.json" | ConvertFrom-Json
$imageMap = @{}
foreach ($prop in $json.PSObject.Properties) {
    $imageMap[$prop.Name] = $prop.Value
}

# Define files to process
$files = Get-ChildItem -Recurse -Include *.html, *.css

foreach ($file in $files) {
    Write-Host "Processing $($file.FullName)..."
    $content = Get-Content -Raw -Path $file.FullName
    $modified = $false
    
    foreach ($imgName in $imageMap.Keys) {
        $base64 = $imageMap[$imgName]
        
        # Search patterns
        $patterns = @(
            "assets/img/$imgName",
            "../img/$imgName",
            "img/$imgName",
            "$imgName" # Dangerous? Maybe, but usually image names are unique enough.
        )
        
        foreach ($pattern in $patterns) {
            # Avoid replacing the filename if it's already inside a data URI
            if ($content.Contains($pattern) -and -not $content.Contains("data:") -and -not $content.Contains(";base64,")) {
               # This check is too simple. Let's just replace the path versions.
            }
        }
        
        # Safer: replace with paths
        if ($content.Contains("assets/img/$imgName")) {
            $content = $content.Replace("assets/img/$imgName", $base64)
            $modified = $true
        }
        if ($content.Contains("../img/$imgName")) {
            $content = $content.Replace("../img/$imgName", $base64)
            $modified = $true
        }
        # Sometimes images are just "img/..." or just the name
        if ($content.Contains("url($imgName)")) {
             $content = $content.Replace("url($imgName)", "url($base64)")
             $modified = $true
        }
    }
    
    if ($modified) {
        $content | Out-File -FilePath $file.FullName -Encoding utf8 -NoNewline
        Write-Host "  Updated."
    }
}

Write-Host "Done!"
