param([string]$file)
$hivelocation = "C:\Program Files\Common Files\microsoft shared\Web Server Extensions\15\TEMPLATE\LAYOUTS\"

$separator = @("Layouts\")
$option = [System.StringSplitOptions]::RemoveEmptyEntries

if ($file.Contains("Layouts"))
{
	$dest = "$($hivelocation)$($file.Split($separator, $option)[-1])"
	Copy-Item $file $dest
	Echo "File uploaded to the hive."
} else {
	Echo "This script is only able to copy things to Layouts in hive."
}
