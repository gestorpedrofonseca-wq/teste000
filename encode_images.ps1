$images = @(
    "assets/img/favicon.405cd09d.ico",
    "assets/img/white-logo.a195d627.png",
    "assets/img/sopa-solidaria1.90eb9325.jpg",
    "assets/img/zumba1.735b7a1b.jpg",
    "assets/img/sede-os-fenix.69d530f4.jpg",
    "assets/img/46yYWfa.jpg",
    "assets/img/BuN7Gym.jpg",
    "assets/img/ODN13IE.jpg",
    "assets/img/qtshKGQ.jpg",
    "assets/img/pix-qr.png",
    "assets/img/Charity.ec4e9031.jpg"
)

$imageMap = @{}

foreach ($img in $images) {
    if (Test-Path $img) {
        $bytes = [System.IO.File]::ReadAllBytes($img)
        $base64 = [System.Convert]::ToBase64String($bytes)
        $ext = [System.IO.Path]::GetExtension($img).TrimStart('.').ToLower()
        if ($ext -eq "ico") { $mime = "image/x-icon" }
        elseif ($ext -eq "jpg" -or $ext -eq "jpeg") { $mime = "image/jpeg" }
        elseif ($ext -eq "png") { $mime = "image/png" }
        elseif ($ext -eq "svg") { $mime = "image/svg+xml" }
        else { $mime = "image/$ext" }
        $imageMap[$img] = "data:$mime;base64,$base64"
    }
}

$imageMap | ConvertTo-Json | Out-File -FilePath "scratch\image_map.json" -Encoding utf8
