$basePath = "assets/img"
$filesToProcess = Get-ChildItem -Recurse -Include *.html, *.css
$images = Get-ChildItem -Path $basePath

$imageMap = @{}

Write-Host "Encoding images..."
foreach ($img in $images) {
    $imgPath = "$basePath/$($img.Name)"
    $bytes = [System.IO.File]::ReadAllBytes($img.FullName)
    $base64 = [System.Convert]::ToBase64String($bytes)
    $ext = $img.Extension.TrimStart('.').ToLower()
    
    if ($ext -eq "ico") { $mime = "image/x-icon" }
    elseif ($ext -eq "jpg" -or $ext -eq "jpeg") { $mime = "image/jpeg" }
    elseif ($ext -eq "png") { $mime = "image/png" }
    elseif ($ext -eq "svg") { $mime = "image/svg+xml" }
    else { $mime = "image/$ext" }
    
    $dataUri = "data:$mime;base64,$base64"
    $imageMap[$img.Name] = $dataUri
}

Write-Host "Replacing references in files..."
foreach ($file in $filesToProcess) {
    Write-Host "Processing $($file.FullName)..."
    $content = Get-Content -Raw -Path $file.FullName
    $modified = $false
    
    foreach ($imgName in $imageMap.Keys) {
        $dataUri = $imageMap[$imgName]
        
        # Define patterns to search for
        $patterns = @(
            "assets/img/$imgName",
            "../img/$imgName",
            "img/$imgName",
            # Sometimes just the filename is used if it's in the same dir or handled by a bundler
            # But we must be careful not to replace it if it's already a data URI or something else.
            # We'll stick to path-like patterns for safety first.
            "'$imgName'",
            "`"$imgName`""
        )
        
        foreach ($pattern in $patterns) {
            if ($content.Contains($pattern)) {
                # If it's a quoted filename, we need to keep the quotes or check carefully.
                # However, usually it's src="filename" or url('filename')
                if ($pattern -eq "'$imgName'") {
                    $content = $content.Replace($pattern, "'$dataUri'")
                }
                elseif ($pattern -eq "`"$imgName`"") {
                    $content = $content.Replace($pattern, "`"$dataUri`"")
                }
                else {
                    $content = $content.Replace($pattern, $dataUri)
                }
                $modified = $true
            }
        }
    }
    
    if ($modified) {
        $content | Out-File -FilePath $file.FullName -Encoding utf8 -NoNewline
        Write-Host "  Updated $($file.Name)"
    }
}

Write-Host "Finishing up..."
# Save the map for reference
$imageMap | ConvertTo-Json | Out-File -FilePath "scratch/full_auto_image_map.json" -Encoding utf8

Write-Host "Done! All images in assets/img have been converted to Base64 in HTML and CSS files."
