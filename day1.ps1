$sumTarget = 2020
$content = gci .\day1.txt -recurse | %{[int]$_}
$content| % { $x = $_ ;  $content | ? { $_ -ne $x } | ?{($_ + $x) -eq $sumTarget} | %{write-host $_ '*' $x ',' ($_*$x) } }
