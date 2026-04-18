$json = Get-Content -Raw -Path "scratch\image_map.json" | ConvertFrom-Json
$imageMap = @{}
foreach ($prop in $json.PSObject.Properties) {
    $imageMap[$prop.Name] = $prop.Value
}

# Define files to process
$files = Get-ChildItem -Recurse -Include *.html, *.css

foreach ($file in $files) {
    Write-Host "Processing $($file.FullName)..."
    $content = Get-Content -Raw -Path $file.FullName
    
    foreach ($imgPath in $imageMap.Keys) {
        $base64 = $imageMap[$imgPath]
        
        # Replace normal path (e.g., assets/img/logo.png)
        $content = $content.Replace($imgPath, $base64)
        
        # Replace relative path for CSS (e.g., ../img/logo.png)
        $relativeImgPath = $imgPath.Replace("assets/img/", "../img/")
        $content = $content.Replace($relativeImgPath, $base64)
    }
    
    $content | Out-File -FilePath $file.FullName -Encoding utf8 -NoNewline
}

Write-Host "Done!"
